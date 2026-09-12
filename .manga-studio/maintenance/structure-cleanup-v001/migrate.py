"""One-shot authorized layout migration; source bytes and approval history stay intact."""
import argparse
import hashlib
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / '.manga-studio'
HERE = Path(__file__).resolve().parent
ARCHIVE = '.manga-studio/history/structure-cleanup-v001/before'
PID = 'ms-70391ae1065048cf8bdd564959abd6c3'
DRAFT = '.manga-studio/manuscript/versions/chapter-001-v001.md'
BRIEF = '.manga-studio/revisions/phase-3-v001/creative-brief-v001.md'
CONTINUITY = '.manga-studio/revisions/phase-4-proposal-v001/working-continuity-v001.md'
PROPOSALS = '.manga-studio/revisions/phase-3-v001/decision-proposals-v001.json'
REVIEW = '.manga-studio/analysis/consistency/chapter-001-manuscript-v001-review.md'
NOTICE = ('Working reference assembled from this story\'s existing material. '
          'This reorganization does not adopt canon, approve the manuscript, or release production.')


def read_json(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    return path.relative_to(ROOT).as_posix()


def files(directory):
    return sorted(p for p in directory.rglob('*') if p.is_file()
                  and '.git' not in p.relative_to(ROOT).parts and not p.name.startswith('._'))


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=True) + '\n').encode()


def link(origin, target, label):
    path = os.path.relpath(target, str(Path(origin).parent)).replace(os.sep, '/')
    return f'[{label}]({path})'


parser = argparse.ArgumentParser()
parser.add_argument('--apply', action='store_true')
args = parser.parse_args()
assert read_json('.manga-studio/project.json')['project_id'] == PID
assert not (HERE / 'archive-manifest.json').exists(), 'Migration already prepared; inspect the manifest before resuming.'

originals = {r['relative_path']: r['sha256'] for r in read_json('.manga-studio/source/inventory-baseline-v001.json')['files']}
for rel, sha in originals.items():
    assert digest(ROOT / rel) == sha, f'Source drift: {rel}'
assert len(originals) == 25
assert digest(ROOT / DRAFT) == 'f195b7e0afc7f875731ade728a1bbf7a28d7becf3f38fa2d920498231f65d500'

retire = set(originals) - {'.gitignore'}
retire.update(relative(p) for p in files(ROOT / 'manga'))
retire.update(relative(p) for p in files(WORK / 'tooling/workspace-refactor-v001'))
retire.update({'MANGA-STUDIO.md', '.manga-studio/workspace-layout-v001.json'})
mutable = {'AGENTS.md', '.manga-studio/project.json'}
mutable.update('.manga-studio/source/' + name + '.json' for name in ('provenance', 'inventory', 'id-map', 'structure'))
mutable.update(relative(p) for p in files(WORK / 'source/documents'))
backup = sorted(retire | mutable)
archive_map = {rel: f'{ARCHIVE}/{rel}' for rel in backup}
before = {relative(p): digest(p) for p in files(ROOT) if HERE not in p.parents}
output = {}
evidence = {}


def text(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def section(rel, title, level=2):
    lines = text(rel).splitlines(keepends=True)
    heading = '#' * level + ' ' + title
    start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    end = next((i for i in range(start + 1, len(lines))
                if re.match(r'^#{1,' + str(level) + r'} ', lines[i])), len(lines))
    return ''.join(lines[start + 1:end]).strip()


def put(rel, title, body, sources=(), notice=NOTICE):
    source_list = list(dict.fromkeys(sources))
    footer = '\n\n## Evidence\n\n' + '\n'.join(
        '- ' + link(rel, archive_map.get(src, src), Path(src).name) for src in source_list) if source_list else ''
    output[rel] = (f'# {title}\n\n' + (notice + '\n\n' if notice else '') + body.strip() + footer + '\n').encode()
    evidence[rel] = [{'relative_path': archive_map.get(src, src), 'sha256': digest(ROOT / src)} for src in source_list]


def index(rel, title, paths, intro=NOTICE):
    body = '\n'.join('- ' + link(rel, path, label) for path, label in paths)
    put(rel, title, body, notice=intro)


def brief(title):
    return section(BRIEF, title)


def continuity(title):
    return section(CONTINUITY, title)


S = 'manga/00-series/'
T = 'manga/01-style/'
R = 'manga/02-references/'
A = 'manga/03-story/arc-01/'
C = A + 'chapter-001/'
P = 'manga/04-production/'
PC = P + 'arc-01/chapter-001/'
put(S + 'story-concept.md', 'Story Concept', brief('Core Premise and Reader Promise'), [BRIEF])
put(S + 'tone-and-genre.md', 'Tone And Genre', brief('Readers and Positioning') + '\n\n' + brief('Format, Scope, and Ending Direction'), [BRIEF])
put(S + 'narrative-rules.md', 'Narrative Rules', brief('Creative Priorities') + '\n\n## Protected Voice\n\n' + brief('Protected Voice and Material'), [BRIEF])
put(S + 'world-rules.md', 'World Rules', continuity('Spatial State') + '\n\n## Transfer And Contact\n\n' + continuity('Object and Contact Ledger') + '\n\n## Undecided Rules\n\n' + continuity('Before Continuation'), [CONTINUITY, DRAFT])
put(S + 'continuity-ledger.md', 'Continuity Ledger', continuity('Object and Contact Ledger') + '\n\n## Knowledge And Causality\n\n' + continuity('Knowledge and Causality'), [CONTINUITY, DRAFT])
put(S + 'character-relationships.md', 'Character Relationships', continuity('Character and Scene Change') + '\n\n## Protected Relationship Material\n\n' + brief('Protected Voice and Material'), [CONTINUITY, BRIEF])
put(S + 'parallel-events-timeline.md', 'Parallel Events Timeline', continuity('Spatial State') + '\n\n## Calendar Boundary\n\n' + continuity('Before Continuation'), [CONTINUITY])
draft_lines = text(DRAFT).splitlines()
markers = [(i + 1, line) for i, line in enumerate(draft_lines) if re.fullmatch(r'12:0[0-7]\.', line)]
timeline = '| Cafe clock | Current draft lines |\n|---|---|\n' + '\n'.join(
    f'| {line[:-1]} | {n}-{markers[i+1][0]-1 if i+1 < len(markers) else len(draft_lines)} |'
    for i, (n, line) in enumerate(markers))
put(S + 'chronology.md', 'Chronology', 'The existing draft retains the full first seven minutes. The ranges below index its text, not manga pages.\n\n' + timeline + '\n\n' + continuity('Before Continuation'), [DRAFT, CONTINUITY])
roadmap = section('series-plan.md', 'Arc Roadmap')
roadmap = re.sub(r'`0([1-7])-Arc-([^`]+)`', lambda m: m[2].replace('-', ' '), roadmap)
roadmap = roadmap.replace('Folder Name', 'Source Arc Title')
put(S + 'arc-roadmap.md', 'Arc Roadmap', '## Provisional Source Roadmap\n\nThese are historical author-intent titles and ranges, not drafted chapters, adopted canon, or a release commitment.\n\n' + roadmap + '\n\n## Accepted Scope Direction\n\n' + brief('Format, Scope, and Ending Direction'), ['series-plan.md', BRIEF])
put(S + 'legacy-concept-extraction.md', 'Legacy Concept Extraction', 'The original premise, cast, style notes and roadmap have been reorganized by role. Historical page and cover prompts are comparison evidence only. Their file-presence claims, page counts and conflicting names do not establish available chapters or approved assets.\n\n' + brief('Purpose and Scope') + '\n\n' + continuity('Knowledge and Causality'), ['README.md', 'characters.md', 'series-plan.md', CONTINUITY])

policy = read_json('manga/01-style/production-policy-v001.json')
style_lines = section('Comics/style-guide.md', 'Black-And-White Time-Slip Railway Romance Manga/Manhwa/Manhua Style Lock').splitlines()
style = '\n'.join(line for line in style_lines if line.startswith(('- Format:', '- Page feel:', '- Linework:', '- Rendering:', '- Human Finish:')))
put(T + 'manga-style-lock.md', 'Manga Style Lock', 'Status: existing visual direction, not an activated lock or approved image specification.\n\n' + style + '\n\nInteriors remain monochrome. Covers require separate approval. No art has been generated or approved.', ['Comics/style-guide.md', 'manga/01-style/production-policy-v001.json'])
put(T + 'reader-visible-language-lock.md', 'Reader-Visible Language Lock', 'Source language: English. Output language: English. Reading direction: left-to-right.\n\nThese are recorded project preferences, not approval of lettering, dialogue, signage or an image job. Preserve exact approved text at the later lettering stage.', ['manga/01-style/production-policy-v001.json'])
put(T + 'screentone-and-hatching-guide.md', 'Screentone And Hatching Guide', '\n'.join(line for line in style_lines if line.startswith(('- Linework:', '- Rendering:', '- Human Finish:'))) + '\n\nColor descriptions in source references are identity notes; interior art uses grayscale. No numeric tone palette or print specification has been approved.', ['Comics/style-guide.md'])
put(T + 'panel-language.md', 'Panel Language', 'Future panels require one dominant event, motivated camera direction, legible staging, continuity and dialogue-safe zones. Variation must follow the event.\n\n' + section('Comics/style-guide.md', 'Panel Pacing Rule'), ['manga/01-style/production-policy-v001.json', 'Comics/style-guide.md'])
put(T + 'page-composition-rules.md', 'Page Composition Rules', 'Future nemu is geometry-only, with explicit reading sequence and event-driven page layouts. No page geometry or panel count is approved. The fourteen legacy interior prompts do not constitute the current storyboard.\n\nThe retained deliverable is panel-first: approve text-free panel returns, then compose and letter separately. Matching another story\'s filenames does not switch this project to complete-page generation.', ['manga/01-style/production-policy-v001.json'])
put(T + 'speech-balloon-guide.md', 'Speech Balloon Guide', 'No approved manga dialogue script or balloon geometry exists. Future balloon placement must preserve approved wording, reading sequence and dialogue-safe zones. Balloons and dialogue are added separately after panel artwork approval; do not embed them in panel-generation requests.', ['manga/01-style/production-policy-v001.json'])
put(T + 'sfx-lettering-guide.md', 'SFX Lettering Guide', 'No SFX script is released. Every future SFX record requires:\n\n' + '\n'.join('- ' + item for item in policy['sfx_required_fields']) + '\n\nSFX text belongs to the separate lettering stage, not panel artwork.', ['manga/01-style/production-policy-v001.json'])

character_text = section('characters.md', 'Core Cast')
names = re.findall(r'^### (.+)$', character_text, re.M)
assert names == ['Daniel Soriano', 'Tomas Rivera', 'Maribel Santos', 'Lilia Ramos', 'Benjamin Manalo', 'Arturo Salcedo', 'Ernesto Galang']
character_paths = []
for name in names:
    slug = name.lower().replace(' ', '-')
    rel = R + f'characters/{slug}/{slug}.md'
    old = section('characters.md', name, 3)
    fields = [line for line in old.splitlines() if line.startswith(('- Age:', '- Occupation:', '- Personality:', '- Visual Design:', '- Signature Props:'))]
    if name == 'Tomas Rivera':
        fields = [line.replace('cream short-sleeved 1980s cafe shirt', 'cream long-sleeved 1980s cafe shirt, rolled to the elbows,') for line in fields]
    body = '## Existing Reference Intent\n\nThese source descriptions are not proof that every prop or future event appears in Chapter 1.\n\n' + '\n'.join(fields)
    if name == 'Tomas Rivera':
        body += '\n\nThe sleeve wording follows accepted SMA-PROP-013 and the current draft, replacing the contradictory short-sleeve reference. No other visual redesign is introduced.'
    put(rel, name, body, ['characters.md', DRAFT, PROPOSALS])
    canon = R + f'characters/{slug}/canon.md'
    put(canon, name + ': Canon Status', 'Status: not adopted. The adjacent character document reorganizes author-reference material; the current Chapter 1 draft remains inactive. Future roles, personal history and unshown objects must not be promoted into confirmed events.\n\n' + continuity('Character and Scene Change') + '\n\n' + link(canon, rel, 'Character reference'), [CONTINUITY, DRAFT])
    character_paths.append((rel, name))

spatial = continuity('Spatial State')
put(R + 'environments/cafe-siete/cafe-floor-plan.md', 'Cafe Siete: Floor Plan', 'No drawn floor plan, dimensions or screen direction is approved. Existing spatial continuity follows.\n\n' + spatial, [CONTINUITY, DRAFT])
put(R + 'environments/cafe-siete/cafe-perspective.md', 'Cafe Siete: Perspective', spatial + '\n\nThe cafe clock is above the cafe door. The station clock above the ticket hall is a separate object. No reference image is available.', [CONTINUITY, DRAFT])
put(R + 'environments/cafe-siete/canon.md', 'Cafe Siete: Canon Status', 'Status: not adopted. Treat the floor-plan and perspective notes as the current draft\'s spatial continuity, not approved geometry or artwork.\n\n' + continuity('Before Continuation'), [CONTINUITY])
env_lines = section('Comics/style-guide.md', 'San Aurelio And Cafe Visual Rules').splitlines()
station = '\n'.join(line for line in env_lines if line.startswith(('- San Aurelio Junction', '- 2026 station spaces', '- 1986 station spaces')))
put(R + 'environments/san-aurelio-junction/station-perspective.md', 'San Aurelio Junction: Perspective', 'Existing visual reference intent, not approved artwork or a measured building plan.\n\n' + station, ['Comics/style-guide.md'])
put(R + 'environments/san-aurelio-junction/canon.md', 'San Aurelio Junction: Canon Status', 'Status: not adopted. Historical architectural details remain source intent; they have not been independently researched.\n\n' + continuity('Knowledge and Causality'), [CONTINUITY])
put(R + 'objects/cafe-and-archive-props/cafe-and-archive-props.md', 'Cafe And Archive Props', continuity('Object and Contact Ledger'), [CONTINUITY, DRAFT])
index(R + 'characters/README.md', 'Characters', character_paths, 'Seven source characters; no adopted character bible or approved character images.')
index(R + 'environments/README.md', 'Environments', [(R + 'environments/cafe-siete/cafe-floor-plan.md', 'Cafe Siete: spatial plan'), (R + 'environments/cafe-siete/cafe-perspective.md', 'Cafe Siete: perspective'), (R + 'environments/san-aurelio-junction/station-perspective.md', 'San Aurelio Junction')], 'Existing location notes only. No approved image paths or dimensions.')
index(R + 'objects/README.md', 'Objects', [(R + 'objects/cafe-and-archive-props/cafe-and-archive-props.md', 'Cafe and archive props')], 'Object custody from the current inactive draft. No approved prop images.')
for folder, title in [('approve-png', 'Reference PNG Masters'), ('approved-webp', 'Reference WebP Conversions')]:
    put(R + folder + '/README.md', title, 'No approved files are present. Placement in this folder never grants approval. Use only actual, reviewed, hash-locked assets and keep matching stable basenames.\n\nThe folder name follows the shared story convention.', notice='Status: empty; no artwork authorized.')
index(R + 'README.md', 'References', [(R + folder + '/README.md', label) for folder, label in [('characters', 'Characters'), ('environments', 'Environments'), ('objects', 'Objects'), ('approve-png', 'PNG masters'), ('approved-webp', 'WebP conversions')]], 'Text references only. There are no approved visual assets. Exact attachment checklists will require real files after the relevant gates.')

put(A + 'arc-bible.md', 'Arc 1: The Fire At San Aurelio Junction', brief('Purpose and Scope') + '\n\n' + brief('Core Premise and Reader Promise'), [BRIEF])
status_section = section('series-plan.md', 'Current Production Status')
titles = status_section.split('Current planned Arc 1 chapters:\n', 1)[1].split('\n\nArc 1', 1)[0].strip()
put(A + 'arc-outline.md', 'Arc 1 Outline', '## Provisional Source Titles\n\n' + titles + '\n\nOnly Chapter 1 is supplied. Chapter 2 is unavailable; no future chapter folders or prose have been fabricated. The fifteen-title envelope is provisional, not a mandatory length.\n\n' + continuity('Before Continuation'), ['series-plan.md', CONTINUITY])
put(A + 'mystery-progression.md', 'Mystery Progression', continuity('Knowledge and Causality') + '\n\n## Unresolved Continuation Dependencies\n\n' + continuity('Before Continuation'), [CONTINUITY])
register = read_json('.manga-studio/analysis/continuity-registers-v001.json')
threads = '| Thread ID | Existing audit subject |\n|---|---|\n' + '\n'.join(f"| {row['id']} | {row['name']} |" for row in register['threads_and_setups_payoffs'])
put(A + 'event-thread-map.md', 'Event Thread Map', 'This is a navigation index to the existing audit, not a claim that every historical issue is still open. Current issue dispositions are in the manuscript consistency review.\n\n' + threads + '\n\n' + link(A + 'event-thread-map.md', REVIEW, 'Current draft consistency review'), ['.manga-studio/analysis/continuity-registers-v001.json', REVIEW])
put(C + 'chapter-outline.md', 'Chapter 1 Outline', continuity('Character and Scene Change'), [CONTINUITY, DRAFT])
prelude_start = next(i + 1 for i, line in enumerate(draft_lines) if line.startswith('Daniel Soriano trusted paper'))
station_start = next(i + 1 for i, line in enumerate(draft_lines) if line.startswith('At 11:41 PM'))
put(C + 'scene-sequence.md', 'Chapter 1 Scene Sequence', f'Existing prose sequence; not a manga beat allocation.\n\n| Source scene ID | Segment | Draft lines |\n|---|---|---|\n| scene-2f59e856c58d4d6db58d635cbc64e0bb | Archive prelude | {prelude_start}-{station_start-1} |\n| scene-3b27382ec9a049e2acde70d7cf88fc10 | Station encounter | {station_start}-{len(draft_lines)} |\n\n' + continuity('Character and Scene Change'), [DRAFT, CONTINUITY])
put(C + 'dialogue-script.md', 'Chapter 1 Dialogue Script', 'Status: not adapted. No manga dialogue script, balloon assignments or rewritten dialogue has been created. The complete dialogue remains in the inactive prose draft.\n\n' + link(C + 'dialogue-script.md', DRAFT, 'Read the full draft') + '\n\n## Voice Constraints\n\n' + brief('Protected Voice and Material'), [DRAFT, BRIEF])
put(C + 'parallel-events.md', 'Chapter 1 Parallel Events', spatial + '\n\n' + timeline, [DRAFT, CONTINUITY])
put(C + 'page-map.md', 'Chapter 1 Page Map', 'Status: awaiting manuscript adoption and storyboard planning. No current page count, panel allocation, reading geometry or page-turn plan is approved. The fourteen retired interior prompts are evidence only and must not be released.\n\n' + link(C + 'page-map.md', PC + 'page-order.md', 'Production page order'), [DRAFT])
put(C + 'reference-needs.md', 'Chapter 1 Reference Needs', 'This is an index of existing reference notes, not an approved asset request or attachment checklist. No visual assets are available.\n\n' + '\n'.join('- ' + link(C + 'reference-needs.md', path, name) for path, name in character_paths[:2]) + '\n- ' + link(C + 'reference-needs.md', R + 'environments/README.md', 'Station and cafe notes') + '\n- ' + link(C + 'reference-needs.md', R + 'objects/README.md', 'Object custody notes') + '\n\nSupporting cast and exact image needs must be determined from the approved storyboard.', [DRAFT])

put(P + 'page-standard.md', 'Page Standard', 'English, left-to-right, paged monochrome; quality profile: high. The configured 1654 x 2339 dimensions are runtime placeholders, not an approved print standard.\n\nRetain the requested panel-first workflow. A panel is not a finished page. Approve panel artwork before composition and separate lettering. No page or panel jobs are released.\n\nPanel artwork prohibits:\n\n' + '\n'.join('- ' + item for item in policy['panel_art_prohibited']) + '\n\nStory, storyboard, references and production approvals are still required. Codex must never generate, edit, retouch or correct artwork.', ['manga/01-style/production-policy-v001.json'])
put(PC + 'page-order.md', 'Chapter 1 Page Order', 'Released pages: 0. Approved page images: 0.\n\nNo c001-p### prompt is active. Page numbering will follow the adopted storyboard, not the old fourteen-page prompt set. Nothing in the empty output directory is approval evidence.', notice='Status: blocked pending manuscript adoption and preproduction.')
put(PC + 'README.md', 'Chapter 1 Production', '\n'.join('- ' + link(PC + 'README.md', path, label) for path, label in [(C + 'README.md', 'Story draft and planning'), (PC + 'page-order.md', 'Page order'), (P + 'page-standard.md', 'Page standard')]) + '\n\nThe approved-png directory is empty. No art, prompt release or image generation is authorized.', notice='Status: not ready. No active manuscript, adopted canon, locked storyboard or approved reference images.')
index(P + 'arc-01/README.md', 'Arc 1 Production', [(PC + 'README.md', 'Chapter 1')], 'Only the existing Chapter 1 scope is represented.')
index(P + 'README.md', 'Production', [(P + 'page-standard.md', 'Page standard'), (P + 'arc-01/README.md', 'Arc 1')], 'No released image jobs or approved images. Production remains blocked.')

for base, title in [(S, 'Series'), (T, 'Style'), (A, 'Arc 1: The Fire At San Aurelio Junction'), (C, 'Chapter 1: The Cafe That Opened For Seven Minutes')]:
    child_paths = [(rel, data.decode().splitlines()[0][2:]) for rel, data in sorted(output.items())
                   if str(Path(rel).parent) + '/' == base and Path(rel).name != 'README.md']
    if base == A:
        child_paths += [(C + 'README.md', 'Chapter 1')]
    if base == C:
        child_paths = [(DRAFT, 'Read the complete inactive draft'), (REVIEW, 'Draft consistency review')] + child_paths
    index(base + 'README.md', title, child_paths)
index('manga/03-story/README.md', 'Story', [(A + 'README.md', 'Arc 1: The Fire At San Aurelio Junction')], 'Chapter 1 has one inactive reconstructed draft. No Chapter 2 source or new continuation is available.')
put('manga/naming-standard.md', 'Naming Standard', '''Use stable working filenames without dates, version suffixes, final, latest or correction numbers. Technical versions stay inside .manga-studio.

## Reference Files

Keep the same basename for a specification and its eventual PNG and WebP. Use this story's entity names: daniel-soriano, tomas-rivera, cafe-floor-plan, cafe-perspective, station-perspective and cafe-and-archive-props.

Specifications live under characters, environments or objects. PNG masters use 02-references/approve-png; verified conversions use 02-references/approved-webp. These folder names match the shared convention; they do not grant approval. Do not create image placeholders.

## Chapter Files

Use arc-01/chapter-001. Complete-page output names follow c001-p001.png and c001-p001.webp. Future page records use c001-p001.md. Panel assets use distinct names such as c001-p001-panel-01.png; never disguise a panel as a complete page.

The currently requested deliverable is panel-first, with separate composition and lettering. No executable page or panel prompt exists yet. Complete-page integrated-lettering jobs would require a separate workflow decision.

## One Working Copy

Keep one current specification or released prompt per asset. Preserve prior bytes, checksums and approvals internally before replacement. Authoritative manuscripts remain versioned internally; the chapter index links to the draft instead of keeping a second editable copy.

Current files and their evidence are registered in the cleanup working-files manifest. A stable name does not imply canon adoption, artwork approval or permission to generate.''', notice='Shared layout convention; story-specific content and workflow are preserved.')
index('manga/README.md', 'Seven Minutes After Midnight', [(S + 'README.md', '00 Series'), (T + 'README.md', '01 Style'), (R + 'README.md', '02 References'), ('manga/03-story/README.md', '03 Story'), (P + 'README.md', '04 Production'), ('manga/naming-standard.md', 'Naming standard'), (C + 'README.md', 'Chapter 1: draft and status')], 'Current scope: Arc 1, Chapter 1. The reconstructed draft is inactive and awaiting manuscript adoption. No approved artwork or released image jobs.')
put('README.md', 'Seven Minutes After Midnight', 'Open [Manga production](manga/README.md) for the current workspace.\n\nWorking files use stable names. Original sources, old prompts, versions, approvals and technical history are preserved inside `.manga-studio/`.\n\nScope remains Arc 1, Chapter 1. This cleanup does not approve the manuscript or authorize additional chapters, artwork, publication or a Git push.', notice='')
output['AGENTS.md'] = b'''<!-- BEGIN MANGA STUDIO MANAGED -->
## Manga Studio

- This repository is the project root; manga is the working surface, not a separate project.
- The user explicitly authorized the structure-cleanup-v001 migration. Archived originals are immutable evidence at the paths in .manga-studio/maintenance/structure-cleanup-v001/archive-manifest.json. Keep their bytes, snapshots, normalized sources, source maps, stable IDs and approvals intact.
- Current source records point to archived original bytes. Immutable maps and historical evidence retain their as-imported paths. Resolve old paths with the manifest and expected SHA-256; never confuse the new root README with the original README.
- The current working register is .manga-studio/maintenance/structure-cleanup-v001/working-files.json. Verification is .manga-studio/maintenance/structure-cleanup-v001/verify.py. Historical layout verifiers apply only to their archived state.
- Keep stable filenames under manga/00-series, 01-style, 02-references, 03-story and 04-production. Preserve a version internally before replacing a working file. Do not restore obsolete Comics, AppCover, versioned visible indexes, or duplicate manuscript copies.
- Authoritative manuscript versions stay in .manga-studio/manuscript/versions. Chapter 1 v001 remains draft_inactive. No canon, manuscript or storyboard is adopted; no locks have changed.
- Working extracts are navigation and reference material, not new canon or production authority. Use this story's evidence only. Other stories supply generic folder roles, never characters, assets, approvals or workflow choices.
- Do not run a fresh inventory over the cleaned root and overwrite the imported archive records. Runtime scanning excludes .manga-studio; future intake must preserve/merge the approved archived inventory and stable IDs. Do not import README, AGENTS or manga derivatives as new original sources.
- Future ingestion and structural parsing require explicit new sources and a provenance check. Historical source-map paths are preserved as import coordinates, not current storage paths.
- Retain panel_first: externally generated text-free, borderless panel art, then approval, composition and separate lettering. Naming parity does not select complete_page.
- Image generation remains disabled. Codex must never generate, edit, retouch or correct artwork. Future structured ChatGPT image jobs require high quality, approved hash-locked references, exact attachments, structured SFX, reading order and all applicable gates.
- Do not activate versions, approve artifacts, change locks, draft new chapters, release prompts, publish or push without explicit authorization for that action.
<!-- END MANGA STUDIO MANAGED -->
'''

# Relocate mutable storage indexes while keeping all original source maps and evidence locators immutable.
config = read_json('.manga-studio/project.json')
config['source_exclusion_patterns'] = [p for p in config['source_exclusion_patterns'] if p != 'MANGA-STUDIO.md']
config['source_exclusion_patterns'].append('README.md')
config['blocking_reasons'] = [b.replace(' and its matching manga reading copy', '').replace('both remain inactive', 'it remains inactive') for b in config['blocking_reasons']]
output['.manga-studio/project.json'] = json_bytes(config)
prov = read_json('.manga-studio/source/provenance.json')
for row in prov['records']:
    row['original_path'] = archive_map[row['original_path']]
output['.manga-studio/source/provenance.json'] = json_bytes(prov)
inventory = read_json('.manga-studio/source/inventory.json')
for row in inventory['files']:
    row['relative_path'] = archive_map.get(row['relative_path'], row['relative_path'])
output['.manga-studio/source/inventory.json'] = json_bytes(inventory)
ids = read_json('.manga-studio/source/id-map.json')
for row in ids['namespaces']['source_documents']:
    if row['path'] in archive_map:
        row['aliases'] = sorted(set(row['aliases'] + [row['path']]))
        row['path'] = archive_map[row['path']]
output['.manga-studio/source/id-map.json'] = json_bytes(ids)
structure = read_json('.manga-studio/source/structure.json')
for row in structure['documents']:
    row['source_relative_path'] = archive_map[row['source_relative_path']]
output['.manga-studio/source/structure.json'] = json_bytes(structure)
for path in files(WORK / 'source/documents'):
    doc = read_json(relative(path))
    old = doc['source_relative_path']
    doc['aliases'] = sorted(set(doc['aliases'] + [old]))
    doc['source_relative_path'] = archive_map[old]
    output[relative(path)] = json_bytes(doc)

now = datetime.now(timezone.utc).isoformat()
decision_rel = '.manga-studio/decisions/structure-cleanup-v001.json'
output[decision_rel] = json_bytes({
    'schema_version': '3.0.0', 'project_id': PID, 'decision_id': 'SMA-DEC-STRUCTURE-CLEANUP-V001',
    'decision_type': 'editorial', 'subject_ids': [PID], 'actor': 'user', 'decided_at': now,
    'decision': 'Rename and reorganize useful material; remove obsolete working files; follow the existing story layout for consistency.',
    'rationale': 'The user explicitly approved the proposed archival migration and said: yes rename if uses on the story if not remove just follow 100% on the structure on the existing stories for consistencies. Scope is layout and naming, not creative adoption or artwork.',
    'evidence': [], 'result_artifacts': ['README.md', 'manga/README.md', relative(HERE / 'archive-manifest.json'), relative(HERE / 'working-files.json')],
    'supersedes_decision_id': 'SMA-DEC-WORKSPACE-STRUCTURE-V001'
})
empty_dirs = [PC + 'approved-png']
for path in files(ROOT):
    rel = relative(path)
    if rel in output:
        assert rel in backup, f'Unbacked replacement: {rel}'
for rel in output:
    assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
manifest = {
    'record_type': 'authorized_structure_cleanup_archive', 'project_id': PID, 'created_at': now,
    'status': 'prepared', 'decision_relative_path': decision_rel, 'project_root': '.',
    'archive_root': ARCHIVE, 'source_bytes_changed': False,
    'entries': [{'original_relative_path': rel, 'archived_relative_path': archive_map[rel], 'sha256': before[rel],
                 'action': 'replace' if rel in output else 'retire_from_working_tree',
                 'imported_source': rel in originals and rel != '.gitignore'} for rel in backup],
    'before_hashes': [{'relative_path': rel, 'sha256': sha} for rel, sha in sorted(before.items())],
    'expected_working_files': sorted(rel for rel in output if rel.startswith('manga/')),
    'expected_empty_directories': empty_dirs,
    'historical_path_resolution': 'Resolve by original_relative_path AND expected SHA-256; immutable source maps retain as-imported coordinates.',
    'recovery': 'Do not run migration twice. Verify archive hashes first. Reversal requires explicit user approval: preserve any later work, restore entries to their original paths, and remove only unchanged generated files listed in working-files.json.'
}
summary = {'archived_files': len(backup), 'original_story_sources': 24, 'retired_working_paths': len(retire - set(output)),
           'working_markdown_files': len(manifest['expected_working_files']), 'empty_output_directories': empty_dirs}
if not args.apply:
    print(json.dumps(summary, indent=2))
    raise SystemExit(0)

# Finish and verify every backup before changing a single existing file.
for rel in backup:
    dest = ROOT / archive_map[rel]
    assert not dest.exists(), f'Archive collision: {dest}'
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / rel, dest)
    assert digest(dest) == before[rel]
(HERE / 'archive-manifest.json').write_bytes(json_bytes(manifest))
for rel in sorted(retire):
    assert digest(ROOT / rel) == before[rel]
    (ROOT / rel).unlink()
for rel, data in output.items():
    path = ROOT / rel
    if path.exists():
        assert digest(path) == before[rel], f'Concurrent edit: {rel}'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
for old_tree in ['Comics', 'AppCover', 'manga', '.manga-studio/tooling/workspace-refactor-v001']:
    directory = ROOT / old_tree
    for path in sorted((p for p in directory.rglob('*') if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
        if not any(path.iterdir()):
            path.rmdir()
    if directory.exists() and not any(directory.iterdir()):
        directory.rmdir()
for directory in empty_dirs:
    (ROOT / directory).mkdir(parents=True, exist_ok=True)
working = {'record_type': 'current_working_layout', 'project_id': PID, 'created_at': now,
           'reference_layout': '01-My Roommate Only Appears During Blackouts: generic paths only, inspected read-only',
           'other_story_content_copied': False, 'production_mode': 'panel_first',
           'active_manuscript_version': None, 'active_canon_version': None, 'active_storyboard_version': None,
           'summary': summary, 'artifacts': [{'relative_path': rel, 'sha256': digest(ROOT / rel),
                                           'evidence': evidence.get(rel, [])} for rel in sorted(output)],
           'intentional_differences': ['Story-specific character and location slugs.', 'No c001-p### prompts: no adopted storyboard or released jobs.', 'No PNG/WebP files: no approved artwork.', 'Only historical/runtime-required internal directories; no copied history IDs or foreign assets.']}
(HERE / 'working-files.json').write_bytes(json_bytes(working))
print(json.dumps(summary, indent=2))
