#!/usr/bin/env python3

import json
from pathlib import Path

SKILLS_DIR = Path("skills")
errors = []

for metadata_file in SKILLS_DIR.rglob("metadata.json"):
    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        author = metadata.get("author")

        if not isinstance(author, str) or not author.strip():
            errors.append(f"{metadata_file}: missing or invalid author")
        else:
            print(f"✓ {metadata_file}: {author}")

    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"{metadata_file}: {error}")

if errors:
    print("\nAuthor validation failed:")
    for error in errors:
        print(f"✗ {error}")
    raise SystemExit(1)

print("\n✓ All module authors are valid.")
