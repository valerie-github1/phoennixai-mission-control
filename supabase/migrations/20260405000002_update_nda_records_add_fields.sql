-- ============================================================
-- Migration: add full_name and status to nda_records
-- Project:   phoennixai-backend (erfvunwhpsdbyyayzdimz)
-- Created:   2026-04-05
-- Ref:       PAI-DB-003
-- ============================================================
-- Run AFTER 20260405000000_create_nda_records.sql
-- https://supabase.com/dashboard/project/erfvunwhpsdbyyayzdimz/sql
-- ============================================================

ALTER TABLE public.nda_records
  ADD COLUMN IF NOT EXISTS full_name text,
  ADD COLUMN IF NOT EXISTS company   text,
  ADD COLUMN IF NOT EXISTS status    text NOT NULL DEFAULT 'signed';

COMMENT ON COLUMN public.nda_records.full_name IS 'Signer full name from sigName field';
COMMENT ON COLUMN public.nda_records.company   IS 'Signer business name from sigCompany field';
COMMENT ON COLUMN public.nda_records.status    IS 'Record status: signed | revoked';
