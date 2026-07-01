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
