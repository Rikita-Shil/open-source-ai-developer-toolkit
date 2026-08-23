#!/usr/bin/env bash

set -e

echo "Running metadata validation..."
./scripts/validate-metadata.py

echo ""
echo "Running module structure validation..."
./scripts/check-module-structure.py

echo ""
echo "✓ All toolkit validation checks passed."
