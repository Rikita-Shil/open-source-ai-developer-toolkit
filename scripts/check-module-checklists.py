#!/usr/bin/env python3

from pathlib import Path

SKILLS_DIR = Path("skills")
errors = []

for skill_file in SKILLS_DIR.rglob("SKILL.md"):
    module_dir = skill_file.parent
    checklist = module_dir / "CHECKLIST.md"

    if not checklist.exists():
        errors.append(f"{module_dir}: CHECKLIST.md is missing")
        continue

    content = checklist.read_text(encoding="utf-8").strip()

    if not content:
        errors.append(f"{checklist}: checklist is empty")
    else:
        print(f"✓ {checklist}")

if errors:
    print("\nChecklist validation failed:")

    for error in errors:
        print(f"✗ {error}")

    raise SystemExit(1)

print("\n✓ All module checklists passed validation.")
