# Approved References And Deferred Generation

Five final character model sheets are approved under stable, unversioned production filenames. Technical versions, review history, approval IDs, and hashes stay under `.manga-studio` rather than appearing in ordinary attachment names.

| Reference | Specification | PNG master | Approved WebP |
|---|---|---|---|
| Daniel Soriano | [Specification](characters/daniel-soriano/daniel-soriano.md) | [PNG](approve-png/daniel-soriano.png) | [WebP](approved-webp/daniel-soriano.webp) |
| Tomas Rivera | [Specification](characters/tomas-rivera/tomas-rivera.md) | [PNG](approve-png/tomas-rivera.png) | [WebP](approved-webp/tomas-rivera.webp) |
| Maribel Santos | [Specification](characters/maribel-santos/maribel-santos.md) | [PNG](approve-png/maribel-santos.png) | [WebP](approved-webp/maribel-santos.webp) |
| Arturo Salcedo | [Specification](characters/arturo-salcedo/arturo-salcedo.md) | [PNG](approve-png/arturo-salcedo.png) | [WebP](approved-webp/arturo-salcedo.webp) |
| Lilia Ramos | [Specification](characters/lilia-ramos/lilia-ramos.md) | [PNG](approve-png/lilia-ramos.png) | [WebP](approved-webp/lilia-ramos.webp) |

The earlier combined Daniel-and-Tomas image remains available only as approved legacy identity evidence. Production jobs should attach the individual model sheets above.

## Printed Manga Reference Lock

Every generated reference must be a finished clean black-and-white human-drawn 2D manga production sketch/reference sheet on white paper. Use confident variable ink contours, small flat solid-black shapes, restrained discrete screentone, and sparse functional hatching. The result must be more resolved than a rough thumbnail or construction sketch and less atmospheric than a story panel.

Reject color or tint, sepia, gloss, reflections, glow, bloom, rim light, cinematic exposure or contrast, dark vignette, lens effects, blur, smooth gradients, airbrush, painterly grayscale, photorealism, CGI, 3D rendering, rough construction residue, story-page framing, or generated lettering.

## Characters

| Order | Reference record | Approved output | Status |
|---:|---|---|---|
| 1 | [Daniel model sheet](characters/daniel-soriano/daniel-soriano-reference-generation.md) | [daniel-soriano.webp](approved-webp/daniel-soriano.webp) | Approved |
| 2 | [Tomas model sheet](characters/tomas-rivera/tomas-rivera-reference-generation.md) | [tomas-rivera.webp](approved-webp/tomas-rivera.webp) | Approved |
| 3 | [Maribel model sheet](characters/maribel-santos/maribel-santos-reference-generation.md) | [maribel-santos.webp](approved-webp/maribel-santos.webp) | Approved |
| 4 | [Arturo model sheet](characters/arturo-salcedo/arturo-salcedo-reference-generation.md) | [arturo-salcedo.webp](approved-webp/arturo-salcedo.webp) | Approved; attach only when visible |
| 5 | [Lilia model sheet](characters/lilia-ramos/lilia-ramos-reference-generation.md) | [lilia-ramos.webp](approved-webp/lilia-ramos.webp) | Approved; attach only when visible |

Do not attach the Daniel-and-Tomas image to Maribel, Arturo, or Lilia jobs. Benjamin Manalo and Ernesto Galang are not required for Chapter 1 and have no generation briefs in this package.

## Environments

| Order | Reference | Planned output | Required image attachment | Status |
|---:|---|---|---|---|
| 6 | [San Aurelio Junction, 2026](environments/san-aurelio-junction/san-aurelio-junction-2026-reference-generation.md) | `san-aurelio-junction-2026.png` | None | Deferred |
| 7 | [San Aurelio Junction, 1986](environments/san-aurelio-junction/san-aurelio-junction-1986-reference-generation.md) | `san-aurelio-junction-1986.png` | Approved output from order 6 | Deferred dependency |
| 8 | [Cafe Siete dual-era floor plan](environments/cafe-siete/cafe-siete-dual-era-floor-plan-reference-generation.md) | `cafe-siete-dual-era-floor-plan.png` | None | Deferred |
| 9 | [Cafe Siete dual-era perspective](environments/cafe-siete/cafe-siete-dual-era-perspective-reference-generation.md) | `cafe-siete-dual-era-perspective.png` | Approved output from order 8 | Deferred dependency |
| 10 | [Municipal museum archive](environments/municipal-museum-archive/municipal-museum-archive-reference-generation.md) | `municipal-museum-archive.png` | None | Deferred |

Character images must not be attached to empty environment-reference jobs.

## Objects And Phenomena

| Order | Reference | Planned output | Required image attachments | Status |
|---:|---|---|---|---|
| 11 | [Time-transfer props](objects/cafe-and-archive-props/time-transfer-props-reference-generation.md) | `time-transfer-props.png` | None | Deferred |
| 12 | [Clocks, signage, and door](objects/cafe-and-archive-props/clocks-signage-door-reference-generation.md) | `clocks-signage-door.png` | Approved outputs from orders 6 and 8 | Deferred dependencies |
| 13 | [Time-slip and aging](objects/temporal-phenomena/time-slip-and-aging-reference-generation.md) | `time-slip-and-aging.png` | Approved outputs from orders 9, 11, and 12 | Deferred dependencies |

## Release Boundary

The five character records are fulfilled. The remaining environment, object, and phenomenon files are evidence-based deferred generation briefs, not paste-ready ChatGPT handoffs. Each eventual structured job must bind every required image by real project-relative path and SHA-256.

Canon is approved, active, hash-bound, and story-locked. Current blockers are Chapter 1 storyboard approval and lock, `image_generation_enabled=false`, unresolved environment and object dependencies, and absent schema-valid image jobs. No executable environment, object, panel, or page handoff has been released.

- [Characters](characters/README.md)
- [Environments](environments/README.md)
- [Objects](objects/README.md)
- [PNG masters](approve-png/README.md)
- [WebP conversions](approved-webp/README.md)
