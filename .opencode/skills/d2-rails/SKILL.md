---
name: d2-rails
description: Repo conventions and workflow for the d2 monorepo (Symfony+Vue+Mercure)
compatibility: opencode
---
## What this repo is
- Monorepo: `/server` (Symfony) + `/client` (Vue) + `/infra` (FrankenPHP+Mercure).
- No Canvas on client.
- Combat is turn-based by rounds.
- Server is authoritative; client only renders state and submits commands.

## Where the truth lives
- Behaviour & contracts: `docs/contracts.md`
- Process: `AGENTS.md`, `docs/process.md`
- Backlog: `docs/backlog.md`

## Working rules
- Keep changes small and testable.
- If you change a wire payload or event, update `docs/contracts.md` in the same commit.
- Avoid introducing complex infrastructure unless it unlocks the next MVP milestone.

## Quick commands (OpenCode)
- `/dev` start infra
- `/ci` run full checks
- `/doctor` check tooling
