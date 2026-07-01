# SLO Template

## Service

Name:

Owner:

Critical user journeys:

- 

## SLI definitions

| SLI | Definition | Source |
|---|---|---|
| Availability | Successful requests / total valid requests | API metrics |
| Latency | p95 request latency | Tracing/APM |
| Correctness | Valid outputs / total outputs | Business events |

## SLO targets

| Journey | SLO | Window |
|---|---|---|
|  | 99.9% success | 30 days |

## Error budget

Allowed failures per window:

Policy when budget is burned:

- Freeze risky launches
- Prioritize reliability fixes
- Increase review level for deploys

## Alerts

Alert on symptoms, not every cause.

- High burn rate
- Sustained latency above threshold
- Error rate above threshold
- Queue lag above threshold
