#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "SKILL.md",
    "README.md",
    "VERSION",
    "metadata.json",
    "sources/sources.json",
    "sources/freshness-policy.json",
    "references/product-map.md",
    "references/billing.md",
    "references/licensing.md",
]
for item in required:
    if not (ROOT / item).exists():
        errors.append(f"Missing required file: {item}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n"):
    errors.append("SKILL.md must start with YAML frontmatter")
if not re.search(r"(?m)^name:\s*copilot-m365-ops\s*$", skill):
    errors.append("SKILL.md name must be copilot-m365-ops")
if not re.search(r"(?m)^description:\s*>-", skill):
    errors.append("SKILL.md must include an agent-facing description")

metadata = json.loads((ROOT / "metadata.json").read_text(encoding="utf-8"))
for key in ("name", "description", "platforms", "tags", "version"):
    if key not in metadata:
        errors.append(f"metadata.json missing {key}")

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
if metadata.get("version") != version:
    errors.append("VERSION and metadata.json version differ")

sources = json.loads((ROOT / "sources" / "sources.json").read_text(encoding="utf-8"))
policy = json.loads((ROOT / "sources" / "freshness-policy.json").read_text(encoding="utf-8"))["policy"]
ids = set()
for source in sources.get("sources", []):
    if source["id"] in ids:
        errors.append(f"Duplicate source id: {source['id']}")
    ids.add(source["id"])
    if source["category"] not in policy:
        errors.append(f"No policy for source category: {source['category']}")
    if not source["url"].startswith("https://"):
        errors.append(f"Non-HTTPS source: {source['id']}")

scenarios_path = ROOT / "tests" / "scenarios.json"
if scenarios_path.exists():
    scenarios = json.loads(scenarios_path.read_text(encoding="utf-8"))
    scenario_ids = set()
    for s in scenarios["scenarios"]:
        if s["id"] in scenario_ids:
            errors.append(f"Duplicate scenario id: {s['id']}")
        scenario_ids.add(s["id"])
        for key in ("prompt", "expected"):
            if key not in s:
                errors.append(f"Scenario {s.get('id')} missing {key}")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print("Repository validation passed.")
