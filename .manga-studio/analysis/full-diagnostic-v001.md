# Full Diagnostic Audit v001

Status: proposed, not approved. Complete review of the available root, not of unavailable future chapters. No reconstruction or artwork performed.

Source keys resolve to exact root-relative paths in coverage-v001.md and coverage-v001.json. Every locator is checked against an active source-map unit and immutable original snapshot. Priorities describe order of work; severity describes impact. No P0 emergency is asserted.

Document-level chapter IDs on supporting sources are parser containers, not additional story chapters. The actual manuscript has one chapter and two analytical scenes; their boundaries are not approved story restructuring.

## SMA-ISS-001: Production notes overstate the available story

Priority: P1 | Category: unresolved_plot_thread | Severity: high | Confidence: 100%

Evidence class: confirmed evidence gap. Status: open, awaiting review.

README, arc notes, and series plan claim a drafted Chapter 2 and Chapter 1 reader images. The root inventory contains only Chapter 1 prose, fourteen interior page prompts, three cover prompts including the app cover, and supporting notes; no reader image files or second chapter are present.

Why it matters: An audit cannot claim coverage of unavailable chapters or assess the ending of a 105-chapter plan as completed fiction.

Preserve: Every existing file and the planned second chapter title.

Evidence:

- SRC-22 lines 71-71 (unit source-unit-53b176a4c0114398a9d7456011734989): "Status: Arc 1 planned.". Source: `README.md`.
- SRC-19 lines 8-9 (unit source-unit-d77a72566c874802bd931022316e75b7): "16 WebP reader assets present". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/README.md`.
- SRC-24 lines 49-49 (unit source-unit-d56cc976e50f45a98db1724da9c63781): "Current drafted chapters:". Source: `series-plan.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: None.

Possible solutions and tradeoffs:

1. Recover the claimed originals into a separately inventoried source addition and extend the audit. Risk: further findings may change priorities.
2. Approve an available-material audit and treat Chapter 2 onward as unwritten or unavailable, with later expansion from approved plans. Risk: recovered material may require reconciliation.

Uncertainty: Absence is confirmed only within this story root; files could exist elsewhere. No deletion or loss is inferred.

Adaptation impact: Rendered continuity and later chapter pacing cannot be reviewed.

Dependencies: No prerequisite finding.

## SMA-ISS-002: Lilia becomes Inez in Page 10

Priority: P1 | Category: relationship_continuity | Severity: high | Confidence: 100%

Evidence class: confirmed cross-source contradiction. Status: open, awaiting review.

The prose calls the kitchen voice Tiya Lilia, and the character reference identifies Lilia Ramos as the cafe owner and chosen aunt. Page 10 assigns the same lines and role to Inez without explanation.

Why it matters: The adaptation changes a supporting character's identity and obscures the chosen-family relationship.

Preserve: The off-panel kitchen interruption, payment joke, and chosen-family warmth.

Evidence:

- SRC-04 lines 349-349 (unit source-unit-f62b2bab7db84973a6e2c7672c9a0d2f): "Only the impossible ones, Tiya Lilia.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-23 lines 63-69 (unit source-unit-a658f681501f4433bf5a58cc3078ab06): "- Role: Owner of Cafe Siete in 1986". Source: `characters.md`.
- SRC-14 lines 17-18 (unit source-unit-c8fdf8b1c77644a8b6fb87414af995b4): "SUPPORTING VOICE - INEZ". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-010-chatgpt-image-prompt.md`.
- SRC-14 lines 33-36 (unit source-unit-9ed2cfc930c641b18ba0628814a74062): "ONLY THE IMPOSSIBLE ONES, TIYA INEZ.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-010-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Lilia Ramos: character-3f6621b20e6e4c0da53cb42678b5c277

Possible solutions and tradeoffs:

1. Use Lilia in a new version of the affected script after approval. Risk: any unavailable artwork would also need reconciliation.
2. Retain Inez only through an explicit rename or separate-character decision with all affected references versioned. Risk: unnecessary cast complexity and divergence from prose.

Uncertainty: No supplied source establishes Inez as an alias or approved replacement; do not silently merge her into canon.

Adaptation impact: Character labels and future voice/reference jobs would carry the wrong identity.

Dependencies: SMA-ISS-001

## SMA-ISS-003: Arturo becomes Rafael in Page 11

Priority: P1 | Category: plot_logic | Severity: high | Confidence: 100%

Evidence class: confirmed cross-source contradiction. Status: open, awaiting review.

The prose and character reference name Arturo Salcedo as the visiting broker. Page 11 instead labels the figure and notebook entry Rafael Aragon while retaining Arturo's physical and behavioral traits.

Why it matters: A mystery depends on stable evidence attribution. A silent suspect rename creates a different apparent suspect.

Preserve: The untouched coffee, pale suit, human civic menace, and restrained clue delivery.

Evidence:

- SRC-04 lines 385-385 (unit source-unit-ce80ac6835624df48585b49354eec721): "Arturo Salcedo. He has been visiting". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-23 lines 83-90 (unit source-unit-9141d784709e4c64b0abf146cf304a7a): "- Role: Primary human antagonist of Arc 1". Source: `characters.md`.
- SRC-15 lines 17-18 (unit source-unit-1242364868ab44baa98516415d4fcceb): "BACKGROUND FIGURE - RAFAEL ARAGON". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-011-chatgpt-image-prompt.md`.
- SRC-15 lines 43-48 (unit source-unit-cb2503e2015c4828bf5ce4f57765e424): "RAFAEL ARAGON. SMILES LIKE A KNIFE UNDER A NAPKIN.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-011-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Arturo Salcedo: character-28e7610c7be1473aa1d5fb041293cf19

Possible solutions and tradeoffs:

1. Restore Arturo in a newly versioned Page 11 script subject to approval. Risk: later unavailable scripts may have propagated Rafael.
2. Approve a deliberate rename and update new versions of every dependent reference. Risk: broad revision for no demonstrated story benefit.

Uncertainty: No alias, second broker, or rename decision is supplied.

Adaptation impact: Suspect silhouettes, notebook lettering, and future reference jobs would disagree.

Dependencies: SMA-ISS-001

## SMA-ISS-004: The adaptation removes the introduction needed for the name clue

Priority: P1 | Category: character_knowledge | Severity: high | Confidence: 99%

Evidence class: confirmed adaptation omission. Status: open, awaiting review.

The prose introduces Daniel and Tomas by name before Daniel recognizes TOMAS on the door. Pages 5-7 omit that exchange, but Page 7 has Daniel say I FOUND YOUR NAME. Character-lock text is not reader-facing dialogue.

Why it matters: Daniel identifies the stranger's name without the scene supplying how he learned it. A fair mystery should preserve this causal link.

Preserve: The shock of a scratched future name matching a living person.

Evidence:

- SRC-04 lines 191-191 (unit source-unit-4fef04f396864b15af48636eabea8dfb): "My name is Daniel Soriano". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 193-193 (unit source-unit-1e98a1a10c4047b4ad2d3a89a5455c8e): "Tomas Rivera.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-09 lines 31-34 (unit source-unit-8273263b50ba4727bd0ff86e6ae54aaa): "YOU ARE NOT FROM THE EVENING TRAIN.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-005-chatgpt-image-prompt.md`.
- SRC-10 lines 17-18 (unit source-unit-3ca78b2e608b4d8aaca16f691d954ab7): "PAGE LAYOUT AND SCRIPT". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-006-chatgpt-image-prompt.md`.
- SRC-11 lines 33-36 (unit source-unit-18590315e2d14b119eafca06e8aaa720): "I FOUND YOUR NAME.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-007-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; Tomas Rivera: character-a096cba8416847d4947a94012733a09b

Possible solutions and tradeoffs:

1. Restore a concise mutual introduction before the scratched-name discussion. Risk: extra lettering requires page rebalance.
2. Give Tomas an explicitly staged name-bearing object and let Daniel connect it to the scratch. Risk: invents a prop and weakens the voluntary intimacy of an introduction.

Uncertainty: A generated image might add a name, but no images exist here and unrequested additions cannot supply evidence.

Adaptation impact: Repair knowledge order before lettering or panel jobs.

Dependencies: SMA-ISS-002, SMA-ISS-003

## SMA-ISS-005: Counter-to-window movement lacks a stable physical layout

Priority: P1 | Category: world_rule_continuity | Severity: high | Confidence: 95%

Evidence class: spatial ambiguity requiring decision. Status: open, awaiting review.

The service window is behind the counter and opens into the kitchen, yet later opens between the two men, who are already on opposite sides of a shared counter. No movement explains how both access opposite faces of that window.

Why it matters: The exchange boundary is the central action constraint; confusing its location makes safe touch and prohibited crossing hard to read.

Preserve: The narrow opening, shared counter, asymmetric damage, and contrast between dangerous and safe contact.

Evidence:

- SRC-04 lines 51-51 (unit source-unit-ad5f0a5daa3946b49ba41ba395edbb95): "Behind the counter, a narrow service window opened into the kitchen.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 253-253 (unit source-unit-259c5c14baf545699aa54063d980ba91): "Between them, the service window slid open by itself.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-23 lines 113-122 (unit source-unit-f9cfce8b95e14151aaa3337d3ed5e67a): "- Service Window: Narrow opening between the kitchen and counter.". Source: `characters.md`.
- SRC-12 lines 25-28 (unit source-unit-af4ffc840b6e46e797c8751c328b8de3): "The narrow service window slides open by itself between the kitchen and counter.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Cafe Siete: location-ec00909b6a1244d0ae35b1f2881055a5; service window: prop-ce6d2b5f51db4da0a3de67a809c13925; shared counter: prop-d988556780d44dbb999ac13c70c7aaad

Possible solutions and tradeoffs:

1. Approve a simple fixed cafe floor plan and add motivated movement from the counter to the kitchen hatch. Risk: costs a transition beat.
2. Define the original counter explicitly as the hatch sill and revise the contradictory spatial descriptions in new versions. Risk: changes the opening's established architecture.

Uncertainty: An unusual layout or supernatural relocation could explain this, but neither is established.

Adaptation impact: Requires geometry-only staging before panel direction; no artwork needed now.

Dependencies: No prerequisite finding.

## SMA-ISS-006: The transformation's visible extent is inconsistent in description

Priority: P1 | Category: world_rule_continuity | Severity: medium | Confidence: 94%

Evidence class: presentation ambiguity. Status: open, awaiting review.

The prose first says the painted glass clears and broken stools stand upright, then says Daniel's side remains ruined and the painted door still carries the scratch. Page 4 similarly restores objects around Daniel before later split-era staging.

Why it matters: Readers need to know whether physical objects restore, an overlay is visible, or only the far side changes, especially when marks become evidence.

Preserve: The sensory rush of warmth and the striking split between inhabited past and ruined present.

Evidence:

- SRC-04 lines 85-85 (unit source-unit-43ac3a99bb66476483aa417a3e39185b): "The painted glass cleared.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 137-137 (unit source-unit-3a7388a34d734921b5b07ab8dc5b0104): "His side of the cafe remained abandoned.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 215-215 (unit source-unit-e09b1ca0d2254f64ac26e86809f5cb4f): "On his side, the name remained scratched into old paint.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-08 lines 29-32 (unit source-unit-5832d974b8a743f9adc6c79fa5b8ef01): "Every light in the cafe turns on at once around Daniel.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-004-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Cafe Siete: location-ec00909b6a1244d0ae35b1f2881055a5; shared counter: prop-d988556780d44dbb999ac13c70c7aaad

Possible solutions and tradeoffs:

1. Limit restoration to Tomas's visible side and define what Daniel feels across the boundary. Risk: slightly reduces the enveloping miracle.
2. Keep a transient full-room overlap, explicitly followed by separation. Risk: adds a rule that must remain consistent and may affect later evidence.

Uncertainty: These passages may describe a subjective overlay, not a factual contradiction; the presentation does not identify it.

Adaptation impact: Value patterns, damage, and the same objects need stable era states.

Dependencies: SMA-ISS-005

## SMA-ISS-007: The reply arrives after the stated exchange interval

Priority: P1 | Category: world_rule_continuity | Severity: high | Confidence: 98%

Evidence class: unexplained exception, potentially intentional. Status: open, awaiting review.

After 12:07, closure, and several seconds alone, Daniel's notebook page slips from the sealed window with Tomas's reply. The stated exchange rules restrict the reliable connection to seven minutes.

Why it matters: This powerful ending can become an unlimited communication loophole unless delayed delivery has a bounded cause.

Preserve: I will bring better bread, the smoke-stained aged page, and Daniel's broken laugh.

Evidence:

- SRC-22 lines 40-51 (unit source-unit-6e81f10343fd4977bfd40faf49fa7087): "1. The abandoned railway cafe returns to life". Source: `README.md`.
- SRC-04 lines 441-441 (unit source-unit-a7bbc928754345c89e3d5f430a22b28c): "For several seconds he did not move.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 443-443 (unit source-unit-d6c71bcf9aa5438e8c7eaa1e8295d6c8): "Then something pale slipped from the sealed service window". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-17 lines 33-36 (unit source-unit-998274dcd23f4fac9c6c695880e41639): "A yellowed notebook page slips from beneath it". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-013-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: service window: prop-ce6d2b5f51db4da0a3de67a809c13925; notebook reply: prop-1461014f20054066aa266d61a245d1b6

Possible solutions and tradeoffs:

1. Show the paper already caught beneath the closing sill, released seconds later. Risk: makes the wonder more mechanically explicit.
2. Approve a narrowly defined delayed-return mechanism and track its cost and limits. Risk: adds complexity and invites attempts to bypass the countdown.

Uncertainty: Delivery could be physical release rather than a new crossing. The audit does not declare time travel impossible or demand immediate exposition.

Adaptation impact: A panel must distinguish a caught page from a reopened connection.

Dependencies: SMA-ISS-005, SMA-ISS-006

## SMA-ISS-008: Object protection and backward adaptation are undefined

Priority: P1 | Category: world_rule_continuity | Severity: high | Confidence: 98%

Evidence class: rule specification gap. Status: open, awaiting review.

The rules permit objects to avoid forty years of aging if protected by the interval, but the pastry ages while the interval is active. Backward objects later adapt to the older time, without a defined trigger or physical effect. The preserved note and ordinary notebook page are separate objects.

Why it matters: Letters, pastries, photographs, and evidence are the romance and investigation engine. Undefined exceptions let any later outcome seem convenient.

Preserve: Asymmetric travel, tactile aging, and archival materials as Daniel's meaningful contribution.

Evidence:

- SRC-22 lines 40-51 (unit source-unit-6e81f10343fd4977bfd40faf49fa7087): "5. Objects passed from 1986 to 2026 arrive aged". Source: `README.md`.
- SRC-22 lines 40-51 (unit source-unit-6e81f10343fd4977bfd40faf49fa7087): "6. Objects passed from 2026 to 1986". Source: `README.md`.
- SRC-04 lines 269-269 (unit source-unit-d10bd4385fba4e2fb1c7c95d95de390e): "For one impossible second, it remained perfect.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 317-317 (unit source-unit-cc540924f20249129a806415c25f81be): "The paper did not age.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 335-335 (unit source-unit-d271c46efee641b9a32930a59465b10b): "Tomas folded the sleeve and tucked it carefully". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: archival sleeve: prop-84030ef95dc848289c02a5c81ccff4fb; notebook reply: prop-1461014f20054066aa266d61a245d1b6; aged pastry: prop-d12d36e4106949ac8be1873a74057a59

Possible solutions and tradeoffs:

1. Specify testable conditions for aging and protection privately, then reveal them through small experiments. Risk: excessive testing could crowd intimacy.
2. Remove the protection exception from proposed canon and keep consistent forward aging plus ordinary preservation. Risk: restricts future pastry and letter possibilities.

Uncertainty: No demonstrated protective technique or completed post-closure observation of the first sleeve exists.

Adaptation impact: Each exchange needs before/after state and custody; avoid conflating the two notes.

Dependencies: SMA-ISS-007

## SMA-ISS-009: Historical-warning costs need a consistent causal model

Priority: P1 | Category: causality | Severity: high | Confidence: 96%

Evidence class: planned rule gap. Status: open, awaiting review.

Direct warnings shorten the connection; coded clues do less damage but the cafe understands intent. Minute loss does not recover easily, implying unspecified recovery. No supplied scene establishes a baseline cost, threshold, or distinction between ordinary flicker and permanent loss.

Why it matters: The central dilemma needs consequential choices the reader can learn from. Punishment based on unseen intent risks feeling author-controlled.

Preserve: Saving Tomas threatens the means of knowing him; indirect communication should create moral and emotional pressure.

Evidence:

- SRC-22 lines 40-51 (unit source-unit-6e81f10343fd4977bfd40faf49fa7087): "8. Direct warnings about major historical events". Source: `README.md`.
- SRC-22 lines 40-51 (unit source-unit-6e81f10343fd4977bfd40faf49fa7087): "9. Indirect clues, coded letters". Source: `README.md`.
- SRC-22 lines 40-51 (unit source-unit-6e81f10343fd4977bfd40faf49fa7087): "10. The cafe clock records the remaining connection.". Source: `README.md`.
- SRC-04 lines 241-241 (unit source-unit-9799d281fc174a8aa91853533b94efe6): "The lights flickered.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-24 lines 56-70 (unit source-unit-1db292e5fb9f45bf941dd8e12d59c606): "6. Archive Box 7-M". Source: `series-plan.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: cafe clock: prop-2feac2a1d9fd42e6975c1ed120a2e16a; connection cost: plot-thread-0289f530f9af462cb23c4cf0ccdb6efd

Possible solutions and tradeoffs:

1. Approve a private rule matrix with triggers, observables, and recovery limits; dramatize the first measurable loss. Risk: makes a poetic mechanism more constrained.
2. Retain uncertainty for the characters but establish repeated observable cause/effect for readers. Risk: deliberate ambiguity must still avoid arbitrary exceptions.

Uncertainty: Chapter 1 still reaches 12:07. Its flickers and painful touch are not evidence of a shortened first meeting.

Adaptation impact: Clock inserts must distinguish elapsed time from lost capacity.

Dependencies: SMA-ISS-008, SMA-ISS-010

## SMA-ISS-010: Calendar progression and the fire deadline are not yet specified

Priority: P1 | Category: timeline | Severity: high | Confidence: 99%

Evidence class: unknown requiring decision. Status: open, awaiting review.

Tomas gives October 17, 1986, and Daniel gives only 2026. The opening says 11:41 PM but does not establish Daniel's calendar date. Notes describe both nightly recurrence and two specific nights; the fire's exact date and how successive meetings advance each era are unavailable.

Why it matters: The number of nights before the fire governs rescue urgency, chapter pacing, and whether a long serial can fit the story's clock.

Preserve: The forty-year separation and the opening's 12:00-to-12:07 experience.

Evidence:

- SRC-04 lines 29-29 (unit source-unit-7eabb1ef43df4d50b0662bf7b9d85ab3): "At 11:41 PM". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 167-167 (unit source-unit-4a59e04f57ae454cb2c6ba802a261d5a): "October seventeenth.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 173-173 (unit source-unit-0ae3d111405142f8bdd6b5180e4c6fac): "Twenty twenty-six". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-22 lines 22-22 (unit source-unit-c9eefe2e08ef4256a97c21345e869c3c): "It is a fragile wound between two specific nights.". Source: `README.md`.
- SRC-22 lines 40-51 (unit source-unit-6e81f10343fd4977bfd40faf49fa7087): "1. The abandoned railway cafe returns to life". Source: `README.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: first meeting: timeline-event-68f360f43d8a47ebb62965eff6732e6e; station fire: timeline-event-8f8c4b747b494551aa21f1af3bd64e6b; Cafe Siete: location-ec00909b6a1244d0ae35b1f2881055a5

Possible solutions and tradeoffs:

1. Choose paired advancing dates and a defined private fire deadline. Risk: imposes a finite timeline and constrains expansion.
2. Use deliberately repeated or nonconsecutive past nights, with a consistent mapping rule. Risk: substantially increases reader load and reconstruction scope.

Uncertainty: Do not assume October 17, 2026, an October 17 fire, or equal date advancement. A year offset alone does not establish exact elapsed days.

Adaptation impact: Every future page needs explicit era/date state where chronology matters.

Dependencies: No prerequisite finding.

## SMA-ISS-011: Daniel knows the exact past year before receiving evidence

Priority: P2 | Category: character_knowledge | Severity: medium | Confidence: 95%

Evidence class: point-of-view interpretation risk. Status: open, awaiting review.

Before Tomas states the year, the close Daniel narration says the kitchen lived in 1986 and that he knew it before proof. His archives are from 1986, but the visible cafe details do not uniquely establish that year.

Why it matters: A protagonist defined by evidence loses some credibility when precise knowledge arrives as certainty without a marked intuition.

Preserve: Daniel's expertise and the uncanny feeling that the archive has become alive.

Evidence:

- SRC-04 lines 133-133 (unit source-unit-96fe1374a74447fdbfcf5f4130141f39): "Behind the man, the kitchen lived in 1986.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 167-167 (unit source-unit-4a59e04f57ae454cb2c6ba802a261d5a): "Nineteen eighty-six". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047

Possible solutions and tradeoffs:

1. Frame 1986 as a hypothesis tied to the archive, then let Tomas verify it. Risk: slightly softens the lyrical certainty.
2. Keep the intuition as a deliberate supernatural symptom with later accountable payoff. Risk: adds a new ability or mystery requiring approval.

Uncertainty: This may be expressive narration rather than literal knowledge; revise only if the intended viewpoint is strict close third.

Adaptation impact: Use an inference caption only if needed; avoid presenting guessed dates as proven visual labels.

Dependencies: SMA-ISS-010

## SMA-ISS-012: The white suit attracts investigative focus without a stated link

Priority: P2 | Category: causality | Severity: medium | Confidence: 90%

Evidence class: under-motivated inference. Status: open, awaiting review.

Daniel singles out the white suit from a list that also includes a failed signal. The opening evidence contains no stated white-suit connection, and Page 11 labels the broker as a suspect or important clue.

Why it matters: A fair investigation benefits from a reason for choosing one lead; otherwise the narrative appears to identify the antagonist for Daniel.

Preserve: Tomas's observant humor and Daniel missing the compliment while investigating.

Evidence:

- SRC-04 lines 375-375 (unit source-unit-51de7067630a4133ae844dc5ec6a75c6): "A broker in a white suit bought coffee and did not drink it.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 379-379 (unit source-unit-94d295c33da3497b95dfb8f6684e50ee): "White suit?". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-15 lines 38-41 (unit source-unit-f139bfa0f995484b9c3ad78105d2e6a8): "Daniel's pencil stopping over the notebook". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-011-chatgpt-image-prompt.md`.
- SRC-15 lines 50-51 (unit source-unit-0fcc9b562d104ede81866874cfe563b1): "a suspect or important clue". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-011-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; Arturo Salcedo: character-28e7610c7be1473aa1d5fb041293cf19

Possible solutions and tradeoffs:

1. Supply a small existing-record connection before Daniel focuses on the suit. Risk: extra opening information may telegraph the suspect.
2. Let Daniel ask neutrally about both the broker and signal, with suspicion emerging from later corroboration. Risk: slightly longer exchange.

Uncertainty: A conservator can follow a hunch; this is a motivation-strengthening opportunity, not proof of impossible knowledge.

Adaptation impact: Avoid villain framing that resolves the mystery before evidence does.

Dependencies: SMA-ISS-003, SMA-ISS-010

## SMA-ISS-013: Page 14 overstates what the final warning proves

Priority: P1 | Category: character_knowledge | Severity: high | Confidence: 98%

Evidence class: confirmed script-evidence mismatch. Status: open, awaiting review.

Page 14 says Daniel found a warning the official archive did not contain and depicts the moment as a murder mystery. The opening archive already places the fire in the service corridor. The new fact is the scratched warning's form, apparent age, and proximity to TOMAS, not a new corridor location or confirmed murder.

Why it matters: The ending should escalate the right question without granting Daniel knowledge of Tomas's death or targeted arson before he has it.

Preserve: The transition from intimate proof to danger and the scratch beneath Tomas's name.

Evidence:

- SRC-04 lines 23-23 (unit source-unit-f382583d75f74c52bc81bd180b8afc0c): "The station fire report listed an electrical fault in a service corridor". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 469-469 (unit source-unit-c6a7150ac9fc488e9cad4e9e0e6d5390): "FIRE STARTS IN THE SERVICE CORRIDOR.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-18 lines 39-42 (unit source-unit-8dafc6b074474224ae40f2216cc018a3): "the moment the romance becomes a murder mystery.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-014-chatgpt-image-prompt.md`.
- SRC-18 lines 44-45 (unit source-unit-62fbfeef126c40af85cd77cdb65622ed): "a warning that the official archive did not contain.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-014-chatgpt-image-prompt.md`.
- SRC-22 lines 55-69 (unit source-unit-6f5031c922c4452aa2067c70e55cc052): "3. The Baker In The Newspaper Photograph". Source: `README.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; station fire: timeline-event-8f8c4b747b494551aa21f1af3bd64e6b

Possible solutions and tradeoffs:

1. Clarify that the warning makes the known fire personal and suspicious; save proof of death and intent for later evidence. Risk: less overt murder language.
2. Add a precise discrepancy between the archive and the scratch in a future revision. Risk: introduces a new clue that must be approved and tracked.

Uncertainty: The literal scratched imperative is new; the location is not. Death and arson remain planned revelations, not proved Chapter 1 facts.

Adaptation impact: Caption, expression direction, and later reveal order must agree.

Dependencies: SMA-ISS-004, SMA-ISS-012

## SMA-ISS-014: The late-night site visit needs a specific practical reason

Priority: P2 | Category: character_motivation | Severity: medium | Confidence: 86%

Evidence class: plausibility opportunity. Status: open, awaiting review.

Daniel has permits and an archive assignment, but his choice to inspect the damaged station alone at 11:41 PM has no concrete deadline, access constraint, or immediate objective beyond inventory.

Why it matters: One purposeful reason would make the opening encounter feel caused by his choices rather than a convenient appointment with the premise.

Preserve: The permitted professional visit, institutional satire, and Daniel's stubborn dedication.

Evidence:

- SRC-04 lines 19-19 (unit source-unit-dbb9308fb67a48f58755bcce1a647b1d): "The mayor wanted a clean display case before demolition began.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 29-29 (unit source-unit-7eabb1ef43df4d50b0662bf7b9d85ab3): "At 11:41 PM". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-06 lines 25-28 (unit source-unit-890f3d3dbe4e4d17b9be981bbe55b47a): "an authorized side entrance with permit folder". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-002-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; San Aurelio Junction: location-e3d6a8be72a14872bb4be3930a5ac297

Possible solutions and tradeoffs:

1. Establish a time-limited access or evidence-preservation reason. Risk: invented operational detail needs approval.
2. Make his deliberate after-hours return an emotionally meaningful rule break with later consequences. Risk: changes his professional characterization.

Uncertainty: No real-world workplace rule has been researched; this is narrative motivation, not a safety or professional-practice verdict.

Adaptation impact: A short visual objective may replace additional exposition.

Dependencies: No prerequisite finding.

## SMA-ISS-015: Tomas's independent want is less developed than his rescue function

Priority: P2 | Category: character_arc | Severity: medium | Confidence: 90%

Evidence class: forward-looking characterization gap. Status: open, awaiting review.

Tomas acts in Chapter 1: he offers bread, asks for a return object, and agrees to meet again. The reference emphasizes his warmth, concealed loneliness, and status as a target, but gives no concrete personal goal that can conflict with Daniel's rescue plan.

Why it matters: A long romance needs Tomas to make consequential choices beyond being loved, endangered, or saved.

Preserve: His initiative, competence, teasing, chosen family, and bravery under fear.

Evidence:

- SRC-04 lines 295-295 (unit source-unit-f0597e48a8be47c3a974a10d566c25ed): "Can you send something back?". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-23 lines 40-48 (unit source-unit-5888edaed49c4018a8c24e3a92e27e33): "- Story Function: Gives the cafe its warmth". Source: `characters.md`.
- SRC-23 lines 83-90 (unit source-unit-9141d784709e4c64b0abf146cf304a7a): "- Story Function: May have arranged the fire". Source: `characters.md`.
- SRC-23 lines 104-109 (unit source-unit-144f49412c82492490b20c90016aa5ed): "- Tomas's central fear:". Source: `characters.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Tomas Rivera: character-a096cba8416847d4947a94012733a09b; Lilia Ramos: character-3f6621b20e6e4c0da53cb42678b5c277

Possible solutions and tradeoffs:

1. Develop an independent obligation or goal from the cafe and notebook material, allowing Tomas to reject a rescue method. Risk: adds plot work and must be approved.
2. Keep the scope intimate and build his arc through choices about trust, disclosure, and Lilia. Risk: may not support the proposed 105 chapters.

Uncertainty: One opening chapter need not complete his arc; the gap concerns architecture for continuation, not absence of all agency.

Adaptation impact: Give Tomas observable decisions and work outside Daniel's gaze in later approved scripts.

Dependencies: SMA-ISS-010

## SMA-ISS-016: Daniel's emotional need is suggested, while specific grief is unknown

Priority: P2 | Category: character_arc | Severity: medium | Confidence: 91%

Evidence class: interpretation requiring author choice. Status: open, awaiting review.

Daniel trusts paper more than people, presents I am real, and fears losing the encounter. Notes prescribe adults carrying grief but supply no event explaining his isolation or a particular bereavement.

Why it matters: Reconstruction could accidentally invent trauma or reduce his growth to receiving romance. His conflict between preserving evidence and accepting a living person's agency is already stronger material.

Preserve: Emotional caution, tactile care, dry humor, and tenderness leaking through professional ritual.

Evidence:

- SRC-04 lines 11-11 (unit source-unit-3392356bfe1d40a1b1b44ed2fd61fc05): "Daniel Soriano trusted paper more than people.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 333-333 (unit source-unit-94c332b10eb844fa997807816f048e4a): "Daniel wished he had written something better.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-23 lines 28-36 (unit source-unit-b1183dd2a0d84313bb026002ba5fe572): "- Personality: Patient, precise, lonely without admitting it". Source: `characters.md`.
- SRC-22 lines 18-18 (unit source-unit-d08690c6fb8d4de29f2810f3fead91b7): "adults carrying grief quietly". Source: `README.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; Tomas Rivera: character-a096cba8416847d4947a94012733a09b

Possible solutions and tradeoffs:

1. Build his need around relinquishing control and treating Tomas as a partner; leave personal history understated. Risk: interior change requires precise behavioral beats.
2. Approve a specific grief history and connect it sparingly to present choices. Risk: risks formulaic backstory and extra exposition.

Uncertainty: Distrust, loneliness, fear of impermanence, and need for connection are interpretations; no deceased lover or family trauma is canon.

Adaptation impact: Preserve the note and hand acting; do not replace them with explanatory flashbacks by default.

Dependencies: SMA-ISS-015

## SMA-ISS-017: Supporting-cast secrets are promises rather than causal architecture

Priority: P2 | Category: character_motivation | Severity: medium | Confidence: 94%

Evidence class: outline incompleteness. Status: open, awaiting review.

Maribel will notice changing records, Lilia may hide an object, Benjamin leaves conflicting testimony, Ernesto misremembers, and Arturo may have arranged arson. The notes do not yet connect their specific knowledge, choices, incentives, and costs.

Why it matters: A conspiracy sustained by several witnesses needs distinct reasons for silence and action, rather than successive information dispensers.

Preserve: Institutional competence, chosen family, compromised ordinary people, and human financial motives.

Evidence:

- SRC-23 lines 52-59 (unit source-unit-ef0c08b70b944fdab7c05c64f096f99a): "- Story Function: Helps Daniel access restricted records". Source: `characters.md`.
- SRC-23 lines 63-69 (unit source-unit-a658f681501f4433bf5a58cc3078ab06): "- Story Function: Knows what Tomas was carrying". Source: `characters.md`.
- SRC-23 lines 73-79 (unit source-unit-8c6f6f47006d4208b403c2bdf6482ed3): "- Story Function: Patrols the station the night of the fire". Source: `characters.md`.
- SRC-23 lines 94-100 (unit source-unit-3be3fd6c4a524ede888f14bfa365026c): "- Story Function: Connects the fire to tampered platform signals". Source: `characters.md`.
- SRC-23 lines 83-90 (unit source-unit-9141d784709e4c64b0abf146cf304a7a): "- Story Function: May have arranged the fire". Source: `characters.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Maribel Santos: character-eac21dd0fae140d0b5fc6cd85bbbac0c; Lilia Ramos: character-3f6621b20e6e4c0da53cb42678b5c277; Benjamin Manalo: character-457a700f0c6c478fb525eb3fb81f30a3; Ernesto Galang: character-073f27ce849748799a3a2ed06dabc898; Arturo Salcedo: character-28e7610c7be1473aa1d5fb041293cf19

Possible solutions and tradeoffs:

1. Build a knowledge-and-cost matrix before outlining later investigations. Risk: requires consequential secrets to be decided.
2. Use only the witnesses needed for a focused first arc and defer expansion. Risk: reduces the breadth implied by the long-series plan.

Uncertainty: Only Maribel in narrated background, Lilia's voice, and Arturo by report occur in the supplied chapter; later execution cannot be judged.

Adaptation impact: Future dialogue and flashback ownership depend on who actually witnessed each fact.

Dependencies: SMA-ISS-003, SMA-ISS-010, SMA-ISS-015

## SMA-ISS-018: The roadmap risks repeating clues already established

Priority: P1 | Category: setup_payoff | Severity: high | Confidence: 94%

Evidence class: serialization risk. Status: open, awaiting review.

Chapter 1 already ages a pastry and shows falsified-looking records. Chapter 5 is titled The Pastry That Aged Forty Years; Arc 2 again promises evidence of falsified fire records. Arc 1 includes The Man Who Bought The Station Fire and a burning-twice climax, while Arc 3 revisits the man behind the fire and Arc 6 the repeating year.

Why it matters: Repeated discoveries can reset progress unless later versions change a meaningful state or reinterpret earlier evidence.

Preserve: Recurring object motifs and layered discoveries with emotional consequences.

Evidence:

- SRC-04 lines 275-275 (unit source-unit-2d8f06e1bdef4346aab4238dd62b53b5): "By the time Daniel lifted it, the roll was forty years old.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 23-23 (unit source-unit-f382583d75f74c52bc81bd180b8afc0c): "Witness statements from 1986 had been copied twice". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-24 lines 56-70 (unit source-unit-1db292e5fb9f45bf941dd8e12d59c606): "5. The Pastry That Aged Forty Years". Source: `series-plan.md`.
- SRC-24 lines 20-28 (unit source-unit-b339228c4e4d4b7380f13c1d8c079cfe): "Deepen the romance through letters". Source: `series-plan.md`.
- SRC-24 lines 20-28 (unit source-unit-b339228c4e4d4b7380f13c1d8c079cfe): "Expand the arson plot into railway officials". Source: `series-plan.md`.
- SRC-24 lines 20-28 (unit source-unit-b339228c4e4d4b7380f13c1d8c079cfe): "1986 begins repeating in fragments". Source: `series-plan.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: aged pastry: prop-d12d36e4106949ac8be1873a74057a59; station fire: timeline-event-8f8c4b747b494551aa21f1af3bd64e6b

Possible solutions and tradeoffs:

1. Assign each planned return a distinct state change, such as proving custody or overturning a prior inference. Risk: requires a rigorous revelation ladder.
2. Compress or combine redundant planned beats while retaining their best imagery. Risk: alters the preferred chapter count and needs approval.

Uncertainty: Titles are not scenes; repetition is a planning risk, not proof that unwritten chapters contain filler.

Adaptation impact: Later visual echoes should communicate a new consequence, not merely repeat the same transformation.

Dependencies: SMA-ISS-008, SMA-ISS-009, SMA-ISS-010, SMA-ISS-017

## SMA-ISS-019: The 105-chapter commitment is not supported by developed beats or capacity evidence

Priority: P1 | Category: pacing | Severity: high | Confidence: 99%

Evidence class: scope and reader hypothesis. Status: open, awaiting review.

The series plan recommends seven equal fifteen-chapter arcs and possible expansion to 150 chapters. The available story is one drafted chapter; no scene-level long-series architecture, production capacity, reader feedback, or release calendar is supplied.

Why it matters: A numeric target can force delay in the central rescue question and create an unsustainable commitment before the story has earned the length.

Preserve: Long-term creative ambition and Daniel/Tomas as the emotional center.

Evidence:

- SRC-24 lines 11-14 (unit source-unit-f30646eb347344a3a21c4ad70a854cac): "- Total chapters: 105". Source: `series-plan.md`.
- SRC-24 lines 11-14 (unit source-unit-f30646eb347344a3a21c4ad70a854cac): "- Average arc length: 15 chapters". Source: `series-plan.md`.
- SRC-24 lines 32-32 (unit source-unit-fd5e2f3e462c488695531adfb06d281a): "expand toward 120-150 chapters". Source: `series-plan.md`.
- SRC-24 lines 72-72 (unit source-unit-fd4b381915aa4900b50bcbce3816d6c8): "Arc 1 is the opening season and should remain compact at 15 chapters.". Source: `series-plan.md`.

Affected manuscript chapter IDs: None; whole-outline or workflow scope.

Affected scene IDs: None; future scenes are not invented.

Related entity IDs: connection cost: plot-thread-0289f530f9af462cb23c4cf0ccdb6efd

Possible solutions and tradeoffs:

1. Treat Arc 1 as a provisional season envelope and validate a small opening sequence before committing beyond it. Risk: changes expectations about the 105-chapter target.
2. Retain 105 as an aspiration but require each arc to justify new conflict, relationship development, and capacity. Risk: substantial planning burden before release.

Uncertainty: No market demand, paid schedule, or author capacity has been validated. No claim that a shorter series sells better is made.

Adaptation impact: Page count and release frequency remain provisional until production timing and reader checks exist.

Dependencies: SMA-ISS-001, SMA-ISS-010, SMA-ISS-018

## SMA-ISS-020: Other cafes could dilute the specific place and relationship

Priority: P2 | Category: world_rule_continuity | Severity: medium | Confidence: 91%

Evidence class: creative-promise tension. Status: open, awaiting review.

The premise calls the cafe a fragile connection between two specific nights. Arc 4 proposes other seven-minute crossings at abandoned railway sites without a rationale that connects them to Daniel and Tomas's choices.

Why it matters: Expansion can replace a singular romance mystery with repeatable location cases and weaken the intimacy that differentiates the premise.

Preserve: San Aurelio Junction as a physical place, emotional anchor, and civic-history mystery.

Evidence:

- SRC-22 lines 22-22 (unit source-unit-c9eefe2e08ef4256a97c21345e869c3c): "It is a fragile wound between two specific nights.". Source: `README.md`.
- SRC-24 lines 20-28 (unit source-unit-b339228c4e4d4b7380f13c1d8c079cfe): "Reveal other seven-minute crossings at abandoned railway sites". Source: `series-plan.md`.
- SRC-24 lines 36-39 (unit source-unit-65ed5ecd8c9341f49ce8eb1b1dd12d83): "one or two other railway cafes with separate emotional cases.". Source: `series-plan.md`.

Affected manuscript chapter IDs: None; whole-outline or workflow scope.

Affected scene IDs: None; future scenes are not invented.

Related entity IDs: Cafe Siete: location-ec00909b6a1244d0ae35b1f2881055a5

Possible solutions and tradeoffs:

1. Make any other crossing directly test or threaten an established rule of Daniel and Tomas's connection. Risk: requires broader mythology and careful restraint.
2. Defer or remove the multi-cafe expansion from the preferred reconstruction option. Risk: narrows the planned world and total length.

Uncertainty: Plural crossings are not inherently contradictory; their relevance and mechanism are simply unbuilt.

Adaptation impact: Do not commission new location references before the expansion decision.

Dependencies: SMA-ISS-009, SMA-ISS-010, SMA-ISS-019

## SMA-ISS-021: Memory-loss and repeat-year arcs need persistent consequences

Priority: P2 | Category: relationship_continuity | Severity: medium | Confidence: 92%

Evidence class: future relationship risk. Status: open, awaiting review.

Arc 5 has Tomas no longer remember Daniel clearly, Arc 6 repeats fragments of 1986, and the final arc again asks which future can survive. Without persistent changes, these devices may repeatedly undo earned intimacy.

Why it matters: Readers investing in small trust-building acts need those acts to matter even when memory becomes unreliable.

Preserve: The cost of rescue and the question of what survives in objects, choices, and relationships.

Evidence:

- SRC-24 lines 20-28 (unit source-unit-b339228c4e4d4b7380f13c1d8c079cfe): "Tomas no longer remembers him clearly". Source: `series-plan.md`.
- SRC-24 lines 20-28 (unit source-unit-b339228c4e4d4b7380f13c1d8c079cfe): "1986 begins repeating in fragments". Source: `series-plan.md`.
- SRC-22 lines 40-51 (unit source-unit-6e81f10343fd4977bfd40faf49fa7087): "may lose every memory made there.". Source: `README.md`.

Affected manuscript chapter IDs: None; whole-outline or workflow scope.

Affected scene IDs: None; future scenes are not invented.

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; Tomas Rivera: character-a096cba8416847d4947a94012733a09b; notebook reply: prop-1461014f20054066aa266d61a245d1b6

Possible solutions and tradeoffs:

1. Define which consequences and choices survive each alteration; protect Tomas's agency in re-consent. Risk: requires a demanding continuity ledger.
2. Use one decisive memory rupture near the climax rather than repeated resets. Risk: changes the seven-arc architecture.

Uncertainty: No completed reset scene exists; this is a preemptive test for the outline, not a diagnosed reader response.

Adaptation impact: Visual motifs can preserve recognition, but must not replace freely made relationship choices.

Dependencies: SMA-ISS-009, SMA-ISS-010, SMA-ISS-015, SMA-ISS-018

## SMA-ISS-022: Legacy full-page prompts conflict with the requested future production contract

Priority: P1 | Category: manga_adaptation_risk | Severity: high | Confidence: 100%

Evidence class: confirmed workflow incompatibility. Status: open, awaiting review.

Existing prompts request whole pages with gutters, dialogue, captions, and SFX inside generated images. The current request requires structured versioned jobs, panel artwork without lettering or borders, and separate approved downstream composition.

Why it matters: Using these legacy prompts as ready jobs would bypass the user's approval and reference requirements and embed text that should be independently editable.

Preserve: The existing scripts as immutable adaptation evidence and their strong event choices.

Evidence:

- SRC-21 lines 48-48 (unit source-unit-6d6d0dba516648269858f5b36244eec1): "The prompt may request readable speech bubbles, captions, SFX". Source: `Comics/style-guide.md`.
- SRC-20 lines 67-84 (unit source-unit-3c7f309a04e54097aa6a0b0e71a25560): "Keep the actual panel script, dialogue, captions". Source: `Comics/README.md`.
- SRC-05 lines 21-22 (unit source-unit-045985d3675748a19b198d373c8bd9c1): "Create one vertical manga/manhwa page with clean gutters and 5 panels.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-001-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: None.

Possible solutions and tradeoffs:

1. After story/storyboard approval, translate scripts into panel jobs plus separate lettering and composition data. Risk: more preproduction work, but supports traceable changes.
2. Retain legacy prompts as historical notes and rebuild the approved storyboard from prose. Risk: may discard useful existing layout effort.

Uncertainty: This is a conflict with the new requested workflow, not evidence that artwork has been generated or that old prompts were once approved.

Adaptation impact: No legacy prompt is released as a production job in this audit.

Dependencies: SMA-ISS-002, SMA-ISS-003, SMA-ISS-004, SMA-ISS-005, SMA-ISS-013

## SMA-ISS-023: Visual reference fallback lacks approved hash-locked assets

Priority: P1 | Category: manga_adaptation_risk | Severity: high | Confidence: 100%

Evidence class: confirmed readiness gap. Status: open, awaiting review.

Page 1 allows the prompt itself to be a primary visual lock when no images exist. Later pages conditionally attach earlier WebP outputs. No such assets or reference approvals are present in the root.

Why it matters: A prose description or a filename mentioned in a prompt does not establish an approved, consistent visual reference.

Preserve: Explicit adult ages, occupational silhouettes, differentiated hair, hands, props, and grounded station design.

Evidence:

- SRC-05 lines 8-10 (unit source-unit-c8b3f5f93e994148b9c37a42523de881): "If no Seven Minutes images exist yet". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-001-chatgpt-image-prompt.md`.
- SRC-06 lines 3-3 (unit source-unit-f5e529c130604b9791425c0f95b9024b): "If `1.webp` exists". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-002-chatgpt-image-prompt.md`.
- SRC-03 lines 11-12 (unit source-unit-743fde63b031408a9204415a5c1851b0): "If approved pages already exist". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter-01-front-cover-chatgpt-image-prompt.md`.
- SRC-19 lines 8-9 (unit source-unit-d77a72566c874802bd931022316e75b7): "16 WebP reader assets present". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/README.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; Tomas Rivera: character-a096cba8416847d4947a94012733a09b; Cafe Siete: location-ec00909b6a1244d0ae35b1f2881055a5

Possible solutions and tradeoffs:

1. At the authorized production stage, create reference jobs first and block dependent jobs until approved hash-locked images are supplied. Risk: adds a reference approval round.
2. Prepare only deferred structured job specifications until references exist. Risk: cannot release executable panel handoffs yet.

Uncertainty: Conditional legacy filenames are not actual image paths, and text headed Lock does not create a Manga Studio approval.

Adaptation impact: Every eventual handoff needs an exact ordered attachment checklist built from real approved assets.

Dependencies: SMA-ISS-001, SMA-ISS-022

## SMA-ISS-024: Page counts and reading sequence do not yet express event priorities

Priority: P2 | Category: pacing | Severity: medium | Confidence: 98%

Evidence class: adaptation layout risk. Status: open, awaiting review.

All fourteen page prompts use five or six panels, totaling 75. Page 8 packs painful touch, a moving window, a joke, a pastry crossing, aging, and both reactions into six panels. No explicit reading direction, panel geometry, or dialogue-safe zones is supplied.

Why it matters: The key miracle and emotional turns may have insufficient space, and a numbered script alone does not resolve a composed page's reading path.

Preserve: Archive-to-miracle escalation, the first touch, I am real, and the final warning.

Evidence:

- SRC-12 lines 17-18 (unit source-unit-052743cf2c3d4756ad6122b75f7510ef): "Create one vertical page with 6 panels.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md`.
- SRC-12 lines 38-41 (unit source-unit-ae72db5bee8345dca0691d2674b77391): "PANEL 5 - FORTY YEARS TAKE IT". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md`.
- SRC-21 lines 43-43 (unit source-unit-6df398f004304777b8e470c2bb25619e): "Do not mechanically reuse the same page grid.". Source: `Comics/style-guide.md`.
- SRC-16 lines 47-50 (unit source-unit-f218eccf3399448a912632e91da70b34): "PANEL 6 - FINGERS THROUGH WINDOW". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-012-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: service window: prop-ce6d2b5f51db4da0a3de67a809c13925; aged pastry: prop-d12d36e4106949ac8be1873a74057a59

Possible solutions and tradeoffs:

1. Rebalance the same events into a varied event-driven page plan, giving transformations and reactions room. Risk: page count may change.
2. Keep fourteen pages provisionally but trim or redistribute dialogue and establish exact reading sequences. Risk: significant compression may flatten banter.

Uncertainty: No rendered pages exist, so actual readability, overlap, and artistic quality cannot be scored.

Adaptation impact: Future nemu should be geometry-only, with one dominant event per panel and motivated shot changes.

Dependencies: SMA-ISS-004, SMA-ISS-005, SMA-ISS-022

## SMA-ISS-025: Compressed dialogue drops connective questions and one key clue

Priority: P2 | Category: dialogue_voice | Severity: medium | Confidence: 96%

Evidence class: confirmed adaptation omissions with interpretive impact. Status: open, awaiting review.

Page 6 jumps from Museum conservator to Possessed and then the year without the prose's year question and defensive exchange. Page 7 begins Your side without its original prompting line. Page 11 omits the failed southbound signal while isolating the broker.

Why it matters: Compression can preserve quoted lines while losing conversational logic and narrowing a mystery's evidence unfairly.

Preserve: Dry reciprocal humor and the contrast between Daniel's literal responses and Tomas's hospitality.

Evidence:

- SRC-04 lines 141-141 (unit source-unit-20310901061c4d7bbed8f596485c1435): "What year is it?". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-10 lines 30-35 (unit source-unit-6f8b6b55d3cc49669f1b327417008462): "PANEL 3 - POSSESSED?". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-006-chatgpt-image-prompt.md`.
- SRC-10 lines 42-45 (unit source-unit-065ca125d8d84087969c095e88c4ed8a): "PANEL 5 - TOMAS STATES HIS YEAR". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-006-chatgpt-image-prompt.md`.
- SRC-11 lines 23-26 (unit source-unit-43423d7eeb1e4b74a3edc69c2d8b1a87): "YOUR SIDE.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-007-chatgpt-image-prompt.md`.
- SRC-04 lines 375-375 (unit source-unit-51de7067630a4133ae844dc5ec6a75c6): "The southbound signal failed.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-15 lines 33-36 (unit source-unit-5c03bda7ca2c48489c8d89e22e416c8c): "PANEL 3 - WHITE SUIT". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-011-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; Tomas Rivera: character-a096cba8416847d4947a94012733a09b; Arturo Salcedo: character-28e7610c7be1473aa1d5fb041293cf19

Possible solutions and tradeoffs:

1. Restore only the short connective lines and signal clue needed for causality. Risk: lettering requires space checks.
2. Rewrite approved dialogue for the compressed page structure while retaining distinct voices. Risk: literal favorite lines may need to move or change.

Uncertainty: Some abruptness could read as nervous humor; test the complete lettered sequence after storyboard approval.

Adaptation impact: Do not restore every prose line indiscriminately; protect cause, response, and voice.

Dependencies: SMA-ISS-004, SMA-ISS-012, SMA-ISS-024

## SMA-ISS-026: Clock, flashlight, and costume details drift across production notes

Priority: P2 | Category: prop_continuity | Severity: medium | Confidence: 98%

Evidence class: confirmed reference mismatch and unstaged transitions. Status: open, awaiting review.

The cafe clock is above the door in prose and Page 4 but above the menu board in characters.md; a separate station clock exists. The prose drops the flashlight at 12:04, but Page 10 omits that beat and Page 13 places it on the floor. Tomas's reference specifies a short-sleeved shirt while prose repeatedly describes sleeves rolled to the elbows.

Why it matters: Small physical inconsistencies become repeated visual errors when prompts are used as independent production instructions.

Preserve: Two distinct clocks, Daniel's work props, and Tomas's practical rolled-sleeve silhouette.

Evidence:

- SRC-04 lines 71-71 (unit source-unit-c4d78a6b615d4de1a6019aa0aaf3e91b): "Above the cafe door". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-23 lines 113-122 (unit source-unit-f9cfce8b95e14151aaa3337d3ed5e67a): "- Cafe Clock: Brass-rimmed wall clock above the menu board.". Source: `characters.md`.
- SRC-04 lines 343-343 (unit source-unit-aa1c7fdc85ce443aa57f677c554d200f): "Daniel's flashlight rolled off the counter". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-17 lines 28-31 (unit source-unit-513c2e9096e34fd4be066cc51342ab6b): "His flashlight lies on the floor.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-013-chatgpt-image-prompt.md`.
- SRC-23 lines 40-48 (unit source-unit-5888edaed49c4018a8c24e3a92e27e33): "Wears a cream short-sleeved 1980s cafe shirt". Source: `characters.md`.
- SRC-04 lines 91-91 (unit source-unit-fb0ddbd964bf421b928b59d42406d895): "His cream cafe shirt was rolled to the elbows". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: cafe clock: prop-2feac2a1d9fd42e6975c1ed120a2e16a; station clock: prop-abfd3210cb6e4133ab15d662bd6aa138; flashlight: prop-67b953d0295447f788ff0fb7cf202823; Tomas Rivera: character-a096cba8416847d4947a94012733a09b

Possible solutions and tradeoffs:

1. Approve a prop and costume state sheet and stage needed transitions in revised scripts. Risk: small panel adjustments.
2. Choose one consistent depiction for each ambiguity and mark symbolic covers separately from literal scene continuity. Risk: requires explicit decisions rather than treating all descriptions as compatible.

Uncertainty: Door and menu board might be colocated, and sleeves might be unusually long; the missing specification is the problem. No rendered error is claimed.

Adaptation impact: Reference and panel plans must distinguish clock identities and current prop custody.

Dependencies: SMA-ISS-005, SMA-ISS-023

## SMA-ISS-027: SFX are text tokens rather than complete sound instructions

Priority: P2 | Category: manga_adaptation_risk | Severity: medium | Confidence: 100%

Evidence class: confirmed specification gap. Status: open, awaiting review.

The scripts include DRIP, KREEEAK, CLICK, FWOOM, CLINK, TICK, ZZT, CLACK, KRRK, WHUMP, FSSHT, and SSHHH, but do not consistently specify source, reader meaning, intensity, language, translation context, and lettering intent. Page 7 places TICK with a coffee-ring image rather than an explicit clock shot.

Why it matters: Unclear sound ownership can make supernatural mechanics resemble electricity or turn paper release into another portal opening.

Preserve: Rain, clock ticks, cafe machinery, and the sharp loss of inhabited sound at closure.

Evidence:

- SRC-11 lines 28-31 (unit source-unit-be91f31d1c8f405ba1c57b6fe58d8d56): "TICK". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-007-chatgpt-image-prompt.md`.
- SRC-12 lines 20-23 (unit source-unit-a0d3641d00b746b0824cb6370ffa1f85): "ZZT". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-008-chatgpt-image-prompt.md`.
- SRC-17 lines 33-36 (unit source-unit-998274dcd23f4fac9c6c695880e41639): "FSSHT". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-013-chatgpt-image-prompt.md`.
- SRC-08 lines 29-32 (unit source-unit-5832d974b8a743f9adc6c79fa5b8ef01): "FWOOM". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-004-chatgpt-image-prompt.md`.
- SRC-18 lines 30-33 (unit source-unit-1d23dae938ed4113bb566d02a103677e): "SSHHH". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-014-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: cafe clock: prop-2feac2a1d9fd42e6975c1ed120a2e16a; service window: prop-ce6d2b5f51db4da0a3de67a809c13925

Possible solutions and tradeoffs:

1. Map each sound to a physical or deliberately subjective source and separate it from artwork jobs. Risk: a few legacy tokens may need replacement.
2. Favor silence for uncertain supernatural beats and retain only literal environment sounds. Risk: may reduce the intended impact of transformation.

Uncertainty: English output is requested; Tiya and pan de leche are cultural terms, not untranslated SFX. Their meaning should be conveyed contextually.

Adaptation impact: Structured SFX and lettering belong to later approved preproduction, not image generation during this audit.

Dependencies: SMA-ISS-005, SMA-ISS-007, SMA-ISS-022

## SMA-ISS-028: Repeated hair and figurative beats can compete with the countdown

Priority: P3 | Category: exposition | Severity: low | Confidence: 84%

Evidence class: editorial interpretation. Status: open, awaiting review.

The chapter repeatedly notes Tomas's fallen hair and pairs many emotional or sensory beats with figurative interpretation. This establishes a recognizable voice, but some repetition can slow a seven-minute scene or become redundant when drawn.

Why it matters: Selective trimming could preserve the strongest images and give reactions more room without flattening the author's style.

Preserve: Paper lied less often; collapse by etiquette; bread turning elderly; practical hair movement; tenderness through objects.

Evidence:

- SRC-04 lines 209-209 (unit source-unit-137fe2fa314f4e89a676164f90e2ff4a): "one dark strand fell across his lips.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 329-329 (unit source-unit-4548ea5e2baa4f2e87525518fee26702): "The long strand of hair had fallen across his face again". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 357-357 (unit source-unit-2ca9a9cb924e45e98a3cc10163393759): "Long hair tied with green cord.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 371-371 (unit source-unit-764a4fbed7804de491e8b6742c714551): "Seven minutes was strange. Two minutes was a door closing.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Tomas Rivera: character-a096cba8416847d4947a94012733a09b; Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047

Possible solutions and tradeoffs:

1. Keep repetitions that change emotional meaning and trim only descriptive duplicates in a new version. Risk: over-editing can erase rhythm.
2. Preserve prose density but translate recurrent description into silent visual continuity. Risk: adaptation must replace narrator intimacy through acting.

Uncertainty: This is taste-sensitive. No supplied reader feedback establishes a pacing failure, and no wholesale style rewrite is recommended.

Adaptation impact: Avoid repeated hair-close-up panels unless the gesture marks a state change.

Dependencies: SMA-ISS-024

## SMA-ISS-029: Historical setting and reader-facing content boundaries remain provisional

Priority: P2 | Category: manga_adaptation_risk | Severity: medium | Confidence: 97%

Evidence class: research and audience unknown. Status: open, awaiting review.

The text uses Filipino-coded names, Tiya, pan de leche, municipal redevelopment, and 1986, while only Maribel is explicitly described as Filipina-Spanish. No country, city model, period-research dossier, formal rating, platform, or romance ending commitment is supplied.

Why it matters: An adaptation may otherwise invent period conditions, cultural assumptions, rating expectations, or a promised happy ending without author intent or evidence.

Preserve: Adult queer intimacy, ordinary work, chosen family, civic erasure, and cultural texture without reducing the setting to stereotypes.

Evidence:

- SRC-23 lines 28-36 (unit source-unit-b1183dd2a0d84313bb026002ba5fe572): "- Age: 36 in 2026.". Source: `characters.md`.
- SRC-23 lines 40-48 (unit source-unit-5888edaed49c4018a8c24e3a92e27e33): "- Age: 28 in 1986.". Source: `characters.md`.
- SRC-23 lines 52-59 (unit source-unit-ef0c08b70b944fdab7c05c64f096f99a): "Filipina-Spanish woman". Source: `characters.md`.
- SRC-04 lines 349-349 (unit source-unit-f62b2bab7db84973a6e2c7672c9a0d2f): "Tiya Lilia.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 375-375 (unit source-unit-51de7067630a4133ae844dc5ec6a75c6): "pan de leche". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-22 lines 20-20 (unit source-unit-ae6220b497b24b979891e3caa7fad4de): "Keep the romance emotionally adult and restrained.". Source: `README.md`.
- SRC-24 lines 20-28 (unit source-unit-b339228c4e4d4b7380f13c1d8c079cfe): "accepting a future neither timeline can fully keep.". Source: `series-plan.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-2f59e856c58d4d6db58d635cbc64e0bb, scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047; Tomas Rivera: character-a096cba8416847d4947a94012733a09b; Maribel Santos: character-eac21dd0fae140d0b5fc6cd85bbbac0c; San Aurelio Junction: location-e3d6a8be72a14872bb4be3930a5ac297

Possible solutions and tradeoffs:

1. Adopt a provisional mature-teen-and-adult suspense framing with non-graphic violence and restrained intimacy, and decide setting/ending boundaries before continuation. Risk: platform categories may differ.
2. Approve a specific setting and content brief, then separately authorize targeted historical and reader research. Risk: additional research and possible revision.

Uncertainty: BL is not itself a reason for an adult-only rating. No claims about real history, professional conservation accuracy, legal rights, market size, or accidental imitation are verified.

Adaptation impact: Treat country, architecture references, uniforms, rating, and marketing promise as decisions; do not fabricate reference images or research.

Dependencies: SMA-ISS-010, SMA-ISS-019

## SMA-ISS-030: The fire-warning scratch needs a fair evidence and custody trail

Priority: P2 | Category: setup_payoff | Severity: medium | Confidence: 94%

Evidence class: intentional mystery with payoff obligation. Status: open, awaiting review.

Daniel photographs the TOMAS scratch before the encounter. Later dust reveals FIRE STARTS IN THE SERVICE CORRIDOR beneath it. The current text does not establish whether the second line was physically obscured, newly changed, or present in the first photograph, and its author is unknown.

Why it matters: The original photograph is a natural test. Ignoring it could make the evidence-focused protagonist passive or allow a later solution to change the clue's origin retroactively.

Preserve: The scratched warning, tactile age, photo documentation, and ending dread.

Evidence:

- SRC-04 lines 45-45 (unit source-unit-f4f565dd8a764844a82dc82eb0425589): "He photographed the glass, logged the position". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 467-467 (unit source-unit-5baeaf5c38e0478c9ced56c85a719c75): "hidden until the dust shifted". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-04 lines 469-469 (unit source-unit-c6a7150ac9fc488e9cad4e9e0e6d5390): "FIRE STARTS IN THE SERVICE CORRIDOR.". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`.
- SRC-07 lines 30-31 (unit source-unit-e0006dc29ca94d3195e03a828273f675): "Daniel photographs the scratched name". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-003-chatgpt-image-prompt.md`.
- SRC-18 lines 30-33 (unit source-unit-1d23dae938ed4113bb566d02a103677e): "dust sliding down the glass beneath Tomas's name". Source: `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/page-014-chatgpt-image-prompt.md`.

Affected manuscript chapter IDs: chapter-fb585a7fd3e7450e936edbcfce992566

Affected scene IDs: scene-3b27382ec9a049e2acde70d7cf88fc10

Related entity IDs: door scratches: prop-3c56d67fe71743d58ecaf605e59e5c46; phone photograph: prop-0b3caadd963c437787cd95d5af12ca9e; Daniel Soriano: character-7aa0419823314e0787fe55c54aa83047

Possible solutions and tradeoffs:

1. Use the already-taken photograph as an early comparison and track the result before deciding the scratch's author. Risk: commits a branch of the time-change model.
2. Keep the photo inconclusive for a specific physical reason while Daniel tries another comparison. Risk: repeated convenient unreadability would frustrate the investigation.

Uncertainty: The scratch's author and date are intentional unknowns, not contradictions. No self-writing loop or future Daniel is inferred as canon.

Adaptation impact: Record precisely what the first photograph contains before any later image or dialogue reveals it.

Dependencies: SMA-ISS-006, SMA-ISS-010, SMA-ISS-013

