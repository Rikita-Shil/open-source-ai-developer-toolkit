#!/usr/bin/env python3

import sys
from pathlib import Path

SKILLS_DIR = Path("skills")

modules = list(SKILLS_DIR.rglob("SKILL.md"))

categories = {
    module.parent.parent.name
    for module in modules
}

if "--help" in sys.argv:
    print("Open Source AI Developer Toolkit Summary")
    print()
    print("Usage:")
    print("  ./scripts/toolkit-summary.py")
    print("  ./scripts/toolkit-summary.py --count-only")
    print("  ./scripts/toolkit-summary.py --categories-only")
    print("  ./scripts/toolkit-summary.py --help")
    raise SystemExit(0)

unknown_args = [
    arg for arg in sys.argv[1:]
    if arg not in {"--count-only", "--categories-only"}
]

if unknown_args:
    print(f"Error: unknown option(s): {' '.join(unknown_args)}")
    print("Run with --help to see available options.")
    raise SystemExit(1)

if "--count-only" in sys.argv:
    print(len(modules))
    raise SystemExit(0)

if "--categories-only" in sys.argv:
    for category in sorted(categories):
        print(category.replace("-", " ").title())
    raise SystemExit(0)

print("Open Source AI Developer Toolkit")
print("--------------------------------")
print(f"Modules: {len(modules)}")
print(f"Categories: {len(categories)}")

print("\nAvailable categories:")

for category in sorted(categories):
    print(f"- {category.replace('-', ' ').title()}")
