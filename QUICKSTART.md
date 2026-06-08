# Claude for Legal — Quick Start

Get up and running in about 60 seconds.

## Step 1: Install

### Claude Cowork (easiest)
1. Install Claude Desktop
2. Click **Customize → Browse plugins**
3. Search for `claude-for-legal`
4. Click **Install** next to your practice area plugin
5. **Important:** choose **user scope** (not project scope) — project scope blocks the plugin from reading files outside the project folder

### Claude Code
```bash
/plugin marketplace add https://github.com/anthropics/claude-for-legal
/plugin install commercial-legal@claude-for-legal
```

## Step 2: Choose your plugin

| I work in... | Install this |
|---|---|
| In-house contracts / vendor agreements | `commercial-legal` |
| Privacy / data protection | `privacy-legal` |
| Product / go-to-market | `product-legal` |
| M&A / corporate | `corporate-legal` |
| Employment / HR legal | `employment-legal` |
| Regulatory / compliance monitoring | `regulatory-legal` |
| AI policy / AI governance | `ai-governance-legal` |
| IP / patents / trademarks | `ip-legal` |
| Litigation / disputes | `litigation-legal` |
| Law school clinic | `legal-clinic` |
| Law student | `law-student` |

## Step 3: Run setup

```
/commercial-legal:cold-start-interview
```

Replace `commercial-legal` with whichever plugin you installed.

The interview takes 10-15 minutes and learns your specific playbook. Every skill in the plugin reads the practice profile it creates — skip it and you'll get generic outputs.

## Step 4: Connect research tools (optional but recommended)

```
/commercial-legal:cold-start-interview --check-integrations
```

Tests which MCP connectors are responding. Connected research tools (Westlaw, CourtListener) enable verified citations instead of `[model knowledge — verify]` tags.

## Step 5: Run your first skill

```
/commercial-legal:review
```

Paste or point at an agreement. The skill reads your playbook and produces a deviation analysis.

---

## Troubleshooting

**Command not found**
Restart Claude Desktop / Claude Code after installing. Plugin commands register on restart.

**File access errors**
Reinstall as user scope. Project scope restricts file access to the project directory only.

**Citations tagged [model knowledge — verify]**
No research connector is responding. Run `--check-integrations` to diagnose. Outputs are still useful — citations just need manual verification.

**Setup interview output is wrong**
Edit the practice profile directly: `~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md`. Changes take effect immediately.

---

## Managed Agents

Deploy headless agents for scheduled workflows:

```bash
export ANTHROPIC_API_KEY=sk-ant-...

# Validate all cookbooks
bash scripts/test-cookbooks.sh

# Deploy an agent
scripts/deploy-managed-agent.sh renewal-watcher
scripts/deploy-managed-agent.sh docket-watcher
scripts/deploy-managed-agent.sh reg-monitor
```

---

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
