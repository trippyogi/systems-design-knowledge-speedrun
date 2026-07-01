# START HERE: Your First Systems Design Rep in 30 Minutes

Set a 25-minute timer. Do not read the repo first.

You are going to design a URL shortener from scratch, score it, then improve it.

## The prompt

Design a URL shortener like bit.ly.

It should:

- Create short links for long URLs.
- Redirect short links to long URLs.
- Track basic click analytics.
- Survive popular links, spammy link creation, and partial dependency failures.

## The 25-minute rep

Spend your time like this:

1. **3 min — Requirements**
   - Users:
   - Functional requirements:
   - Non-goals:
   - Hardest non-functional requirement:

2. **5 min — Numbers**
   - New links/day:
   - Redirects/day:
   - Peak redirects/sec:
   - Storage/year:
   - Cache working set:

3. **5 min — API + data model**
   - `POST /links`
   - `GET /{slug}`
   - `GET /links/{slug}/analytics`
   - Tables/entities:
   - Indexes:

4. **5 min — Architecture**
   - Draw the synchronous redirect path.
   - Draw the async analytics path.
   - Label cache, DB, queue, workers.

5. **5 min — Break it**
   - What happens if one slug gets 10k redirects/sec?
   - What happens if the database is down?
   - What happens if bots create millions of links?
   - What happens if analytics is 30 minutes behind?

6. **2 min — Tradeoff**
   - Biggest decision:
   - Alternative rejected:
   - What changes at 10x:

## Five-line self score

Score 0-2 for each:

| Check | Score |
|---|---:|
| Requirements and non-goals are clear |  |
| Numbers changed at least one design choice |  |
| Data model matches access patterns |  |
| Failure modes include mitigation |  |
| Tradeoff explains why, not just what |  |

Total:

- 0-3: redo immediately with the playbook open.
- 4-7: compare with the worked solution and revise.
- 8-10: run AI review, then attempt rate limiter.

## Next 30 minutes

1. Run the [AI design-review prompt](prompts/design-review-prompt.md) against your answer.
2. Diff against the [worked URL shortener solution](docs/drills/solutions/url-shortener.md).
3. Rewrite the weakest section.
4. Write a 10-line teach-back: “Here is the system, here is what breaks, here is the tradeoff.”

That is one rep. Repeat daily.
