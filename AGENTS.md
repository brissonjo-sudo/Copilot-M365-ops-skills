# Maintainer instructions

This repository contains a time-sensitive Microsoft Copilot Agent Skill.

## Non-negotiable rules

1. Do not update pricing, licensing, Copilot Credits rates, quotas, preview/GA status, or roadmap dates without an official Microsoft source.
2. Update `sources/sources.json` verification metadata whenever a volatile claim is reviewed.
3. Keep stable architecture guidance separate from volatile facts.
4. Run `python scripts/check_freshness.py` and `python scripts/validate_repo.py` before release.
5. Add or update a regression scenario when a Microsoft change alters a decision path.
6. Prefer one canonical statement over duplicated facts across many files.
7. Do not silently weaken security or cost guardrails to make a test pass.

## Release rule

A release is blocked if a critical source category is stale:
- pricing;
- billing rates;
- licensing;
- Cowork usage-based billing;
- Copilot Studio harness billing.

Roadmap staleness creates a warning, not a hard failure.
