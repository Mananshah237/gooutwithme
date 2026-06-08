#!/usr/bin/env python3
"""Validate marketplace.json and all plugin.json files for schema conformance."""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []


def err(msg):
    ERRORS.append(msg)
    print(f"  ✗ {msg}", file=sys.stderr)


def ok(msg):
    print(f"  ✓ {msg}")


def validate_name(name, context):
    import re
    if not re.match(r'^[a-z0-9-]{2,64}$', name):
        err(f"{context}: name '{name}' must be alphanumeric + hyphens, 2-64 chars")


def validate_description(desc, context):
    if not (10 <= len(desc) <= 2000):
        err(f"{context}: description length {len(desc)} outside 10-2000 range")
    if any(c in desc for c in ['​', '﻿', '‎', '‏']):
        err(f"{context}: description contains hidden Unicode")


def validate_marketplace():
    path = os.path.join(ROOT, '.claude-plugin', 'marketplace.json')
    if not os.path.exists(path):
        err(f"marketplace.json not found at {path}")
        return

    with open(path) as f:
        data = json.load(f)

    print("\nValidating marketplace.json...")
    validate_name(data.get('name', ''), 'marketplace')
    validate_description(data.get('description', ''), 'marketplace')

    names = set()
    for plugin in data.get('plugins', []):
        name = plugin.get('name', '')
        if name in names:
            err(f"marketplace: duplicate plugin name '{name}'")
        names.add(name)
        validate_name(name, f"marketplace plugin '{name}'")
        validate_description(plugin.get('description', ''), f"marketplace plugin '{name}'")

        plugin_json_path = os.path.join(ROOT, plugin.get('path', ''), '.claude-plugin', 'plugin.json')
        if not os.path.exists(plugin_json_path):
            err(f"plugin.json not found for '{name}' at {plugin_json_path}")
        else:
            ok(f"plugin.json found for '{name}'")


def validate_plugin_jsons():
    print("\nValidating plugin.json files...")
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if '.claude-plugin' in dirpath and 'plugin.json' in filenames:
            path = os.path.join(dirpath, 'plugin.json')
            with open(path) as f:
                data = json.load(f)

            context = path.replace(ROOT, '')
            validate_name(data.get('name', ''), context)
            validate_description(data.get('description', ''), context)

            for skill in data.get('skills', []):
                skill_path = os.path.join(os.path.dirname(dirpath), skill.get('path', ''))
                if not os.path.exists(skill_path):
                    err(f"{context}: skill path not found: {skill_path}")
                else:
                    ok(f"skill '{skill.get('name')}' path ok")

            ok(f"{context} valid")


def main():
    print("=== Claude for Legal — Validation ===")
    validate_marketplace()
    validate_plugin_jsons()

    print()
    if ERRORS:
        print(f"Found {len(ERRORS)} error(s):", file=sys.stderr)
        sys.exit(1)
    else:
        print("All checks passed.")


if __name__ == '__main__':
    main()
