# CLAUDE-v3.md — PhoennixAI Permanent Memory
> Claude Code reads this file every session. Do not delete or rename.
> Version: v3 | April 2026 | Supersedes CLAUDE-v2.md and CLAUDE.md

---

## 01 · Who Valerie Is

| | |
|---|---|
| **Full name** | Valerie Wilcox |
| **Role** | CEO & Founder |
| **Companies** | PhoennixAI · Phantom Gaming Studio · Cupcakes & Cocktails |
| **Location** | London, UK |
| **Primary email** | valerie@phoennixai.com |
| **Personal email** | wilcox.valerie@yahoo.co.uk |
| **Remote control** | phoenixdigitec3@gmail.com |
| **CTO / co-builder** | Dilpreet — dilpreet@phoennixai.com |

---

## 02 · The Three Brands

### A · PhoennixAI
**What it is:** The world's first AI-powered Business Operating System (BOS) for solo founders.
Replaces 6–12 tools with one command centre staffed by 22 AI agents.

**Tagline:** "The world's first AI-human co-led company."
**Website:** phoennixai.com
**GitHub:** valerie-github1/phoennixai-mission-control
**Vercel:** phoennixai-mission-control.vercel.app

**22 AI agents:** ARIA · PULSE · SCRIBE · SIGNAL · RELAY · PROBE · LEDGER · NEXUS ·
FORGE · GRID · ECHO · SAGE · SCOUT · PHANTOM AGENT (PA) · CLAUDE + 7 others

**Modules:**
- Mission Control (BOS core)
- Marketing OS (MOS) — email, content, brand voice
- PULSE — internal ops manual
- SCRIBE — document hub
- Client Intake — Aria AI form (client-intake-bay.vercel.app)

---

### B · Phantom Gaming Studio
**What it is:** AI-native game development studio. Phoenix AI subsidiary.
**Flagship:** Phantom Drive — holographic EV cockpit simulator (prototype complete)
**Pre-seed ask:** £150,000
**Website:** phantom.phoennixai.com (planned)
**GitHub:** valerie-github1/phantom-gaming-studio
**Live (meeting page):** valerie-github1.github.io/phantom-gaming-studio/

---

### C · Cupcakes & Cocktails
**What it is:** Artisan lifestyle and events brand. Phoenix AI subsidiary.
**Offering:** Premium events, AI-personalised menus, corporate gifting
**GitHub:** valerie-github1/cupcakes-and-cocktails
**Live:** valerie-github1.github.io/cupcakes-and-cocktails/

---

## 03 · Brand Identity

### Colours
```
--midnight  : #060A18   (deep background)
--fire      : #FF6B2B   (primary CTA / brand orange)
--electric  : #00E5FF   (cyan / links / accents)
--gold      : #FFB830   (highlights / premium)
--sapphire  : #46ABD7   (secondary blue)
--royal     : #215CAE   (deep blue)
--surface   : #0D1220   (card backgrounds)
--text      : #E8E8E8   (primary text)
--text2     : rgba(255,255,255,0.55)
--text3     : rgba(255,255,255,0.28)
```

### Typography
```
Bebas Neue       → display / headlines
DM Sans          → body / UI (primary)
Playfair Display → serif accent / italic quotes
DM Mono          → code / data / labels
Cormorant Garamond → elegant headers (Phantom Gaming, C&C)
Rajdhani         → holographic dashboard HUD
```

---

## 04 · Brand Voice Rules

Apply to ALL copy — emails, UI, docs, social, everything.

1. Short sentences. Always.
2. Banned words: leverage, utilise, synergy, robust, seamless, cutting-edge, innovative
3. Speak to ONE founder. Never "founders" (plural) in body copy.
4. Cut hedging: "might", "could possibly", "you may want to"
5. Never open with "I hope this email finds you well"
6. Structure: Pain → Transformation → One clear action
7. Aria = warm, curious. Valerie = decisive, direct.
8. One CTA per message. Never three.

---

## 05 · Tech Stack

| Layer | Technology |
|---|---|
| BOS frontend | Vanilla HTML / CSS / JS (no build step) |
| Holographic dashboard | React 18 + Three.js + TypeScript + Vite |
| Client intake | Vanilla HTML + Anthropic API + jsPDF |
| AI model (Aria) | claude-sonnet-4-20250514 |
| Database | Supabase (PostgreSQL + Edge Functions) |
| Deployment | Vercel (primary) + GitHub Pages (static) |
| Knowledge graph | graphify (graphifyy 0.4.8) |
| Remote control | graphify + Claude Code hooks |

---

## 06 · All Repos — valerie-github1

| Repo | Visibility | Status | URL |
|---|---|---|---|
| `client-intake` | PUBLIC | LIVE | client-intake-bay.vercel.app |
| `phoennixai-mission-control` | PUBLIC | deployed | phoennixai-mission-control.vercel.app |
| `phoennixai-holographic-dashboard` | PUBLIC | built | deploy via Vercel |
| `phantom-gaming-studio` | PUBLIC | LIVE | valerie-github1.github.io/phantom-gaming-studio/ |
| `cupcakes-and-cocktails` | PUBLIC | LIVE | valerie-github1.github.io/cupcakes-and-cocktails/ |
| `phoennixai-agency-backend` | PRIVATE | active | — |
| `phoennixai-agency-website` | PRIVATE | active | — |
| `wilcoxdesigns-website` | PRIVATE | active | — |

---

## 07 · GitHub & Deployment

```
Account       : valerie-github1
Dev branch    : claude/setup-remote-control-qpnp8
Vercel account: valerie@phoennixai.com
```

**3-command push workflow:**
```bash
git add -p
git commit -m "feat: <description>"
git push -u origin main   # or dev branch
```

---

## 08 · Supabase

```
Table         : client_intake
URL env var   : SUPABASE_URL
Key env var   : SUPABASE_KEY
Notify emails : valerie@phoennixai.com · dilpreet@phoennixai.com
```

---

## 09 · Claude Code Config

**`~/.claude/settings.json` — MCP servers active:**
```
github    → @modelcontextprotocol/server-github (GITHUB_TOKEN)
supabase  → @supabase/mcp-server-supabase (SUPABASE_ACCESS_TOKEN)
composio  → composio-mcp (COMPOSIO_API_KEY)
graphify  → graphify . --mcp
```

**Hooks active:**
```
PreToolUse  (Glob/Grep)  → read graphify-out/GRAPH_REPORT.md first
PostToolUse (Write/Edit) → auto-rebuild knowledge graph
SessionStart             → remote control setup
```

**Plugins installed:**
```
graphify     (pip3 install graphifyy → graphify install → graphify claude install)
vercel       (npx plugins add vercel/vercel-plugin)  — 25 skills loaded
```

---

## 10 · Marketing OS (MOS)

MOS is the marketing module inside Mission Control.

**Beta email sequence:** 6 emails over 8 weeks (full copy in BETA_LAUNCH_PROMPT.txt)
**MOS agents:** SIGNAL · SCRIBE · ARIA · PROBE · RELAY
**Brand voice calibrator:** Input 3 writing samples → outputs voice brief
**Content calendar:** 30-day, topic-clustered, auto-scheduled
**Social templates:** Instagram + LinkedIn, in PhoennixAI brand voice

---

## 11 · Beta Programme

```
Programme     : PhoennixAI Beta
Model         : Invite-only, NDA signed at intake
Target cohort : 50–100 solo founders
Duration      : 8 weeks
Goal          : 30%+ conversion to paid on public launch
```

**Beta email cadence:** Day 0 · Day 3 · Week 2 · Week 4 · Week 7 · Week 8 (Launch)
**Full prompts:** BETA_LAUNCH_PROMPT.txt

---

## 12 · Claw Code — New Project Directive

Every new PhoennixAI project:
```bash
claw install --claude
graphify claude install
```

---

## 13 · Rules for Claude Code

1. Read this file first, every session.
2. Before any beta/MOS/email/copy task → read `BETA_LAUNCH_PROMPT.txt`
3. Before any design task → check `PhoennixAI_BrandGuidelines.html`
4. Apply brand voice rules to ALL copy without exception
5. Never hardcode tokens/keys in files pushed to GitHub — use env var refs
6. Always use `--acc` / `--fire` / `--electric` CSS vars, never raw hex
7. Commit to dev branch first, never force-push main
8. Run `graphify claude install` on every new project
9. One CTA per email/page section. Never three.
10. Valerie is the decision-maker. When in doubt, ask her.
