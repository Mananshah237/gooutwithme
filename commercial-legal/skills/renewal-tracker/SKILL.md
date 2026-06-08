---
name: renewal-tracker
description: Scan contract register for cancel-by deadlines within 90 days
command: /commercial-legal:renewal-tracker
tools: [read_file, write_file]
requires_setup: true
---

# Renewal Tracker — Commercial Contracts

Scan the contract register for agreements with cancel-by or auto-renewal opt-out deadlines within the next 90 days (or a custom window). Produce a deadline digest.

## Pre-flight

1. Load the practice profile. If unpopulated, stop.
2. Check CLM integration status. If CLM is connected, query it. If not, look for a local register at `~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-register.yaml` or ask the user to provide one.

## Data Sources (in priority order)

1. CLM connector (Ironclad, Agiloft, etc.) — live query
2. Local renewal register — `skills/renewal-tracker/references/renewal-register.yaml`
3. User-provided spreadsheet or paste

## Logic

For each contract in the register:

1. Calculate days until the cancel-by deadline (not the auto-renewal date — the date BY WHICH the company must act to cancel).
2. Classify:
   - 🔴 **Action required now** — deadline within 14 days
   - 🟠 **Review this week** — deadline 15-30 days out
   - 🟡 **On watch** — deadline 31-90 days out
   - 🟢 **OK** — deadline >90 days out (include only if requested)
3. For each flagged contract, note: counterparty, contract type, ARR/TCV if available, cancel-by date, days remaining, current owner, and recommended action.

## Output

```
⚠️ Reviewer note
- Sources: [CLM connected ✓ | local register | user-provided]
- Contracts reviewed: [N]
- Window: [90 days / custom]
- Run date: [YYYY-MM-DD]

---

# Renewal Digest — [Date]

## Action Required Now 🔴 ([N] contracts)
| Counterparty | Type | ARR | Cancel-by | Days left | Owner | Action |
|---|---|---|---|---|---|---|
...

## Review This Week 🟠 ([N] contracts)
...

## On Watch 🟡 ([N] contracts)
...

---

**One question I'd ask:** [e.g., "Is the $240K Acme renewal worth a renegotiation conversation before the cancel-by date?"]

**What next?**
1. **Draft renewal decision memos** for the 🔴 contracts
2. **Escalate** the ones over your dollar threshold
3. **Post this digest to [channel]** per your house style
4. **Something else**
```

## Scheduled Agent

This skill is also deployed as the `renewal-watcher` managed agent. See `agents/renewal-watcher.md`.
