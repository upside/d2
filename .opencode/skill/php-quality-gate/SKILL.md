    ---
    name: php-quality-gate
    description: How to run and interpret cs-fixer, PHPStan, Psalm, and Deptrac in this repo
    compatibility: opencode
    ---
    ## What I do
- Ensure PHP code quality tools are run consistently:
  - php-cs-fixer (style)
  - PHPStan (static analysis)
  - Psalm (deep static analysis)
  - Deptrac (architecture dependency rules)
  - PHPUnit (tests)

## Commands
From `server/`:
- `composer cs` — style check (dry-run)
- `composer cs:fix` — auto-fix style
- `composer stan` — PHPStan
- `composer psalm` — Psalm
- `composer deptrac` — Deptrac
- `composer test` — PHPUnit
- `composer ci` — all of the above (quality gate)

## How to debug failures
- Fix **cs-fixer** first (it can produce noisy diffs).
- Then **stan/psalm**: fix one error category at a time.
- Deptrac: either move code to the correct layer/module or adjust deptrac.yaml if the rule is wrong.
