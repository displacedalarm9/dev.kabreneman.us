UNISYS — CODESPACE TRANSFER AUDIT AND RECOMMENDATIONS
REP-00001
REP-Class Report

Page ID:      REP-00001
System:       DOCSYS
Class Letter: REP
Scope:        CROSS-REPOSITORY
Document Type: Report (REP-Class)
Status:       ACTIVE
TSN:          TSN-20260403-CSAUDIT
AUID:         AUID-REP-00001
Author:       Kyle Breneman
Date Created: 2026-04-03

Section 1 — Purpose

This report documents the results of an audit performed on 2026-04-03 to assess the
transfer status of content from the two predecessor repositories (kabreneman.us and KABDMSV2)
into the unified UNISYS destination repository (dev.kabreneman.us).

The audit covers:

  — Inventory of content in each source codespace
  — Confirmation of what has and has not been transferred
  — Gap analysis identifying missing or incomplete migrations
  — Recommended next actions for completing the consolidation

Section 2 — Scope

  Source A:     displacedalarm9/kabreneman.us      (KABDMSV2 public system files)
  Source B:     displacedalarm9/KABDMSV2           (DMS V2 governance and device configs)
  Destination:  displacedalarm9/dev.kabreneman.us  (UNISYS unified repository)

  Audit date:   2026-04-03
  Auditor:      @copilot acting under direction of Kyle Breneman (displacedalarm9)
  Scope limit:  Public repository content only. Local file systems and private repositories
                were not directly accessible and are referenced by documentation only.

Section 3 — Methodology

  1. Enumerated all files and directories in displacedalarm9/kabreneman.us (default branch: master)
  2. Enumerated all files and directories in displacedalarm9/KABDMSV2 (default branch: production)
  3. Enumerated all files and directories in displacedalarm9/dev.kabreneman.us (default branch: main)
  4. Cross-referenced each source artifact against the destination
  5. Classified each artifact as: TRANSFERRED, PARTIAL, NOT TRANSFERRED, or NOT APPLICABLE
  6. Documented findings and recommendations

Section 4 — Current State of dev.kabreneman.us

As of 2026-04-03, the destination repository contains the following artifacts:

  File / Directory                          Status
  ────────────────────────────────────────  ─────────────────────────────────────
  M-00001.md                                ACTIVE — MANIFEST Founding Page
  UNISYS metadata standard.md              ACTIVE — X-00002 Constitutional Standard
  DOCSYS document creation governance      ACTIVE — G-00002 Governance Document
  README.md                                 ACTIVE — Repository overview
  .github/copilot-instructions.md          ACTIVE — Copilot governance instructions
  devices/README.md                         ACTIVE — Placeholder
  docs/README.md                            ACTIVE — Placeholder
  financials/README.md                      ACTIVE — Placeholder
  scripts/README.md                         ACTIVE — Placeholder

  Total substantive artifacts in destination: 5 (governance/constitutional)
  Total placeholder artifacts:                4 (directory READMEs only)

  Observation: The destination repository has established the UNISYS constitutional layer
  but contains no operational content migrated from either source repository.

Section 5 — Source A Inventory: kabreneman.us

5.1 Root-Level Artifacts

  Artifact                     Size      Transfer Status         Notes
  ───────────────────────────  ────────  ──────────────────────  ────────────────────────
  WorkingCapital.md            6.0 KB    NOT TRANSFERRED         → financials/ (review)
  allocation.md                1.1 KB    NOT TRANSFERRED         → financials/ (review)
  cashflowsfy26.md             3.2 KB    NOT TRANSFERRED         → financials/ (review)
  expenses.md                  2.2 KB    NOT TRANSFERRED         → financials/ (review)
  obligations.md               1.1 KB    NOT TRANSFERRED         → financials/ (review)
  obligationadherence.md       5.2 KB    NOT TRANSFERRED         → financials/ (review)
  progress.md                  4.6 KB    NOT TRANSFERRED         → docs/ or deprecated
  review.md                    1.3 KB    NOT TRANSFERRED         → docs/ or deprecated
  standards.md                 6.2 KB    NOT TRANSFERRED         → docs/ (review)
  OPERCAP1.xlsm                92.4 KB   NOT TRANSFERRED         → financials/ (archived)
  debts.csv                    2.2 KB    NOT TRANSFERRED         SENSITIVE — backup only
  topics.json                  241 B     NOT TRANSFERRED         → metadata (review)

5.2 docs/ Directory (kabreneman.us)

  Artifact                     Size      Transfer Status         Notes
  ───────────────────────────  ────────  ──────────────────────  ────────────────────────
  automation-guide.md          4.1 KB    NOT TRANSFERRED         → docs/ (adapt to UNISYS)
  canonical-context.md         8.4 KB    NOT TRANSFERRED         Superseded by UNISYS docs
  filename.md                  575 B     NOT TRANSFERRED         → docs/ (adapt to UNISYS)
  folder-audit.md              1.0 KB    NOT TRANSFERRED         Superseded by this report
  history.md                   932 B     NOT TRANSFERRED         → docs/ (archive/reference)
  metadata-wizard.md           10.3 KB   NOT TRANSFERRED         → docs/ (adapt to DOCSYS)
  report-standards.md          1.1 KB    NOT TRANSFERRED         → docs/ (adapt to DOCSYS)
  docs/project_support/        (dir)     NOT TRANSFERRED         Review for UNISYS relevance

5.3 procedures/ Directory (kabreneman.us)

  Artifact                     Size      Transfer Status         Notes
  ───────────────────────────  ────────  ──────────────────────  ────────────────────────
  changeover.md                855 B     NOT TRANSFERRED         → procedures/ (phase plan)
  changes.md                   1.5 KB    NOT TRANSFERRED         → procedures/ (UNISYS CR)
  emergency.md                 771 B     NOT TRANSFERRED         → procedures/ (adapt)
  matrix.md                    2.4 KB    NOT TRANSFERRED         → financials/ (adapt)
  schedule.md                  585 B     NOT TRANSFERRED         → procedures/ (adapt)

5.4 templates/ Directory (kabreneman.us)

  Artifact                     Transfer Status         Notes
  ───────────────────────────  ──────────────────────  ────────────────────────────────
  accounts.md                  NOT TRANSFERRED         → templates/ (WORKCAP template)
  daily.md                     NOT TRANSFERRED         → templates/ (WORKCAP template)
  distribution.md              NOT TRANSFERRED         → templates/ (WORKCAP template)
  index.md                     NOT TRANSFERRED         → templates/ (WORKCAP template)
  investment.md                NOT TRANSFERRED         → templates/ (WORKCAP template)
  monthly.md                   NOT TRANSFERRED         → templates/ (WORKCAP template)
  obligations.md               NOT TRANSFERRED         → templates/ (WORKCAP template)
  opercap1.md                  NOT TRANSFERRED         → archive (OPERCAP archived)
  quarterly.md                 NOT TRANSFERRED         → templates/ (WORKCAP template)
  reports.md                   NOT TRANSFERRED         → templates/ (WORKCAP template)
  sidu.md                      NOT TRANSFERRED         → templates/ (WORKCAP template)
  status.md                    NOT TRANSFERRED         → templates/ (WORKCAP template)
  utilities.md                 NOT TRANSFERRED         → templates/ (WORKCAP template)
  variance.md                  NOT TRANSFERRED         → templates/ (WORKCAP template)
  weekly.md                    NOT TRANSFERRED         → templates/ (WORKCAP template)
  templates/data/              NOT TRANSFERRED         → templates/data/ (review contents)
  templates/report/            NOT TRANSFERRED         → templates/report/ (review)

5.5 scripts/ Directory (kabreneman.us)

  Artifact                     Size      Transfer Status         Notes
  ───────────────────────────  ────────  ──────────────────────  ────────────────────────
  fix_filenames.py             (present) NOT TRANSFERRED         → scripts/ (adapt to UNISYS)
  workcap_analyzer.py          (present) NOT TRANSFERRED         → scripts/ (adapt to UNISYS)

5.6 configs/ Directory (kabreneman.us)

  Artifact                     Transfer Status         Notes
  ───────────────────────────  ──────────────────────  ────────────────────────────────
  config_NODE-OPS-001_*.xml    NOT TRANSFERRED         → devices/configs/ (see Source B)
  config_NODE-VR-002_*.xml     NOT TRANSFERRED         → devices/configs/ (see Source B)
  config_NODE-ARC-003_*.xml    NOT TRANSFERRED         → devices/configs/ (see Source B)

5.7 Other Directories (kabreneman.us)

  Directory                    Transfer Status         Notes
  ───────────────────────────  ──────────────────────  ────────────────────────────────
  archive/                     NOT TRANSFERRED         → Review for UNISYS relevance
  data/                        NOT TRANSFERRED         SENSITIVE — local/backup only
  logs/                        NOT TRANSFERRED         SENSITIVE — local/backup only
  projects/                    NOT TRANSFERRED         → Review for UNISYS relevance
  reports/                     NOT TRANSFERRED         SENSITIVE — local/backup only
  reviews/                     NOT TRANSFERRED         SENSITIVE — local/backup only
  shared/                      NOT TRANSFERRED         → Review for UNISYS relevance
  utilities/                   NOT TRANSFERRED         → Review for UNISYS relevance

5.8 Source A Summary

  Total directories audited:   11
  Total files audited:         ~50+
  Transferred:                 0
  Partially transferred:       0
  Not transferred:             ~50+
  Not applicable (sensitive):  ~10+ (data/, logs/, reviews/, reports/, debts.csv)

  Repository status: kabreneman.us is ACTIVE (31 open issues as of 2026-04-03).
  It is NOT marked as deprecated and is clearly still in active use.

Section 6 — Source B Inventory: KABDMSV2

6.1 Root-Level Artifacts

  Artifact                            Size       Transfer Status         Notes
  ──────────────────────────────────  ─────────  ──────────────────────  ────────────────
  SECURITY.md                         3.2 KB     NOT TRANSFERRED         Superseded by P-00001
  BRANCH_MERGE_SUMMARY.md             4.0 KB     NOT TRANSFERRED         → docs/ (archive)
  CODE_OF_CONDUCT.md                  5.1 KB     NOT TRANSFERRED         → Review (standard)
  CONTRIBUTING.md                     3.0 KB     NOT TRANSFERRED         → Review for UNISYS
  file-management.md                  7.1 KB     NOT TRANSFERRED         → docs/ (adapt)
  system-info-formatted.md            5.4 KB     NOT TRANSFERRED         → devices/ (adapt)
  sysinfo.txt                         942 KB     NOT TRANSFERRED         → devices/ (raw data)
  topics.json                         241 B      NOT TRANSFERRED         → metadata (review)

6.2 Node Configuration Files (KABDMSV2 root)

  Artifact                                  Transfer Status         Notes
  ────────────────────────────────────────  ──────────────────────  ──────────────────────
  config_NODE-OPS-001_Legion5Gen10.xml      NOT TRANSFERRED         → devices/configs/
  config_NODE-VR-002_LegionPro5Gen10.xml   NOT TRANSFERRED         → devices/configs/
  config_NODE-ARC-003_CustomArchival.xml    NOT TRANSFERRED         → devices/configs/

6.3 docs/ Directory (KABDMSV2)

  Artifact                                  Transfer Status         Notes
  ────────────────────────────────────────  ──────────────────────  ──────────────────────
  docs/docsys-lifecycle-stages.md           NOT TRANSFERRED         → docs/ (adapt to UNISYS)
  docs/standards/README.md                  NOT TRANSFERRED         Superseded by UNISYS docs
  docs/standards/coding-standards.md        NOT TRANSFERRED         → docs/ (adapt to UNISYS)
  docs/standards/configuration-standards.md NOT TRANSFERRED         → docs/ (adapt to UNISYS)
  docs/standards/documentation-standards.md NOT TRANSFERRED         → docs/ (adapt to UNISYS)
  docs/standards/file-organization.md       NOT TRANSFERRED         → docs/ (adapt to UNISYS)

6.4 procedures/ Directory (KABDMSV2)

  Artifact                                  Transfer Status         Notes
  ────────────────────────────────────────  ──────────────────────  ──────────────────────
  procedures/repository-audit-remediation.md NOT TRANSFERRED        → docs/ (adapt to UNISYS)

6.5 data/ Directory (KABDMSV2)

  Status: NOT TRANSFERRED — contains operational/sensitive data. Must remain outside the
  repository or be evaluated file-by-file before any migration.

6.6 Source B Summary

  Total directories audited:   4
  Total files audited:         ~20
  Transferred:                 0
  Partially transferred:       0
  Not transferred:             ~20
  Not applicable (sensitive):  ~3 (data/, sysinfo.txt — raw system data)

  Repository status: KABDMSV2 is ACTIVE (8 open issues, last updated 2025-12-23).
  It is NOT marked as deprecated.

Section 7 — Transfer Status Summary

  Category                     kabreneman.us    KABDMSV2     Total
  ───────────────────────────  ─────────────    ──────────   ──────
  Files confirmed transferred  0                0            0
  Files partially transferred  0                0            0
  Files not transferred        ~50+             ~17          ~67+
  Files sensitive (no migrate) ~15              ~3           ~18
  Files superseded by UNISYS   ~5               ~6           ~11

  Overall transfer completion: EARLY STAGE — constitutional layer established;
                               no operational content migrated.

  FINDING: Both source repositories remain active and contain content that has not
  been evaluated for migration. The UNISYS destination repository contains only the
  governance/constitutional foundation. The migration is at approximately 5–10% of
  estimated completion.

Section 8 — Detailed Findings

Finding F-001: Node Configurations Not Migrated
  Severity: HIGH
  Detail: Three node configuration XML files exist in both kabreneman.us/configs/ and
  KABDMSV2 root. These are system files (safe to commit) and belong in devices/configs/.
  devices/ in dev.kabreneman.us has only a README placeholder.
  Action required: Migrate all three node configs to devices/configs/.

Finding F-002: No Operational Templates Present
  Severity: HIGH
  Detail: 15+ WORKCAP templates from kabreneman.us/templates/ have not been migrated.
  These are system files (blank templates, no data) and are safe to commit.
  Action required: Migrate templates to a templates/ directory in dev.kabreneman.us,
  adapting naming conventions to UNISYS standards.

Finding F-003: No Procedures Directory
  Severity: HIGH
  Detail: Neither a procedures/ directory nor any P-class procedure documents
  (beyond P-00001, which was just created) exist in dev.kabreneman.us.
  Five procedures from kabreneman.us and one from KABDMSV2 need evaluation.
  Action required: Create procedures/ directory; evaluate and migrate applicable procedures.

Finding F-004: Scripts Not Migrated
  Severity: MEDIUM
  Detail: Two Python utility scripts (fix_filenames.py, workcap_analyzer.py) from
  kabreneman.us/scripts/ have not been migrated. The destination has a scripts/ directory
  placeholder only.
  Action required: Migrate scripts, updating internal path references for UNISYS structure.

Finding F-005: Financial Documents Not Migrated
  Severity: MEDIUM
  Detail: Multiple financial planning documents (WorkingCapital.md, allocation.md,
  cashflowsfy26.md, expenses.md, obligations.md, obligationadherence.md) have not been
  migrated. Some may contain sensitive data and require review before migration.
  Action required: Review each file; migrate non-sensitive documents to financials/.

Finding F-006: KABDMSV2 Standards Documents Not Migrated
  Severity: MEDIUM
  Detail: Five standards documents in KABDMSV2/docs/standards/ (coding, configuration,
  documentation, file-organization) have not been migrated or superseded.
  Action required: Review each; adapt applicable standards to DOCSYS/UNISYS format and
  register as P-class or X-class artifacts.

Finding F-007: Neither Source Repository Marked Deprecated
  Severity: LOW (current state, will escalate as migration progresses)
  Detail: Both kabreneman.us (31 open issues) and KABDMSV2 (8 open issues) remain
  active. Neither carries a deprecation notice. Active work is continuing in the
  predecessor repos alongside the new UNISYS repository.
  Action required: Establish a migration completion target date; add deprecation notices
  to source repos when migration is complete.

Finding F-008: No Migration Manifest (M-00002) Created
  Severity: LOW
  Detail: M-00001.md identifies M-00002 as a planned Migration Manifest. M-00002.md
  does not currently exist in dev.kabreneman.us. The migration cannot be tracked without it.
  Action required: Create M-00002.md as the official Migration Manifest per M-00001
  Section 7 specification.

Finding F-009: No Outstanding Document Index (L-class)
  Severity: LOW
  Detail: No L-class Outstanding Document Index has been created in dev.kabreneman.us.
  Action required: Create L-00001_.md as the master append-only artifact index.

Finding F-010: Sensitive Data Files Present in kabreneman.us
  Severity: HIGH (security note, not a transfer issue)
  Detail: debts.csv (2.2 KB) is committed to kabreneman.us. This file likely contains
  sensitive financial data (account names, debt amounts). Additionally, the data/ and
  reviews/ directories may contain sensitive filled templates.
  Action required: Audit kabreneman.us for sensitive files. Do NOT migrate debts.csv or
  similar files to dev.kabreneman.us. Ensure P-00001 guidelines are followed.

Section 9 — Recommendations

Priority 1 — IMMEDIATE (Complete within 1 week)

  REC-001: Apply security procedure P-00001 to dev.kabreneman.us now.
           Verify .gitignore covers all sensitive patterns. Document what is in
           ~/secure-kabreneman-backup/. This is the security foundation for the migration.

  REC-002: Audit kabreneman.us for sensitive committed data (Finding F-010).
           Review debts.csv and the data/ directory. If sensitive data was committed,
           remove it from history using BFG Repo Cleaner or git filter-repo.

  REC-003: Migrate three node configuration files to devices/configs/.
           These are: config_NODE-OPS-001_Legion5Gen10.xml,
                      config_NODE-VR-002_LegionPro5Gen10.xml,
                      config_NODE-ARC-003_CustomArchival.xml
           Source: Both kabreneman.us/configs/ and KABDMSV2 root (identical files).
           Destination: devices/configs/ in dev.kabreneman.us.
           Add UNISYS_IMPORT_RECORD metadata block to each file.

Priority 2 — SHORT TERM (Complete within 2–4 weeks)

  REC-004: Create M-00002.md — Migration Manifest (Finding F-008).
           This is the authoritative tracking artifact for the consolidation.
           Use type MF-CHK (Checklist Manifest) to track migration status of each artifact.

  REC-005: Create L-00001_.md — Outstanding Document Index (Finding F-009).
           This should be the master append-only index of all UNISYS artifacts
           as they are created and registered.

  REC-006: Migrate and adapt WORKCAP templates to dev.kabreneman.us/templates/.
           Create a templates/ directory. Migrate blank templates, adapting names to
           UNISYS naming conventions. Do NOT migrate any filled templates with data.

  REC-007: Create procedures/ directory and migrate applicable procedures.
           Evaluate each of the 5 kabreneman.us procedures and 1 KABDMSV2 procedure.
           Adapt to UNISYS P-class format and register with DOC IDs.

  REC-008: Migrate Python scripts to scripts/.
           Update internal path references for UNISYS structure.
           Add UNISYS_IMPORT_RECORD metadata to each script.

Priority 3 — MEDIUM TERM (Complete within 1–3 months)

  REC-009: Review and migrate financial documents to financials/.
           Evaluate WorkingCapital.md, allocation.md, cashflowsfy26.md, expenses.md,
           obligations.md, and obligationadherence.md for sensitive content.
           Migrate non-sensitive structural documents; keep filled/data documents in backup.

  REC-010: Adapt KABDMSV2 standards documents to DOCSYS format.
           Register coding-standards, configuration-standards, documentation-standards,
           and file-organization standards as UNISYS artifacts with proper DOC IDs.

  REC-011: Evaluate kabreneman.us/docs/ for applicable content.
           automation-guide.md, metadata-wizard.md, report-standards.md, and history.md
           may be adapted or superseded by DOCSYS/UNISYS equivalents.

  REC-012: Establish migration completion criteria.
           Define what "done" looks like for the consolidation. Set a target date.
           Once criteria are met, add deprecation notices to kabreneman.us and KABDMSV2.

Priority 4 — DEFERRED (After core migration complete)

  REC-013: Evaluate archive/, projects/, shared/, utilities/ in kabreneman.us.
           Determine which artifacts have UNISYS relevance. Register valuable artifacts
           as M-class or archive-class entries. Discard the rest.

  REC-014: Mark source repositories as deprecated upon migration completion.
           Add archival README to kabreneman.us and KABDMSV2 pointing to dev.kabreneman.us.

Section 10 — Migration Progress Tracker

  The following table represents the current migration state. Update as work progresses.

  Component                     Source Repo        Destination              Status
  ───────────────────────────   ─────────────────  ───────────────────────  ─────────────
  UNISYS governance docs        (new — UNISYS)     /root                    COMPLETE
  Node configs (3 XML)          KABDMSV2 + kab.us  devices/configs/         NOT STARTED
  Templates (15+)               kabreneman.us      templates/               NOT STARTED
  Procedures (5+)               kabreneman.us      procedures/ or docs/     NOT STARTED
  Python scripts (2)            kabreneman.us      scripts/                 NOT STARTED
  Financial docs (6)            kabreneman.us      financials/              NOT STARTED
  KABDMSV2 standards (5)        KABDMSV2           docs/                    NOT STARTED
  Migration Manifest (M-00002)  (new — UNISYS)     /root                    NOT STARTED
  Document Index (L-00001_)     (new — UNISYS)     /root                    NOT STARTED
  Security policy (P-00001)     (new — UNISYS)     docs/                    COMPLETE
  Audit report (REP-00001)      (new — UNISYS)     docs/                    COMPLETE (this doc)

Section 11 — Cross-References

  P-00001_security-and-backup-procedures.md   Security and backup procedures (UNISYS)
  M-00001.md                                   MANIFEST founding page — lists M-00002 candidate
  UNISYS metadata standard.md                 TSN/AUID/UDIS identity rules
  DOCSYS document creation governance         Document class and workflow governance
  kabreneman.us Issue #21                      Original backup documentation request
  KABDMSV2/SECURITY.md                        Predecessor security policy
  kabreneman.us/docs/folder-audit.md          Predecessor folder structure audit

Section 12 — Revision History

  2026-04-03   REP-00001   Initial publication   Kyle Breneman / @copilot
               TSN-20260403-CSAUDIT — Created as part of UNISYS migration governance.
               Addresses kabreneman.us Issue #21 comment (2026-04-03): "Audit codespace
               to confirm transfer to dev.kabreneman.us. Then, report back, recommend actions."

Unified System Architecture™   UNISYS™   ©2026 Kyle Breneman

REP-00001  |  Codespace Transfer Audit and Recommendations  |  Status: ACTIVE  |  2026-04-03
