# Knowledge Speedrun Method

Use this method to turn any domain into a fast-learning repo.

## 1. Create the map

Create a dependency graph of concepts. Label each node by payoff:

- **A-tier**: unlocks many other ideas or improves real work immediately.
- **B-tier**: useful after the core is stable.
- **C-tier**: interesting, niche, or advanced.

## 2. Identify primitives and moves

A primitive is a reusable idea. A move is how you apply it.

Example:

- Primitive: cache
- Move: cache-aside read path
- Failure mode: stale data
- Tradeoff: lower latency, more invalidation complexity

## 3. Convert concepts into drills

Every concept needs an active drill.

Bad:

- “Read about queues.”

Good:

- “Design image upload processing where the encoder fails 1% of the time. Add retries, idempotency, and a dead-letter queue.”

## 4. Capture decisions

Every real design has tradeoffs. Write ADRs so learners see why decisions were made.

## 5. Teach back

The fastest way to find gaps is to explain the concept in simple language.

Use this script:

1. Problem it solves
2. Simple example
3. How it works
4. Common failure mode
5. Tradeoff
6. When not to use it

## 6. Score against a rubric

A rubric makes knowledge visible. It also prevents false confidence.

Score designs on:

- Requirements clarity
- Sizing
- Data model
- Scalability
- Reliability
- Security
- Cost
- Communication

## 7. Publish small increments

Repos die when they require giant perfect contributions. Prefer tiny artifacts:

- One concept card
- One drill
- One diagram
- One ADR
- One review note
