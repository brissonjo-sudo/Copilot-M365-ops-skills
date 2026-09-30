# Product map

Use this file to identify the correct Microsoft surface before discussing implementation or cost.

| Surface | Primary role | Typical trigger | Cost model to verify |
|---|---|---|---|
| Microsoft 365 Copilot | User productivity across M365 apps | Human prompt | User subscription / included capabilities |
| Copilot Chat | Conversational Microsoft 365 entry point | Human prompt | License-dependent |
| Agent Builder / M365 agents | Lightweight internal agent experiences | Human prompt | License / metering depends on scenario |
| Copilot Studio — standard harness | Internal/external custom agents and agent flows | Human, flow, event | Copilot Credits, with documented zero-rating cases |
| Copilot Studio — GitHub Copilot harness | Reasoning-heavy multistep agents/workflows | Build, test, human, autonomous | Usage-based Copilot Credits |
| Cowork | Long-running / multistep work across tools and skills | User task / supported automation | Usage-based Copilot Credits |
| Power Automate | Deterministic workflow automation | Manual, scheduled, event | Power Platform licensing + connected-service costs |
| Microsoft Graph / Work IQ APIs | Programmatic enterprise data/intelligence | API call | Service/API-specific usage model |
| SharePoint agents | Grounded M365 knowledge experiences | Human prompt | License / metering depends on user and scenario |

## Rule

Do not select a product because it sounds more "agentic." Select it based on:
- need for reasoning;
- trigger;
- identity;
- data scope;
- action scope;
- expected volume;
- governance;
- cost.

For repetitive deterministic work, prefer a deterministic workflow before a reasoning-heavy autonomous agent.
