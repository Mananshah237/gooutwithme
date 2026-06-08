---
name: review
description: Route and review inbound agreements against your team playbook
command: /commercial-legal:review
tools: [read_file, write_file, web_search]
requires_setup: true
---

# Review — Commercial Contracts

Route an inbound agreement to the appropriate review skill, then run the review against your playbook and produce a memo.

## Pre-flight

1. Load the practice profile from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.
2. If the profile is unpopulated, stop and say: "Run `/commercial-legal:cold-start-interview` first."
3. Check whether a research connector (Westlaw, CourtListener) is responding. Record in the reviewer note.

## Step 1: Load the Agreement

Accept: a file path, a pasted document, or a URL. If none provided, ask.

For large documents (>50 pages): note coverage in the reviewer note. Prioritize definitions, key obligations, term, termination, liability, indemnity, IP, data, confidentiality, and governing law sections.

## Step 2: Determine the Active Side

1. Whose paper is this? (Check the header, parties clause, and whose standard terms apply.)
2. Load the matching playbook section (sales-side or purchasing-side).
3. If not obvious, ask: "This looks like [X]-side paper. Is that right, or are you on the [Y] side?"

If `confirm_routing: true` in the profile, confirm with the user before proceeding.

## Step 3: Route by Agreement Type

Extract the agreement title and any exhibits. Route to the appropriate sub-skill:

| Document type | Routes to |
|---|---|
| NDA / Confidentiality Agreement / MNDA | `nda-review` |
| Master Services Agreement / MSA / SOW-only | `vendor-agreement-review` |
| SaaS / Subscription Agreement / Order Form | `saas-msa-review` |
| Amendment / Addendum | `amendment-history` first, then the base agreement skill |
| Other / unclear | Ask the user |

If `confirm_routing: true`, say: "This looks like a [type]. I'll run `/commercial-legal:[skill]`. Confirm?" before proceeding.

## Step 4: Run the Review

Apply the playbook. For each material clause:

1. Identify the clause and the playbook position.
2. Determine: Standard ✓ / Acceptable fallback ✓ / Deviation 🟠 / Never accept 🔴 / Missing clause 🟡.
3. For deviations: draft a redline or proposed language.
4. Apply dual severity — legal risk AND business friction. See CLAUDE.md for the scale.

Cover at minimum: liability cap, indemnification, data protection, term and termination, IP ownership, governing law, confidentiality, warranties, and any clause on the Never list.

## Step 5: Output

**Format:**

```
[Work-product header per CLAUDE.md]

⚠️ Reviewer note
- Sources: [connector status]
- Read: [coverage]
- Flagged for your judgment: [N items marked [review]]
- Currency: [search status]
- Before relying: [1-2 actions]

---

# Agreement Review: [Agreement title]
**Party:** [Counterparty] | **Date:** [Date] | **Side:** [Sales/Purchasing]

## Bottom Line
[2-3 sentence summary — blocking issues, key deviations, overall posture]

## Findings

| # | Clause | Finding | Severity | Proposed language |
|---|---|---|---|---|
| 1 | [Clause name] | [Finding] | 🔴/🟠/🟡/🟢 | [Redline or "None needed"] |
...

## Escalation Triggers
[Any automatic escalations per your escalation matrix]

---

**One question I'd ask that isn't in my checklist:** [The second-order observation]

**What next? Pick one and I'll help you build it out:**
1. **Draft the redline memo** — I'll produce a tracked-changes memo for counterparty.
2. **Escalate** — I'll draft a short escalation to [approver] with the key facts.
3. **Get more facts** — I'd want to know [2-3 open questions] before advising.
4. **Watch and wait** — I'll add this to the tracker with a note on why.
5. **Something else** — tell me what you'd do with this.
```

## Escalation Check

After generating findings, check the escalation matrix. If any finding triggers an automatic escalation (unlimited liability, IP assignment to vendor, anything on a Never list), flag it prominently above the findings table.

## Dashboard Offer

If there are more than 10 findings, offer a visual dashboard per the standard template in `references/dashboard-template.md`.
