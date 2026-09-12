"""Register the deferred Chapter 1 reference-generation brief package."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
HERE = Path(__file__).resolve().parent
BEFORE = WORK / "history/reference-generation-briefs-v001/before"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"


BRIEF_PATHS = [
    "manga/02-references/environments/san-aurelio-junction/san-aurelio-junction-2026-reference-generation.md",
    "manga/02-references/environments/san-aurelio-junction/san-aurelio-junction-1986-reference-generation.md",
    "manga/02-references/environments/cafe-siete/cafe-siete-dual-era-floor-plan-reference-generation.md",
    "manga/02-references/environments/cafe-siete/cafe-siete-dual-era-perspective-reference-generation.md",
    "manga/02-references/environments/municipal-museum-archive/municipal-museum-archive-reference-generation.md",
    "manga/02-references/objects/cafe-and-archive-props/time-transfer-props-reference-generation.md",
    "manga/02-references/objects/cafe-and-archive-props/clocks-signage-door-reference-generation.md",
    "manga/02-references/objects/temporal-phenomena/time-slip-and-aging-reference-generation.md",
]


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
    "record_type": "reference_generation_briefs_v001_relocations",
    "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "reason": "Preserve the exact pre-update indexes, working register, and verifier before adding eight deferred Chapter 1 reference-generation briefs.",
    "entries": entries,
}
write_json(HERE / "relocations.json", relocations)

for relative in BRIEF_PATHS:
    if not (ROOT / relative).is_file():
        raise FileNotFoundError(relative)

register = json.loads(REGISTER.read_text(encoding="utf-8"))
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["post_cleanup_working_files"] = sorted(BRIEF_PATHS)
register["summary"]["working_markdown_files"] = sum(
    1
    for path in (ROOT / "manga").rglob("*.md")
    if path.is_file() and not path.name.startswith("._")
)
register["summary"]["deferred_reference_generation_briefs"] = len(BRIEF_PATHS)
register["intentional_differences"] = [
    "Story-specific character and location slugs.",
    "Eight story-specific reference-generation briefs are deferred; no c001-p### prompt exists because no storyboard or page job is adopted.",
    "Only the user-approved shared Daniel-and-Tomas PNG/WebP reference is present; no environment, prop or effect artwork has been generated.",
    "Only historical/runtime-required internal directories; no copied history IDs or foreign assets.",
]

authority = register["current_authority"]
authority["reference_generation_briefs_version"] = "v001"
authority["reference_generation_briefs_decision_relative_path"] = ".manga-studio/decisions/chapter-001-reference-generation-briefs-v001.json"
authority["reference_generation_release_status"] = "deferred"
authority["deferred_reference_generation_briefs"] = BRIEF_PATHS
authority["reference_artwork_created_by_brief_update"] = False
authority["stage_locks_changed_by_brief_update"] = False
authority["image_generation_enabled_by_brief_update"] = False

by_path = {row["relative_path"]: row for row in register["artifacts"]}
new_paths = BRIEF_PATHS + [
    ".manga-studio/continuity/reviews/chapter-001-reference-generation-briefs-v001-review.json",
    ".manga-studio/continuity/reviews/chapter-001-reference-generation-briefs-v001-review.md",
    ".manga-studio/decisions/chapter-001-reference-generation-briefs-v001.json",
    ".manga-studio/maintenance/reference-generation-briefs-v001/finalize.py",
    ".manga-studio/maintenance/reference-generation-briefs-v001/relocations.json",
    ".manga-studio/maintenance/structure-cleanup-v001/verify.py",
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
            "working_markdown_files": register["summary"]["working_markdown_files"],
            "deferred_reference_generation_briefs": len(BRIEF_PATHS),
            "release_status": authority["reference_generation_release_status"],
        },
        indent=2,
    )
)
