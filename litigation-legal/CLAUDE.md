<!--
CONFIGURATION LOCATION
  ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md

Rules: READ from that path. If missing or has [PLACEHOLDER] markers, stop and prompt to run cold-start-interview.
This file is the TEMPLATE — replaced on plugin updates. Never write user data here.
Company profile: ~/.claude/plugins/config/claude-for-legal/company-profile.md
-->

# Litigation Practice Profile

*Run `/litigation-legal:cold-start-interview` to populate this template.*

---

## Who we are

**Firm / organization:** [PLACEHOLDER — from company-profile.md]
**Litigation team size:** [PLACEHOLDER]
**Managing partner / GC:** [PLACEHOLDER]
**Practice setting:** [PLACEHOLDER — Plaintiff / Defense / Both | In-house | Boutique | General practice]

---

## Who's using this

**Role:** [PLACEHOLDER — Litigator | Associate | Legal ops | Non-lawyer with attorney access]
**Supervising attorney:** [PLACEHOLDER]

---

## Active matters

**Matter workspace enabled:** [PLACEHOLDER ✓/✗ — set at cold-start; in-house users often don't need this]
**Active matter:** [PLACEHOLDER — none | matter name]

---

## Practice areas

**Primary:** [PLACEHOLDER — commercial litigation | IP | employment | products liability | securities | other]
**Courts:** [PLACEHOLDER — federal / state / both, key districts/circuits]
**Typical case size:** [PLACEHOLDER — number of documents, custodians, matter duration]

---

## Privilege handling

**Privilege log format:** [PLACEHOLDER — court-required format | house format]
**Clawback agreement standard:** [PLACEHOLDER — FRE 502(d) order in place ✓/✗]
**Inadvertent production protocol:** [PLACEHOLDER — immediate notification, clawback demand, court order]

---

## Discovery

**E-discovery platform:** [PLACEHOLDER — Everlaw | Relativity | other | none]
**Default custodian list approach:** [PLACEHOLDER — broad first / targeted]
**Hold notice system:** [PLACEHOLDER — tool or manual]

---

## Brief writing

**Court-specific local rules jurisdiction:** [PLACEHOLDER — district(s) where you primarily practice]
**Citation format:** [PLACEHOLDER — Bluebook | ALWD | court-specific]
**Word/page limits:** [PLACEHOLDER — note common limits for your courts]

---

## Integrations

| Integration | Status |
|---|---|
| CourtListener | [PLACEHOLDER ✓/✗] |
| Trellis | [PLACEHOLDER ✓/✗] |
| Westlaw / CoCounsel | [PLACEHOLDER ✓/✗] |
| Everlaw | [PLACEHOLDER ✓/✗] |
| Relativity | [PLACEHOLDER ✓/✗] |

---

## Shared guardrails

**Citations in briefs:** NEVER fabricate case citations. If a case cannot be retrieved from a connected research tool and verified, it must be tagged `[model knowledge — verify]` and the attorney must verify against Westlaw or Lexis before filing. An unverified citation in a filed brief is a Rule 11 violation.

**Local rules currency:** local rules change. Before citing a page/word limit, deadline rule, or formatting requirement, check the current court website or local rules database.

---

*To re-run: `/litigation-legal:cold-start-interview --redo`*
