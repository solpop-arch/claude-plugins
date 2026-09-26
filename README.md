# solpop — Claude Code plugins

A small Claude Code plugin marketplace.

[한국어](README.ko.md)

## Plugins

| Plugin | What it does |
|---|---|
| [docflow](plugins/docflow/) | Opinionated project documentation layout: root `CLAUDE.md` + `README.md` only, a fixed `docs/` tree anchored on `product.md`, and a four-section `CLAUDE.md` that replaces task files. `/docflow:init` scaffolds it, `/docflow:audit` checks it. |

## Install

```
claude plugin marketplace add solpop-arch/claude-plugins
claude plugin install docflow@solpop
```

Or from inside a session: `/plugin install docflow --marketplace solpop-arch/claude-plugins`.

## License

MIT
