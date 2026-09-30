# Tests

The baseline suite is decision-oriented rather than model-specific.

`scenarios.json` captures the invariants the skill must preserve when models or Microsoft licensing rules change.

## CI

CI validates schema and repository consistency only. It does **not** call an LLM.

## Release evaluation

Before a significant release:
1. run the scenario prompts through at least one target assistant;
2. use a stronger judge model to evaluate factual correctness, source freshness, cost classification and governance;
3. record failures;
4. change the skill only when the failure indicates an instruction/reference problem rather than a model-only failure.

Do not weaken billing/security invariants to increase pass rate.
