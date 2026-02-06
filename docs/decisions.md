# Decisions (log)

We keep decisions lightweight. Add a new bullet when something matters.

- 2026-02-06: Monorepo layout: `/server` (Symfony) + `/client` (Vue) + `/infra` (FrankenPHP+Mercure) + `/docs` rails.
- 2026-02-06: Combat: turn-based rounds; server authoritative; results delivered as events + snapshot.
- 2026-02-06: Realtime transport: Mercure (SSE) via FrankenPHP.

- 2026-02-06: Use a modular monolith layout (`src/Modules/*` + `src/Shared/*`) to keep feature boundaries while staying a single deployable app.
- 2026-02-06: Enforce PHP quality gate via cs-fixer + PHPStan + Psalm + Deptrac + PHPUnit (run via `composer ci`).
