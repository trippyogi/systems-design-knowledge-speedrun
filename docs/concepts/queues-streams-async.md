# Queues, Streams, and Async Work

Async architecture removes slow or unreliable work from the request path.

## Queue vs stream

- **Queue**: work distribution; each message usually processed by one consumer.
- **Stream**: ordered event log; multiple consumers can independently read the same event history.

## Use a queue when

- Work can happen later
- You need retries
- You need to smooth traffic spikes
- Workers can scale independently
- The request path should be fast

## Use a stream when

- Multiple consumers need the same event
- Event history matters
- Ordering by key matters
- You need replay
- You are building data pipelines or event-sourced flows

## Design checklist

- Message schema
- Ordering guarantee
- Idempotency key
- Retry policy
- Dead-letter queue
- Visibility timeout or lease
- Backpressure behavior
- Poison message handling
- Consumer scaling
- Monitoring: lag, failure rate, processing latency

## Example: image upload

```mermaid
sequenceDiagram
  participant U as User
  participant API as Upload API
  participant OBJ as Object Storage
  participant Q as Queue
  participant W as Worker
  participant DB as Metadata DB

  U->>API: Upload image
  API->>OBJ: Store original
  API->>DB: Create image record: pending
  API->>Q: Enqueue process-image job
  API-->>U: 202 Accepted
  W->>Q: Consume job
  W->>OBJ: Read original, write thumbnails
  W->>DB: Mark ready
```

## Idempotency rule

Every retried operation should be safe to run more than once, or it should detect duplicates.

## Recall questions

<details><summary>What work should move off the request path?</summary>Slow, retryable, non-critical, fanout, analytics, notification, and enrichment work.</details>

<details><summary>What does a queue usually force you to handle?</summary>Retries, duplicate delivery, idempotency, backlog, poison messages, and observability.</details>

<details><summary>When is a stream better than a queue?</summary>When consumers need replayable ordered history or multiple independent consumers.</details>

<details><summary>Why do retries cause outages?</summary>They can amplify load on an already failing dependency unless bounded with backoff/jitter.</details>

<details><summary>What should every async design define?</summary>Delivery semantics, retry policy, DLQ behavior, idempotency key, ordering needs, and replay plan.</details>
