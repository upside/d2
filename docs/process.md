# Process (lightweight)

Goal: keep the project **simple** but still "agent-friendly".

## What we maintain
- `AGENTS.md` — how to run/check/work in this repo
- `docs/contracts.md` — source of truth for wire format (commands/events)
- `docs/decisions.md` — tiny decision log (instead of ADRs)
- `docs/backlog.md` — small backlog (epics → stories → tasks)

## Definition of Done (DoD)
A task is done when:
- It has clear acceptance criteria
- Server domain logic is tested (unit tests)
- Client renders server results (no duplicated combat logic)
- `docs/contracts.md` is updated if the wire format changed

## Where logic lives
- **Server**: all combat rules and validation
- **Client**: UI + state + calls API + renders events/snapshots
