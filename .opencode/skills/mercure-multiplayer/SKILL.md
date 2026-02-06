---
name: mercure-multiplayer
description: How d2 uses Mercure topics, auth, and realtime event payloads
compatibility: opencode
---
## Goals
- Realtime delivery for PvP matches.
- Each match has its own topic: `match/{matchId}`.
- Server publishes RoundResult payloads; clients subscribe and update UI.

## Dev mode
- Hub: `http://localhost:8080/.well-known/mercure`
- We may allow anonymous subscribers early for speed.

## Production hardening (later)
- Topics should be private: generate a JWT per participant with subscribe permissions limited to that match topic.
- Never allow a player to subscribe to someone else's match topic.

## Contracts
- RoundResult is defined in `docs/contracts.md`.
