# CLAUDE-v2.md — PhoennixAI Plugin Bootstrap
> Run all commands below to wire in every agent superpower across all PhoennixAI projects.
> One file. One run. Full stack.

---

## Plugin Installs

```bash
# 1. Graphify — knowledge graph for every project
pip3 install graphifyy
graphify install
graphify claude install

# 2. Vercel — deploy from Claude Code
npx plugins add vercel/vercel-plugin

# 3. GitHub MCP — full repo access from Claude
npx -y @modelcontextprotocol/server-github

# 4. Supabase MCP — database access from Claude
npx -y @supabase/mcp-server-supabase@latest

# 5. Composio MCP — 250+ tool integrations
npx -y composio-mcp@latest
```

---

## MCP Servers (added to ~/.claude/settings.json)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    },
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp-server-supabase@latest", "--access-token", "${SUPABASE_ACCESS_TOKEN}"]
    },
    "composio": {
      "command": "npx",
      "args": ["-y", "composio-mcp@latest", "start", "--api-key", "${COMPOSIO_API_KEY}"]
    },
    "graphify": {
      "command": "graphify",
      "args": [".", "--mcp"]
    }
  }
}
```

---

## Hooks (auto-applied by graphify claude install)

| Hook | Trigger | Action |
|---|---|---|
| PreToolUse | Glob / Grep | Read knowledge graph before searching |
| PostToolUse | Write / Edit | Rebuild graph after every code change |
| SessionStart | New session | Remote control + graphify re-index |

---

## New Project Bootstrap (Claw Code directive)

```bash
mkdir my-project && cd my-project
git init
claw install --claude
graphify claude install
```

---

## Brands covered

- **PhoennixAI** — `phoennixai-mission-control`, `client-intake`, `phoennixai-holographic-dashboard`
- **Phantom Gaming Studio** — `phantom-gaming-studio`
- **Cupcakes & Cocktails** — `cupcakes-and-cocktails`

## Contacts

| Role | Email |
|---|---|
| CEO / Founder | valerie@phoennixai.com |
| CTO | dilpreet@phoennixai.com |
| Remote Control | phoenixdigitec3@gmail.com |
| Personal | wilcox.valerie@yahoo.co.uk |
