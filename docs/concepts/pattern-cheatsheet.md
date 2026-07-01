# Pattern Cheatsheet

## Scale patterns

| Pattern | When to use | Main tradeoff |
|---|---|---|
| Cache-aside | Read-heavy hot data | Staleness/invalidation |
| CDN | Static or cacheable global content | Purge complexity |
| Read replicas | Read-heavy relational workloads | Replica lag |
| Sharding | Dataset or write load exceeds one node | Cross-shard queries |
| Queue | Slow work can be async | Eventual consistency |
| Stream | Replayable event history | Operational complexity |
| Materialized view | Fast reads from derived data | Staleness and rebuilds |
| Rate limiter | Protect APIs and enforce quotas | Legit traffic can be throttled |
| Saga | Distributed transaction across services | Compensation complexity |

## Reliability patterns

| Pattern | When to use | Main tradeoff |
|---|---|---|
| Timeout | Every remote call | Choosing good thresholds |
| Retry with backoff | Transient failures | Retry storms |
| Circuit breaker | Failing dependency | Recovery tuning |
| Bulkhead | Shared dependencies | Capacity fragmentation |
| Health check | Load balancer routing | False positives/negatives |
| Blue/green deploy | Safer releases | Extra infrastructure |
| Canary deploy | Detect regressions early | Slower rollout |
| Dead-letter queue | Poison messages | Requires human/automated repair |

## Data patterns

| Pattern | When to use | Main tradeoff |
|---|---|---|
| Outbox | Reliable event publishing with DB writes | Extra table/process |
| CQRS | Separate write/read models | More moving parts |
| Event sourcing | Need full event history | Complex projections |
| Leader-follower replication | Read scale + redundancy | Lag/failover |
| Consistent hashing | Dynamic shard membership | Hot keys still possible |
