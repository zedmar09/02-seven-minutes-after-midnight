# Approved References And Deferred Generation

One user-supplied shared lead-character reference has an approved PNG working master and approved WebP. Its scope is character identity only; it does not approve the depicted rendering style, environment, props, pose, clothing details, dates, signage, newspaper copy, clock state, lighting, or title text.

| Reference | Specification | PNG master | WebP |
|---|---|---|---|
| Daniel and Tomas | [Daniel](characters/daniel-soriano/daniel-soriano.md) and [Tomas](characters/tomas-rivera/tomas-rivera.md) | [PNG](approve-png/daniel-tomas-shared.png) | [WebP](approved-webp/daniel-tomas-shared.webp) |

Daniel Soriano is the curly-haired man on the left and Tomas Rivera is the long-haired man on the right. Use the image only for their scoped adult identities. The approved manuscript, textual specifications, and future approved model sheets remain authoritative for every other detail.

## Printed Manga Reference Lock

Every generated reference must be a finished clean black-and-white human-drawn 2D manga production sketch/reference sheet on white paper. Use confident variable ink contours, small flat solid-black shapes, restrained discrete screentone, and sparse functional hatching. The result must be more resolved than a rough thumbnail or construction sketch and less atmospheric than a story panel.

Reject color or tint, sepia, gloss, reflections, glow, bloom, rim light, cinematic exposure or contrast, dark vignette, lens effects, blur, smooth gradients, airbrush, painterly grayscale, photorealism, CGI, 3D rendering, rough construction residue, story-page framing, or generated lettering.

## Characters

| Order | Reference | Planned output | Required image attachment | Status |
|---:|---|---|---|---|
| 1 | [Daniel model sheet](characters/daniel-soriano/daniel-soriano-reference-generation.md) | `daniel-soriano-reference-v001.png` | Approved shared PNG, Daniel on left; identity only | Deferred |
| 2 | [Tomas model sheet](characters/tomas-rivera/tomas-rivera-reference-generation.md) | `tomas-rivera-reference-v001.png` | Approved shared PNG, Tomas on right; identity only | Deferred |
| 3 | [Maribel model sheet](characters/maribel-santos/maribel-santos-reference-generation.md) | `maribel-santos-reference-v001.png` | None | Deferred; storyboard conditional |
| 4 | [Arturo model sheet](characters/arturo-salcedo/arturo-salcedo-reference-generation.md) | `arturo-salcedo-reference-v001.png` | None | Deferred; storyboard conditional |
| 5 | [Lilia model sheet](characters/lilia-ramos/lilia-ramos-reference-generation.md) | `lilia-ramos-reference-v001.png` | None | Deferred; off-panel unless storyboard requires her |

Do not attach the Daniel-and-Tomas image to Maribel, Arturo, or Lilia jobs. Benjamin Manalo and Ernesto Galang are not required for Chapter 1 and have no generation briefs in this package.

## Environments

| Order | Reference | Planned output | Required image attachment | Status |
|---:|---|---|---|---|
| 6 | [San Aurelio Junction, 2026](environments/san-aurelio-junction/san-aurelio-junction-2026-reference-generation.md) | `san-aurelio-junction-2026-reference-v001.png` | None | Deferred |
| 7 | [San Aurelio Junction, 1986](environments/san-aurelio-junction/san-aurelio-junction-1986-reference-generation.md) | `san-aurelio-junction-1986-reference-v001.png` | Approved output from order 6 | Deferred dependency |
| 8 | [Cafe Siete dual-era floor plan](environments/cafe-siete/cafe-siete-dual-era-floor-plan-reference-generation.md) | `cafe-siete-dual-era-floor-plan-reference-v001.png` | None | Deferred |
| 9 | [Cafe Siete dual-era perspective](environments/cafe-siete/cafe-siete-dual-era-perspective-reference-generation.md) | `cafe-siete-dual-era-perspective-reference-v001.png` | Approved output from order 8 | Deferred dependency |
| 10 | [Municipal museum archive](environments/municipal-museum-archive/municipal-museum-archive-reference-generation.md) | `municipal-museum-archive-reference-v001.png` | None | Deferred |

Character images must not be attached to empty environment-reference jobs.

## Objects And Phenomena

| Order | Reference | Planned output | Required image attachments | Status |
|---:|---|---|---|---|
| 11 | [Time-transfer props](objects/cafe-and-archive-props/time-transfer-props-reference-generation.md) | `time-transfer-props-reference-v001.png` | None | Deferred |
| 12 | [Clocks, signage, and door](objects/cafe-and-archive-props/clocks-signage-door-reference-generation.md) | `clocks-signage-door-reference-v001.png` | Approved outputs from orders 6 and 8 | Deferred dependencies |
| 13 | [Time-slip and aging](objects/temporal-phenomena/time-slip-and-aging-reference-generation.md) | `time-slip-and-aging-reference-v001.png` | Approved outputs from orders 9, 11, and 12 | Deferred dependencies |

## Release Boundary

These thirteen files are evidence-based deferred generation briefs, not paste-ready ChatGPT handoffs. Each eventual structured job must bind every required image by real project-relative path and SHA-256. No future filename counts as an attachment before its generated output is reviewed, explicitly approved, and hash-locked.

Canon v002 is approved, active, hash-bound, and story-locked. Current blockers are storyboard v001 approval and lock, `image_generation_enabled=false`, unresolved visual dependencies, and absent schema-valid image jobs. No reference artwork or executable handoff has been released.

- [Characters](characters/README.md)
- [Environments](environments/README.md)
- [Objects](objects/README.md)
- [PNG masters](approve-png/README.md)
- [WebP conversions](approved-webp/README.md)
