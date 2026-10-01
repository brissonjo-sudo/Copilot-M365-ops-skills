# ChatGPT skill merge-ready implementation plan

**Goal:** Prepare PR #1 for merge without merging.
**Architecture:** ChatGPT executes the skill; Microsoft products are the advice domain. JSON defines review freshness; live checks establish volatile claims at answer time.
**Tech stack:** Markdown, JSON, Python standard library, GitHub Actions.
**Spec:** User request: ChatGPT orientation, freshness consistency, complete audit, 17 ChatGPT responses judged by GPT-6.1 Sol, targeted fixes/replays, final gates.

## Constraints
- No merge; leave draft until every gate passes.
- Preserve billing and security invariants; distinguish skill/source/model/test defects.
- Never claim native skill activation or an exact responder model without evidence.

## Review focus
- Offline answers must disclose unverifiable volatile facts.
- Agent flows and Power Automate cloud flows have separate billing.
- Future review dates must fail validation.
- Warning-only stale sources must trigger maintenance without blocking release.
- Every scenario must have a captured answer and an independent judge verdict.

## Tasks
- [ ] 1. Correct metadata, README, roadmap; add INSTALL_CHATGPT.md using official OpenAI documentation. Check platform declarations and links.
- [ ] 2. Audit all references/playbooks/examples against official Microsoft sources; record source redirects and verification evidence.
- [ ] 3. Reproduce freshness/maintenance defects, fix tooling, add meaningful regression checks and run local CI commands.
- [ ] 4. Load the full skill corpus into ChatGPT, capture 17 answers without supplying expected outcomes; have GPT-6.1 Sol judge each invariant and classify defects. Fix true skill/reference defects only and replay affected cases.
- [ ] 5. Publish changes to the existing PR branch, verify final commit CI/freshness/reviews/mergeability, update PR description. Mark ready only if all gates pass.

## Execution
User explicitly authorized planning and execution in this session; proceed without another plan approval. Plan completion is tracked in the release audit.
