"""Register the released San Aurelio Junction 2026 v003 correction packet."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
JOB = ".manga-studio/handoff/pending/san-aurelio-junction-2026-v003.json"
HANDOFF = ".manga-studio/handoff/pending/san-aurelio-junction-2026-v003.md"
PREVIOUS_JOB = ".manga-studio/handoff/pending/san-aurelio-junction-2026-v002.json"
REVIEW = ".manga-studio/continuity/reviews/chapter-001-san-aurelio-junction-2026-reference-v002-review.json"
STYLE_MANIFEST = ".manga-studio/references/printed-manga-finish-v001/manifest.json"
OUTPUT = ".manga-studio/handoff/corrections/san-aurelio-junction-2026-v003.png"
FINALIZER = ".manga-studio/maintenance/san-aurelio-junction-2026-correction-v003/finalize.py"
REFERENCES = [
    {
        "reference_id": "printed-manga-finish-action-v001",
        "path": ".manga-studio/handoff/approved/style-guides/printed-manga-finish-v001/flat-ink-action-page.png",
        "sha256": "09d4088f48f684aa7d6acca4168654f0defb31f6959addd743312cb6e4b8a420",
    },
    {
        "reference_id": "printed-manga-finish-dialogue-v001",
        "path": ".manga-studio/handoff/approved/style-guides/printed-manga-finish-v001/flat-ink-dialogue-page.png",
        "sha256": "a1c6c67c208fbf3770f7b9a6b617e17ad689cf4fcd21d3ab931c9617dcddc7fa",
    },
    {
        "reference_id": "san-aurelio-junction-2026-v002-rejected-architecture",
        "path": ".manga-studio/handoff/approved/correction-inputs/san-aurelio-junction-2026-v002/candidate.png",
        "sha256": "7ef255c1752b482f0cb0e92eb09f08be7b597cc3b779ed2c050dc79ebc814403",
    },
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


runtime = Path.home() / ".agents/skills/.manga-studio-runtime"
installed = runtime / read_json(runtime / "current.json")["version_path"]
sys.path.insert(0, str(installed / "scripts/lib"))
from manga_studio.validation import validate_image_job


project = read_json(WORK / "project.json")
job_path = ROOT / JOB
handoff_path = ROOT / HANDOFF
previous_job_path = ROOT / PREVIOUS_JOB
job = read_json(job_path)

assert project["workflow_phase"] == "phase_7_san_aurelio_junction_2026_correction_v003_released"
assert project["image_generation_enabled"] is True
assert project["stage_locks"]["IMAGE_READY"] is True
errors = validate_image_job(job_path, ROOT, previous_job_path=previous_job_path)
assert not errors, errors
assert job["job_id"] == "san-aurelio-junction-2026-v003"
assert job["job_type"] == "correction"
assert job["revision_of_job_id"] == "san-aurelio-junction-2026-v002"
assert job["release_status"] == "released" and not job["blocking_reasons"]
assert job["output_filename"] == OUTPUT
assert job["output_spec"] == {
    "format": "png",
    "width": 1536,
    "height": 1024,
    "color_mode": "grayscale",
    "alpha_allowed": False,
}
assert not (ROOT / OUTPUT).exists()
assert job["correction_requirements"]["source_review_id"] == "chapter-001-san-aurelio-junction-2026-reference-v002-review"
assert len(job["correction_requirements"]["requested_changes"]) >= 5
assert len(job["correction_requirements"]["preserve_elements"]) >= 5

expected_ids = [row["reference_id"] for row in REFERENCES]
assert job["reference_priority"] == expected_ids
assert len(job["required_reference_images"]) == len(REFERENCES) == 3
attachment_hashes = job["scene_state"]["attachment_hashes"]
for expected, actual in zip(REFERENCES, job["required_reference_images"]):
    assert actual["reference_id"] == expected["reference_id"]
    assert actual["path"] == expected["path"]
    assert actual["locked"] is True
    assert sha(ROOT / expected["path"]) == expected["sha256"]
    assert attachment_hashes[expected["reference_id"]] == expected["sha256"]

source_review = job["scene_state"]["source_review"]
previous_job = job["scene_state"]["previous_job"]
style_package = job["scene_state"]["style_reference_package"]
assert source_review["path"] == REVIEW and sha(ROOT / REVIEW) == source_review["sha256"]
assert previous_job["path"] == PREVIOUS_JOB and sha(previous_job_path) == previous_job["sha256"]
assert style_package["path"] == STYLE_MANIFEST and sha(ROOT / STYLE_MANIFEST) == style_package["sha256"]
review = read_json(ROOT / REVIEW)
assert review["status"] == "changes_requested"
assert any(row["severity"] == "error" for row in review["findings"])

attestation = job["scene_state"]["release_attestation"]
assert attestation["user_authorized_correction_v003"] is True
assert attestation["schema_valid_hash_bound_job_released"] is True
assert attestation["blocking_reasons"] == []
handoff_text = handoff_path.read_text(encoding="utf-8")
assert handoff_text.count(". Attach `") == 3
for filename in ("flat-ink-action-page.png", "flat-ink-dialogue-page.png", "candidate.png"):
    assert f"Attach `{filename}`" in handoff_text
assert "THIS V003 CORRECTION IS RELEASED FOR IMMEDIATE IMAGE GENERATION." in handoff_text
assert "Redraw the sheet from clean line art." in handoff_text

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["released_reference_jobs"] = 1
register["summary"]["released_reference_job_versions"] = 3
register["summary"]["released_correction_jobs"] = 1

authority = register["current_authority"]
authority["reference_generation_release_status"] = "san_aurelio_junction_2026_correction_v003_released"
authority["released_reference_job_relative_path"] = JOB
authority["released_reference_job_sha256"] = sha(job_path)
authority["released_reference_handoff_relative_path"] = HANDOFF
authority["released_reference_handoff_sha256"] = sha(handoff_path)
authority["san_aurelio_junction_2026_correction_job_status"] = "released_v003"
authority["san_aurelio_junction_2026_correction_job_relative_path"] = JOB
authority["san_aurelio_junction_2026_correction_job_sha256"] = sha(job_path)
authority["san_aurelio_junction_2026_correction_handoff_relative_path"] = HANDOFF
authority["san_aurelio_junction_2026_correction_handoff_sha256"] = sha(handoff_path)
authority["san_aurelio_junction_2026_correction_attachments"] = REFERENCES

rows = {row["relative_path"]: row for row in register["artifacts"]}
for relative in (JOB, HANDOFF, FINALIZER):
    rows.setdefault(relative, {"relative_path": relative, "evidence": []})
for relative, row in rows.items():
    row["sha256"] = sha(ROOT / relative)
register["artifacts"] = [rows[key] for key in sorted(rows)]
write_json(REGISTER, register)

print(json.dumps({
    "status": "pass",
    "job": JOB,
    "job_sha256": sha(job_path),
    "handoff": HANDOFF,
    "handoff_sha256": sha(handoff_path),
    "attachments_required": len(REFERENCES),
    "correction_output_exists": False,
}, indent=2))
