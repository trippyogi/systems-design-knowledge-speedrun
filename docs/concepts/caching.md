# Caching

Caching trades freshness and complexity for latency and cost reduction.

## Cache placement

- Browser cache
- CDN / edge cache
- API gateway cache
- Application cache
- Distributed cache
- Database buffer/cache

## Common strategies

### Cache-aside

App checks cache first. On miss, reads DB and fills cache.

Good for:

- Read-heavy data
- Tolerable staleness
- Simple adoption

Risks:

- Cache stampede
- Stale values
- Invalidation complexity

### Write-through

Writes go to cache and DB together.

Good for:

- Data expected to be read soon
- Consistency between cache and DB matters

Risks:

- Higher write latency
- Cache stores cold data

### Write-back

Writes go to cache first and flush to DB later.

Good for:

- Very high write throughput

Risks:

- Data loss if cache fails
- More complex recovery

## Cache failure modes

| Failure | Symptom | Mitigation |
|---|---|---|
| Stampede | Many requests hit DB after miss | Request coalescing, jittered TTL, locks |
| Hot key | One key overloads a shard | Replicate hot keys, local cache, split key |
| Stale data | Users see old state | TTLs, versioning, invalidation, read-through repair |
| Cache outage | DB overload | Circuit breakers, degraded mode, rate limits |

## Good interview phrase

> I would cache this only after identifying the hot read path and defining acceptable staleness.

## Recall questions

<details><summary>When does cache-aside work best?</summary>Read-heavy data where misses can safely fall back to the source of truth.</details>

<details><summary>What is a cache stampede?</summary>Many requests miss or expire the same key at once and overload the backing store.</details>

<details><summary>Name two stampede mitigations.</summary>Request coalescing, jittered TTLs, stale-while-revalidate, early refresh, or hot-key replication.</details>

<details><summary>When does write-through beat cache-aside?</summary>When newly written data is read immediately and write-path complexity is acceptable.</details>

<details><summary>What should you define for every cache?</summary>Key format, TTL, invalidation, stale-read tolerance, cold-start behavior, and fallback path.</details>
