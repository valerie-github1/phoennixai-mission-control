# Skill: mission-control-ops

Handles build, update, and maintenance operations for the PhoennixAI Mission Control ecosystem.

## What this skill does

- Update Mission Control (`PhoennixAI_InternalOps_MC.html`, v3.4) -- GRID Command panel, Agent Intelligence Feed, PA + ARIA Smart Scheduler, Calendar, Org Chart, Backlog, Session Log
- Update the Workspace (`PhoennixAI_Workspace.html`, v3.2) -- deliverables tracker, ARIA capabilities, bookmarks
- Update the Document Hub (`PhoennixAI_DocumentHub.html`, v2.3) -- agent registry, automation log, version history
- Add backlog items (BL-001 to BL-036+) to the correct app
- Update agent status across apps when new agents are signed or queue status changes
- Wire new Supabase table data into the front-end apps
- Run the Session Scan Protocol at the start of any session

## Agent owner

**GRID** -- Agent 009, Deep Royal #215CAE  
PM and BA. Owns Mission Control. Prince2 and Agile frameworks.

## Session Scan Protocol (Key Decision 28)

Run at the start of every session:
1. Check all 10 live apps are accessible on GitHub Pages
2. Review agent roster -- any new signings or status changes?
3. Check GitHub for any uncommitted changes
4. Review revenue position (Revenue Mandate -- Key Decision 29)
5. Identify highest-priority pending tasks from the backlog

## App versions to maintain

| File | App | Version | Owner |
|------|-----|---------|-------|
| `PhoennixAI_InternalOps_MC.html` | Mission Control | v3.4 | GRID |
| `PhoennixAI_Workspace.html` | Workspace | v3.2 | ARIA |
| `PhoennixAI_DocumentHub.html` | Document Hub | v2.3 | SCRIBE |
| `PhoennixAI_TraceabilityDashboard.html` | Traceability Dashboard | v1.0 | SAGE + SCRIBE |
| `PhoennixAI_UserManual.html` | New Hire Manual | v1.2 | SCRIBE |
| `PhoennixAI_PULSE_App.html` | PULSE Social Media | v2.0 | PULSE |
| `PhoennixAI_Beta_MissionControl.html` | Beta Mission Control | v1.1 | RELAY |
| `PhoennixAI_SignHub.html` | SignHub | v1.0 | SCRIBE |
| `PhoennixAI_InsightVisualBoard.html` | Insight Visual Board | v1.0 | SAGE |
| `BetaDashboard.html` | Beta Dashboard | latest | GRID |

## Supabase connection

- Project: `phoennixai-backend`
- Region: London
- URL: `https://erfvunwhpsdbyyayzdimz.supabase.co`
- 12 tables: events, tasks, notes, agents, products, schedule, agent_log, documents, backlog, sessions, notifications, revenue
- Phase 0: manual entry. Phase 2: automatic agent logging.

## Rules

- Mission Control is the sole alpha and beta MVP (Key Decision 31). All beta testing goes through here.
- All testers use the clean version (`PhoennixAI_Beta_MissionControl.html`). Nobody sees internal data except Valerie and Claude (Key Decision 33).
- Every agent action of significance is logged to the Traceability Dashboard and the `agent_log` Supabase table.
- LEDGER is advisory only inside the Agent Intelligence Feed -- it never executes (Key Decision 8).
- When updating agent counts or roster, ensure all three apps (Mission Control, Document Hub, New Hire Manual) are updated consistently.
- The cross-sell architecture between all 5 entities is the billion-pound mechanism (Key Decision 27) -- Mission Control must always reflect and support this.
