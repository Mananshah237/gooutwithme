<!--
CONFIGURATION LOCATION

User-specific configuration for this plugin lives at:
  ~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md

Rules for every skill in this plugin:
1. READ configuration from that path. Not from this file.
2. If that file does not exist or contains [PLACEHOLDER] markers, stop and prompt:
   "Run /privacy-legal:cold-start-interview first."
3. This file is the TEMPLATE — replaced on every plugin update.

Company-level facts live in ~/.claude/plugins/config/claude-for-legal/company-profile.md.
-->

# Privacy Practice Profile

*Run `/privacy-legal:cold-start-interview` to populate this template.*

---

## Who we are

**Company:** [PLACEHOLDER — from company-profile.md]
**Privacy team size:** [PLACEHOLDER]
**DPO or privacy lead:** [PLACEHOLDER]
**Practice setting:** [PLACEHOLDER — In-house | External DPO | Consulting]

---

## Who's using this

**Role:** [PLACEHOLDER — Privacy lawyer | DPO | Privacy engineer | Non-lawyer with counsel access]
**Attorney/DPO contact:** [PLACEHOLDER]

---

## Jurisdiction footprint

**Primary:** [PLACEHOLDER — e.g., GDPR (EU/UK), CCPA/CPRA (California), PIPEDA (Canada)]
**Secondary:** [PLACEHOLDER — additional jurisdictions where you have data subjects or operations]
**Excluded:** [PLACEHOLDER — jurisdictions explicitly out of scope]

---

## Processing activities

**ROPA maintained:** [PLACEHOLDER ✓/✗]
**ROPA location:** [PLACEHOLDER — local file / tool]
**Last updated:** [PLACEHOLDER — YYYY-MM-DD]

---

## DSAR handling

**Response deadline (GDPR):** 30 days (extendable to 3 months for complex requests)
**Response deadline (CCPA):** 45 days (extendable to 90 days)
**Verification method:** [PLACEHOLDER — how you verify requestor identity]
**Default response channel:** [PLACEHOLDER — email / portal / letter]
**Closing action:** [PLACEHOLDER — routing step after draft is produced]

---

## DPA requirements

**When we're a controller:** [PLACEHOLDER — what we require from processors]
**When we're a processor:** [PLACEHOLDER — what controllers typically require of us]
**Standard clauses:** [PLACEHOLDER — EU SCCs | UK IDTA | APEC CBPR | other]
**Transfer mechanisms:** [PLACEHOLDER — which transfer mechanisms are approved]

---

## Risk posture

**PIA threshold** (when a PIA is required): [PLACEHOLDER — e.g., new processing of special categories, large-scale profiling, systematic monitoring]
**DPIA threshold** (when a DPIA is required under GDPR Art. 35): [PLACEHOLDER]

---

## Integrations

| Integration | Status |
|---|---|
| OneTrust / TrustArc / Ketch | [PLACEHOLDER ✓/✗] |
| Slack | [PLACEHOLDER ✓/✗] |
| Document storage | [PLACEHOLDER ✓/✗] |

---

## Shared guardrails

Same tag vocabulary and guardrails as described in the commercial-legal CLAUDE.md. Key additions for privacy:

- **Jurisdiction-first:** Always identify which law applies before applying any framework. GDPR, CCPA, PIPEDA, and LGPD have different rights, timelines, and penalties.
- **Currency is critical:** Privacy law changes fast. Always check currency for regulation status, enforcement guidance, and adequacy decisions before relying on model knowledge. Tag `[model knowledge — verify]`.
- **Special categories:** Flag any processing of special category data (health, biometric, political views, etc.) immediately — higher PIA threshold, additional legal basis requirements.

---

*To re-run: `/privacy-legal:cold-start-interview --redo`*
