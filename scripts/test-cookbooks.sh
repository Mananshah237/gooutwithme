#!/usr/bin/env bash
# Validate all managed-agent cookbooks
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COOKBOOKS_DIR="$ROOT/managed-agent-cookbooks"
ERRORS=0

echo "=== Claude for Legal — Cookbook Test ==="
echo ""

for cookbook in "$COOKBOOKS_DIR"/*/; do
  name=$(basename "$cookbook")
  echo "Testing cookbook: $name"

  # Check required files
  for required in "README.md" "agent.json"; do
    if [[ ! -f "$cookbook/$required" ]]; then
      echo "  ✗ Missing required file: $required"
      ((ERRORS++))
    else
      echo "  ✓ $required present"
    fi
  done

  # Validate agent.json
  if [[ -f "$cookbook/agent.json" ]]; then
    if python3 -c "import json; json.load(open('$cookbook/agent.json'))" 2>/dev/null; then
      echo "  ✓ agent.json is valid JSON"
    else
      echo "  ✗ agent.json is invalid JSON"
      ((ERRORS++))
    fi
  fi

  echo ""
done

echo "Running schema validation..."
python3 "$ROOT/scripts/validate.py"

echo ""
echo "Running tool-scope lint..."
python3 "$ROOT/scripts/lint-tool-scope.py"

echo ""
if [[ $ERRORS -gt 0 ]]; then
  echo "Found $ERRORS error(s) in cookbook validation."
  exit 1
else
  echo "All cookbooks validated successfully."
fi
