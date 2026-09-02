# Environment Reference Policy

## Absolute Rule

Environment canonicals belong to LOCATIONS, not chapters.

For every environment used in Manhwa production:
- reuse an approved canonical pack if the place already exists
- create a new location-named pack only for a genuinely new environment
- do not duplicate the same place under chapter-numbered folders
- do not let individual strips independently redesign the same place

## Naming

Use permanent location names such as:
- `San-Aurelio-Junction/`
- `Cafe-Siete/`
- future museum/archive locations by their actual place identity

Never prefix reusable environment references with chapter numbers.

## Generation / Repository Format

Prompts may request PNG as local first output. After approval:
1. convert accepted PNG to WebP
2. commit/store only the approved `.webp` authority
3. production Markdown uses exact committed `.webp` path/basename

A Markdown prompt is not a visual canonical.

## Minimum Reference Package

Every important new environment gets at least:
1. geometry/orientation reference — floor plan/map/equivalent
2. canonical establishing view
3. reverse/secondary view sufficient to prevent axis flips

Recurring critical locations additionally require:
- multi-angle atlas
- key-zone details
- relevant era/day/night/weather states
- recurring furniture/fixture anchors

## Dual-Era Rule — Seven Minutes Specific

For a location existing in both 1986 and 2026:
- build one structural geometry authority first
- derive era-specific state views from that authority
- preserve walls/openings/routes/counter/window relationships
- allow age, damage, fire scars, dirt, furniture state, operational state, signage, redevelopment barriers, and plausible documented later modifications
- do not independently redesign 1986/2026 for visual mood

## Authority

Approved environment WebPs control architecture, doors/windows, room relationships, fixed fixtures, paths, proportions, materials/colors, and physically valid camera axes.

Current strip/previous approved strip controls temporary people/props/lighting/action state only.

If a previous strip conflicts with environment canon, reject/correct the drift.

## Attachment Discipline

Attach only the smallest relevant environment set for the current strip. The chapter strip manifest maps exact required WebPs; each strip repeats exact paths.

## New Chapter Checklist

Before production:
- list every environment
- mark `reuse existing` or `new canonical needed`
- create/approve only genuinely new packs
- convert approved images to WebP
- record exact paths
- add exact attachments to strip manifest/prompts
- then begin sequential strip generation.