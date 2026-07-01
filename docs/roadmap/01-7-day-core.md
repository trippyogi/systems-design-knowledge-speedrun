# 7-Day Core Sprint

Assumption: 90 to 120 focused minutes per day.

The daily loop is intentionally short:

> **Read one primitive → apply it to one kata → break it → write the tradeoff.**

By the end of the week you should have one polished design and several rough but useful artifacts.

## Day 1 — Requirements, APIs, and baseline diagram

Outcome: You can run the first 15 minutes of a systems design conversation without hand-waving.

Read:

- [Systems design playbook](../concepts/systems-design-playbook.md), sections 1, 3, and 4.
- C4 model overview: https://c4model.com/

Do:

1. Pick [URL shortener](../drills/url-shortener.md).
2. Write functional requirements, non-goals, and top non-functional requirements.
3. Sketch APIs: create short URL, redirect, analytics lookup.
4. Draw a baseline architecture with request path and async path separated.

Deliverable:

- `docs/drills/solutions/url-shortener.md` with requirements, API sketch, and baseline diagram.

## Day 2 — Capacity estimation and first bottleneck

Outcome: You can turn vague scale into architecture pressure.

Read:

- [Capacity estimation](../concepts/capacity-estimation.md).
- System Design Primer estimation section: https://github.com/donnemartin/system-design-primer#back-of-the-envelope-estimation
- Latency numbers: https://gist.github.com/jboner/2841832

Do:

1. Estimate redirects/sec, creates/sec, storage/year, bandwidth, and cache working set.
2. Name the first bottleneck at 10x scale.
3. Revise the URL shortener architecture using the numbers.

Deliverable:

- A sizing table and one paragraph: “The first thing that breaks is…”

## Day 3 — Data model, indexes, and consistency boundary

Outcome: You can choose storage from access patterns instead of vibes.

Read:

- [Data modeling](../concepts/data-modeling.md).
- PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
- DynamoDB NoSQL design guide: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html

Do:

1. Create an entity/access-pattern table for URL shortener.
2. Choose primary keys and indexes.
3. Decide what needs strong consistency: slug creation, redirect reads, analytics counters.

Deliverable:

- Entity table + access pattern table + consistency notes.

## Day 4 — Caching, CDN, and hot key behavior

Outcome: You can speed up the hot path and explain stale-data risk.

Read:

- [Caching](../concepts/caching.md).
- Redis cache-aside pattern: https://redis.io/learn/howtos/solutions/caching-architecture/cache-aside
- Cloudflare CDN explainer: https://www.cloudflare.com/learning/cdn/what-is-a-cdn/

Do:

1. Add cache-aside for slug redirects.
2. Define cache keys, TTL, negative caching, and invalidation behavior.
3. Handle celebrity/hot-link traffic and cache cold starts.
4. Write an ADR: cache-aside vs write-through.

Deliverable:

- `docs/adr/0001-cache-strategy.md`.

## Day 5 — Queues, retries, and idempotency

Outcome: You can remove slow work from the request path safely.

Read:

- [Queues and streams](../concepts/queues-streams-async.md).
- AWS Builders Library on retries/backoff: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- SQS visibility timeout: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html

Do:

1. Move analytics/event processing off the redirect path.
2. Add idempotency keys or dedupe logic.
3. Define retry, dead-letter queue, and replay behavior.

Deliverable:

- Sequence diagram: redirect request → event enqueue → analytics worker → aggregate update.

## Day 6 — Failure modes, abuse, and recovery

Outcome: You can explain what breaks, how users notice, and how operators recover.

Read:

- [Reliability and SRE](../concepts/reliability-sre.md).
- [Security, cost, and abuse](../concepts/security-cost-abuse.md).
- OWASP API Security Top 10: https://owasp.org/API-Security/editions/2023/en/0x11-t10/

Do:

1. Fill out a failure-mode table for database outage, cache outage, queue backlog, bad deploy, hot key, and bot abuse.
2. Add rate limits and abuse controls.
3. Define backup/restore and rollback expectations.

Deliverable:

- Failure mode table with detection, mitigation, and recovery.

## Day 7 — Review-ready design

Outcome: You can present and defend a complete design.

Read:

- [Design review rubric](../artifact-templates/design-review-rubric.md).
- Google SRE alerting on SLOs: https://sre.google/workbook/alerting-on-slos/
- OpenTelemetry overview: https://opentelemetry.io/docs/what-is-opentelemetry/

Do:

1. Turn the URL shortener artifacts into a polished one-page design.
2. Add SLOs, dashboard signals, and alerts.
3. Score the design with the rubric.
4. Write three gaps to study next.

Deliverable:

- One complete design doc + self-review.

## Minimum viable week

If time is tight, only produce these five artifacts:

1. Requirements + non-goals.
2. Sizing table.
3. Baseline diagram.
4. Failure mode table.
5. Tradeoff note or ADR.
