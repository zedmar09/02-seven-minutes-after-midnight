# Chapter 1 Reference Prompt Style Audit v001

Status: completed; corrections adopted in deferred reference-generation package v002.

## Scope

This audit compares the Chapter 1 reference-generation briefs with the approved visual-reference standard demonstrated by the existing `01-My Roommate Only Appears During Blackouts` workspace and with the user-provided manga-page examples. The other story supplies only a generic reference-sheet finish and organizational precedent. It supplies no characters, places, story facts, approvals, or assets to this project.

## Evidence Standard

The applicable reference finish is a finished, clean, black-and-white, human-drawn 2D printed manga production sketch/reference sheet on white paper. It uses confident variable ink lines, restrained discrete screentone, sparse hatching, and small controlled flat blacks. Forms and spatial relationships must remain easy to inspect.

The word `sketch` means a resolved inked production reference. It does not authorize rough thumbnails, construction residue, loose gray rendering, unfinished studies, or painterly concept art.

The reference-page examples also support varied panel counts and controlled overlaps for later storyboard and page design. They do not change the reference-sheet finish or release any image job.

## Findings

### P1: Character reference briefs were missing

Chapter 1 had no generation briefs for its visible lead and supporting cast. Package v002 adds briefs for Daniel Soriano and Tomas Rivera, plus storyboard-conditional briefs for Maribel Santos, Arturo Salcedo, and Lilia Ramos. Benjamin Manalo and Ernesto Galang remain outside Chapter 1.

### P1: Several prompts described cinematic concept art

The station, Cafe Siete perspective, museum, and time-slip briefs used language such as wet reflections, warm light pools, deep blacks, and cinematic contrast. Those cues could produce color concept art, glossy surfaces, or atmospheric illustrations instead of inspectable manga production references.

Package v002 replaces those cues with flat monochrome line-and-tone instructions and explicitly excludes color, tint, sepia, gloss, reflections, glow, bloom, rim light, cinematic lighting, gradients, blur, painterly rendering, photorealism, CGI, and 3D rendering.

### P1: The rendering lock was inconsistent

Some briefs requested technical diagrams while others requested mood-driven scenes. Package v002 applies one printed-manga reference lock to all thirteen briefs while preserving the subject-appropriate view requirements for model sheets, environments, floor plans, props, and effects.

### P2: Attachment scope was too broad or ambiguous

The approved shared Daniel-and-Tomas image is evidence only for the two leads' identity traits and visual chemistry. It is not evidence for style, wardrobe, pose, environment, signage, text, props, dates, or lighting. Package v002 attaches the approved PNG only to Daniel's and Tomas's character briefs and isolates the applicable person in each prompt.

Supporting-character briefs have no input image. Empty environment and object briefs do not attach character art. Derived-reference briefs name only the approved environment or object assets they will require after those assets exist and are hash-bound.

### P2: Gate language was stale

Earlier briefs described active story gates incorrectly. Package v002 records the current state: canon v001 and `STORY_LOCKED` remain active, canon v002 is a proposed correction awaiting separate approval and relock, `STORYBOARD_LOCKED` is false, `IMAGE_READY` is false, and `image_generation_enabled` is false.

## Corrected Package

Thirteen deferred briefs are indexed in `manga/02-references/README.md` in production order: five character model sheets, five environment references, two object-reference sheets, and one temporal-effect sheet.

No artwork, structured image job, paste-ready external handoff, asset approval, canon approval, storyboard approval, lock change, or image-generation enablement is created by this correction.

