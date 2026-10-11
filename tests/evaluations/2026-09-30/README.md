# Captured release evaluation — 2026-09-30

**Release gate: NOT SATISFIED. Keep PR #1 draft. No merge performed.**

All 17 original scenarios were executed in separate ChatGPT conversations with the complete final skill corpus explicitly loaded. GPT-6.1 Sol (High) independently judged their contents and checked Microsoft sources. Initial campaign: **13 PASS, 3 PARTIAL, 1 FAIL**. Three unchanged-prompt replays and one workload clarification are preserved separately; no original response was overwritten.

## Evidence

- `manifest.json`: exact original prompts, responder settings, corpus hash, loading and evaluation limitations.
- `corpus.txt`: the 15-file evaluated corpus, UTF-8/LF SHA256 `ef89cfef6e9edc05ae31dcd66250aa2be3df425e3789123455b94df77b1f3a8c`.
- `{scenario-id}.json`: raw completed ChatGPT response and its conversation identifier.
- `*-replay-1.json`: original prompt, unchanged corpus, fresh context, no failing-invariant hint.
- `scheduled-mail-briefing-supplemental.json`: explicit workload, exact additional prompt and raw result; does not replace the original.
- `sources-observed.json`: Microsoft citation links observed in response DOM. Queries were removed to exclude tracking/session parameters; grouped citations can contain additional hidden links.
- `judgment.json`: independent GPT-6.1 Sol verdicts, invariant evidence, source verification and residual gates.

## Residual quality findings

| Case | Initial result | Subsequent observation | Attribution |
|---|---|---|---|
| Scheduled briefing | PARTIAL | Explicit-workload complement computes 5.72 flow + 41.25 AI = 46.97 credits/month; exclusions and manual alternative stated | Ambiguous quantitative test input, not a demonstrated skill defect |
| Unlicensed Teams user | PARTIAL | Replay still assumes/proposes standard harness without verifying the existing agent's exact harness | Responder omission |
| Monthly cost | FAIL | Arbitrary 30–50 EUR budget removed; replay ties numbers to hypotheses but still presents an incomplete component model as a budgeting recommendation | Responder defect; billing scope remains incomplete |
| Cheapest deterministic architecture | PARTIAL | Replay still omits governance prerequisites | Responder omission |

The roadmap prompt names no feature. Its safe request for an exact feature and warning that rollout dates are not guarantees passes the clarification behavior only; no concrete France availability is certified.

No additional skill/instruction defect or stale-reference defect was demonstrated by the evaluated responses. The independently found missing Copilot Chat harness and cloud-flow distinction were corrected before this corpus was evaluated. Do not weaken billing or governance invariants, or change correct instructions solely to make these model responses pass.

## Limits and next release gate

The ChatGPT UI exposed the setting `Moyen 2/5`, not an exact responder model identifier. Explicit file loading was exercised; native ChatGPT installation/activation was not. No Microsoft tenant, invoice or deployment was tested because these scenarios concern documented decisions. The initial 17-in-one-context batch is excluded as a pretest. Visible citations establish response-source provenance; independent factual checks are recorded separately and do not prove every hidden retrieval operation.

Before declaring merge-ready, resolve or independently validate the remaining harness, complete-cost and governance behaviors without changing sound billing/security rules. Review the independent final verdict and all applicable repository/remote CI gates on the exact published head. Successful CI alone does not close this behavioral gate.
