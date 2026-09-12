<!-- BEGIN MANGA STUDIO MANAGED -->
## Manga Studio

- Treat files recorded in `.manga-studio/source/inventory-baseline-v001.json`, including the original `Comics/` tree and root story documents, as immutable source evidence. Keep their original paths and bytes.
- Store normalized derivatives and every revision as separate versioned files under `.manga-studio/`.
- Use `manga/00-series`, `manga/01-style`, `manga/02-references`, `manga/03-story`, and `manga/04-production` as the reader-facing organization. The confirmed project root remains this repository, not `manga/`.
- Keep authoritative manuscript versions in `.manga-studio/manuscript/versions/`. Any versioned reading copy under `manga/03-story/` must match its registered canonical SHA-256; never edit the copy independently.
- Do not re-import `manga/` or `MANGA-STUDIO.md` as original sources. The layout index is `.manga-studio/workspace-layout-v001.json`; new versions must preserve historical paths and approval hashes.
- Other projects may inform generic folder conventions only when the user authorizes inspection. Do not import their stories, identities, canon, approvals, production rules, or assets.
- Require explicit approval before adopting revisions or changing approved canon.
- Approved canon is authoritative over analysis, drafts, storyboards, and production notes; original sources remain the provenance authority.
- Image generation is disabled by default and may be enabled only after the story and storyboard gates are locked.
- Codex must never generate or edit artwork. Character, location, prop, panel, cover, splash-page, and correction art must be represented by structured ChatGPT Image Generation Jobs.
- ChatGPT Image Generation is reserved for eventual external image production; Codex may validate, organize, letter, compose, review, and export approved outputs.
- Future ready jobs require the high-quality contract, approved hash-locked references, explicit reading order, structured SFX and the user's separate approval gates. Empty reference or production folders are not evidence of ready assets.
<!-- END MANGA STUDIO MANAGED -->
