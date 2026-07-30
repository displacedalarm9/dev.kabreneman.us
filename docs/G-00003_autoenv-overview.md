UNISYS — AUTOENV ENVIRONMENT LAYER OVERVIEW
G-00003_
G-Class Governance Overview

Page ID:      G-00003_
System:       AUTOENV
Class Letter: G
Scope:        SYSTEM-WIDE (AUTOENV subsystem)
Document Type: Governance Overview (G-Class)
Status:       ACTIVE
TSN:          TSN-20260404-AUTOENV
AUID:         AUID-G-00003
Author:       Kyle Breneman
Date Created: 2026-04-04

─────────────────────────────────────────────────────────────────────────────────────────
Section 1 — Purpose
─────────────────────────────────────────────────────────────────────────────────────────

This document defines the governance, architecture, and operational rules for AUTOENV —
the UNISYS Environment and Daemon Layer. AUTOENV is the execution substrate that hosts
all UNISYS pawn daemons and front-line executables.

AUTOENV sits between the DOCSYS document subsystem and the raw data/compute layer. It
provides the runtime environment in which automated analysis, report generation, and
dataset processing occur.

─────────────────────────────────────────────────────────────────────────────────────────
Section 2 — Scope
─────────────────────────────────────────────────────────────────────────────────────────

This governance document applies to:

  — All AUTOENV daemons and executables
  — AE-RPG (AUTOENV Report Generator)
  — Any future AUTOENV pawn components
  — Interactions between AUTOENV and DOCSYS, SyncKit, and AE-RPG

This document does not govern:

  — DOCSYS document lifecycle (governed by G-00002 / P-00000)
  — SyncKit transport operations (governed separately)
  — Identity assignment (governed by X-00002_)

─────────────────────────────────────────────────────────────────────────────────────────
Section 3 — AUTOENV Architecture
─────────────────────────────────────────────────────────────────────────────────────────

3.1 Role in the UNISYS Stack

AUTOENV occupies the computation and consolidation layer of UNISYS:

  DOCSYS         — Document subsystem (pages, PMFs, identity, lifecycle)
  ↕
  AUTOENV        — Environment/daemon layer (pawn executables, report generation)
  ↕
  SyncKit        — Transport/sync layer (GitHub ↔ DOCSYS sync)

3.2 AUTOENV Responsibilities

  — Host and execute pawn daemons (e.g., AE-RPG)
  — Read structured input data from DOCSYS artifacts and synced datasets
  — Process and analyze data according to governance-approved logic
  — Produce deterministic, fixed-format outputs
  — Hand off generated artifacts to SyncKit for sync
  — Treat all immutable identity fields as read-only (per X-00002_, Section 5)

3.3 AUTOENV Non-Responsibilities

AUTOENV does NOT:

  — Assign TSNs, AUIDs, or UDISes (identity authority belongs to DOCSYS)
  — Modify lifecycle state (lifecycle authority belongs to DOCSYS/SyncKit)
  — Generate metadata schemas (governed by X-00002_)
  — Silently overwrite any artifact or metadata field

─────────────────────────────────────────────────────────────────────────────────────────
Section 4 — AUTOENV Daemons
─────────────────────────────────────────────────────────────────────────────────────────

4.1 Daemon Classification

AUTOENV daemons are classified as "pawns" — subordinate executables that operate under
governance constraints defined by DOCSYS/X-Class documents. Pawns may not:

  — Invent or reuse identity fields
  — Alter lifecycle state
  — Override metadata rules

4.2 Current Daemons

  Daemon     Location               Purpose
  ─────────  ─────────────────────  ────────────────────────────────────────────────
  AE-RPG     autoenv/ae_rpg.py      AUTOENV Report Generator — produces R-Class reports
                                    by reading synced data, analyzing patterns, and
                                    instantiating fixed-format report templates.

4.3 Daemon Governance Requirements

All AUTOENV daemons must:

  1. Validate all input metadata before processing (TSN, AUID, required fields)
  2. Treat immutable fields (TSN, AUID, UDIS, CreatedBy, CreatedOn, Class) as read-only
  3. Log all operations with sufficient detail for audit tracing
  4. Fail loudly on metadata errors — never guess or auto-repair identity
  5. Request UDIS from DOCSYS when instantiating a report output
  6. Pass generated artifacts to SyncKit; never self-publish

─────────────────────────────────────────────────────────────────────────────────────────
Section 5 — AE-RPG (AUTOENV Report Generator)
─────────────────────────────────────────────────────────────────────────────────────────

5.1 Definition

AE-RPG is the primary AUTOENV daemon. It is a cross-system programmatic utility that:

  — Reads synced datasets (validations, reviews, reports, and other structured inputs)
  — Accepts standardized prompt/parameter inputs
  — Analyzes and aggregates data to surface patterns (e.g., "which month overspent?")
  — Produces fixed-format R-Class reports with:
      • Static layout (template-driven, deterministic)
      • Dynamic header/footer applied only at instantiation time

AE-RPG is NOT a Report, Form, Procedure, or Workflow. It is a programmatic component
that produces R-Class report artifacts.

5.2 AE-RPG Input Contract

Inputs to AE-RPG must include:

  Field           Required   Description
  ─────────────   ────────   ──────────────────────────────────────────────────────
  tsn             YES        Inherited TSN from the originating event
  data_sources    YES        List of structured input files or datasets
  report_type     YES        Report type identifier (maps to a template)
  parameters      YES        Analysis parameters (date range, filters, thresholds)
  operator        YES        Operator ID (passed through to output metadata)
  template_id     YES        Template ID for the fixed-format output layout

5.3 AE-RPG Output Contract

Outputs from AE-RPG:

  — One R-Class report file (fixed-format, static layout)
  — One PMF (Provenance Metadata File) for the generated report
  — A run log entry

Output metadata fields assigned by AE-RPG:

  Field        Value
  ──────────   ───────────────────────────────────────────────────────────────────
  TSN          Inherited from input (never regenerated)
  AUID         New AUID requested from DOCSYS identity layer
  UDIS         New UDIS requested from DOCSYS at instantiation time
  Class        R (always — AE-RPG produces R-Class outputs)
  CreatedBy    AE-RPG (daemon identity)
  CreatedOn    Timestamp at instantiation

5.4 AE-RPG Constraints

  — AE-RPG must never bake identity or lifecycle logic into report content
  — Dynamic header/footer is applied once, at instantiation — never re-applied
  — AE-RPG must write a PMF for every generated report
  — AE-RPG must hand off to SyncKit after generation; it does not self-publish

─────────────────────────────────────────────────────────────────────────────────────────
Section 6 — AUTOENV Metadata Compliance
─────────────────────────────────────────────────────────────────────────────────────────

Per X-00002_ (UNISYS Metadata Standard, Section 5 and Section 8):

  — AUTOENV daemons must treat immutable fields as read-only
  — AE-RPG must validate input dataset structure before processing
  — AE-RPG must verify presence of required metadata fields
  — AE-RPG must confirm template compatibility before instantiation
  — AE-RPG must verify identity fields before generating output

Violation handling:

  — Any metadata validation failure must halt execution
  — Failures must be logged with the offending field and value
  — Failures must be surfaced to the operator (not silently swallowed)

─────────────────────────────────────────────────────────────────────────────────────────
Section 7 — AUTOENV Directory Structure
─────────────────────────────────────────────────────────────────────────────────────────

  autoenv/
  ├── README.md       AUTOENV module overview (human-readable entry point)
  └── ae_rpg.py       AE-RPG daemon — AUTOENV Report Generator implementation

─────────────────────────────────────────────────────────────────────────────────────────
Section 8 — Cross-References
─────────────────────────────────────────────────────────────────────────────────────────

  UNISYS metadata standard.md (X-00002_)              Metadata rules; immutability constraints
  DOCSYS document creation governance (G-00002/P-00000) Document class governance
  autoenv/README.md                                    AUTOENV module README
  autoenv/ae_rpg.py                                    AE-RPG daemon implementation
  L-00001_.md                                          Outstanding Document Index

─────────────────────────────────────────────────────────────────────────────────────────
Section 9 — Revision History
─────────────────────────────────────────────────────────────────────────────────────────

  2026-04-04   G-00003_   v1.0   Initial creation   Kyle Breneman / @copilot
               TSN-20260404-AUTOENV
               AUID-G-00003

Unified System Architecture™   UNISYS™   ©2026 Kyle Breneman

G-00003_  |  AUTOENV Environment Layer Overview  |  Status: ACTIVE  |  2026-04-04
