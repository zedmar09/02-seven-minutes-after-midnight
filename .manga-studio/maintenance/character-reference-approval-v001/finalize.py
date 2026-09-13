"""Register the user-approved stable character reference files."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
REGISTER = WORK / "maintenance/structure-cleanup-v001/working-files.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


references = [
    {
        "reference_id": "reference-daniel-soriano-v002",
        "display_name": "Daniel Soriano",
        "webp_relative_path": "manga/02-references/approved-webp/daniel-soriano.webp",
        "webp_sha256": "22590d7505a35fc99c54d101e82b3bc8f0d270e759cb003e6913d2be55818374",
        "png_relative_path": "manga/02-references/approve-png/daniel-soriano.png",
        "png_sha256": "74e62b1f802ee56d063d229554153f741aec7cae13ca83b0fd20f8eff68b320d",
        "reference_record_relative_path": ".manga-studio/continuity/references/daniel-soriano-v002.json",
    },
    {
        "reference_id": "reference-tomas-rivera-v001",
        "display_name": "Tomas Rivera",
        "webp_relative_path": "manga/02-references/approved-webp/tomas-rivera.webp",
        "webp_sha256": "f63902770629677011a9a25fa737066aec7ac57a86740021379d26b056933160",
        "png_relative_path": "manga/02-references/approve-png/tomas-rivera.png",
        "png_sha256": "b544117bf68b89c8ebf7487a4efd4a82fb820bde51bae4f11b6237974b306377",
        "reference_record_relative_path": ".manga-studio/continuity/references/tomas-rivera-v001.json",
    },
    {
        "reference_id": "reference-maribel-santos-v002",
        "display_name": "Maribel Santos",
        "webp_relative_path": "manga/02-references/approved-webp/maribel-santos.webp",
        "webp_sha256": "47ca0ad93d43f33ed449e44e53fd174756f60542bd4fcf23d1e45f675f0089f7",
        "png_relative_path": "manga/02-references/approve-png/maribel-santos.png",
        "png_sha256": "056d0292a7fc8bd67f4381b4a535cd0a47201cef981283ad26ab701a9bd85ec2",
        "reference_record_relative_path": ".manga-studio/continuity/references/maribel-santos-v002.json",
    },
    {
        "reference_id": "reference-arturo-salcedo-v001",
        "display_name": "Arturo Salcedo",
        "webp_relative_path": "manga/02-references/approved-webp/arturo-salcedo.webp",
        "webp_sha256": "b87fe969e9813ccd5636e86220b392f95bc952b95abc97ab271134f6628d4d71",
        "png_relative_path": "manga/02-references/approve-png/arturo-salcedo.png",
        "png_sha256": "460244df578008c5854279f0464e73b152969402726ed6012e2a2532866f7c96",
        "reference_record_relative_path": ".manga-studio/continuity/references/arturo-salcedo-v001.json",
    },
    {
        "reference_id": "reference-lilia-ramos-v002",
        "display_name": "Lilia Ramos",
        "webp_relative_path": "manga/02-references/approved-webp/lilia-ramos.webp",
        "webp_sha256": "6a150940441a40cd8bd22dd383be6062dffe688afbf4cd3ccfcb505cb764797d",
        "png_relative_path": "manga/02-references/approve-png/lilia-ramos.png",
        "png_sha256": "a1fde5d8381b54abf93963c140cf9ab9cf07442138ef067246af4f6d8d02f586",
        "reference_record_relative_path": ".manga-studio/continuity/references/lilia-ramos-v002.json",
    },
]

legacy = {
    "reference_id": "reference-daniel-tomas-shared-v001",
    "display_name": "Daniel and Tomas shared legacy identity input",
    "webp_relative_path": "manga/02-references/approved-webp/daniel-tomas-shared.webp",
    "webp_sha256": "985cb554a78cca3367845b7cea089fee230f950629ae2da67d6c2fe90fd45ceb",
    "png_relative_path": "manga/02-references/approve-png/daniel-tomas-shared.png",
    "png_sha256": "48f2680a489156033f49b11f5a7c02a7a0e92e0442a3a60fc2bc1487cd1bf2b6",
    "reference_record_relative_path": ".manga-studio/continuity/references/daniel-tomas-shared-v001.json",
    "usage": "legacy_identity_evidence_only",
}

for reference in references + [legacy]:
    assert sha(ROOT / reference["webp_relative_path"]) == reference["webp_sha256"]
    assert sha(ROOT / reference["png_relative_path"]) == reference["png_sha256"]
    assert (ROOT / reference["reference_record_relative_path"]).is_file()

register = read_json(REGISTER)
register["updated_at"] = datetime.now(timezone.utc).isoformat()
register["summary"]["approved_reference_sets"] = 6
register["summary"]["approved_reference_files"] = 12
register["summary"]["fulfilled_character_reference_briefs"] = 5
register["summary"]["deferred_reference_generation_briefs"] = 8

authority = register["current_authority"]
authority["approved_visual_references"] = references + [legacy]
authority["primary_character_reference_ids"] = [row["reference_id"] for row in references]
authority["reference_generation_release_status"] = "characters_approved_environments_deferred_pending_storyboard_lock_image_enable_and_dependencies"

new_paths = [
    ".manga-studio/maintenance/character-reference-approval-v001/finalize.py",
    *[f".manga-studio/approvals/{name}" for name in [
        "approval-99458f572ec34943a25360319f766bc1.json",
        "approval-1b916d5ebf8e47ac9def0da59f41e643.json",
        "approval-313583c297e24ac4a74e5244449d1c2e.json",
        "approval-1f8c16463d6d4244aba621d623448ee0.json",
        "approval-c054db61edf1446a93d6003229bf9740.json",
        "approval-f070e865073e48c0aa9a21d5006a7eb5.json",
        "approval-c59175951b1b43f999102192d9658c8e.json",
        "approval-100a3235433746688446faed2cd02278.json",
        "approval-dd6be9cdee12493282b102ff0b8d5c6e.json",
        "approval-b47cf38aa10a4be19bef3eec1903d6aa.json",
    ]],
    *[row["reference_record_relative_path"] for row in references],
    *[row[key] for row in references for key in ("png_relative_path", "webp_relative_path")],
]

artifacts = {row["relative_path"]: row for row in register["artifacts"]}
for relative_path in new_paths:
    artifacts.setdefault(relative_path, {"relative_path": relative_path, "evidence": []})
for relative_path, row in artifacts.items():
    path = ROOT / relative_path
    assert path.is_file(), relative_path
    row["sha256"] = sha(path)
register["artifacts"] = [artifacts[key] for key in sorted(artifacts)]
write_json(REGISTER, register)

print(json.dumps({
    "status": "pass",
    "approved_character_references": [row["display_name"] for row in references],
    "stable_webp_paths": [row["webp_relative_path"] for row in references],
    "approved_reference_files": register["summary"]["approved_reference_files"],
    "storyboard_approved": False,
    "image_generation_enabled": False,
}, indent=2))
