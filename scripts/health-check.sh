#!/usr/bin/env bash

set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=================================="
echo " Open Source AI Toolkit Health Check"
echo "=================================="
echo ""

MODULE_COUNT=$(find skills -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
echo "Modules detected: $MODULE_COUNT"
echo ""

checks_passed=0
checks_failed=0

run_check() {
    local label="$1"
    shift

    echo "----------------------------------"
    echo "$label"
    echo "----------------------------------"

    if "$@"; then
        echo "✓ PASS: $label"
        checks_passed=$((checks_passed + 1))
    else
        echo "✗ FAIL: $label"
        checks_failed=$((checks_failed + 1))
    fi

    echo ""
}

run_check "Toolkit validation" ./scripts/validate-all.sh
run_check "Metadata unit tests" python3 -m unittest discover -s tests -v

echo "=================================="
echo " Health Check Summary"
echo "=================================="
echo "Checks passed: $checks_passed"
echo "Checks failed: $checks_failed"

if [ "$checks_failed" -eq 0 ]; then
    echo ""
    echo "✓ Toolkit is healthy."
    exit 0
else
    echo ""
    echo "✗ Toolkit health check found issues."
    exit 1
fi
