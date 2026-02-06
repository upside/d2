---
description: Run all checks (server + client) and summarize failures
agent: build
---

Run the full local CI for both server and client. If anything fails, focus on the first error, explain it briefly, and suggest the smallest fix.

```bash
cd server
composer ci
cd ../client
npm run ci
```
