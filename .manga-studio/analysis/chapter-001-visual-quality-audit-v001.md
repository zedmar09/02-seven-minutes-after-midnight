# Chapter 1 Visual-Quality Audit v001

Status: reviewed and accepted as the Chapter 1 quality direction. This is not canon approval, a stage lock, an approved storyboard, artwork approval, image-job release, or permission to generate images.

## Scope

This audit compares the approved active Chapter 1 manuscript, the retired fourteen-page prompt set, the current `panel_first` production policy, the shared structural roles used by `01-My Roommate Only Appears During Blackouts`, and three user-supplied manga examples. The other story is a workflow and pacing benchmark only. Its story data, characters, assets, approvals, layouts and production mode are not copied.

## Evidence

- Active manuscript v001: SHA-256 `f195b7e0afc7f875731ade728a1bbf7a28d7becf3f38fa2d920498231f65d500`; 2,896 story words; exact prose unchanged by this approval update.
- Retired Chapter 1 plan: 14 interior pages, 75 panels, average 5.36 panels per page; every page contains five or six panels.
- Reference-story Chapter 1 benchmark: 36 pages, 133 panels, average 3.69 panels per page. Several reference pages are held, correction, or unreleased, so this is a pacing and document-discipline benchmark rather than blanket quality approval.
- User example `Codex Image Sep 8, 2026, 06_13_47 PM.png`: 920 x 1379; SHA-256 `cdc9223276453b63e629747dc42bf0f8a4b7d862c3a698cd05732f3a72ffb20e`.
- User example `images.jpeg`: 480 x 640; SHA-256 `ef4c8faf33dcefa964c8e2cd0157c2f6fd47a74a87d610eccaa9035efc727daa`.
- User example `Screenshot 2026-09-03 at 2.12.17 PM.png`: 266 x 886; SHA-256 `a1c6c67c208fbf3770f7b9a6b617e17ad689cf4fcd21d3ab931c9617dcddc7fa`.

The three image files remain external review evidence. They were not copied into the project, promoted to approved visual references, or treated as instructions to reproduce copyrighted layouts or artwork.

## Findings

1. The retired 14-page plan is too compressed for the approved manuscript and desired visual standard. Its uniform five-to-six-panel density leaves too little page area for establishing geography, the time-slip reveal, tactile object continuity, restrained intimacy, clock pressure, and the final warning.
2. The retired prompts are complete-page generation prompts, which conflict with the retained `panel_first` pipeline of text-free borderless panel art, approval, deterministic composition, and separate lettering.
3. No current page map, panel plan, storyboard, released image job, approved project visual reference, or approved image exists. Historical prompts cannot fill those roles.
4. The user examples consistently support variable visual hierarchy: one dominant beat, secondary reaction or information panels, controlled reading flow, and panel area proportional to narrative weight. They do not support a mandatory template or a copied panel arrangement.
5. The reference-story benchmark supports a longer chapter envelope and lower average panel density, but its page count must not substitute for story-specific beat allocation.

## Approved Direction

- Use a provisional target of 36 interior pages and a 32-40 page working range.
- Keep English left-to-right reading and the existing `panel_first` workflow.
- Build page geometry from event density. Vary panel area, camera distance, silence, reaction space and page turns according to the approved manuscript beats.
- Reserve strong visual emphasis for location establishment, the first impossible contact, evidence exchange, clock escalation, reciprocal proof, closure, the aged reply, and the final warning.
- Treat 1654 x 2339 pixels as the current high-resolution working target, not a final print specification.
- Use the supplied examples as quality principles only. Do not copy panels, characters, lettering, compositions or assets.

## Remaining Gates

- Canon remains unapproved.
- All nine stage locks remain false.
- Exact page count, panel count, page order, page turns, camera plan, dialogue placement and SFX placement require a versioned storyboard and explicit approval.
- Character, environment and prop references require separate hash-bound approval before image jobs.
- Image generation remains disabled. No prompt or artwork is released.

## Approval Boundary

The user approved the exact manuscript v001 and this quality direction after reviewing the audit summary. The manuscript approval is recorded in `.manga-studio/approvals/approval-feb5212823b84aeaaa04bac3fedc4fc6.json`. The seven disclosed manuscript-review warnings remain on record; the manuscript-activation portion of warning SMA-WARN-006 is now resolved, while canon and lock requirements remain open.
