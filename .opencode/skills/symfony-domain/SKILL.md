---
name: symfony-domain
description: Domain-first Symfony structure for turn-based combat (unit-testable core)
compatibility: opencode
---
## Layering
- Domain (pure PHP): rules, state, events. No Symfony, no Doctrine, no IO.
- Application: use-cases/handlers orchestrating domain + persistence + publishing.
- Infrastructure: Controllers, DB, Mercure publishing, serialization.

## Rules
- Controllers must be thin (validate, call handler, return response).
- The combat engine must be deterministic and unit-tested.

## Suggested directories
- `server/src/Combat/Domain/...`
- `server/src/Combat/Application/...`
- `server/src/Combat/Infrastructure/...`
