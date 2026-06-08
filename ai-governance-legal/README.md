# ai-governance-legal

AI governance and compliance plugin for Claude. Triages AI use cases against legal frameworks, generates impact assessments, reviews vendor AI systems, and tracks the evolving AI regulatory landscape.

## Setup

```
/ai-governance-legal:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/ai-governance-legal:cold-start-interview` | Initial setup — learns your AI inventory, frameworks, and governance structure |
| `/ai-governance-legal:use-case-triage` | Risk-rate a described AI use case and surface required next steps |
| `/ai-governance-legal:aia-generation` | Generate an AI impact assessment for a specified use case |
| `/ai-governance-legal:vendor-ai-review` | Review vendor AI documentation against your procurement standards |
| `/ai-governance-legal:policy-tracker` | Track AI legislation and regulatory guidance relevant to your operations |

## Scheduled Agents

| Agent | Schedule | What it does |
|---|---|---|
| policy-watcher | Weekly | Surfaces new AI legislation, guidance, and enforcement actions |
| inventory-audit | Quarterly | Prompts review of the AI use-case inventory for accuracy |

## MCP Connectors

| System | What it enables |
|---|---|
| Google Drive / SharePoint / Box | Document access for vendor AI review and policy documents |
| Jira / Linear | Link use-case triage findings to engineering tickets |
| Slack | Policy alerts and governance review notifications |
| CoCounsel (Westlaw) | Verified citations for AI regulatory research |

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
