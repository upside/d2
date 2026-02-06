# AGENTS.md — d2 (monorepo)

This repo is set up for agent-driven development with **minimal process overhead**.

## Non‑negotiable product rules
- **No Canvas** on the client.
- Combat is **turn-based by rounds**.
- The **server is authoritative**: clients submit actions; the server resolves the round and returns/publishes results.
- Multiplayer is core. Real-time delivery uses **Mercure** (built into FrankenPHP).

## Repo layout

### Architecture: modular monolith
- We build a **modular monolith**: feature modules live under `server/src/Modules/*`.
- Shared reusable model lives under `server/src/Shared/*`.
- Convention: `Module/*` may depend on `Shared/*`; avoid direct cross-module calls.

- `server/` — Symfony (PHP 8.4+)
- `client/` — Vue 3 + Router + Pinia + TypeScript
- `infra/` — FrankenPHP (+ Mercure) + Postgres
- `docs/` — lightweight rails: contracts/specs/decisions/templates

## How to run (dev)

1) Start infrastructure:

```bash
cd infra
cp .env.example .env
docker compose up -d --build
```

2) Install dependencies:

```bash
cd ../server
composer install

cd ../client
npm install
```

3) Run the frontend:

```bash
npm run dev
```

URLs:
- Frontend: http://localhost:5173
- Backend: http://localhost:8080
- Mercure hub: http://localhost:8080/.well-known/mercure

Quick smoke test:
- Open http://localhost:5173/api/health (proxied to backend)

## Mandatory checks before committing

Server (from `server/`):
```bash
composer cs
composer stan
composer psalm
composer deptrac
composer test
# or all at once:
composer ci
```

Client (from `client/`):
```bash
npm run lint
npm run type-check
npm run test:unit
# or all at once:
npm run ci
```

## Working rules (minimal process)

We do **not** maintain formal ADRs. Instead:
- If a decision matters, add a short bullet to `docs/decisions.md`.
- All API/real-time changes must update `docs/contracts.md`.

When implementing a feature:
1) Start from `docs/templates/story.md`.
2) Keep domain logic on the server (no combat math in Vue).
3) Prefer deterministic, unit-testable domain code.

## Contracts-first
- Commands/events are documented in `docs/contracts.md`.
- Any wire change requires updating the contract doc in the same commit.


## UI / art style
- Follow `docs/style/art-ui-style.md` (prompts + do/don't) when generating UI mockups or icons.
