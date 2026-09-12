"""Preserve import coordinates and relocate historical decision outputs, not approvals."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


receipt = HERE / 'path-relocations.json'
assert not receipt.exists(), 'Already finalized; use verify.py.'
archive = read(HERE / 'archive-manifest.json')
mapping = {row['original_relative_path']: row['archived_relative_path'] for row in archive['entries']}
working = read(HERE / 'working-files.json')
assert not (HERE / 'working-files-v001.json').exists()
(HERE / 'working-files-v001.json').write_bytes((HERE / 'working-files.json').read_bytes())
changes = []


def preserve(rel):
    path = ROOT / rel
    dest = ROOT / '.manga-studio/history/structure-cleanup-v001/compatibility-before' / rel
    assert not dest.exists()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(path.read_bytes())
    record = {'original_relative_path': rel, 'archived_relative_path': dest.relative_to(ROOT).as_posix(), 'sha256': sha(dest)}
    changes.append(record)
    return path


# Inventory is an as-imported classification ledger, not a rescan of archived files.
inventory_rel = '.manga-studio/source/inventory.json'
inventory = preserve(inventory_rel)
inventory.write_bytes((ROOT / mapping[inventory_rel]).read_bytes())
for name in ['apply-chapter-001-v001.json', 'workspace-structure-v001.json']:
    path = preserve('.manga-studio/decisions/' + name)
    decision = read(path)
    before = decision.copy()
    decision['result_artifacts'] = [mapping.get(rel, rel) for rel in decision['result_artifacts']]
    assert all((ROOT / rel).is_file() for rel in decision['result_artifacts'])
    assert {k: v for k, v in decision.items() if k != 'result_artifacts'} == {k: v for k, v in before.items() if k != 'result_artifacts'}
    write(path, decision)
agents = preserve('AGENTS.md')
agents.write_text(agents.read_text().replace(
    'Current source records point to archived original bytes. Immutable maps and historical evidence retain their as-imported paths.',
    'Provenance, document storage records and the ID map point to archived original bytes. The classification inventory, immutable maps and historical evidence retain their as-imported paths.'))
changes_by_path = {row['original_relative_path']: row for row in changes}
rows = {row['relative_path']: row for row in working['artifacts']}
for rel in changes_by_path:
    if rel not in rows:
        rows[rel] = {'relative_path': rel, 'evidence': []}
    rows[rel]['sha256'] = sha(ROOT / rel)
working['artifacts'] = [rows[rel] for rel in sorted(rows)]
working['inventory_semantics'] = 'As-imported classification paths; current storage is provenance.original_path. All historical lookups require path plus expected hash.'
working['path_relocation_receipt'] = receipt.relative_to(ROOT).as_posix()
write(receipt, {'record_type': 'storage_path_compatibility', 'project_id': working['project_id'],
                'reason': 'Runtime inventory forbids managed-workspace intake; keep original import coordinates. Existing decision outputs now address the archived result bytes. Decision IDs, meaning, actors, timestamps and evidence remain unchanged. No approval record or target was edited.',
                'entries': changes})
write(HERE / 'working-files.json', working)
print(json.dumps({'storage_records_corrected': len(changes), 'approval_records_changed': 0}, indent=2))
