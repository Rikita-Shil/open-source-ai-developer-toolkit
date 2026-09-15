#!/usr/bin/env bash

set -e

echo "Running metadata validation..."
./scripts/validate-metadata.py

echo ""
echo "Running module structure validation..."
./scripts/check-module-structure.py

echo ""
echo "Checking for empty module files..."
./scripts/check-empty-files.py

echo ""
echo "Running metadata tag validation..."
./scripts/check-metadata-tags.py

echo ""
echo "Checking for duplicate module names..."
./scripts/check-duplicate-modules.py

echo ""
echo ""
echo "Running module version validation..."
./scripts/check-module-versions.py

echo ""
echo "Running module category validation..."
./scripts/check-module-categories.py

echo ""
echo "Running module README validation..."
./scripts/check-module-readmes.py

echo "✓ All toolkit validation checks passed."
