# Tests

The baseline suite is decision-oriented rather than model-specific.

`scenarios.json` captures the invariants the skill must preserve when models or Microsoft licensing rules change.

## CI

CI validates schema and repository consistency only. It does **not** call an LLM.

## Release evaluation

Before a significant release:

1. Run the 17 scenario prompts in **ChatGPT with the skill loaded**.
2. Use the target ChatGPT model as the responder for the main campaign.
3. Use **GPT-6.1 Sol** as the judge.
4. Evaluate at minimum:
   - factual correctness;
   - source freshness;
   - architecture choice;
   - billing/licensing classification;
   - governance/security;
   - absence of false precision;
   - adherence to requested concise/TDAH-friendly formatting when applicable.
5. Record failures and classify them:
   - skill/instruction defect;
   - stale reference/source defect;
   - responder-model defect;
   - ambiguous test case.
6. Change the skill only when the failure indicates an instruction/reference problem rather than a responder-model-only failure.

Use a fresh conversation and the complete corpus for each scenario; never supply the expected invariants to the responder. The scheduled briefing scenario carries only the licensed-director context from scenario 1. Record the exact prompt, corpus hash, responder settings, raw response, visible citation URLs, independent verdict and every replay. A replay does not erase an original failure.

Some prompts intentionally omit information: the roadmap case needs a feature identifier, and cost cases need architecture and workload assumptions. A safe clarification is valid; do not require a fabricated date or price. Record untested invariants separately and use a clearly labelled supplemental prompt to resolve missing inputs before certifying the release.

The captured [2026-09-30 campaign](evaluations/2026-09-30/README.md) is a real ChatGPT file-loaded evaluation, not an LLM run in CI or a native-installation test. Its unresolved responder omissions keep the release gate open.

Do not weaken billing/security invariants to increase pass rate.

## Live Microsoft tests

Live Copilot Studio / Cowork tests are **not required** for the 17 regression scenarios. Use them only when validating a Microsoft tenant capability, billing behavior, publishing path, or integration that cannot be established from official documentation alone.
