# solpop plugins — product definition

## Identity

- **One line**: Claude Code plugins that encode working conventions so every project behaves the same way.
- **For whom**: developers who use Claude Code across many personal or small-team projects and want consistent, low-overhead structure.
- **Non-goals**: heavy process tooling, external services, anything that needs accounts or secrets.

## Core principles

1. Conventions over configuration — opinionated defaults, few knobs.
2. Rules that must always apply are written into the project's CLAUDE.md. Auto-loaded skills only help when relevant; they don't replace it.
3. Report before changing: audit-style skills never modify files without approval.
4. Standard library only; nothing to install beyond the plugin.

## Release history

- 2026-09-26 — marketplace created; docflow first release
