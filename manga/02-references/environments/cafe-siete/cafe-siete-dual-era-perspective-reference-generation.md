# Cafe Siete Dual-Era Perspective Reference Generation

Status: `DEFERRED`

Future job type: `location_reference`

Planned output: `cafe-siete-dual-era-perspective.png`

Deferred dependency: `cafe-siete-dual-era-floor-plan` must first become an approved, hash-locked geometry reference.

## Purpose

Turn the approved floor plan into matched eye-level spatial views that later panels can use for camera continuity. The sheet must clarify the counter, service hatch, adjacent kitchen doorway, pastry case, and separate era states without staging the Chapter 1 encounter itself.

## Authority And Limits

1. The future approved dual-era floor-plan PNG will control geometry, footprints, openings, and orientation.
2. [Cafe perspective notes](cafe-perspective.md) control the current spatial intent.
3. [Cafe canon status](canon.md) records unresolved authority.
4. The active manuscript controls damage, objects, and temporal behavior.

At release time, attach exactly the approved floor-plan reference with its verified path and SHA-256. Do not invent a missing image path. The Daniel-and-Tomas identity reference is not needed because this is an empty environment sheet.

## Generation Brief

Produce ONE 1536 x 1024 landscape PNG named `cafe-siete-dual-era-perspective.png`. Draw exactly two matched wide interior perspectives of Cafe Siete from the same camera coordinate, lens, eye height, and direction.

Place the camera on the public customer side near the cafe entrance, looking across the customer counter toward the back kitchen wall. The service hatch and the full-height kitchen doorway beside it must both be clearly visible. The display case and the open end of the customer counter must remain readable enough to understand Daniel's route.

The left view shows the intact 1986 cafe in its ordinary working state. The right view shows the same cafe ruined in 2026 before the connection opens. Do not create a half-restored split inside either view.

## 1986 View

- Smooth worn counter wood and brass edge details, complete stools, stocked pastry case, intact tile, clear glass entrance, polished service-hatch frame, and a functional kitchen doorway.
- Ordinary working illumination indicated through sparse light screentone, with coffee-steam contours, flour traces, used work surfaces, ceiling-fan motion lines, paper cups, brass tongs, saucers, and a handwritten-menu surface with no readable writing. Do not render luminous bulb pools.
- The kitchen beyond the hatch and doorway feels active but does not introduce visible staff or supporting-character designs.

## 2026 View

- Same geometry and camera, with missing stools, broken tile, dust, rust, old sugar residue, cracked or displaced pastry case, fallen plaster, painted glass, twisted grille, darkness, and a charred lower edge on the service hatch.
- The public floor and furniture stay ruined even where the 1986 counter or kitchen may later become visible through the time connection.
- Preserve the clear route around the counter end to the hatch. Damage cannot make the manuscript's movement impossible.

## Camera And Continuity Rules

- Use normal human eye height and a natural architectural lens. Avoid fisheye, extreme wide-angle stretching, Dutch angle, or cinematic depth blur.
- Match vanishing points, crop, and object coordinates across both era views.
- Keep the customer counter and service hatch visually distinct. Do not imply that the hatch is the main counter or that the kitchen doorway is passable across time.
- Reserve uncluttered wall and glass areas for later exact signage and scratch lettering. Do not render `CAFE SIETE` or `TOMAS` here.

## Printed Manga Reference Finish

Create a finished clean black-and-white human-drawn 2D manga production sketch/reference sheet on white paper. Use crisp matched perspective, confident variable ink contours, small flat solid-black shapes, restrained discrete screentone, and sparse functional hatching. Keep both era views equally readable and matte. Express wood, tile, steam, flour, dust, and damage through contour and flat print texture, not cinematic light.

More resolved than a rough thumbnail or construction sketch, less atmospheric than a story panel. No rough construction residue, color, tint, sepia, gloss, reflections, glow, bloom, rim light, cinematic exposure or contrast, vignette, lens effects, bokeh, blur, smooth gradient, airbrush, painterly grayscale, photorealism, CGI, 3D rendering, floating particles without a physical source, or fantasy portal treatment.

## Exclusions

- No characters, hands, active time-slip, tray exchange, notes, bread-aging event, dialogue, captions, SFX, frames, page layout, logo, signature, or watermark.
- No invented furniture, door, room, exterior view, clue, fire evidence, or new business sign.
- No architecture change between views.

## Final Check

Confirm identical camera and geometry, visible separate hatch and doorway, readable public-to-counter-to-kitchen relationships, a clear counter-end route, complete 1986 versus ruined 2026 states, clean lettering zones, and no unsupported story action.

## Deferred Release Blockers

- The floor-plan dependency is not yet generated, reviewed, approved, or hash-locked.
- `STORYBOARD_LOCKED` is false.
- `image_generation_enabled` is false.
- No schema-valid image job or external handoff has been released.

## Evidence

- [Active Chapter 1 manuscript](../../../../.manga-studio/manuscript/versions/chapter-001-v001.md), especially lines 51-89, 133-139, 243-277, and 433-463.
- [Dual-era floor-plan generation brief](cafe-siete-dual-era-floor-plan-reference-generation.md)
