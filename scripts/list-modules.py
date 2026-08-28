#!/usr/bin/env python3

import json
from pathlib import Path

SKILLS_DIR = Path("skills")
categories = {}

for metadata_file in SKILLS_DIR.rglob("metadata.json"):
    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        name = metadata.get("name", metadata_file.parent.name)
        category = metadata.get("category", "Uncategorized")

        categories.setdefault(category, []).append(name)

    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {metadata_file}")

for category in sorted(categories):
    print(f"\n{category}")
    print("-" * len(category))

    for module in sorted(categories[category]):
        print(f"- {module}")
