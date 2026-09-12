"""Verify current layout plus the complete, hash-addressed pre-migration state."""
import argparse
import difflib
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WORK = ROOT / '.manga-studio'
PID = 'ms-70391ae1065048cf8bdd564959abd6c3'


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe(rel):
    assert isinstance(rel, str) and not Path(rel).is_absolute() and '..' not in Path(rel).parts, rel
    path = ROOT / rel
    assert path.resolve().is_relative_to(ROOT), rel
    return path


def file_set(directory):
    return {p.relative_to(ROOT).as_posix() for p in directory.rglob('*') if p.is_file() and not p.name.startswith('._')}


parser = argparse.ArgumentParser()
parser.add_argument('--record', action='store_true')
parser.add_argument('--record-path', help='Write a new validation record to this project-relative path')
parser.add_argument('--compare', type=Path, help='Read-only path to the structural reference project')
args = parser.parse_args()
archive = read(HERE / 'archive-manifest.json')
current = read(HERE / 'working-files.json')
assert archive['project_id'] == current['project_id'] == PID
entries = list(archive['entries'])
for filename in ['path-relocations.json', 'working-note-relocations.json']:
    entries += read(HERE / filename)['entries']
for relative in [
    'maintenance/manuscript-adoption-v001/relocations.json',
    'maintenance/visual-quality-direction-v002/relocations.json',
    'maintenance/character-reference-intake-v001/relocations.json',
]:
    relocation_record = WORK / relative
    if relocation_record.is_file():
        entries += read(relocation_record)['entries']
for row in entries:
    assert sha(safe(row['archived_relative_path'])) == row['sha256'], row


def resolve(rel, expected=None):
    path = safe(rel)
    if path.is_file() and (expected is None or sha(path) == expected):
        return path
    matches = [row for row in entries if row['original_relative_path'] == rel and (expected is None or row['sha256'] == expected)]
    assert expected is not None or len(matches) == 1, f'Ambiguous historical path: {rel}'
    assert matches, f'Missing historical artifact: {rel}'
    path = safe(matches[0]['archived_relative_path'])
    assert expected is None or sha(path) == expected
    return path


for row in archive['before_hashes']:
    assert sha(resolve(row['relative_path'], row['sha256'])) == row['sha256']
for row in current['artifacts']:
    assert sha(safe(row['relative_path'])) == row['sha256'], row['relative_path']
    for evidence in row['evidence']:
        assert sha(safe(evidence['relative_path'])) == evidence['sha256']
history_counts = {}
for relative, key in [
    ('.manga-studio/analysis/validation-v001.json', 'artifact_hashes'),
    ('.manga-studio/revisions/phase-3-v001/package-manifest-v001.json', 'artifacts'),
    ('.manga-studio/revisions/phase-4-proposal-v001/package-manifest-v001.json', 'artifacts'),
    ('.manga-studio/analysis/workspace-refactor-v001-validation.json', 'artifact_hashes'),
]:
    rows = read(safe(relative))[key]
    for row in rows:
        assert sha(resolve(row['relative_path'], row['sha256'])) == row['sha256']
    history_counts[relative] = len(rows)

runtime = Path.home() / '.agents/skills/.manga-studio-runtime'
installed = runtime / read(runtime / 'current.json')['version_path']
sys.path.insert(0, str(installed / 'scripts/lib'))
from manga_studio.approvals import validate_approval, validate_locks
from manga_studio.json_schema import validate_json_file
from manga_studio.profiles import validate_profile
from manga_studio.project import WORKSPACE_DIRECTORIES, discover_project, provenance_errors
from manga_studio.structure import validate_source_maps
context = discover_project(ROOT)
errors = provenance_errors(context) + validate_source_maps(context) + validate_locks(context) + validate_profile(context, 'story')
schema_files = [('project.json', 'project'), ('source/inventory.json', 'source-inventory'), ('source/provenance.json', 'provenance'), ('source/id-map.json', 'stable-id-map')]
for filename, schema in schema_files:
    errors += validate_json_file(WORK / filename, installed / f'schemas/{schema}.schema.json')
for path in (WORK / 'source/documents').glob('doc-*.json'):
    errors += validate_json_file(path, installed / 'schemas/source-document.schema.json')
approvals = [p for p in (WORK / 'approvals').glob('approval-*.json')]
assert len(approvals) == 7
for path in approvals:
    errors += validate_approval(context, path)
manuscript_approval_path = WORK / 'approvals/approval-feb5212823b84aeaaa04bac3fedc4fc6.json'
manuscript_approval = read(manuscript_approval_path)
assert manuscript_approval['status'] == manuscript_approval['decision'] == 'approved'
assert manuscript_approval['target_relative_path'] == '.manga-studio/manuscript/versions/chapter-001-v001.md'
assert manuscript_approval['target_version'] == 'v001'
assert manuscript_approval['target_sha256'] == 'f195b7e0afc7f875731ade728a1bbf7a28d7becf3f38fa2d920498231f65d500'
reference_approval_expectations = {
    'approval-68dbddb1b25b43df8ecd0db11b1d86ee.json': ('manga/02-references/approved-webp/daniel-tomas-shared.webp', '985cb554a78cca3367845b7cea089fee230f950629ae2da67d6c2fe90fd45ceb'),
    'approval-f06708bac3194fed87dd9f57e10bc2ca.json': ('manga/02-references/approve-png/daniel-tomas-shared.png', '48f2680a489156033f49b11f5a7c02a7a0e92e0442a3a60fc2bc1487cd1bf2b6'),
}
for filename, (target, target_hash) in reference_approval_expectations.items():
    approval = read(WORK / f'approvals/{filename}')
    assert approval['status'] == approval['decision'] == 'approved'
    assert approval['artifact_type'] == 'continuity'
    assert approval['target_relative_path'] == target
    assert approval['target_sha256'] == target_hash
for path in (WORK / 'decisions').glob('*.json'):
    if not path.name.startswith('._'):
        errors += validate_json_file(path, installed / 'schemas/decision-log.schema.json')
assert not errors, errors

baseline = read(WORK / 'source/inventory-baseline-v001.json')
inventory = read(WORK / 'source/inventory.json')
old_inventory_path = next(row['archived_relative_path'] for row in entries if row['original_relative_path'] == '.manga-studio/source/inventory.json')
assert inventory == read(safe(old_inventory_path))
for row in baseline['files']:
    assert sha(resolve(row['relative_path'], row['sha256'])) == row['sha256']
prov = read(WORK / 'source/provenance.json')['records']
assert len(prov) == 24 and all(row['source_status'] == 'active' for row in prov)
by_id = {row['document_id']: row for row in inventory['files']}
source_ids = {row['id']: row for row in read(WORK / 'source/id-map.json')['namespaces']['source_documents']}
units = {}
for row in prov:
    old = by_id[row['document_id']]
    assert safe(row['original_path']) == resolve(old['relative_path'], row['original_sha256'])
    assert sha(safe(row['original_path'])) == sha(safe(row['snapshot_path'])) == row['original_sha256']
    assert source_ids[row['document_id']]['path'] == row['original_path']
    doc = read(WORK / f"source/documents/{row['document_id']}.json")
    assert doc['source_relative_path'] == row['original_path']
    source_map = read(safe(row['source_map_path']))
    units.update({unit['source_unit_id']: unit for unit in source_map['source_units']})

locator_count = 0


def locators(value):
    global locator_count
    if isinstance(value, dict):
        if 'source_unit_id' in value and 'project_id' in value:
            locator_count += 1
            unit = units[value['source_unit_id']]
            for key in ('document_id', 'chapter_id', 'scene_id', 'source_relative_path', 'line_start', 'line_end', 'byte_start', 'byte_end', 'content_fingerprint'):
                assert value[key] == unit[key], (value['source_unit_id'], key)
        for item in value.values():
            locators(item)
    elif isinstance(value, list):
        for item in value:
            locators(item)


for folder in ['approvals', 'decisions', 'analysis/diagnostics', 'analysis/consistency', 'revisions/plans', 'revisions/change-sets']:
    for path in (WORK / folder).glob('*.json'):
        if not path.name.startswith('._'):
            locators(read(path))

draft = WORK / 'manuscript/versions/chapter-001-v001.md'
meta = read(draft.with_suffix('.metadata.json'))
expected = 'f195b7e0afc7f875731ade728a1bbf7a28d7becf3f38fa2d920498231f65d500'
assert sha(draft) == expected == meta['sha256']
assert meta['active'] is True and meta['status'] == 'approved_active'
assert meta['adoption_approval'] == '.manga-studio/approvals/approval-feb5212823b84aeaaa04bac3fedc4fc6.json'
source = resolve(meta['source']['relative_path'], meta['source']['sha256']).read_text()
text = draft.read_text()
register = read(WORK / 'revisions/phase-4-proposal-v001/exact-edit-register-v001.json')
parts, cursor = [], 0
for edit in register['edits']:
    a, b = edit['source_lines']
    assert ''.join(source.splitlines(keepends=True)[a-1:b]) == edit['before']
    parts += [''.join(source.splitlines(keepends=True)[cursor:a-1]), edit['after']]
    cursor = b
parts.append(''.join(source.splitlines(keepends=True)[cursor:]))
assert ''.join(parts) == text
diff = ''.join(difflib.unified_diff(source.splitlines(keepends=True), text.splitlines(keepends=True), fromfile=meta['source']['relative_path'], tofile=meta['relative_path']))
assert safe(meta['diff_relative_path']).read_text() == diff
review = read(safe(meta['consistency_review_relative_path']))
assert not review['errors'] and not review['approval_granted']
assert len(review['warnings']) == 7 and len(review['issue_dispositions']) == 30

config = context.config
before_config_rel = next(row['archived_relative_path'] for row in archive['entries'] if row['original_relative_path'] == '.manga-studio/project.json')
old_config = read(safe(before_config_rel))
for key in ['stage_locks', 'stage_lock_records', 'active_canon_version', 'active_storyboard_version', 'image_generation_enabled']:
    assert config[key] == old_config[key], key
assert config['active_manuscript_version'] == current['active_manuscript_version'] == '.manga-studio/manuscript/versions/chapter-001-v001.md'
assert config['workflow_phase'] == 'phase_4_manuscript_v001_approved_active_awaiting_canon_and_stage_locks'
assert not any(config['stage_locks'].values()) and not config['image_generation_enabled']
assert current['production_mode'] == 'panel_first'
authority = current['current_authority']
assert authority['visual_quality_direction_version'] == 'v002'
assert authority['visual_quality_decision_relative_path'] == '.manga-studio/decisions/chapter-001-quality-direction-v002.json'
assert authority['panel_count_policy'] == 'situation_driven_no_fixed_total'
assert authority['controlled_overlap_allowed'] is True
assert authority['overlap_requirements'] == ['explicit_reading_sequence', 'frame_or_clip_geometry', 'z_index', 'overlap_permission', 'focus_point', 'dialogue_safe_zones', 'continuity_clearance']
approved_reference = authority['approved_visual_references'][0]
assert approved_reference['reference_id'] == 'reference-daniel-tomas-shared-v001'
assert approved_reference['webp_relative_path'] == 'manga/02-references/approved-webp/daniel-tomas-shared.webp'
assert approved_reference['webp_sha256'] == '985cb554a78cca3367845b7cea089fee230f950629ae2da67d6c2fe90fd45ceb'
assert approved_reference['png_relative_path'] == 'manga/02-references/approve-png/daniel-tomas-shared.png'
assert approved_reference['png_sha256'] == '48f2680a489156033f49b11f5a7c02a7a0e92e0442a3a60fc2bc1487cd1bf2b6'
for directory in WORKSPACE_DIRECTORIES:
    assert (WORK / directory).is_dir()
root_names = {p.name for p in ROOT.iterdir() if not p.name.startswith('._')}
assert root_names == {'.git', '.gitignore', '.manga-studio', 'AGENTS.md', 'README.md', 'manga'}, root_names
reference_assets = {
    'manga/02-references/approve-png/daniel-tomas-shared.png',
    'manga/02-references/approved-webp/daniel-tomas-shared.webp',
}
manga_files = file_set(ROOT / 'manga')
actual = manga_files - reference_assets
assert manga_files == set(archive['expected_working_files']) | reference_assets
assert all(rel.endswith('.md') and not re.search(r'-v\d{3}|-chatgpt-image-prompt|\bfinal\b|\blatest\b', Path(rel).name) for rel in actual)
for directory in archive['expected_empty_directories']:
    assert safe(directory).is_dir() and not any(safe(directory).iterdir())
for obsolete in ['Comics', 'AppCover', 'characters.md', 'series-plan.md', 'MANGA-STUDIO.md', 'manga/02-references/effects']:
    assert not (ROOT / obsolete).exists()
links = 0
for rel in sorted(actual | {'README.md'}):
    content = safe(rel).read_text()
    assert not re.search(r'\b(Nari|Jiho)\b', content), rel
    for href in re.findall(r'\[[^\]]+\]\(([^)]+)\)', content):
        assert '://' not in href and not Path(href).is_absolute(), (rel, href)
        target = (safe(rel).parent / unquote(href.split('#', 1)[0])).resolve()
        assert target.is_relative_to(ROOT) and target.is_file(), (rel, href)
        links += 1
actual_reference_assets = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'manga').rglob('*') if p.is_file() and not p.name.startswith('._') and p.suffix.lower() in {'.png', '.webp', '.jpg', '.jpeg'}}
assert actual_reference_assets == reference_assets
assert not any(p for p in (WORK / 'handoff').rglob('*.json') if not p.name.startswith('._'))


def shared_role(rel):
    parts = Path(rel).parts
    if not rel.endswith('.md') or re.fullmatch(r'c\d{3}-p\d{3}\.md', parts[-1]):
        return False
    if len(parts) > 4 and parts[1] == '02-references' and parts[2] in {'characters', 'environments', 'objects'}:
        return False
    return True


shared = sorted(rel for rel in actual if shared_role(rel))
comparison = 'not_requested'
if args.compare:
    reference = args.compare.resolve()
    assert reference != ROOT and reference.name == '01-My Roommate Only Appears During Blackouts'
    expected_roles = {p.relative_to(reference).as_posix() for p in (reference / 'manga').rglob('*.md') if not p.name.startswith('._') and shared_role(p.relative_to(reference).as_posix())}
    assert set(shared) == expected_roles, {'missing': sorted(expected_roles - set(shared)), 'extra': sorted(set(shared) - expected_roles)}
    comparison = 'all_shared_working_document_paths_match'
result = {'record_type': 'structure_cleanup_validation', 'project_id': PID, 'checked_at': datetime.now(timezone.utc).isoformat(), 'status': 'pass',
          'runtime_story_profile': 'pass', 'source_maps': 'pass', 'sources_preserved': len(prov), 'original_candidates_verified': len(baseline['files']),
          'pre_cleanup_files_recoverable': len(archive['before_hashes']), 'archived_file_versions_verified': len(entries), 'historical_hash_bindings': history_counts,
          'approvals_valid': len(approvals), 'manuscript_approval': manuscript_approval_path.relative_to(ROOT).as_posix(), 'draft_sha256': expected, 'exact_approved_edits_verified': len(register['edits']), 'strict_source_locators_verified': locator_count,
          'working_markdown_files': len(actual), 'working_links_verified': links, 'shared_template_document_paths': shared, 'reference_comparison': comparison,
          'visual_quality_direction_version': authority['visual_quality_direction_version'], 'panel_count_policy': authority['panel_count_policy'], 'controlled_overlap_allowed': authority['controlled_overlap_allowed'],
          'approved_reference_files': len(reference_assets), 'approved_reference_id': approved_reference['reference_id'], 'user_supplied_reference_ingested': True,
          'locks_changed': False, 'active_versions_changed': True, 'artwork_created': False, 'production_ready': False,
          'warnings': ['Canon approval, prerequisite stage locks and storyboard approval remain pending.', 'Seven existing editorial warnings remain recorded; the manuscript-activation portion of SMA-WARN-006 is resolved.', 'Environment, object, effect and supporting-character references remain pending.', 'The inventory records import coordinates, not a fresh root scan. Use provenance and the relocation manifest for current storage.', 'Historical reports and evidence keep original paths and require hash-aware resolution.', 'Entity-specific folders and unreleased page prompts intentionally differ from the reference story.']}
if args.record:
    report = HERE / 'validation.json'
    assert not report.exists(), 'Refusing to overwrite a recorded validation.'
    result['manifest_sha256'] = sha(HERE / 'working-files.json')
    result['archive_manifest_sha256'] = sha(HERE / 'archive-manifest.json')
    report.write_text(json.dumps(result, indent=2) + '\n')
if args.record_path:
    report = safe(args.record_path)
    assert not report.exists(), 'Refusing to overwrite a recorded validation.'
    report.parent.mkdir(parents=True, exist_ok=True)
    result['manifest_sha256'] = sha(HERE / 'working-files.json')
    result['archive_manifest_sha256'] = sha(HERE / 'archive-manifest.json')
    report.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({key: value for key, value in result.items() if key != 'shared_template_document_paths'}, indent=2))
