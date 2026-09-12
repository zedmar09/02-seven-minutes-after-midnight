"""Register the proposed Chapter 1 canon without adopting or approving it."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
HERE = Path(__file__).resolve().parent
BEFORE = WORK / "history/canon-proposal-v001/before"
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
    "record_type": "canon_proposal_v001_relocations",
    "project_id": "ms-70391ae1065048cf8bdd564959abd6c3",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "reason": "Preserve the exact pre-proposal working register and verifier before registering inactive Chapter 1 canon v001.",
    "entries": entries,
}
write_json(HERE / "relocations.json", relocations)

canon_path = WORK / "canon/versions/chapter-001-canon-v001.json"
canon = json.loads(canon_path.read_text(encoding="utf-8"))
if canon["status"] != "proposed":
    raise ValueError("Canon proposal must remain proposed until separate user approval.")

register = json.loads(REGISTER.read_text(encoding="utf-8"))
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["proposed_canon_versions"] = 1
authority = register["current_authority"]
authority["proposed_canon_version"] = ".manga-studio/canon/versions/chapter-001-canon-v001.json"
authority["proposed_canon_status"] = "proposed_review_ready"
authority["proposed_canon_decision_relative_path"] = ".manga-studio/decisions/chapter-001-canon-proposal-v001.json"
authority["canon_adopted_by_proposal_update"] = False
authority["stage_locks_changed_by_canon_proposal_update"] = False
authority["image_generation_enabled_by_canon_proposal_update"] = False

by_path = {row["relative_path"]: row for row in register["artifacts"]}
new_paths = [
    ".manga-studio/analysis/consistency/chapter-001-canon-v001-review.md",
    ".manga-studio/canon/versions/chapter-001-canon-v001.json",
    ".manga-studio/decisions/chapter-001-canon-proposal-v001.json",
    ".manga-studio/maintenance/canon-proposal-v001/finalize.py",
    ".manga-studio/maintenance/canon-proposal-v001/relocations.json",
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
            "canon_version": authority["proposed_canon_version"],
            "canon_status": canon["status"],
            "canon_adopted": False,
            "locks_changed": False,
        },
        indent=2,
    )
)
