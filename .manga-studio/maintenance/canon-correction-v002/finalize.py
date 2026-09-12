"""Register canon v002 as an inactive one-fact correction proposal."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
HERE = Path(__file__).resolve().parent
BEFORE = WORK / "history/canon-correction-v002/before"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"
V001_SHA256 = "8e99db551f9eda9f3b56116b15cd6425a807d27b439df3a493864385612cfb58"
V002_SHA256 = "897ed992c1106ee39b10f903019a4eb24fd9a51309cc69960e7505d7c9365725"
EXPECTED_WARNING = (
    "The 2026 cafe door glass is painted over. The name TOMAS is already scratched "
    "into it, and after closure dust reveals the separate warning FIRE STARTS IN THE "
    "SERVICE CORRIDOR."
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


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
    "record_type": "canon_correction_v002_relocations",
    "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "reason": "Preserve the exact pre-correction project guidance, project state, working register, and verifier before registering canon v002.",
    "entries": entries,
}
write_json(HERE / "relocations.json", relocations)

v001_path = WORK / "canon/versions/chapter-001-canon-v001.json"
v002_path = WORK / "canon/versions/chapter-001-canon-v002.json"
v001 = read_json(v001_path)
v002 = read_json(v002_path)
if sha(v001_path) != V001_SHA256 or v001["status"] != "approved":
    raise ValueError("Approved canon v001 changed or is no longer approved.")
if sha(v002_path) != V002_SHA256 or v002["status"] != "proposed":
    raise ValueError("Canon v002 must remain the exact proposed correction.")

v001_comparable = dict(v001)
v002_comparable = dict(v002)
for value in (v001_comparable, v002_comparable):
    value.pop("canon_id")
    value.pop("version")
    value.pop("status")
v001_fact = next(row for row in v001_comparable["confirmed_facts"] if row["fact_id"] == "canon-fact-ch001-023")
v002_fact = next(row for row in v002_comparable["confirmed_facts"] if row["fact_id"] == "canon-fact-ch001-023")
v001_fact["value"] = EXPECTED_WARNING
if v001_comparable != v002_comparable or v002_fact["value"] != EXPECTED_WARNING:
    raise ValueError("Canon v002 changes more than the reviewed warning correction.")

project = read_json(WORK / "project.json")
expected_true_locks = {
    "SOURCE_LOCKED",
    "CANON_APPROVED",
    "DIAGNOSTIC_APPROVED",
    "REVISION_PLAN_APPROVED",
    "MANUSCRIPT_APPROVED",
    "STORY_LOCKED",
}
actual_true_locks = {key for key, value in project["stage_locks"].items() if value}
if actual_true_locks != expected_true_locks:
    raise ValueError(f"Unexpected active lock set: {sorted(actual_true_locks)}")
if project["active_canon_version"] != ".manga-studio/canon/versions/chapter-001-canon-v001.json":
    raise ValueError("Canon v002 must remain inactive until separate approval.")
if project["active_storyboard_version"] is not None or project["image_generation_enabled"]:
    raise ValueError("Storyboard and image generation must remain inactive.")

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["proposed_canon_versions"] = 1
register["summary"]["approved_active_canon_versions"] = 1
register["summary"]["proposed_canon_corrections"] = 1
authority = register["current_authority"]
authority["stage_locks_changed"] = True
authority["active_stage_locks"] = sorted(expected_true_locks)
authority["story_locked"] = True
authority["active_canon_version"] = ".manga-studio/canon/versions/chapter-001-canon-v001.json"
authority["active_canon_status"] = "approved_active"
authority["active_canon_sha256"] = V001_SHA256
authority["canon_approval_relative_path"] = ".manga-studio/approvals/approval-84d84d30ba764d1b845e80a28d88a628.json"
authority["proposed_canon_version"] = ".manga-studio/canon/versions/chapter-001-canon-v002.json"
authority["proposed_canon_status"] = "correction_proposed_review_ready"
authority["proposed_canon_sha256"] = V002_SHA256
authority["proposed_canon_decision_relative_path"] = ".manga-studio/decisions/chapter-001-canon-correction-proposal-v002.json"
authority["canon_adopted_by_proposal_update"] = True
authority["stage_locks_changed_by_canon_proposal_update"] = True
authority["image_generation_enabled_by_canon_proposal_update"] = False
authority["storyboard_status"] = "blocked_pending_canon_v002_approval_and_relock"
authority["image_generation_enabled"] = False

by_path = {row["relative_path"]: row for row in register["artifacts"]}
new_paths = [
    "AGENTS.md",
    ".manga-studio/project.json",
    ".manga-studio/analysis/consistency/chapter-001-canon-v002-review.md",
    ".manga-studio/canon/versions/chapter-001-canon-v002.json",
    ".manga-studio/decisions/chapter-001-canon-correction-proposal-v002.json",
    ".manga-studio/maintenance/canon-correction-v002/finalize.py",
    ".manga-studio/maintenance/canon-correction-v002/relocations.json",
    ".manga-studio/maintenance/canon-correction-v002/validation.json",
    ".manga-studio/maintenance/structure-cleanup-v001/verify.py",
]
new_paths += [path.relative_to(ROOT).as_posix() for path in sorted((WORK / "approvals").glob("approval-*.json"))]
new_paths += [path.relative_to(ROOT).as_posix() for path in sorted((WORK / "locks").glob("*-v001.json"))]
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
            "active_canon": authority["active_canon_version"],
            "proposed_correction": authority["proposed_canon_version"],
            "proposed_sha256": V002_SHA256,
            "storyboard_blocked": True,
            "image_generation_enabled": False,
        },
        indent=2,
    )
)
