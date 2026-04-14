# SKILL-v3.md — PhoennixAI Agent Skills
> Claude Code reads this file to understand what skills are active.
> Version: v3 | April 2026 | Supersedes SKILL-v2.md

---

## Install All Skills (run once per machine)

```bash
# Step 1 — Core tools
pip3 install graphifyy
graphify install
graphify claude install

# Step 2 — Vercel plugin (deploy from Claude Code)
echo "Y" | npx plugins add vercel/vercel-plugin

# Step 3 — MCP servers
npx -y @modelcontextprotocol/server-github
npx -y @supabase/mcp-server-supabase@latest
npx -y composio-mcp@latest

# Step 4 — New project bootstrap (Claw Code directive)
# Run in every new PhoennixAI project root:
claw install --claude
graphify claude install
```

---

## Skill Registry

### 01 · graphify
**Trigger:** `/graphify`
**Purpose:** Any input → knowledge graph → clustered communities → HTML + JSON + audit report.

```bash
/graphify .                    # full pipeline on current directory
/graphify . --update           # incremental rebuild (new/changed files only)
/graphify . --wiki             # build agent-crawlable wiki
/graphify . --mcp              # start MCP stdio server for agent access
```

Auto-runs via PostToolUse hook after every Write/Edit.

---

### 02 · vercel (25 skills loaded)
**Trigger:** `/deploy`, `vercel:deploy`, `vercel:status`, `vercel:env`

```bash
vercel:deploy prod             # deploy to production
vercel:status                  # project overview + recent deployments
vercel:env list                # list environment variables
vercel:env pull                # sync env vars locally
vercel:marketplace             # discover integrations
```

**Active projects:**
| Project | Type | Deploy command |
|---|---|---|
| `phoennixai-mission-control` | Static HTML / PWA | `vercel --prod` |
| `phoennixai-holographic-dashboard` | Vite | `vercel --prod` |
| `client-intake` | Static HTML | `vercel --prod` |
| `cupcakes-and-cocktails` | Static HTML | `vercel --prod` |
| `phantom-gaming-studio` | Static HTML | GitHub Pages |

---

### 03 · Marketing OS (MOS)
**Trigger:** Any task referencing MOS, email sequences, brand voice, content calendar, social posts.
**Reference file:** `BETA_LAUNCH_PROMPT.txt`

**MOS agents:**
| Agent | Role |
|---|---|
| SIGNAL | Social media scheduling + content |
| SCRIBE | Copywriting + email sequences |
| ARIA | Client comms + intake |
| PROBE | Market research + competitor analysis |
| RELAY | Campaign coordination |

**MOS tasks Claude can run:**
```
- Generate beta email sequence (use 6-email structure in BETA_LAUNCH_PROMPT.txt)
- Write brand voice brief (input: 3 writing samples → output: voice doc)
- Build content calendar (30 days, topic-clustered)
- Write Instagram / LinkedIn posts in PhoennixAI brand voice
- Generate launch kit copy (subject lines, CTAs, landing page sections)
- Build email HTML using brand colour palette
```

**Always read `BETA_LAUNCH_PROMPT.txt` before any MOS task.**

---

### 04 · Beta Launch Operations
**Reference file:** `BETA_LAUNCH_PROMPT.txt`

**Beta email sequence (6 emails):**
| # | Name | Send timing | Goal |
|---|---|---|---|
| 1 | Invitation | Day 0 | Access + first login |
| 2 | Day 3 check-in | Day 3 | Activation (meet Aria) |
| 3 | Feedback request | Week 2 | Honest product feedback |
| 4 | MOS unlock | Week 4 | Module adoption |
| 5 | Pre-launch conversion | Week 7 | Founder pricing lock-in |
| 6 | Launch day | Week 8 | Public launch celebration |

**Beta cohort:** 50–100 solo founders, NDA signed, invite-only.

---

### 05 · PhoennixAI Brand Voice
**Always apply these rules to ALL copy:**

| Rule | Detail |
|---|---|
| Sentence length | Short. Always. |
| Banned words | leverage, utilise, synergy, robust, seamless, cutting-edge |
| Audience framing | Speak to ONE founder. Never "founders" (plural) in body copy |
| Hedging | Cut "might", "could possibly", "you may want to" |
| Openers | Never "I hope this email finds you well" |
| Structure | Acknowledge pain → show transformation → one clear action |
| Aria vs Valerie | Aria = warmer, more curious. Valerie = decisive, direct |
| CTA | One per message. Never three. |

**Brand palette (email-safe):**
```
#060A18  — background (midnight)
#FF6B2B  — fire (primary CTA)
#00E5FF  — electric (accents/links)
#FFB830  — gold (highlights)
#46ABD7  — sapphire (secondary)
#E8E8E8  — body text
```

**Fonts:**
```
Bebas Neue     → headlines (fallback: Impact)
DM Sans        → body (fallback: system-ui)
Playfair Display → accent/italic quotes (fallback: Georgia)
DM Mono        → code/data (fallback: monospace)
```

---

### 06 · GitHub MCP (all repos)
**Configured in:** `~/.claude/settings.json`

All `valerie-github1` repos accessible via MCP:
```
client-intake                    (PUBLIC · LIVE · client-intake-bay.vercel.app)
phoennixai-holographic-dashboard (PUBLIC · built · needs Vercel deploy)
phoennixai-mission-control       (PUBLIC · pushed · needs Vercel deploy)
phantom-gaming-studio            (PUBLIC · LIVE · GitHub Pages)
cupcakes-and-cocktails           (PUBLIC · LIVE · GitHub Pages)
phoennixai-agency-backend        (PRIVATE)
phoennixai-agency-website        (PRIVATE)
wilcoxdesigns-website            (PRIVATE)
```

---

### 07 · Supabase MCP
**Configured in:** `~/.claude/settings.json` via `${SUPABASE_ACCESS_TOKEN}`

**Active table:** `client_intake`
```sql
-- Key columns
id, submitted_at, name, email, company, role,
app_description, problem_solved, app_type,
target_users, must_have_features[], budget,
funding_stage, nda_signed
```

---

### 08 · Composio MCP
**Configured in:** `~/.claude/settings.json` via `${COMPOSIO_API_KEY}`
250+ tool integrations available (Gmail, Slack, Notion, Airtable, etc.)

---

## Claw Code — New Project Directive

Every new PhoennixAI project starts with:
```bash
claw install --claude
graphify claude install
```

Applies to all three brands:
- **PhoennixAI** (Mission Control, client-intake, holographic dashboard)
- **Phantom Gaming Studio** (phantom-gaming-studio)
- **Cupcakes & Cocktails** (cupcakes-and-cocktails)

---

## Files to read before starting any session

| File | When to read |
|---|---|
| `CLAUDE-v3.md` | Every session — permanent memory |
| `BETA_LAUNCH_PROMPT.txt` | Any beta / MOS / email / brand voice task |
| `PhoennixAI_BrandGuidelines.html` | Any design or copy task |
| `phoennixai_beta_launch_kit.html` | Beta operations |
| `graphify-out/GRAPH_REPORT.md` | Architecture / codebase questions |
