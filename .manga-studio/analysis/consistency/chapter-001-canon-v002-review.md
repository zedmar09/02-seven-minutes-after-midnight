# Chapter 1 Canon v002 Consistency Review

Status: `REVIEW_READY`

Target: `.manga-studio/canon/versions/chapter-001-canon-v002.json`

Target SHA-256: `897ed992c1106ee39b10f903019a4eb24fd9a51309cc69960e7505d7c9365725`

## Review Result

The pre-storyboard evidence check found one blocking mismatch in the approved active canon v001. Canon fact `canon-fact-ch001-023` names the final door warning as `HE DIED HERE / DO NOT LET HIM STAY`, but the approved active manuscript states `FIRE STARTS IN THE SERVICE CORRIDOR.` at lines 475-477.

Canon v002 is a narrow correction proposal. It preserves the entity mappings, fact IDs, predicates, basis records, twenty-seven confirmed facts, two provisional facts, two inferred facts, two deprecated facts, and ten unknowns from v001. Only the canon version metadata and the value of fact `canon-fact-ch001-023` differ.

No additional direct contradiction was found while rechecking the retained confirmed facts against the approved Chapter 1 manuscript. The v001 canon file remains byte-identical to its approval-bound SHA-256 `8e99db551f9eda9f3b56116b15cd6425a807d27b439df3a493864385612cfb58`.

## Evidence

- Approved active manuscript: `.manga-studio/manuscript/versions/chapter-001-v001.md`
- Manuscript SHA-256: `f195b7e0afc7f875731ade728a1bbf7a28d7becf3f38fa2d920498231f65d500`
- Exact passage: lines 471-477 establish `TOMAS` and then `FIRE STARTS IN THE SERVICE CORRIDOR.` as separate scratched messages.
- Active canon v001 fact: `.manga-studio/canon/versions/chapter-001-canon-v001.json`, `canon-fact-ch001-023`

## Exact Correction

Before:

`The 2026 cafe door glass is painted over. The name TOMAS is already scratched into it, and after closure dust reveals the separate warning HE DIED HERE / DO NOT LET HIM STAY.`

Proposed:

`The 2026 cafe door glass is painted over. The name TOMAS is already scratched into it, and after closure dust reveals the separate warning FIRE STARTS IN THE SERVICE CORRIDOR.`

## Approval Boundary

Canon v002 is proposed and inactive. It requires a separate hash-bound user approval before it can replace v001 as active canon.

Because `CANON_APPROVED` and `STORY_LOCKED` currently bind canon v001, adoption must use an explicit controlled lock transition: clear dependent story/canon locks, approve and activate the exact v002 hash, then restore `CANON_APPROVED` and `STORY_LOCKED` against v002. The already approved manuscript and source remain unchanged.

No storyboard, panel plan, page geometry, image job, or artwork may proceed from the incorrect v001 clue. Storyboard drafting is paused until the v002 correction is approved and the story lock is restored.

