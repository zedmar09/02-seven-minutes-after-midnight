"""Register the blocking review of the San Aurelio Junction 2026 v002 return."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
CANDIDATE = ".manga-studio/continuity/reference-candidates/san-aurelio-junction-2026-v002/candidate.png"
CORRECTION_INPUT = ".manga-studio/handoff/approved/correction-inputs/san-aurelio-junction-2026-v002/candidate.png"
CANDIDATE_SHA = "7ef255c1752b482f0cb0e92eb09f08be7b597cc3b779ed2c050dc79ebc814403"
INTAKE = ".manga-studio/continuity/reference-candidates/san-aurelio-junction-2026-v002/intake.json"
REVIEW_JSON = ".manga-studio/continuity/reviews/chapter-001-san-aurelio-junction-2026-reference-v002-review.json"
REVIEW_MD = ".manga-studio/continuity/reviews/chapter-001-san-aurelio-junction-2026-reference-v002-review.md"
STYLE_MANIFEST = ".manga-studio/references/printed-manga-finish-v001/manifest.json"
STYLE_REFERENCES = [
    {
        "reference_id": "printed-manga-finish-action-v001",
        "path": ".manga-studio/handoff/approved/style-guides/printed-manga-finish-v001/flat-ink-action-page.png",
        "sha256": "09d4088f48f684aa7d6acca4168654f0defb31f6959addd743312cb6e4b8a420",
        "approval": ".manga-studio/approvals/approval-f6f235a3d6c64d4f94c04ac6ae74066e.json",
    },
    {
        "reference_id": "printed-manga-finish-dialogue-v001",
        "path": ".manga-studio/handoff/approved/style-guides/printed-manga-finish-v001/flat-ink-dialogue-page.png",
        "sha256": "a1c6c67c208fbf3770f7b9a6b617e17ad689cf4fcd21d3ab931c9617dcddc7fa",
        "approval": ".manga-studio/approvals/approval-d5608c39f41e4d7d8330a60f26a453d8.json",
    },
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


project = read_json(WORK / "project.json")
intake = read_json(ROOT / INTAKE)
review = read_json(ROOT / REVIEW_JSON)
manifest = read_json(ROOT / STYLE_MANIFEST)

assert project["workflow_phase"] == "phase_7_san_aurelio_junction_2026_changes_requested"
assert project["image_generation_enabled"] is True
assert project["stage_locks"]["IMAGE_READY"] is True
assert sha(ROOT / CANDIDATE) == sha(ROOT / CORRECTION_INPUT) == CANDIDATE_SHA
assert intake["result"] == "changes_requested" and intake["approved"] is False
assert review["target"] == CANDIDATE and review["status"] == "changes_requested"
assert any(row["severity"] == "error" for row in review["findings"])
assert manifest["status"] == "author_selected_for_finish_guidance"
assert len(manifest["references"]) == len(STYLE_REFERENCES) == 2
for expected in STYLE_REFERENCES:
    assert sha(ROOT / expected["path"]) == expected["sha256"]
    approval = read_json(ROOT / expected["approval"])
    assert approval["status"] == approval["decision"] == "approved"
    assert approval["target_relative_path"] == expected["path"]
    assert approval["target_sha256"] == expected["sha256"]
assert not (WORK / "handoff/pending/san-aurelio-junction-2026-v003.json").exists()
assert not (WORK / "handoff/pending/san-aurelio-junction-2026-v003.md").exists()

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["generated_reference_candidates"] = 1
register["summary"]["reference_candidates_changes_requested"] = 1
register["summary"]["approved_style_finish_references"] = 2

authority = register["current_authority"]
authority["reference_generation_release_status"] = "san_aurelio_junction_2026_v002_changes_requested_no_correction_released"
authority["latest_generated_reference_review_relative_path"] = REVIEW_JSON
authority["san_aurelio_junction_2026_candidate_relative_path"] = CANDIDATE
authority["san_aurelio_junction_2026_candidate_sha256"] = CANDIDATE_SHA
authority["san_aurelio_junction_2026_candidate_status"] = "changes_requested_not_approved"
authority["san_aurelio_junction_2026_correction_input_relative_path"] = CORRECTION_INPUT
authority["printed_manga_finish_manifest_relative_path"] = STYLE_MANIFEST
authority["printed_manga_finish_manifest_sha256"] = sha(ROOT / STYLE_MANIFEST)
authority["approved_style_finish_references"] = STYLE_REFERENCES
authority["san_aurelio_junction_2026_correction_job_status"] = "not_released"

new_paths = [
    CANDIDATE,
    CORRECTION_INPUT,
    INTAKE,
    REVIEW_JSON,
    REVIEW_MD,
    STYLE_MANIFEST,
    *(row["path"] for row in STYLE_REFERENCES),
    *(row["approval"] for row in STYLE_REFERENCES),
    ".manga-studio/maintenance/san-aurelio-junction-2026-review-v001/finalize.py",
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
    "approval_recommended": False,
    "style_finish_references": len(STYLE_REFERENCES),
    "correction_job_released": False,
}, indent=2))
