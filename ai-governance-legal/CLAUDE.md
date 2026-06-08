<!--
CONFIGURATION LOCATION
  ~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md

Rules: READ from that path. If missing or has [PLACEHOLDER] markers, stop and prompt to run cold-start-interview.
This file is the TEMPLATE — replaced on plugin updates. Never write user data here.
Company profile: ~/.claude/plugins/config/claude-for-legal/company-profile.md
-->

# AI Governance Practice Profile

*Run `/ai-governance-legal:cold-start-interview` to populate this template.*

---

## Who we are

**Company:** [PLACEHOLDER — from company-profile.md]
**AI governance team size:** [PLACEHOLDER]
**CISO / AI risk lead / DPO:** [PLACEHOLDER]
**Practice setting:** [PLACEHOLDER — In-house | Consulting | Regulator-facing]

---

## Who's using this

**Role:** [PLACEHOLDER — Lawyer / Privacy engineer / AI risk officer / Non-lawyer with counsel access]
**Attorney contact:** [PLACEHOLDER]

---

## AI jurisdiction footprint

**Primary:** [PLACEHOLDER — EU AI Act | NIST AI RMF | Colorado AI Act | OECD Principles | other]
**Secondary:** [PLACEHOLDER — additional AI regulations in scope]
**Industry-specific:** [PLACEHOLDER — e.g., FDA AI/ML guidance for medical devices, FFIEC guidance for banking]

---

## Use-case triage thresholds

**High-risk AI systems (EU AI Act Annex III equivalent):** [PLACEHOLDER — which use cases automatically trigger AIA]
**Limited-risk:** [PLACEHOLDER — transparency obligations only]
**Minimal-risk:** [PLACEHOLDER — no regulatory requirement, internal policy applies]

**Internal policy threshold (stricter than regulation):** [PLACEHOLDER — e.g., "any AI system making employment decisions requires AIA regardless of regulatory classification"]

---

## AI Impact Assessment (AIA) requirements

**When required:** [PLACEHOLDER — EU AI Act Art. 9 DPIA-equivalent, Colorado, internal policy]
**Template:** [PLACEHOLDER — internal template location]
**Approval required from:** [PLACEHOLDER — AI Ethics Board / CISO / GC / other]
**Documentation location:** [PLACEHOLDER — where completed AIAs are stored]

---

## Vendor AI review

**When triggered:** [PLACEHOLDER — e.g., any vendor contract where vendor uses AI to process our data or make decisions affecting our customers]
**Key requirements:** [PLACEHOLDER — audit rights, transparency, human oversight, bias testing, data residency]
**Deal-breaker terms:** [PLACEHOLDER — e.g., no audit rights, no transparency on training data, no human override]

---

## Integrations

| Integration | Status |
|---|---|
| Slack | [PLACEHOLDER ✓/✗] |
| Document storage | [PLACEHOLDER ✓/✗] |
| Jira / Linear (for tracking) | [PLACEHOLDER ✓/✗] |

---

## Shared guardrails

Currency is especially critical for AI governance — the regulatory landscape changes monthly. Always run web search for current status before relying on model knowledge about:
- EU AI Act implementing acts and guidelines
- State AI legislation effective dates (Colorado, Texas, etc.)
- NIST RMF updates
- Enforcement actions and guidance

Tag all regulatory status items `[model knowledge — verify]` unless retrieved from a primary source this session.

---

*To re-run: `/ai-governance-legal:cold-start-interview --redo`*
