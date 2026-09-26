---
name: audit
description: Check the current project against the docflow document rules and report violations with suggested fixes. Read-only.
disable-model-invocation: true
allowed-tools: Read Glob Grep Bash(python3 *audit.py*)
---

# /docflow:audit

## Structural checks

!`python3 "${CLAUDE_SKILL_DIR}/scripts/audit.py" . 2>&1`

## Steps

1. Report the structural findings above as they are. Don't re-derive them.
2. Then check content-level rules the script can't see. Read only what you need:
   - `docs/product.md`: does it state identity, principles, direction, and release history? Do other internal docs repeat the product definition instead of linking to it?
   - `README.md`: is it self-contained for an outside reader, or does it just point into `docs/`?
   - `CLAUDE.md`: is "Current work" stale (all items checked, or clearly finished)? Does "Project setup" point to `docs/product.md`?
   - Per-feature documents (for example `docs/plan/feature-login.md`) that should be folded into a phase document or CLAUDE.md.
   - The same document duplicated in two places.
3. Output one list, errors first. For each item: path, rule, and a concrete fix (target path for moves).
4. **Change nothing.** This skill only reports. Offer to apply the fixes, and do so only after the user agrees.

Full rules: the `rules` skill in this plugin.
