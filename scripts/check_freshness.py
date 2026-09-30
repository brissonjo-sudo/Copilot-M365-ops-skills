#!/usr/bin/env python3
import json
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sources = json.loads((ROOT / "sources" / "sources.json").read_text(encoding="utf-8"))
policy = json.loads((ROOT / "sources" / "freshness-policy.json").read_text(encoding="utf-8"))["policy"]

today = date.today()
blocked = []
warnings = []

for source in sources["sources"]:
    category = source["category"]
    rule = policy.get(category)
    if not rule:
        warnings.append(f"{source['id']}: no freshness policy for category {category}")
        continue
    verified = datetime.strptime(source["last_verified"], "%Y-%m-%d").date()
    age = (today - verified).days
    if age >= rule["max_age_days"]:
        msg = f"{source['id']} ({category}) is {age}d old; max {rule['max_age_days']}d"
        if rule["severity"] == "block":
            blocked.append(msg)
        else:
            warnings.append(msg)

for item in warnings:
    print(f"WARNING: {item}")

for item in blocked:
    print(f"BLOCK: {item}")

print(f"Checked {len(sources['sources'])} sources: {len(blocked)} blocking, {len(warnings)} warnings.")
sys.exit(1 if blocked else 0)
