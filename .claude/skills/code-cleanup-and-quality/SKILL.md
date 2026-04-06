---
name: code-cleanup-and-quality
description: >
  Automated code cleanup, refactoring, and quality enforcement for PhoennixAI.
  Use whenever NEXUS writes or edits code, before any commit to main, and at
  every sprint end. Combines Code Cleanup Refactoring, Safe Code Refactoring,
  and Code Quality Standards into one standing protocol. PROBE must sign off
  before any file built under this skill ships to production.
---

# PhoennixAI Code Cleanup and Quality Skill

## Identity

This skill governs all code quality, cleanup, and refactoring operations
across the PhoennixAI codebase. NEXUS applies this skill when building.
PROBE applies it when reviewing. No file ships without passing this protocol.

## Phase 1: Code Cleanup
Run on every file NEXUS touches before committing.
- Remove dead code, commented-out blocks, unused variables
- Fix inconsistent indentation (2 spaces HTML/JS, 4 for Python)
- Clean import order: external libraries first, then internal
- Remove duplicate CSS class declarations
- Remove console.log statements left from debugging

## Phase 2: Safe Code Refactoring
Use when touching more than 3 files or restructuring logic.
1. Document current behaviour first
2. Refactor in atomic steps
3. Confirm behaviour unchanged after each step
4. Run codebase-auditor to confirm no regressions

## Phase 3: Code Quality Standards
- Naming: descriptive, consistent, no abbreviations
- Comments: present on all non-obvious logic
- Functions: single responsibility, under 50 lines
- Error handling: every async call has try/catch with user-visible feedback
- Security: no credentials except Supabase anon key in client files
- Testability: manually testable by PROBE without special setup

## PhoennixAI Non-Negotiable Standards
- Tailwind CDN JIT only (cdn.tailwindcss.com)
- No em dashes in any file
- PhoennixAI always two Ns
- Copyright year: 2026
- Footer tagline: Created to Create. Intelligent by nature.
- Fonts: Bebas Neue, DM Sans, DM Mono, Playfair Display only
- All links use: phoennixai-mission-control-eight.vercel.app
- No GitHub Pages domain references

## PROBE Sign-Off Checklist
- [ ] No dead code or debug statements
- [ ] All async calls have try/catch
- [ ] No em dashes
- [ ] PhoennixAI two Ns throughout
- [ ] Copyright 2026
- [ ] Footer tagline on all pages
- [ ] No wrong domain references
- [ ] Tailwind JIT CDN confirmed
- [ ] No credentials beyond Supabase anon key
- [ ] codebase-auditor score: no worker below 7

## Standing Rules
- This skill runs automatically, NEXUS does not wait to be asked
- PROBE sign-off mandatory before any merge to main
- Safe Code Refactoring required for changes touching 3 or more files
- Sprint-end audit is non-negotiable, GRID owns the reminder
- SCRIBE files audit report in Document Hub after every sprint
