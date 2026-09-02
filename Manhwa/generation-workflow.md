# Manhwa Generation Workflow

## Production Authority

`Manhwa/` is the sole active visual-production pipeline. Every active chapter is rebuilt from current story canon into continuous-scroll production authority. Retired page prompts are not generation targets.

Always binding:
- `style-guide.md`
- `lettering-sfx-guide.md`
- `seam-continuity-protocol.md`
- `vertical-scroll-layout-guide.md`
- `production-readiness-gate.md`

## Required Canonicals

Recurring humans use approved canonical character WebPs under `Character-References/`.
Recurring locations use approved environment WebPs under `Environment-References/`.
Recurring plot-critical objects use approved object WebPs under `Object-References/`.

Generation may produce PNG locally, but only approved committed WebP is permanent repository authority.

Missing/stale/wrong-path/unapproved required WebP → STOP.

## Permanent Canon vs Previous Strip

Previous APPROVED strip controls temporary state only: pose, facing, gesture, held items, prop location, clock minute, era state, damage, food amount, open/closed state, emotional intensity, and seam continuity.

Previous strip never overrides permanent face/hair/build, structural environment geometry, recurring-object construction, or other canonical WebP authority.

## Cause → Action → Result

Every meaningful change must pass:
`START STATE → CAUSE → VISIBLE PHYSICAL ACTION → RESULT → END STATE THAT PERSISTS`

A camera cut may not hide teleportation, duplicate an object, swap hands, change era state, advance/rewind the clock, or silently reset a pose.

## Deterministic Single Mechanism

For continuity-critical actions choose one physical mechanism and carry it through the entire strip. Do not offer mutually incompatible alternatives in one prompt.

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
- Daniel writes the warning page and sends it
- the returned page is that same page forty years older
- the final scratched warning is physically on the Cafe Siete glass

## Same-Object Rule

A close-up/inset never creates a second physical copy. Same-moment wide/detail states must agree. State advances only once.

## Micro-Continuity Ledger

Track at minimum:
- Daniel/Tomas pose, facing, hand occupancy and distance
- Daniel glasses/gloves/notebook/pencil/flashlight/folder/token
- Tomas tray/tongs/saucer/pastry/apron/hair cord
- service-window open/closed state
- counter and cafe geometry
- exact clock minute
- 1986 vs 2026 environment state
- sent/received page provenance and aging
- pastry/saucer aging state
- `TOMAS` scratch and final fire-warning scratch
- lighting and station/cafe activation state

Occlusion is not disappearance.

## Anatomical-Side Continuity

Use production-only side identities only when needed to prevent reverse-shot drift, such as WRITING HAND, NOTE HAND, TRAY HAND, TOKEN HAND, FLASHLIGHT HAND, or APRON POCKET. Screen-left/right may flip; physical side may not silently change.

## Object Provenance Across Time

Crossing through the service window changes timeline/age state, not identity.

For every crossing object track:
1. origin era
2. source hand/surface
3. threshold crossing
4. transformed state
5. destination hand/surface
6. later storage/use

Never show both pre-crossing and post-crossing copies as simultaneously real.

## Dual-Era Architecture

The cafe and station are one physical structure in different historical states. Preserve permanent geometry while changing era-appropriate condition/occupancy. Do not mirror, relocate, enlarge, or redesign the service window, counter, clock wall, or station structure for composition.

## Clock / Time State

Every strip declares its clock start and end when the seven-minute interval is active. Time may advance only in scripted order. No accidental duplicate minute, skipped causality, or decorative contradictory clock.

## Legal Cut

A legal time/location cut may reset ordinary noncritical clutter or pose, but cannot erase evidence, duplicate crossing objects, reset permanent architecture, or change historical facts required by the next beat.

## Camera / Eyeline

Preserve coherent world-space axis and real gaze targets across uninterrupted conversation. A reverse shot may flip screen positions but not exchange physical sides or contradict the shared counter/window geometry.

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

1. validate all required canonicals
2. generate Strip 001 only
3. visually audit actual pixels
4. repair/regenerate until PASS
5. attach only newly approved Strip 001 as temporary continuity input to Strip 002
6. repeat sequentially through final strip
7. stitch approved strips
8. run stitched-chapter audit
9. run fresh final clean-room audit

Never skip ahead because later prompts exist.

## Completion Language

`PRODUCTION COMPLETE` is allowed only after all current mandatory rendered/stitch/final gates pass.
