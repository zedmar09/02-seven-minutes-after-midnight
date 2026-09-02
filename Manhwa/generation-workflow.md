# Manhwa Generation Workflow

## Production Authority

`Manhwa/` is the sole active visual-production pipeline.

Always binding on every active strip:
- `style-guide.md`
- `reference-vibe-profile.md`
- `vertical-scroll-layout-guide.md`
- `seam-continuity-protocol.md`
- `lettering-sfx-guide.md`
- `production-readiness-gate.md`
- adopted hardening addenda

A chapter/strip may make these rules stricter but never looser.

## Character Card Authority — Absolute

Recurring humans use approved canonical WebPs under `../Character-References/` generated from prompts following `character-card-standard.md`.

Approved cards control face, age presentation, proportions, hair, permanent marks/accessories, and primary silhouette from all angles.

PNG may be a local generation/QA intermediate. After approval, manually convert to WebP and commit the exact WebP. Production Markdown must reference exact committed `.webp` filenames.

## Attached Visual References Are Binding — Absolute

Approved WebPs are permanent authority, not inspiration.

Preserve:
- character identity
- environment geometry
- service-window/counter architecture
- clock construction
- recurring object construction
- materials/proportions
- physically valid reverse angles

If a desired composition conflicts with approved canon, recompose the shot/action. Never modify canon to make generation easier.

## Permanent Canon vs Previous Strip — Absolute

Immediately previous APPROVED strip controls temporary story state only:
- pose/facing
- emotional intensity
- held items
- sleeves/clothing layer
- temporary flour/wetness
- object location/state
- clock minute
- connection/era state
- service-window open/closed state
- temporary light state
- seam continuity

It does not outrank permanent canon. If previous rendered strip contains permanent drift, correct that drift in the next repair rather than promoting it.

## Derived Micro-Detail — Canon-Subordinate Only

If a small practical detail is required but not clearly visible in canonical WebPs:
- exhaust existing floor plans/wides/details/angle atlases first
- derive only the smallest necessary detail within canonical geometry
- do not add/move walls, doors, windows, counter, service window, clock wall, major fixtures, or architecture
- keep derived detail temporary chapter continuity unless a deliberate new canonical later adopts it
- canonical conflict later → canonical wins and affected strip is corrected

## Legal Time / Location Cut Rule

A legal cut may change ordinary noncritical clutter, routine body position, and mundane prop placement when prior state is no longer story-critical.

It does not erase:
- permanent identity
- evidence
- scratch text
- object provenance
- lost clock time
- established fire damage
- structural architecture
- known connection rules

Do not use “time passed” to erase evidence or duplicate objects.

## Real-Scenario Cause / Action / Consequence — Absolute

Every meaningful state change must pass:

`START STATE → CAUSE → VISIBLE PHYSICAL ACTION → RESULT → END STATE THAT PERSISTS`

Audit small actions too: reach, grip, hand occupancy, step, lean, pocket placement, tray/tongs handling, writing, tearing paper, passing threshold, catching wrist, dropping flashlight, clock glance, window opening, object transformation.

A camera cut cannot hide teleport/reset.

## Deterministic Single-Mechanism Rule — Absolute

When continuity-critical action requires one physical solution, choose one authoritative mechanism and carry it through every section of that strip.

Do not write alternatives like:
- left or right hand
- tray or counter
- pocket or apron
- standing or leaning
- glass door or service window

when those choices would create different physical states.

## Mandatory Action-Proof Framing — Absolute

When an action establishes a continuity-critical fact, artwork must visually prove the mechanism, not only before/result.

Examples:
- Daniel's gloved hand + Tomas's hand stabilize same tray edge → finger contact → both react
- Daniel's unstable counter hand → Tomas catches same wrist → pain → release
- service window physically opens → open threshold persists
- Tomas grips bread with tongs → places on saucer → pushes same saucer across opening
- object crosses threshold → same object visibly ages
- Daniel writes on one sleeve/page → physically passes same carrier → Tomas receives/pockets it
- flashlight leaves counter → fall → floor impact → remains on floor
- Daniel writes Arturo → pencil lead physically snaps → broken pencil state persists
- Daniel tears one notebook page → writes three lines → passes same page
- returned aged page emerges from sealed window → Daniel receives/preserves same page

Do not crop decisive contact. SFX/reaction/narration cannot substitute.

## Same-Object Representation / Insert — Absolute

A close-up/inset/magnified detail does not create another copy.

When wide + detail show one continuity-critical object/person:
- both views refer to SAME physical object/person unless script explicitly establishes otherwise
- same-moment views show compatible state
- later-action slice advances state once
- earlier incompatible state no longer remains physically true

## Micro-Continuity / Persistence Ledger — Absolute

Track at minimum when relevant:
- Daniel/Tomas position/facing/distance
- hands/held items/anatomical side
- gloves/glasses/hair tie/sleeves/apron
- tray/tongs/bread/saucer
- token
- flashlight
- notebook/pencil/torn page
- acid-free sleeve
- apron-pocket paper
- service-window state
- cafe door/glass scratch state
- clock minute
- station/cafe era state
- lights/steam/rain/occupancy
- object aging/damage/stain state

Occlusion is not disappearance.

## Camera-Cut Conservation — Absolute

Close-up, reverse shot, reaction insert, gutter, diagonal split, or strip boundary cannot silently change quantity, anatomical ownership, orientation, connection state, scale, depth order, location, era, minute, or object-age state.

## Temporary Anatomical-Side Identity

When a continuity-critical temporary state remains on one physical side, establish an internal identity and preserve it until visible transfer/expiry.

Possible Chapter 1 labels:
- `TOKEN HAND`
- `FLASHLIGHT HAND`
- `NOTEBOOK HAND`
- `PENCIL HAND`
- `TRAY HAND`
- `TONGS HAND`
- `WRIST-CATCH HAND`
- `WINDOW HAND`

Screen-left/right may reverse; anatomical side may not. Labels are NEVER reader-facing.

## Worn-Accessory Persistence

Established worn items remain same body location unless visibly moved:
- Daniel glasses/gloves where currently worn
- Tomas hair cord
- later character watches/rings/rosary/etc.

Partial occlusion allowed. Disappearance, duplication, clipping, or side swap is not.

## Orientation / Hinge / Handle Conservation

Preserve:
- service-window opening/track/hinge mechanism
- cafe gate/door orientation
- notebook spine/page-turn direction
- tray/saucer orientation where continuity matters
- clock face orientation
- fixed architectural front/back relationships

Reverse camera may flip screen-left/right but not physical mechanics.

## Object Scale / Fit Conservation

Recurring objects keep stable world-space size:
- brass token
- clock
- notebook
- acid-free sleeve
- tray
- tongs
- saucer
- roll/pan de leche
- flashlight

Close-up magnifies on page only; it never changes object world size.

## Depth / Occlusion / Contact Proof

2D overlap is not automatically contact.

For threshold actions, show enough contour/depth to prove which side of the window each hand/object occupies, when an object crosses, and who owns the contact.

## Flexible Object / Gravity / No-Clipping

Paper, notebook pages, hair, apron ties, jacket fabric, flashlight, pastry crumbs, and loose props obey gravity/support/collision.

## Era-State Ledger — Absolute

Every Chapter 1 beat belongs to one of:
- `2026_ABANDONED_CLOSED`
- `CONNECTION_OPEN_SHARED_THRESHOLD`
- `1986_VISIBLE_ACTIVE` as part of the shared connection
- `CONNECTION_DESTABILIZING`
- `2026_ABANDONED_POST_CLOSE`

These are production labels only and must never appear in artwork.

Do not allow a background slice to show 2026 ruin behind Tomas on his actual 1986 side unless the composition deliberately communicates the established time-overlap and remains physically legible.

## Clock-State Ledger — Absolute

Chapter 1 minute sequence:

`PRE:12:07_STOPPED → 12:00 → 12:01 → 12:02 → 12:03 → 12:04 → 12:05 → 12:06 → 12:07_CLOSE → POST:12:07_STOPPED`

No silent skips/repeats/reversals.

## Time-Crossing Object Provenance — Absolute

For each exchanged object track:

`origin era → original owner/location → threshold approach → crossing → transformation → destination owner/location → later state`

### Chapter 1 roll/saucer

1986 Tomas/tray → tongs → saucer → service window → crosses to 2026 → same roll dries/shrinks/cracks + same saucer ages → Daniel handles same aged set.

### Chapter 1 acid-free sleeve

2026 Daniel folder/supplies → Daniel writes identity/year/`I am real.` → passes through service window → 1986 Tomas receives → same sleeve remains unnaturally new → Tomas folds/pockets it.

### Chapter 1 torn warning page

2026 Daniel notebook → page torn/written → passes backward → Tomas receives → connection closes → same page later returns forward aged forty years/smoke-stained with Tomas's added line → Daniel sleeves/preserves same page.

Never duplicate any of these.

## Camera Axis / Eyeline

Continuous conversation/action preserves world-space sides and gaze targets. Crossing 180° axis requires neutral reorientation.

Daniel/Tomas cannot switch physical sides of counter/service window merely because the camera reverses.

## Physical Text Plane

Scratches remain on glass. Handwriting remains on paper. Clock time remains on clock. Station signs remain on real sign planes.

## Reflection / Shadow False-Duplicate Ban

No unscripted reflected/shadow duplicate humans, hands, faces, or evidence objects. Glass may show restrained environmental sheen only.

## Grip / Finger Ergonomics

Critical grips must be usable:
- tongs held by handles
- tray supported realistically
- wrist catch uses believable hand/wrist relationship
- pencil grip supports actual writing
- paper supported during passing
- flashlight fall begins from a physically plausible counter position

## Audio Source / Reaction Direction

Offscreen 1986 station audio and Lilia's kitchen audio remain at actual story-world source. Reactions orient toward that source when relevant. Do not float audio from Daniel's 2026 side.

## Sequential Generation — Mandatory

1. confirm all required canonical WebPs for Strip 001
2. generate Strip 001 only
3. visually inspect actual pixels against all current gates
4. reject/repair/regenerate until PASS
5. only approved Strip 001 may be temporary attachment for Strip 002
6. repeat sequentially to final strip
7. stitch all approved strips
8. run fresh stitched-chapter clean-room audit

Do not batch-generate unapproved future strips using an unverified earlier strip.

## Re-Audit Rule

After any correction:
- re-audit corrected strip
- re-audit neighboring seam(s)
- re-audit affected continuity ledger entries

After all strips pass, perform a fresh full chapter audit rather than inheriting old PASS labels.

## Production Completion Rule

`PRODUCTION COMPLETE` is forbidden until:
- required permanent canonicals exist and are approved
- every current strip passes rendered visual QA
- every seam passes
- stitched chapter passes
- exact ending matches locked story
- fresh clean-room final audit reports zero unresolved mandatory findings.