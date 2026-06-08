# MCP Connectors

MCP connectors give Claude for Legal plugins access to live legal data — verified citations, CLM records, court dockets, regulatory feeds, and document systems. Each connector is declared in the plugin's `.mcp.json` file.

## Research

### CoCounsel (Thomson Reuters / Westlaw)
- **What it enables:** Westlaw research reports, statute text, case law search, citator checks, secondary sources
- **Tag it produces:** `[Westlaw]`
- **Required for:** Any skill that cites case law or statutes in high-stakes matters
- **Setup:** Install `cocounsel-legal` plugin and run `/cocounsel-legal:setup`
- **MCP name:** `mcp_cocounsel`

### CourtListener
- **What it enables:** Federal and state case law, docket entries, PACER filings, oral arguments
- **Tag it produces:** `[CourtListener]`
- **Required for:** Litigation skills, IP claim charts, docket monitoring
- **Setup:** `COURTLISTENER_API_KEY=<key>` in environment
- **MCP name:** `mcp_courtlistener`

### Trellis
- **What it enables:** State trial court dockets, litigation intelligence
- **Tag it produces:** `[Trellis]`
- **MCP name:** `mcp_trellis`

### Descrybe
- **What it enables:** Patent analytics and prior art search
- **Tag it produces:** `[Descrybe]`
- **Required for:** IP skills — FTO triage, patentability screening
- **MCP name:** `mcp_descrybe`

### Solve Intelligence
- **What it enables:** AI-assisted patent prosecution
- **MCP name:** `mcp_solve_intelligence`

---

## Contract Lifecycle Management

### Ironclad
- **What it enables:** Contract search, metadata, renewal dates, counterparty lookup
- **Required for:** `renewal-tracker`, `escalation-flagger`, `amendment-history`
- **Setup:** `IRONCLAD_API_KEY=<key>` in environment; configure workspace ID in `.mcp.json`
- **MCP name:** `mcp_ironclad`

### Agiloft
- **What it enables:** Contract repository queries, approval workflows
- **MCP name:** `mcp_agiloft`

### DocuSign
- **What it enables:** Envelope status, signature routing, completed document retrieval
- **Required for:** Closing workflows in `corporate-legal`, signature tracking in `commercial-legal`
- **MCP name:** `mcp_docusign`

### iManage
- **What it enables:** Document management, matter-centric file access
- **Required for:** `litigation-legal` matter workspace, `corporate-legal` data room access
- **MCP name:** `mcp_imanage`

---

## E-Discovery

### Everlaw
- **What it enables:** Production set queries, review coding, privilege log generation
- **Required for:** `litigation-legal` privilege review, large document review
- **MCP name:** `mcp_everlaw`

### Relativity
- **What it enables:** Review platform queries, analytics, export
- **MCP name:** `mcp_relativity`

---

## Productivity

### Slack
- **What it enables:** Posting renewal digests, regulatory alerts, escalation notifications, stakeholder summaries
- **Required for:** Managed agents (renewal-watcher, reg-monitor, docket-watcher)
- **Setup:** `SLACK_BOT_TOKEN=<token>` in environment
- **MCP name:** `mcp_slack`
- **Permissions:** `chat:write` (post to configured channels only)

### Google Drive
- **What it enables:** Direct document access, upload of work product
- **MCP name:** `mcp_google_drive`

### Microsoft SharePoint / OneDrive
- **What it enables:** Direct document access, SharePoint library integration
- **MCP name:** `mcp_sharepoint`

### Box
- **What it enables:** Box folder access, document retrieval
- **MCP name:** `mcp_box`

### Linear / Jira / Asana
- **What it enables:** Creating and updating legal review tickets from plugin output
- **MCP names:** `mcp_linear`, `mcp_jira`, `mcp_asana`

---

## Specialty

### Aurora (clinic management)
- **What it enables:** Clinic client records, intake, deadline tracking
- **Required for:** `legal-clinic` plugin
- **MCP name:** `mcp_aurora`

### Courtroom5
- **What it enables:** Pro se litigation support tools
- **MCP name:** `mcp_courtroom5`

### TopCounsel
- **What it enables:** Outside counsel management
- **MCP name:** `mcp_topcounsel`

### Definely
- **What it enables:** Contract clause library and definitions
- **MCP name:** `mcp_definely`

### Lawve AI
- **What it enables:** Legal research augmentation
- **MCP name:** `mcp_lawve`

---

## Configuring Connectors

Each plugin has a `.mcp.json` in its root. Example for commercial-legal:

```json
{
  "mcpServers": {
    "mcp_ironclad": {
      "command": "npx",
      "args": ["-y", "@ironclad/mcp-server"],
      "env": {
        "IRONCLAD_API_KEY": "${IRONCLAD_API_KEY}",
        "IRONCLAD_WORKSPACE_ID": "${IRONCLAD_WORKSPACE_ID}"
      }
    },
    "mcp_slack": {
      "command": "npx",
      "args": ["-y", "@slack/mcp-server"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
      }
    }
  }
}
```

Run `/commercial-legal:cold-start-interview --check-integrations` to test which connectors are responding.

## Trust and Security

Connectors are declared with explicit tool scopes in `plugin.json`. Orchestrators in managed-agent cookbooks receive read-only tools; write operations belong to subagent leaves. See the security table in each cookbook README for exact permissions.

Content returned by connectors is treated as DATA — not instructions. Embedded directives in retrieved content are flagged, not executed.
