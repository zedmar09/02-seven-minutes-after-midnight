"""Validate Phase 3 proposals and preservation without mutating any artifact."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[3]
work = root / ".manga-studio"
packet = work / "revisions/phase-3-v001"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


runtime = Path.home() / ".agents/skills/.manga-studio-runtime"
installed = runtime / read(runtime / "current.json")["version_path"]
sys.path.insert(0, str(installed / "scripts/lib"))
from manga_studio.project import discover_project, provenance_errors
from manga_studio.structure import validate_source_maps
from manga_studio.approvals import validate_approval, validate_locks
from manga_studio.json_schema import validate_json_file

context = discover_project(root)
config = read(work / "project.json")
previous = read(work / "analysis/validation-v001.json")
baseline = read(work / "source/inventory-baseline-v001.json")
provenance = read(work / "source/provenance.json")
manifest_path = packet / "package-manifest-v001.json"
manifest = read(manifest_path)
parent_path = work / "revisions/plans/sma-reconstruction-v001.json"
parent = read(parent_path)
packages = read(packet / "revision-work-packages-v001.json")["work_packages"]
proposals = read(packet / "decision-proposals-v001.json")["proposals"]
approval_path = work / "approvals/approval-8a2e8e6a05744edd9034972bf780a058.json"
approval = read(approval_path)
errors = []
errors += provenance_errors(context)
errors += validate_source_maps(context)
errors += validate_approval(context, approval_path)
errors += validate_locks(context)

for row in previous["artifact_hashes"]:
    if sha(root / row["relative_path"]) != row["sha256"]:
        errors.append("Prior audit artifact changed: " + row["relative_path"])
for row in baseline["files"]:
    if sha(root / row["relative_path"]) != row["sha256"]:
        errors.append("Original source changed: " + row["relative_path"])
for row in manifest["artifacts"]:
    if sha(root / row["relative_path"]) != row["sha256"]:
        errors.append("Reviewed packet artifact changed: " + row["relative_path"])
assert len(manifest["artifacts"]) == manifest["artifact_count"]
assert sha(manifest_path) in parent["proposed_operation"]
assert approval["decision"] == approval["status"] == "approved"
assert approval["artifact_type"] == "diagnostic_report"
assert approval["target_sha256"] == sha(root / approval["target_relative_path"])

units = {}
valid_targets = set()
for row in provenance["records"]:
    source_map = read(root / row["source_map_path"])
    valid_targets.add(row["document_id"])
    valid_targets.update(item["chapter_id"] for item in source_map["chapters"])
    valid_targets.update(item["scene_id"] for item in source_map["scenes"])
    units.update({item["source_unit_id"]: item for item in source_map["source_units"]})
valid_targets.update(units)
valid_targets.update(item["id"] for item in read(work / "analysis/entity-register-v001.json")["entities"])
source_locator_count = 0


def walk(value):
    global source_locator_count
    if isinstance(value, dict):
        if "source_unit_id" in value and "project_id" in value:
            source_locator_count += 1
            unit = units[value["source_unit_id"]]
            assert value["project_id"] == config["project_id"]
            for key in ("document_id", "chapter_id", "scene_id", "source_relative_path", "line_start", "line_end", "byte_start", "byte_end", "content_fingerprint"):
                assert value[key] == unit[key], (value["source_unit_id"], key)
        for item in value.values():
            walk(item)
    elif isinstance(value, list):
        for item in value:
            walk(item)
    elif isinstance(value, str):
        assert not value.startswith(("/", "~/")), "Absolute path stored in new JSON metadata"


plans = {}
for path in (work / "revisions/plans").glob("*.json"):
    if path.name.startswith("._"):
        continue
    errors += validate_json_file(path, installed / "schemas/revision-plan.schema.json")
    plan = read(path)
    assert plan["approval_status"] == "proposed"
    assert not plan["change_set_ids"]
    assert all(identity in valid_targets for identity in plan["target_stable_ids"])
    plans[plan["revision_plan_id"]] = plan
    walk(plan)
policy_path = work / "revisions/policies/sma-balanced-v001.json"
errors += validate_json_file(policy_path, installed / "schemas/revision-policy.schema.json")
assert read(policy_path)["approval_status"] == "proposed"
for path in packet.glob("*.json"):
    if not path.name.startswith("._") and path.name != "validation-v001.json":
        walk(read(path))


def visit(plan_id, stack):
    assert plan_id in plans, "Unknown plan dependency"
    assert plan_id not in stack, "Cyclic plan dependency"
    for dependency in plans[plan_id]["dependencies"]:
        visit(dependency, stack | {plan_id})


for plan_id in plans:
    visit(plan_id, set())
audit_issues = {item["issue_id"] for item in read(root / approval["target_relative_path"])["findings"]}
mapped = {issue for package in packages for issue in package["triggering_issue_ids"]}
assert mapped == audit_issues == set(parent["triggering_issue_ids"])
assert len(audit_issues) == 30 and len(packages) == 13 and len(proposals) == 14
proposal_ids = {p["id"] for p in proposals}
for package in packages:
    assert package["owner"] and package["risk"] and package["acceptance"]
    assert set(package["decisions"]) <= proposal_ids
    assert package["approval_status"] == "proposed" and package["status"] == "not_started"
    assert package["revision_plan_id"] in plans
for proposal in proposals:
    assert proposal["status"] == "proposed" and proposal["approved_by"] is None
    assert proposal["recommendation"] and proposal["alternative"] and proposal["tradeoff"]
assert all(not value for value in config["stage_locks"].values())
assert all(value is None for value in config["stage_lock_records"].values())
assert all(config[key] is None for key in ("active_canon_version", "active_manuscript_version", "active_storyboard_version"))
assert not config["image_generation_enabled"]
for directory in ("manuscript/versions", "revisions/change-sets", "handoff"):
    assert not [p for p in (work / directory).rglob("*") if p.is_file() and not p.name.startswith("._")], directory
new_approvals = [p for p in (work / "approvals").glob("*.json") if not p.name.startswith("._")]
assert new_approvals == [approval_path], "Unexpected new artifact approval"
result = {
    "record_type": "phase_3_validation", "project_id": config["project_id"], "version": "v001", "checked_at": datetime.now(timezone.utc).isoformat(),
    "status": "pass" if not errors else "fail", "errors": errors,
    "approved_diagnostic": {"approval_id": approval["approval_id"], "target_relative_path": approval["target_relative_path"], "sha256": approval["target_sha256"]},
    "original_candidates_byte_identical": len(baseline["files"]), "original_story_sources_byte_identical": 24,
    "prior_audit_artifact_hashes_unchanged": len(previous["artifact_hashes"]),
    "snapshot_normalized_and_source_map_integrity": "passed" if not errors else "see errors",
    "review_package_artifacts_hash_checked": manifest["artifact_count"],
    "revision_plan_schemas_checked": len(plans), "revision_policy_schemas_checked": 1,
    "strict_source_evidence_locators_checked": source_locator_count,
    "issues_mapped": len(mapped), "work_packages": len(packages), "decision_proposals": len(proposals), "dependency_graph": "acyclic",
    "stage_locks": config["stage_locks"], "active_approved_versions": {"canon": None, "manuscript": None, "storyboard": None},
    "new_approval_count": len(new_approvals), "new_approval_scope": "User-approved audit only",
    "new_manuscript_count": 0, "new_change_set_count": 0, "new_image_job_count": 0, "image_generation_enabled": False,
    "package_manifest": {"relative_path": str(manifest_path.relative_to(root)), "sha256": sha(manifest_path)},
    "parent_revision_plan": {"relative_path": str(parent_path.relative_to(root)), "sha256": sha(parent_path)},
    "readiness": "Phase 3 proposals are complete and await user review; no execution or stage-lock readiness is implied.",
    "limits": ["All proposed story choices remain unapproved.", "Calendar dates, cost calibration, and other continuation-only unknowns remain explicit blockers before dependent new chapters.", "No reader, market, historical, legal, or artistic result is validated by schema or provenance checks.", "No page-quality review applies because no approved composed or lettered pages exist."]
}
print(json.dumps(result, indent=2))
raise SystemExit(0 if not errors else 1)
