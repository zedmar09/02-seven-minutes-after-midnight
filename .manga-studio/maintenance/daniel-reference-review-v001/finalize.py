"""Retain and register the externally generated Daniel reference candidate."""
import hashlib
import json
import shutil
import struct
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
HERE = Path(__file__).resolve().parent
SOURCE = Path("/Users/edmarsanchez/Downloads/daniel-tomas.png")
CANDIDATE = WORK / "continuity/reference-candidates/daniel-soriano-v001/candidate.png"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
BEFORE_REGISTER = WORK / "history/daniel-reference-review-v001/before/.manga-studio/maintenance/structure-cleanup-v001/working-files.json"
EXPECTED_SHA = "134cc5dfbacb0f7a45f859901e86c781da986be11101df63df7c8a7143d13f59"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def png_dimensions(path):
    data = path.read_bytes()[:24]
    assert data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR"
    return struct.unpack(">II", data[16:24])


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


assert SOURCE.is_file()
assert sha(SOURCE) == EXPECTED_SHA
assert png_dimensions(SOURCE) == (1024, 1536)

CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
if CANDIDATE.exists():
    assert sha(CANDIDATE) == EXPECTED_SHA
else:
    shutil.copy2(SOURCE, CANDIDATE)
assert sha(CANDIDATE) == EXPECTED_SHA

BEFORE_REGISTER.parent.mkdir(parents=True, exist_ok=True)
if not BEFORE_REGISTER.exists():
    shutil.copy2(REGISTER, BEFORE_REGISTER)

now = datetime.now(timezone.utc).isoformat()
write_json(
    HERE / "relocations.json",
    {
        "record_type": "daniel_reference_review_v001_relocations",
        "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
        "created_at": now,
        "reason": "Preserve the pre-review working register before recording a non-approved, byte-identical external Daniel reference candidate and its review.",
        "entries": [
            {
                "original_relative_path": ".manga-studio/maintenance/structure-cleanup-v001/working-files.json",
                "archived_relative_path": BEFORE_REGISTER.relative_to(ROOT).as_posix(),
                "sha256": sha(BEFORE_REGISTER),
            }
        ],
    },
)

verification_path = HERE / "verification.json"
write_json(
    verification_path,
    {
        "record_type": "daniel_reference_review_verification",
        "version": "v001",
        "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
        "recorded_at": now,
        "status": "pass",
        "review_result": "changes_requested",
        "source_unchanged": sha(SOURCE) == EXPECTED_SHA,
        "candidate_matches_source": sha(CANDIDATE) == EXPECTED_SHA,
        "dimensions": list(png_dimensions(CANDIDATE)),
        "candidate_approved": False,
        "candidate_promoted": False,
        "artwork_generated_or_edited_by_codex": False,
        "stage_locks_changed": False,
        "image_generation_enabled": False,
    },
)

register = json.loads(REGISTER.read_text(encoding="utf-8"))
register["updated_at"] = now
authority = register["current_authority"]
authority["latest_generated_reference_review_relative_path"] = ".manga-studio/continuity/reviews/chapter-001-daniel-soriano-reference-v001-review.json"
authority["daniel_reference_candidate_relative_path"] = CANDIDATE.relative_to(ROOT).as_posix()
authority["daniel_reference_candidate_sha256"] = EXPECTED_SHA
authority["daniel_reference_candidate_status"] = "changes_requested_not_approved"

new_paths = [
    CANDIDATE.relative_to(ROOT).as_posix(),
    ".manga-studio/continuity/reference-candidates/daniel-soriano-v001/intake.json",
    ".manga-studio/continuity/reviews/chapter-001-daniel-soriano-reference-v001-review.json",
    ".manga-studio/continuity/reviews/chapter-001-daniel-soriano-reference-v001-review.md",
    ".manga-studio/history/daniel-reference-review-v001/before/.manga-studio/maintenance/structure-cleanup-v001/working-files.json",
    ".manga-studio/maintenance/daniel-reference-review-v001/finalize.py",
    ".manga-studio/maintenance/daniel-reference-review-v001/relocations.json",
    ".manga-studio/maintenance/daniel-reference-review-v001/verification.json",
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

print(
    json.dumps(
        {
            "status": "pass",
            "candidate_sha256": EXPECTED_SHA,
            "dimensions": list(png_dimensions(CANDIDATE)),
            "review_result": "changes_requested",
            "candidate_approved": False,
            "working_artifacts_hashed": len(register["artifacts"]),
        },
        indent=2,
    )
)
