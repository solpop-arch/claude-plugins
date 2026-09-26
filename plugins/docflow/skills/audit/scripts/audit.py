#!/usr/bin/env python3
"""docflow audit — deterministic layout checks for a project root.

Usage: audit.py [ROOT] [--json]
Exit code: 0 if no errors, 1 if any error-level finding.
"""
import json
import re
import sys
from pathlib import Path

ROOT_MD_ALLOWED = {
    "CLAUDE.md", "README.md", "AGENTS.md",
    "LICENSE.md", "CHANGELOG.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
}
LOCALIZED_README = re.compile(r"^README\.[A-Za-z]{2,3}(-[A-Za-z]{2,4})?\.md$")
DOCS_SUBDIRS = {"plan", "architecture", "design", "review", "reference"}
CLAUDE_SECTIONS = {
    "Project setup": re.compile(r"^##\s+(project setup|프로젝트 설정)", re.I | re.M),
    "Current work": re.compile(r"^##\s+(current work|현재 작업)", re.I | re.M),
    "Backlog": re.compile(r"^##\s+backlog", re.I | re.M),
    "Gotchas": re.compile(r"^##\s+gotchas", re.I | re.M),
}
REVIEW_NAME = re.compile(r"^[a-z0-9]+-[a-z0-9][a-z0-9-]*-\d{8}\.md$")


def audit(root: Path):
    findings = []

    def add(level, rule, path, message, fix):
        findings.append({"level": level, "rule": rule, "path": path, "message": message, "fix": fix})

    for p in sorted(root.glob("*.md")):
        if p.name not in ROOT_MD_ALLOWED and not LOCALIZED_README.match(p.name):
            add("error", "root-md", p.name, "Markdown document at the project root",
                "Move it under docs/ (plan/, architecture/, design/, review/, or reference/)")

    for name in ("tasks", "TODO.md", "todo.md", "TODO"):
        if (root / name).exists():
            add("error", "no-tasks", name, "Separate task tracker",
                "Move items into CLAUDE.md Current work / Backlog and remove it")

    docs = root / "docs"
    if not docs.is_dir():
        add("error", "docs-dir", "docs/", "No docs/ folder", "Run /docflow:init")
    else:
        if not (docs / "product.md").is_file():
            add("warn", "product-md", "docs/product.md", "Missing product definition",
                "Create docs/product.md (identity, principles, direction, releases)")
        for d in sorted(p for p in docs.iterdir() if p.is_dir()):
            if d.name not in DOCS_SUBDIRS:
                add("error", "docs-subdir", f"docs/{d.name}/", "Subfolder outside the fixed five",
                    "Move its contents into plan/, architecture/, design/, review/, or reference/")
        plan = docs / "plan"
        if plan.is_dir():
            mds = [p.name for p in plan.glob("*.md")]
            if mds and "master-plan.md" not in mds:
                add("warn", "master-plan", "docs/plan/", "Plan files exist but no master-plan.md",
                    "Name the overall plan docs/plan/master-plan.md")
        review = docs / "review"
        if review.is_dir():
            for p in sorted(review.glob("*.md")):
                if not REVIEW_NAME.match(p.name):
                    add("warn", "review-name", f"docs/review/{p.name}", "Review file name format",
                        "Rename to <type>-<topic>-<YYYYMMDD>.md")

    claude = root / "CLAUDE.md"
    if not claude.is_file():
        add("error", "claude-md", "CLAUDE.md", "No CLAUDE.md", "Run /docflow:init")
    else:
        text = claude.read_text(encoding="utf-8", errors="replace")
        missing = [k for k, rx in CLAUDE_SECTIONS.items() if not rx.search(text)]
        if missing:
            add("warn", "claude-sections", "CLAUDE.md", "Missing sections: " + ", ".join(missing),
                "Add the missing ## headings (Project setup / Current work / Backlog / Gotchas)")

    return findings


def main(argv):
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    root = Path(args[0] if args else ".").resolve()
    findings = audit(root)
    errors = sum(f["level"] == "error" for f in findings)
    if as_json:
        print(json.dumps({"root": str(root), "errors": errors,
                          "warnings": len(findings) - errors, "findings": findings},
                         ensure_ascii=False, indent=2))
    else:
        print(f"docflow audit: {root}")
        if not findings:
            print("  ✔ no findings")
        for f in findings:
            mark = "✖" if f["level"] == "error" else "⚠"
            print(f"  {mark} [{f['rule']}] {f['path']} — {f['message']}\n      → {f['fix']}")
        print(f"  {errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
