---
description: Start local infra (FrankenPHP+Mercure+Postgres) and show URLs
agent: build
---

Start local infrastructure with Docker:

```bash
cd infra
cp -n .env.example .env || true
docker compose up -d --build
```

Then print the key URLs:
- Frontend (Vite): http://localhost:5173
- Backend: http://localhost:8080
- Mercure hub: http://localhost:8080/.well-known/mercure
- Mercure UI: http://localhost:8080/ui/
