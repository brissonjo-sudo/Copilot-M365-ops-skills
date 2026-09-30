# Billing and Copilot Credits

**Volatility: CRITICAL. Live verification required.**

## Standard harness

As verified from Microsoft documentation on 2026-09-30, Copilot Studio publishes feature-level Copilot Credit rates for the standard harness. The same table identifies documented "No charge" cases for Microsoft 365 Copilot licensed users in qualifying employee-facing scenarios.

Important trigger distinction:
- for agent flows, the documented zero-rating for a Microsoft 365 Copilot licensed user applies to runs triggered through **When an agent calls the flow**;
- other agent-flow triggers consume Copilot Credits at the standard rate.

Microsoft also states that Computer-Using Agents are not included in that Microsoft 365 Copilot zero-rating.

Never copy cached numeric rates into an answer without a current source check.

## GitHub Copilot harness

Microsoft documents a separate usage-based billing model for agents and workflows powered by the GitHub Copilot harness.

Key difference:
- usage can consume Copilot Credits while building, previewing, testing, evaluating, and running;
- Microsoft 365 Copilot user licensing should not be assumed to zero-rate this harness.

## Cowork

Cowork is listed by Microsoft among services managed through usage-based Copilot Credits billing. Users can use `/cost` in Cowork to inspect approximate task credit usage and monthly remaining allocation.

## Purchasing

Microsoft supports multiple purchasing approaches depending on product and scenario, including prepaid capacity and pay-as-you-go. Public list prices can change and can differ by market/contract.

Always use the current Microsoft pricing or licensing page for monetary estimates.

## Cost calculation template

1. Count runs per day/month.
2. Identify harness.
3. Identify user license status.
4. Identify trigger.
5. Count billable feature types.
6. Estimate tokens/pages/actions only where relevant.
7. Apply current rates.
8. Add Power Platform/Azure/third-party costs separately.
9. Show low / expected / high range.
