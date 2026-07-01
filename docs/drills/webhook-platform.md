# Kata: Webhook Delivery Platform

## Prompt

Design a platform that delivers webhooks to customer endpoints.

## Requirements to clarify

- Delivery guarantees
- Retry schedule
- Customer rate limits
- Signature verification
- Event history retention
- Replay support
- Dead-letter behavior

## Expected concepts

- Queue-based delivery
- Per-customer ordering
- Idempotency
- Exponential backoff
- Dead-letter queues
- HMAC signatures
- Delivery logs
- Backpressure

## Stretch questions

- How do you prevent one bad customer endpoint from affecting others?
- How do you replay events safely?
- How do you handle a customer returning 200 but failing internally?
- What metrics matter most?
