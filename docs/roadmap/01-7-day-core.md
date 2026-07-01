# 7-Day Core Sprint

Assumption: 90 to 120 focused minutes per day.

## Day 1 — Learn the interview/system design loop

Outcome: You can run a design conversation from requirements to tradeoffs.

Do:

1. Read the one-page design template.
2. Draw a C4-style context and container diagram for a familiar app.
3. Complete the URL shortener kata.

Deliverable:

- `docs/drills/solutions/url-shortener.md`

## Day 2 — Sizing and bottlenecks

Outcome: You can estimate traffic, storage, and cache needs.

Do:

1. Read capacity estimation.
2. Estimate Twitter/X feed reads, image upload storage, and rate limiter memory.
3. Revise yesterday’s URL shortener using actual numbers.

Deliverable:

- A before/after design note with changed decisions.

## Day 3 — Data models and storage

Outcome: You can choose storage based on access patterns.

Do:

1. Read data modeling and indexing.
2. Design a notification system.
3. Identify primary entities, query patterns, and indexes.

Deliverable:

- Entity model + query table.

## Day 4 — Caching, CDN, and load balancing

Outcome: You know where caches help and where they hurt.

Do:

1. Read caching.
2. Add cache, CDN, and load balancer layers to URL shortener or feed.
3. Write one ADR: cache-aside vs write-through.

Deliverable:

- `docs/adr/0001-cache-strategy.md`

## Day 5 — Queues, streams, and async work

Outcome: You can remove slow work from the request path.

Do:

1. Read queues and streams.
2. Design image/video upload processing.
3. Add idempotency keys and retry behavior.

Deliverable:

- Sequence diagram of upload -> process -> notify.

## Day 6 — Consistency, replication, and failure modes

Outcome: You can reason about what breaks and how users notice.

Do:

1. Read consistency and replication.
2. Design a collaborative document or inventory reservation flow.
3. Decide what must be strongly consistent and what can be eventually consistent.

Deliverable:

- Failure mode table with mitigations.

## Day 7 — Reliability, observability, and review

Outcome: You can present a complete design.

Do:

1. Read SLOs and observability.
2. Pick one kata and write a polished one-page design.
3. Score it with the design review rubric.
4. Record three gaps to study next.

Deliverable:

- One complete design doc + self-review.
