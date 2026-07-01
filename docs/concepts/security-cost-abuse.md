# Security, Cost, and Abuse

A design that scales but leaks data or bankrupts the business is not a good design.

## Security checklist

- Authentication: who are you?
- Authorization: what can you do?
- Tenant isolation
- Encryption in transit
- Encryption at rest
- Secrets management
- Audit logs
- Rate limits and abuse controls
- Data retention and deletion
- Least privilege for services

## Abuse checklist

- Signup spam
- Credential stuffing
- API scraping
- Payment fraud
- Bot traffic
- Hotlinking assets
- Notification spam
- Resource exhaustion attacks

## Cost checklist

- Request volume
- Data transfer / egress
- Storage growth
- Replication factor
- Index/storage amplification
- Cache memory
- Queue retention
- Logging/cardinality explosion
- Multi-region overhead
- Idle overprovisioning

## Design phrase

> I would add guardrails before optimizing: authentication, authorization, tenant isolation, rate limits, audit logs, and cost visibility.

## Recall questions

<details><summary>Why is abuse a systems design concern?</summary>Abuse changes traffic shape, cost, capacity needs, and failure modes.</details>

<details><summary>What is the difference between authentication and authorization?</summary>Authentication proves identity; authorization decides what that identity can do.</details>

<details><summary>What should every public API define?</summary>Rate limits, quotas, auth model, audit logs, abuse signals, and data retention.</details>

<details><summary>What is a noisy neighbor?</summary>A tenant or user whose load harms others sharing the same infrastructure.</details>

<details><summary>What is a cost guardrail?</summary>A limit, alert, quota, or degradation rule that prevents runaway spend.</details>
