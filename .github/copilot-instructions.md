# UNISYS — GitHub Copilot Instructions

## Section 6: GitHub Copilot Workflow & Principles

---

### Overview

This repository (`dev.kabreneman.us`) serves as the **UNISYS** unified system repository. All components, documentation, scripts, financial modules, and device specifications relevant to the UNISYS system are consolidated here.

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
