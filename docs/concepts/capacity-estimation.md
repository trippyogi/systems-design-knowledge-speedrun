# Capacity Estimation

Capacity estimation is the bridge between product requirements and architecture.

## Core formulae

```text
QPS = requests per day / 86,400
Peak QPS ≈ average QPS × peak factor
Storage per day = writes per day × average object size
Bandwidth = QPS × average response size
Cache memory = hot objects × object size × overhead factor
```

## Estimation checklist

- Daily active users
- Requests per user per day
- Read/write ratio
- Peak-to-average multiplier
- Object size
- Retention period
- Replication factor
- Compression ratio
- Cache hit rate

## Example: URL shortener

Assumptions:

- 100 million redirects/day
- 1 million new URLs/day
- Redirect response metadata: 500 bytes
- Short link row: 1 KB
- 5-year retention

Rough sizing:

```text
Redirect QPS = 100,000,000 / 86,400 ≈ 1,157 average QPS
Peak redirect QPS ≈ 1,157 × 10 ≈ 11,570 QPS
New URL QPS = 1,000,000 / 86,400 ≈ 12 QPS
Storage/year = 1,000,000 × 1 KB × 365 ≈ 365 GB/year before replication/indexes
```

Design implication:

- Reads dominate writes.
- Cache redirects aggressively.
- Writes can go through a relational DB or strongly consistent key-value store.
- The short-code namespace must avoid collisions.

## Common mistakes

- Forgetting peak load
- Ignoring indexes and replication overhead
- Treating storage as the only bottleneck
- Not separating read path and write path
- Giving precise-looking numbers without assumptions

## Recall questions

<details><summary>How do you convert events/day into average QPS?</summary>Divide by 86,400, then apply a peak multiplier for bursty traffic.</details>

<details><summary>Why are rough numbers useful even when they are wrong?</summary>They reveal the likely first bottleneck and force architecture decisions to match scale.</details>

<details><summary>What usually dominates media-heavy systems?</summary>Storage, bandwidth, CDN behavior, and object lifecycle costs.</details>

<details><summary>What usually dominates feed/notification systems?</summary>Fanout and read/write amplification.</details>

<details><summary>What should a sizing table change?</summary>At least one design decision: cache size, partition count, queue capacity, storage choice, or SLO.</details>
