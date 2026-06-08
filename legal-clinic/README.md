# legal-clinic

Law school clinic and legal aid plugin for Claude. Supports supervised client intake, legal memo drafting, deadline tracking, and student clinician onboarding — designed for academic clinical programs and nonprofit legal services organizations.

## Setup

```
/legal-clinic:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the practice profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/legal-clinic:cold-start-interview` | Initial setup — learns your clinic's practice areas, jurisdiction, and team |
| `/legal-clinic:client-intake` | Structure a new client matter — facts, legal theories, and conflicts check |
| `/legal-clinic:memo` | Draft a structured legal memorandum (QP, Short Answer, Facts, Analysis, Conclusion) |
| `/legal-clinic:deadlines` | Track filing deadlines, SOL, and court dates across active matters |
| `/legal-clinic:student-ramp` | Onboard a new student clinician with matter queue and initial assignments |

## MCP Connectors

| System | What it enables |
|---|---|
| CourtListener | Free case law and docket access for student research |
| Google Drive | Shared matter files and memo storage |
| Google Calendar | Deadline and hearing date synchronization |
| Slack | Supervising attorney notifications and student check-ins |

## Disclaimer

Every output is a draft for review by a supervising attorney — not legal advice. The supervising attorney reviews, verifies, and takes professional responsibility for all work product before it is provided to clients or filed with any tribunal. Student clinicians must obtain attorney approval before relying on any output.
