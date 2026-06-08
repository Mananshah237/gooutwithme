# corporate-legal

In-house corporate transactions plugin for Claude. Automates M&A diligence grids, board consent drafting, closing checklists, disclosure schedule population, and entity compliance calendars — against your team's specific deal playbook.

## Setup

```
/corporate-legal:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/corporate-legal:cold-start-interview` | Initial setup — learns your deal playbook and entity roster |
| `/corporate-legal:tabular-review` | Extract key terms from deal documents into a diligence grid |
| `/corporate-legal:closing-checklist` | Generate and track a transaction closing checklist |
| `/corporate-legal:board-consent` | Draft board or unanimous written consent for a corporate action |
| `/corporate-legal:entity-compliance` | Surface upcoming filing deadlines across your entity roster |
| `/corporate-legal:disclosure-schedule` | Draft and populate disclosure schedules keyed to reps and warranties |

## MCP Connectors

| System | What it enables |
|---|---|
| Carta / Cooley GO | Cap table and entity data for diligence and compliance |
| Google Drive / SharePoint / Box | Direct document access for diligence review |
| Slack | Closing checklist updates and deadline alerts |
| CoCounsel (Westlaw) | Verified citations in diligence memos |

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
