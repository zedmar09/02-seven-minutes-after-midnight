# Canonical Character Card Standard — Flat 2D Manhwa

This is the reusable visual-reference standard for every recurring human character in `Seven Minutes After Midnight`.

## Purpose

A canonical character reference is a multi-view model sheet detailed enough to preserve identity across camera angles, expressions, poses, eras, and full-body compositions throughout the Manhwa.

Once generated, visually approved, manually converted, and committed, reuse the SAME canonical WebP across later chapters. Do not generate chapter-specific replacements unless canon deliberately changes.

## Generation / Repository Format Rule

The image-generation prompt may request PNG as a local intermediate.

After approval:
1. manually convert the approved PNG to WebP
2. commit/store the canonical `.webp`
3. production Markdown must reference that exact committed filename

An intermediate/deleted PNG is not active authority.

## Absolute Visual Style

- 100% flat 2D human-drawn full-color Korean manhwa/webtoon
- clean visible linework
- matte solid colors
- restrained hard-edged cel shading only where useful
- natural adult anatomy
- readable hands and feet
- stable proportions across repeated views
- plain light-neutral sheet background

ABSOLUTELY NO glossy webtoon shine, shiny skin/hair, cinematic lighting, bloom, rim light, lens flare, volumetric light, photorealism, semi-photorealism, 3D/CG, painterly rendering, airbrushed gradients, mirror-like reflections, depth-of-field blur, or over-rendering.

## Required Card Layout

### 1. Full-Body Turnaround

Show the same person at consistent scale:
- front
- 3/4 left
- left profile
- back
- 3/4 right

Add right profile when needed. Do not crop head, hands, shoes, or feet.

### 2. Face / Hair Angles

Show larger head/shoulder references:
- front
- 3/4
- profile
- rear/back-of-hair when hairstyle construction matters

### 3. Expression Set

Include 6–8 grounded expressions appropriate to the character. Expression may change; face geometry, age, scar/marks, glasses, hair, and permanent identity may not.

### 4. Signature Detail Area

Show only recurring identity details that benefit from scale/reference coordination: glasses, scar, hair tie, signet ring, watch, rosary, work accessories, etc.

Plot-critical reusable objects with their own authority under `Manhwa/Object-References/` remain separate.

### 5. Primary Outfit Authority

Show the primary outfit clearly enough to preserve garment lengths, layering, sleeves, footwear, accessories, and silhouette. Later scripted outfits may change; identity does not.

## Card Composition Rules

- one unified reference sheet, not a story scene
- clean whitespace
- no dramatic environment or story lighting
- prefer zero generated reader-facing labels
- no speech balloons, captions, SFX, watermarks, signatures, measurements, fake UI, or story panels

## Production Authority

Character cards control:
- face identity
- age presentation
- height/build/body proportions
- hair length/part/tie/fringe/color
- permanent marks and their anatomical location
- recurring accessories
- primary outfit silhouette/construction
- signature detail design shown on card

Current strip controls temporary pose, performance, injury, wetness, temporary flour/dirt, currently held props, and legal wardrobe changes.

## Anatomical-Side Rule

If a permanent landmark has a side, that side is anatomical—not screen-left/right.

Reverse camera may visually swap screen side but may not move:
- Daniel's nose scar geometry
- a watch/bracelet/ring established on one hand/wrist
- Tomas's hair-tie construction
- Lilia's rosary wrist once canonicalized
- Arturo's signet-ring hand once canonicalized
- any other permanent mark/accessory

## Acceptance Gate

Reject a card if:
- repeated views look like different people
- face/hair/body proportions change between angles
- age changes between expressions
- hands/feet are missing from full-body views
- scar/mark/accessory disappears or moves sides
- front/back views imply different clothing construction
- hairstyle changes length/tie/part between views
- duplicated props or impossible anatomy appears
- character becomes glossy, cinematic, 3D, painterly, airbrushed, or photoreal

`../characters.md` supplies character-specific identity locks. `../Manhwa/style-guide.md` supplies absolute rendering rules.