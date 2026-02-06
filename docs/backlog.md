# Backlog (seed)

## Epic 1 — PvP match loop (MVP)
- Story: Create match, join match (2 players)
- Story: Subscribe to match realtime topic (Mercure)
- Story: Submit action for round (HTTP)
- Story: Resolve round on server, publish RoundResult
- Story: Client renders events + snapshot

## Epic 2 — Basic combat domain
- Story: CombatState (participants, hp, round)
- Story: ApplyEvents reducer (events → new state)
- Story: ResolveRound for `Attack` (deterministic)
- Story: Validation (round mismatch, invalid target)
