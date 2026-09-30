# Maintenance policy

Microsoft Copilot changes too quickly for a static skill to remain reliable without explicit freshness controls.

## Weekly review

Run after Microsoft's Tuesday Copilot Studio release-page update:

1. `python scripts/check_freshness.py`
2. `python scripts/check_sources.py`
3. Review Copilot Studio released versions.
4. Review What's new.
5. Review AI at Work Roadmap.
6. Review licensing/billing pages if their TTL is expired.
7. Update only changed facts.
8. Set the verified date on reviewed sources.
9. Add a regression scenario if a decision rule changed.

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
