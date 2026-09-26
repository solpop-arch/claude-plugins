---
name: init
description: Set up the docflow document layout in the current project — docs/ skeleton, product.md and master-plan.md templates, and a four-section CLAUDE.md with the docflow rules block.
disable-model-invocation: true
allowed-tools: Read Glob
---

# /docflow:init

Set up the docflow layout in the current project root. Templates are in `${CLAUDE_SKILL_DIR}/templates/`.

## Current state

!`find . -maxdepth 2 -not -path "./.git*" -not -path "./node_modules*"`

## Steps

1. **Never overwrite an existing file.** For every file below, create it only if it doesn't exist.
2. Create `docs/plan/`, `docs/architecture/`, `docs/design/`, `docs/review/`, `docs/reference/`. Put an empty `.gitkeep` in each folder that ends up empty.
3. `docs/product.md` — copy `templates/product.md`. Fill in the project name and a one-line identity if you can infer them from README.md or the package manifest; otherwise leave the placeholders.
4. `docs/plan/master-plan.md` — copy `templates/master-plan.md`.
5. `CLAUDE.md`
   - **Doesn't exist**: copy `templates/CLAUDE.md` and fill in "Project setup" from what you can see (stack, main folders). Leave the other sections empty.
   - **Exists**: don't rewrite it. Check it for the four section headings (`## Project setup`, `## Current work`, `## Backlog`, `## Gotchas`) and for the `## Docs rules (docflow)` block. Show the user exactly what you would append (missing headings at the end, the rules block from the template) and append only after they agree. Existing sections in another language or with slightly different names count as present — mention them instead of duplicating.
6. **Stray documents**: if the root has other `.md` files (besides README variants and standard community files like LICENSE.md or CHANGELOG.md), or there is a `tasks/` folder or `TODO.md`, list them with a suggested destination under `docs/`. **Don't move anything without the user's approval.**
7. Report what you created, what you skipped because it existed, and any suggestions from step 6.

Rules reference: the `rules` skill in this plugin (`/docflow:rules`).
