---
description: Start local dev infra (FrankenPHP + Mercure + Postgres)
agent: build
---
Bring up the local development infrastructure.

Steps:
1) From repo root, ensure infra env exists:
   - If `infra/.env` does not exist, copy it from `infra/.env.example`.
2) Start containers:
   - `docker compose -f infra/docker-compose.yml up -d --build`
3) Print the important URLs:
   - Backend: http://localhost:8080
   - Mercure hub: http://localhost:8080/.well-known/mercure
   - Mercure UI (dev): http://localhost:8080/ui/
4) Smoke test:
   - `curl -fsS http://localhost:8080/api/health`

If anything fails, show the relevant docker logs.
