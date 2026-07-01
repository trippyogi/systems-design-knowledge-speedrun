# Kata: Rate Limiter

## Prompt

Design a distributed rate limiter for public APIs.

## Requirements to clarify

- Per user, IP, API key, endpoint, tenant, or global?
- Hard limit or soft limit?
- Fixed window, sliding window, token bucket, or leaky bucket?
- Single region or multi-region?
- What happens when the limiter is unavailable?

## Expected concepts

- Token bucket
- Sliding window counters
- Redis or in-memory counters
- Approximate vs exact limits
- Hot key risk
- Fail open vs fail closed
- Latency budget
- Abuse prevention

## Stretch questions

- How do you handle clock skew?
- How do you shard counters?
- How do you support burst credits?
- How do you expose rate-limit headers?
