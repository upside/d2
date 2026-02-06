# Combat (MVP)

## Round flow
1) Server exposes `state.round`.
2) Each participant submits exactly one action for that round.
3) When all actions are submitted, the server resolves the round.
4) The server produces `events[]` + new `state`.
5) The server publishes `RoundResult` to Mercure.

## MVP action set
- `Attack(targetId)`

## MVP order
For v1: resolve in a deterministic order:
1) player1 action
2) player2 action

## Validation
- Round mismatch → reject action.
- Target must exist and be alive.
