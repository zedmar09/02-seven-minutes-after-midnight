"""Finalize hash manifests for visual-quality direction v002."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
HERE = Path(__file__).resolve().parent
BEFORE = WORK / "history/visual-quality-direction-v002/before"
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
    "record_type": "visual_quality_direction_v002_relocations",
    "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "reason": "Preserve the exact v001 working state before adopting variable panel totals and controlled overlap as visual-quality direction v002.",
    "entries": entries,
}
write_json(HERE / "relocations.json", relocations)

register = json.loads(REGISTER.read_text(encoding="utf-8"))
register["updated_at"] = datetime.now(timezone.utc).isoformat()
authority = register["current_authority"]
authority["visual_quality_decision_relative_path"] = ".manga-studio/decisions/chapter-001-quality-direction-v002.json"
authority["visual_quality_direction_version"] = "v002"
authority["panel_count_policy"] = "situation_driven_no_fixed_total"
authority["controlled_overlap_allowed"] = True
authority["overlap_requirements"] = [
    "explicit_reading_sequence",
    "frame_or_clip_geometry",
    "z_index",
    "overlap_permission",
    "focus_point",
    "dialogue_safe_zones",
    "continuity_clearance",
]

by_path = {row["relative_path"]: row for row in register["artifacts"]}
new_paths = [
    ".manga-studio/analysis/chapter-001-visual-quality-audit-v002.md",
    ".manga-studio/decisions/chapter-001-quality-direction-v002.json",
    ".manga-studio/maintenance/visual-quality-direction-v002/finalize.py",
    ".manga-studio/maintenance/visual-quality-direction-v002/relocations.json",
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
            "visual_quality_direction_version": authority["visual_quality_direction_version"],
            "panel_count_policy": authority["panel_count_policy"],
            "controlled_overlap_allowed": authority["controlled_overlap_allowed"],
        },
        indent=2,
    )
)
