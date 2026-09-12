"""Assemble an exact, source-bound revision proposal; never apply it to prose authority."""
import argparse
import difflib
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).resolve().parent
REL = PACKET.relative_to(ROOT).as_posix()
PID = "ms-70391ae1065048cf8bdd564959abd6c3"
CHAPTER = "chapter-fb585a7fd3e7450e936edbcfce992566"
SCENE = "scene-3b27382ec9a049e2acde70d7cf88fc10"
CHANGE = ".manga-studio/revisions/change-sets/sma-ch01-balanced-v001.json"
PREVIEW = f"{REL}/chapter-01-reading-preview-v001.md"
DIFF = ".manga-studio/revisions/diffs/sma-ch01-balanced-proposal-v001.diff"
DECISION = ".manga-studio/decisions/editorial-option-b-approval-v001.json"
PLAN_APPROVAL = ".manga-studio/approvals/approval-8300f092c2fb44d98842a89d829e3fb3.json"
POLICY_APPROVAL = ".manga-studio/approvals/approval-389787b7b7e747c1ba1be1d3204dc970.json"


def read(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode()


def assemble():
    inputs = read(f"{REL}/edit-input-v001.json")
    raw = (ROOT / inputs["source_relative_path"]).read_bytes()
    assert digest(raw) == inputs["source_sha256"], "Original changed; rebase required"
    original = raw.decode("utf-8")
    lines = original.splitlines(keepends=True)
    provenance = read(".manga-studio/source/provenance.json")
    source = next(r for r in provenance["records"] if r["original_path"] == inputs["source_relative_path"])
    assert (ROOT / source["snapshot_path"]).read_bytes() == raw
    source_map = read(source["source_map_path"])
    locator_keys = ("document_id", "chapter_id", "scene_id", "source_unit_id", "source_relative_path", "line_start", "line_end", "byte_start", "byte_end", "content_fingerprint")
    cursor = 0
    parts = []
    edits = []
    evidence = {}
    for proposed in inputs["edits"]:
        start, end = proposed["lines"]
        assert cursor <= start - 1 < end <= len(lines), proposed["id"]
        before = "".join(lines[start - 1:end])
        after = proposed["after"] + "\n"
        assert before != after and original.count(before) == 1
        parts.append("".join(lines[cursor:start - 1]))
        preview_start = sum(p.count("\n") for p in parts) + 1
        parts.append(after)
        locators = []
        for unit in source_map["source_units"]:
            if unit["line_start"] <= end and unit["line_end"] >= start:
                locator = {"project_id": PID, **{key: unit[key] for key in locator_keys}}
                locators.append(locator)
                evidence[unit["source_unit_id"]] = locator
        assert locators, proposed["id"]
        edits.append({
            "edit_id": proposed["id"], "source_lines": [start, end],
            "preview_lines": [preview_start, preview_start + after.count("\n") - 1],
            "triggering_issue_ids": [f"SMA-ISS-{i:03}" for i in proposed["issues"]],
            "accepted_proposal_ids": [f"SMA-PROP-{i:03}" for i in proposed["proposals"]],
            "owner": "manga-chapter-writer", "purpose": proposed["purpose"], "risk": proposed["risk"],
            "source_evidence": locators, "before": before, "after": after,
            "acceptance": "Exact before span matches the preserved source; exact after span appears at the recorded preview lines; the purpose holds in the full scene.",
        })
        cursor = end
    parts.append("".join(lines[cursor:]))
    preview = "".join(parts)
    assert preview.split("At 11:41 PM", 1)[0] == original.split("At 11:41 PM", 1)[0]
    assert preview.endswith(original[original.index("The scratched name waited"):])
    assert preview.count("I will bring better bread.") == 1
    # New wording must not identify Tomas before the existing mutual introduction.
    first_name = preview.index('"Tomas Rivera."')
    assert not re.search(r"\bTomas\b", preview[preview.index("## Story Draft"):first_name])
    for hour in range(8):
        marker = f"12:{hour:02}."
        assert preview.count("\n" + marker + "\n") == 1, marker
    issue_ids = sorted({i for e in edits for i in e["triggering_issue_ids"]})
    plan = read(".manga-studio/revisions/plans/sma-reconstruction-v001.json")
    assert set(issue_ids) <= set(plan["triggering_issue_ids"])
    change = {
        "schema_version": "3.0.0", "project_id": PID, "change_set_id": "SMA-CS-CH01-BALANCED",
        "version": "v001", "revision_policy_id": "SMA-POLICY-BALANCED", "revision_plan_id": "SMA-PLAN-RECONSTRUCTION",
        "target_stable_ids": [CHAPTER, SCENE], "triggering_issue_ids": issue_ids,
        "source_evidence": list(evidence.values()),
        "operation": {"type": "replace_text", "target_relative_path": source["snapshot_path"], "target_sha256": digest(raw), "before": original, "after": preview},
        "expected_result": "Proposed source-to-new-derivative transformation only: 22 exact localized edits in one atomic payload. The immutable snapshot is a comparison base, NEVER an in-place write target. After separate exact-change approval, the chapter-writer may materialize identical reviewed text in a new inactive manuscript version and create a deterministic diff. The runtime apply-change-set helper is deliberately not invoked: it requires a managed manuscript target and automatically changes active_manuscript_version.",
        "alternatives": ["Retain the original and decline these changes.", "Request a separately versioned amendment by edit ID before any prose application."],
        "preserve": plan["preserve"] + ["Exact archive prelude and final scratched-warning passage.", "First meeting's 12:00-12:07 sequence, names, banter, reciprocal choice and distinct paper exchanges."],
        "author_voice_impact": {"level": "medium", "notes": "Localized continuity additions and one hair-description trim; no global prose polish. Read the full preview to judge whether the added handling is too explicit."},
        "canon_impact": {"level": "medium", "notes": "Implements accepted physical-model and rule directions provisionally. Exact permit, doorway, split-sill and apron-pencil details remain reviewable. No active canon version is created."},
        "continuity_impact": {"level": "high", "notes": "Clarifies spatial state, completed transfer, reply timing, prop custody, year inference and clue selection. Does not repair untouched legacy scripts or decide continuation-only unknowns."},
        "structural_impact": {"level": "low", "notes": "Preserves two analytical scenes and the opening's core sequence; no new chapters or forced arc formula."},
        "dependencies": [],
        "acceptance_criteria": [
            "Separate user approval binds this exact payload and preview checksum before any new manuscript is materialized.",
            "All 25 original candidates, 24 imported snapshots/maps and prior approved package hashes remain unchanged.",
            "All 22 source spans match uniquely and reassembly yields the exact preview and deterministic diff.",
            "Both men stay in their own eras; the returned page fully crosses before 12:07; the two paper objects remain distinct.",
            "The year is a supported guess before Tomas answers; both signal and broker are recorded without proving guilt.",
            "Full first seven minutes, author voice anchors, names and final emotional sequence are preserved.",
            "All 30 diagnostic issues have an honest disposition, including deferrals and missing material.",
            "No automatic approval, active-version assignment, lock activation, source overwrite, artwork or publishing."
        ], "approval_status": "proposed",
    }
    diff = "".join(difflib.unified_diff(original.splitlines(keepends=True), preview.splitlines(keepends=True), fromfile=inputs["source_relative_path"], tofile=PREVIEW))
    plan_approval = read(PLAN_APPROVAL)
    decision = {
        "schema_version": "3.0.0", "decision_id": "SMA-DEC-OPTION-B-APPROVAL-001", "project_id": PID,
        "decision_type": "editorial", "subject_ids": ["SMA-PLAN-RECONSTRUCTION", "SMA-POLICY-BALANCED"] + [f"SMA-PROP-{i:03}" for i in range(1, 15)],
        "decision": "Accept Option B and its manifest-bound brief, success plan, balanced policy, revision plan and fourteen recommended choices as directions for exact Chapter 1 proposal preparation.",
        "rationale": "The user replied 'lets proceed' to the preceding request to approve Option B and its accompanying proposed choices and revision plan. The reviewed package explicitly reserved exact-change approval, canon adoption and stage-lock activation. Record the actual plan decision, not an approval of unseen text.",
        "actor": "user", "decided_at": plan_approval["decided_at"], "evidence": [],
        "result_artifacts": [PLAN_APPROVAL, POLICY_APPROVAL, f"{REL}/authorization-v001.json"], "supersedes_decision_id": None,
    }
    authorization = {
        "record_type": "exact_change_preparation_authorization", "project_id": PID, "version": "v001",
        "user_message": "lets proceed", "preceding_question_summary": "Approval of Option B and the accompanying proposed choices and revision plan.",
        "approval_paths": [PLAN_APPROVAL, POLICY_APPROVAL], "decision_path": DECISION,
        "package_manifest_relative_path": ".manga-studio/revisions/phase-3-v001/package-manifest-v001.json",
        "package_manifest_sha256": "39a56110a135bccb13cb9ccbf0b0d03600ef4e621a6992d7b08362ee54dd976a",
        "accepted_direction_ids": [f"SMA-PROP-{i:03}" for i in range(1, 15)],
        "exact_changes_approved": False, "canon_adopted": False, "stage_locks_authorized": False,
        "scope": "Prepare exact text, readable preview, deterministic comparison and consistency review inside revisions. Do not materialize or activate a manuscript until the exact payload is approved.",
        "gate_note": "The diagnostic and plan approval records are valid but their runtime stage locks remain false. Proposal preparation follows explicit user authorization without representing activation gates as passed.",
        "application_note": "This is a source-bound proposal, not a runtime-executable managed-manuscript change set. Never edit its snapshot target in place. Use the chapter-writer for a new inactive draft after exact-change approval; the runtime helper would automatically activate its output.",
    }
    word_count = lambda t: len(t.split("## Story Draft\n", 1)[1].split())
    metrics = {"original_story_words": word_count(original), "preview_story_words": word_count(preview), "localized_edits": len(edits), "changed_source_lines": sum(b-a+1 for a,b in (e["source_lines"] for e in edits)), "original_total_lines": len(lines)}
    outputs = {CHANGE: encoded(change), PREVIEW: preview.encode(), DIFF: diff.encode(), DECISION: encoded(decision), f"{REL}/authorization-v001.json": encoded(authorization)}
    outputs[f"{REL}/exact-edit-register-v001.json"] = encoded({"record_type": "source_to_preview_edits", "project_id": PID, "version": "v001", "status": "proposed", "source_relative_path": inputs["source_relative_path"], "source_sha256": digest(raw), "snapshot_relative_path": source["snapshot_path"], "preview_relative_path": PREVIEW, "preview_sha256": digest(preview.encode()), "change_set_relative_path": CHANGE, "metrics": metrics, "edits": edits})
    md = ["# Exact Chapter 1 Edits v001", "", "Status: proposed. This register shows every exact change; nothing here has been applied to an authoritative manuscript. Line numbers identify the immutable original and the complete reading preview, respectively.", "", f"Source: `{inputs['source_relative_path']}`", "", f"Reading preview: `{PREVIEW}`", "", f"Atomic payload: `{CHANGE}`", "", f"{len(edits)} localized edits. Story words: {metrics['original_story_words']} -> {metrics['preview_story_words']} (whitespace-delimited, adaptation note excluded).", ""]
    for edit in edits:
        a,b = edit["source_lines"]
        c,d = edit["preview_lines"]
        md += [f"## {edit['edit_id']}", "", f"Original lines {a}-{b}; preview lines {c}-{d}. Issues: {', '.join(edit['triggering_issue_ids'])}. Accepted directions: {', '.join(edit['accepted_proposal_ids'])}.", "", edit["purpose"], "", "Before:", "", "```text", edit["before"].rstrip("\n"), "```", "", "After:", "", "```text", edit["after"].rstrip("\n"), "```", "", "Risk: " + edit["risk"], ""]
    outputs[f"{REL}/exact-edits-v001.md"] = ("\n".join(md) + "\n").encode()
    return outputs, metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    artifacts, metrics = assemble()
    if args.write:
        for relative in artifacts:
            assert not (ROOT / relative).exists(), "Refusing to overwrite: " + relative
        for relative, contents in artifacts.items():
            target = ROOT / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(contents)
    print(json.dumps({"mode": "write_new" if args.write else "dry_run", "metrics": metrics, "artifacts": [{"relative_path": p, "sha256": digest(b)} for p,b in artifacts.items()]}, indent=2))
