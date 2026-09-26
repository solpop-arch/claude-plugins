# {{PROJECT_NAME}}

## Project setup

- **What it is**: {{ONE_LINE_IDENTITY}} → Product definition, principles, direction: `docs/product.md`
- **Stack**: {{STACK}}
- **Folders**: {{MAIN_FOLDERS}}

## Docs rules (docflow)

- Root: only `CLAUDE.md` and `README.md` as project documents (localized READMEs and LICENSE/CHANGELOG/CONTRIBUTING are fine). Everything else goes in `docs/`.
- `docs/`: `product.md` + `plan/` · `architecture/` · `design/` · `review/` · `reference/`. No new subfolders; if nothing fits, use `reference/`.
- Plans: `docs/plan/master-plan.md`; phase files only when a phase starts. No per-feature documents.
- Reviews: `docs/review/<type>-<topic>-<YYYYMMDD>.md`.
- Work and bugs live in this file: Current work (now), Backlog (later, one line each), Gotchas (traps you'd hit again — never delete). No `tasks/` or `TODO.md`.
- After changing structure, design, or visuals, update the matching doc in the same task. Edit existing docs; describe only the current state.
- README.md stays self-contained for outside readers; internal docs link to `docs/product.md`.

## Current work

## Backlog

## Gotchas
