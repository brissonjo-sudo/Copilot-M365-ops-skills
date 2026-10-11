# Playbook — choose the architecture

Use this six-line summary first:

1. **Need**: what outcome?
2. **Trigger**: manual / agent-called / scheduled / event / autonomous?
3. **Users**: licensed Microsoft 365 Copilot or not?
4. **Data/actions**: M365 only / external / premium?
5. **Reasoning**: deterministic or reasoning-heavy?
6. **Constraint**: cost / latency / governance / scale?

Then compare only viable options.

## Default preference order

For a licensed internal user:
1. native Microsoft 365 Copilot;
2. standard-harness internal agent;
3. agent-called deterministic flow;
4. scheduled/event workflow;
5. Cowork / GitHub Copilot harness for genuinely reasoning-heavy multistep work.

This is not a universal ranking. Change the order when the task requires capabilities unavailable at an earlier level.

## Required answer format

**Recommended architecture**  
One sentence.

**Why**  
Maximum three bullets.

**Cost path**  
Included / zero-rated / credits / other — with live verification status.

**DSI prerequisites**  
Maximum five bullets.

**Alternative**  
One cheaper or simpler fallback.
