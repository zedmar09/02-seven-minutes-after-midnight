"""Read-only draft/layout verification; --record writes one new validation artifact."""
import argparse
import difflib
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REPORT = ".manga-studio/analysis/workspace-refactor-v001-validation.json"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--record", action="store_true")
args = parser.parse_args()
runtime = Path.home() / ".agents/skills/.manga-studio-runtime"
installed = runtime / read(runtime / "current.json")["version_path"]
sys.path.insert(0, str(installed / "scripts/lib"))
from manga_studio.approvals import validate_approval, validate_locks
from manga_studio.json_schema import validate_json_file
from manga_studio.profiles import validate_profile
from manga_studio.project import WORKSPACE_DIRECTORIES, _is_excluded, _matches_any, discover_project, provenance_errors
from manga_studio.structure import validate_source_maps

context = discover_project(ROOT)
config = context.config
assert context.project_root == ROOT
assert config["project_id"] == "ms-70391ae1065048cf8bdd564959abd6c3"
assert config["source_roots"] == ["."]
assert config["revision_mode"] == "approved_versions_only"
assert config["existing_structure_preservation"] == {"preserve_original_paths": True, "preserve_chapter_order": True, "preserve_titles": True, "never_rewrite_originals": True}
errors = provenance_errors(context) + validate_source_maps(context) + validate_locks(context) + validate_profile(context, "story")
baseline = read(WORK / "source/inventory-baseline-v001.json")
for row in baseline["files"]:
    assert sha(ROOT / row["relative_path"]) == row["sha256"], row["relative_path"]
historical_counts = {}
for relative, key in [
    (".manga-studio/analysis/validation-v001.json", "artifact_hashes"),
    (".manga-studio/revisions/phase-3-v001/package-manifest-v001.json", "artifacts"),
    (".manga-studio/revisions/phase-4-proposal-v001/package-manifest-v001.json", "artifacts"),
]:
    rows = read(ROOT / relative)[key]
    for row in rows:
        assert sha(ROOT / row["relative_path"]) == row["sha256"], row["relative_path"]
    historical_counts[relative] = len(rows)
assert sha(WORK / "revisions/phase-4-proposal-v001/package-manifest-v001.json") == "7dd762c042129d11b9e4cd09815912122051c6057eee03bb26733c7a2295bd50"
assert sha(WORK / "revisions/phase-3-v001/package-manifest-v001.json") == "39a56110a135bccb13cb9ccbf0b0d03600ef4e621a6992d7b08362ee54dd976a"

# Use the runtime's own matching rules without rewriting its historical inventory.
candidates = set()
for source_root in context.source_roots:
    for path in source_root.rglob("*"):
        if path.is_file():
            rel = path.relative_to(ROOT).as_posix()
            if not _is_excluded(rel, config["source_exclusion_patterns"]) and _matches_any(rel, config["source_inclusion_patterns"]):
                candidates.add(rel)
assert candidates == {r["relative_path"] for r in baseline["files"]}
for rel in ("manga/03-story/arc-01/chapter-001/chapter-001-v001.md", "MANGA-STUDIO.md"):
    assert _is_excluded(rel, config["source_exclusion_patterns"])
approvals = [p for p in (WORK / "approvals").glob("*.json") if not p.name.startswith("._")]
assert len(approvals) == 4
assert {read(p)["artifact_type"] for p in approvals} == {"diagnostic_report", "revision_plan", "revision_policy", "change_set"}
for path in approvals:
    errors += validate_approval(context, path)
    assert read(path)["status"] == "approved" and read(path)["actor"] == "user"

draft = WORK / "manuscript/versions/chapter-001-v001.md"
meta = read(WORK / "manuscript/versions/chapter-001-v001.metadata.json")
copy_map = read(ROOT / "manga/03-story/arc-01/chapter-001/reading-copy-v001.json")
change = read(WORK / "revisions/change-sets/sma-ch01-balanced-v001.json")
preview = ROOT / meta["reviewed_preview"]["relative_path"]
copy = ROOT / copy_map["reading_copy_relative_path"]
expected = "f195b7e0afc7f875731ade728a1bbf7a28d7becf3f38fa2d920498231f65d500"
assert draft.read_bytes() == copy.read_bytes() == preview.read_bytes() == change["operation"]["after"].encode()
assert sha(draft) == sha(copy) == meta["sha256"] == copy_map["reading_copy_sha256"] == copy_map["canonical_sha256"] == expected
assert copy_map["canonical_relative_path"] == draft.relative_to(ROOT).as_posix()
assert meta["status"] == copy_map["status"] == "draft_inactive"
assert meta["active"] is False and meta["adoption_approval"] is None
assert meta["chapter_id"] == "chapter-fb585a7fd3e7450e936edbcfce992566"
assert meta["approved_change_set"]["sha256"] == sha(WORK / "revisions/change-sets/sma-ch01-balanced-v001.json")
assert sha(ROOT / meta["source"]["relative_path"]) == meta["source"]["sha256"]
register = read(WORK / "revisions/phase-4-proposal-v001/exact-edit-register-v001.json")
original = (ROOT / meta["source"]["relative_path"]).read_text()
text = draft.read_text()
parts = []
cursor = 0
for edit in register["edits"]:
    a,b = edit["source_lines"]
    c,d = edit["preview_lines"]
    assert "".join(original.splitlines(keepends=True)[a-1:b]) == edit["before"]
    assert "".join(text.splitlines(keepends=True)[c-1:d]) == edit["after"]
    parts += ["".join(original.splitlines(keepends=True)[cursor:a-1]), edit["after"]]
    cursor = b
parts.append("".join(original.splitlines(keepends=True)[cursor:]))
assert "".join(parts) == text
expected_diff = "".join(difflib.unified_diff(original.splitlines(keepends=True), text.splitlines(keepends=True), fromfile=meta["source"]["relative_path"], tofile=meta["relative_path"]))
assert (ROOT / meta["diff_relative_path"]).read_text() == expected_diff
assert re.findall(r"^12:0[0-7]\.$", text, re.M) == [f"12:0{i}." for i in range(8)]
assert len(text.split("## Story Draft\n", 1)[1].split()) == 2896
for path in [WORK / "decisions/apply-chapter-001-v001.json", WORK / "decisions/workspace-structure-v001.json"]:
    errors += validate_json_file(path, installed / "schemas/decision-log.schema.json")

review_path = ROOT / meta["consistency_review_relative_path"]
review = read(review_path)
assert review["target"]["relative_path"] == meta["relative_path"] and review["target"]["sha256"] == expected
assert review["approval_granted"] is False and not review["errors"]
assert len(review["checks"]) == 8 and len(review["warnings"]) == 7
assert {r["issue_id"] for r in review["issue_dispositions"]} == {f"SMA-ISS-{i:03}" for i in range(1,31)}
assert sha(ROOT / review["review_basis"]["relative_path"]) == review["review_basis"]["sha256"]
for row in review["checks"]:
    for span in row["manuscript_spans"]:
        assert span["relative_path"] == meta["relative_path"] and 1 <= span["line_start"] <= span["line_end"] <= len(text.splitlines())
units = {}
for row in read(WORK / "source/provenance.json")["records"]:
    units.update({u["source_unit_id"]: u for u in read(ROOT / row["source_map_path"])["source_units"]})
locator_count = 0


def check_json(value):
    global locator_count
    if isinstance(value, dict):
        if "source_unit_id" in value and "project_id" in value:
            locator_count += 1
            unit = units[value["source_unit_id"]]
            assert value["project_id"] == config["project_id"]
            for key in ("document_id", "chapter_id", "scene_id", "source_relative_path", "line_start", "line_end", "byte_start", "byte_end", "content_fingerprint"):
                assert value[key] == unit[key]
        if "project_id" in value:
            assert value["project_id"] == config["project_id"]
        if "relative_path" in value and "sha256" in value:
            assert sha(ROOT / value["relative_path"]) == value["sha256"]
        for key, item in value.items():
            if key.endswith("relative_path") and isinstance(item, str):
                assert not Path(item).is_absolute() and ".." not in Path(item).parts
                assert (ROOT / item).exists(), item
            check_json(item)
    elif isinstance(value, list):
        for item in value:
            check_json(item)
    elif isinstance(value, str):
        assert not value.startswith(("/", "~/")), "Non-relative stored value"


layout = read(WORK / "workspace-layout-v001.json")
assert layout["project_root"] == "." and layout["managed_root"] == ".manga-studio" and layout["visible_root"] == "manga"
assert layout["originals_moved"] is False and layout["comparison"]["content_imported"] is False
assert set(layout["required_runtime_directories"]) == {".manga-studio/" + p for p in WORKSPACE_DIRECTORIES}
for directory in layout["required_runtime_directories"] + layout["additional_directories"]:
    assert (ROOT / directory).is_dir(), directory
for directory in layout["managed_ownership"].values():
    assert (ROOT / directory).is_dir()
assert len(layout["visible_sections"]) == 5
for section in layout["visible_sections"]:
    assert (ROOT / section["relative_path"] / "README.md").is_file()
policy = read(ROOT / "manga/01-style/production-policy-v001.json")
references = read(ROOT / "manga/02-references/reference-register-v001.json")
readiness = read(ROOT / "manga/04-production/arc-01/chapter-001/readiness-v001.json")
assert policy["quality_profile_tier"] == policy["detail_budget"] == readiness["required_quality_profile"] == "high"
assert not policy["image_generation_enabled"] and not policy["release_readiness"]
assert not references["assets"] and not references["reference_image_paths"] and not readiness["image_jobs"] and not readiness["approved_assets"]
new_json_paths = [WORK / "workspace-layout-v001.json", WORK / "manuscript/versions/chapter-001-v001.metadata.json", review_path, WORK / "decisions/apply-chapter-001-v001.json", WORK / "decisions/workspace-structure-v001.json"]
new_json_paths += [p for p in (ROOT / "manga").rglob("*.json") if not p.name.startswith("._")]
for path in new_json_paths:
    check_json(read(path))
links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", (ROOT / "MANGA-STUDIO.md").read_text())
for href in links:
    href = unquote(href)
    assert not Path(href).is_absolute() and ".." not in Path(href).parts and "://" not in href
    if href == REPORT and args.record and not (ROOT / href).exists():
        continue
    assert (ROOT / href).is_file(), href
assert all(v is False for v in config["stage_locks"].values())
assert all(v is None for v in config["stage_lock_records"].values())
assert all(config[k] is None for k in ("active_canon_version", "active_manuscript_version", "active_storyboard_version"))
assert not config["image_generation_enabled"]
assert not [p for p in (WORK / "handoff").rglob("*.json") if not p.name.startswith("._")]
assert not errors, errors

tracked_outputs = [ROOT / "MANGA-STUDIO.md", ROOT / "AGENTS.md", WORK / "workspace-layout-v001.json", draft, ROOT / "manga/03-story/arc-01/chapter-001/reading-copy-v001.json", ROOT / meta["diff_relative_path"], review_path, review_path.with_suffix(".md"), WORK / "decisions/workspace-structure-v001.md"]
tracked_outputs += [p for p in (ROOT / "manga").rglob("*") if p.is_file() and not p.name.startswith("._")]
tracked_outputs += new_json_paths
tracked_outputs += [p for p in Path(__file__).resolve().parent.glob("*.py") if not p.name.startswith("._")]
tracked_outputs = sorted(set(tracked_outputs))
result = {"record_type": "workspace_refactor_and_manuscript_validation", "project_id": config["project_id"], "version": "v001", "checked_at": datetime.now(timezone.utc).isoformat(), "status": "pass", "errors": [], "runtime_story_profile": "pass", "original_candidate_hashes_unchanged": len(baseline["files"]), "original_story_sources_unchanged": 24, "source_inventory_candidates_after_exclusions": len(candidates), "historical_package_hash_checks": historical_counts, "source_provenance_and_maps": "pass", "separate_user_approvals_valid": len(approvals), "new_managed_manuscripts": 1, "new_reading_copies": 1, "draft_and_copy_sha256": expected, "approved_edits_applied": len(register["edits"]), "additional_prose_edits": 0, "deterministic_diff": "pass", "clock_markers_checked": 8, "editorial_checks_carried_forward": len(review["checks"]), "editorial_warnings_preserved": len(review["warnings"]), "audit_issue_dispositions": len(review["issue_dispositions"]), "strict_source_locators_checked": locator_count, "runtime_directories_verified": len(WORKSPACE_DIRECTORIES), "visible_sections_verified": 5, "entry_point_links_checked": len(links), "new_json_paths_and_hash_bindings_checked": len(new_json_paths), "other_project_content_imported": False, "active_versions": {"canon": None, "manuscript": None, "storyboard": None}, "stage_locks": config["stage_locks"], "image_generation_enabled": False, "production_ready": False, "source_files_moved_or_renamed": 0, "scope_note": "Additive working-layout refactor preserves the original Comics tree and all hash-bound history. The comparison project informed directory conventions only. Draft approval, authority adoption and production gates remain distinct.", "artifact_hashes": [{"relative_path": p.relative_to(ROOT).as_posix(), "sha256": sha(p)} for p in tracked_outputs]}
if args.record:
    path = ROOT / REPORT
    assert not path.exists(), "Refusing to overwrite historical validation"
    with path.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
else:
    recorded = read(ROOT / REPORT)
    for row in recorded["artifact_hashes"]:
        assert sha(ROOT / row["relative_path"]) == row["sha256"], row["relative_path"]
print(json.dumps({k: v for k, v in result.items() if k != "artifact_hashes"}, indent=2))
