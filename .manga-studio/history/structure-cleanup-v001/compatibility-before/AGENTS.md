<!-- BEGIN MANGA STUDIO MANAGED -->
## Manga Studio

- This repository is the project root; manga is the working surface, not a separate project.
- The user explicitly authorized the structure-cleanup-v001 migration. Archived originals are immutable evidence at the paths in .manga-studio/maintenance/structure-cleanup-v001/archive-manifest.json. Keep their bytes, snapshots, normalized sources, source maps, stable IDs and approvals intact.
- Current source records point to archived original bytes. Immutable maps and historical evidence retain their as-imported paths. Resolve old paths with the manifest and expected SHA-256; never confuse the new root README with the original README.
- The current working register is .manga-studio/maintenance/structure-cleanup-v001/working-files.json. Verification is .manga-studio/maintenance/structure-cleanup-v001/verify.py. Historical layout verifiers apply only to their archived state.
- Keep stable filenames under manga/00-series, 01-style, 02-references, 03-story and 04-production. Preserve a version internally before replacing a working file. Do not restore obsolete Comics, AppCover, versioned visible indexes, or duplicate manuscript copies.
- Authoritative manuscript versions stay in .manga-studio/manuscript/versions. Chapter 1 v001 remains draft_inactive. No canon, manuscript or storyboard is adopted; no locks have changed.
- Working extracts are navigation and reference material, not new canon or production authority. Use this story's evidence only. Other stories supply generic folder roles, never characters, assets, approvals or workflow choices.
- Do not run a fresh inventory over the cleaned root and overwrite the imported archive records. Runtime scanning excludes .manga-studio; future intake must preserve/merge the approved archived inventory and stable IDs. Do not import README, AGENTS or manga derivatives as new original sources.
- Future ingestion and structural parsing require explicit new sources and a provenance check. Historical source-map paths are preserved as import coordinates, not current storage paths.
- Retain panel_first: externally generated text-free, borderless panel art, then approval, composition and separate lettering. Naming parity does not select complete_page.
- Image generation remains disabled. Codex must never generate, edit, retouch or correct artwork. Future structured ChatGPT image jobs require high quality, approved hash-locked references, exact attachments, structured SFX, reading order and all applicable gates.
- Do not activate versions, approve artifacts, change locks, draft new chapters, release prompts, publish or push without explicit authorization for that action.
<!-- END MANGA STUDIO MANAGED -->
