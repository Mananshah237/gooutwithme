# product-legal

In-house product law plugin for Claude. Covers pre-launch legal review, marketing claims clearance, feature triage, and terms of service analysis — against your team's specific product playbook and regulatory footprint.

## Setup

```
/product-legal:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/product-legal:cold-start-interview` | Initial setup — learns your product lines, risk tolerance, and review cadence |
| `/product-legal:launch-review` | Structured legal checklist before a product or feature ships |
| `/product-legal:marketing-claims-review` | FTC compliance and substantiation review for advertising and copy |
| `/product-legal:feature-triage` | Quick risk triage for a described feature — flags regulated areas |
| `/product-legal:tos-review` | Review or draft terms of service, EULAs, and acceptable use policies |

## MCP Connectors

| System | What it enables |
|---|---|
| Google Drive / SharePoint / Box | Direct document access for policy and TOS review |
| Jira / Linear | Pull feature specs and link legal findings to tickets |
| Slack | Launch-gate alerts and review-complete notifications |
| CoCounsel (Westlaw) | Verified citations for FTC guidance and consumer protection research |

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
