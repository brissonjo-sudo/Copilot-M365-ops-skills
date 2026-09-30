# Copilot M365 Ops Skill

A maintainable Agent Skill for **Microsoft 365 Copilot, Copilot Studio, Cowork, agents, automation, licensing, Copilot Credits, governance, security and architecture decisions**.

## What problem this solves

Microsoft's Copilot stack changes rapidly. Static advice becomes unreliable when pricing, licensing, agent harnesses, billing rules, previews or governance controls change.

This repository therefore separates:

- **stable decision logic** from
- **volatile Microsoft facts** that require freshness checks.

## Core capabilities

- choose between Microsoft 365 Copilot, Copilot Studio, Cowork, flows and related surfaces;
- distinguish standard-harness and GitHub Copilot harness billing;
- identify when Microsoft 365 Copilot licensed-user usage can be zero-rated;
- identify scheduled/autonomous scenarios that can consume Copilot Credits;
- estimate cost without false precision;
- prepare DSI/admin requests;
- apply public-sector/enterprise governance checks;
- force live verification for volatile facts.

## Repository structure

```
SKILL.md                         canonical agent instructions
metadata.json                   catalog metadata
references/                     focused product/billing/governance knowledge
playbooks/                      reusable decision procedures
examples/                       worked use cases
sources/                        official source registry + freshness policy
tests/                          decision regression scenarios
scripts/                        validation and freshness tooling
docs/                           maintenance, research notes and roadmap
.github/workflows/              CI and scheduled freshness checks
```

## Freshness model

Critical facts have short TTLs:

- pricing: 1 day;
- billing rates: 1 day;
- licensing: 7 days;
- Cowork/harness billing: 7 days;
- roadmap/releases: 7 days;
- governance: 30 days.

A weekly GitHub Action runs after Microsoft's Tuesday Copilot Studio release-page update window and opens/updates an issue when review is required.

## Local validation

```bash
python scripts/validate_repo.py
python scripts/check_freshness.py
python scripts/check_sources.py
```

## Current status

**v0.1.0 foundation**

The first version focuses on architecture, billing correctness, freshness and governance rather than copying Microsoft documentation.

## Important

This project is not affiliated with Microsoft. Licensing, pricing, availability and roadmap information must be checked against current official Microsoft sources before operational or purchasing decisions.

## License

MIT. See [LICENSE](LICENSE).
