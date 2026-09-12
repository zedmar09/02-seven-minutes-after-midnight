# Structure Cleanup

The author authorized this migration to match the shared working layout of the existing Blackouts story. Only generic folder roles and filenames were used. No other story content, assets, approvals or production workflow were imported.

## Current State

Open [the manga workspace](../../../manga/README.md). The root now contains only the repository metadata, managed history, agent instructions, README and manga directory.

- [Working files](working-files.json): current paths, hashes and source evidence.
- [Validation](validation.json): source integrity, runtime checks, template comparison and link checks.
- [Migration archive](archive-manifest.json): original paths, archived bytes and pre-cleanup hashes.
- [Storage compatibility](path-relocations.json): preserved intermediate files and path-only changes to two historical decision output lists.
- [Working-note history](working-note-relocations.json): prior working copies before deduplication and status clarification.
- [Cleanup authorization](../../decisions/structure-cleanup-v001.json): layout-only authorization, not artifact adoption.

The original 24 story sources remain byte-identical in the archive and their immutable snapshots. The reconstructed Chapter 1 draft, four approval records and approval targets are unchanged. There is no active manuscript, adopted canon, locked storyboard, released image job or approved artwork.

## Path Resolution

The classification inventory and immutable source maps preserve their original import coordinates. Provenance, document storage records and the source-document ID map point to the archived originals. The new root README is not the old source README.

For a historical path, use its expected SHA-256 and the three relocation manifests above. Try the current path only if its hash matches. Otherwise select the archived entry with both that original path and hash. The verifier implements this rule and verifies every pre-cleanup file.

Do not run the old layout verifiers against the current tree. They describe their archived layout. Do not rescan the cleaned root and replace the imported inventory: the runtime intentionally excludes its managed workspace. Future source intake must preserve the existing classification ledger and stable IDs while registering any explicitly supplied new sources.

## Verification

From the project root:

```sh
python3 .manga-studio/maintenance/structure-cleanup-v001/verify.py
```

The optional `--compare` argument reads the structural reference project without modifying it. Recorded validation includes the exact shared document paths; story-specific entity directories and unavailable image/page-prompt files are intentional differences.

The migration and cleanup helpers are one-shot historical tooling, not commands to rerun. A rollback requires separate authorization and must first preserve any subsequent work. Restore only hash-verified archived bytes and never overwrite newer work blindly.
