# ip-legal

Intellectual property plugin for Claude. Supports trademark clearance, freedom-to-operate triage, cease-and-desist drafting, patent claim charting, open-source license scanning, and DMCA compliance — against your IP portfolio and enforcement playbook.

## Setup

```
/ip-legal:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/ip-legal:cold-start-interview` | Initial setup — learns your IP portfolio and enforcement posture |
| `/ip-legal:clearance` | Trademark clearance search and risk assessment for a new mark |
| `/ip-legal:cease-desist` | Draft a cease-and-desist letter for trademark, copyright, or trade secret claims |
| `/ip-legal:claim-chart` | Map patent claims to an accused product in a structured claim chart |
| `/ip-legal:oss-scan` | Review a dependency manifest for license compatibility and copyleft obligations |
| `/ip-legal:dmca` | Draft DMCA takedown notices or counter-notifications |
| `/ip-legal:fto-triage` | Freedom-to-operate triage — identify relevant patents and design-around options |

## MCP Connectors

| System | What it enables |
|---|---|
| USPTO / EUIPO APIs | Live trademark and patent database queries |
| Google Patents | Patent search and prior art retrieval |
| Google Drive / SharePoint / Box | Document access for portfolio review |
| Slack | Enforcement alerts and deadline reminders |
| CoCounsel (Westlaw) | Verified citations for IP research |

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
