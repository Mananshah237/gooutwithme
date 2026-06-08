---
name: nda-review
description: Triage NDAs — mutual vs. one-way, term, permitted purpose, residuals, and playbook deviations
command: /commercial-legal:nda-review
tools: [read_file, write_file, web_search]
requires_setup: true
---

# NDA Review — Commercial Contracts

Fast-triage an NDA against your playbook. Flag material deviations and produce a one-page memo with redlines.

## Pre-flight

1. Load the practice profile. If unpopulated, stop.
2. Determine active side (whose paper, who's disclosing).

## Structure Check

First, extract the agreement structure:

- **Type:** Mutual / One-way (which direction)
- **Parties:** Discloser / Recipient / Both
- **Scope:** What confidential information is covered, what's excluded
- **Purpose:** The permitted use — is it specific enough?
- **Term:** Duration of the NDA and of the confidentiality obligation (often different)
- **Residuals clause:** Does it permit employees to use information retained in unaided memory?
- **Governing law:** Matches playbook preference?
- **Return/destroy:** Required on termination? Within what period?

## Playbook Check

Compare each extracted term against the playbook. Flag:

- 🔴 **Blocking** — e.g., residuals clause that effectively permits competitive use, one-way NDA on wrong terms, unlimited term
- 🟠 **High** — e.g., overly broad definition of confidential information, no carveout for publicly available info
- 🟡 **Medium** — e.g., governing law outside preferred jurisdictions, return/destroy obligation that's operationally difficult
- 🟢 **Low / Standard** — no action needed

## Output

One-page memo with:
1. Summary (3 sentences: type, key terms, overall posture)
2. Findings table (clause, finding, severity, proposed redline)
3. Recommended disposition: sign as-is / redline and return / escalate / reject
4. Closing action per `nda_triage_preferences.closing_action` in the profile

Apply the closing action exactly as configured — this is usually a routing step like "forward to contracts manager."
