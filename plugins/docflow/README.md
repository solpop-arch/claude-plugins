# docflow

Opinionated documentation layout and workflow for Claude Code projects. It gives every project the same predictable shape, so Claude (and you) always know where a document belongs and which one is current.

[한국어](README.ko.md)

## What it enforces

```
<project>/
├── CLAUDE.md        ← setup · current work · backlog · gotchas
├── README.md        ← self-contained public intro
└── docs/
    ├── product.md   ← single source of truth for what the product is
    ├── plan/        ← master-plan.md (+ phase files when a phase starts)
    ├── architecture/
    ├── design/
    ├── review/      ← <type>-<topic>-<YYYYMMDD>.md
    └── reference/
```

- **Two root docs only**: `CLAUDE.md` and `README.md`. Localized READMEs and standard community files (LICENSE, CHANGELOG, CONTRIBUTING, …) are fine.
- **Fixed `docs/` tree**: five subfolders, never more. If a document fits nowhere, it goes in `reference/`.
- **`product.md` is the hub**: internal docs link to it instead of repeating the product definition. README stays self-contained for outsiders.
- **CLAUDE.md replaces task files**: *Current work* (now) → *Backlog* (later, one line each) → *Gotchas* (traps you'd hit again, never deleted). No `tasks/`, no `TODO.md`.
- **Docs stay current**: after changing structure, design, or visuals, the matching document is updated in the same task. Edit the existing document; describe only the current state.
- **Repo or docs tool**: documents that feed decisions or agents live in git; latest-state-only material (dashboards, portfolio overviews, generic guides) goes in your docs tool.

## Install

```
claude plugin marketplace add solpop-arch/claude-plugins
claude plugin install docflow@solpop
```

## Skills

| Skill | How it runs | What it does |
|---|---|---|
| `/docflow:init` | You run it | Creates the `docs/` skeleton, `product.md` and `master-plan.md` templates, and a four-section `CLAUDE.md` with a short rules block. Never overwrites existing files; for an existing CLAUDE.md it shows what it would append and asks first. |
| `/docflow:audit` | You run it | Runs structural checks (stray root docs, extra `docs/` folders, task files, missing sections, review file names), then reviews content-level rules. Reports only; changes nothing without your approval. |
| `rules` | Claude loads it automatically | The full rule set, loaded when Claude is about to create or move a document or edit CLAUDE.md. |

**Tip**: run `/docflow:init` once per project, even if the docs already exist. The rules block it adds to `CLAUDE.md` is what makes the rules apply in every session. Skills that load automatically only load when Claude judges them relevant.

## License

MIT
