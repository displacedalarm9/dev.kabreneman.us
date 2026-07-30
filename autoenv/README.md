# autoenv/

AUTOENV — UNISYS Environment and Daemon Layer

This module contains the AUTOENV subsystem: the execution substrate that hosts all
UNISYS pawn daemons and front-line executables.

## Overview

AUTOENV sits between the DOCSYS document subsystem and the raw data/compute layer.
It provides the runtime environment for automated analysis, report generation, and
dataset processing across UNISYS.

## Governance

AUTOENV is governed by `docs/G-00003_autoenv-overview.md`.
All AUTOENV daemons must comply with the UNISYS Metadata Standard (`UNISYS metadata standard.md`, X-00002_).

## Components

| Component    | File          | Purpose                                      |
|--------------|---------------|----------------------------------------------|
| AE-RPG       | `ae_rpg.py`   | AUTOENV Report Generator — produces R-Class reports from synced datasets |

## Constraints

- AUTOENV daemons treat all immutable identity fields (TSN, AUID, UDIS, CreatedBy, CreatedOn, Class) as **read-only**.
- AUTOENV never self-assigns TSNs or AUIDs — identity is assigned by the DOCSYS identity layer.
- All daemon operations must be logged with sufficient detail for audit tracing.
- Failures must surface loudly; no silent swallowing of metadata errors.

## Related

- `docs/G-00003_autoenv-overview.md` — AUTOENV Governance Overview
- `UNISYS metadata standard.md` — Metadata rules (X-00002_)
- `L-00001_.md` — Outstanding Document Index

---

Unified System Architecture™  UNISYS™  ©2026 Kyle Breneman
