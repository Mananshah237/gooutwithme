# employment-legal

In-house employment law plugin for Claude. Supports termination and hiring reviews, worker classification analysis, leave tracking, and separation agreement drafting — against your team's specific HR playbook and jurisdiction mix.

## Setup

```
/employment-legal:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/employment-legal:cold-start-interview` | Initial setup — learns your HR playbook and jurisdiction mix |
| `/employment-legal:termination-review` | Review a proposed termination for legal risk and documentation gaps |
| `/employment-legal:hiring-review` | Screen offer letters and job postings against applicable law |
| `/employment-legal:leave-tracker` | Track leave requests against FMLA and state leave laws |
| `/employment-legal:classification-check` | Assess employee vs. contractor classification risk |
| `/employment-legal:separation-agreement` | Draft a separation agreement and release |

## MCP Connectors

| System | What it enables |
|---|---|
| Workday / BambooHR / Rippling | Live headcount and leave data for tracking |
| Google Drive / SharePoint / Box | Direct document access for policy and agreement review |
| Slack | Deadline alerts for leave return dates and WARN notice windows |
| CoCounsel (Westlaw) | Verified citations for jurisdiction-specific research |

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
