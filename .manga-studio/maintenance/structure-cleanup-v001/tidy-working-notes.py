"""Remove repeated working notes and obsolete status wording; preserve prior copies."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
assert not (HERE / 'working-note-relocations.json').exists()
registry_path = HERE / 'working-files.json'
registry = json.loads(registry_path.read_text())
(HERE / 'working-files-v002.json').write_bytes(registry_path.read_bytes())
entries = []
for row in registry['artifacts']:
    rel = row['relative_path']
    if not rel.startswith('manga/'):
        continue
    path = ROOT / rel
    old = path.read_text()
    new = old.replace('Remains in his era; exact addition requires prose approval', 'Remains in his era; included in the inactive draft, not adopted canon')
    new = new.replace('The next prose deliverable is a new version of the one supplied Chapter 1, not a reconstruction of unavailable chapters.', 'The one supplied Chapter 1 now has an inactive reconstructed draft; unavailable chapters have not been reconstructed.')
    if rel.startswith('manga/02-references/characters/') and path.name == 'canon.md':
        start = new.index('The archive prelude changes Daniel')
        end = new.index('\n\n[Character reference]', start)
        new = new[:start] + '[Shared relationship and identity continuity](../../../00-series/character-relationships.md)' + new[end:]
    if new != old:
        dest = ROOT / '.manga-studio/history/structure-cleanup-v001/working-notes-before' / rel
        assert not dest.exists()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(path.read_bytes())
        entries.append({'original_relative_path': rel, 'archived_relative_path': dest.relative_to(ROOT).as_posix(), 'sha256': hashlib.sha256(dest.read_bytes()).hexdigest()})
        path.write_text(new)
        row['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
(HERE / 'working-note-relocations.json').write_text(json.dumps({'project_id': registry['project_id'], 'reason': 'Working-note deduplication and accurate existing draft status only. No source or manuscript text changed.', 'entries': entries}, indent=2) + '\n')
registry_path.write_text(json.dumps(registry, indent=2) + '\n')
print(json.dumps({'working_notes_tidied': len(entries)}))
