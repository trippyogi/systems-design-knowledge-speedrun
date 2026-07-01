# Concrete Resource Map

This is the recommended order for diving in. Each resource is attached to a systems-design move and a drill so learning turns into an artifact.

## Day-zero setup

Read only after your first 25-minute rep:

- C4 model overview: https://c4model.com/
- Architecture Decision Records: https://adr.github.io/
- Google SRE workbook, alerting overview: https://sre.google/workbook/alerting-on-slos/

Do:

- Draw one C4 container diagram for the system you just attempted.
- Write one ADR for the biggest choice you made.
- Define one user-facing SLO.

## 1. Requirements and design conversation

Read/watch:

- Google Cloud Architecture Framework overview: https://cloud.google.com/architecture/framework
- AWS Well-Architected Framework: https://aws.amazon.com/architecture/well-architected/
- C4 model: https://c4model.com/

Apply to:

- [URL shortener kata](../drills/url-shortener.md)
- [One-page design template](../artifact-templates/one-page-design-template.md)

Deliverable:

- Requirements, non-goals, and a one-diagram baseline.

## 2. Capacity estimation

Read/watch:

- System Design Primer, back-of-the-envelope estimation: https://github.com/donnemartin/system-design-primer#back-of-the-envelope-estimation
- Latency numbers every programmer should know: https://gist.github.com/jboner/2841832
- AWS pricing pages for rough cost intuition: https://aws.amazon.com/pricing/

Apply to:

- URL shortener: redirects/sec, write/sec, storage/year, cache memory.
- News feed: reads/sec, post fanout, feed storage.
- Metrics ingestion: samples/sec, compression, retention.

Deliverable:

- A sizing table with 5-8 numbers and a note on what bottleneck appears first.

## 3. Data modeling and storage choices

Read/watch:

- Designing Data-Intensive Applications reference page: https://dataintensive.net/ — especially chapters 2, 3, and 4 for data models, storage, and encoding.
- PostgreSQL indexes documentation: https://www.postgresql.org/docs/current/indexes.html
- DynamoDB design guide: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html

Apply to:

- [News feed kata](../drills/news-feed.md)
- [Chat kata](../drills/chat.md)

Deliverable:

- Entity table, access pattern table, index/partition key choices, and consistency notes.

## 4. Caching, CDN, and hot paths

Read/watch:

- AWS caching overview: https://aws.amazon.com/caching/
- Cloudflare CDN learning center: https://www.cloudflare.com/learning/cdn/what-is-a-cdn/
- Redis cache patterns: https://redis.io/learn/howtos/solutions/caching-architecture/cache-aside

Apply to:

- URL shortener redirects.
- News feed timelines.
- Media metadata and image delivery.

Deliverable:

- Cache key design, TTL/invalidation plan, cold-start behavior, stale-read risk.

## 5. Queues, streams, and async work

Read/watch:

- Enterprise Integration Patterns, message queue: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html
- Kafka design docs: https://kafka.apache.org/documentation/#design
- AWS SQS visibility timeout: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html

Apply to:

- [Webhook platform kata](../drills/webhook-platform.md)
- Image/video processing pipeline.
- Notification fanout.

Deliverable:

- Sequence diagram with retries, idempotency, dead-letter queue, and replay/backfill plan.

## 6. Consistency, replication, and coordination

Read/watch:

- Designing Data-Intensive Applications: chapters 5 and 9 for replication, consistency, and consensus.
- MIT 6.5840 Distributed Systems schedule: https://pdos.csail.mit.edu/6.824/schedule.html
- Martin Kleppmann, transactions/consistency talks: https://martin.kleppmann.com/talks.html
- Jepsen analyses for failure intuition: https://jepsen.io/analyses

Apply to:

- Inventory reservation.
- Collaborative document editing.
- Chat message ordering.

Deliverable:

- Table of operations that require strong consistency vs eventual consistency, plus the user-visible compromise.

## 7. Reliability, observability, and incident thinking

Read/watch:

- Google SRE book: https://sre.google/sre-book/table-of-contents/
- Google SRE workbook: https://sre.google/workbook/table-of-contents/
- OpenTelemetry overview: https://opentelemetry.io/docs/what-is-opentelemetry/
- AWS Builders Library: timeouts, retries, and backoff: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- AWS Builders Library index: https://aws.amazon.com/builders-library/

Apply to:

- Any completed kata.

Deliverable:

- SLO, dashboard signals, alert conditions, failure mode table, and postmortem stub.

## 8. Security, abuse, and cost controls

Read/watch:

- OWASP API Security Top 10: https://owasp.org/API-Security/editions/2023/en/0x11-t10/
- Google Cloud rate limiting strategies: https://cloud.google.com/architecture/rate-limiting-strategies-techniques
- AWS multi-tenant SaaS whitepapers and guidance: https://aws.amazon.com/solutions/guidance/saas/

Apply to:

- [Rate limiter kata](../drills/rate-limiter.md)
- Multi-tenant SaaS API.
- Public webhook platform.

Deliverable:

- Abuse cases, quota model, tenant isolation plan, audit logging, and cost guardrails.

## Drill → reality diff

After solving a drill, compare your design with one real-world article or case study:

| Drill | Reality diff target |
|---|---|
| URL shortener | Compare your cache/redirect path against CDN and edge-caching docs from Cloudflare or AWS. |
| Rate limiter | Compare against Cloudflare/AWS/API-gateway rate limiting writeups and note fairness vs latency tradeoffs. |
| News feed | Compare against public Instagram/Twitter/Meta feed architecture writeups or High Scalability case studies. |
| Chat | Compare against Discord/Slack/WebSocket scaling posts and message ordering discussions. |
| Webhook platform | Compare against Stripe/GitHub webhook docs: retries, signatures, idempotency, replay. |
| Metrics ingestion | Compare against Prometheus/OpenTelemetry/Kafka ingestion architectures. |

The artifact is a delta note:

- What did your design miss?
- What did the real system optimize for that you ignored?
- What did the real system accept as a tradeoff?
- What will you change in the second pass?

## Interview lane

Use these only if your goal is interview performance:

- Alex Xu, System Design Interview Vol. 1: https://bytebytego.com/
- Hello Interview system design writeups: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction

Treat interview resources as prompt practice, not as a substitute for building and breaking systems.

## How to use resources without getting stuck

For each topic, cap passive reading at 30 minutes, then produce one artifact:

1. One diagram.
2. One sizing table.
3. One tradeoff note.
4. One failure mode table.
5. One ADR.

If a resource does not change a design decision, move on.
