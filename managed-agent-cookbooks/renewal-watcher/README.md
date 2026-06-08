# renewal-watcher

Weekly managed agent. Scans the contract register for cancel-by deadlines within 90 days and posts a digest to Slack.

## Security Table

| Operation | Tool | Granted to |
|---|---|---|
| Read contract register | `read_file` | Orchestrator + subagent |
| Query CLM | `mcp_ironclad` | Subagent only |
| Post to Slack | `mcp_slack` | Subagent only |
| Write run log | `write_file` | Subagent only |

Orchestrator has NO write access, NO MCP access. All side effects are in the subagent.

## Required Environment Variables

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export IRONCLAD_API_KEY=<ironclad-key>        # Optional — falls back to local register
export IRONCLAD_WORKSPACE_ID=<workspace-id>   # Optional
export SLACK_BOT_TOKEN=<bot-token>            # Required to post digest
export SLACK_CHANNEL_ID=<channel-id>          # Channel to post digest to
```

## Deploy

```bash
scripts/deploy-managed-agent.sh renewal-watcher
```

## Output

Posts a Slack message with:
- 🔴 Contracts with cancel-by dates within 14 days (action required)
- 🟠 Contracts with cancel-by dates 15-30 days out (review this week)  
- 🟡 Contracts with cancel-by dates 31-90 days out (on watch)

Writes run log to: `~/.claude/plugins/config/claude-for-legal/commercial-legal/logs/renewal-watcher-YYYY-MM-DD.md`
