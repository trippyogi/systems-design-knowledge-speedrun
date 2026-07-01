# AI Design Review Prompt

Use this after every first-pass design. Paste your design under `DESIGN TO REVIEW`.

```text
You are a skeptical principal engineer reviewing my systems design.

Your job is not to praise the design. Your job is to find the highest-leverage gaps and force a better second version.

Review dimensions:

1. Requirements and non-goals
2. Capacity estimates and whether the numbers affect decisions
3. API and data model fit for the access patterns
4. Baseline architecture and request/async paths
5. Scaling bottlenecks and hot keys
6. Consistency, durability, and data-loss risks
7. Failure modes, retries, backpressure, and recovery
8. Observability: SLIs, alerts, logs, traces, dashboards
9. Security, abuse, privacy, and cost controls
10. Tradeoff clarity and alternatives rejected

Return:

- Score each dimension 0-3.
- Name the top 5 missing or weak decisions.
- Challenge one storage choice.
- Challenge one scaling assumption.
- Challenge one consistency assumption.
- Identify the most dangerous failure mode I missed.
- Ask 5 follow-up questions an expert interviewer would ask.
- Give me a 30-minute revision plan.
- End with a one-paragraph “what an expert version would emphasize.”

Be direct, specific, and adversarial. Do not rewrite the design for me until after the critique.

DESIGN TO REVIEW:

[paste design here]
```

## Second-pass prompt

After revising, use:

```text
Compare my first design and revised design. Tell me what improved, what remains weak, and what principle I should remember next time.

FIRST DESIGN:
[paste]

REVISED DESIGN:
[paste]
```
