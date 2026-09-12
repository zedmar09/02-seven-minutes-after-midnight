"""Resolve reviewed audit inputs against immutable sources; never edit story files."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / ".manga-studio"
ANALYSIS = WORK / "analysis"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_new(path, value):
    encoded = value if isinstance(value, str) else json.dumps(value, indent=2, ensure_ascii=True) + "\n"
    with path.open("x", encoding="utf-8") as stream:
        stream.write(encoded)


def issue_id(number):
    return f"SMA-ISS-{number:03d}"


config = read_json(WORK / "project.json")
project_id = config["project_id"]
provenance = read_json(WORK / "source/provenance.json")
inventory = read_json(WORK / "source/inventory-baseline-v001.json")
spec = read_json(ANALYSIS / "audit-issue-input-v001.json")
register = read_json(ANALYSIS / "audit-register-input-v001.json")
aliases = register["aliases"]
records = {item["original_path"]: item for item in provenance["records"] if item["source_status"] == "active"}
maps = {name: read_json(ROOT / record["source_map_path"]) for name, record in records.items()}
texts = {name: (ROOT / record["normalized_path"]).read_bytes() for name, record in records.items()}
catalog_ids = {name: f"SRC-{i:02d}" for i, name in enumerate(sorted(records), 1)}


def evidence(alias, needle):
    name = aliases[alias]
    data = texts[name]
    hits = []
    for unit in maps[name]["source_units"]:
        excerpt = data[unit["byte_start"]:unit["byte_end"]].decode("utf-8")
        if needle in excerpt:
            hits.append(unit)
    if len(hits) != 1:
        raise ValueError(f"Evidence must resolve to one source unit: {alias}: {needle!r}; matches={len(hits)}")
    unit = hits[0]
    raw = (ROOT / records[name]["snapshot_path"]).read_text(encoding="utf-8").splitlines()
    source_lines = "\n".join(raw[unit["line_start"] - 1:unit["line_end"]])
    if needle not in source_lines:
        raise ValueError(f"Original and normalized line locators disagree: {alias}: {needle}")
    return {
        "project_id": project_id,
        **{key: unit[key] for key in (
            "document_id", "chapter_id", "scene_id", "source_unit_id", "source_relative_path",
            "line_start", "line_end", "byte_start", "byte_end", "content_fingerprint"
        )},
    }


def citation(locator):
    return f"{catalog_ids[locator['source_relative_path']]} lines {locator['line_start']}-{locator['line_end']} (unit {locator['source_unit_id']})"


errors = []
resolved_issues = []
for item in spec["issues"]:
    try:
        resolved_issues.append((item, [evidence(*pair) for pair in item["evidence"]]))
    except ValueError as exc:
        errors.append(str(exc))
for collection, field in ((register["threads"], "setup"), (register["timeline"], "evidence"), (register["cast"], "evidence")):
    for row in collection:
        try:
            row["source_evidence"] = evidence(*row[field])
        except ValueError as exc:
            errors.append(str(exc))
for name, namespace, alias, needle in register["entities"]:
    try:
        evidence(alias, needle)
    except ValueError as exc:
        errors.append(str(exc))
if errors:
    raise SystemExit("\n".join(errors))

outputs = ["diagnostic-draft-v001.json", "full-diagnostic-v001.md", "coverage-v001.json", "coverage-v001.md", "entity-register-v001.json", "continuity-registers-v001.json", "continuity-registers-v001.md", "character-assessment-v001.md", "source-integrity-v001.json"]
for filename in outputs:
    if (ANALYSIS / filename).exists():
        raise SystemExit(f"Refusing to overwrite versioned artifact: .manga-studio/analysis/{filename}")

# Register identifiers only; this does not adopt entity facts or merge disputed names.
runtime = Path.home() / ".agents/skills/.manga-studio-runtime"
runtime_version = read_json(runtime / "current.json")["version_path"]
sys.path.insert(0, str(runtime / runtime_version / "scripts/lib"))
from manga_studio.project import discover_project, get_or_create_entity_id, provenance_errors
from manga_studio.structure import validate_source_maps

context = discover_project(ROOT)
entity_records = []
entity_index = {}
for name, namespace, alias, needle in register["entities"]:
    identity = get_or_create_entity_id(context, namespace, "audit-source-entity:" + name, name)
    entity_index[name] = (identity, namespace)
    entity_records.append({"id": identity, "display_name": name, "namespace": namespace, "status": "source-attested label; not adopted canon", "source_evidence": evidence(alias, needle), "identity_note": "Unresolved substitute label; no automatic alias merge" if name in {"Inez", "Rafael Aragon"} else "Analytical identifier only"})

chapter_map = maps[aliases["chapter"]]
chapter_id = chapter_map["chapters"][0]["chapter_id"]
scene_ids = {"prelude": chapter_map["scenes"][0]["scene_id"], "station": chapter_map["scenes"][1]["scene_id"]}
related_namespaces = {"characters": "character_ids", "locations": "location_ids", "props": "prop_ids", "timeline_events": "timeline_event_ids", "plot_threads": "plot_thread_ids"}
findings = []
markdown = ["# Full Diagnostic Audit v001", "", "Status: proposed, not approved. Complete review of the available root, not of unavailable future chapters. No reconstruction or artwork performed.", "", "Source keys resolve to exact root-relative paths in coverage-v001.md and coverage-v001.json. Every locator is checked against an active source-map unit and immutable original snapshot. Priorities describe order of work; severity describes impact. No P0 emergency is asserted.", "", "Document-level chapter IDs on supporting sources are parser containers, not additional story chapters. The actual manuscript has one chapter and two analytical scenes; their boundaries are not approved story restructuring.", ""]
for item, locators in resolved_issues:
    related = {field: [] for field in related_namespaces.values()}
    for name in item["entities"]:
        identity, namespace = entity_index[name]
        if namespace in related_namespaces:
            related[related_namespaces[namespace]].append(identity)
    finding = {
        "issue_id": issue_id(item["n"]), "category": item["category"], "severity": item["severity"],
        "confidence": item["confidence"], "status": "open", "description": item["description"],
        "why_it_matters": item["why"], "evidence": locators,
        "affected_chapter_ids": [chapter_id] if item["scenes"] else [],
        "affected_scene_ids": [scene_ids[key] for key in item["scenes"]], "related_ids": related,
        "alternatives": item["solutions"], "uncertainty": item["uncertainty"], "adaptation_impact": item["impact"],
    }
    findings.append(finding)
    markdown.extend([f"## {finding['issue_id']}: {item['title']}", "", f"Priority: {item['priority']} | Category: {item['category']} | Severity: {item['severity']} | Confidence: {item['confidence']:.0%}", "", f"Evidence class: {item['kind']}. Status: open, awaiting review.", "", item["description"], "", "Why it matters: " + item["why"], "", "Preserve: " + item["preserve"], "", "Evidence:", ""])
    for pair, locator in zip(item["evidence"], locators):
        markdown.append(f"- {citation(locator)}: \"{pair[1]}\". Source: `{locator['source_relative_path']}`.")
    markdown.extend(["", "Affected manuscript chapter IDs: " + (", ".join(finding["affected_chapter_ids"]) or "None; whole-outline or workflow scope."), "", "Affected scene IDs: " + (", ".join(finding["affected_scene_ids"]) or "None; future scenes are not invented."), "", "Related entity IDs: " + ("; ".join(f"{name}: {entity_index[name][0]}" for name in item["entities"]) or "None."), "", "Possible solutions and tradeoffs:", "", "1. " + item["solutions"][0], "2. " + item["solutions"][1], "", "Uncertainty: " + item["uncertainty"], "", "Adaptation impact: " + item["impact"], "", "Dependencies: " + (", ".join(issue_id(n) for n in item["dependencies"]) or "No prerequisite finding."), ""])

created = datetime.now(timezone.utc).isoformat()
draft = {"schema_version": "3.0.0", "project_id": project_id, "report_id": "sma-comprehensive-audit", "report_version": "v001", "title": "Seven Minutes After Midnight: Complete Available-Source Audit", "scope": "All 24 supplied story documents: one complete prose chapter, fourteen page scripts, three cover prompts, and six supporting documents; all seven planned arcs reviewed as outline only.", "status": "proposed", "generated_by": "manga-story-diagnostician coordinated by manga-creator", "created_at": created, "source_map_checksums": sorted({r["source_map_checksum"] for r in records.values()}), "findings": findings, "limitations": ["Chapter 2 and claimed reader assets are absent from this root.", "Only one manuscript chapter exists; planned scenes, endings, audience response, and commercial success cannot be evaluated as completed work.", "No approved canon, manuscript, storyboard, reference images, or stage locks are present.", "No online manuscript search, external historical/market/IP research, publication, or artwork operations were performed.", "Two analytical scenes are evidence navigation, not approved story restructuring; supporting document chapter IDs are parser containers.", "Priorities, evidence classes, preserve notes, dependencies, and tradeoffs are retained in the full Markdown companion and versioned issue input because the core issue schema does not have fields for all of them."]}
write_new(ANALYSIS / "diagnostic-draft-v001.json", draft)
write_new(ANALYSIS / "full-diagnostic-v001.md", "\n".join(markdown) + "\n")
write_new(ANALYSIS / "entity-register-v001.json", {"project_id": project_id, "version": "v001", "status": "analysis_only", "entities": entity_records})

coverage = []
for name, record in sorted(records.items()):
    text = texts[name].decode("utf-8")
    match = re.search(r"page-(\d{3})-chatgpt", name)
    batch = "B01 prose and supporting documents"
    if match:
        page = int(match.group(1))
        batch = "B02 pages 1-4" if page <= 4 else "B03 pages 5-8" if page <= 8 else "B04 pages 9-12" if page <= 12 else "B05 pages 13-14 and covers"
    elif "cover" in name.lower():
        batch = "B05 pages 13-14 and covers"
    coverage.append({"source_key": catalog_ids[name], "document_id": record["document_id"], "relative_path": name, "usage_role": record["usage_role"], "original_sha256": record["original_sha256"], "source_map_path": record["source_map_path"], "source_map_sha256": record["source_map_checksum"], "line_count": len(text.splitlines()), "word_count": len(re.findall(r"\b[\w'-]+\b", text)), "reviewed_lines": [1, len(text.splitlines())], "review_status": "entire document read and assessed", "batch": batch, "panel_count": len(re.findall(r"^PANEL \d+ -", text, re.M)) if match else 0})
story_text = texts[aliases["chapter"]].decode("utf-8").split("## Story Draft", 1)[1]
coverage_report = {"project_id": project_id, "version": "v001", "coverage_basis": "all current imported story sources; no sampling", "documents_reviewed": len(coverage), "documents_available": len(records), "coverage_percent": 100, "prose_chapters_available": 1, "analytical_scenes": scene_ids, "manuscript_chapter_id": chapter_id, "prose_word_count": len(re.findall(r"\b[\w'-]+\b", story_text)), "page_scripts": 14, "scripted_panels": sum(r["panel_count"] for r in coverage), "cover_prompts": 3, "supporting_documents": 6, "planned_arcs_reviewed": 7, "planned_chapters": 105, "drafted_chapters_claimed_by_notes": 2, "reader_images_available": 0, "excluded_material": [{"relative_path": ".gitignore", "reason": "repository housekeeping", "imported": False}, {"pattern": "._*", "reason": "macOS sidecars; left untouched", "imported": False}, {"pattern": ".git/**", "reason": "repository internal metadata", "imported": False}, {"pattern": ".manga-studio/**", "reason": "new audit workspace, not original story", "imported": False}, {"relative_path": "AGENTS.md", "reason": "new workspace operating instructions", "imported": False}], "records": coverage}
write_new(ANALYSIS / "coverage-v001.json", coverage_report)
lines = ["# Audit Coverage v001", "", f"24/24 available story documents read in full (100%); one manuscript chapter, {coverage_report['prose_word_count']} prose words, two analytical scenes. Fourteen page scripts contain {coverage_report['scripted_panels']} panels. Three cover prompts and six supporting documents were also reviewed.", "", "The 105-chapter target is a plan. Coverage does not mean that 105 chapters were supplied. Chapter 2 and all claimed reader images are absent from the root.", "", f"Chapter 1 ID: {chapter_id}", "", f"Archive prelude (prose lines 11-27): {scene_ids['prelude']}", "", f"Station encounter and aftermath (prose lines 29-end): {scene_ids['station']}", "", "Source map chapter containers in the other 23 documents are not manuscript chapters. Scene boundaries are analytical, not adopted or locked.", "", "| Source | Batch | Lines reviewed | Role | Root-relative path |", "|---|---|---|---|---|"]
for row in coverage:
    lines.append(f"| {row['source_key']} | {row['batch']} | 1-{row['line_count']} | {row['usage_role']} | `{row['relative_path']}` |")
lines.extend(["", "No unsupported story formats were found. The one unsupported inventory item is .gitignore, excluded as housekeeping. Sidecars and repository internals were not story inputs. The full inventory baseline includes SHA-256 for all 25 content/housekeeping candidates.", ""])
write_new(ANALYSIS / "coverage-v001.md", "\n".join(lines))

for row in register["threads"]:
    row["stable_id"] = get_or_create_entity_id(context, "plot_threads", row["id"], row["name"])
    row["setup_payoff_id"] = get_or_create_entity_id(context, "setups_payoffs", row["id"], row["name"])
    row["entity_ids"] = [entity_index[name][0] for name in row["entities"]]
    row["issue_ids"] = [issue_id(n) for n in row["issues"]]
for row in register["timeline"]:
    row["stable_id"] = get_or_create_entity_id(context, "timeline_events", row["id"], row["event"])
write_new(ANALYSIS / "continuity-registers-v001.json", {"project_id": project_id, "version": "v001", "status": "analysis_only_not_canon", "threads_and_setups_payoffs": register["threads"], "timeline": register["timeline"]})
lines = ["# Continuity, Threads, and Setups/Payoffs v001", "", "Analysis only. Confirmed source statements, reported events, and future plans have different authority. Stable IDs provide traceability, not canon adoption.", "", "## Timeline", ""]
for row in register["timeline"]:
    lines.extend([f"### {row['id']}: {row['time']}", "", f"Status: {row['status']}. {row['event']}", "", "Unknown: " + row["unknown"], "", "Evidence: " + citation(row["source_evidence"]), "", "Persistent timeline ID: " + row["stable_id"], ""])
lines.extend(["## Unresolved Threads and Setup/Payoff Register", "", "An open setup in an opening chapter is not automatically an error. Some objects are atmosphere unless the story promotes them to promises.", ""])
for row in register["threads"]:
    lines.extend([f"### {row['id']}: {row['name']}", "", "State: " + row["state"], "", "Setup evidence: " + citation(row["source_evidence"]) + f"; \"{row['setup'][1]}\".", "", "Payoff status: " + row["payoff"], "", "Continuity/next-review test: " + row["test"], "", "Related issues: " + ", ".join(row["issue_ids"]), "", "Persistent thread ID: " + row["stable_id"] + "; setup/payoff ID: " + row["setup_payoff_id"], ""])
write_new(ANALYSIS / "continuity-registers-v001.md", "\n".join(lines))

lines = ["# Character and Relationship Assessment v001", "", "Analysis only. Character ages and later functions come from the author's reference, not necessarily on-page dialogue. A described arc is not a completed arc.", ""]
for row in register["cast"]:
    lines.extend([f"## {row['name']}", "", "Status: " + row["status"], "", "Entity ID: " + entity_index[row["name"]][0], ""])
    for label, key in (("Want", "want"), ("Need", "need"), ("Fear", "fear"), ("Flaw or contradiction", "flaw"), ("Agency", "agency"), ("Voice", "voice"), ("Relationships", "relations"), ("Preservation boundary", "guardrail")):
        lines.extend([label + ": " + row[key], ""])
    lines.extend(["Evidence: " + citation(row["source_evidence"]), ""])
lines.extend(["## Relationship Progression", "", "The available chapter moves Daniel and Tomas from mutual alarm to playful recognition, shared physical proof, vulnerability, and an agreed return. Attraction is reciprocal; love and a committed relationship remain future development. Neither knows from this encounter that Tomas is definitively dead or targeted. Lilia's chosen-family bond is explicit in prose and should not disappear through name substitution or dialogue compression.", "", "The touch sequence changes both physical and emotional state: shared tray contact, painful wrist contact during instability, then safe fingertips through the window. The two paper exchanges are distinct acts: an archival sleeve asserting reality, then a notebook instruction returned with a promise. These are the chapter's strongest relationship beats.", "", "No completed arc exists for any character. Benjamin and Ernesto have no supplied scenes or dialogue; their voice differentiation cannot honestly be rated as executed. Inez and Rafael are retained as disputed source labels with separate identifiers; no new people or approved aliases are declared.", ""])
write_new(ANALYSIS / "character-assessment-v001.md", "\n".join(lines))

checks = []
for row in inventory["files"]:
    original = ROOT / row["relative_path"]
    checks.append({"relative_path": row["relative_path"], "baseline_sha256": row["sha256"], "current_sha256": sha(original.read_bytes()), "byte_identical": sha(original.read_bytes()) == row["sha256"]})
integrity_errors = provenance_errors(context)
map_errors = validate_source_maps(context)
integrity = {"project_id": project_id, "version": "v001", "checked_at": created, "original_candidates_checked": len(checks), "original_story_sources_checked": len(records), "snapshots_checked": len(records), "normalized_derivatives_checked": len(records), "active_source_maps_checked": len(records), "originals_byte_identical": all(row["byte_identical"] for row in checks), "provenance_errors": integrity_errors, "source_map_errors": map_errors, "records": checks, "scope_note": "24 story documents and .gitignore were hashed before import and rechecked. No writes were made to originals. Runtime active source maps, snapshots, and normalized hashes were also checked. Historical parser maps remain preserved."}
write_new(ANALYSIS / "source-integrity-v001.json", integrity)
if not integrity["originals_byte_identical"] or integrity_errors or map_errors:
    raise SystemExit("Integrity verification failed; inspect source-integrity-v001.json")
print(json.dumps({"issues": len(findings), "priorities": dict(Counter(item["priority"] for item in spec["issues"])), "sources": len(records), "prose_words": coverage_report["prose_word_count"], "panels": coverage_report["scripted_panels"], "chapter_id": chapter_id, "scene_ids": scene_ids, "originals_identical": True, "outputs_created": outputs}, indent=2))
