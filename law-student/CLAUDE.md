<!--
CONFIGURATION LOCATION
  ~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md

Rules: READ from that path. If missing or has [PLACEHOLDER] markers, stop and prompt to run cold-start-interview.
This file is the TEMPLATE — replaced on plugin updates. Never write user data here.
-->

# Law Student Practice Profile

*Run `/law-student:cold-start-interview` to populate this template.*

---

## Who I am

**Name:** [PLACEHOLDER]
**School:** [PLACEHOLDER]
**Year:** [PLACEHOLDER — 1L | 2L | 3L | LLM | Bar candidate]
**Concentration / focus:** [PLACEHOLDER — e.g., corporate, litigation, IP, public interest]

---

## Current courses

**This semester:** [PLACEHOLDER — list courses]
**Subjects for bar prep:** [PLACEHOLDER — MBE subjects + state-specific MEE subjects]

---

## Bar exam details

**Exam:** [PLACEHOLDER — UBE | California | New York | other]
**Target date:** [PLACEHOLDER — YYYY-MM]
**MBE subjects:** Contracts, Torts, Real Property, Criminal Law & Procedure, Constitutional Law, Civil Procedure, Evidence
**State-specific subjects:** [PLACEHOLDER — jurisdiction's MEE topics]

---

## Learning preferences

**Socratic style:** [PLACEHOLDER — hard / medium / guided — how aggressively to challenge answers]
**IRAC feedback depth:** [PLACEHOLDER — outline only | full analysis | line-by-line]
**Case brief format:** [PLACEHOLDER — standard (Facts/Issue/Rule/Holding/Reasoning) | IRAC-first | professor-specific]

---

## Exam forecast preferences

**Professor signals to track:** [PLACEHOLDER — specific professors or courses]
**Issue-spotting focus:** [PLACEHOLDER — subjects where issue-spotting is weakest]

---

## Guardrails for this plugin

This plugin is for learning and practice — not for providing legal advice to clients. The socratic drill and IRAC grading outputs are educational feedback, not legal conclusions. The bar prep content is study material, not a guarantee of what will appear on the exam.

Every case cited should be verified against a primary source (Westlaw, LexisNexis, your casebook) before relying on it. Tag: `[model knowledge — verify]`.

---

*To re-run: `/law-student:cold-start-interview --redo`*
