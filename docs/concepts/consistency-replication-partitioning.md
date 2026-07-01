# Consistency, Replication, and Partitioning

Distributed systems force tradeoffs between correctness, availability, latency, and operational complexity.

## Consistency questions

Ask per operation, not for the whole system:

- What happens if a user reads immediately after writing?
- Can two users update the same object at once?
- Is stale data acceptable?
- Is duplicate processing acceptable?
- Is lost update acceptable?
- Can we repair inconsistency later?

## Common models

- **Strong consistency**: reads reflect latest committed writes.
- **Eventual consistency**: replicas converge if no new writes occur.
- **Read-your-writes**: a user sees their own updates.
- **Monotonic reads**: once a user sees a value, they do not later see older values.

## Replication tradeoffs

| Choice | Benefit | Cost |
|---|---|---|
| Leader-follower | Simpler writes | Read replica lag, leader failover |
| Multi-leader | Regional writes | Conflicts |
| Leaderless/quorum | Availability and tunable consistency | Complex reads/writes, repair |

## Partitioning/sharding tradeoffs

| Key choice | Benefit | Risk |
|---|---|---|
| User ID | Simple ownership | Hot celebrity users |
| Random/hash | Even distribution | Hard range queries |
| Time | Great for time windows | Hot latest partition |
| Tenant ID | Isolation | Large tenants become hot |

## Failure-mode prompt

> What does the user see during replica lag, leader failover, network partition, and partial write failure?

## Recall questions

<details><summary>What is the practical question behind consistency?</summary>What stale or conflicting state can the user observe, and is that acceptable?</details>

<details><summary>Where do you usually need strong consistency?</summary>Money, inventory, permissions, uniqueness, irreversible actions, and safety-critical state.</details>

<details><summary>What does replication trade off?</summary>Availability/read scale against lag, failover complexity, and conflict handling.</details>

<details><summary>Why is global strong consistency expensive?</summary>It requires coordination across distance, which increases latency and failure coupling.</details>

<details><summary>What should you write for each operation?</summary>Consistency requirement, failure behavior, user-visible compromise, and recovery path.</details>
