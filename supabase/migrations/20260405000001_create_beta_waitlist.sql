-- ============================================================
-- Migration: create beta_waitlist table
-- Project:   phoennixai-backend (erfvunwhpsdbyyayzdimz)
-- Created:   2026-04-05
-- Ref:       PAI-DB-002
-- ============================================================
-- Run this in the Supabase SQL editor:
-- https://supabase.com/dashboard/project/erfvunwhpsdbyyayzdimz/sql
-- ============================================================

CREATE TABLE IF NOT EXISTS public.beta_waitlist (
  id            uuid        DEFAULT gen_random_uuid() PRIMARY KEY,
  full_name     text        NOT NULL,
  email         text        NOT NULL,
  business_type text,
  source        text,
  challenge     text,
  tier          text,
  created_at    timestamptz DEFAULT now()
);

-- Enable Row Level Security
ALTER TABLE public.beta_waitlist ENABLE ROW LEVEL SECURITY;

-- Policy: allow anonymous inserts (public-facing waitlist form)
CREATE POLICY "anon_insert_beta_waitlist"
  ON public.beta_waitlist
  FOR INSERT
  TO anon
  WITH CHECK (true);

-- No SELECT/UPDATE/DELETE for anon — write-only from client.
-- Only service role (dashboard / server) can read records.
