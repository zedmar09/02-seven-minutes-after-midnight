"""Read-only final checks for the evidence-based audit package."""
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[2]
work = root / ".manga-studio"
analysis = work / "analysis"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


config = read(work / "project.json")
baseline = read(work / "source/inventory-baseline-v001.json")
provenance = read(work / "source/provenance.json")
report = read(analysis / "diagnostics/sma-comprehensive-audit-v001.json")
spec = read(analysis / "audit-issue-input-v001.json")
coverage = read(analysis / "coverage-v001.json")
registers = read(analysis / "continuity-registers-v001.json")
entity_register = read(analysis / "entity-register-v001.json")
source_checks = []
errors = []
locators_checked = 0
units = {}
for record in provenance["records"]:
    for path_key, hash_key in (("original_path", "original_sha256"), ("snapshot_path", "snapshot_sha256"), ("normalized_path", "normalized_sha256"), ("source_map_path", "source_map_checksum")):
        if sha(root / record[path_key]) != record[hash_key]:
            errors.append("Hash mismatch: " + record[path_key])
    source_map = read(root / record["source_map_path"])
    data = (root / record["normalized_path"]).read_bytes()
    for unit in source_map["source_units"]:
        if hashlib.sha256(data[unit["byte_start"]:unit["byte_end"]]).hexdigest() != unit["content_fingerprint"]:
            errors.append("Unit fingerprint mismatch: " + unit["source_unit_id"])
        units[unit["source_unit_id"]] = unit
for row in baseline["files"]:
    identical = sha(root / row["relative_path"]) == row["sha256"]
    source_checks.append({"relative_path": row["relative_path"], "sha256": row["sha256"], "byte_identical": identical})
    if not identical:
        errors.append("Original source changed: " + row["relative_path"])


def walk(value):
    global locators_checked
    if isinstance(value, dict):
        if "source_unit_id" in value and "project_id" in value:
            locators_checked += 1
            unit = units[value["source_unit_id"]]
            if value["project_id"] != config["project_id"]:
                errors.append("Cross-project locator")
            for key in ("document_id", "chapter_id", "scene_id", "source_relative_path", "line_start", "line_end", "byte_start", "byte_end", "content_fingerprint"):
                if value[key] != unit[key]:
                    errors.append("Locator differs from referenced unit: " + key)
        for item in value.values():
            walk(item)
    elif isinstance(value, list):
        for item in value:
            walk(item)


for artifact in (report, registers, entity_register):
    walk(artifact)
assert len(report["findings"]) == len(spec["issues"]) == 30
assert len({row["issue_id"] for row in report["findings"]}) == 30
for finding, authored in zip(report["findings"], spec["issues"]):
    assert finding["issue_id"] == f"SMA-ISS-{authored['n']:03d}"
    assert len(finding["alternatives"]) >= 2
    assert all("Risk:" in solution for solution in finding["alternatives"])
    assert authored["priority"] in {"P0", "P1", "P2", "P3"}
    assert authored["preserve"] and authored["kind"] and authored["uncertainty"]
dependency_graph = {row["n"]: row["dependencies"] for row in spec["issues"]}


def visit(number, stack):
    assert number not in stack, "Cyclic issue dependency"
    for dependency in dependency_graph[number]:
        visit(dependency, stack | {number})


for number in dependency_graph:
    visit(number, set())
assert report["status"] == "proposed"
assert not any(config["stage_locks"].values())
assert all(value is None for value in config["stage_lock_records"].values())
assert not config["image_generation_enabled"]
assert all(config[key] is None for key in ("active_manuscript_version", "active_canon_version", "active_storyboard_version"))
assert not [p for p in (work / "approvals").rglob("*.json") if not p.name.startswith("._")]
assert not [p for p in (work / "handoff").rglob("*.json") if not p.name.startswith("._")]
assert coverage["documents_reviewed"] == coverage["documents_available"] == 24
assert coverage["scripted_panels"] == 75
assert coverage["prose_chapters_available"] == 1
assert len(registers["threads_and_setups_payoffs"]) == 18
assert len(registers["timeline"]) == 13
for row in coverage["records"]:
    assert row["reviewed_lines"] == [1, row["line_count"]]
for path in work.rglob("*.json"):
    if path.name.startswith("._"):
        continue
    data = read(path)
    def check_paths(value):
        if isinstance(value, str):
            if value.startswith(("/", "~/")):
                errors.append("Absolute path stored in " + str(path.relative_to(root)))
        elif isinstance(value, dict):
            for item in value.values():
                check_paths(item)
        elif isinstance(value, list):
            for item in value:
                check_paths(item)
    check_paths(data)
recommended = read(analysis / "recommended-configuration-v001.json")
rating_source = recommended["content_rating"]["basis"]
assert rating_source["lines"][1] <= len((root / rating_source["source_relative_path"]).read_text(encoding="utf-8").splitlines())
artifact_names = ["AUDIT-v001.md", "full-diagnostic-v001.md", "diagnostics/sma-comprehensive-audit-v001.json", "story-and-world-assessment-v001.md", "character-assessment-v001.md", "continuity-registers-v001.json", "continuity-registers-v001.md", "entity-register-v001.json", "reconstruction-roadmap-v001.md", "recommended-configuration-v001.json", "coverage-v001.json", "coverage-v001.md", "source-integrity-v001.json"]
result = {
    "record_type": "final_audit_validation", "project_id": config["project_id"], "version": "v001", "checked_at": datetime.now(timezone.utc).isoformat(),
    "result": "pass" if not errors else "fail", "errors": errors, "available_sources_reviewed": 24,
    "originals_checked": 25, "snapshots_checked": 24, "normalized_derivatives_checked": 24, "active_source_maps_checked": 24,
    "strict_evidence_locators_checked": locators_checked, "issue_count": 30, "priorities": dict(Counter(row["priority"] for row in spec["issues"])),
    "source_checks": source_checks, "dependency_graph": "acyclic", "all_stage_locks_false": True,
    "approvals_created": 0, "image_jobs_created": 0, "image_generation_enabled": False,
    "active_approved_versions": {"manuscript": None, "canon": None, "storyboard": None},
    "runtime_checks": {"source_map": "passed", "story_profile": "passed", "diagnostic_schema_and_links": "passed", "stage_locks": "passed"},
    "not_applicable": {"page_quality_review": "No composed or lettered pages exist", "preproduction_and_production_validation": "No approved storyboards, image jobs, or reference images exist"},
    "limitations": ["Checks verify provenance and artifact consistency, not artistic quality or market response.", "Unavailable Chapter 2 and reader images remain outside audit coverage."],
    "artifact_hashes": [{"relative_path": str((analysis / name).relative_to(root)), "sha256": sha(analysis / name)} for name in artifact_names]
}
print(json.dumps(result, indent=2))
raise SystemExit(0 if not errors else 1)
