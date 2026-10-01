# Maintenance policy

Microsoft Copilot changes too quickly for a static skill to remain reliable without explicit freshness controls.

## Weekly review

Run after Microsoft's Tuesday Copilot Studio release-page update:

1. `python scripts/check_freshness.py --review`
2. `python scripts/check_sources.py`
3. Review Copilot Studio released versions.
4. Review What's new.
5. Review AI at Work Roadmap.
6. Review licensing/billing pages if their TTL is expired.
7. Update only changed facts.
8. Set the verified date on reviewed sources.
9. Add a regression scenario if a decision rule changed.

The canonical review ages are in `sources/freshness-policy.json`: 7 days for volatile categories, 30 days for governance, 180 days for stable architecture. The age expires at the threshold (`age >= max_age_days`), using UTC calendar dates. Future/invalid review dates fail. The scheduled `--review` mode also fails on warning-only stale categories so maintenance is requested; normal release mode blocks only critical categories.

A successful HTTP check verifies reachability only. Read the actual content before setting `last_verified`; record the claim, final URL and verification date in the audit. Answer-time live verification remains required for categories marked `live_check_required`, even immediately after repository review.

## Immediate review triggers

Do not wait for the weekly cycle after:
- a Microsoft pricing announcement;
- a Copilot Credits model change;
- a harness change;
- a new agent billing rule;
- Cowork entitlement/billing changes;
- a major tenant governance control change.

## Release discipline

Patch: source/date wording or non-behavioral maintenance.  
Minor: new product path, decision rule or playbook.  
Major: incompatible SKILL trigger/behavior or major architecture rewrite.

## Source philosophy

The repository stores:
- stable rules;
- verified snapshots;
- source pointers.

It does not attempt to mirror Microsoft Learn.
