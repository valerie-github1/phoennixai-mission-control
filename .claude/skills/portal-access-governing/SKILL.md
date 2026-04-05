# Skill: portal-access-governing

Defines the PhoennixAI 3-tier RBAC framework for portal access control, Supabase RLS rules, audit logging, and agent responsibilities.

---

## Access Tiers

### Tier 1 — Founder
- **Who:** Valerie Wilcox only
- **Access:** Full read/write across all Supabase tables, all apps, all agent configurations, billing, and infrastructure settings
- **Auth:** Supabase service role key (never exposed to client). Direct dashboard access only.
- **Agent owner:** GRID (access decisions), NEXUS (implementation), SCRIBE (audit trail)

### Tier 2 — Trusted Leadership
- **Who:** Dilpreet Kaur (CTO), designated senior team members (written authorisation from Valerie required)
- **Access:** Read access to all non-financial tables. Write access to `tasks`, `sessions`, `notes`, `agents`. No access to `revenue`, `billing`, or service role operations.
- **Auth:** Supabase magic link (OTP). Email must be on the `trusted_users` allowlist.
- **Agent owner:** SIGNAL (vetting), SAGE (governance review), GRID (access grant)

### Tier 3 — Beta Testers
- **Who:** Approved beta registrants who have signed the NDA (status = 'signed' in `nda_records`)
- **Access:** Read-only access to their own profile data. Write access to `beta_waitlist` (own record only), `nda_records` (insert only). No access to internal tables.
- **Auth:** Supabase magic link (OTP). Email must exist in both `beta_waitlist` and `nda_records` with `status = 'signed'`.
- **Agent owner:** RELAY (onboarding), ECHO (support), GUARDIAN (access enforcement — planned)

---

## Supabase RLS Rules

### beta_waitlist
```sql
-- Anon insert only (public waitlist form)
CREATE POLICY "anon_insert_beta_waitlist"
  ON public.beta_waitlist FOR INSERT TO anon WITH CHECK (true);

-- Authenticated users can read their own record only
CREATE POLICY "auth_select_own_waitlist"
  ON public.beta_waitlist FOR SELECT TO authenticated
  USING (email = auth.jwt() ->> 'email');
```

### nda_records
```sql
-- Anon insert only (NDA SignHub — pre-auth flow)
CREATE POLICY "anon_insert_nda_records"
  ON public.nda_records FOR INSERT TO anon WITH CHECK (true);

-- Authenticated users can read their own NDA record
CREATE POLICY "auth_select_own_nda"
  ON public.nda_records FOR SELECT TO authenticated
  USING (user_email = auth.jwt() ->> 'email');
```

### Internal tables (tasks, agents, sessions, etc.)
```sql
-- Only authenticated Tier 1/2 users (enforced via JWT custom claims)
CREATE POLICY "tier1_tier2_only"
  ON public.tasks FOR ALL TO authenticated
  USING ((auth.jwt() ->> 'user_tier') IN ('founder', 'leadership'));
```

---

## Next.js Middleware Patterns (Phase 2)

When the stack migrates to Next.js (Phase 2 Unlock 2), enforce access at the middleware layer:

```typescript
// middleware.ts
import { createMiddlewareClient } from '@supabase/auth-helpers-nextjs'
import { NextResponse } from 'next/server'

export async function middleware(req) {
  const res = NextResponse.next()
  const supabase = createMiddlewareClient({ req, res })
  const { data: { session } } = await supabase.auth.getSession()

  // Public routes — no auth required
  const publicRoutes = ['/', '/waitlist', '/nda', '/login']
  if (publicRoutes.includes(req.nextUrl.pathname)) return res

  // Protected routes — require session
  if (!session) {
    return NextResponse.redirect(new URL('/login', req.url))
  }

  // Tier-gated routes — require founder or leadership
  const adminRoutes = ['/admin', '/mission-control', '/agents']
  const userTier = session.user.user_metadata?.tier
  if (adminRoutes.some(r => req.nextUrl.pathname.startsWith(r))) {
    if (!['founder', 'leadership'].includes(userTier)) {
      return NextResponse.redirect(new URL('/dashboard', req.url))
    }
  }

  return res
}
```

---

## Audit Logging Requirements

Every access-sensitive event must write to the `agent_log` table:

```sql
-- Required fields for every audit log entry
INSERT INTO public.agent_log (
  agent,        -- Which agent triggered the event
  action,       -- e.g. 'ACCESS_GRANT', 'ACCESS_DENY', 'NDA_SIGNED', 'LOGIN_SUCCESS'
  user_email,   -- Who triggered it
  resource,     -- Which table/page/route was accessed
  tier,         -- User tier at time of event
  metadata,     -- JSONB: IP, user agent, timestamp, additional context
  created_at
) VALUES (...);
```

### Events that must be logged
| Event | Agent | Severity |
|---|---|---|
| Magic link sent | RELAY | INFO |
| Login success | NEXUS | INFO |
| Login failure (3+ attempts) | SIGNAL | WARN |
| NDA signed | SCRIBE | INFO |
| Tier 2 access granted | GRID | HIGH |
| Tier 1 action (any) | SCRIBE | HIGH |
| Unauthorised route access attempt | SIGNAL | WARN |
| Sign out | RELAY | INFO |

---

## Agent Responsibilities

| Agent | Role in Access Governance |
|---|---|
| **GUARDIAN** (planned, Agent 014) | Primary access enforcement agent. Owns allowlists, reviews access requests, flags anomalies. Not yet signed. |
| **GRID** (Agent 009) | Approves Tier 2 access grants. Ensures access changes are logged in Mission Control. |
| **NEXUS** (Agent 017) | Implements RLS policies, middleware, and auth flows. All access code must be reviewed by NEXUS before deploy. |
| **SCRIBE** (Agent 015) | Maintains the audit trail. Every access event logged. Every policy change documented. |
| **SIGNAL** (Agent 010) | Monitors for anomalous access patterns. Flags repeated failed logins, unusual IP ranges, off-hours access. |

---

## Rules

- Never expose the Supabase service role key to any client-side code. Anon key only on client.
- Every new table must have RLS enabled before any data is written to it.
- Any Tier 2 access grant requires written authorisation from Valerie (stored in `documents` table).
- GUARDIAN must review all RLS policy changes before they are applied in production.
- All auth flows must use Supabase magic link (OTP). No passwords. No OAuth in Phase 0.
- `nda_records.status` must be `'signed'` before a beta tester is granted dashboard access.
- Audit log entries are immutable — no UPDATE or DELETE policy on `agent_log`.
