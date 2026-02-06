    ---
    name: modular-monolith
    description: Conventions for modules in src/Modules/* and shared model in src/Shared/*
    compatibility: opencode
    ---
    ## Goal
Keep a single deployable Symfony app, but structure code by feature modules.

## Layout
- `src/Modules/<ModuleName>/...` — feature modules (Chat, Forum, World, Matchmaking, etc.)
  - `Controller/` — HTTP controllers for that module
  - `Entity/` — Doctrine entities owned by the module
  - `Repository/` — repositories
  - `Service/` — application services/use-cases
  - Optional: `Message/` (Messenger), `Dto/`, `Form/`, `Event/`

- `src/Shared/...` — shared model and cross-cutting code used by many modules
  - `Model/` — reusable domain models (e.g., User, Character)
  - `Service/` — shared services (id generation, time, etc.)
  - Keep shared small and stable.

## Dependency rule (simple)
- Modules may depend on `Shared`.
- Avoid direct cross-module calls; prefer shared abstractions or events.

## When to add to Shared
Put something in Shared only if:
- It is used by 2+ modules, and
- It is stable and not feature-specific.
