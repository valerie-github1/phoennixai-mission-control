# Skill: vercel-deploy

Handles Vercel deployment operations for PhoennixAI apps.

## What this skill does

- Deploy HTML/JS apps to Vercel from the local repo
- Update or replace the Vercel deployment URL across HTML files in the repo
- Verify a Vercel deployment is live and returning the correct content
- Swap between Vercel preview URLs and the canonical production URL

## When to use

- When a new Vercel deployment is created and internal links need updating
- When the Vercel URL changes (e.g. from a project rename) and all `href`/`src` references need a bulk find-and-replace
- When checking whether a Vercel-hosted page is live and up to date

## Rules

- The canonical production URL pattern is: `phoennixai-mission-control.vercel.app`
- When replacing Vercel URLs across HTML files, use a targeted sed or Grep+Edit approach -- never overwrite file content blindly
- Always run `git diff --stat` after a bulk URL replacement to confirm the scope of changes before committing
- Vercel deployments are secondary hosting. GitHub Pages (`valerie-github1.github.io/phoennixai-mission-control/`) remains the primary live environment in Phase 0.

## URL reference

| Context | URL |
|---------|-----|
| Primary (GitHub Pages) | `https://valerie-github1.github.io/phoennixai-mission-control/` |
| Vercel (current) | `https://phoennixai-mission-control.vercel.app` |
