# Workspace Structure Refactor v001

## User Authorization

The user approved the exact Chapter 1 changes for creation of a new inactive manuscript draft and requested a folder refactor consistent with manga-creator, permitting inspection of the Blackouts project as a comparison.

The comparison was limited to directory organization and the structural headings/path entries in its root README. No story, character, canon, image, approval or generation instruction from that project was imported or used as narrative evidence. That project was not modified.

## Implemented Organization

Added the five visible sections `manga/00-series/`, `manga/01-style/`, `manga/02-references/`, `manga/03-story/` and `manga/04-production/`, with a root `MANGA-STUDIO.md` entry point. Arc and chapter paths use `arc-01/chapter-001` below the story and production sections. Empty reference categories remain explicitly empty.

Manga Creator's runtime-required directories remain under `.manga-studio/`. References, tooling, storyboard panel plans and continuity snapshots have explicit reserved homes. The new manuscript and metadata are managed under `.manga-studio/manuscript/versions/`; the visible story file is a byte-identical versioned reading copy with a registered hash, not a second authority.

The project root and identity are unchanged. The comparison project's claim that its visible manga folder is active is not copied here. All active versions and locks in this project remain unset.

## Preservation Boundary

This is an additive refactor of the working layout, not relocation of original sources. The earlier explicit prohibition on moving or renaming originals remains in force. The source `Comics/` tree, root story documents, immutable snapshots and all previously reviewed artifacts stay at their recorded paths with matching hashes.

Moving the old packages would break recorded source locations, deterministic diff labels and hash-bound approval references. They therefore remain immutable history. New work follows the indexed layout. Existing helper scripts in old audit/review packages are also retained; new maintenance tooling is isolated under `.manga-studio/tooling/`.

`manga/**` and `MANGA-STUDIO.md` are excluded from source ingestion so reading copies and navigation cannot silently become duplicate source documents. Original candidates are still exactly the same 25 files. Revision mode now permits approved versions only, matching the explicitly approved change set; it does not permit unapproved direct prose changes.

## Draft Application

The new draft has exactly the approved reading-preview bytes. The original source-bound change-set proposal is unchanged; its separate approval record binds the user's actual approval. No proposed JSON status is retroactively rewritten.

The chapter-writer materializes a new inactive version, deterministic source-to-version diff and execution decision. The runtime apply-change-set helper is not used because it requires a managed manuscript base and automatically assigns an active version; neither behavior fits the approved source-preserving, inactive-draft operation.

## Remaining Gates

No canon, manuscript or storyboard has been adopted, and no lock has changed. No reference images exist. Storyboards, image jobs, artwork, composed pages and exports have not been produced. Next-visit access, calendar/cost decisions, the photograph comparison and missing Chapter 2 material remain open. No manuscript search, upload or Git push was performed.
