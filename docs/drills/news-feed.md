# Kata: News Feed

## Prompt

Design a social media news feed.

## Requirements to clarify

- Home feed vs profile feed
- Follow graph size
- Celebrity accounts
- Ranking vs chronological feed
- Media support
- Freshness requirements
- Privacy/blocking rules

## Expected concepts

- Fanout-on-write
- Fanout-on-read
- Hybrid fanout for celebrities
- Feed cache
- Follow graph storage
- Ranking pipeline
- Eventual consistency
- Backpressure

## Stretch questions

- What happens when a celebrity posts?
- How do deletes propagate?
- How do privacy changes affect cached feeds?
- How do you rebuild feeds after a bug?
