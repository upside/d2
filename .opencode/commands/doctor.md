---
description: Check local environment (docker, node, php) and required ports
agent: plan
---

Check that Docker, PHP, Composer, Node, and NPM are available and that ports are free.

Suggested manual checks:

```bash
docker --version
docker compose version
php -v
composer -V
node -v
npm -v
lsof -i :5173 || true
lsof -i :8080 || true
```

If something is missing, propose the quickest fix for macOS (Homebrew) and Linux.
