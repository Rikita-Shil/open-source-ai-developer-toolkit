#!/usr/bin/env python3

from pathlib import Path

SKILLS_DIR = Path("skills")

modules = list(SKILLS_DIR.rglob("SKILL.md"))

categories = {
    module.parent.parent.name
    for module in modules
}

print("Open Source AI Developer Toolkit")
print("--------------------------------")
print(f"Modules: {len(modules)}")
print(f"Categories: {len(categories)}")

print("\nAvailable categories:")

for category in sorted(categories):
    print(f"- {category.replace('-', ' ').title()}")
