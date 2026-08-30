#!/usr/bin/env python3

from pathlib import Path

SKILLS_DIR = Path("skills")

REQUIRED_FILES = [
    "README.md",
    "SKILL.md",
    "CHECKLIST.md",
    "examples.md",
    "sample-input.md",
    "metadata.json",
]

empty_files = []

for skill_file in SKILLS_DIR.rglob("SKILL.md"):
    module_dir = skill_file.parent

    for filename in REQUIRED_FILES:
        file_path = module_dir / filename

        if file_path.exists() and not file_path.read_text(encoding="utf-8").strip():
            empty_files.append(file_path)

if empty_files:
    print("Empty module files found:")

    for file_path in empty_files:
        print(f"✗ {file_path}")

    raise SystemExit(1)

print("✓ No empty module files found.")
