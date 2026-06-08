#!/usr/bin/env bash
# Deploy a managed agent cookbook
set -euo pipefail

AGENT=${1:-}
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COOKBOOKS_DIR="$ROOT/managed-agent-cookbooks"

usage() {
  echo "Usage: $0 <agent-name>"
  echo ""
  echo "Available agents:"
  ls "$COOKBOOKS_DIR" 2>/dev/null | sed 's/^/  /'
  exit 1
}

if [[ -z "$AGENT" ]]; then
  usage
fi

COOKBOOK="$COOKBOOKS_DIR/$AGENT"
if [[ ! -d "$COOKBOOK" ]]; then
  echo "Error: no cookbook found for '$AGENT' at $COOKBOOK"
  usage
fi

if [[ -z "${ANTHROPIC_API_KEY:-}" ]]; then
  echo "Error: ANTHROPIC_API_KEY is not set"
  echo "  export ANTHROPIC_API_KEY=sk-ant-..."
  exit 1
fi

echo "=== Deploying managed agent: $AGENT ==="

# Validate the cookbook before deploying
echo "→ Validating cookbook..."
python "$ROOT/scripts/validate.py" || {
  echo "Validation failed. Fix errors before deploying."
  exit 1
}

echo "→ Linting tool scopes..."
python "$ROOT/scripts/lint-tool-scope.py" || {
  echo "Tool scope lint failed. Fix errors before deploying."
  exit 1
}

# Load agent config
CONFIG="$COOKBOOK/agent.json"
if [[ ! -f "$CONFIG" ]]; then
  echo "Error: agent.json not found at $CONFIG"
  exit 1
fi

AGENT_NAME=$(python3 -c "import json; d=json.load(open('$CONFIG')); print(d['name'])")
SCHEDULE=$(python3 -c "import json; d=json.load(open('$CONFIG')); print(d.get('schedule', 'manual'))")

echo "→ Agent: $AGENT_NAME"
echo "→ Schedule: $SCHEDULE"

# In a real deployment, this would call the Anthropic Managed Agents API.
# For now, print the deployment plan.
echo ""
echo "Deployment plan:"
echo "  Agent:      $AGENT_NAME"
echo "  Cookbook:   $COOKBOOK"
echo "  Schedule:   $SCHEDULE"
echo "  Model:      claude-opus-4-8"
echo "  Tools:      $(python3 -c "import json; d=json.load(open('$CONFIG')); print(', '.join(d.get('tools', {}).get('subagent', [])))")"
echo ""
echo "To deploy:"
echo "  1. Ensure ANTHROPIC_API_KEY is set"
echo "  2. Ensure MCP connector env vars are set (see $COOKBOOK/README.md)"
echo "  3. Run: claude managed-agents deploy --cookbook $COOKBOOK"
echo ""
echo "=== Done ==="
