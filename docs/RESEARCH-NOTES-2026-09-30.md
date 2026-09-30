# Research notes — 2026-09-30

Official Microsoft documentation reviewed for the initial architecture.

## High-impact findings

1. Copilot Studio billing must distinguish the **standard harness** from the **GitHub Copilot harness**.
2. For the standard harness, Microsoft documents qualifying zero-rated employee-facing usage for authenticated Microsoft 365 Copilot licensed users.
3. For agent flows, that zero-rating is trigger-specific: the documented inclusion applies to **When an agent calls the flow**; other triggers use the standard Copilot Credit rate.
4. Microsoft explicitly excludes Computer-Using Agent usage from the Microsoft 365 Copilot user-license inclusion described in the standard-harness billing table.
5. The GitHub Copilot harness uses usage-based Copilot Credits, including build/preview/evaluation activities.
6. Cowork is managed through usage-based Copilot Credits; `/cost` exposes approximate task and monthly credit use.
7. Copilot controls cover security/governance, management, and measurement/reporting.
8. Copilot Studio's released-versions page states it is updated weekly on Tuesday and rollout is regional.
9. The AI at Work Roadmap is forward-looking and its dates can change.

See `sources/sources.json` for the canonical URLs and verification dates.
