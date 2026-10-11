# v0.1.0 pilot preparation

**Status: validation incomplète — not published.**

Baseline: `main` commit `0612889b757b9a7e1016d0e268ab732d1dc1474c`, 2026-10-11. The original ChatGPT file-loaded campaign and GPT-6.1 Sol judgments remain historical evidence, not native-installation results.

## Native installation and respondent evaluation

The ChatGPT desktop app was discovered running. Its accessibility observation contained only a window and empty regions, without skill controls. Screenshot capture failed with `FrameArrived timed out: timed out waiting on channel`; after refreshing the app/window selection and activating the window, the recovery capture failed with `window capture timed out: timed out waiting on channel`.

After the user confirmed the desktop window was visible and not minimized, a new capture again returned `window capture timed out: timed out waiting on channel`. This is an automation/capture blocker, not proof that ChatGPT lacks native skills. No skill installation, selector visibility, activation, companion-file access, Business Premium smoke test or persistence check has been confirmed. Three native replays remain NOT RUN; there are no new respondent outputs to judge. GPT-6.1 Sol High remains the required independent judge once outputs exist.

The prepared native-test inputs and observed blocker are stored in `tests/evaluations/2026-10-11-native/manifest.json`. They contain no fabricated responses or verdicts. The skill instructions and runtime references have not been changed to mask the historical respondent omissions.

## Test procedure once native UI access is available

1. Install the extracted `copilot-m365-ops` folder using the supported desktop Skills workflow. Preserve companion directories; do not equate a filesystem copy or file upload with native activation.
2. In a fresh ChatGPT conversation, select the actual skill with `@`. Record selection, visible model/reasoning settings and confirmation that `SKILL.md` and `references/billing.md` can be read. Keep this loading check separate from each scenario response; never provide expected answers to the respondent.
3. Run the Business Premium smoke prompt from `INSTALL_CHATGPT.md`. Open another fresh conversation and confirm the skill is still selectable.
4. Replay `unlicensed-internal-user`, `cost-estimate` and `cheapest-architecture`, each in a fresh conversation with the original prompt and native skill selected. Preserve raw answers, dates, citations and activation evidence.
5. Give the captured answers and invariant rubric only to the independent GPT-6.1 Sol High judge. A safe clarification is valid when facts are missing; separate supplemented cases from originals.
6. Classify failures as skill defect, stale reference, model defect or ambiguous test. Fix only demonstrated skill/reference defects; replay affected cases, or all 17 if a decision rule changes.

## Packaging and release status

`python scripts/build_pilot.py --output-dir dist` creates a deterministic `copilot-m365-ops-0.1.0.zip`, a file-hash manifest and archive SHA256. The extracted archive is verified against every payload hash and the skill's companion paths. The package preserves instructions, license, runtime resources, tooling and evaluation records. It excludes Git state, environment files, caches and authoring plans.

The package is a reviewable pilot candidate, not a certified production release. Native activation and three replay verdicts remain release limitations. No tag, published release, plugin-directory submission or Microsoft deployment is created by this work.

## Maintenance verification

The registered `freshness` workflow has a manual trigger and a Wednesday `30 6 * * 3` schedule (UTC). Before this work, its GitHub workflow page displayed zero runs. Local regression tests cover stale critical/warning sources and the seven-day expiry boundary. HTTP tests distinguish 403 access denial, 404, 429, server errors and network errors; none updates verification dates. Issue-handler tests cover creation, pagination, exclusion of PRs and reuse without duplicate issues.

The proposed workflow reports freshness and HTTP access separately, links its exact run/commit, updates an existing maintenance issue and serializes concurrent reviews. Manual-run outcomes are recorded in the PR once executed; no scheduled run is certified merely from configuration.
