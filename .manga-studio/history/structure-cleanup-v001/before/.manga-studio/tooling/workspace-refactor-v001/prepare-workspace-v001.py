"""Materialize approved text and indexed folders without changing source or authority."""
import argparse
import difflib
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PID = "ms-70391ae1065048cf8bdd564959abd6c3"
APPROVAL = ".manga-studio/approvals/approval-3fbababa82a6464fb8ceb7c32fca4077.json"
CHANGE = ".manga-studio/revisions/change-sets/sma-ch01-balanced-v001.json"
PREVIEW = ".manga-studio/revisions/phase-4-proposal-v001/chapter-01-reading-preview-v001.md"
DRAFT = ".manga-studio/manuscript/versions/chapter-001-v001.md"
METADATA = ".manga-studio/manuscript/versions/chapter-001-v001.metadata.json"
COPY = "manga/03-story/arc-01/chapter-001/chapter-001-v001.md"
COPY_MAP = "manga/03-story/arc-01/chapter-001/reading-copy-v001.json"
DIFF = ".manga-studio/revisions/diffs/sma-ch01-balanced-manuscript-v001.diff"
DECISION = ".manga-studio/decisions/apply-chapter-001-v001.json"
REVIEW = ".manga-studio/analysis/consistency/chapter-001-manuscript-v001-review"
OLD_REVIEW = ".manga-studio/analysis/consistency/chapter-01-proposal-review-v001.json"


def read(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(data):
    return (json.dumps(data, indent=2, ensure_ascii=True) + "\n").encode()


def binding(relative, role):
    return {"relative_path": relative, "sha256": sha((ROOT / relative).read_bytes()), "role": role}


def assemble():
    runtime = Path.home() / ".agents/skills/.manga-studio-runtime"
    installed = runtime / json.loads((runtime / "current.json").read_text())["version_path"]
    sys.path.insert(0, str(installed / "scripts/lib"))
    from manga_studio.approvals import validate_approval
    from manga_studio.project import WORKSPACE_DIRECTORIES, discover_project

    context = discover_project(ROOT)
    assert context.config["project_id"] == PID
    assert not validate_approval(context, ROOT / APPROVAL)
    approval = read(APPROVAL)
    assert approval["artifact_type"] == "change_set" and approval["status"] == "approved" and approval["actor"] == "user"
    assert approval["target_relative_path"] == CHANGE
    assert approval["target_sha256"] == sha((ROOT / CHANGE).read_bytes()) == "e153b390bb498aac3b535ad3d93d87b2da8272a0b14681de54df28a61557c0bb"
    old_manifest = read(".manga-studio/revisions/phase-4-proposal-v001/package-manifest-v001.json")
    for row in old_manifest["artifacts"]:
        assert sha((ROOT / row["relative_path"]).read_bytes()) == row["sha256"], row["relative_path"]
    baseline = read(".manga-studio/source/inventory-baseline-v001.json")
    for row in baseline["files"]:
        assert sha((ROOT / row["relative_path"]).read_bytes()) == row["sha256"]
    change = read(CHANGE)
    preview = (ROOT / PREVIEW).read_bytes()
    assert sha(preview) == "f195b7e0afc7f875731ade728a1bbf7a28d7becf3f38fa2d920498231f65d500"
    assert preview == change["operation"]["after"].encode("utf-8")
    original = (ROOT / change["operation"]["target_relative_path"]).read_bytes()
    assert original == change["operation"]["before"].encode("utf-8")
    assert sha(original) == change["operation"]["target_sha256"]
    source = next(row for row in read(".manga-studio/source/provenance.json")["records"] if row["snapshot_path"] == change["operation"]["target_relative_path"])
    chapter_id = "chapter-fb585a7fd3e7450e936edbcfce992566"
    scenes = ["scene-2f59e856c58d4d6db58d635cbc64e0bb", "scene-3b27382ec9a049e2acde70d7cf88fc10"]
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    metadata = {
        "record_type": "versioned_manuscript_draft", "project_id": PID, "version": "v001", "chapter_id": chapter_id,
        "document_id": source["document_id"], "scene_ids": scenes, "display_title": "Chapter 01: The Cafe That Opened For Seven Minutes",
        "relative_path": DRAFT, "sha256": sha(preview), "created_at": timestamp, "created_by": "manga-chapter-writer",
        "status": "draft_inactive", "active": False, "adoption_approval": None, "source": {"relative_path": source["original_path"], "sha256": source["original_sha256"], "snapshot_relative_path": source["snapshot_path"]},
        "approved_change_set": binding(CHANGE, "Exact changes approved for new inactive draft creation"), "approval_relative_path": APPROVAL,
        "reviewed_preview": binding(PREVIEW, "Exact reviewed text, not independently edited"), "reading_copy_relative_path": COPY,
        "diff_relative_path": DIFF, "decision_relative_path": DECISION, "consistency_review_relative_path": REVIEW + ".json",
        "story_word_count": 2896, "word_count_method": "Whitespace-delimited words after the Story Draft heading; adaptation note excluded.",
        "application_scope": "All 22 approved edits and no additional prose changes. The archive prelude and final warning passage remain exact.",
        "authority_boundary": "Approval to create this draft does not adopt the manuscript or canon and does not change active versions or stage locks.",
        "unresolved": ["Chapter 2 and approved images unavailable", "Private calendar and historical-warning costs before continuation", "Next-visit access after permit expiry and loose-fitting clearance", "Scratch authorship and first-photo comparison", "Formal manuscript adoption before manga preproduction"]
    }
    copy_map = {"record_type": "versioned_manuscript_reading_copy", "project_id": PID, "version": "v001", "status": "draft_inactive", "chapter_id": chapter_id, "canonical_relative_path": DRAFT, "canonical_sha256": sha(preview), "reading_copy_relative_path": COPY, "reading_copy_sha256": sha(preview), "metadata_relative_path": METADATA, "independent_editing_allowed": False, "source_ingestion": "excluded", "refresh_policy": "Create a new version from a separately approved managed manuscript; never edit or replace this version in place."}
    diff = "".join(difflib.unified_diff(original.decode().splitlines(keepends=True), preview.decode().splitlines(keepends=True), fromfile=source["original_path"], tofile=DRAFT))
    decision = {"schema_version": "3.0.0", "decision_id": "SMA-DEC-APPLY-CHAPTER-001-V001", "project_id": PID, "decision_type": "apply_change_set", "subject_ids": [change["change_set_id"], chapter_id, *scenes], "decision": "Applied the user-approved exact changes to a new inactive manuscript version and an identical versioned reading copy; did not replace source or activate authority.", "rationale": "The user approved the exact Chapter 1 changes for inactive draft creation. Materialized precisely the approved preview bytes with a deterministic source-to-version diff. The runtime helper was not invoked because it requires a managed base and automatically sets active_manuscript_version.", "actor": "manga-chapter-writer", "decided_at": timestamp, "evidence": change["source_evidence"], "result_artifacts": [DRAFT, METADATA, COPY, COPY_MAP, DIFF, REVIEW + ".json"], "supersedes_decision_id": None}
    layout_decision = {"schema_version": "3.0.0", "decision_id": "SMA-DEC-WORKSPACE-STRUCTURE-V001", "project_id": PID, "decision_type": "editorial", "subject_ids": [PID], "decision": "Authorized Manga Creator folder refactoring and read-only comparison with the Blackouts project's generic structure, alongside approved inactive Chapter 1 draft creation.", "rationale": "The user explicitly requested folder refactoring and permitted checking the named comparison project. Keep the earlier source-preservation rule in force: add the organized working tree and indexes, do not move originals or rewrite historical packages. Import no other story content or authority.", "actor": "user", "decided_at": approval["decided_at"], "evidence": [], "result_artifacts": [".manga-studio/workspace-layout-v001.json", ".manga-studio/decisions/workspace-structure-v001.md", "MANGA-STUDIO.md", "manga/README.md"], "supersedes_decision_id": None}
    old_review = read(OLD_REVIEW)
    review = {**old_review, "record_type": "manuscript_consistency_review", "target": {**old_review["target"], "relative_path": DRAFT}, "status": "review_ready_with_warnings", "approval_granted": False,
        "scope": "Entire materialized Chapter 1 is byte-identical to the previously reviewed full preview. Rechecked exact change application, source preservation, diff, copy parity, active state and folder isolation; carry forward the existing editorial findings without claiming an independent reader test.",
        "review_basis": binding(OLD_REVIEW, "Prior full-preview editorial review"), "application_decision_relative_path": DECISION, "reading_copy_relative_path": COPY,
        "draft_application": {"exact_reviewed_text": True, "localized_edits": 22, "additional_prose_edits": 0, "active": False},
        "checks": []}
    for check in old_review["checks"]:
        converted = {k: v for k, v in check.items() if k != "preview_spans"}
        converted["manuscript_spans"] = [{**span, "relative_path": DRAFT} for span in check.get("preview_spans", [])]
        if converted["id"] == "SMA-CHECK-008":
            converted["assessment"] = "Exact-change approval is now recorded and a new inactive draft and hash-bound reading copy exist. No manuscript adoption, canon adoption, active-version assignment, stage lock, artwork, image job or publication is inferred. Original and historical package bytes remain unchanged."
        review["checks"].append(converted)
    review["schema_note"] = "This textual manuscript review uses the project-local structured report, with target hashes, exact source locators and known issue IDs checked. Installed production review schemas do not represent textual manuscript review; no page-quality score or artwork review is claimed."
    review_md = ["# Chapter 1 Manuscript v001 Consistency Review", "", "Status: review ready with warnings. The exact changes are approved for creation; the resulting manuscript remains inactive and unadopted.", "", review["scope"], "", "## Application", "", "- New managed draft: `" + DRAFT + "`", "- Reading copy: `" + COPY + "`", "- Both match the approved preview SHA-256: `" + sha(preview) + "`", "- 22 approved edits; zero additional prose edits.", "- Deterministic diff: `" + DIFF + "`", "", "## Editorial Assessment", "", old_review["assessment"], "", "All eight prior checks and all thirty issue dispositions are carried forward with the manuscript target and identical line spans. This is not a claim of an independent reader review. No chapter or artwork unavailable in the source root was reviewed.", "", "## Warnings", ""]
    review_md += ["- " + w["id"] + ": " + w["message"] for w in old_review["warnings"]]
    review_md += ["", "## Authority", "", "All active versions remain unset and all nine locks remain false. Manuscript adoption is still required before manga preproduction. The JSON companion includes exact source evidence, manuscript spans and all thirty issue dispositions.", ""]
    dirs = [".manga-studio/" + d for d in WORKSPACE_DIRECTORIES] + [".manga-studio/references", ".manga-studio/storyboard/panel-plans", ".manga-studio/continuity/snapshots", ".manga-studio/tooling", "manga/00-series", "manga/01-style", "manga/02-references", "manga/03-story/arc-01/chapter-001", "manga/04-production/arc-01/chapter-001"] + ["manga/02-references/" + category for category in ("characters", "environments", "objects", "effects")]
    layout = {"record_type": "manga_studio_workspace_layout", "project_id": PID, "version": "v001", "project_root": ".", "managed_root": ".manga-studio", "visible_root": "manga", "entry_point": "MANGA-STUDIO.md", "source_roots": ["."], "runtime_version_checked": "3.1.0", "refactor_mode": "additive_non_destructive", "originals_moved": False, "comparison": {"project_display_name": "01-My Roommate Only Appears During Blackouts", "scope": "Top-level folder organization and arc/chapter nesting only", "content_imported": False, "approval_or_lock_state_imported": False, "comparison_modified": False}, "source_inventory_relative_path": ".manga-studio/source/inventory-baseline-v001.json", "required_runtime_directories": [".manga-studio/" + d for d in WORKSPACE_DIRECTORIES], "additional_directories": [d for d in dirs if d not in [".manga-studio/" + r for r in WORKSPACE_DIRECTORIES]], "visible_sections": [{"relative_path": "manga/00-series", "authority": "Indexes existing project planning/evidence; no new canon"}, {"relative_path": "manga/01-style", "authority": "Required format and high-quality policy; no visual lock"}, {"relative_path": "manga/02-references", "authority": "Empty reference register; no approved assets"}, {"relative_path": "manga/03-story", "authority": "Versioned reading copies; managed manuscript remains canonical storage"}, {"relative_path": "manga/04-production", "authority": "Reserved production organization; all production gates pending"}], "managed_ownership": {"source": ".manga-studio/source", "canon": ".manga-studio/canon", "story_architecture": ".manga-studio/story", "manuscript": ".manga-studio/manuscript/versions", "revision_policy_plan_changes_diff": ".manga-studio/revisions", "analysis": ".manga-studio/analysis", "storyboard": ".manga-studio/storyboard", "panel_direction": ".manga-studio/storyboard/panel-plans", "continuity": ".manga-studio/continuity", "visual_reference_records": ".manga-studio/references", "job_handoffs": ".manga-studio/handoff", "approved_panels": ".manga-studio/panels", "lettering": ".manga-studio/lettering", "composed_pages": ".manga-studio/pages", "exports": ".manga-studio/exports", "approvals": ".manga-studio/approvals", "locks": ".manga-studio/locks", "decisions": ".manga-studio/decisions", "tooling": ".manga-studio/tooling"}, "reading_copies": [COPY_MAP], "source_exclusions_added": ["manga/**", "MANGA-STUDIO.md"], "path_policy": "Artifact paths are relative to this project root. No external project or reference-image paths are stored.", "history_policy": "Keep old sources, snapshots, reviewed packages, tool scripts and approval targets at their original paths and bytes."}
    series = {"record_type": "series_direction_index", "project_id": PID, "version": "v001", "active_canon": None, "entries": [binding(".manga-studio/revisions/phase-3-v001/creative-brief-v001.md", "Accepted creative direction through the approved parent-plan manifest"), binding(".manga-studio/revisions/phase-3-v001/success-plan-v001.md", "Accepted success plan, no validated market result"), binding(".manga-studio/revisions/phase-3-v001/decision-proposals-v001.json", "Fourteen accepted reconstruction directions; unresolved details not adopted"), binding(".manga-studio/analysis/AUDIT-v001.md", "Historical evidence-based audit"), binding(".manga-studio/revisions/phase-4-proposal-v001/working-continuity-v001.md", "Working continuity, not adopted canon")], "parent_plan_approval_relative_path": ".manga-studio/approvals/approval-8300f092c2fb44d98842a89d829e3fb3.json"}
    policy = {"record_type": "future_production_requirements", "project_id": PID, "version": "v001", "status": "requirements_only_not_a_job_or_lock", "source_language": "en", "output_language": "en", "reading_direction": "left-to-right", "format": "paged_manga", "interiors": "black-and-white", "covers": "color permitted only in separately approved cover planning", "quality_profile_tier": "high", "detail_budget": "high", "self_check_required": True, "panel_variation_policy": "event_driven", "reference_variation_policy": "reference_driven", "future_reference_requirement": "Actual approved hash-locked references and exact ordered attachment checklists before dependent job release", "panel_art_prohibited": ["dialogue", "captions", "balloons", "SFX text", "borders", "page numbers", "signatures", "watermarks", "color"], "sfx_required_fields": ["sound source", "reader-facing meaning", "intensity", "language", "translation context", "lettering intent"], "nemu": "geometry-only", "reading_sequence": "explicit", "panel_event": "one dominant event with motivated camera and dialogue-safe zones", "image_generation_enabled": False, "approved_reference_images": [], "release_readiness": False, "print_dimensions": "Configured dimensions remain runtime placeholders, not approved print specifications."}
    references = {"record_type": "reference_availability_register", "project_id": PID, "version": "v001", "status": "no_approved_visual_assets", "assets": [], "category_directories": ["manga/02-references/" + c for c in ("characters", "environments", "objects", "effects")], "job_generation_started": False, "reference_image_paths": [], "note": "These are organizational directories, not reference images. No external project assets or nonexistent attachment paths have been imported."}
    readiness = {"record_type": "chapter_production_readiness", "project_id": PID, "version": "v001", "chapter_id": chapter_id, "status": "not_started", "draft_relative_path": DRAFT, "draft_is_active": False, "storyboard_relative_path": None, "nemu_relative_path": None, "image_jobs": [], "approved_assets": [], "stage_locks": context.config["stage_locks"], "image_generation_enabled": False, "required_quality_profile": "high", "blocking_reasons": ["Manuscript not adopted", "Canon not adopted", "Story and storyboard locks not authorized", "No approved reference artwork", "No approved storyboard, geometry-only nemu or panel plans"], "original_page_prompts": "Preserved source evidence only, not revised production scripts."}
    outputs = {DRAFT: preview, COPY: preview, METADATA: encode(metadata), COPY_MAP: encode(copy_map), DIFF: diff.encode(), DECISION: encode(decision), ".manga-studio/decisions/workspace-structure-v001.json": encode(layout_decision), REVIEW + ".json": encode(review), REVIEW + ".md": ("\n".join(review_md) + "\n").encode(), ".manga-studio/workspace-layout-v001.json": encode(layout), "manga/00-series/index-v001.json": encode(series), "manga/01-style/production-policy-v001.json": encode(policy), "manga/02-references/reference-register-v001.json": encode(references), "manga/04-production/arc-01/chapter-001/readiness-v001.json": encode(readiness)}
    for directory in sorted(set(dirs)):
        path = ROOT / directory
        has_existing_content = path.is_dir() and any(p.name[:2] != "._" for p in path.iterdir())
        has_planned_content = any(p.startswith(directory + "/") for p in outputs)
        has_planned_subdir = any(d.startswith(directory + "/") for d in dirs)
        if not has_existing_content and not has_planned_content and not has_planned_subdir:
            outputs[directory + "/.gitkeep"] = b""
    return outputs, sorted(set(dirs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    outputs, directories = assemble()
    if args.write:
        for relative in outputs:
            assert not (ROOT / relative).exists(), "Refusing to overwrite: " + relative
        for directory in directories:
            (ROOT / directory).mkdir(parents=True, exist_ok=True)
        for relative, data in outputs.items():
            target = ROOT / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(data)
    print(json.dumps({"mode": "write_new" if args.write else "dry_run", "new_files": len(outputs), "managed_and_visible_directories": len(directories), "draft_relative_path": DRAFT, "draft_sha256": sha(outputs[DRAFT]), "reading_copy_relative_path": COPY, "reading_copy_sha256": sha(outputs[COPY]), "active": False}, indent=2))
