---
name: cold-start-interview
description: Initial practice profile setup — learns your team playbook in 10-15 minutes
command: /commercial-legal:cold-start-interview
flags:
  - name: --redo
    description: Re-run the full interview, overwriting existing config
  - name: --side
    values: [sales, purchasing]
    description: Run only the sales-side or purchasing-side playbook interview
  - name: --check-integrations
    description: Test which MCP connectors are currently responding
tools: [read_file, write_file]
requires_setup: false
---

# Cold-Start Interview — Commercial Contracts

You are running the setup interview for the commercial-legal plugin. This interview writes the practice profile at `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. Every other skill in this plugin reads that file before doing anything.

**Do not skip or abbreviate the interview.** A vague or incomplete profile produces generic outputs that won't match how the team actually works.

## Pre-flight

Check whether `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` exists and is populated (no `[PLACEHOLDER]` values). If it is:

- Without `--redo`: "Your practice profile is already configured. Run `/commercial-legal:cold-start-interview --redo` to update it, or edit the file directly at `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`."
- With `--redo`: proceed, overwriting.

If `--check-integrations` is passed, skip the interview and run the integration check only (see Integration Check section below).

## Phase 1: Company Profile

Check whether `~/.claude/plugins/config/claude-for-legal/company-profile.md` exists. If not, gather:

1. **Company name** and entity type (LLC, Inc., LLP, etc.)
2. **Industry** (SaaS, financial services, healthcare, manufacturing, etc.)
3. **Size** (headcount or revenue range — helps calibrate risk posture)
4. **Where you operate** — jurisdiction footprint (US states, EU, UK, APAC, global)
5. **Risk posture** — conservative / market / aggressive on risk
6. **GC or senior legal contact** — name and preferred escalation channel

Write to `~/.claude/plugins/config/claude-for-legal/company-profile.md`.

## Phase 2: Practice Profile

Gather plugin-specific facts:

1. **Team size** — how many people handle contracts
2. **Volume** — roughly how many agreements per month
3. **Mix** — mostly vendor / mostly customer / balanced
4. **CLM system** — Ironclad, Agiloft, manual, none
5. **Active side** — sales-side, purchasing-side, or both
6. **Role of the person running this** — lawyer / non-lawyer with attorney access / non-lawyer without
7. **The thing that hurts** — in their words, what takes too long or goes wrong most often

## Phase 3: Playbook — Sales Side

*(Skip if active side is purchasing-only)*

Walk through each playbook position. For each one, ask what the standard position is, what fallbacks are acceptable, and what to never accept.

Cover: limitation of liability (cap, carveouts, base definition), indemnification, data protection, term and termination, governing law and venue, and "the one thing" — the deal-breaker on sales-side deals.

Tip: ask the lawyer to pull 2-3 signed agreements that represent their "standard" deals and use those as the seed — the playbook learned from real paper is more accurate than a playbook built from preferences stated in the abstract.

## Phase 4: Playbook — Purchasing Side

*(Skip if active side is sales-only)*

Same structure as Phase 3, for purchasing-side deals. The positions typically flip — what you required of vendors when selling, you now ask of vendors when buying.

## Phase 5: Escalation Matrix

Build the approval table:
- Who can approve what without escalation (dollar thresholds, risk thresholds)
- Who they escalate to and how (Slack, email, in-person)
- Automatic escalations regardless of dollar value (e.g., unlimited liability, IP assignments, anything on a Never list)

## Phase 6: House Style

1. **Tone in redlines** — aggressive / collaborative / neutral / whatever the client typically uses
2. **Stakeholder summaries** — who reads them (business partner, CFO, board), how long, what format
3. **Where work product goes** — CLM, Drive folder, Slack channel, email
4. **Renewal alert channel** — where to post the renewal digest

## Phase 7: Integrations

Check which MCP tools are responding. For each integration below, test the connection and record the result in the profile:

| Integration | How to test |
|---|---|
| CLM (Ironclad, Agiloft) | Attempt to list contracts |
| DocuSign | Attempt to list envelopes |
| Google Drive / SharePoint / Box | Attempt to list a folder |
| Slack | Attempt to list channels |
| Westlaw / CoCounsel | Attempt a stub search |
| CourtListener | Attempt a stub search |

Record ✓ (responding) or ✗ (not configured / not responding) for each. Note the fallback behavior in the profile.

## Integration Check (--check-integrations)

Re-run Phase 7 only. Print a status table and update the profile's integration table. Do not re-run the interview.

## Writing the Profile

Write the completed profile to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, replacing all `[PLACEHOLDER]` values with the gathered information. Create parent directories as needed.

After writing, confirm: "Your practice profile is saved. Every skill in this plugin will now use your playbook. Run `/commercial-legal:review` to review your first agreement."

## What This Skill Does NOT Do

- Does not make legal judgments — it records yours
- Does not connect to any external system during the interview (that's Phase 7 / --check-integrations)
- Does not require a research connector to run
