# Failure Mode Table

| Component | Failure | Detection | User impact | Mitigation | Residual risk |
|---|---|---|---|---|---|
| API | Instance crash | Health check | Retry / brief failure | Load balancer removes instance | Increased latency |
| Cache | Outage | Error rate, cache connection alerts | Slower reads | Bypass cache, rate limit, protect DB | DB overload |
| DB primary | Unavailable | DB health + write errors | Writes fail | Failover, queue non-critical writes | Data loss if async not durable |
| Queue | Backlog | Consumer lag | Delayed processing | Scale workers, shed load | Stale results |
| Worker | Poison message | Retry count/DLQ | One job stuck | Dead-letter queue | Manual repair needed |
