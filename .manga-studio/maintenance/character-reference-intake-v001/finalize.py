"""Finalize the approved Daniel-and-Tomas shared reference intake."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
HERE = Path(__file__).resolve().parent
BEFORE = WORK / "history/character-reference-intake-v001/before"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


entries = []
for path in sorted(BEFORE.rglob("*")):
    if not path.is_file() or path.name.startswith("._"):
        continue
    entries.append(
        {
            "original_relative_path": path.relative_to(BEFORE).as_posix(),
            "archived_relative_path": path.relative_to(ROOT).as_posix(),
            "sha256": sha(path),
        }
    )

relocations = {
    "record_type": "character_reference_intake_v001_relocations",
    "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "reason": "Preserve the exact pre-intake working state before registering the user-supplied Daniel-and-Tomas character reference.",
    "entries": entries,
}
write_json(HERE / "relocations.json", relocations)

register = json.loads(REGISTER.read_text(encoding="utf-8"))
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["approved_reference_sets"] = 1
register["summary"]["approved_reference_files"] = 2
authority = register["current_authority"]
authority["approved_visual_references"] = [
    {
        "reference_id": "reference-daniel-tomas-shared-v001",
        "scope": "Daniel and Tomas adult identity, hair, build, age impression, Daniel's glasses, shared scale and visual chemistry only",
        "webp_relative_path": "manga/02-references/approved-webp/daniel-tomas-shared.webp",
        "webp_sha256": "985cb554a78cca3367845b7cea089fee230f950629ae2da67d6c2fe90fd45ceb",
        "png_relative_path": "manga/02-references/approve-png/daniel-tomas-shared.png",
        "png_sha256": "48f2680a489156033f49b11f5a7c02a7a0e92e0442a3a60fc2bc1487cd1bf2b6",
        "reference_record_relative_path": ".manga-studio/continuity/references/daniel-tomas-shared-v001.json",
    }
]

by_path = {row["relative_path"]: row for row in register["artifacts"]}
new_paths = [
    ".manga-studio/approvals/approval-68dbddb1b25b43df8ecd0db11b1d86ee.json",
    ".manga-studio/approvals/approval-f06708bac3194fed87dd9f57e10bc2ca.json",
    ".manga-studio/continuity/references/daniel-tomas-shared-v001.json",
    ".manga-studio/continuity/reviews/chapter-001-daniel-tomas-shared-reference-v001-review.json",
    ".manga-studio/continuity/reviews/chapter-001-daniel-tomas-shared-reference-v001-review.md",
    ".manga-studio/decisions/chapter-001-daniel-tomas-shared-reference-v001.json",
    ".manga-studio/history/character-reference-intake-v001/source/daniel-tomas-shared-v001.webp",
    ".manga-studio/maintenance/character-reference-intake-v001/finalize.py",
    ".manga-studio/maintenance/character-reference-intake-v001/relocations.json",
    "manga/02-references/approve-png/daniel-tomas-shared.png",
    "manga/02-references/approved-webp/daniel-tomas-shared.webp",
]
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
            "backups_recorded": len(entries),
            "working_artifacts_hashed": len(register["artifacts"]),
            "approved_reference_sets": register["summary"]["approved_reference_sets"],
            "approved_reference_files": register["summary"]["approved_reference_files"],
            "reference_id": authority["approved_visual_references"][0]["reference_id"],
        },
        indent=2,
    )
)
