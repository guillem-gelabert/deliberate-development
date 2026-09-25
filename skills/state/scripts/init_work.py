#!/usr/bin/env python3
"""Initialize a deliberate-development task workspace without overwriting anything.

Usage:
    init_work.py <task-id> [--root .work] [--fill-missing]

- No task files present: creates all five from assets/templates/.
- All five present: changes nothing (already initialized).
- Some present: refuses, because a partial workspace is ambiguous state.
  Pass --fill-missing to create only the missing files from templates.

Existing files are never modified.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

FILES = ["STATUS.md", "SPEC.md", "CURRENT_STATE.md", "ARCHITECTURE.md", "PLAN.md"]


def task_id(value: str) -> str:
    value = value.strip()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", value):
        raise argparse.ArgumentTypeError(
            "task id must start with a letter or digit and contain only letters, digits, '.', '_' and '-'"
        )
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("task_id", type=task_id)
    parser.add_argument("--root", default=".work", help="workspace root directory (default: .work)")
    parser.add_argument("--fill-missing", action="store_true",
                        help="in a partial workspace, create only the missing files")
    args = parser.parse_args()

    templates = Path(__file__).resolve().parent.parent / "assets" / "templates"
    missing_templates = [n for n in FILES if not (templates / n).is_file()]
    if missing_templates:
        print(f"ERROR: templates not found in {templates}: {', '.join(missing_templates)}", file=sys.stderr)
        return 1

    target = Path(args.root) / args.task_id
    if target.exists() and not target.is_dir():
        print(f"ERROR: {target} exists and is not a directory", file=sys.stderr)
        return 1

    present = [n for n in FILES if (target / n).exists()]
    absent = [n for n in FILES if n not in present]

    if not absent:
        print(f"Workspace already initialized: {target} (no files changed)")
        return 0
    if present and not args.fill_missing:
        print(f"ERROR: partial workspace at {target}", file=sys.stderr)
        print(f"  present: {', '.join(present)}", file=sys.stderr)
        print(f"  missing: {', '.join(absent)}", file=sys.stderr)
        print("  Inspect it first. Re-run with --fill-missing to create only the missing files.", file=sys.stderr)
        return 2

    target.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    for name in absent:
        text = (templates / name).read_text(encoding="utf-8").replace("{{DATE}}", today)
        with open(target / name, "x", encoding="utf-8") as fh:  # "x" never overwrites
            fh.write(text)

    print(f"Workspace: {target}")
    print(f"Created: {', '.join(absent)}")
    if present:
        print(f"Preserved: {', '.join(present)}")
        if "STATUS.md" in absent:
            print("NOTE: STATUS.md was created from the template; update it to match the existing files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
