# Decision tree

## 1. Is the task conversational only?

If yes:
- use Microsoft 365 Copilot / Copilot Chat where possible;
- use a dedicated agent only when reusable instructions, tools, or scoped knowledge add value.

## 2. Does it need reusable domain behavior?

If yes:
- consider an internal agent;
- determine Copilot Chat, standard or GitHub Copilot harness from the actual authoring/runtime path;
- verify user licensing and publishing path.

## 3. Does it execute actions?

If yes:
- identify every connector/tool;
- determine whether human approval is required;
- apply least privilege and DLP;
- calculate action/flow billing separately from the response generation.

## 4. Is the trigger automatic?

If scheduled or event-driven:
- do not assume Microsoft 365 Copilot user licensing zero-rates the run;
- check the documented trigger-specific billing rules;
- compare with manual or agent-called execution.

## 5. Is the work reasoning-heavy and multistep?

If yes:
- consider Cowork or GitHub Copilot harness;
- model usage-based cost;
- set spending limits before scale.

## 6. Is it repetitive and deterministic?

Prefer:
1. agent-invoked deterministic flow when appropriate;
2. Power Automate / agent flow;
3. autonomous reasoning only when rules cannot reliably express the task.
