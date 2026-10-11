#!/usr/bin/env python3
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "sources" / "sources.json").read_text(encoding="utf-8"))

failures = []
for source in data["sources"]:
    req = urllib.request.Request(
        source["url"],
        headers={"User-Agent": "Copilot-M365-Ops-Skill-source-check/0.1"}
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            status = getattr(response, "status", 200)
            if status >= 400:
                failures.append(f"{source['id']}: HTTP {status}")
            else:
                print(f"OK {source['id']}: HTTP {status}")
    except (urllib.error.URLError, TimeoutError) as exc:
        failures.append(f"{source['id']}: {exc}")

for item in failures:
    print(f"FAIL: {item}")

sys.exit(1 if failures else 0)
