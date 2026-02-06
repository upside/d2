---
description: Run full CI checks (server + client)
agent: build
---
Run the project's CI checks from the repo root.

Server:
- `cd server && composer ci`

Client:
- `cd client && npm run ci`

If anything fails:
1) Show the failing output.
2) Identify the root cause.
3) Propose the smallest fix.
4) Re-run the failing command(s) to confirm.
