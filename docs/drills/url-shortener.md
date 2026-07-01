# Kata: URL Shortener

## Prompt

Design a URL shortener like bit.ly.

## Requirements to clarify

- Create short links
- Redirect short links
- Optional custom aliases
- Expiration
- Analytics?
- Authenticated or anonymous users?
- Abuse controls?

## Scale assumptions

Start with:

- 100 million redirects/day
- 1 million new links/day
- 10x peak multiplier
- 5-year retention

## Expected concepts

- Read-heavy traffic
- Short-code generation
- Collision avoidance
- Cache-aside
- CDN/edge redirect discussion
- Relational or key-value storage
- Analytics async path
- Abuse/rate limits

## Stretch questions

- How do you prevent malicious links?
- How do you handle hot short links?
- How do you support custom aliases without races?
- How would multi-region redirects work?
- What can be eventually consistent?
