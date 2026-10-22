#!/usr/bin/env python3
"""Check local Markdown links and Codex skill metadata. No external dependencies."""

import argparse
from pathlib import Path
import re
import sys

SKILL_NAME = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)")


def check(root):
    problems = []
    files = list(root.rglob("*.md"))
    skills = sorted((root / ".agents" / "skills").glob("*/SKILL.md"))
    if not (root / "AGENTS.md").is_file() or not (root / "README.md").is_file():
        problems.append("Missing root README.md or AGENTS.md")
    if not skills:
        problems.append("No SKILL.md files found")
    names = set()
    for path in skills:
        content = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", content, flags=re.DOTALL)
        if not match:
            problems.append(f"{path.relative_to(root)}: missing front matter")
            continue
        header = match.group(1)
        fields = {}
        for line in header.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                fields[key.strip()] = val.strip().strip('"').strip("'")
        name, desc = fields.get("name", ""), fields.get("description", "")
        if not SKILL_NAME.fullmatch(name) or name != path.parent.name:
            problems.append(f"{path.relative_to(root)}: invalid or mismatched skill name")
        if name in names:
            problems.append(f"Duplicate skill name: {name}")
        names.add(name)
        if not 40 <= len(desc) <= 400:
            problems.append(f"{path.relative_to(root)}: description length outside 40..400")
        if len(content.splitlines()) > 110:
            problems.append(f"{path.relative_to(root)}: consider reducing length (over 110 lines)")
    for path in files:
        content = path.read_text(encoding="utf-8")
        for raw in LINK.findall(content):
            target = raw.split("#", 1)[0].strip()
            if not target or target.startswith(("http:", "https:", "mailto:", "$")):
                continue
            dest = (path.parent / target).resolve()
            if not dest.exists():
                problems.append(f"{path.relative_to(root)}: broken local link: {target}")
        if "\r" in content:
            problems.append(f"{path.relative_to(root)}: unexpected CR line endings")
    # Enforce useful documentation rather than an exact count of skills.
    for p in ("docs/skill-map.md", "docs/provenance.md", "CONTRIBUTING.md", "LICENSE"):
        if not (root / p).exists():
            problems.append(f"Missing essential file: {p}")
    return problems, len(skills), len(files)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    issues, skills, markdown = check(root)
    if issues:
        for issue in issues:
            print("ERROR:", issue, file=sys.stderr)
        print(f"Failed: {len(issues)} issue(s)", file=sys.stderr)
        return 1
    print(f"OK: {skills} skills, {markdown} Markdown files; metadata and local links valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
