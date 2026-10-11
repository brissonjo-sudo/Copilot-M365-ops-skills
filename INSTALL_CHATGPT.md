# Use in ChatGPT

This is a ChatGPT skill about Microsoft 365 Copilot. Microsoft Copilot Studio and Microsoft Copilot Cowork are the advice domain.

## Native skill route

Official OpenAI documentation describes standalone skills in the ChatGPT desktop app and plugin-bundled skills across Chat and Work. In a workspace with skill management, make the `copilot-m365-ops` folder available using the supported import/creation workflow. Preserve `SKILL.md`, `references/`, `playbooks/`, `examples/` and `sources/` together. Do not rename or flatten companion paths.

Select the skill with `@` and verify that ChatGPT can read `SKILL.md` and a companion reference. If the skill is absent from the selector, installation is not confirmed. Workspace policy and product availability may restrict this route; a repository clone is not proof of installation.

## Explicit file-loading route for evaluation

If native import is unavailable, attach the complete instruction/reference corpus as files in a fresh ChatGPT chat and explicitly ask ChatGPT to read and apply it. Record this as **explicitly loaded files**, not native installation or automatic skill activation. Ask for confirmation that the manifest and required references were read before submitting a scenario. An inaccessible attachment invalidates the run.

Use a fresh context per scenario (except explicitly defined follow-up pairs). Allow current official web retrieval. Never supply the expected outcomes to the responder.

## Verification

Try: `Use copilot-m365-ops. We have Business Premium: is all Copilot Studio usage included?`

The answer should establish the actual license, feature, harness and trigger, verify current Microsoft terms, and avoid assuming inclusion. Capture the selected model/settings, loading method, source checks, prompt, answer and date. This smoke check does not replace the [17-scenario campaign](tests/README.md).

This skill grants no Microsoft tenant access. Connected Microsoft tools require their own authorization. It does not install an agent into Copilot Studio or Cowork.

## Official installation reference

[Build skills — ChatGPT Learn](https://learn.chatgpt.com/docs/build-skills), checked 2026-09-30. Use current product documentation if the interface differs; do not invent a universal ZIP-import button.
