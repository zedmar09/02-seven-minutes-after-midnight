"""Register Chapter 1 storyboard approval and active locks."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
STORYBOARD = ".manga-studio/storyboard/chapter-001-storyboard-v001.json"
STORYBOARD_SHA = "ea431653fe9d7b6cd7f5fed58d219e46116ad16a4e8194bc62740c6babcde107"
STORYBOARD_APPROVAL = ".manga-studio/approvals/approval-c81e30db6a5045ab9afdbc9bd17b0464.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


project = read_json(WORK / "project.json")
storyboard = read_json(ROOT / STORYBOARD)
approval = read_json(ROOT / STORYBOARD_APPROVAL)
assert project["active_storyboard_version"] == STORYBOARD
assert project["stage_locks"]["STORYBOARD_APPROVED"] is True
assert project["stage_locks"]["STORYBOARD_LOCKED"] is True
assert project["image_generation_enabled"] is False
assert storyboard["status"] == "approved"
assert storyboard["approval_boundary"] == {
    "user_approval_required": True,
    "storyboard_approved": True,
    "storyboard_locked": True,
    "panel_direction_authorized": True,
    "image_generation_authorized": False,
}
assert sha(ROOT / STORYBOARD) == STORYBOARD_SHA
assert approval["target_relative_path"] == STORYBOARD
assert approval["target_sha256"] == STORYBOARD_SHA

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["active_storyboard_version"] = STORYBOARD
register["summary"]["proposed_storyboard_versions"] = 0
register["summary"]["approved_active_storyboard_versions"] = 1

authority = register["current_authority"]
authority["storyboard_status"] = "v001_approved_active_locked"
authority["storyboard_approval_required"] = False
authority["proposed_storyboard_version"] = None
authority["preapproval_storyboard_sha256"] = "a03f068d4503ea348c65590d065ee383d695b6ed14a9cd54c72f78a8593f840b"
authority["active_storyboard_version"] = STORYBOARD
authority["active_storyboard_sha256"] = STORYBOARD_SHA
authority["storyboard_approval_relative_path"] = STORYBOARD_APPROVAL
authority["storyboard_approved_lock_relative_path"] = ".manga-studio/locks/STORYBOARD_APPROVED-v001.json"
authority["storyboard_locked_lock_relative_path"] = ".manga-studio/locks/STORYBOARD_LOCKED-v001.json"
authority["active_stage_locks"] = sorted(key for key, value in project["stage_locks"].items() if value)
authority["image_generation_enabled"] = False

new_paths = [
    ".manga-studio/approvals/approval-c81e30db6a5045ab9afdbc9bd17b0464.json",
    ".manga-studio/locks/STORYBOARD_APPROVED-v001.json",
    ".manga-studio/locks/STORYBOARD_LOCKED-v001.json",
    ".manga-studio/maintenance/storyboard-approval-v001/finalize.py",
]
rows = {row["relative_path"]: row for row in register["artifacts"]}
for relative in new_paths:
    rows.setdefault(relative, {"relative_path": relative, "evidence": []})
for relative, row in rows.items():
    row["sha256"] = sha(ROOT / relative)
register["artifacts"] = [rows[key] for key in sorted(rows)]
write_json(REGISTER, register)

print(json.dumps({
    "status": "pass",
    "active_storyboard": STORYBOARD,
    "active_storyboard_sha256": STORYBOARD_SHA,
    "storyboard_approved": True,
    "storyboard_locked": True,
    "panel_direction_authorized": True,
    "image_generation_enabled": False,
}, indent=2))
