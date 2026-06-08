# regulatory-legal

Regulatory monitoring and compliance plugin for Claude. Watches agency dockets, diffs regulation versions, maps compliance gaps, and drafts notice-and-comment responses — keyed to your organization's regulatory universe.

## Setup

```
/regulatory-legal:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/regulatory-legal:cold-start-interview` | Initial setup — learns your agencies, dockets, and compliance calendar |
| `/regulatory-legal:reg-feed-watcher` | Monitor Federal Register and agency dockets for new rules and proposals |
| `/regulatory-legal:policy-diff` | Compare two regulation versions and surface material changes |
| `/regulatory-legal:gaps` | Map your compliance posture against a new or amended regulation |
| `/regulatory-legal:nprm-response` | Draft a notice-and-comment response to a proposed rulemaking |
| `/regulatory-legal:comment-tracker` | Track comment letters submitted and agency response timelines |

## Scheduled Agents

| Agent | Schedule | What it does |
|---|---|---|
| docket-watcher | Daily | Scans configured agency dockets for new publications |
| compliance-calendar | Weekly | Posts upcoming effective dates and comment deadlines |

## MCP Connectors

| System | What it enables |
|---|---|
| Federal Register API | Live docket and rule publication data |
| Regulations.gov | Comment submission and docket monitoring |
| Google Drive / SharePoint | Document access for policy and gap analysis |
| Slack | Regulatory alerts and comment deadline reminders |
| CoCounsel (Westlaw) | Verified citations for regulatory research |

## Disclaimer

Every output is a draft for attorney review — not legal advice. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.
