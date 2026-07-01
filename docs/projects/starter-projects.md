# Starter Projects

These projects turn systems design from talk into instinct.

## 1. Webhook delivery service

Core features:

- Register endpoint
- Publish event
- Queue delivery
- Retry with exponential backoff
- Dead-letter queue
- Per-customer rate limits
- Delivery log API
- HMAC signatures

Learning payoff:

- Queues
- Idempotency
- Backpressure
- Multi-tenant fairness
- Observability

## 2. Distributed-ish rate limiter

Core features:

- Token bucket
- Sliding window counter
- Redis-backed shared state
- Per-key limits
- Rate-limit headers
- Fail-open/fail-closed mode

Learning payoff:

- Hot keys
- Approximation
- Latency budgets
- Abuse prevention

## 3. Metrics ingestion toy platform

Core features:

- HTTP ingestion endpoint
- Batch writes
- Rollups
- Query API
- Cardinality guardrails
- Simple dashboard

Learning payoff:

- Write-heavy systems
- Time-series modeling
- Retention
- Cost controls

## 4. News feed simulator

Core features:

- Follow users
- Create posts
- Fanout-on-write worker
- Feed read cache
- Celebrity-user special path

Learning payoff:

- Fanout tradeoffs
- Cache invalidation
- Eventual consistency
- Hot keys
