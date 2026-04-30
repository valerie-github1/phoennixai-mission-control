# PhoennixAI Mission Control

> Internal operating system for PhoennixAI — the AI-powered Business OS for solo founders.

**Status:** Private · Active development  
**Maintainer:** Valerie Wilcox — valerie@phoennixai.com  
**Deployed:** [phoennixai-mission-control.vercel.app](https://phoennixai-mission-control.vercel.app)

---

## What this repo contains

| Area | Files |
|---|---|
| Mission Control dashboard | `index.html`, `BetaDashboard.html`, `PhoennixAI_Beta_MissionControl.html` |
| Agent ecosystem | `*_CV_PhoennixAI.html`, `*_JobDescription_PhoennixAI.html` |
| Brand & design system | `PhoennixAI_BrandGuidelines.html`, `PhoennixAI_DNA_Intelligence_Standard.html` |
| Beta programme | `PhoennixAI_BetaWaitlist*.html`, `BETA_LAUNCH_PROMPT.txt` |
| NDA & sign hub | `PhoennixAI_NDA_SignHub.html`, `PhoennixAI_SignHub.html` |
| Internal operations | `PhoennixAI_InternalOps_MC.html`, `PhoennixAI_Workspace.html` |
| Supabase migrations | `supabase/migrations/` |
| Claude AI config | `CLAUDE.md`, `.claude/` |
| Next.js app (Phase 2) | `nextapp/` |

---

## Tech stack

- **Frontend:** Vanilla HTML / CSS / JS (Phase 1) · Next.js + TypeScript (Phase 2)
- **Database:** Supabase (PostgreSQL + RLS + Edge Functions)
- **Deploy:** Vercel
- **AI model:** Claude (Anthropic) via server-side API

---

## Security

- Never commit `config.js`, `.env*`, or any credential file.
- All API keys must be set as **Vercel environment variables** only.
- See `.gitignore` for full exclusion list.

---

## Dev branch

All changes must go through a PR against `main`. Direct pushes to `main` are blocked.

Working branch: `claude/setup-remote-control-qpnp8`

---

## Related repos

| Repo | Purpose |
|---|---|
| `client-intake` | AI-powered client intake form |
| `phoennixai-holographic-dashboard` | React + Three.js holographic dashboard |
| `phantom-gaming-studio` | Phantom Gaming Studio subsidiary site |
| `cupcakes-and-cocktails` | Cupcakes & Cocktails subsidiary site |

---

*PhoennixAI — confidential. Do not distribute.*
