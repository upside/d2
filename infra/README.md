# Infra (dev)

We use FrankenPHP as the PHP app server and enable its built-in Mercure hub for realtime.

- Backend: http://localhost:8080
- Mercure hub: http://localhost:8080/.well-known/mercure

## Start

```bash
cd infra
cp .env.example .env
docker compose up -d --build
```

## Notes
- Mercure is enabled via `infra/Caddyfile`.
- By default `anonymous` subscribers are enabled (dev-only). For real PvP, we'll disable anonymous and issue per-match JWTs.
