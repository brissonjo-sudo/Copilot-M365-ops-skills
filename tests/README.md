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

Do not weaken billing/security invariants to increase pass rate.

## Live Microsoft tests

Live Copilot Studio / Cowork tests are **not required** for the 17 regression scenarios. Use them only when validating a Microsoft tenant capability, billing behavior, publishing path, or integration that cannot be established from official documentation alone.
