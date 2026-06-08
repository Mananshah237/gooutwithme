# law-student

Bar and exam prep plugin for Claude. Supports Socratic drilling, IRAC coaching, case briefing, bar exam practice, and exam performance forecasting — calibrated to your law school, year, and bar jurisdiction.

## Setup

```
/law-student:cold-start-interview
```

Takes 10-15 minutes. Every other skill depends on the study profile it creates.

## Skills

| Command | What it does |
|---|---|
| `/law-student:cold-start-interview` | Initial setup — learns your school, year, bar jurisdiction, and study preferences |
| `/law-student:socratic-drill` | Escalating Socratic dialogue on a rule, doctrine, or case |
| `/law-student:irac-practice` | Grade and coach an IRAC answer — spots rule gaps and analysis weaknesses |
| `/law-student:bar-prep` | Generate MBE questions, MEE prompts, or MPT tasks for your jurisdiction |
| `/law-student:case-brief` | Produce a structured case brief for any cited decision |
| `/law-student:exam-forecast` | Analyze a syllabus and prior exams to forecast high-probability exam issues |

## MCP Connectors

| System | What it enables |
|---|---|
| CourtListener | Free case law access for case brief and research tasks |
| Google Drive | Upload syllabi, prior exams, and outlines for analysis |

## Disclaimer

This plugin supports study and exam preparation. It is not a substitute for attending class, reading primary materials, or working with faculty. Bar exam outputs are study tools — verify rules against official bar prep materials and your jurisdiction's current law before relying on them.
