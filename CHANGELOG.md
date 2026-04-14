# CHANGELOG — PhoennixAI

All significant deployments and changes across PhoennixAI projects.

---

## 2026-04-14

### phoennixai-mission-control
- **v3.4** — Full BOS dashboard: GRID as PM, holographic charts, working commands, dark hologram palette
- **v2** — Previous version: Orbitron/Exo 2 palette, /command bar, 29 agents hub, Snowy companion, PWA

### phoennixai-holographic-dashboard
- Added `vercel.json` — Vite build config (`npm run build`, output: `dist`)
- Source: React 18 + Three.js + TypeScript + `@react-three/fiber`

### phoennixai-nda
- `vercel.json` added for static deploy
- `index.html`: PhoennixAI NDA with typed e-signature, 11 clauses, confirmation screen

### client-intake (client-intake-bay.vercel.app)
- **EmailJS integration** — `doEmail()` now sends via `@emailjs/browser` SDK
  - Service: `service_950ppyc` · Template: `template_qkl2xa6`
  - Falls back to `mailto:` draft if `EMAILJS_PUBLIC_KEY` not set
  - Add `EMAILJS_PUBLIC_KEY` in Vercel env vars to activate
- `/api/chat` edge function proxies Anthropic API (key stays server-side)
- Brand update: `--midnight`/`--fire`/`--electric` palette, Bebas Neue display font

---

## 2026-04-13

### All repos
- CLAUDE.md master directive v3 pushed to all repos
- graphify knowledge graph rebuilt
- Remote control hooks active (SessionStart, PreToolUse, PostToolUse)

### client-intake
- `api/chat.js` Vercel Edge Function — proxies Anthropic API server-side
- `new-intake.html` — brand-updated intake form replacing old teal palette
