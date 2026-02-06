---
description: Check local dev prerequisites and common port conflicts
agent: build
---
Check that required tooling is installed and common ports are available.

Verify:
- docker + docker compose
- php + composer
- node + npm

Then check whether ports are free:
- 8080 (backend)
- 5173 (vite)
- 5432 (postgres)

Output a short checklist with OK/MISSING/WARN.
If a port is in use, show the process if possible (e.g. `lsof -iTCP:<port> -sTCP:LISTEN -nP`).
