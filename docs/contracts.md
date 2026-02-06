# Contracts (v1, MVP)

This document is the source of truth for client↔server payloads.

## Realtime (Mercure)
- Hub URL (dev): `http://localhost:8080/.well-known/mercure`
- Topic per match: `match/{matchId}`

In production, match topics should be **private** (JWT per participant). In early dev we can keep anonymous subscribers.

## HTTP API

### POST /api/matches
Create a match.

Response (201):
```json
{
  "matchId": "...",
  "state": {
    "round": 1,
    "participants": []
  }
}
```

### POST /api/matches/{matchId}/join
Join an existing match.

Request:
```json
{ "playerName": "Alice" }
```

Response (200):
```json
{
  "matchId": "...",
  "state": {
    "round": 1,
    "participants": [
      { "id": "p1", "name": "Alice", "hp": 30 }
    ]
  }
}
```

### POST /api/matches/{matchId}/actions
Submit an action for the current round.

Request (SubmitAction):
```json
{
  "actorId": "p1",
  "round": 1,
  "action": { "type": "Attack", "targetId": "p2" }
}
```

Response (202):
```json
{ "queued": true }
```

The actual round result is delivered via Mercure.

## Round result (Mercure payload)

Published to topic: `match/{matchId}`

Payload (RoundResult):
```json
{
  "matchId": "...",
  "round": 1,
  "events": [
    { "type": "ActionDeclared", "actorId": "p1", "action": { "type": "Attack", "targetId": "p2" } },
    { "type": "DamageDealt", "sourceId": "p1", "targetId": "p2", "amount": 7 },
    { "type": "RoundEnded", "round": 1 }
  ],
  "state": {
    "round": 2,
    "participants": [
      { "id": "p1", "hp": 30 },
      { "id": "p2", "hp": 23 }
    ]
  }
}
```

## Events (minimum)
- `ActionDeclared { actorId, action }`
- `DamageDealt { sourceId, targetId, amount }`
- `EntityDied { entityId }`
- `RoundEnded { round }`
