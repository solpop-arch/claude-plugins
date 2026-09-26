# claude-plugins (solpop marketplace)

## Project setup

- **What it is**: a Claude Code plugin marketplace (`solpop`) → product definition: `docs/product.md`
- **Layout**: `.claude-plugin/marketplace.json` lists plugins; each plugin lives in `plugins/<name>/` with `.claude-plugin/plugin.json` and `skills/<skill>/SKILL.md`.
- **Plugins**: `docflow` (documentation layout rules — `/docflow:init`, `/docflow:audit`, auto-loaded `rules`).
- **Validate before every push**: `claude plugin validate --strict ./plugins/<name>` and `claude plugin validate .`
- **Versioning**: `version` is omitted in plugin.json, so users receive updates by commit SHA.
- **Naming**: plugin names are permanent (install ids are `<name>@solpop`). Change `displayName` for a new label. For an unavoidable rename, use `renames` in marketplace.json.
- **Scripts**: keep executables inside a skill (`skills/<skill>/scripts/`), not in plugin `bin/`. claude.ai and Cowork won't install plugins that have `bin/`.
- **Docs rules**: this repo follows docflow itself. Run `python3 plugins/docflow/skills/audit/scripts/audit.py .`

## Current work

## Backlog

- Consider submitting docflow to Anthropic's directory (claude.ai/directory/manage) once it has some usage
- Plugin eval suite (`claude plugin eval`)

## Gotchas

- The marketplace entry `name` must equal the `name` in the plugin's plugin.json, or installs fail with "not found in marketplace".
- A command in a skill's !`...` injection that exits non-zero, or isn't pre-approved, aborts the whole skill **silently** under `claude -p` (no output). Keep injected commands exit-0 and pre-approve them narrowly in `allowed-tools` (e.g. `Bash(python3 *audit.py*)`).
- Relative `source` paths are written from the marketplace root and must not contain `..`.
