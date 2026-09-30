# Licensing reference

**Volatility: HIGH. Live verification required for production decisions.**

## Concepts to keep separate

- Base Microsoft 365 plan (for example Business Premium, E3/E5, etc.).
- Microsoft 365 Copilot user license/add-on.
- Copilot Studio maker access.
- Copilot Studio tenant capacity / Copilot Credits.
- Power Platform / Power Automate entitlements.
- Usage-based billing policies and Azure linkage.
- Premium connectors and third-party service charges.

A user being able to open Copilot Studio does not, by itself, prove every publishing or runtime scenario is included.

## Current documented principles — verify before applying

Microsoft documentation states that a Microsoft 365 Copilot license allows users to extend Microsoft 365 Copilot with agents. For standard-harness employee-facing scenarios, specific capabilities used by an authenticated Microsoft 365 Copilot licensed user can be zero-rated, subject to Microsoft conditions and fair-use limits.

The same inclusion must not be generalized to:
- unlicensed users;
- external channels;
- autonomous/scheduled triggers;
- GitHub Copilot harness usage;
- Computer-Using Agents;
- unrelated Power Platform premium licensing.

## Fair use

Treat "fair use" as a contractual/product constraint, not as a known fixed request quota unless Microsoft publishes a current numeric limit for the exact feature.

When asked "how many prompts are included?", answer with the documented rule and verify whether a numeric limit exists today.
