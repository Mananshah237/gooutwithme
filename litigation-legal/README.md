# litigation-legal

Litigation support plugin for Claude. Handles matter intake, factual chronology building, privilege review, deposition preparation, brief drafting, and claim charting — keyed to your practice area, court mix, and matter management preferences.

## Setup

```
/litigation-legal:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/litigation-legal:cold-start-interview` | Initial setup — learns your practice area, courts, and matter workflow |
| `/litigation-legal:matter-intake` | Structure a new matter — parties, claims, defenses, SOL, discovery needs |
| `/litigation-legal:chronology` | Build a factual chronology from uploaded documents and transcripts |
| `/litigation-legal:privilege-review` | Screen documents for privilege and generate a privilege log |
| `/litigation-legal:deposition-prep` | Generate a deposition outline with topics, anchors, and impeachment hooks |
| `/litigation-legal:brief-draft` | Draft or review a brief section with cited authority |
| `/litigation-legal:claim-chart` | Map legal claims to the factual record for trial or arbitration |

## MCP Connectors

| System | What it enables |
|---|---|
| CourtListener | Live docket monitoring, case law retrieval, and PACER data |
| CoCounsel (Westlaw) | Verified citations and case law research |
| Relativity / Everlaw | Document review integration for privilege screening |
| Google Drive / SharePoint / Box | Direct document access for matter materials |
| Slack | Deadline alerts and matter status updates |

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
