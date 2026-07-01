# API Design for Systems Design

APIs make requirements concrete.

## Minimum API sketch

For each endpoint:

- Method and path
- Request body
- Response body
- Auth requirements
- Idempotency behavior
- Rate limits
- Error cases
- Pagination/filtering

## Example: create short URL

```http
POST /v1/links
Authorization: Bearer <token>
Idempotency-Key: <uuid>
Content-Type: application/json

{
  "long_url": "https://example.com/a/very/long/path",
  "custom_alias": null,
  "expires_at": null
}
```

Response:

```json
{
  "id": "lnk_123",
  "short_code": "aB91xZ",
  "short_url": "https://sho.rt/aB91xZ",
  "created_at": "2026-07-01T00:00:00Z"
}
```

## Pagination rules

Prefer cursor pagination for large changing datasets.

```http
GET /v1/events?limit=50&cursor=eyJpZCI6...
```

Avoid offset pagination for massive or frequently changing lists.

## Idempotency rules

Use idempotency keys for operations where retries could create duplicates:

- Payments
- Orders
- Reservations
- Messages
- Webhook deliveries
- File uploads

## Recall questions

<details><summary>Why should APIs be idempotent where possible?</summary>Retries and duplicate client requests should not create duplicate side effects.</details>

<details><summary>What belongs in an API sketch?</summary>Endpoint/message, caller, request/response shape, errors, latency target, auth, and idempotency behavior.</details>

<details><summary>When should work be async?</summary>When it is slow, retryable, non-critical to the immediate response, or fanout-heavy.</details>

<details><summary>What does pagination protect?</summary>Database, memory, latency, and clients from unbounded reads.</details>

<details><summary>What should error responses help clients do?</summary>Know whether to retry, back off, fix input, re-authenticate, or stop.</details>
