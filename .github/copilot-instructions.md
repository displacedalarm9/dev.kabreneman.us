# UNISYS — GitHub Copilot Instructions

## Section 1: System Context

You're operating inside a governed system with its own architecture. When generating or editing code in this repo, treat these as hard constraints.

- **UNISYS** = overarching governed system.
- **DOCSYS** = document subsystem (Pages, PMFs, identity, lifecycle).
- **AUTOENV** = environment/daemon layer (pawn/front‑line executables).
- **DOCSYS SynchronizationKit** = syncs DOCSYS artifacts and metadata with GitHub.

Code in this repo is assumed to be part of one of those layers — never "free‑floating."

---

## Section 2: Identity and Metadata

- Every governed artifact must support:
  - **TSN** (event identity)
  - **AUID** (artifact identity)
  - **UDIS** (instance identity, if applicable)
- Identity is immutable and must not be silently changed or reused.
- SyncKit and any tools must preserve identity and PMF metadata.

When in doubt, do not invent IDs — expect them to be passed in or read from metadata.

---

## Section 3: AE‑RPG (AUTOENV Report Generator)

AE‑RPG is a cross‑system daemon/utility that:
- reads synced data (validations, reviews, reports, other datasets)
- accepts standardized prompts/parameters
- analyzes/aggregates data to find patterns (e.g., "which month overspent?")
- outputs fixed‑format reports with:
  - static layout
  - dynamic header/footer applied at instantiation time only

AE‑RPG is **not** a Report, Form, Procedure, or Workflow. It is a programmatic component that produces R‑Class reports.

When generating code for AE‑RPG:
- Expect structured inputs (files, JSON, DB, etc.) and structured outputs (report files).
- Keep formatting deterministic and template‑driven.
- Do not bake identity or lifecycle logic into AE‑RPG — those come from DOCSYS/PMF.

---

## Section 4: DOCSYS SynchronizationKit

Responsible for syncing:
- Pages
- PMFs
- related artifacts

between local DOCSYS and GitHub.

Must:
- preserve identity fields
- preserve lifecycle state
- avoid collisions
- log or surface conflicts rather than silently overwriting

When generating code around SyncKit:
- Prefer explicit, auditable operations (clear logs, clear error states).
- Never "auto‑fix" identity or metadata — only detect and report.

---

## Section 5: General Behavior Expectations

- **Determinism**: same inputs → same outputs.
- **Auditability**: logs and outputs should make decisions traceable.
- **No hidden magic**: avoid implicit behavior that changes identity, lifecycle, or governance state.
- **Separation of concerns**:
  - DOCSYS = documents, metadata, lifecycle
  - AUTOENV/AE‑RPG = computation and consolidation
  - SyncKit = transport/sync

If a task is ambiguous, prefer:
1. Preserving identity and metadata.
2. Producing explicit, inspectable outputs.
3. Failing loudly rather than guessing.

---

## Section 6: GitHub Copilot Workflow & Principles

---

### Overview

This repository (`displacedalarm9/dev.kabreneman.us`) serves as the **UNISYS** unified system repository. All components, documentation, scripts, financial modules, and device specifications relevant to the UNISYS system are consolidated here.

---

### Repository Structure

```
dev.kabreneman.us/
├── .github/               # Copilot instructions, workflows, and GitHub configuration
│   └── copilot-instructions.md
├── docs/                  # Documentation: Canonical Context, system instructions, guides
├── scripts/               # Asset identity generators, acquisition workflows, automation
├── financials/            # WORKCAP and financial modules
├── devices/               # DEVICEOPS and hardware specifications
└── README.md
```

---

### Principles

1. **Unified Source of Truth**: This repository is the single canonical source for all UNISYS system components. Avoid duplicating content across repositories.

2. **Incremental Migration**: When migrating content from `kabreneman.us` or `kabdmsv2`, bring only relevant, non-deprecated components. Audit before migrating.

3. **Clean Repository Hygiene**:
   - Do not commit secrets, credentials, or sensitive data.
   - Exclude build artifacts and temporary files via `.gitignore`.
   - Keep commits small and focused with descriptive messages.

4. **Deprecation Protocol**: Once all applicable content has been migrated from `kabdmsv2`, that repository is to be marked deprecated with an archival README.

---

### Workflow Guidelines

#### Branching Strategy
- Use `main` as the stable production branch.
- Feature work and migrations go through named branches: `feature/`, `migrate/`, `fix/`.
- Open Pull Requests for all changes; do not push directly to `main`.

#### Commit Messages
- Use the imperative mood: "Add financial module scaffold", "Migrate DEVICEOPS specs".
- Reference related issues or migration tasks where applicable.

#### Pull Requests
- Include a summary of what was added, changed, or removed.
- For migrations from `kabdmsv2` or `kabreneman.us`, note the source and confirm the original has been audited for deprecation.

---

### Directory Ownership

| Directory     | Purpose                                              |
|---------------|------------------------------------------------------|
| `docs/`       | Canonical context documents, system guides, notes    |
| `scripts/`    | Automation scripts, asset generators, workflows      |
| `financials/` | WORKCAP, budgeting, and financial planning modules   |
| `devices/`    | DEVICEOPS configurations and hardware specifications |

---

### Migration Checklist (from kabdmsv2 / kabreneman.us)

- [ ] Audit source repository for outdated or deprecated files
- [ ] Identify components applicable to UNISYS
- [ ] Copy relevant files into the appropriate subdirectory
- [ ] Update internal references and paths as needed
- [ ] Confirm original content is no longer needed in the source repo
- [ ] Mark source repository as deprecated (when fully migrated)

---

*This file governs Copilot and contributor behavior within the UNISYS system repository.*
