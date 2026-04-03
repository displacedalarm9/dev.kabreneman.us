# dev.kabreneman.us — UNISYS

Unified system repository for the UNISYS platform.

**Consolidation note:** This repository now incorporates content from `kabreneman.us`, `KABDMSV2`, and the prior `dev.kabreneman.us` scaffold. All migrated artifacts carry a `UNISYS_IMPORT_RECORD` metadata block identifying their original location. See [M-00002.md](M-00002.md) for the full migration manifest and [L-00001_.md](L-00001_.md) for the complete document index.

## Structure

| Directory | Contents | Purpose |
|-----------|----------|---------|
| `docs/` | Guides, standards, procedures, lifecycle docs, archive | Canonical context documents and operational guides |
| `docs/procedures/` | Changeover, changes, emergency, matrix, schedule, audit | Operational procedure documents |
| `docs/standards/` | Coding, documentation, configuration, file organization | Standards from KABDMSV2 |
| `docs/archive/` | Historical and archived documents | Archive of migrated one-off artifacts |
| `scripts/` | `fix_filenames.py`, `workcap_analyzer.py` | Automation scripts and utilities |
| `financials/` | WORKCAP, budgeting, and financial planning modules | Financial documents and templates |
| `financials/templates/` | 17 financial templates (daily, weekly, monthly, variance, etc.) | WORKCAP template library |
| `devices/` | Node configs (XML), system info | DEVICEOPS configurations and hardware specifications |
| `devices/configs/` | `config_NODE-*.xml` | XML configs for NODE-OPS-001, NODE-VR-002, NODE-ARC-003 |
| `.github/` | Copilot instructions and GitHub configuration | Governance and contributor guidelines |

## Key Governance Artifacts

| Artifact | Purpose |
|----------|---------|
| [M-00001.md](M-00001.md) | MANIFEST Founding Page — governs M-class artifacts |
| [M-00002.md](M-00002.md) | Migration Manifest — enumerates all 43 imported artifacts |
| [L-00001_.md](L-00001_.md) | Outstanding Document Index — master index of all 48 artifacts |
| [UNISYS metadata standard.md](UNISYS%20metadata%20standard.md) | X-00002_ — governs TSN/AUID/UDIS semantics |
| [DOCSYS document creation governance](DOCSYS%20document%20creation%20governance) | G-00002 — document class definitions and workflows |

## Consolidated Sources

| Source Repository | Artifacts | Migration TSN |
|-------------------|-----------|---------------|
| `displacedalarm9/kabreneman.us` | 33 files | TSN-20260403-MIGRATE |
| `displacedalarm9/KABDMSV2` | 10 files | TSN-20260403-MIGRATE |
| `dev.kabreneman.us` (prior scaffold) | 5 native UNISYS artifacts | — |

See [`.github/copilot-instructions.md`](.github/copilot-instructions.md) for contributor guidelines and UNISYS principles.