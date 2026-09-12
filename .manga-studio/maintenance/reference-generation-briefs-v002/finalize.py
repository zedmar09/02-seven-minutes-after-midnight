"""Register and validate the corrected Chapter 1 reference brief package."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
HERE = Path(__file__).resolve().parent
BEFORE = WORK / "history/reference-generation-briefs-v002/before"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"

BRIEF_PATHS = [
    "manga/02-references/characters/daniel-soriano/daniel-soriano-reference-generation.md",
    "manga/02-references/characters/tomas-rivera/tomas-rivera-reference-generation.md",
    "manga/02-references/characters/maribel-santos/maribel-santos-reference-generation.md",
    "manga/02-references/characters/arturo-salcedo/arturo-salcedo-reference-generation.md",
    "manga/02-references/characters/lilia-ramos/lilia-ramos-reference-generation.md",
    "manga/02-references/environments/san-aurelio-junction/san-aurelio-junction-2026-reference-generation.md",
    "manga/02-references/environments/san-aurelio-junction/san-aurelio-junction-1986-reference-generation.md",
    "manga/02-references/environments/cafe-siete/cafe-siete-dual-era-floor-plan-reference-generation.md",
    "manga/02-references/environments/cafe-siete/cafe-siete-dual-era-perspective-reference-generation.md",
    "manga/02-references/environments/municipal-museum-archive/municipal-museum-archive-reference-generation.md",
    "manga/02-references/objects/cafe-and-archive-props/time-transfer-props-reference-generation.md",
    "manga/02-references/objects/cafe-and-archive-props/clocks-signage-door-reference-generation.md",
    "manga/02-references/objects/temporal-phenomena/time-slip-and-aging-reference-generation.md",
]

UPDATED_INDEXES = [
    "AGENTS.md",
    ".manga-studio/project.json",
    "manga/02-references/README.md",
    "manga/02-references/characters/README.md",
    "manga/02-references/environments/README.md",
    "manga/02-references/objects/README.md",
    "manga/03-story/arc-01/chapter-001/reference-needs.md",
]

PACKAGE_RECORDS = [
    ".manga-studio/analysis/chapter-001-reference-prompt-style-audit-v001.md",
    ".manga-studio/continuity/reviews/chapter-001-reference-generation-briefs-v002-review.json",
    ".manga-studio/continuity/reviews/chapter-001-reference-generation-briefs-v002-review.md",
    ".manga-studio/decisions/chapter-001-reference-generation-briefs-v002.json",
    ".manga-studio/maintenance/reference-generation-briefs-v002/finalize.py",
    ".manga-studio/maintenance/reference-generation-briefs-v002/relocations.json",
    ".manga-studio/maintenance/reference-generation-briefs-v002/validation.json",
    ".manga-studio/maintenance/structure-cleanup-v001/verify.py",
]

PRINTED_MANGA_LOCK = (
    "black-and-white human-drawn 2D manga production "
    "sketch/reference sheet on white paper"
)
LEAD_ATTACHMENT = "../../approve-png/daniel-tomas-shared.png"
LEAD_HASH = "48f2680a489156033f49b11f5a7c02a7a0e92e0442a3a60fc2bc1487cd1bf2b6"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


now = datetime.now(timezone.utc).isoformat()
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

assert entries, "Missing pre-update history snapshot"
write_json(
    HERE / "relocations.json",
    {
        "record_type": "reference_generation_briefs_v002_relocations",
        "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
        "created_at": now,
        "reason": "Preserve the exact pre-correction references, indexes, project instructions, working register, and verifier before adopting thirteen corrected deferred Chapter 1 reference-generation briefs.",
        "entries": entries,
    },
)

texts = {}
for relative in BRIEF_PATHS:
    path = ROOT / relative
    if not path.is_file():
        raise FileNotFoundError(relative)
    texts[relative] = path.read_text(encoding="utf-8")
    assert PRINTED_MANGA_LOCK in texts[relative], relative
    assert "image_generation_enabled" in texts[relative], relative

lead_paths = BRIEF_PATHS[:2]
for relative in lead_paths:
    assert LEAD_ATTACHMENT in texts[relative], relative
    assert LEAD_HASH in texts[relative], relative

for relative in BRIEF_PATHS[2:]:
    assert LEAD_ATTACHMENT not in texts[relative], relative

validation = {
    "record_type": "reference_generation_briefs_v002_validation",
    "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
    "checked_at": now,
    "status": "pass",
    "briefs_verified": len(BRIEF_PATHS),
    "printed_manga_reference_lock": "pass",
    "lead_identity_attachment_scope": "pass",
    "supporting_character_attachment_scope": "pass",
    "dependency_attachment_policy": "approved_hash_bound_predecessors_only",
    "release_status": "deferred",
    "artwork_created": False,
    "structured_image_jobs_created": False,
    "stage_locks_changed": False,
    "image_generation_enabled": False,
    "brief_hashes": [
        {"relative_path": relative, "sha256": sha(ROOT / relative)}
        for relative in BRIEF_PATHS
    ],
}
write_json(HERE / "validation.json", validation)

register = json.loads(REGISTER.read_text(encoding="utf-8"))
register["updated_at"] = now
register["post_cleanup_working_files"] = sorted(BRIEF_PATHS)
register["summary"]["working_markdown_files"] = sum(
    1
    for path in (ROOT / "manga").rglob("*.md")
    if path.is_file() and not path.name.startswith("._")
)
register["summary"]["deferred_reference_generation_briefs"] = len(BRIEF_PATHS)
register["intentional_differences"] = [
    "Story-specific character and location slugs.",
    "Thirteen story-specific reference-generation briefs are deferred; no c001-p### prompt exists because no storyboard or page job is adopted.",
    "Only the user-approved shared Daniel-and-Tomas PNG/WebP identity input is present; no environment, prop, effect, or supporting-character artwork has been generated.",
    "Only historical/runtime-required internal directories; no copied history IDs or foreign assets.",
]

authority = register["current_authority"]
authority["reference_generation_briefs_version"] = "v002"
authority["reference_generation_briefs_decision_relative_path"] = ".manga-studio/decisions/chapter-001-reference-generation-briefs-v002.json"
authority["reference_prompt_style_audit_relative_path"] = ".manga-studio/analysis/chapter-001-reference-prompt-style-audit-v001.md"
authority["reference_generation_release_status"] = "deferred"
authority["deferred_reference_generation_briefs"] = BRIEF_PATHS
authority["reference_rendering_lock"] = "clean_flat_black_and_white_printed_manga_reference_on_white_paper"
authority["reference_attachment_policy"] = "identity_and_approved_hash_bound_dependencies_only"
authority["reference_artwork_created_by_brief_update"] = False
authority["stage_locks_changed_by_brief_update"] = False
authority["image_generation_enabled_by_brief_update"] = False

by_path = {row["relative_path"]: row for row in register["artifacts"]}
for relative in BRIEF_PATHS + UPDATED_INDEXES + PACKAGE_RECORDS:
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
