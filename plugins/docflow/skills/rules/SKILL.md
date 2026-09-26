---
name: rules
description: Project document layout and workflow rules (docflow). Use whenever you are about to create, move, rename, or reorganize a project document (plans, specs, design docs, architecture notes, retrospectives, READMEs, guides), edit a project's CLAUDE.md, record a bug or lesson, or decide where a document should live (repo vs a docs tool like Notion).
---

# docflow rules

Apply these rules to every project document. Full rules with examples: [reference.md](reference.md).

## Where documents go

- **Root**: only `CLAUDE.md` and `README.md` as project documents. Localized READMEs (`README.ko.md`), standard community files (`LICENSE.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`), and an existing `AGENTS.md` are also fine.
- **Everything else goes in `docs/`**:

| Path | For |
|---|---|
| `docs/product.md` | Product definition: identity, principles, direction, release history. The single source of truth. |
| `docs/plan/` | Plans. The overall plan is always `master-plan.md`; phase files (`phase1-xxx.md`) only when that phase starts |
| `docs/architecture/` | The system as built: components, data flow |
| `docs/design/` | Visual system: typography, color, spacing, UI patterns |
| `docs/review/` | Retrospectives, named `<type>-<topic>-<YYYYMMDD>.md` (`bug-`, `postmortem-`, `audit-`) |
| `docs/reference/` | Reference material, external docs, setup guides — and anything that fits nowhere else |

- **Never create a new subfolder** under `docs/`. **Never write per-feature documents** — use the phase document or CLAUDE.md "Current work".
- A plan-mode or tool scratch file is not a deliverable. When asked for a plan/spec/design doc, write it into `docs/`.

## CLAUDE.md has four sections

`## Project setup` (fixed) · `## Current work` (rotates per feature) · `## Backlog` (one line per item) · `## Gotchas` (cumulative, never delete).
No `tasks/` folder, no `TODO.md`. Bugs: fix now → Current work; later → Backlog; a trap you'd hit again → also Gotchas.

## Keep documents current

After changing structure, design, or visuals, update the matching document in the same task: `product.md`, `docs/architecture/`, `docs/design/`, `README.md` (only for externally visible changes), `CLAUDE.md`.
Edit the existing document instead of creating a new one. Describe only the current state.

## Linking

Internal docs link to `docs/product.md` instead of repeating the product definition. `README.md` is the exception: it must be self-contained for outside readers.

## Repo or docs tool

If the document feeds a decision or an agent and you may need to reproduce the result later → git. If only its latest state matters (dashboards, portfolio overviews, generic guides) → the team's docs tool (Notion, Confluence, …). Don't keep copies of the same document in two places.
