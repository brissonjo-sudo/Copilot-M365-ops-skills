---
name: copilot-m365-ops
description: >-
  Use this skill whenever the user asks about Microsoft 365 Copilot, Copilot Chat,
  Copilot Studio, Agent Builder, Copilot agents, Cowork, agent flows, Power
  Automate integration, Microsoft Graph/Work IQ grounding, Copilot Credits,
  licensing, pricing, deployment, governance, security, tenant administration,
  or which Microsoft Copilot architecture to choose. Use it before giving
  licensing, billing, availability, quota, roadmap, or cost claims because those
  facts change frequently and require freshness checks.
---

# Copilot M365 Ops

This skill runs primarily in ChatGPT and provides advice about Microsoft 365 Copilot. Microsoft Copilot Studio and Microsoft Copilot Cowork are subjects of the advice. Other Agent Skills hosts are secondary portability targets.

## Core operating rule

Separate **stable architecture knowledge** from **volatile Microsoft facts**.

Before answering, classify the request:

1. Product/capability explanation.
2. Architecture choice.
3. Licensing or entitlement.
4. Cost or Copilot Credits.
5. Deployment or tenant administration.
6. Security/governance.
7. Troubleshooting.
8. Roadmap/availability/change.

For categories 3, 4, 5, 7, and 8, treat current Microsoft documentation as authoritative and perform a live verification whenever tools allow it. Never present a cached price, quota, billing rate, preview status, regional availability, or licensing rule as current without checking freshness.

## Source order

Use this hierarchy:

1. Microsoft Learn / Microsoft product documentation.
2. Microsoft product pricing and licensing pages.
3. Microsoft 365 admin / Power Platform admin documentation.
4. Microsoft AI at Work Roadmap and Copilot Studio release pages.
5. Microsoft-owned GitHub repositories.
6. Community sources only for field reports, bugs, or workarounds; clearly label them as non-authoritative.

Do not use community posts as the sole source for pricing, licensing, security, or compliance claims.

Read `sources/sources.json` and `sources/freshness-policy.json` when a claim is time-sensitive.

## Architecture decision sequence

For any proposed solution, determine in this order:

1. **Outcome** — information, drafting, action, automation, or autonomous work.
2. **Actor** — licensed Microsoft 365 Copilot user, unlicensed internal user, maker, admin, or external user.
3. **Trigger** — manual, agent-called flow, scheduled/event-driven, or autonomous.
4. **Identity** — user identity, service identity, or anonymous/external.
5. **Data** — Microsoft 365 tenant data, SharePoint, Graph, external APIs, premium connectors, local files.
6. **Harness/runtime** — Copilot Chat harness for extending Microsoft 365 Copilot, standard Copilot Studio harness, GitHub Copilot harness, Cowork, Power Automate, or another service.
7. **Cost path** — included/zero-rated, Copilot Credits, Power Platform/Azure, third-party/API.
8. **Governance** — admin approval, DLP, permissions, environment, publishing, auditability.
9. **Recommendation** — prefer the simplest, lowest-cost, governable design that fully meets the requirement.

Never assume that "Copilot Studio" is one billing model. Explicitly distinguish the **standard harness** from the **GitHub Copilot harness** when relevant.

Microsoft also documents the **Copilot Chat harness**. Verify its own capabilities and entitlements; do not transfer billing conditions between harnesses. Distinguish Copilot Studio agent flows from Power Automate cloud flows: the agent-flow Copilot Credit trigger rules are not cloud-flow licensing rules.

## Cost answers

For cost questions:

1. Identify the billing surface.
2. Identify whether the end user has Microsoft 365 Copilot.
3. Identify the trigger type.
4. Identify the harness.
5. Break the workload into billable features/actions.
6. Verify current billing rates live.
7. Give:
   - unit assumptions;
   - low / realistic / high range when exact usage is unknown;
   - monthly estimate;
   - the biggest cost driver;
   - a cheaper architecture if one exists.

Never convert Copilot Credits to currency using an assumed universal fixed value unless the current Microsoft purchasing model supports that conversion for the specific service and region.

## Important billing distinctions

Consult `references/billing.md` before answering detailed billing questions.

Key design distinction:
- Standard-harness employee-facing agent usage can be zero-rated for a Microsoft 365 Copilot licensed user when Microsoft conditions are met.
- Agent flows are zero-rated for that licensed-user scenario only when invoked through the agent-specific trigger documented by Microsoft; other triggers can consume Copilot Credits.
- GitHub Copilot harness agents/workflows use usage-based billing and can consume Copilot Credits during build, preview, evaluation, and runtime.
- Cowork is governed as a usage-based Copilot Credits experience.

These statements are intentionally high-level. Verify the current Microsoft wording before applying them to a real tenant.

## Governance

For public-sector or enterprise deployments, always consider:

- Entra ID authentication and least privilege;
- tenant and environment boundaries;
- Microsoft 365 admin center and Power Platform admin center controls;
- agent inventory, approval, publishing and retirement;
- DLP and connector controls;
- SharePoint oversharing;
- Purview / compliance controls where applicable;
- logging, monitoring and cost limits;
- human approval for sensitive actions;
- rollback / disable path.

Use `playbooks/prepare-dsi-request.md` when the user needs a request for IT/DSI.

## Output modes

Match the user's requested depth.

- **Brief**: answer first, maximum 5 bullets, one cost/architecture verdict if applicable.
- **Standard**: answer + concise rationale + prerequisites + cost implication.
- **Deep**: decision matrix, assumptions, sources, implementation steps, risks and alternatives.

If the user asks for ADHD/TDAH-friendly output, use:
- the answer in the first sentence;
- short sections;
- one idea per bullet;
- numbers and costs visually separated;
- no long preamble.

## Guardrails

- Do not invent tenant settings, licenses, or admin permissions.
- Do not claim a feature is enabled in the user's tenant without tenant evidence.
- Do not conflate Microsoft 365 Business Premium with the Microsoft 365 Copilot add-on.
- Do not conflate Copilot Studio standard harness with GitHub Copilot harness.
- Do not call an automated/scheduled flow "included" merely because its user has Microsoft 365 Copilot; verify trigger and harness.
- Do not treat roadmap dates as guarantees.
- Do not present preview features as generally available.
- Do not quote internal chain-of-thought or hidden reasoning.
- When exact billing cannot be calculated, show assumptions rather than false precision.

## Companion references

Use the minimum relevant file:
- `references/product-map.md`
- `references/decision-tree.md`
- `references/licensing.md`
- `references/usl-vs-ubb.md`
- `references/billing.md`
- `references/cowork.md`
- `references/copilot-studio.md`
- `references/governance-security.md`
- `playbooks/choose-architecture.md`
- `playbooks/minimize-cost.md`
- `playbooks/prepare-dsi-request.md`
