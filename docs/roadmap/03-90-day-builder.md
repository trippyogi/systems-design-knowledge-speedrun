# 90-Day Builder Path

The 90-day path turns interview knowledge into engineering intuition.

## Month 1 — Design fluency

Build a design portfolio:

- 8 design docs
- 8 C4 container diagrams
- 8 failure-mode tables
- 4 ADRs

Recommended systems:

- URL shortener
- Rate limiter
- Notification service
- News feed
- Chat
- File storage
- Search autocomplete
- Metrics ingestion

## Month 2 — Build small production-like systems

Build 2 or 3 small services with real operational concerns.

Suggested projects:

1. **Webhook delivery service**
   - Idempotency keys
   - Retries with exponential backoff
   - Dead-letter queue
   - Per-customer rate limits
   - Delivery logs

2. **Metrics ingestion pipeline**
   - Write-heavy ingestion endpoint
   - Batch worker
   - Time-series rollups
   - Dashboard query API
   - Load test

3. **Collaborative notes toy app**
   - Real-time editing or sync
   - Conflict handling
   - Offline writes
   - Version history

## Month 3 — Operate and review

Add production muscles:

- SLOs and alerts
- Dashboards
- Tracing
- Load testing
- Chaos/failure tests
- Runbooks
- Postmortems
- Cost estimates
- Security review

## Final portfolio package

Create a public portfolio folder with:

- Architecture diagrams
- Design docs
- ADRs
- Load test results
- Postmortems
- Screenshots or demo videos
- A short README explaining tradeoffs
