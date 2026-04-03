UNISYS — SECURITY AND BACKUP PROCEDURES
P-00001
P-Class Procedure

Page ID:      P-00001
System:       DOCSYS
Class Letter: P
Scope:        SYSTEM-WIDE
Document Type: Procedure (P-Class)
Status:       ACTIVE
TSN:          TSN-20260403-SECBAK
AUID:         AUID-P-00001
Author:       Kyle Breneman
Date Created: 2026-04-03

Section 1 — Purpose

This procedure defines the security boundaries, data classification rules, backup procedures,
restore procedures, and related security best practices for the UNISYS system hosted in the
dev.kabreneman.us repository.

It is the authoritative operational reference for:

  — What artifacts belong in the repository vs. what must stay outside it
  — How to back up sensitive artifacts to the local secure backup location
  — How to restore from backup, including selective restore
  — How to verify backup integrity
  — Encryption and off-site backup recommendations
  — Repository access control requirements

Section 2 — Scope

This procedure applies to:

  — The dev.kabreneman.us GitHub repository (displacedalarm9/dev.kabreneman.us)
  — All UNISYS-governed artifacts stored therein
  — The local secure backup directory (~/secure-kabreneman-backup/ or equivalent)
  — All active UNISYS nodes: NODE-OPS-001, NODE-VR-002, NODE-ARC-003

This procedure does not apply to:

  — Third-party service configurations not under UNISYS governance
  — Content in predecessor repositories (kabreneman.us, KABDMSV2) until formally migrated
  — External private data stores governed by other policies

Section 3 — Definitions

  Repository          The dev.kabreneman.us GitHub repository; the UNISYS unified source of truth.
  Sensitive Data      Financial records, account numbers, balances, credentials, personal
                      identifiers, or any data whose exposure would cause harm or privacy breach.
  System File         Any artifact governing the UNISYS system — templates, procedures, scripts,
                      configuration schemas, documentation, node configs (without credentials).
  Secure Backup Dir   The local directory designated for sensitive artifact storage, defaulting
                      to ~/secure-kabreneman-backup/. Must not be committed to any repository.
  PMF                 Provenance Metadata File — tracks artifact identity and lifecycle.
  TSN                 Trace Serial Number — event-scoped identity field (immutable).
  AUID                Artifact Unique Identifier — artifact-scoped identity field (immutable).

Section 4 — Data Classification

4.1 Commit to Repository (System Files — SAFE)

  Category              Examples
  ──────────────────    ──────────────────────────────────────────────────────────
  UNISYS governance     M-class manifests, X-class crosswalks, G-class governance
  DOCSYS documents      P-class, W-class, R-class, A-class, D-class, REP-class docs
  Templates             Blank review/report/tracking templates (no filled-in data)
  Procedures            Operational workflows and checklists (no credentials)
  Node configs          Hardware specification XML files (no passwords or tokens)
  Scripts               Python utilities, automation helpers (no embedded credentials)
  Documentation         Standards, guides, README files

4.2 Never Commit to Repository (Sensitive Data — FORBIDDEN)

  Category              Examples
  ──────────────────    ──────────────────────────────────────────────────────────
  Financial records     Account balances, transactions, bank account numbers
  Credentials           Passwords, API keys, tokens, SSH private keys
  Personal identifiers  SSNs, birthdate, address, phone numbers
  Filled templates      Any template with real financial or personal data filled in
  Log files             ~/secure-kabreneman-backup/logs/ and similar
  Backup archives       Encrypted or unencrypted backup archives
  Raw data exports      CSV/JSON exports containing account or financial data

4.3 Borderline — Evaluate Before Committing

  Category              Guidance
  ──────────────────    ──────────────────────────────────────────────────────────
  Debt summaries        Totals without account numbers may be acceptable. Itemized
                        lists with institution names require careful review.
  Obligation lists      Institution names without balances/account numbers may be
                        committed. Any numerical financial data requires review.
  Device node specs     Hardware specs are safe. Software license keys are not.
  Archive indexes       File listings are safe. Content of archived files is not.

Section 5 — Pre-Commit Security Check

Before every commit, verify:

  Step 1 — Review staged changes:
    git diff --staged

  Step 2 — Search for common sensitive patterns:
    git diff --staged | grep -iE '(password|passwd|secret|token|api[_-]?key|account|balance|ssn|routing)'

  Step 3 — Verify .gitignore covers all sensitive paths:
    git status --short | grep '^?'

  Step 4 — Confirm no data files (.csv, .xlsx, .xlsm) are staged unless explicitly reviewed:
    git diff --staged --name-only | grep -E '\.(csv|xlsx|xlsm|json)$'

If any sensitive content is detected:

  — Unstage immediately: git reset HEAD <file>
  — If already committed: rotate the exposed credential immediately, then clean history
    using git filter-branch or BFG Repo Cleaner before any push

.gitignore must include at minimum:

  *.csv                 (financial data exports)
  *.xlsm                (macro-enabled workbooks)
  data/                 (raw data directories)
  logs/                 (log output)
  reviews/              (filled review documents, if stored locally)
  # Note: The secure backup directory lives outside the repository root and therefore
  # does not require a .gitignore entry. .gitignore only affects files within the
  # repository working tree. Keep ~/secure-kabreneman-backup/ outside the repo root.

Section 6 — Backup Procedures

6.1 Backup Directory Structure

The secure backup directory must follow this structure:

  ~/secure-kabreneman-backup/
  ├── financial/          # Financial records and filled templates
  │   ├── reviews/        # Filled review documents
  │   ├── reports/        # Generated financial reports
  │   └── raw/            # Raw data exports (CSV, XLSX)
  ├── credentials/        # Credentials and secrets (keep minimal)
  │   └── README.md       # Index of what is stored here
  ├── archive/            # Retired documents (per RETENSYS policy)
  │   └── YYYY/           # Organized by year
  └── logs/               # Activity and audit logs

6.2 Directory Permissions

The secure backup directory and all subdirectories must have permissions set to 700 (owner
read/write/execute only). No group or other access is permitted.

  # Set permissions on the backup root and all subdirectories:
  chmod 700 ~/secure-kabreneman-backup/
  find ~/secure-kabreneman-backup/ -type d -exec chmod 700 {} \;

  # Set permissions on all files to 600 (owner read/write only):
  find ~/secure-kabreneman-backup/ -type f -exec chmod 600 {} \;

  # Verify:
  ls -la ~/secure-kabreneman-backup/

6.3 Backing Up New Sensitive Files

When a new sensitive file is created:

  Step 1 — Confirm the file is in .gitignore or outside the repository root.
  Step 2 — Copy to the appropriate subdirectory in ~/secure-kabreneman-backup/.
  Step 3 — Set correct permissions (chmod 600 for files, 700 for directories).
  Step 4 — Update the backup log: ~/secure-kabreneman-backup/logs/backup.log

  Example backup log entry format:
    [YYYY-MM-DD HH:MM] BACKED UP: <filename> → <backup path> | SHA256: <checksum>

  Compute checksum:
    sha256sum <file> >> ~/secure-kabreneman-backup/logs/backup.log

6.4 Backed-Up File Categorization Checklist

  □ Is this file a filled template (real data)?   → financial/reviews/ or financial/reports/
  □ Is this file a raw data export (CSV/XLSX)?    → financial/raw/
  □ Does this file contain credentials?           → credentials/ (and consider password manager)
  □ Is this an archived/retired artifact?         → archive/YYYY/
  □ Is this an activity or system log?            → logs/

Section 7 — Restore Procedures

7.1 Full Restore

To restore all files from backup to their working location:

  Step 1 — Confirm destination directory exists and is clean:
    ls -la ~/kabreneman-working/    (or equivalent working directory)

  Step 2 — Copy files from backup:
    cp -r ~/secure-kabreneman-backup/financial/ ~/kabreneman-working/
    cp -r ~/secure-kabreneman-backup/archive/ ~/kabreneman-working/

  Step 3 — Restore permissions (use find for cross-shell compatibility):
    find ~/kabreneman-working/ -type f -name "*.md" -exec chmod 600 {} \;
    find ~/kabreneman-working/ -type f -name "*.csv" -exec chmod 600 {} \;

  Step 4 — Run verification (see Section 8).

7.2 Selective Restore

To restore a specific file:

  Step 1 — Locate the file in the backup directory:
    find ~/secure-kabreneman-backup/ -name "<filename>"

  Step 2 — Verify checksum before restore:
    sha256sum ~/secure-kabreneman-backup/<path>/<filename>
    Compare against ~/secure-kabreneman-backup/logs/backup.log

  Step 3 — Copy to destination:
    cp ~/secure-kabreneman-backup/<path>/<filename> <destination>

  Step 4 — Set permissions:
    chmod 600 <destination>/<filename>

7.3 Repository Restore

If the repository itself is lost or corrupted:

  Step 1 — Re-clone from GitHub:
    git clone git@github.com:displacedalarm9/dev.kabreneman.us.git

  Step 2 — Restore sensitive artifacts from ~/secure-kabreneman-backup/ as needed.

  Step 3 — Verify all UNISYS identity fields (TSN, AUID) are intact.

Section 8 — Verification Steps

8.1 Post-Backup Verification

After every backup operation:

  □ Checksum recorded in backup.log (see Section 6.3)
  □ File permissions are 600 (files) and 700 (directories)
  □ File is NOT present in git status output (not tracked by repository)
  □ Backup log entry is dated and complete

  Verify a file is not tracked:
    git ls-files --error-unmatch <filename>
    (exit code 1 = not tracked = correct)

8.2 Post-Restore Verification

After every restore operation:

  □ Checksum of restored file matches backup.log entry
  □ File is readable: open and visually verify content
  □ File permissions reset to 600
  □ File is not staged for commit (git status shows it as untracked or ignored)

  Verify checksum match:
    sha256sum <restored-file>
    (compare against entry in ~/secure-kabreneman-backup/logs/backup.log)

8.3 Periodic Backup Audit

Perform at minimum monthly:

  □ List all files in ~/secure-kabreneman-backup/ and verify all expected files are present
  □ Spot-check 3–5 checksums against backup.log
  □ Confirm no new sensitive files have accumulated outside backup location
  □ Confirm .gitignore still covers all known sensitive patterns

Section 9 — Encryption Recommendations

9.1 At-Rest Encryption

Sensitive files in ~/secure-kabreneman-backup/ should be encrypted at rest.

  Recommended tools:
  — GPG symmetric encryption (built-in on most Linux/macOS systems):
      gpg --symmetric --cipher-algo AES256 <file>
      gpg --decrypt <file>.gpg > <file>

  — VeraCrypt volume for the entire backup directory (recommended for bulk storage):
      Create a VeraCrypt volume at ~/secure-kabreneman-backup.vc
      Mount before use, unmount when done

  — OS-level full-disk encryption (BitLocker on Windows, FileVault on macOS, LUKS on Linux):
      This is the minimum baseline and should always be enabled on NODE-OPS-001 and NODE-VR-002.

9.2 Credentials Management

  — Never store credentials as plaintext files
  — Use a password manager (Bitwarden, 1Password, or KeePassXC)
  — If storing in ~/secure-kabreneman-backup/credentials/, encrypt the directory separately
  — Rotate credentials if any file is accidentally committed to a repository

Section 10 — Off-Site Backup Recommendations

A single local backup is not sufficient. Maintain off-site copies.

  Tier 1 — Local (current):
    ~/secure-kabreneman-backup/ on NODE-OPS-001 (primary)

  Tier 2 — Secondary local node:
    Replicate to NODE-ARC-003 (archival node)
    Use rsync over SSH:
      rsync -avz --chmod=D700,F600 ~/secure-kabreneman-backup/ <NODE-ARC-003>:~/backup/

  Tier 3 — Encrypted cloud storage:
    Encrypt backup archive first, then upload:
      tar czf - ~/secure-kabreneman-backup/ | gpg --symmetric --cipher-algo AES256 > backup-YYYY-MM-DD.tar.gz.gpg
    Upload encrypted archive to a private cloud store (not a public bucket)
    Recommended services: Backblaze B2 (private bucket), AWS S3 (private bucket with SSE)

  Minimum backup retention:
    Keep 30 days of daily backups
    Keep 12 months of monthly archives
    Keep 1 permanent archival snapshot per fiscal year

Section 11 — Repository Access Controls

  — Enable 2-factor authentication (2FA) on the GitHub account displacedalarm9
  — Use SSH key authentication for git operations (not HTTPS with password)
  — Rotate SSH keys if any device is compromised
  — Limit repository collaborator access to trusted parties only
  — Review and revoke any OAuth app tokens that are no longer needed
  — Use branch protection on main branch: require PR review before merge

Section 12 — Cross-References

  UNISYS metadata standard.md     Identity and metadata immutability rules
  DOCSYS document creation governance   Document class and lifecycle governance
  M-00001.md                       MANIFEST founding page (M-class identity)
  kabreneman.us/docs/canonical-context.md  Security boundaries (predecessor system)
  KABDMSV2/SECURITY.md             Security policy (predecessor system)
  kabreneman.us Issue #21          Backup and restore documentation request
  P-00001 (this document)          DOC ID: P-00001 | AUID: AUID-P-00001

Section 13 — Revision History

  2026-04-03   P-00001   Initial publication   Kyle Breneman
               TSN-20260403-SECBAK — Created in response to kabreneman.us Issue #21
               and transfer to dev.kabreneman.us (UNISYS).

Unified System Architecture™   UNISYS™   ©2026 Kyle Breneman

P-00001  |  Security and Backup Procedures  |  Status: ACTIVE  |  2026-04-03
