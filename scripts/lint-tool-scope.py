#!/usr/bin/env python3
"""Lint plugin.json tool scopes — flag over-granted permissions."""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tools that require explicit justification
HIGH_RISK_TOOLS = {
    'execute_code',
    'run_command',
    'shell',
    'delete_file',
    'send_email',
    'browser_navigate',
}

# Tools that orchestrators in managed-agent cookbooks must NOT have
ORCHESTRATOR_BLOCKED = {
    'write_file',
    'mcp_slack',
    'mcp_ironclad',
    'mcp_docusign',
    'mcp_imanage',
    'mcp_everlaw',
}

ERRORS = []
WARNINGS = []


def err(msg):
    ERRORS.append(msg)
    print(f"  ✗ ERROR: {msg}", file=sys.stderr)


def warn(msg):
    WARNINGS.append(msg)
    print(f"  ⚠ WARN: {msg}")


def ok(msg):
    print(f"  ✓ {msg}")


def lint_plugin(path):
    with open(path) as f:
        data = json.load(f)

    context = path.replace(ROOT, '')
    tools = set(data.get('tools', []))

    for tool in tools:
        if tool in HIGH_RISK_TOOLS:
            err(f"{context}: high-risk tool '{tool}' declared — must be justified in PR description")

    ok(f"{context} tool scope ok ({len(tools)} tools)")


def lint_cookbooks():
    cookbook_dir = os.path.join(ROOT, 'managed-agent-cookbooks')
    if not os.path.exists(cookbook_dir):
        return

    for cookbook in os.listdir(cookbook_dir):
        orchestrator_path = os.path.join(cookbook_dir, cookbook, 'orchestrator.json')
        if not os.path.exists(orchestrator_path):
            continue

        with open(orchestrator_path) as f:
            data = json.load(f)

        tools = set(data.get('tools', []))
        for tool in tools:
            if tool in ORCHESTRATOR_BLOCKED:
                err(f"cookbook/{cookbook}/orchestrator.json: orchestrators must not have '{tool}' — move write/MCP ops to subagent leaf")


def main():
    print("=== Claude for Legal — Tool Scope Lint ===\n")

    print("Linting plugin tool scopes...")
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if '.claude-plugin' in dirpath and 'plugin.json' in filenames:
            lint_plugin(os.path.join(dirpath, 'plugin.json'))

    print("\nLinting managed-agent cookbook scopes...")
    lint_cookbooks()

    print()
    if ERRORS:
        print(f"{len(ERRORS)} error(s), {len(WARNINGS)} warning(s).", file=sys.stderr)
        sys.exit(1)
    elif WARNINGS:
        print(f"0 errors, {len(WARNINGS)} warning(s). Review before merging.")
    else:
        print("Tool scope lint passed.")


if __name__ == '__main__':
    main()
