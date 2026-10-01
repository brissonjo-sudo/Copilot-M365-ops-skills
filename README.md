# Copilot M365 Ops Skill

A maintainable **ChatGPT skill specializing in Microsoft 365 Copilot**: Copilot Studio, Microsoft Copilot Cowork, agents, automation, licensing, Copilot Credits, governance, security and architecture decisions.

ChatGPT is the primary execution platform. Copilot Studio and Microsoft Copilot Cowork are products the skill advises on. Agent Skills format portability to other hosts is secondary and does not imply tested support.

Start with [INSTALL_CHATGPT.md](INSTALL_CHATGPT.md). Installation and native skill availability depend on the ChatGPT surface and workspace.

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

The canonical policy is [sources/freshness-policy.json](sources/freshness-policy.json). Review ages are 7 days for pricing, billing, licensing, quotas, availability and roadmap/releases; 30 days for governance; 180 days for stable architecture.

These are repository review ages, not permission to answer from cache. Categories marked `live_check_required` require a current official source check at answer time. If retrieval is unavailable, disclose the limitation and keep advice conditional.

A weekly GitHub Action runs Wednesday at 06:30 UTC after the documented Tuesday release-page update. It opens/updates a maintenance issue for stale sources, including warning categories, or unreachable URLs. HTTP reachability alone does not verify the content or refresh review dates.

## Local validation

```bash
python scripts/validate_repo.py
python scripts/check_freshness.py
python scripts/check_sources.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

## Current status

**v0.1.0 foundation**

The first version focuses on architecture, billing correctness, freshness and governance rather than copying Microsoft documentation.

## Important

This project is not affiliated with Microsoft. Licensing, pricing, availability and roadmap information must be checked against current official Microsoft sources before operational or purchasing decisions.

## License

MIT. See [LICENSE](LICENSE).
