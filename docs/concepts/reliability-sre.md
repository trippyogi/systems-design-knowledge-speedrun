# Reliability and SRE Basics

Reliability is about whether the system does what users expect, not just whether servers are up.

## Core ideas

- **SLO**: target level of service, such as 99.9% successful checkout requests under 300 ms.
- **SLI**: measurement of service behavior, such as success rate or latency percentile.
- **Error budget**: allowed unreliability over a time window.
- **Toil**: manual repetitive operational work that should be reduced.

## Failure design checklist

- What dependencies can fail?
- What happens when a dependency is slow?
- What happens when the cache is empty or down?
- What happens when the queue backs up?
- What happens during deploy rollback?
- What happens during regional outage?
- What user-facing behavior is acceptable during degraded mode?

## Resilience patterns

| Pattern | Solves | Risk |
|---|---|---|
| Timeout | Prevents infinite waits | Too aggressive causes false failures |
| Retry | Handles transient failures | Can amplify load |
| Circuit breaker | Stops repeated failing calls | Can block recovery if misconfigured |
| Bulkhead | Isolates failures | More capacity planning |
| Graceful degradation | Preserves core UX | Requires product decisions |
| Rate limit | Protects system | Can reject legitimate traffic |

## Observability minimum

- Golden path success rate
- p50/p95/p99 latency
- Error rate by dependency
- Saturation: CPU, memory, queue depth, connection pools
- Business metrics: checkout completed, messages delivered, uploads processed
- Traces for cross-service requests
- Structured logs with request IDs

## Recall questions

<details><summary>What is an SLI?</summary>A measured signal of user experience, such as success rate or latency.</details>

<details><summary>What is an SLO?</summary>A target for an SLI over a time window, used to guide reliability decisions.</details>

<details><summary>Why are timeouts mandatory?</summary>Without timeouts, slow dependencies can exhaust threads, queues, and connection pools.</details>

<details><summary>What should a failure-mode table include?</summary>Trigger, user impact, detection, mitigation, recovery, and owner.</details>

<details><summary>What is graceful degradation?</summary>Preserving the most important user flows while reducing optional or expensive functionality.</details>
