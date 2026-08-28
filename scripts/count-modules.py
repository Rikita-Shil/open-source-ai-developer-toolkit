#!/usr/bin/env python3

from pathlib import Path

SKILLS_DIR = Path("skills")

modules = sorted(
    skill_file.parent
    for skill_file in SKILLS_DIR.rglob("SKILL.md")
)

print(f"Total modules: {len(modules)}")

for module in modules:
    print(f"- {module}")
