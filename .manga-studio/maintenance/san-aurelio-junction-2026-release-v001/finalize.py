"""Register the first released environment-reference job and IMAGE_READY lock."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
CONTINUITY = ".manga-studio/continuity/state.json"
CONTINUITY_SHA = "388cf8f31be36a63c24e50e119ed2e517b753d7f5b37ad1a6d0c983f7b7b3ca3"
CONTINUITY_APPROVAL = ".manga-studio/approvals/approval-8a03736f527b4df5aefcc46fa8578650.json"
IMAGE_READY_LOCK = ".manga-studio/locks/IMAGE_READY-v001.json"
JOB = ".manga-studio/handoff/pending/san-aurelio-junction-2026-v001.json"
HANDOFF = ".manga-studio/handoff/pending/san-aurelio-junction-2026-v001.md"
SOURCE_BRIEF = "manga/02-references/environments/san-aurelio-junction/san-aurelio-junction-2026-reference-generation.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


project = read_json(WORK / "project.json")
continuity = read_json(ROOT / CONTINUITY)
approval = read_json(ROOT / CONTINUITY_APPROVAL)
lock = read_json(ROOT / IMAGE_READY_LOCK)
job = read_json(ROOT / JOB)

assert project["workflow_phase"] == "phase_7_san_aurelio_junction_2026_released"
assert project["image_generation_enabled"] is True
assert project["stage_locks"]["IMAGE_READY"] is True
assert project["stage_lock_records"]["IMAGE_READY"] == IMAGE_READY_LOCK
assert continuity["project_id"] == project["project_id"]
assert sha(ROOT / CONTINUITY) == CONTINUITY_SHA
assert approval["status"] == approval["decision"] == "approved"
assert approval["target_relative_path"] == CONTINUITY
assert approval["target_sha256"] == CONTINUITY_SHA
assert lock["gate"] == "IMAGE_READY" and lock["status"] == "locked"
assert lock["approval_ids"] == [approval["approval_id"]]
assert lock["target_hashes"] == [{"relative_path": CONTINUITY, "sha256": CONTINUITY_SHA}]
assert job["job_id"] == "san-aurelio-junction-2026-v001"
assert job["job_type"] == "location_reference"
assert job["release_status"] == "released" and not job["blocking_reasons"]
assert job["required_reference_images"] == [] and job["reference_priority"] == []
assert job["output_filename"] == ".manga-studio/handoff/generated/san-aurelio-junction-2026.png"
assert (ROOT / HANDOFF).is_file()
assert "No reference-image attachments are required for this job." in (ROOT / HANDOFF).read_text(encoding="utf-8")

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["deferred_reference_generation_briefs"] = 7
register["summary"]["released_reference_jobs"] = 1

authority = register["current_authority"]
authority["active_stage_locks"] = sorted(key for key, value in project["stage_locks"].items() if value)
authority["image_generation_enabled"] = True
authority["image_ready"] = True
authority["continuity_state_relative_path"] = CONTINUITY
authority["continuity_state_sha256"] = CONTINUITY_SHA
authority["continuity_approval_relative_path"] = CONTINUITY_APPROVAL
authority["image_ready_lock_relative_path"] = IMAGE_READY_LOCK
authority["reference_generation_release_status"] = "san_aurelio_junction_2026_released"
authority["released_reference_job_relative_path"] = JOB
authority["released_reference_job_sha256"] = sha(ROOT / JOB)
authority["released_reference_handoff_relative_path"] = HANDOFF
authority["released_reference_handoff_sha256"] = sha(ROOT / HANDOFF)
authority["released_reference_source_brief_relative_path"] = SOURCE_BRIEF
authority["released_reference_source_brief_sha256"] = sha(ROOT / SOURCE_BRIEF)
authority["remaining_deferred_reference_generation_briefs"] = authority["deferred_reference_generation_briefs"][6:]

new_paths = [
    CONTINUITY,
    CONTINUITY_APPROVAL,
    IMAGE_READY_LOCK,
    JOB,
    HANDOFF,
    ".manga-studio/maintenance/san-aurelio-junction-2026-release-v001/finalize.py",
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
    "image_generation_enabled": True,
    "image_ready": True,
    "job": JOB,
    "job_sha256": sha(ROOT / JOB),
    "handoff": HANDOFF,
    "handoff_sha256": sha(ROOT / HANDOFF),
    "attachments_required": 0,
}, indent=2))
