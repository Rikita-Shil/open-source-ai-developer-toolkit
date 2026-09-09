#!/usr/bin/env python3

import json
import re
from pathlib import Path

SKILLS_DIR = Path("skills")
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")

errors = []

for metadata_file in SKILLS_DIR.rglob("metadata.json"):
    try:
        with metadata_file.open(encoding="utf-8") as file:
            metadata = json.load(file)

        version = metadata.get("version")

        if not isinstance(version, str) or not VERSION_PATTERN.match(version):
            errors.append(
                f"{metadata_file}: invalid version '{version}'"
            )
        else:
            print(f"✓ {metadata_file}: {version}")

    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"{metadata_file}: {error}")

if errors:
    print("\nModule version validation failed:")

    for error in errors:
        print(f"✗ {error}")

    raise SystemExit(1)

print("\n✓ All module versions are valid.")
