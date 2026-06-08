---
name: dsar-response
description: Draft DSAR responses within applicable deadlines, with identity verification and data subject rights analysis
command: /privacy-legal:dsar-response
tools: [read_file, write_file, web_search]
requires_setup: true
---

# DSAR Response — Privacy Legal

Draft a data subject access request response. Determine applicable law, verify the request is valid, identify responsive data, and draft the response within the legal deadline.

## Pre-flight

1. Load the privacy practice profile. If unpopulated, stop.
2. Check the jurisdiction — which law governs (GDPR, CCPA, PIPEDA, UK GDPR, other)?
3. Identify the request date — calculate the response deadline.
4. Check research connector status. Currency matters here: enforcement guidance changes.

## Step 1: Request Triage

Gather:
- **Requestor identity** — how was identity verified (or not yet)?
- **Request type** — access / erasure / portability / restriction / objection / correction
- **Request date** — for deadline calculation
- **Scope of request** — all data, specific systems, specific time period?
- **Special circumstances** — is this requestor a current/former employee? Litigation hold in place?

## Step 2: Deadline Calculation

| Law | Standard deadline | Extension |
|---|---|---|
| GDPR (EU/UK) | 30 days from receipt | Up to 3 months for complex/numerous requests — must notify within 30 days |
| CCPA/CPRA | 45 days from receipt | Up to 90 days — must notify within 45 days |
| PIPEDA | 30 days from receipt | Extension possible with notification |
| LGPD | 15 days from receipt | — |

Flag if deadline is within 7 days — escalate per practice profile.

## Step 3: Exemptions Analysis

Check whether any exemptions apply (jurisdiction-specific):
- Third-party data in the responsive data
- Legal professional privilege
- Disproportionate effort
- National security / law enforcement
- Ongoing litigation / legal hold

Flag any exemptions as `[review]` — these are attorney judgment calls.

## Step 4: Responsive Data Identification

Based on the systems listed in the ROPA (if available), identify which systems are likely to hold responsive data. List them. Note any systems that require manual review vs. automated export.

If ROPA is not available, ask the user to identify the relevant systems.

## Step 5: Draft Response

Draft the response letter. Format:
- Acknowledge receipt and confirm deadline
- Identity verification confirmation (or request, if not yet verified)
- Description of the responsive data (or redactions and exemptions applied)
- Instructions for the data subject on how to receive/access the data
- Rights reminder (right to complain to supervisory authority)
- Contact information

Apply the practice profile's `closing_action` for routing after the draft is approved.

## Output

```
⚠️ Reviewer note
- Jurisdiction: [GDPR / CCPA / PIPEDA / other]
- Request date: [YYYY-MM-DD]
- Response deadline: [YYYY-MM-DD] ([N] days remaining)
- Exemptions flagged: [N items marked [review]]
- Currency: [enforcement guidance checked via [source] / model knowledge — verify]

---

[Draft response letter]

---

What next?
1. Send as drafted (route per closing_action)
2. Apply exemptions — I'll redact [specific items] and update the letter
3. Request identity verification — I'll draft the verification request
4. Escalate — [N] days left, flag to [DPO/counsel]
5. Something else
```
