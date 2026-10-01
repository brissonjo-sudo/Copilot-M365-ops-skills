#!/usr/bin/env python3
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sources = json.loads((ROOT / "sources" / "sources.json").read_text(encoding="utf-8"))
policy = json.loads((ROOT / "sources" / "freshness-policy.json").read_text(encoding="utf-8"))["policy"]

parser = argparse.ArgumentParser()
parser.add_argument('--review', action='store_true', help='Fail for warnings too, for scheduled maintenance')
args = parser.parse_args()
today = datetime.now(timezone.utc).date()
blocked = []
warnings = []

for source in sources["sources"]:
    category = source["category"]
    rule = policy.get(category)
    if not rule:
        blocked.append(f"{source['id']}: no freshness policy for category {category}")
        continue
    try:
        verified = datetime.strptime(source["last_verified"], "%Y-%m-%d").date()
    except (ValueError, KeyError, TypeError):
        blocked.append(f"{source.get('id')}: invalid verification date")
        continue
    age = (today - verified).days
    if age < 0:
        blocked.append(f"{source['id']}: verification date is in the future")
        continue
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
sys.exit(1 if blocked or (args.review and warnings) else 0)
