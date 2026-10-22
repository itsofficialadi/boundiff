#!/usr/bin/env python3
"""Preview or copy Boundiff into an existing project.

Never overwrites, deletes, executes skill scripts, or touches Git state.
"""

import argparse
from pathlib import Path
import re
import shutil
import sys

SOURCE = Path(__file__).resolve().parents[1]
SKILLS = SOURCE / ".agents" / "skills"
POLICIES = {
    "default": SOURCE / "AGENTS.md",
    "minimal": SOURCE / "templates" / "minimal" / "AGENTS.md",
    "startup": SOURCE / "templates" / "startup" / "AGENTS.md",
    "security-sensitive": SOURCE / "templates" / "security-sensitive" / "AGENTS.md",
}


def build_plan(target, policy, selection):
    names = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    if selection == "all":
        picked = names
    else:
        picked = [x.strip() for x in selection.split(",") if x.strip()]
        if len(set(picked)) != len(picked):
            raise ValueError("Skill names must not be repeated")
        bad = [x for x in picked if x not in names or not re.fullmatch(r"[a-z][a-z0-9-]*", x)]
        if bad:
            raise ValueError("Unknown skills: " + ", ".join(bad) + ". Run --list to see options.")
    jobs = []
    if policy != "none":
        jobs.append((POLICIES[policy], target / "AGENTS.md"))
    jobs.extend((SKILLS / name, target / ".agents" / "skills" / name) for name in picked)
    return jobs


def safe_destination(target, destination):
    # No destination may point through a symlink, including an existing skill dir.
    if target.is_symlink():
        raise ValueError(f"Target is a symlink: {target}")
    relative = destination.relative_to(target)
    path = target
    for piece in relative.parts:
        path = path / piece
        if path.is_symlink():
            raise ValueError(f"Refusing symlink destination: {path}")


def source_has_symlinks(path):
    if path.is_symlink():
        return True
    if path.is_dir():
        return any(p.is_symlink() for p in path.rglob("*"))
    return False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, help="Existing target project directory")
    parser.add_argument("--preset", choices=sorted(POLICIES), default="default", help="Baseline AGENTS.md policy")
    parser.add_argument("--policy", choices=("default", "minimal", "startup", "security-sensitive", "none"),
                        help="Alias for --preset, or 'none' to keep existing AGENTS.md")
    parser.add_argument("--skills", default="surgical-change,bug-fix-verification,independent-review",
                        help="Comma-separated skill names or 'all'")
    parser.add_argument("--apply", action="store_true", help="Copy after a conflict-free preflight; otherwise preview only")
    parser.add_argument("--list", action="store_true", help="List available skills")
    args = parser.parse_args(argv)
    if args.list:
        for p in sorted(SKILLS.iterdir()):
            if p.is_dir():
                print(p.name)
        return 0
    if args.target is None or not args.target.is_dir():
        parser.error("--target must be an existing project directory")
    target = args.target.absolute()
    policy = args.policy if args.policy is not None else args.preset
    try:
        jobs = build_plan(target, policy, args.skills)
        if not jobs:
            raise ValueError("Nothing selected")
        conflicts = []
        for src, dest in jobs:
            if not src.exists() or source_has_symlinks(src):
                raise ValueError(f"Invalid or symlinked source: {src}")
            safe_destination(target, dest)
            if dest.exists():
                conflicts.append(dest)
        if conflicts:
            print("Installation blocked. Existing paths would be overwritten:", file=sys.stderr)
            for dest in conflicts:
                print(f"  {dest}", file=sys.stderr)
            print("Merge those files manually, or rerun with --policy none and selected nonconflicting skills.", file=sys.stderr)
            return 2
        print(f"Target: {target}")
        print("Mode: " + ("COPY" if args.apply else "PREVIEW (no changes)"))
        for src, dest in jobs:
            print(f"  {src.relative_to(SOURCE)} -> {dest.relative_to(target)}")
        if not args.apply:
            print("Run the same command with --apply to copy these paths.")
            return 0
        for src, dest in jobs:
            dest.parent.mkdir(parents=True, exist_ok=True)
            # Recheck immediately before writing rather than overwriting on a race.
            safe_destination(target, dest)
            if dest.exists():
                raise ValueError(f"Destination appeared during copy: {dest}")
            if src.is_dir():
                shutil.copytree(src, dest, dirs_exist_ok=False)
            else:
                with src.open("rb") as inp, dest.open("xb") as out:
                    shutil.copyfileobj(inp, out)
        print("Installed. Review the new instructions in the target repository before using them.")
        return 0
    except (OSError, ValueError) as e:
        print(f"Installation stopped: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
