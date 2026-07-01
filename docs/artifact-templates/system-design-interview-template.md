# 45-Minute System Design Interview Template

## Minute 0-5 — Clarify requirements

Ask:

- Who are the users?
- What are the core use cases?
- What scale should we target?
- What matters most: latency, availability, consistency, cost, privacy?
- What is explicitly out of scope?

## Minute 5-10 — Estimates

Estimate:

- DAU/MAU
- Read/write QPS
- Peak QPS
- Storage/day and retention
- Bandwidth
- Hot path/cache size

## Minute 10-15 — API and data model

Sketch:

- 2 to 4 core endpoints
- Main entities
- Primary keys and indexes
- Access pattern table

## Minute 15-25 — Baseline design

Draw:

- Client
- Load balancer
- Stateless service
- Storage
- Cache
- Queue/worker if needed

Explain request flows.

## Minute 25-35 — Scale and failure modes

Discuss:

- Bottlenecks
- Caching
- Partitioning
- Replication
- Async processing
- Rate limiting
- Failover
- Data consistency

## Minute 35-42 — Production readiness

Cover:

- SLOs
- Observability
- Security
- Abuse
- Disaster recovery
- Cost

## Minute 42-45 — Tradeoff summary

End with:

- Final architecture
- Biggest tradeoff
- Alternative rejected
- Next steps if given more time
