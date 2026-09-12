"""Verify the review packet; --finalize creates new reports once, without activation."""
import argparse
import difflib
import hashlib
import json
import re
import runpy
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).resolve().parent
REL = PACKET.relative_to(ROOT).as_posix()
WORK = ROOT / ".manga-studio"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encode(value):
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode()


parser = argparse.ArgumentParser()
parser.add_argument("--finalize", action="store_true")
args = parser.parse_args()
runtime = Path.home() / ".agents/skills/.manga-studio-runtime"
installed = runtime / read(runtime / "current.json")["version_path"]
sys.path.insert(0, str(installed / "scripts/lib"))
from manga_studio.approvals import validate_approval, validate_locks
from manga_studio.json_schema import validate_instance, validate_json_file
from manga_studio.project import discover_project, provenance_errors
from manga_studio.structure import validate_source_maps

context = discover_project(ROOT)
config = read(WORK / "project.json")
errors = provenance_errors(context) + validate_source_maps(context) + validate_locks(context)
for path, schema in [
    (WORK / "project.json", "project.schema.json"),
    (WORK / "source/id-map.json", "stable-id-map.schema.json"),
    (WORK / "revisions/change-sets/sma-ch01-balanced-v001.json", "change-set.schema.json"),
    (WORK / "decisions/editorial-option-b-approval-v001.json", "decision-log.schema.json"),
]:
    errors += validate_json_file(path, installed / "schemas" / schema)

baseline = read(WORK / "source/inventory-baseline-v001.json")
old_audit = read(WORK / "analysis/validation-v001.json")
old_manifest = read(WORK / "revisions/phase-3-v001/package-manifest-v001.json")
for row in baseline["files"] + old_audit["artifact_hashes"] + old_manifest["artifacts"]:
    assert sha(ROOT / row["relative_path"]) == row["sha256"], row["relative_path"]
assert sha(WORK / "revisions/phase-3-v001/package-manifest-v001.json") == "39a56110a135bccb13cb9ccbf0b0d03600ef4e621a6992d7b08362ee54dd976a"
assert sha(WORK / "revisions/plans/sma-reconstruction-v001.json") == "426e11d146f23f61b98e34f30f7918df51caebc4b3dbe9bf188ac170196dec60"
approvals = [p for p in (WORK / "approvals").glob("*.json") if not p.name.startswith("._")]
assert len(approvals) == 3
assert {read(p)["artifact_type"] for p in approvals} == {"diagnostic_report", "revision_plan", "revision_policy"}
for path in approvals:
    errors += validate_approval(context, path)
    assert read(path)["actor"] == "user" and read(path)["status"] == "approved"

builder = runpy.run_path(str(PACKET / "build-review-v001.py"))
reassembled, metrics = builder["assemble"]()
for relative, contents in reassembled.items():
    assert (ROOT / relative).read_bytes() == contents, "Non-deterministic or edited output: " + relative
register = read(PACKET / "exact-edit-register-v001.json")
change_path = WORK / "revisions/change-sets/sma-ch01-balanced-v001.json"
change = read(change_path)
assert change["approval_status"] == "proposed"
original = change["operation"]["before"]
preview = change["operation"]["after"]
assert sha(ROOT / change["operation"]["target_relative_path"]) == change["operation"]["target_sha256"]
assert sha(ROOT / register["preview_relative_path"]) == register["preview_sha256"]
assert preview == (ROOT / register["preview_relative_path"]).read_text(encoding="utf-8")
assert metrics["preview_story_words"] == 2896 and metrics["original_story_words"] == 2655
for edit in register["edits"]:
    a,b = edit["source_lines"]
    c,d = edit["preview_lines"]
    assert "".join(original.splitlines(keepends=True)[a-1:b]) == edit["before"]
    assert "".join(preview.splitlines(keepends=True)[c-1:d]) == edit["after"]
    assert original.count(edit["before"]) == 1
assert original != preview
ndiff = list(difflib.ndiff(original.splitlines(keepends=True), preview.splitlines(keepends=True)))
assert "".join(difflib.restore(ndiff, 1)) == original
assert "".join(difflib.restore(ndiff, 2)) == preview
assert re.findall(r"^12:0[0-7]\.$", preview, re.M) == [f"12:0{i}." for i in range(8)]
assert preview.index("Tomas let go. It yellowed") < preview.index("\n12:07.\n") < preview.index("Then the pale corner came free") < preview.index("I will bring better bread.") < preview.index("The sound broke in the middle.") < preview.index("FIRE STARTS IN THE SERVICE CORRIDOR.")

units = {}
provenance = read(WORK / "source/provenance.json")
for row in provenance["records"]:
    units.update({u["source_unit_id"]: u for u in read(ROOT / row["source_map_path"])["source_units"]})
locator_count = 0


def walk(value):
    global locator_count
    if isinstance(value, dict):
        if "source_unit_id" in value and "project_id" in value:
            locator_count += 1
            actual = units[value["source_unit_id"]]
            assert value["project_id"] == config["project_id"]
            for key in ("document_id", "chapter_id", "scene_id", "source_relative_path", "line_start", "line_end", "byte_start", "byte_end", "content_fingerprint"):
                assert value[key] == actual[key], (value["source_unit_id"], key)
        for item in value.values():
            walk(item)
    elif isinstance(value, list):
        for item in value:
            walk(item)
    elif isinstance(value, str):
        assert not value.startswith(("/", "~/")), "Absolute path in new stored JSON"


walk(change)
walk(register)
assessment = read(PACKET / "consistency-input-v001.json")
assert len(assessment["checks"]) == 8 and len(assessment["warnings"]) == 7
assert {d["issue"] for d in assessment["issue_dispositions"]} == set(range(1,31))
assert len(assessment["issue_dispositions"]) == 30
diagnostic = read(WORK / "analysis/diagnostics/sma-comprehensive-audit-v001.json")
findings = {f["issue_id"]: f for f in diagnostic["findings"]}
edits_by_id = {e["edit_id"]: e for e in register["edits"]}
checks = []
for row in assessment["checks"]:
    assert set(row["edit_ids"]) <= edits_by_id.keys()
    checks.append({**row, "preview_spans": [{"relative_path": register["preview_relative_path"], "line_start": edits_by_id[i]["preview_lines"][0], "line_end": edits_by_id[i]["preview_lines"][1]} for i in row["edit_ids"]]})
dispositions = []
for row in assessment["issue_dispositions"]:
    issue = f"SMA-ISS-{row['issue']:03}"
    fact = findings[issue]
    dispositions.append({"issue_id": issue, "status": row["status"], "reason": row["reason"], "diagnostic_description": fact["description"], "source_evidence": fact["evidence"], "candidate_edit_ids": [e["edit_id"] for e in register["edits"] if issue in e["triggering_issue_ids"]]})
report = {
    "record_type": "story_consistency_review", "project_id": config["project_id"], "version": "v001",
    "status": "review_ready_with_warnings", "reviewer": "manga-consistency-manager", "approval_granted": False,
    "scope": "Entire supplied Chapter 1 reading preview compared with immutable source and accepted Option B directions; all thirty audit dispositions. No Chapter 2, rendered artwork or unapproved production asset reviewed.",
    "target": {"relative_path": register["preview_relative_path"], "sha256": register["preview_sha256"], "chapter_id": builder["CHAPTER"], "scene_ids": ["scene-2f59e856c58d4d6db58d635cbc64e0bb", builder["SCENE"]]},
    "change_set": {"relative_path": str(change_path.relative_to(ROOT)), "sha256": sha(change_path)},
    "assessment": assessment["assessment"], "errors": [], "checks": checks, "warnings": assessment["warnings"],
    "intentional_changes": [{"edit_id": e["edit_id"], "accepted_proposal_ids": e["accepted_proposal_ids"], "description": e["purpose"], "risk": e["risk"]} for e in register["edits"]],
    "issue_dispositions": dispositions, "metrics": metrics,
    "schema_note": "Installed review.schema.json enumerates production review types only; continuity-state.schema.json requires a page. This textual pre-manuscript report uses a project-local structured record with explicit field, locator, issue-ID and target-hash checks, not a falsely labeled page/image review. Runtime schemas validate project, IDs, change set, decision and approvals separately.",
}
walk(report)
assert all(not v for v in config["stage_locks"].values())
assert all(v is None for v in config["stage_lock_records"].values())
assert all(config[k] is None for k in ("active_manuscript_version", "active_canon_version", "active_storyboard_version"))
assert not config["image_generation_enabled"]
for directory in ("manuscript/versions", "handoff"):
    assert not [p for p in (WORK / directory).rglob("*") if p.is_file() and not p.name.startswith("._")]
assert len([p for p in (WORK / "revisions/change-sets").glob("*.json") if not p.name.startswith("._")]) == 1
assert not errors, errors

review_rel = ".manga-studio/analysis/consistency/chapter-01-proposal-review-v001"
md = ["# Chapter 1 Proposal Consistency Review v001", "", report["assessment"], "", "Status: review ready with warnings; no approval granted. Entire Chapter 1 preview reviewed, all 30 diagnostic issues dispositioned. No artwork review is applicable.", "", "Target: `" + register["preview_relative_path"] + "`", "", "## Checks", ""]
for c in checks:
    md += ["### " + c["id"] + ": " + c["topic"], "", "Result: " + c["result"] + ". " + c["assessment"], "", "Exact changes: " + (", ".join(c["edit_ids"]) or "Approval and project records") + ".", ""]
md += ["## Warnings and Open Decisions", ""]
for w in assessment["warnings"]:
    md += ["- " + w["id"] + ": " + w["message"]]
md += ["", "## All Audit Dispositions", "", "Nothing marked repaired in proposal has yet been adopted as manuscript or applied to an original source.", "", "| Issue | Current status | Disposition |", "|---|---|---|"]
for d in dispositions:
    md.append("| " + d["issue_id"] + " | " + d["status"] + " | " + d["reason"] + " |")
md += ["", "## Evidence and Limits", "", "The JSON companion carries exact original source-unit evidence for each audit issue and computed preview lines for every changed check. The exact-edit register supplies every before/after span. Working-continuity-v001.md contains the private location, knowledge and prop ledgers.", "", report["schema_note"], "", "No external reader, timed performance, historical, legal or market validation was conducted. No active canon, manuscript or storyboard exists; all locks remain false. Approval must come from the user.", ""]
new_outputs = {review_rel + ".json": encode(report), review_rel + ".md": ("\n".join(md) + "\n").encode()}
if not args.finalize:
    for relative, contents in new_outputs.items():
        assert (ROOT / relative).read_bytes() == contents, "Review drift: " + relative

paths = set(reassembled) | set(new_outputs)
paths.update(p.relative_to(ROOT).as_posix() for p in PACKET.iterdir() if p.is_file() and not p.name.startswith("._") and p.name not in ("package-manifest-v001.json", "validation-v001.json"))
paths.update(p.relative_to(ROOT).as_posix() for p in approvals)
manifest = {"record_type": "exact_change_review_manifest", "project_id": config["project_id"], "version": "v001", "status": "proposed", "artifact_count": len(paths), "artifacts": [{"relative_path": p, "sha256": hashlib.sha256(new_outputs[p]).hexdigest() if p in new_outputs else sha(ROOT / p)} for p in sorted(paths)], "exclusions": ["This manifest excludes itself and the generated validation report to avoid circular checksums. Mutable project metadata is checked by state, not frozen here."]}
new_outputs[f"{REL}/package-manifest-v001.json"] = encode(manifest)
if not args.finalize:
    assert (PACKET / "package-manifest-v001.json").read_bytes() == encode(manifest)
result = {
    "record_type": "exact_change_review_validation", "project_id": config["project_id"], "version": "v001", "checked_at": datetime.now(timezone.utc).isoformat(), "status": "pass", "errors": [],
    "original_candidates_byte_identical": len(baseline["files"]), "imported_story_sources_byte_identical": len(provenance["records"]),
    "prior_audit_artifact_hashes_unchanged": len(old_audit["artifact_hashes"]), "approved_planning_artifact_hashes_unchanged": old_manifest["artifact_count"],
    "snapshot_normalization_and_source_maps": "pass", "current_user_approvals_valid": 3,
    "runtime_schema_checks": ["project", "stable-id-map", "change-set", "decision-log", "approval"],
    "textual_review_checks": "Project-local structure, known issue/edit IDs, strict evidence locators and exact target hashes; no production-review schema or page scores claimed.",
    "strict_source_locators_checked": locator_count, "deterministic_artifacts_reassembled": len(reassembled), "exact_edits_checked": len(register["edits"]), "clock_markers_checked": 8,
    "diff_roundtrip": "Both original and preview restored exactly", "diagnostic_dispositions": len(dispositions), "editorial_consistency_checks": len(checks), "editorial_warnings": len(assessment["warnings"]),
    "package_artifact_count": len(paths), "package_manifest_sha256": hashlib.sha256(encode(manifest)).hexdigest(),
    "change_set_sha256": sha(change_path), "preview_sha256": register["preview_sha256"], "metrics": metrics,
    "active_versions": {"canon": None, "manuscript": None, "storyboard": None}, "stage_locks": config["stage_locks"], "image_generation_enabled": False,
    "readiness": "Exact-change review ready. No exact-change approval, manuscript application, authority adoption, stage-lock activation or production readiness is implied."
}
if args.finalize:
    new_outputs[f"{REL}/validation-v001.json"] = encode(result)
    for relative in new_outputs:
        assert not (ROOT / relative).exists(), "Refusing to overwrite: " + relative
    for relative, contents in new_outputs.items():
        target = ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(contents)
print(json.dumps(result, indent=2))
