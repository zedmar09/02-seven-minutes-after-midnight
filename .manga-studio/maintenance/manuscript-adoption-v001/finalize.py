"""Finalize hash manifests for the Chapter 1 manuscript-adoption update."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
HERE = Path(__file__).resolve().parent
BEFORE = WORK / "history/manuscript-adoption-v001/before"
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
    "record_type": "manuscript_adoption_relocations",
    "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "reason": "Preserve the exact pre-adoption working files before activating the approved Chapter 1 manuscript and recording the approved visual-quality direction.",
    "entries": entries,
}
write_json(HERE / "relocations.json", relocations)

register = json.loads(REGISTER.read_text(encoding="utf-8"))
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["active_manuscript_version"] = ".manga-studio/manuscript/versions/chapter-001-v001.md"
register["current_authority"] = {
    "manuscript_status": "approved_active",
    "manuscript_sha256": "f195b7e0afc7f875731ade728a1bbf7a28d7becf3f38fa2d920498231f65d500",
    "approval_relative_path": ".manga-studio/approvals/approval-feb5212823b84aeaaa04bac3fedc4fc6.json",
    "visual_quality_decision_relative_path": ".manga-studio/decisions/chapter-001-quality-direction-v001.json",
    "provisional_interior_pages": 36,
    "working_page_range": [32, 40],
    "stage_locks_changed": False,
    "image_generation_enabled": False,
}

by_path = {row["relative_path"]: row for row in register["artifacts"]}
new_paths = [
    ".manga-studio/analysis/chapter-001-visual-quality-audit-v001.md",
    ".manga-studio/approvals/approval-feb5212823b84aeaaa04bac3fedc4fc6.json",
    ".manga-studio/decisions/chapter-001-quality-direction-v001.json",
    ".manga-studio/manuscript/versions/chapter-001-v001.metadata.json",
    ".manga-studio/maintenance/manuscript-adoption-v001/finalize.py",
    ".manga-studio/maintenance/manuscript-adoption-v001/relocations.json",
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
            "active_manuscript_version": register["active_manuscript_version"],
        },
        indent=2,
    )
)
