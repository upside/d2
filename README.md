# d2 (pet project)

Monorepo:

- `server/` — Symfony (PHP 8.4+) backend
- `client/` — Vue 3 + Router + Pinia + TypeScript frontend
- `infra/` — FrankenPHP (+ built-in Mercure) + Postgres dev stack
- `docs/` — lightweight project rails (contracts, specs, decisions, templates)

## Quick start (dev)

1) Start infra:

```bash
cd infra
cp .env.example .env
docker compose up -d --build
```

2) Install deps:

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
