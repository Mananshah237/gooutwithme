# claude-for-legal — Development Guide

This repository contains a Claude Code plugin marketplace with twelve first-party legal plugins, one vendor plugin (CoCounsel/Thomson Reuters), and five managed-agent cookbooks.

## Repository Structure

```
claude-for-legal/
├── commercial-legal/          # Vendor agreements, NDAs, SaaS, renewals
├── corporate-legal/           # M&A diligence, closing, board consents
├── employment-legal/          # Hiring, termination, classification, leave
├── privacy-legal/             # DSAR, DPA, PIA, triage, policy monitor
├── product-legal/             # Launch review, marketing claims, triage
├── regulatory-legal/          # Feed watcher, policy diff, gaps, NPRM
├── ai-governance-legal/       # Use-case triage, AIA, vendor review
├── ip-legal/                  # Trademark, FTO, C&D, DMCA, OSS, patent
├── litigation-legal/          # Portfolio, matters, holds, demands, claims
├── legal-clinic/              # Student ramp, intake, deadlines, memos
├── law-student/               # Socratic drilling, IRAC, bar prep
├── legal-builder-hub/         # Community skill discovery & install
├── external_plugins/
│   └── cocounsel-legal/       # Thomson Reuters Westlaw integration
├── managed-agent-cookbooks/
│   ├── diligence-grid/
│   ├── docket-watcher/
│   ├── launch-radar/
│   ├── reg-monitor/
│   └── renewal-watcher/
├── scripts/
│   ├── deploy-managed-agent.sh
│   ├── validate.py
│   ├── orchestrate.py
│   ├── lint-tool-scope.py
│   └── test-cookbooks.sh
├── references/
├── .claude-plugin/
│   └── marketplace.json
├── index.html                 # Landing page
├── style.css
├── script.js
├── QUICKSTART.md
├── README.md
├── CONNECTORS.md
└── CLAUDE.md                  # This file
```

## Per-Plugin Structure

```
<plugin>/
├── .claude-plugin/
│   └── plugin.json
├── CLAUDE.md          # Practice profile template (user-facing)
├── README.md
├── skills/
│   └── <skill-name>/
│       └── SKILL.md
├── agents/            # Scheduled agents (optional)
│   └── <agent-name>.md
└── hooks/             # Pre/post tool hooks (optional)
    └── hooks.json
```

## Pre-PR Validation

Before submitting a PR, run all three checks:

```bash
# 1. Schema validation
claude plugin validate .claude-plugin/marketplace.json
claude plugin validate */. claude-plugin/plugin.json

# 2. Tool-scope linting (prevents over-granted permissions)
python scripts/lint-tool-scope.py

# 3. JSON/YAML syntax
python scripts/validate.py
```

## Key Invariants

- Plugin names: alphanumeric + hyphens, 2–64 characters, no duplicates
- Descriptions: 10–2000 characters
- `marketplace.json` must stay in sync with individual `plugin.json` files
- Vendor-maintained content in `external_plugins/` — do not edit without TR approval
- Cookbook orchestrators receive read-only tools; MCP and write operations belong to subagent leaves
- Plugin `CLAUDE.md` is a user-facing template — treat as user-facing docs, not project context

## Conventions

- 2-space indentation, final newlines, no trailing whitespace
- Canonical skill names in documentation — short forms break user commands
- README security tables must accurately reflect actual YAML permissions
- Every skill must declare its tool scope in `plugin.json`

## Landing Page

The `index.html` / `style.css` / `script.js` files are a static landing page for the plugin marketplace. No build step. Open in a browser directly or deploy to GitHub Pages.
