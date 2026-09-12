# Balanced Revision Plan v001

Status: proposed, not active. All 30 audit findings map to work below. Preparing this plan implements no prose, canon, storyboard, or image changes.

## Scope and Dependencies

The next manuscript scope is the single supplied Chapter 1. Chapter 2 recovery or new writing requires its own source/continuation decision. No future chapters are presented as reconstructed. The plan references real chapter, scene, entity, and source-unit IDs from the approved audit.

The audit approval is hash-bound. The source and diagnostic stage locks remain false under the user's no-automatic-lock rule. These are authorized draft proposals, not an activated plan. Before implementation, the relevant creative choices, policy/plan, required locks, and exact change set must be explicitly approved. No approval of these is inferred from the audit approval.

The order is acyclic. Independent proposals may be reviewed together; actual application follows dependencies and stage gates. Later production tasks stay deferred until story and storyboard prerequisites are satisfied.

| Package | Stage | Depends on | Owner |
|---|---|---|---|
| SMA-WP-001: Bind the repair to available sources | Phase 4 preparation | None | manga-source-ingestor with manga-creator |
| SMA-WP-002: Adopt explicit identity and reference-text choices | Phase 4 text planning; visual derivatives in Phase 5 | SMA-WP-001 | manga-canon-manager for proposed facts; manga-revision-planner for edits |
| SMA-WP-003: Resolve the hatch, overlap, and transfer model | Phase 4 prerequisites | SMA-WP-001 | manga-world-bible and manga-canon-manager for proposals |
| SMA-WP-004: Specify the calendar and cost boundaries for continuation | Phase 4 baseline; exact schedule before any continuation | SMA-WP-003 | manga-story-architect with manga-world-bible |
| SMA-WP-005: Restore causal knowledge and investigation sequence | Phase 4 manuscript; adapted dialogue in Phase 5 | SMA-WP-002, SMA-WP-003, SMA-WP-004 | manga-chapter-writer and manga-dialogue-writer after required approvals |
| SMA-WP-006: Build independent goals and witness knowledge | Phase 4 architecture proposals; later development before continuation | SMA-WP-002, SMA-WP-004 | manga-character-bible with manga-story-architect |
| SMA-WP-007: Define a revelation ladder and scope checkpoints | Phase 4 architecture proposal, not additional chapter drafting | SMA-WP-004, SMA-WP-006 | manga-story-architect |
| SMA-WP-008: Set reader, content, and release boundaries | Phase 3 proposal; adoption only by user | SMA-WP-001 | manga-creator |
| SMA-WP-009: Apply approved repairs to a new Chapter 1 version | Phase 4, blocked until plan, relevant decisions, and exact change-set approval | SMA-WP-002, SMA-WP-003, SMA-WP-004, SMA-WP-005, SMA-WP-006, SMA-WP-008 | manga-chapter-writer |
| SMA-WP-010: Verify differences, continuity, and approvals | Phase 4 review | SMA-WP-007, SMA-WP-009 | manga-consistency-manager with manga-creator |
| SMA-WP-011: Reconcile legacy scripts after story approval | Phase 5 only | SMA-WP-010 | manga-dialogue-writer with manga-storyboard-director |
| SMA-WP-012: Specify readable preproduction and SFX | Phase 5 only, after required story approvals and locks | SMA-WP-011 | manga-storyboard-director, manga-panel-director, manga-lettering |
| SMA-WP-013: Prepare gated ChatGPT handoffs | Phase 6 only | SMA-WP-012 | manga-image-job-builder with manga-continuity-reviewer |

## SMA-WP-001: Bind the repair to available sources

Plan ID: SMA-PLAN-001. Status: proposed, not started. Stage: Phase 4 preparation.

Owner: manga-source-ingestor with manga-creator.

Issues: SMA-ISS-001.

Decisions required: SMA-PROP-001

Operation: Use the existing snapshot/manuscript document as the sole prose base; record the absent-source limitation in the derivative status report. Inventory recovered material only if supplied and authorized.

Expected result: Every later revision is attributable to actual sources and does not imply unseen Chapter 2 coverage.

Preserve: Original files and all prior audit versions.

Risk: A recovered source could require a new plan version.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice none; canon none; continuity low; structure none. Proposed canon impact is not canon adoption.

Acceptance checks:

- Original-source hashes still match.
- Chapter 2 and image absence remain explicit.
- No new source is imported without reviewed usage and provenance.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `README.md` lines 71-71; unit `source-unit-53b176a4c0114398a9d7456011734989`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/README.md` lines 8-9; unit `source-unit-d77a72566c874802bd931022316e75b7`


## SMA-WP-002: Adopt explicit identity and reference-text choices

Plan ID: SMA-PLAN-002. Status: proposed, not started. Stage: Phase 4 text planning; visual derivatives in Phase 5.

Owner: manga-canon-manager for proposed facts; manga-revision-planner for edits.

Issues: SMA-ISS-002, SMA-ISS-003, SMA-ISS-026.

Decisions required: SMA-PROP-002, SMA-PROP-013

Operation: Prepare proposed identity and physical-state records using the selected recommendations. Use them in new derivative text only after approval; do not merge disputed IDs silently.

Expected result: Names, clocks, clothing, and object states agree across new text artifacts.

Preserve: Adult silhouettes, occupational detail, chosen-family role, and civic antagonist.

Risk: Unseen images may later need a separate reconciliation plan.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice low; canon medium; continuity high; structure low. Proposed canon impact is not canon adoption.

Acceptance checks:

- Lilia and Arturo have one approved textual identity each.
- Legacy alternative labels remain traceable as conflicts.
- Clock identities and placement are unambiguous.
- No original character/reference text is overwritten.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `character-3f6621b20e6e4c0da53cb42678b5c277`
- `character-4a1f6a05cbd743bfaf528d862bda6202`
- `character-28e7610c7be1473aa1d5fb041293cf19`
- `character-9ed88c78fa9a4040837b28b31b249314`
- `prop-2feac2a1d9fd42e6975c1ed120a2e16a`
- `prop-abfd3210cb6e4133ab15d662bd6aa138`
- `character-a096cba8416847d4947a94012733a09b`
- `prop-67b953d0295447f788ff0fb7cf202823`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 349-349; unit `source-unit-f62b2bab7db84973a6e2c7672c9a0d2f`
- `characters.md` lines 63-69; unit `source-unit-a658f681501f4433bf5a58cc3078ab06`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 385-385; unit `source-unit-ce80ac6835624df48585b49354eec721`
- `characters.md` lines 83-90; unit `source-unit-9141d784709e4c64b0abf146cf304a7a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 71-71; unit `source-unit-c4d78a6b615d4de1a6019aa0aaf3e91b`
- `characters.md` lines 113-122; unit `source-unit-f9cfce8b95e14151aaa3337d3ed5e67a`


## SMA-WP-003: Resolve the hatch, overlap, and transfer model

Plan ID: SMA-PLAN-003. Status: proposed, not started. Stage: Phase 4 prerequisites.

Owner: manga-world-bible and manga-canon-manager for proposals.

Issues: SMA-ISS-005, SMA-ISS-006, SMA-ISS-007, SMA-ISS-008.

Decisions required: SMA-PROP-003, SMA-PROP-004, SMA-PROP-005, SMA-PROP-006

Operation: Prepare one coherent text rule sheet and movement ledger for the recommended physical model; record what is source-supported and what is a proposed addition.

Expected result: Chapter 1 can show safe exchanges and a bounded after-closure reply without moving a person through time.

Preserve: Sensory miracle, narrow window, dangerous wrist contact, safe fingertips, and returned-note reveal.

Risk: Clarifying mechanics can overexplain a lyrical scene; keep the rule sheet private and prose changes minimal.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice low; canon high; continuity high; structure low. Proposed canon impact is not canon adoption.

Acceptance checks:

- Each man remains within his own era while reaching the hatch.
- Ruined and restored objects have explicit sides.
- The reply crosses before closure and falls free later.
- Two paper objects remain separate.
- Protection does not create an unlimited fresh-object loophole.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `location-ec00909b6a1244d0ae35b1f2881055a5`
- `prop-ce6d2b5f51db4da0a3de67a809c13925`
- `prop-d988556780d44dbb999ac13c70c7aaad`
- `prop-1461014f20054066aa266d61a245d1b6`
- `prop-84030ef95dc848289c02a5c81ccff4fb`
- `prop-d12d36e4106949ac8be1873a74057a59`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 51-51; unit `source-unit-ad5f0a5daa3946b49ba41ba395edbb95`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 253-253; unit `source-unit-259c5c14baf545699aa54063d980ba91`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 85-85; unit `source-unit-43ac3a99bb66476483aa417a3e39185b`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 137-137; unit `source-unit-3a7388a34d734921b5b07ab8dc5b0104`
- `README.md` lines 40-51; unit `source-unit-6e81f10343fd4977bfd40faf49fa7087`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 441-441; unit `source-unit-a7bbc928754345c89e3d5f430a22b28c`


## SMA-WP-004: Specify the calendar and cost boundaries for continuation

Plan ID: SMA-PLAN-004. Status: proposed, not started. Stage: Phase 4 baseline; exact schedule before any continuation.

Owner: manga-story-architect with manga-world-bible.

Issues: SMA-ISS-009, SMA-ISS-010.

Decisions required: SMA-PROP-007, SMA-PROP-008

Operation: Document the intact first meeting, paired-day recommendation, and distinction between elapsed minutes and lost capacity. Reserve exact dates, penalty calibration, and recovery for a separate proposed continuation rule table before they enter prose.

Expected result: The repaired opening makes no unsupported permanent-loss or fire-deadline claim.

Preserve: Scarcity and the forty-year separation.

Risk: A long outline may require a different calendar; that must produce a new proposal rather than a silent exception.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice none; canon medium; continuity high; structure medium. Proposed canon impact is not canon adoption.

Acceptance checks:

- Chapter 1 retains 12:00-12:07.
- Tomas's October 17 statement is preserved.
- No exact date for Daniel or fire date is silently added.
- No later chapter is drafted until its calendar, intervention cost, and evidence model are explicitly approved.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `timeline-event-68f360f43d8a47ebb62965eff6732e6e`
- `timeline-event-8f8c4b747b494551aa21f1af3bd64e6b`
- `plot-thread-0289f530f9af462cb23c4cf0ccdb6efd`
- `prop-2feac2a1d9fd42e6975c1ed120a2e16a`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `README.md` lines 40-51; unit `source-unit-6e81f10343fd4977bfd40faf49fa7087`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 29-29; unit `source-unit-7eabb1ef43df4d50b0662bf7b9d85ab3`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 167-167; unit `source-unit-4a59e04f57ae454cb2c6ba802a261d5a`


## SMA-WP-005: Restore causal knowledge and investigation sequence

Plan ID: SMA-PLAN-005. Status: proposed, not started. Stage: Phase 4 manuscript; adapted dialogue in Phase 5.

Owner: manga-chapter-writer and manga-dialogue-writer after required approvals.

Issues: SMA-ISS-004, SMA-ISS-011, SMA-ISS-012, SMA-ISS-013, SMA-ISS-014, SMA-ISS-025, SMA-ISS-030.

Decisions required: SMA-PROP-002, SMA-PROP-009, SMA-PROP-011

Operation: Plan localized changes to the visit motive, guessed year, suspect inquiry, question/response chain, and knowledge ledger. Restore introductions and the signal clue when adapting the approved prose. Preserve an explicit future comparison obligation for the photograph.

Expected result: Every conclusion follows evidence available to its speaker; the final warning increases danger without proving murder.

Preserve: Opening line, dry corrections, mutual introductions, untouched-coffee clue, and ending order.

Risk: Added bridges could crowd banter; offset by selective trimming only where meaning is redundant.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice low; canon medium; continuity high; structure low. Proposed canon impact is not canon adoption.

Acceptance checks:

- Late access has one approved reason.
- 1986 is a hypothesis until confirmed.
- The name is learned before it is recognized on glass.
- The broker and signal are both investigated as leads, not convictions.
- Daniel does not know a proved death or arson from the scratch alone.
- The photo is not silently assigned contents.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `character-7aa0419823314e0787fe55c54aa83047`
- `character-a096cba8416847d4947a94012733a09b`
- `character-28e7610c7be1473aa1d5fb041293cf19`
- `prop-0b3caadd963c437787cd95d5af12ca9e`
- `prop-3c56d67fe71743d58ecaf605e59e5c46`
- `timeline-event-8f8c4b747b494551aa21f1af3bd64e6b`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`

Evidence:

- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 191-191; unit `source-unit-4fef04f396864b15af48636eabea8dfb`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 193-193; unit `source-unit-1e98a1a10c4047b4ad2d3a89a5455c8e`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 133-133; unit `source-unit-96fe1374a74447fdbfcf5f4130141f39`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 167-167; unit `source-unit-4a59e04f57ae454cb2c6ba802a261d5a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 375-375; unit `source-unit-51de7067630a4133ae844dc5ec6a75c6`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 379-379; unit `source-unit-94d295c33da3497b95dfb8f6684e50ee`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 23-23; unit `source-unit-f382583d75f74c52bc81bd180b8afc0c`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 469-469; unit `source-unit-c6a7150ac9fc488e9cad4e9e0e6d5390`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 19-19; unit `source-unit-dbb9308fb67a48f58755bcce1a647b1d`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 29-29; unit `source-unit-7eabb1ef43df4d50b0662bf7b9d85ab3`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 141-141; unit `source-unit-20310901061c4d7bbed8f596485c1435`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-006-chatgpt-image-prompt.md` lines 30-35; unit `source-unit-6f8b6b55d3cc49669f1b327417008462`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 45-45; unit `source-unit-f4f565dd8a764844a82dc82eb0425589`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 467-467; unit `source-unit-5baeaf5c38e0478c9ced56c85a719c75`


## SMA-WP-006: Build independent goals and witness knowledge

Plan ID: SMA-PLAN-006. Status: proposed, not started. Stage: Phase 4 architecture proposals; later development before continuation.

Owner: manga-character-bible with manga-story-architect.

Issues: SMA-ISS-015, SMA-ISS-016, SMA-ISS-017.

Decisions required: SMA-PROP-010

Operation: Prepare goal/knowledge/cost proposals from existing work and chosen-family relationships. Identify who witnessed versus inferred each clue. Do not insert unapproved trauma or secret notebook contents.

Expected result: Tomas can make a choice Daniel must respect; every witness has an independent reason to act or stay silent.

Preserve: Tomas's present initiative, Lilia's chosen-family warmth, and Maribel's competence.

Risk: A larger cast can inflate the opening; most material belongs to future approved architecture, not Chapter 1 exposition.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice low; canon medium; continuity medium; structure medium. Proposed canon impact is not canon adoption.

Acceptance checks:

- Tomas has an independent proposed goal and a possible rescue conflict.
- Daniel's growth is expressed as behavior, not an invented bereavement.
- All witness facts are marked observed, reported, inferred, or proposed.
- No unsupported character voice is treated as an existing dialogue sample.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `character-7aa0419823314e0787fe55c54aa83047`
- `character-a096cba8416847d4947a94012733a09b`
- `character-3f6621b20e6e4c0da53cb42678b5c277`
- `character-eac21dd0fae140d0b5fc6cd85bbbac0c`
- `character-457a700f0c6c478fb525eb3fb81f30a3`
- `character-073f27ce849748799a3a2ed06dabc898`
- `character-28e7610c7be1473aa1d5fb041293cf19`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`

Evidence:

- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 295-295; unit `source-unit-f0597e48a8be47c3a974a10d566c25ed`
- `characters.md` lines 40-48; unit `source-unit-5888edaed49c4018a8c24e3a92e27e33`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 11-11; unit `source-unit-3392356bfe1d40a1b1b44ed2fd61fc05`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 333-333; unit `source-unit-94c332b10eb844fa997807816f048e4a`
- `characters.md` lines 52-59; unit `source-unit-ef0c08b70b944fdab7c05c64f096f99a`
- `characters.md` lines 63-69; unit `source-unit-a658f681501f4433bf5a58cc3078ab06`


## SMA-WP-007: Define a revelation ladder and scope checkpoints

Plan ID: SMA-PLAN-007. Status: proposed, not started. Stage: Phase 4 architecture proposal, not additional chapter drafting.

Owner: manga-story-architect.

Issues: SMA-ISS-018, SMA-ISS-019, SMA-ISS-020, SMA-ISS-021.

Decisions required: SMA-PROP-007, SMA-PROP-008, SMA-PROP-012

Operation: Use existing Arc 1 titles to propose distinct knowledge, agency, danger, or relationship changes. Treat the first three chapters as a development checkpoint and later arcs as conditional proposals. Distinguish a repeated motif from a repeated first discovery.

Expected result: The existing long-series ambition has staged commitments rather than filler obligations.

Preserve: Daniel and Tomas as the center and San Aurelio as the anchor.

Risk: Scope may reduce or vary chapter counts; no original titles or arc folders are changed without explicit approval.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice low; canon medium; continuity high; structure high. Proposed canon impact is not canon adoption.

Acceptance checks:

- Each proposed early chapter changes at least one meaningful state.
- Chapter 5's pastry and Arc 2's false archive material add something beyond Chapter 1.
- Arc 3 and Arc 6 do not simply reveal Arc 1's culprit/fire again.
- Any memory change preserves consequences and mutual choice.
- Other cafes remain deferred until their necessity is demonstrated.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `timeline-event-8f8c4b747b494551aa21f1af3bd64e6b`
- `plot-thread-0289f530f9af462cb23c4cf0ccdb6efd`
- `location-ec00909b6a1244d0ae35b1f2881055a5`
- `character-7aa0419823314e0787fe55c54aa83047`
- `character-a096cba8416847d4947a94012733a09b`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 275-275; unit `source-unit-2d8f06e1bdef4346aab4238dd62b53b5`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 23-23; unit `source-unit-f382583d75f74c52bc81bd180b8afc0c`
- `series-plan.md` lines 11-14; unit `source-unit-f30646eb347344a3a21c4ad70a854cac`
- `README.md` lines 22-22; unit `source-unit-c9eefe2e08ef4256a97c21345e869c3c`
- `series-plan.md` lines 20-28; unit `source-unit-b339228c4e4d4b7380f13c1d8c079cfe`


## SMA-WP-008: Set reader, content, and release boundaries

Plan ID: SMA-PLAN-008. Status: proposed, not started. Stage: Phase 3 proposal; adoption only by user.

Owner: manga-creator.

Issues: SMA-ISS-019, SMA-ISS-029.

Decisions required: SMA-PROP-012

Operation: Review the creative brief and success plan: provisional audience/rating, unnamed-country boundary, preferred hopeful outcome, sustainable scope, offline feedback conditions, and publication assumptions.

Expected result: Production and audience decisions are intentional and distinguish hypotheses from evidence.

Preserve: Adult queer dignity, cultural texture, author control, and creator-health boundaries.

Risk: Real reader or capacity evidence may change the recommended scope.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice none; canon medium; continuity low; structure medium. Proposed canon impact is not canon adoption.

Acceptance checks:

- No country, historical accuracy, formal rating, commercial demand, or IP clearance is claimed without evidence.
- Reader and capacity metrics are defined but not fabricated as measured.
- No sharing, payment, release, or research is executed by this plan.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `character-7aa0419823314e0787fe55c54aa83047`
- `character-a096cba8416847d4947a94012733a09b`
- `location-e3d6a8be72a14872bb4be3930a5ac297`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `series-plan.md` lines 11-14; unit `source-unit-f30646eb347344a3a21c4ad70a854cac`
- `characters.md` lines 28-36; unit `source-unit-b1183dd2a0d84313bb026002ba5fe572`
- `characters.md` lines 40-48; unit `source-unit-5888edaed49c4018a8c24e3a92e27e33`


## SMA-WP-009: Apply approved repairs to a new Chapter 1 version

Plan ID: SMA-PLAN-009. Status: proposed, not started. Stage: Phase 4, blocked until plan, relevant decisions, and exact change-set approval.

Owner: manga-chapter-writer.

Issues: SMA-ISS-005, SMA-ISS-006, SMA-ISS-007, SMA-ISS-008, SMA-ISS-011, SMA-ISS-012, SMA-ISS-013, SMA-ISS-014, SMA-ISS-026, SMA-ISS-028.

Decisions required: SMA-PROP-003, SMA-PROP-004, SMA-PROP-005, SMA-PROP-006, SMA-PROP-009, SMA-PROP-013

Operation: Prepare an exact proposed change set against hashed source units, then after its approval create a separate Chapter 1 manuscript version. Keep title, core sequence, relationship exchanges, and ending order. Trim only repetitions that do not change state or meaning.

Expected result: A recognizable, causally clearer opening with no source overwrite.

Preserve: Paper-worldview voice, museum humor, bread joke, I am real reciprocity, and better-bread reply.

Risk: Mechanical repair can flatten voice; reject changes that explain what an action already makes clear.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice medium; canon medium; continuity high; structure low. Proposed canon impact is not canon adoption.

Acceptance checks:

- Every edit has an issue ID, source-unit target, and an approved change set.
- The original first line and three anchor exchanges remain recognizable.
- No forced new chapter split or cliffhanger is introduced.
- Both analytical scenes retain a meaningful state change.
- The new manuscript remains unapproved until separately reviewed.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `character-7aa0419823314e0787fe55c54aa83047`
- `character-a096cba8416847d4947a94012733a09b`
- `location-ec00909b6a1244d0ae35b1f2881055a5`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`

Evidence:

- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 51-51; unit `source-unit-ad5f0a5daa3946b49ba41ba395edbb95`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 253-253; unit `source-unit-259c5c14baf545699aa54063d980ba91`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 85-85; unit `source-unit-43ac3a99bb66476483aa417a3e39185b`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 137-137; unit `source-unit-3a7388a34d734921b5b07ab8dc5b0104`
- `README.md` lines 40-51; unit `source-unit-6e81f10343fd4977bfd40faf49fa7087`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 441-441; unit `source-unit-a7bbc928754345c89e3d5f430a22b28c`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 133-133; unit `source-unit-96fe1374a74447fdbfcf5f4130141f39`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 167-167; unit `source-unit-4a59e04f57ae454cb2c6ba802a261d5a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 375-375; unit `source-unit-51de7067630a4133ae844dc5ec6a75c6`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 379-379; unit `source-unit-94d295c33da3497b95dfb8f6684e50ee`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 23-23; unit `source-unit-f382583d75f74c52bc81bd180b8afc0c`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 469-469; unit `source-unit-c6a7150ac9fc488e9cad4e9e0e6d5390`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 19-19; unit `source-unit-dbb9308fb67a48f58755bcce1a647b1d`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 29-29; unit `source-unit-7eabb1ef43df4d50b0662bf7b9d85ab3`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 71-71; unit `source-unit-c4d78a6b615d4de1a6019aa0aaf3e91b`
- `characters.md` lines 113-122; unit `source-unit-f9cfce8b95e14151aaa3337d3ed5e67a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 209-209; unit `source-unit-137fe2fa314f4e89a676164f90e2ff4a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 329-329; unit `source-unit-4548ea5e2baa4f2e87525518fee26702`


## SMA-WP-010: Verify differences, continuity, and approvals

Plan ID: SMA-PLAN-010. Status: proposed, not started. Stage: Phase 4 review.

Owner: manga-consistency-manager with manga-creator.

Issues: SMA-ISS-001, SMA-ISS-002, SMA-ISS-003, SMA-ISS-004, SMA-ISS-005, SMA-ISS-006, SMA-ISS-007, SMA-ISS-008, SMA-ISS-009, SMA-ISS-010, SMA-ISS-011, SMA-ISS-012, SMA-ISS-013, SMA-ISS-014, SMA-ISS-015, SMA-ISS-016, SMA-ISS-017, SMA-ISS-018, SMA-ISS-019, SMA-ISS-020, SMA-ISS-021, SMA-ISS-022, SMA-ISS-023, SMA-ISS-024, SMA-ISS-025, SMA-ISS-026, SMA-ISS-027, SMA-ISS-028, SMA-ISS-029, SMA-ISS-030.

Decisions required: Existing approvals and review only; no new factual choice in this package.

Operation: Produce deterministic diffs and an issue disposition matrix distinguishing fixed, proposed, deferred, and not applicable. Check original hashes, knowledge, time, props, relationships, source locators, and voice anchors. Present the manuscript for review.

Expected result: Every audit finding remains accounted for; future-production issues are not falsely marked resolved by prose edits.

Preserve: Source traceability, explicit uncertainty, and separate approvals.

Risk: A technical pass cannot prove emotional success; use author review and authorized reader checks as separate evidence.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice none; canon none; continuity high; structure none. Proposed canon impact is not canon adoption.

Acceptance checks:

- All 30 issues have a disposition and evidence of the current state.
- Deferred items retain owners and prerequisites.
- No original or approved audit bytes change.
- No manuscript or story lock is activated by a validation result.
- Exact diff/review package is presented before manuscript approval.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `README.md` lines 71-71; unit `source-unit-53b176a4c0114398a9d7456011734989`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/README.md` lines 8-9; unit `source-unit-d77a72566c874802bd931022316e75b7`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 349-349; unit `source-unit-f62b2bab7db84973a6e2c7672c9a0d2f`
- `characters.md` lines 63-69; unit `source-unit-a658f681501f4433bf5a58cc3078ab06`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 385-385; unit `source-unit-ce80ac6835624df48585b49354eec721`
- `characters.md` lines 83-90; unit `source-unit-9141d784709e4c64b0abf146cf304a7a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 191-191; unit `source-unit-4fef04f396864b15af48636eabea8dfb`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 193-193; unit `source-unit-1e98a1a10c4047b4ad2d3a89a5455c8e`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 51-51; unit `source-unit-ad5f0a5daa3946b49ba41ba395edbb95`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 253-253; unit `source-unit-259c5c14baf545699aa54063d980ba91`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 85-85; unit `source-unit-43ac3a99bb66476483aa417a3e39185b`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 137-137; unit `source-unit-3a7388a34d734921b5b07ab8dc5b0104`
- `README.md` lines 40-51; unit `source-unit-6e81f10343fd4977bfd40faf49fa7087`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 441-441; unit `source-unit-a7bbc928754345c89e3d5f430a22b28c`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 29-29; unit `source-unit-7eabb1ef43df4d50b0662bf7b9d85ab3`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 167-167; unit `source-unit-4a59e04f57ae454cb2c6ba802a261d5a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 133-133; unit `source-unit-96fe1374a74447fdbfcf5f4130141f39`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 375-375; unit `source-unit-51de7067630a4133ae844dc5ec6a75c6`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 379-379; unit `source-unit-94d295c33da3497b95dfb8f6684e50ee`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 23-23; unit `source-unit-f382583d75f74c52bc81bd180b8afc0c`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 469-469; unit `source-unit-c6a7150ac9fc488e9cad4e9e0e6d5390`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 19-19; unit `source-unit-dbb9308fb67a48f58755bcce1a647b1d`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 295-295; unit `source-unit-f0597e48a8be47c3a974a10d566c25ed`
- `characters.md` lines 40-48; unit `source-unit-5888edaed49c4018a8c24e3a92e27e33`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 11-11; unit `source-unit-3392356bfe1d40a1b1b44ed2fd61fc05`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 333-333; unit `source-unit-94c332b10eb844fa997807816f048e4a`
- `characters.md` lines 52-59; unit `source-unit-ef0c08b70b944fdab7c05c64f096f99a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 275-275; unit `source-unit-2d8f06e1bdef4346aab4238dd62b53b5`
- `series-plan.md` lines 11-14; unit `source-unit-f30646eb347344a3a21c4ad70a854cac`
- `README.md` lines 22-22; unit `source-unit-c9eefe2e08ef4256a97c21345e869c3c`
- `series-plan.md` lines 20-28; unit `source-unit-b339228c4e4d4b7380f13c1d8c079cfe`
- `Comics/style-guide.md` lines 48-48; unit `source-unit-6d6d0dba516648269858f5b36244eec1`
- `Comics/README.md` lines 67-84; unit `source-unit-3c7f309a04e54097aa6a0b0e71a25560`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-001-chatgpt-image-prompt.md` lines 8-10; unit `source-unit-c8b3f5f93e994148b9c37a42523de881`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-002-chatgpt-image-prompt.md` lines 3-3; unit `source-unit-f5e529c130604b9791425c0f95b9024b`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 17-18; unit `source-unit-052743cf2c3d4756ad6122b75f7510ef`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 38-41; unit `source-unit-ae72db5bee8345dca0691d2674b77391`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 141-141; unit `source-unit-20310901061c4d7bbed8f596485c1435`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-006-chatgpt-image-prompt.md` lines 30-35; unit `source-unit-6f8b6b55d3cc49669f1b327417008462`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 71-71; unit `source-unit-c4d78a6b615d4de1a6019aa0aaf3e91b`
- `characters.md` lines 113-122; unit `source-unit-f9cfce8b95e14151aaa3337d3ed5e67a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-007-chatgpt-image-prompt.md` lines 28-31; unit `source-unit-be91f31d1c8f405ba1c57b6fe58d8d56`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 20-23; unit `source-unit-a0d3641d00b746b0824cb6370ffa1f85`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 209-209; unit `source-unit-137fe2fa314f4e89a676164f90e2ff4a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 329-329; unit `source-unit-4548ea5e2baa4f2e87525518fee26702`
- `characters.md` lines 28-36; unit `source-unit-b1183dd2a0d84313bb026002ba5fe572`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 45-45; unit `source-unit-f4f565dd8a764844a82dc82eb0425589`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 467-467; unit `source-unit-5baeaf5c38e0478c9ced56c85a719c75`


## SMA-WP-011: Reconcile legacy scripts after story approval

Plan ID: SMA-PLAN-011. Status: proposed, not started. Stage: Phase 5 only.

Owner: manga-dialogue-writer with manga-storyboard-director.

Issues: SMA-ISS-002, SMA-ISS-003, SMA-ISS-004, SMA-ISS-013, SMA-ISS-022, SMA-ISS-024, SMA-ISS-025, SMA-ISS-026, SMA-ISS-028.

Decisions required: SMA-PROP-002, SMA-PROP-013, SMA-PROP-014

Operation: Create new script versions from the approved manuscript, using legacy scripts only as comparison. Restore causal dialogue, correct identities, and redistribute events by reading pressure rather than preserving every five/six-panel page.

Expected result: A story-faithful, clearly readable proposed adaptation.

Preserve: Strong existing images and quiet reaction beats.

Risk: Fourteen pages may no longer be the best allocation; page count is a proposal until approved.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice medium; canon low; continuity high; structure medium. Proposed canon impact is not canon adoption.

Acceptance checks:

- Introductions and connective questions precede responses.
- All clue captions match character knowledge.
- The fifteen-title arc envelope does not dictate a uniform panel count.
- Text corrections remain separate from artwork and original prompts.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `character-7aa0419823314e0787fe55c54aa83047`
- `character-a096cba8416847d4947a94012733a09b`
- `character-3f6621b20e6e4c0da53cb42678b5c277`
- `character-28e7610c7be1473aa1d5fb041293cf19`
- `prop-2feac2a1d9fd42e6975c1ed120a2e16a`
- `prop-67b953d0295447f788ff0fb7cf202823`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`

Evidence:

- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 349-349; unit `source-unit-f62b2bab7db84973a6e2c7672c9a0d2f`
- `characters.md` lines 63-69; unit `source-unit-a658f681501f4433bf5a58cc3078ab06`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 385-385; unit `source-unit-ce80ac6835624df48585b49354eec721`
- `characters.md` lines 83-90; unit `source-unit-9141d784709e4c64b0abf146cf304a7a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 191-191; unit `source-unit-4fef04f396864b15af48636eabea8dfb`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 193-193; unit `source-unit-1e98a1a10c4047b4ad2d3a89a5455c8e`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 23-23; unit `source-unit-f382583d75f74c52bc81bd180b8afc0c`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 469-469; unit `source-unit-c6a7150ac9fc488e9cad4e9e0e6d5390`
- `Comics/style-guide.md` lines 48-48; unit `source-unit-6d6d0dba516648269858f5b36244eec1`
- `Comics/README.md` lines 67-84; unit `source-unit-3c7f309a04e54097aa6a0b0e71a25560`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 17-18; unit `source-unit-052743cf2c3d4756ad6122b75f7510ef`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 38-41; unit `source-unit-ae72db5bee8345dca0691d2674b77391`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 141-141; unit `source-unit-20310901061c4d7bbed8f596485c1435`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-006-chatgpt-image-prompt.md` lines 30-35; unit `source-unit-6f8b6b55d3cc49669f1b327417008462`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 71-71; unit `source-unit-c4d78a6b615d4de1a6019aa0aaf3e91b`
- `characters.md` lines 113-122; unit `source-unit-f9cfce8b95e14151aaa3337d3ed5e67a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 209-209; unit `source-unit-137fe2fa314f4e89a676164f90e2ff4a`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md` lines 329-329; unit `source-unit-4548ea5e2baa4f2e87525518fee26702`


## SMA-WP-012: Specify readable preproduction and SFX

Plan ID: SMA-PLAN-012. Status: proposed, not started. Stage: Phase 5 only, after required story approvals and locks.

Owner: manga-storyboard-director, manga-panel-director, manga-lettering.

Issues: SMA-ISS-022, SMA-ISS-024, SMA-ISS-027.

Decisions required: SMA-PROP-014

Operation: Prepare event-driven page intents, explicit reading sequence, geometry-only nemu, one dominant panel event, motivated camera directions, dialogue-safe areas, and complete SFX fields.

Expected result: A reviewable storyboard and lettering plan ready for appropriate preproduction checks.

Preserve: Rain and clock soundscape, silence at closure, and deliberate negative space.

Risk: No current image exists to validate rendered clarity; a planning score cannot confer approval.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice low; canon none; continuity high; structure medium. Proposed canon impact is not canon adoption.

Acceptance checks:

- Every SFX has source, reader meaning, intensity, English language, translation context, and lettering intent.
- Every panel has one dominant event.
- All dynamic layouts have a stated narrative reason.
- Reading order and text-space checks pass before artwork handoff.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `prop-ce6d2b5f51db4da0a3de67a809c13925`
- `prop-2feac2a1d9fd42e6975c1ed120a2e16a`
- `prop-d12d36e4106949ac8be1873a74057a59`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `Comics/style-guide.md` lines 48-48; unit `source-unit-6d6d0dba516648269858f5b36244eec1`
- `Comics/README.md` lines 67-84; unit `source-unit-3c7f309a04e54097aa6a0b0e71a25560`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 17-18; unit `source-unit-052743cf2c3d4756ad6122b75f7510ef`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 38-41; unit `source-unit-ae72db5bee8345dca0691d2674b77391`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-007-chatgpt-image-prompt.md` lines 28-31; unit `source-unit-be91f31d1c8f405ba1c57b6fe58d8d56`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 20-23; unit `source-unit-a0d3641d00b746b0824cb6370ffa1f85`


## SMA-WP-013: Prepare gated ChatGPT handoffs

Plan ID: SMA-PLAN-013. Status: proposed, not started. Stage: Phase 6 only.

Owner: manga-image-job-builder with manga-continuity-reviewer.

Issues: SMA-ISS-022, SMA-ISS-023, SMA-ISS-027.

Decisions required: SMA-PROP-014

Operation: After all required approvals and locks, create structured jobs for needed references and later panels/covers. Release dependent jobs only with actual approved hash-locked references and deterministic Markdown attachment checklists.

Expected result: External ChatGPT handoffs satisfy the high-quality contract and have no invented reference paths.

Preserve: Distinct adult designs and the user's complete artwork prohibition.

Risk: Reference turnaround and revisions can change schedule; measure them before public commitments.

Alternatives: retain only conservative corrections and accept deferred rule debt, or adopt a transformative restructure and accept greater voice/scope change. The specific alternatives for every triggering issue remain in the approved diagnostic.

Impact: voice none; canon none; continuity high; structure none. Proposed canon impact is not canon adoption.

Acceptance checks:

- No image is generated, edited, or retouched by Codex.
- Panel artwork jobs forbid dialogue, captions, balloons, SFX text, borders, page numbers, signatures, watermarks, and color.
- All attachment paths exist and hashes match approvals.
- A pending reference blocks only its dependent jobs; no fallback prompt is called an approved reference.

Stable targets:

- `chapter-fb585a7fd3e7450e936edbcfce992566`
- `character-7aa0419823314e0787fe55c54aa83047`
- `character-a096cba8416847d4947a94012733a09b`
- `location-ec00909b6a1244d0ae35b1f2881055a5`
- `prop-ce6d2b5f51db4da0a3de67a809c13925`
- `scene-2f59e856c58d4d6db58d635cbc64e0bb`
- `scene-3b27382ec9a049e2acde70d7cf88fc10`

Evidence:

- `Comics/style-guide.md` lines 48-48; unit `source-unit-6d6d0dba516648269858f5b36244eec1`
- `Comics/README.md` lines 67-84; unit `source-unit-3c7f309a04e54097aa6a0b0e71a25560`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-001-chatgpt-image-prompt.md` lines 8-10; unit `source-unit-c8b3f5f93e994148b9c37a42523de881`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-002-chatgpt-image-prompt.md` lines 3-3; unit `source-unit-f5e529c130604b9791425c0f95b9024b`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-007-chatgpt-image-prompt.md` lines 28-31; unit `source-unit-be91f31d1c8f405ba1c57b6fe58d8d56`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md` lines 20-23; unit `source-unit-a0d3641d00b746b0824cb6370ffa1f85`


## Deterministic Diff Plan

1. Recheck the original Chapter 1 SHA-256 and active source-map checksum against approved provenance before constructing replacements.
2. Use exact source-unit IDs and content fingerprints as edit targets. Record the expected original text and each planned insert/replace/append operation in a new proposed change set. Do not use unanchored global replacement.
3. Present the exact proposed change set for its required approval; no replacement manuscript text has been created in Phase 3.
4. After required approvals, create a new version under .manga-studio/manuscript/versions without modifying the original path. Preserve existing newline handling and retain raw snapshots.
5. Produce a UTF-8 unified diff with deterministic ordering, fixed root-relative source/destination labels, and no filesystem timestamps. Compare the source-normalized base to the new version; record original and normalized hashes so normalization cannot hide a story change.
6. Save the diff and a structured issue-to-operation disposition record as new versions under .manga-studio/revisions/diffs. Never claim the current plan is a completed old/new prose diff.
7. Recheck originals, evidence, state transitions, dialogue ownership, object custody, time markers, and voice anchors. Present manuscript and diff for approval before story locking.

## Issues Deferred by Stage

Issues 022-027 include later production work. Their presence in the plan is accountability, not authorization to execute those stages now. If Chapter 1 is repaired, unresolved script, geometry, lettering, reference, and handoff items must remain deferred rather than marked resolved. The same applies to future arc, calendar, and memory mechanisms where no manuscript exists.
