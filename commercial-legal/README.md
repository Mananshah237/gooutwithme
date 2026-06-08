# commercial-legal

In-house commercial contracts plugin for Claude. Automates vendor agreement review, NDA triage, renewal tracking, and escalation routing — against your team's specific playbook.

## Setup

```
/commercial-legal:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/commercial-legal:cold-start-interview` | Initial setup — learns your playbook |
| `/commercial-legal:review` | Route and review any inbound agreement |
| `/commercial-legal:nda-review` | Fast NDA triage |
| `/commercial-legal:renewal-tracker` | Deadline digest for the next 90 days |
| `/commercial-legal:escalation-flagger` | Route a finding to the right approver |
| `/commercial-legal:amendment-history` | Trace changes across a base agreement and amendments |
| `/commercial-legal:matter-workspace` | Manage per-matter context (private practice only) |
| `/commercial-legal:stakeholder-summary` | Business-facing summary of a review |

## Scheduled Agents

| Agent | Schedule | What it does |
|---|---|---|
| renewal-watcher | Weekly | Posts renewal digest to Slack |
| deal-debrief | On-demand | Debrief after a deal closes |
| playbook-monitor | Monthly | Flags agreements that deviate from current playbook |

## MCP Connectors

| System | What it enables |
|---|---|
| Ironclad / Agiloft | Live CLM queries for renewal-tracker and escalation-flagger |
| DocuSign | Signature status and envelope routing |
| Google Drive / SharePoint / Box | Direct document access |
| Slack | Renewal alerts and stakeholder summary posting |
| CoCounsel (Westlaw) | Verified citations in reviews |
| CourtListener | Case law for governing law analysis |

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
