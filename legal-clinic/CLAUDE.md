<!--
CONFIGURATION LOCATION
  ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md

Rules: READ from that path. If missing or has [PLACEHOLDER] markers, stop and prompt to run cold-start-interview.
This file is the TEMPLATE — replaced on plugin updates. Never write user data here.
Company profile: ~/.claude/plugins/config/claude-for-legal/company-profile.md
-->

# Legal Clinic Practice Profile

*Run `/legal-clinic:cold-start-interview` to populate this template.*

---

## Who we are

**Clinic name:** [PLACEHOLDER]
**Law school / institution:** [PLACEHOLDER]
**Supervising attorney / clinic director:** [PLACEHOLDER]
**Accreditation:** [PLACEHOLDER — ABA-accredited ✓/✗ | state bar student practice rule]
**Practice areas:** [PLACEHOLDER — e.g., housing, immigration, family law, consumer, small business]

---

## Who's using this

**Role:** [PLACEHOLDER — Supervising attorney | 3L under student practice rule | Administrator]
**Student practice rule jurisdiction:** [PLACEHOLDER — state where students appear]

---

## Client intake

**Intake form:** [PLACEHOLDER — Aurora / paper / online form]
**Conflict check system:** [PLACEHOLDER — tool or manual]
**Intake capacity:** [PLACEHOLDER — clients per semester]
**Waitlist policy:** [PLACEHOLDER]

---

## Supervision requirements

**All client communications reviewed by:** [PLACEHOLDER — supervising attorney name / role]
**Work product sign-off:** [PLACEHOLDER — supervising attorney must approve before sending]
**Court appearances:** [PLACEHOLDER — student may appear with supervisor present ✓/✗ per state rule]

---

## Deadlines and calendaring

**Court calendar system:** [PLACEHOLDER — Google Calendar / court-specific / other]
**Statute of limitations tracking:** [PLACEHOLDER — manual / tool]
**Docket monitoring:** [PLACEHOLDER — CourtListener / PACER / manual]

---

## Integrations

| Integration | Status |
|---|---|
| Aurora (clinic management) | [PLACEHOLDER ✓/✗] |
| CourtListener | [PLACEHOLDER ✓/✗] |
| Document storage | [PLACEHOLDER ✓/✗] |

---

## ABA and ethics guardrails

**Competence:** Skills in this plugin support student learning but do not substitute for attorney supervision. All output requires supervising attorney review before use with a client.

**Confidentiality:** Client matters are confidential. Do not include client names or identifying information in prompts unless the conversation is within a secured, clinic-dedicated environment.

**Conflicts:** The conflict check must happen before any substantive work. This plugin does not run conflict checks — that is a system-level function outside the plugin's scope.

---

*To re-run: `/legal-clinic:cold-start-interview --redo`*
