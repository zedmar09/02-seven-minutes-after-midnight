"""Register the review of the author-submitted San Aurelio Junction v006 retry."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
CANDIDATE = ".manga-studio/continuity/reference-candidates/san-aurelio-junction-2026-v006/candidate.png"
CORRECTION_INPUT = ".manga-studio/handoff/approved/correction-inputs/san-aurelio-junction-2026-v006/candidate.png"
CANDIDATE_SHA = "c84de8fd30a6fe27891873cab4fbbce8b1dcca4513e4bcefee25b13d62c9401f"
INTAKE = ".manga-studio/continuity/reference-candidates/san-aurelio-junction-2026-v006/intake.json"
REVIEW_JSON = ".manga-studio/continuity/reviews/chapter-001-san-aurelio-junction-2026-reference-v006-review.json"
REVIEW_MD = ".manga-studio/continuity/reviews/chapter-001-san-aurelio-junction-2026-reference-v006-review.md"
LAST_RELEASED_JOB = ".manga-studio/handoff/pending/san-aurelio-junction-2026-v003.json"
STYLE_MANIFEST = ".manga-studio/references/printed-manga-finish-v001/manifest.json"
FINALIZER = ".manga-studio/maintenance/san-aurelio-junction-2026-review-v005/finalize.py"


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

assert project["workflow_phase"] == "phase_7_san_aurelio_junction_2026_candidate_v006_clock_and_grayscale_changes_requested"
assert project["image_generation_enabled"] is True
assert project["stage_locks"]["IMAGE_READY"] is True
assert sha(ROOT / CANDIDATE) == sha(ROOT / CORRECTION_INPUT) == CANDIDATE_SHA
assert intake["result"] == "changes_requested" and intake["approved"] is False
assert intake["retained_candidate"]["encoded_color_space"] == "RGB"
assert "No v006 image job" in intake["actual_generation_job_provenance"]
assert review["target"] == CANDIDATE and review["status"] == "changes_requested"
error_codes = {row["code"] for row in review["findings"] if row["severity"] == "error"}
assert error_codes == {
    "SAN-AURELIO-2026-V006-CLOCK-001",
    "SAN-AURELIO-2026-V006-FORMAT-001",
}
assert any(row["code"] == "SAN-AURELIO-2026-V006-FINISH-001" for row in review["findings"])
assert job["job_id"] == "san-aurelio-junction-2026-v003"
assert job["release_status"] == "released" and job["job_type"] == "correction"
assert sha(ROOT / LAST_RELEASED_JOB) == intake["comparison_evidence"]["last_released_requirement_job"]["sha256"]
assert manifest["status"] == "author_selected_for_finish_guidance"
assert len(manifest["references"]) == 2
for version in ("v006", "v007"):
    assert not (WORK / f"handoff/pending/san-aurelio-junction-2026-{version}.json").exists()
    assert not (WORK / f"handoff/pending/san-aurelio-junction-2026-{version}.md").exists()

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["generated_reference_candidates"] = 5
register["summary"]["reference_candidates_changes_requested"] = 5

authority = register["current_authority"]
authority["reference_generation_release_status"] = "san_aurelio_junction_2026_v006_clock_and_grayscale_changes_requested_no_v007_released"
authority["latest_generated_reference_review_relative_path"] = REVIEW_JSON
authority["san_aurelio_junction_2026_v005_candidate_relative_path"] = ".manga-studio/continuity/reference-candidates/san-aurelio-junction-2026-v005/candidate.png"
authority["san_aurelio_junction_2026_v005_candidate_sha256"] = "fb6dd01e53366781c537fa65275ad1e7831cc47dff69da5bb7311d5da0cb27be"
authority["san_aurelio_junction_2026_v005_candidate_status"] = "clock_changes_requested_not_approved"
authority["san_aurelio_junction_2026_candidate_relative_path"] = CANDIDATE
authority["san_aurelio_junction_2026_candidate_sha256"] = CANDIDATE_SHA
authority["san_aurelio_junction_2026_candidate_status"] = "v006_clock_and_grayscale_changes_requested_not_approved"
authority["san_aurelio_junction_2026_correction_input_relative_path"] = CORRECTION_INPUT
authority["san_aurelio_junction_2026_correction_job_status"] = "v003_executed_changes_requested"
authority["san_aurelio_junction_2026_author_submitted_retry_status"] = "v006_clock_and_grayscale_changes_requested_no_v007_released"

new_paths = [
    CANDIDATE,
    CORRECTION_INPUT,
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
    "blocking_findings": len(error_codes),
    "manga_finish_passed": True,
    "clock_corrected": False,
    "true_grayscale_passed": False,
    "approval_recommended": False,
    "v007_correction_released": False,
}, indent=2))
