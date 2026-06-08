---
name: renewal-watcher
type: managed-agent
schedule: weekly
description: Weekly scan of contract register for cancel-by deadlines within 90 days
cookbook: managed-agent-cookbooks/renewal-watcher/
tools:
  orchestrator: [read_file]
  subagent: [read_file, write_file, mcp_ironclad, mcp_slack]
---

# Renewal Watcher — Managed Agent

A headless, scheduled agent that runs the renewal-tracker skill weekly and posts a digest to the configured Slack channel.

## Trigger

Runs weekly on Monday at 08:00 local time (configured in deployment).

## Orchestrator

The orchestrator reads the practice profile and the contract register, then delegates to the subagent.

Read-only tools only. No write operations, no MCP writes.

## Subagent

The subagent:
1. Queries the CLM for contracts with cancel-by dates within 90 days
2. Runs the renewal-tracker logic
3. Formats the digest per the profile's house style
4. Posts to the configured Slack channel
5. Writes a run log to `~/.claude/plugins/config/claude-for-legal/commercial-legal/logs/renewal-watcher-YYYY-MM-DD.md`

## Deploy

```bash
scripts/deploy-managed-agent.sh renewal-watcher
```

## Security

Subagent has write access to Slack (post only) and the log directory. It does not have access to: email, calendar, CLM write operations, or any system outside the declared tool scope. See `managed-agent-cookbooks/renewal-watcher/` for the full security table.
