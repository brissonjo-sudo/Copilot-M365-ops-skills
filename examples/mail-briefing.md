# Example — executive mail briefing

## Need

A director wants a daily briefing of the previous day's email activity, including unread messages and meaningful updates to existing topics.

## Option A — manual trigger

User opens a dedicated internal agent and selects "Generate my morning briefing".

Architecture:
- authenticated licensed user;
- standard-harness agent;
- Microsoft 365 data access;
- optional agent-called flow.

Cost principle:
- verify current zero-rating conditions for the licensed user;
- if a flow is used, verify that it is invoked using the documented agent-call trigger.

Use when:
- a single click each morning is acceptable;
- minimizing incremental consumption is important.

## Option B — scheduled automation

A scheduled/event trigger runs without the user starting it.

Cost principle:
- do not apply the manual licensed-user zero-rating automatically;
- model Copilot Credits / Power Automate costs using current rules.

Use when:
- briefing must be ready before the user opens Copilot.

## Option C — Cowork

Use only when the briefing requires genuinely multistep reasoning or cross-tool work that materially exceeds the agent/flow design.

Cost principle:
- usage-based Copilot Credits;
- validate with pilot telemetry and `/cost`.

## Pilot metric

For two weeks record:
- emails scanned;
- messages selected as material;
- elapsed time;
- user corrections;
- credits consumed;
- avoided manual time.
