"""Register the approval-ready review of the author-submitted San Aurelio Junction v007 retry."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
CANDIDATE = ".manga-studio/continuity/reference-candidates/san-aurelio-junction-2026-v007/candidate.png"
CANDIDATE_SHA = "03f1f97fd44ba5ffafbe0c03cd0feded14be5e03d09dd505fb02669c5a1831a8"
INTAKE = ".manga-studio/continuity/reference-candidates/san-aurelio-junction-2026-v007/intake.json"
REVIEW_JSON = ".manga-studio/continuity/reviews/chapter-001-san-aurelio-junction-2026-reference-v007-review.json"
REVIEW_MD = ".manga-studio/continuity/reviews/chapter-001-san-aurelio-junction-2026-reference-v007-review.md"
LAST_RELEASED_JOB = ".manga-studio/handoff/pending/san-aurelio-junction-2026-v003.json"
STYLE_MANIFEST = ".manga-studio/references/printed-manga-finish-v001/manifest.json"
FINALIZER = ".manga-studio/maintenance/san-aurelio-junction-2026-review-v006/finalize.py"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


project = read_json(WORK / "project.json")
intake = read_json(ROOT / INTAKE)
review = read_json(ROOT / REVIEW_JSON)
job = read_json(ROOT / LAST_RELEASED_JOB)
manifest = read_json(ROOT / STYLE_MANIFEST)

assert project["workflow_phase"] == "phase_7_san_aurelio_junction_2026_candidate_v007_review_ready"
assert project["image_generation_enabled"] is True
assert project["stage_locks"]["IMAGE_READY"] is True
assert sha(ROOT / CANDIDATE) == CANDIDATE_SHA
assert intake["result"] == "review_ready_visual_pass"
assert intake["approval_recommended"] is True and intake["approved"] is False
assert intake["promotion_blocked"] is True
assert intake["retained_candidate"]["encoded_color_space"] == "grayscale"
assert intake["retained_candidate"]["pixel_mode"] == "L"
assert "No v007 image job" in intake["actual_generation_job_provenance"]
assert review["target"] == CANDIDATE and review["status"] == "review_ready"
assert not any(row["severity"] == "error" for row in review["findings"])
assert any(row["code"] == "SAN-AURELIO-2026-V007-CLOCK-001" for row in review["findings"])
assert any(row["code"] == "SAN-AURELIO-2026-V007-FINISH-001" for row in review["findings"])
assert job["job_id"] == "san-aurelio-junction-2026-v003"
assert job["release_status"] == "released" and job["job_type"] == "correction"
assert sha(ROOT / LAST_RELEASED_JOB) == intake["comparison_evidence"]["last_released_requirement_job"]["sha256"]
assert manifest["status"] == "author_selected_for_finish_guidance"
assert len(manifest["references"]) == 2
for version in ("v007", "v008"):
    assert not (WORK / f"handoff/pending/san-aurelio-junction-2026-{version}.json").exists()
    assert not (WORK / f"handoff/pending/san-aurelio-junction-2026-{version}.md").exists()

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["generated_reference_candidates"] = 6
register["summary"]["reference_candidates_changes_requested"] = 5
register["summary"]["reference_candidates_review_ready"] = 1
register["summary"]["reference_candidates_approval_recommended"] = 1

authority = register["current_authority"]
authority["reference_generation_release_status"] = "san_aurelio_junction_2026_v007_review_ready_approval_recommended_not_approved"
authority["latest_generated_reference_review_relative_path"] = REVIEW_JSON
authority["san_aurelio_junction_2026_v006_candidate_relative_path"] = ".manga-studio/continuity/reference-candidates/san-aurelio-junction-2026-v006/candidate.png"
authority["san_aurelio_junction_2026_v006_candidate_sha256"] = "c84de8fd30a6fe27891873cab4fbbce8b1dcca4513e4bcefee25b13d62c9401f"
authority["san_aurelio_junction_2026_v006_candidate_status"] = "clock_and_grayscale_changes_requested_not_approved"
authority["san_aurelio_junction_2026_candidate_relative_path"] = CANDIDATE
authority["san_aurelio_junction_2026_candidate_sha256"] = CANDIDATE_SHA
authority["san_aurelio_junction_2026_candidate_status"] = "v007_review_ready_approval_recommended_not_approved"
authority["san_aurelio_junction_2026_correction_job_status"] = "v003_executed_changes_requested"
authority["san_aurelio_junction_2026_author_submitted_retry_status"] = "v007_review_ready_approval_required_no_v008_released"
authority["san_aurelio_junction_2026_approval_recommended"] = True
authority["san_aurelio_junction_2026_approval_status"] = "pending_explicit_user_approval"

new_paths = [
    CANDIDATE,
    INTAKE,
    REVIEW_JSON,
    REVIEW_MD,
    FINALIZER,
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
    "candidate_sha256": CANDIDATE_SHA,
    "review_status": review["status"],
    "blocking_findings": 0,
    "clock_12_07_passed": True,
    "manga_finish_passed": True,
    "true_grayscale_passed": True,
    "approval_recommended": True,
    "approved": False,
    "v008_correction_released": False,
}, indent=2))
