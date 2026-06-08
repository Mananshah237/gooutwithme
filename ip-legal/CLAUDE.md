<!--
CONFIGURATION LOCATION
  ~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md

Rules: READ from that path. If missing or has [PLACEHOLDER] markers, stop and prompt to run cold-start-interview.
This file is the TEMPLATE — replaced on plugin updates. Never write user data here.
Company profile: ~/.claude/plugins/config/claude-for-legal/company-profile.md
-->

# IP Practice Profile

*Run `/ip-legal:cold-start-interview` to populate this template.*

---

## Who we are

**Company:** [PLACEHOLDER — from company-profile.md]
**IP team size:** [PLACEHOLDER]
**IP counsel / patent agent:** [PLACEHOLDER]
**Practice setting:** [PLACEHOLDER — In-house | IP boutique | General practice with IP | Academic]

---

## Who's using this

**Role:** [PLACEHOLDER — IP attorney | Patent agent | Non-lawyer with counsel access]
**Attorney contact:** [PLACEHOLDER]

---

## IP portfolio

**Trademark registrations:** [PLACEHOLDER — jurisdictions, key marks]
**Patent portfolio size:** [PLACEHOLDER — issued, pending, abandoned]
**Copyright registrations:** [PLACEHOLDER — key works registered]
**Trade secrets:** [PLACEHOLDER — program in place ✓/✗]
**Open source footprint:** [PLACEHOLDER — repos, key licenses in use]

---

## Trademark clearance

**Standard clearance scope:** [PLACEHOLDER — US only | US + key international | global]
**Acceptable risk level:** [PLACEHOLDER — identical only | confusingly similar | broader]
**Clearance vendor:** [PLACEHOLDER — in-house | outside search firm]
**Registrability threshold:** [PLACEHOLDER — what level of confidence to proceed with filing]

---

## OSS policy

**Permitted licenses:** [PLACEHOLDER — MIT, Apache 2.0, BSD-2, BSD-3, ISC, etc.]
**Restricted (copyleft):** [PLACEHOLDER — GPL-3.0, AGPL, LGPL — use case restrictions]
**Prohibited:** [PLACEHOLDER — e.g., no AGPL in SaaS product code]
**OSS scan tool:** [PLACEHOLDER — FOSSA, Snyk, Black Duck, manual]
**Review trigger:** [PLACEHOLDER — when a new OSS dependency triggers review]

---

## Cease-and-desist

**Standard response time:** [PLACEHOLDER — e.g., respond within 10 business days]
**Escalation trigger:** [PLACEHOLDER — when to involve outside litigation counsel]
**Settlement authority:** [PLACEHOLDER — who can approve settlement terms]

---

## Integrations

| Integration | Status |
|---|---|
| Descrybe (patent analytics) | [PLACEHOLDER ✓/✗] |
| Solve Intelligence | [PLACEHOLDER ✓/✗] |
| USPTO direct | [PLACEHOLDER ✓/✗] |
| FOSSA / Snyk (OSS scan) | [PLACEHOLDER ✓/✗] |

---

## Shared guardrails

**Patent law currency:** patent eligibility doctrine (Alice/Mayo for software), obviousness standards, and inter partes review success rates change with Federal Circuit decisions. Check currency before relying on model knowledge.

**Trademark geography:** clearance standards, opposition procedures, and similarity tests vary significantly by jurisdiction. The US likelihood-of-confusion test (DuPont factors) does not apply in the EU (EUIPO uses a global assessment). Flag jurisdiction `[review]` on any non-US clearance.

---

*To re-run: `/ip-legal:cold-start-interview --redo`*
