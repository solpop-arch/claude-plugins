# docflow — full rules

The complete document layout and workflow rules. `SKILL.md` in this folder is the short version.

## 1. Folder structure

```
<project-root>/
├── CLAUDE.md              ← instructions for Claude (committed)
├── README.md              ← project introduction, install/run (committed)
├── docs/                  ← every other document (text committed; binaries optional)
│   ├── product.md         ← product definition — the root document
│   ├── plan/              ← plans and roadmaps
│   ├── architecture/      ← design of the system as built
│   ├── design/            ← visual/design system
│   ├── review/            ← retrospectives: bug reports, postmortems, audits
│   └── reference/         ← reference material, external docs, setup guides
├── src/ …                 ← source code
└── .gitignore
```

## 2. Root Markdown files

Only **`CLAUDE.md`** and **`README.md`** are project documents at the root.

Also allowed, because tools and hosting platforms expect them there:
- Localized READMEs: `README.ko.md`, `README.ja.md`, …
- Community files: `LICENSE.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`
- `AGENTS.md`, if the project already uses it for other coding agents

Everything else goes under `docs/`.

## 3. `docs/` layout

`docs/` has one root document plus five fixed subfolders.

| Path | Contents |
|---|---|
| `docs/product.md` | **Product definition.** Identity (what it is, who it's for), core principles, direction, release history. The single source of truth about the product. |
| `docs/plan/` | Plans (`master-plan.md`, per-phase detail) |
| `docs/architecture/` | Design of the system as built: folders, components, data flow |
| `docs/design/` | Visual system: typography, color, spacing, UI patterns. Kept separate from architecture. |
| `docs/review/` | Time-bound records: bug-fix reports, postmortems, audits, large refactor retros. File name: `<type>-<topic>-<YYYYMMDD>.md` (e.g. `bug-login-loop-20260301.md`, `postmortem-…`, `audit-…`). One level of subfolder is fine when one event spans several documents (`review/<topic>/`). |
| `docs/reference/` | Reference material, external docs, setup guides |

**Do not create new subfolders.** If a document doesn't fit, it goes in `reference/`.

User-facing guides (for example `.docx` or `.pdf` handouts) go directly in `docs/`. Subfolders are for development documents.

## 4. `product.md` is the internal link hub

Internal documents don't repeat the product definition; they link to `docs/product.md`.

- **CLAUDE.md → Project setup** — one or two lines of identity plus `→ Product definition, principles, direction: docs/product.md`
- **master-plan.md** — the roadmap opens with "For direction, see product.md"
- **Backlog / plan items** — link the relevant product.md section when they need a reason

**README.md is the exception.** It is a public, self-contained document. It must explain what the product is, who it's for, and how to use it on its own. Don't delegate its explanations to `docs/`, which outsiders may not be able to see. When product.md changes, sync README separately, and only for what is externally visible.

## 5. CLAUDE.md — four sections

A project's CLAUDE.md does four jobs. Don't create a `tasks/` folder, a `TODO.md`, or an external TODO tool.

```markdown
## Project setup       ← fixed (rarely changes)
Stack, folder structure, coding rules, where documents live

## Current work        ← rotates (replaced when a feature is done)
Design details and TODO checklist for the feature in progress

## Backlog             ← added to anytime, drained over time
One line per bug/improvement for later. Move an item to "Current work" when you start it.

## Gotchas             ← cumulative (never deleted)
Platform constraints, counter-intuitive behavior, traps you would otherwise step on again
```

## 6. Plan documents

Choose by project size.

**Pattern A — single file (small projects)**
```
docs/plan/
└── master-plan.md    ← whole roadmap, phase detail included
```

**Pattern B — split by phase (large refactors, technology transitions)**
```
docs/plan/
├── master-plan.md    ← roadmap: phase summaries, direction, priorities
├── phase1-xxx.md     ← Phase 1 detail
└── phase2-xxx.md     ← written when Phase 2 starts
```

Rules:
- The overall plan is always `master-plan.md` (both patterns).
- Write a phase file only when that phase starts. Not in advance.
- No per-feature documents. Put feature detail in the phase document or in CLAUDE.md "Current work".
- A planning tool's scratch file (for example a plan-mode file outside the repo) is not a deliverable. When the user asks for a plan, spec, or design document, write it into `docs/plan/` (or the matching `docs/` folder).

## 7. Work flow

```
docs/plan/master-plan.md (roadmap, rarely changes)
  └→ take the next item → CLAUDE.md "Backlog" (one line)
                            └→ start → CLAUDE.md "Current work" (detail)
                                        └→ done → check off / clear
```

## 8. Keep core documents current

After work that changes a project's structure, design, or visuals, **update the related core documents immediately.** If documents drift from the code, the next task starts from a wrong premise.

Update targets (when they exist):
- `docs/product.md` — identity, principles, or direction changed, or a release shipped
- `docs/architecture/` (e.g. `overview.md`) — architecture, data flow, component structure changed
- `docs/design/` (e.g. `design.md`) — themes, design tokens, UI patterns, layout rules changed
- `README.md` — build/run steps, public API/UX changed. It doesn't have to follow every product.md change; update it when something externally visible changed.
- `CLAUDE.md` — Gotchas, Current work, Backlog

Principles:
- **Edit the existing document; don't create a new one.** One topic, one document.
- Don't touch unrelated parts. Reflect exactly what changed.
- Describe **only the current state**, not a before/after comparison.
- Gotchas accumulate (never delete). Architecture and design documents hold **only current facts** (remove outdated ones).

Examples:
- New theme added → update the theme list in `docs/design/`
- Build pipeline step changed → update the Data Flow section in `docs/architecture/`
- Found a layout-jump trap → one line in CLAUDE.md Gotchas
- New state store added → update the Stores section in `docs/architecture/`

## 9. Bugs

Handled inside CLAUDE.md, no separate tool.

- Fixing now → add to "Current work" TODO → done when fixed
- Fixing later → one line in "Backlog"
- Platform trap → the above, plus one line in "Gotchas" (e.g. "library X silently fails when Y")
- Not every bug goes in Gotchas — only the ones you'd step on again
- Plain coding mistakes: fix and move on
- If more than ~5 pile up, or collaborators join, consider GitHub Issues

## 10. Where a document lives: git or a docs tool

Decide by **reproducibility**: does the document feed a decision, an agent, or an output you may need to reproduce later?

| Put it in | When | Examples |
|---|---|---|
| **git (Markdown)** | It is an input to the system and you need its version history — "which settings produced that result?" must stay answerable | product.md, plans, schemas, parameters, agent prompts/personas |
| **A docs tool** (Notion, Confluence, Google Docs, …) | Only the latest state matters, and it is updated in place rather than versioned | status dashboards, project portfolio overviews, meeting notes, generic how-to guides shared across projects |

If an output in the docs tool depends on a versioned input, record the commit hash next to it so you can trace back.

Project-specific references go in that project's `docs/reference/`. Don't keep a copy in a second repository — copies drift apart.

## Summary

- Root: `CLAUDE.md` and `README.md` (plus localized READMEs and standard community files)
- `docs/`: `product.md` + `plan/`, `architecture/`, `design/`, `review/`, `reference/` — no new folders
- Product definition lives in `product.md`; internal documents link to it (README is the self-contained exception)
- No per-feature documents: use phase documents or `master-plan.md`
- Work, bugs, lessons: no `tasks/`; use the four CLAUDE.md sections
- git for versioned inputs, a docs tool for latest-state-only documents
