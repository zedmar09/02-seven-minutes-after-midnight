"""Register canon v002 adoption and the proposed storyboard in current metadata."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
CANON_REVIEW_SHA = "897ed992c1106ee39b10f903019a4eb24fd9a51309cc69960e7505d7c9365725"
CANON_ACTIVE_SHA = "537dee9e98b9f5b91f86ae3cc611300260b8bb0e6cbe1fbb1bbe81fccef0e762"
CANON_APPROVAL = ".manga-studio/approvals/approval-179120b070e94a71a22d4af7677e67b9.json"
STORYBOARD_PATH = ".manga-studio/storyboard/chapter-001-storyboard-v001.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


project = read_json(WORK / "project.json")
assert project["active_canon_version"] == ".manga-studio/canon/versions/chapter-001-canon-v002.json"
assert project["stage_locks"]["CANON_APPROVED"] is True
assert project["stage_locks"]["STORY_LOCKED"] is True
assert project["stage_locks"]["STORYBOARD_APPROVED"] is False
assert project["stage_locks"]["STORYBOARD_LOCKED"] is False
assert project["image_generation_enabled"] is False
assert sha(ROOT / project["active_canon_version"]) == CANON_ACTIVE_SHA

storyboard = read_json(ROOT / STORYBOARD_PATH)
assert storyboard["status"] == "proposed"
assert storyboard["scope"]["page_count"] == 36
assert storyboard["authority"]["active_canon_sha256"] == CANON_ACTIVE_SHA
assert storyboard["approval_boundary"]["storyboard_approved"] is False

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["active_canon_version"] = project["active_canon_version"]
register["active_storyboard_version"] = None
register["summary"]["proposed_canon_versions"] = 0
register["summary"]["approved_active_canon_versions"] = 1
register["summary"]["proposed_canon_corrections"] = 0
register["summary"]["proposed_storyboard_versions"] = 1

authority = register["current_authority"]
authority["active_canon_version"] = project["active_canon_version"]
authority["active_canon_status"] = "approved_active"
authority["active_canon_sha256"] = CANON_ACTIVE_SHA
authority["canon_approval_relative_path"] = CANON_APPROVAL
authority["canon_adoption_decision_relative_path"] = ".manga-studio/decisions/chapter-001-canon-adoption-v002.json"
authority["proposed_canon_version"] = None
authority["proposed_canon_status"] = "adopted_as_active_v002"
authority["proposed_canon_sha256"] = CANON_REVIEW_SHA
authority["storyboard_status"] = "v001_review_ready_not_approved"
authority["proposed_storyboard_version"] = STORYBOARD_PATH
authority["proposed_storyboard_sha256"] = sha(ROOT / STORYBOARD_PATH)
authority["storyboard_review_relative_path"] = ".manga-studio/analysis/consistency/chapter-001-storyboard-v001-review.md"
authority["storyboard_proposal_decision_relative_path"] = ".manga-studio/decisions/chapter-001-storyboard-proposal-v001.json"
authority["storyboard_approval_required"] = True
authority["reference_generation_release_status"] = "deferred_pending_storyboard_lock_image_enable_and_dependencies"
authority["image_generation_enabled"] = False
authority["active_stage_locks"] = sorted(key for key, value in project["stage_locks"].items() if value)
authority["story_locked"] = True

new_paths = [
    ".manga-studio/analysis/consistency/chapter-001-storyboard-v001-review.json",
    ".manga-studio/analysis/consistency/chapter-001-storyboard-v001-review.md",
    ".manga-studio/approvals/approval-179120b070e94a71a22d4af7677e67b9.json",
    ".manga-studio/decisions/chapter-001-canon-adoption-v002.json",
    ".manga-studio/decisions/chapter-001-storyboard-proposal-v001.json",
    ".manga-studio/locks/CANON_APPROVED-v002.json",
    ".manga-studio/locks/CANON_APPROVED-v003.json",
    ".manga-studio/locks/STORY_LOCKED-v002.json",
    ".manga-studio/locks/STORY_LOCKED-v003.json",
    ".manga-studio/maintenance/storyboard-v001/build.py",
    ".manga-studio/maintenance/storyboard-v001/finalize.py",
    ".manga-studio/maintenance/storyboard-v001/validation.json",
    ".manga-studio/maintenance/remote-reconciliation-v001/record.json",
    ".manga-studio/storyboard/chapter-001-page-turns-v001.md",
    ".manga-studio/storyboard/chapter-001-pages-001-009-v001.md",
    ".manga-studio/storyboard/chapter-001-pages-010-018-v001.md",
    ".manga-studio/storyboard/chapter-001-pages-019-027-v001.md",
    ".manga-studio/storyboard/chapter-001-pages-028-036-v001.md",
    ".manga-studio/storyboard/chapter-001-storyboard-v001.json",
    ".manga-studio/storyboard/chapter-001-storyboard-v001.md",
    "manga/03-story/arc-01/chapter-001/page-map.md",
]

by_path = {row["relative_path"]: row for row in register["artifacts"]}
for relative in new_paths:
    by_path.setdefault(relative, {"relative_path": relative, "evidence": []})

for relative, row in by_path.items():
    path = ROOT / relative
    if not path.is_file():
        raise FileNotFoundError(relative)
    row["sha256"] = sha(path)

register["artifacts"] = [by_path[key] for key in sorted(by_path)]
write_json(REGISTER, register)

print(json.dumps({
    "status": "pass",
    "active_canon": authority["active_canon_version"],
    "canon_sha256": authority["active_canon_sha256"],
    "storyboard": authority["proposed_storyboard_version"],
    "storyboard_sha256": authority["proposed_storyboard_sha256"],
    "storyboard_approved": False,
    "storyboard_locked": False,
    "image_generation_enabled": False,
    "registered_artifacts": len(register["artifacts"]),
}, indent=2))
