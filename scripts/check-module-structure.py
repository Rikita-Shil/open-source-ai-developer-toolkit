#!/usr/bin/env python3

from pathlib import Path

SKILLS_DIR = Path("skills")

REQUIRED_FILES = {
    "README.md",
    "SKILL.md",
    "CHECKLIST.md",
    "examples.md",
    "sample-input.md",
    "metadata.json",
}

errors = []

for skill_file in SKILLS_DIR.rglob("SKILL.md"):
    module_dir = skill_file.parent
    existing_files = {file.name for file in module_dir.iterdir() if file.is_file()}
    missing_files = REQUIRED_FILES - existing_files

    if missing_files:
        errors.append(
            f"{module_dir}: missing {', '.join(sorted(missing_files))}"
        )
    else:
        print(f"✓ {module_dir}")

if errors:
    print("\nModule structure validation failed:")
    for error in errors:
        print(f"✗ {error}")
    raise SystemExit(1)

print("\nAll module structures passed validation.")
