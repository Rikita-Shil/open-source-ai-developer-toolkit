#!/usr/bin/env python3

from pathlib import Path

SKILLS_DIR = Path("skills")
errors = []

for skill_file in SKILLS_DIR.rglob("SKILL.md"):
    module_dir = skill_file.parent
    readme = module_dir / "README.md"

    if not readme.exists():
        errors.append(f"{module_dir}: README.md is missing")
        continue

    content = readme.read_text(encoding="utf-8").strip()

    if len(content) < 50:
        errors.append(f"{readme}: README content is too short")
    else:
        print(f"✓ {readme}")

if errors:
    print("\nREADME validation failed:")

    for error in errors:
        print(f"✗ {error}")

    raise SystemExit(1)

print("\n✓ All module README files passed validation.")
