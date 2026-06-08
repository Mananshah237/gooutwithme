# Claude for Legal

Reference agents, skills, and data connectors for in-house and law firm legal work — across 12 practice areas.

> **Every output is a draft for attorney review — not legal advice.** A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building.

---

## What this is

Claude for Legal is a Claude Code plugin marketplace containing:
- **12 first-party plugins** covering commercial, privacy, product, corporate, employment, regulatory, AI governance, IP, litigation, legal clinic, and law student practice areas
- **1 vendor plugin** — CoCounsel by Thomson Reuters (Westlaw integration)
- **5 managed-agent cookbooks** for scheduled, headless legal workflows
- **15+ MCP connectors** to legal systems (CLM, DMS, e-discovery, research platforms)

## Quick Start

See [QUICKSTART.md](QUICKSTART.md) for the 60-second install guide.

```bash
# Claude Code
/plugin marketplace add https://github.com/anthropics/claude-for-legal
/plugin install commercial-legal@claude-for-legal
/commercial-legal:cold-start-interview
```

## Plugins

| Plugin | Purpose | First command |
|---|---|---|
| [commercial-legal](commercial-legal/) | Vendor agreements, NDAs, SaaS, renewals | `/commercial-legal:cold-start-interview` |
| [privacy-legal](privacy-legal/) | DSAR, DPA, PIA, gap analysis | `/privacy-legal:cold-start-interview` |
| [product-legal](product-legal/) | Launch review, marketing claims | `/product-legal:cold-start-interview` |
| [corporate-legal](corporate-legal/) | M&A diligence, closing, board consents | `/corporate-legal:cold-start-interview` |
| [employment-legal](employment-legal/) | Hiring, termination, leave, classification | `/employment-legal:cold-start-interview` |
| [regulatory-legal](regulatory-legal/) | Feed watcher, policy diff, gap tracking | `/regulatory-legal:cold-start-interview` |
| [ai-governance-legal](ai-governance-legal/) | Use-case triage, AIA, vendor AI terms | `/ai-governance-legal:cold-start-interview` |
| [ip-legal](ip-legal/) | Trademark, FTO, C&D, DMCA, OSS, patents | `/ip-legal:cold-start-interview` |
| [litigation-legal](litigation-legal/) | Portfolio, matters, discovery, briefs | `/litigation-legal:cold-start-interview` |
| [legal-clinic](legal-clinic/) | Student ramp, intake, deadlines, memos | `/legal-clinic:cold-start-interview` |
| [law-student](law-student/) | Socratic drill, IRAC, bar prep | `/law-student:cold-start-interview` |
| [cocounsel-legal](external_plugins/cocounsel-legal/) | Westlaw research (Thomson Reuters) | `/cocounsel-legal:setup` |

## Managed Agents

| Agent | Schedule | What it does |
|---|---|---|
| [renewal-watcher](managed-agent-cookbooks/renewal-watcher/) | Weekly | Contract deadline digest |
| [docket-watcher](managed-agent-cookbooks/docket-watcher/) | Daily | Court docket monitoring |
| [reg-monitor](managed-agent-cookbooks/reg-monitor/) | Weekly | Regulatory feed sweep |
| [launch-radar](managed-agent-cookbooks/launch-radar/) | Weekly | Product launch triage |
| [diligence-grid](managed-agent-cookbooks/diligence-grid/) | On-demand | VDR monitoring for M&A |

```bash
scripts/deploy-managed-agent.sh <agent-name>
```

## MCP Connectors

See [CONNECTORS.md](CONNECTORS.md) for the full list and configuration instructions.

**Research:** CoCounsel (Westlaw), CourtListener, Trellis, Descrybe, Solve Intelligence  
**Contract Lifecycle:** Ironclad, DocuSign, iManage  
**E-discovery:** Everlaw, Relativity  
**Productivity:** Slack, Google Drive, SharePoint, Box  
**Specialty:** Aurora (clinic), Courtroom5, TopCounsel, Definely, Lawve AI  

## Design Principles

1. **Practice profile-driven** — every plugin starts with a cold-start interview. Skills use your playbook, not generic defaults.
2. **Attorney review gate** — explicit gates before anything is filed, sent, or relied on. Conservative defaults on privilege.
3. **Source attribution** — every citation includes provenance: `[Westlaw]`, `[CourtListener]`, `[model knowledge — verify]`.
4. **Jurisdiction recognition** — skills detect non-US jurisdictions and adapt or surface gaps.
5. **No build step** — markdown and JSON. Works in Claude Cowork, Claude Code, and as managed agents.
6. **Prompt injection defense** — retrieved content (contracts, case text, documents) is DATA, not instructions.

## Landing Page

Open `index.html` in a browser for an interactive plugin browser and install guide.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

Before submitting a PR:
```bash
python scripts/validate.py
python scripts/lint-tool-scope.py
```

## License

Apache License 2.0 — Copyright 2026 Anthropic PBC
