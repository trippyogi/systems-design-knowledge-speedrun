# Data Modeling and Access Patterns

Start with access patterns, not database brands.

## Useful question sequence

1. What entities exist?
2. What are the read paths?
3. What are the write paths?
4. Which queries must be fast?
5. Which queries can be async or approximate?
6. What consistency does each path require?
7. What is the retention policy?
8. What data is sensitive?

## Access pattern table

| Path | Query | Scale | Latency target | Consistency | Candidate store |
|---|---|---:|---:|---|---|
| Read profile | Get user by id | High | Low | Strong-ish | SQL / KV |
| Feed read | Get recent posts for user | Very high | Low | Eventual ok | KV / cache |
| Analytics | Count active users/day | Batch | Minutes | Approx ok | Warehouse |

## Storage cheat sheet

- **Relational DB**: transactions, constraints, joins, strong consistency, mature tooling.
- **Key-value store**: simple lookups, high scale, low latency.
- **Document store**: flexible schema, nested objects, app-aligned reads.
- **Search index**: text search, ranking, faceting, autocomplete.
- **Time-series DB**: append-heavy metrics and time-window queries.
- **Object storage**: large blobs, images, videos, backups.
- **Graph DB**: deep relationship traversal when joins become awkward.

## Denormalization rule

Denormalize when read latency or scale demands it, but write down:

- Source of truth
- Derived copies
- Update mechanism
- Staleness tolerance
- Repair process
