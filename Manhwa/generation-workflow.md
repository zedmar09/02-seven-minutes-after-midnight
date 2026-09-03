# Manhwa Generation Workflow

## Production Authority

`Manhwa/` is the sole active visual-production pipeline. Every active chapter is rebuilt from current story canon into continuous-scroll production authority. Retired page prompts are not generation targets.

Always binding:
- creator-only continuity under `Continuity/`
- active chapter story package and any chapter-local state-resolution addendum
- `style-guide.md`
- `lettering-sfx-guide.md`
- `seam-continuity-protocol.md`
- `vertical-scroll-layout-guide.md`
- `production-readiness-gate.md`

## Creator Continuity Inheritance — Mandatory

Before creating or generating a future chapter, inherit the exact relevant state from creator continuity.

For Arc 1 this includes at minimum:
- calendar/date state
- current connection duration and exact close time
- historical changes already settled
- Daniel/Tomas memory/knowledge state
- unresolved evidence and allowed reader interpretation
- temporal-object IDs/provenance
- current physical location of cross-era artifacts
- service-window/counter mechanics
- Cafe-clock versus station-clock identity
- conspiracy facts already revealed vs still creator-only

A chapter may not silently reset a cost, object, clue, date, or mystery answer because the previous chapter folder is absent.

## Required Canonicals

Recurring humans use approved canonical character WebPs under `Character-References/`.
Recurring locations use approved environment WebPs under `Environment-References/`.
Recurring plot-critical objects use approved object WebPs under `Object-References/`.

Generation may produce PNG locally, but only approved committed WebP is permanent repository authority.

Missing/stale/wrong-path/unapproved required WebP → STOP.

## Permanent Canon vs Previous Strip

Previous APPROVED strip controls temporary state only: pose, facing, gesture, held items, prop location, clock minute/second, era state, damage, food amount, open/closed state, emotional intensity, and seam continuity.

Previous strip never overrides creator story canon, face/hair/build, structural environment geometry, recurring-object construction, or object provenance.

## Cause → Action → Result

Every meaningful change must pass:
`START STATE → CAUSE → VISIBLE PHYSICAL ACTION → RESULT → END STATE THAT PERSISTS`

A camera cut may not hide teleportation, duplicate an object, swap hands, change era state, advance/rewind the clock, repair a broken prop, recover lost connection time, or silently reset a pose.

## Deterministic Single Mechanism

For continuity-critical actions choose one physical mechanism and carry it through the entire strip. Do not offer mutually incompatible alternatives in one prompt.

Examples already locked in Chapter 1:
- same pencil point chips but remains bluntly usable
- Daniel gloves remain on through active interval
- returned warning page is closing-boundary transit, not spontaneous duplication
- Cafe clock resets/counts; station clock does not

## Mandatory Action Proof

When an action establishes story evidence, show enough contact/source/result to prove it. Examples for this story:
- Daniel retrieves the brass token from beneath the counter
- both men catch the same tray edge
- unstable contact occurs at the shared counter
- service window opens
- Tomas moves one saucer/pastry across the window
- that same saucer/pastry visibly ages in 2026
- Daniel writes on one archival sheet and sends that same sheet to 1986
- Tomas stores that sheet in his apron
- Daniel writes the warning page with same blunt pencil and sends it
- returned page is that same page forty years older
- final scratched warning is physically on the Cafe Siete painted glass/sign zone

## Same-Object Rule

A close-up/inset never creates a second physical copy. Same-moment wide/detail states must agree. State advances only once.

Every recurring/cross-era object should use its creator ledger ID when one exists.

## Micro-Continuity Ledger

Track at minimum:
- Daniel/Tomas pose, facing, hand occupancy and distance
- Daniel glasses/gloves/notebook/pencil/flashlight/folder/token
- Tomas tray/tongs/saucer/pastry/apron/hair cord
- service-window open/closed state
- counter and cafe geometry
- exact Cafe-clock minute/second
- separate station-clock state if shown
- 1986 vs 2026 environment state
- sent/received page provenance and aging
- pastry/saucer aging state
- `TOMAS` scratch and final fire-warning scratch
- lighting and station/cafe activation state
- current chapter connection duration inherited from creator ledger

Occlusion is not disappearance.

## Anatomical-Side Continuity

Use production-only side identities only when needed to prevent reverse-shot drift, such as WRITING HAND, NOTE HAND, TRAY HAND, TOKEN HAND, FLASHLIGHT HAND, or APRON POCKET. Screen-left/right may flip; physical side may not silently change.

## Object Provenance Across Time

Crossing through the service window changes timeline/age state, not identity.

For every crossing object track:
1. creator object ID
2. origin era
3. source hand/surface
4. threshold crossing
5. transformed state
6. destination hand/surface
7. later storage/use/history

Never show both pre-crossing and post-crossing copies as simultaneously real.

If a new cross-era/evidence object has no creator ID yet, add it to `Continuity/temporal-object-provenance-ledger.md` before generation.

## Dual-Era Architecture

The cafe and station are one physical structure in different historical states. Preserve permanent geometry while changing era-appropriate condition/occupancy. Do not mirror, relocate, enlarge, or redesign the service window, counter, clock wall, station structure, or service routes for composition.

## Clock / Time State

Two separate clocks are currently canon:
- Cafe Siete connection clock — active countdown
- San Aurelio station clock — historical clue

Every strip declares its active Cafe-clock start/end when the connection is open. Later chapters must include exact seconds when the creator state ledger shortens the window to non-whole-minute close times.

No accidental duplicate minute/second, skipped causality, decorative contradictory clock, or clock-identity swap.

## Timeline Settlement

Historical changes do not arbitrarily rewrite Daniel's external 2026 world mid-conversation.

Use `Continuity/timeline-rewrite-protocol.md`:
- local threshold effects can occur immediately
- broader historical changes settle after closure
- Daniel may retain old/new memory state
- external records change only when causally downstream

Do not use timeline rewrite as a repair for production mistakes.

## Legal Cut

A legal time/location cut may reset ordinary noncritical clutter or pose, but cannot erase evidence, duplicate crossing objects, reset permanent architecture, recover lost time, or change historical facts required by the next beat.

## Camera / Eyeline

Preserve coherent world-space axis and real gaze targets across uninterrupted conversation. A reverse shot may flip screen positions but not exchange physical sides or contradict shared counter/window geometry.

## Physical Text

Story-critical text must remain attached to the real carrier and readable at mobile scale. Chapter 1 exact required text includes:
- `CAFE SIETE`
- `TOMAS`
- `12:00` through `12:07` where scripted
- `DANIEL SORIANO`
- `SAN AURELIO MUNICIPAL MUSEUM`
- `2026`
- `I AM REAL.`
- `DO NOT TELL ANYONE ABOUT ME.`
- `KEEP THIS HIDDEN.`
- `COME BACK TOMORROW.`
- `I WILL BRING BETTER BREAD.`
- `FIRE STARTS IN THE SERVICE CORRIDOR.`

## Sequential Generation

1. validate creator continuity inheritance
2. validate all required canonicals
3. validate chapter-local state-resolution addenda
4. generate Strip 001 only
5. visually audit actual pixels
6. repair/regenerate until PASS
7. attach only newly approved Strip 001 as temporary continuity input to Strip 002
8. repeat sequentially through final strip
9. stitch approved strips
10. run stitched-chapter audit
11. run fresh final clean-room audit
12. write final chapter-end state back into continuity/provenance ledgers if the approved visual production establishes any new permanent fact

Never skip ahead because later prompts exist.

## Completion Language

`PRODUCTION COMPLETE` is allowed only after all current mandatory creator-continuity, rendered, stitch, and final gates pass.
