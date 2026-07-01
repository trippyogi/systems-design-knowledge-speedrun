# Kata: Metrics Ingestion

## Prompt

Design a metrics ingestion and query platform.

## Requirements to clarify

- Ingestion QPS
- Metric cardinality
- Query patterns
- Retention
- Rollups
- Alerting latency
- Tenant isolation

## Expected concepts

- Write-heavy ingestion
- Batching
- Time partitioning
- Compression
- Cardinality control
- Hot tenants
- Rollups
- Query acceleration

## Stretch questions

- How do you prevent high-cardinality labels from exploding cost?
- How do you backfill late data?
- How do you isolate noisy tenants?
- How do you query long retention windows cheaply?
