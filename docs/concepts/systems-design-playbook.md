# Systems Design Playbook

Use this as the default path through any systems design prompt.

## 1. Frame the system

Ask only questions that change the architecture.

- Who are the users or producers/consumers?
- What are the top 2-3 user flows?
- What is explicitly out of scope?
- What matters most: latency, availability, consistency, durability, privacy, cost, freshness, throughput?
- What is the expected scale now and at 10x?

Output: a short requirements list and non-goals.

## 2. Put numbers on the design

Do rough math before naming infrastructure.

Common estimates:

- Average and peak requests per second
- Read/write ratio
- Object size and storage growth per day/month/year
- Bandwidth in/out
- Cache working set size
- Fanout multiplier
- Queue depth during spikes
- Partition/shard count

Rules of thumb:

- Start with powers of ten; precision is less important than order of magnitude.
- Convert daily active behavior into QPS: `events/day / 86,400`, then apply peak multiplier.
- For feeds, notifications, and chat, fanout usually dominates naive request counts.
- For media systems, storage and bandwidth usually dominate database cost.

Output: a sizing table that justifies the first architecture.

## 3. Design APIs and access patterns

APIs reveal the real data model.

For each endpoint or message:

- Who calls it?
- Is it read-heavy or write-heavy?
- Does it need strong consistency?
- Can it be idempotent?
- What is the expected latency?
- What is the abuse pattern?

Output: API sketch + table of entities, queries, indexes, and consistency needs.

## 4. Draw baseline architecture

Start boring. Make the first version easy to explain.

Baseline pieces:

- Client/API gateway/load balancer
- Stateless app/service layer
- Primary datastore
- Cache if reads are hot or expensive
- Queue/stream for slow or retryable work
- Worker fleet
- Object storage/CDN for large static assets
- Observability: metrics, logs, traces, alerts

Output: one diagram with the synchronous request path and async path labeled separately.

## 5. Find bottlenecks

Pressure-test the design with targeted questions.

- What is the hottest key, query, endpoint, tenant, or region?
- What happens if read traffic grows 10x?
- What happens if write traffic grows 10x?
- What happens during a regional failover?
- Which dependency sets the latency floor?
- Which component is hardest to backfill or rebuild?
- Where can retries amplify the outage?

Output: bottleneck list and the scaling move for each one.

## 6. Name failure modes

Systems design gets serious when the happy path breaks.

Common failures:

- Cache unavailable or serving stale data
- Database primary unavailable
- Replica lag causing stale reads
- Queue backlog or poison messages
- Worker retries creating duplicate side effects
- Third-party dependency timing out
- Hot partition or celebrity user
- Partial writes across services
- Misconfigured deploy or bad migration
- Abuse spike or bot traffic

Output: failure mode table: trigger, user impact, detection, mitigation, recovery.

## 7. Defend tradeoffs

A design is a set of choices under constraints.

For every major choice, write:

- Decision
- Why this fits the requirements
- Main downside
- Alternative rejected
- What would make us revisit it

Output: 2-4 ADR-style bullets or a full ADR for big choices.

## The high-ROI systems design moves

| Move | Use when | Watch out for |
|---|---|---|
| Cache-aside | Read-heavy hot data | Stale data, invalidation, cold starts |
| CDN | Global static/media delivery | Purge complexity, auth/private content |
| Read replica | Relational reads exceed primary | Replica lag, read-after-write confusion |
| Sharding | Dataset/write load exceeds one node | Cross-shard queries, hot shards, resharding |
| Queue | Work can happen after response | Backlog, duplicates, ordering, poison messages |
| Stream | Need replayable event history | Consumer lag, schema evolution, ops overhead |
| Materialized view | Reads need precomputed shape | Rebuilds, staleness, dual-write bugs |
| Idempotency key | Clients/retries may duplicate writes | Key retention, semantic collisions |
| Rate limiter | Protect APIs or enforce quotas | Shared users/NAT, burst fairness, bypasses |
| Backpressure | Downstream is saturated | Dropping priority, user-visible degradation |
| Circuit breaker | Dependency is failing slowly | Recovery tuning, false opens |
| Outbox | DB write must reliably emit event | Relay lag, table growth |
| Saga | Multi-step workflow across services | Compensation logic, user confusion |

## One sentence test

For every concept, ask:

> What bottleneck, failure mode, or coordination problem does this solve, and what new cost does it introduce?
