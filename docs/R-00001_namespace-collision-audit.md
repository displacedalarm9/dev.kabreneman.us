UNISYS — NAMESPACE COLLISION AUDIT
R-00001_
R-Class Review

Page ID:      R-00001_
System:       DOCSYS
Class Letter: R
Scope:        ALL UNISYS ARTIFACTS — CROSS-REPO
Document Type: Review / Audit (R-Class)
Status:       ACTIVE
TSN:          TSN-20260403-NSAUDIT
AUID:         AUID-R-00001
Author:       Kyle Breneman / @copilot
Date Created: 2026-04-03

Section 1 — Purpose

This review audits the complete UNISYS codespace (dev.kabreneman.us, kabreneman.us, KABDMSV2)
to identify namespace collisions, identity gaps, format inconsistencies, and ghost references
across all artifact identifiers (AUID, TSN, DOC ID, Page ID, Class Letter).

It was created in response to PR comment (2026-04-03):
"Index all identifiers based on AUID. Audit codespace to determine namespace collisions."

The companion index is L-00001_.md.

Section 2 — Scope

  Repository A:  displacedalarm9/dev.kabreneman.us   (UNISYS — primary, audited in full)
  Repository B:  displacedalarm9/kabreneman.us       (predecessor — audited for ID overlap)
  Repository C:  displacedalarm9/KABDMSV2            (predecessor — audited for ID overlap)

  Audit method: Manual enumeration of all identity fields in all files across all three repos.
  Audit date:   2026-04-03

Section 3 — Identifier Inventory: dev.kabreneman.us

  File                                         DOC ID / Page ID   Class      AUID             TSN
  ───────────────────────────────────────────  ─────────────────  ─────────  ───────────────  ─────────────────────────
  UNISYS metadata standard.md                 X-00002_           X          (none)           (none)
  DOCSYS document creation governance         G-00002            G          (none)           (none)
  DOCSYS document creation governance         P-00000            P          (none)           (none)
    ↑ same file — two identities (COLLISION)
  M-00001.md                                   M-00001            M          (none)           (none)
  docs/P-00001_security-and-backup-procedures.md  P-00001         P          AUID-P-00001     TSN-20260403-SECBAK
  docs/REP-00001_codespace-transfer-audit.md   REP-00001         REP        AUID-REP-00001   TSN-20260403-CSAUDIT
  L-00001_.md                                  L-00001_           L          AUID-L-00001     TSN-20260403-AUIDINDEX
  docs/R-00001_namespace-collision-audit.md    R-00001_           R          AUID-R-00001     TSN-20260403-NSAUDIT

  Total files in repo:           9 (non-README, non-.github)
  Total with AUID assigned:      4 (P-00001, REP-00001, L-00001_, R-00001_)
  Total without AUID:            4 (X-00002_, G-00002/P-00000, M-00001)
  Total with namespace collision: 1 file (DOCSYS governance — 2 identities)

Section 4 — Identifier Inventory: kabreneman.us

  kabreneman.us does NOT use the UNISYS AUID scheme. Its identity model uses:
  — YAML frontmatter with last_updated/version/file_status (simple mode)
  — TSN format: YYYYMMDD-XXXX (e.g., 20251219-A5FA via metadata wizard)
  — No AUID field present in any file

  Identity-bearing files found:

  File                         Identity Scheme      Value(s) Found
  ───────────────────────────  ───────────────────  ──────────────────────────────────────
  docs/filename.md             YAML frontmatter     last_updated: 2025-06-06, v1.0.1
  docs/canonical-context.md    YAML frontmatter     last_updated: 2026-04-03, v1.0.0
  docs/folder-audit.md         YAML frontmatter     last_updated: 2026-04-03, v1.1.0
  procedures/emergency.md      YAML frontmatter     last_updated: 2025-06-06, v1.0.0
  (others)                     YAML frontmatter     last_updated / version / file_status

  No UNISYS AUIDs or DOC IDs present in kabreneman.us.
  No collisions with dev.kabreneman.us AUID namespace.

Section 5 — Identifier Inventory: KABDMSV2

  KABDMSV2 does NOT use the UNISYS AUID scheme. No AUID, TSN, or DOC ID fields
  were found in any KABDMSV2 file.

  KABDMSV2 contains a SECURITY.md and standards documents under docs/standards/
  but these carry no UNISYS identity fields.

  No collisions with dev.kabreneman.us AUID namespace.

Section 6 — Collision and Issue Findings

Finding COL-001 — DUAL-CLASS IDENTITY (CRITICAL)
  Artifact:    "DOCSYS document creation governance" (file: `DOCSYS document creation governance`)
  Collision:   The same file carries TWO distinct class identities in two different namespaces:
               — Header/title: "G–00002 — DOCSYS DOCUMENT CREATION GOVERNANCE" → G-class
               — Section 9:   "This Page is assigned the DOC ID P‐00000" → P-class
  Impact:      Any system or agent that resolves DOC IDs will find:
               — G-00002 → "DOCSYS document creation governance"
               — P-00000 → "DOCSYS document creation governance"
               These resolve to the same artifact via different namespaces, which is technically
               allowed (a single artifact can have roles in multiple systems) but the G-class
               and P-class roles are architecturally distinct and the dual assignment is
               undocumented as intentional.
  Classification: Genuine collision if both IDs are used independently to locate the file.
  Recommendation:
    Option A (Preferred): Retain G-00002 as the primary identity (governance artifact).
                          Remove the P-00000 claim from Section 9. The file governs P-class
                          documents but is itself a G-class artifact — these are distinct concepts.
    Option B:             Formally declare this a dual-registered artifact (acceptable per
                          architecture), add a CROSS-REGISTER field to the header noting:
                          CROSS-REGISTER: G-00002 (primary) / P-00000 (role alias)
  Status:  OPEN — requires operator decision

Finding COL-002 — MISSING AUID ASSIGNMENTS (HIGH)
  Artifacts:   X-00002_, G-00002/P-00000, M-00001
  Issue:       Three foundational artifacts (4 identities) lack AUID fields.
               Per X-00002_ (UNISYS Metadata Standard) Section 2: "Every governed artifact
               must contain... AUID — Immutable; assigned after TSN; unique across system."
               These artifacts predate the formal AUID assignment process but are actively
               referenced and cited. They are in violation of the standard they themselves define.
  Impact:      Cannot be looked up in an AUID-indexed registry. Identity is incomplete.
               Future tooling (SyncKit, AE-RPG) cannot process them without AUID.
  Recommendation:
    Retroactively assign AUIDs and TSNs to all three foundational artifacts.
    Proposed assignments (awaiting operator ratification):

    Artifact                           DOC ID      Proposed AUID     Proposed TSN
    ─────────────────────────────────  ──────────  ───────────────   ─────────────────────────
    UNISYS metadata standard.md        X-00002_    AUID-X-00002      TSN-20260403-RETROX002
    DOCSYS document creation govern.   G-00002     AUID-G-00002      TSN-20260403-RETROG002
    M-00001.md                         M-00001     AUID-M-00001      TSN-20260403-RETROM001

    Rationale for suffix alignment: within the class-scoped AUID convention (AUID-X-######),
    the numeric suffix is aligned to the DOC ID suffix (X-00002_ → AUID-X-00002) to make
    the relationship self-evident during cross-referencing. AUID-X-00001 is reserved for
    X-00001_ (Identity Constitution) if that ghost artifact is eventually created.

    Note: If G-00002 is merged with P-00000 (see COL-001), only one AUID is needed.
    Note: TSN prefix TSN-20260403-RETRO* marks retroactive assignments.
  Status:  OPEN — requires operator decision and file edits

Finding COL-003 — CLASS-SCOPED AUID FORMAT (MEDIUM)
  Artifacts:   P-00001 (AUID-P-00001), REP-00001 (AUID-REP-00001)
               L-00001_ (AUID-L-00001), R-00001_ (AUID-R-00001)
  Issue:       AUIDs embed the class prefix (AUID-P-, AUID-REP-, AUID-L-, AUID-R-).
               Per X-00002_ Section 4.2: "Every new artifact receives a new AUID" and
               per G-00002/P-00000 Section 3.2: AUIDs are "Sequential, global, immutable."
               A globally sequential AUID (e.g., AUID-000001, AUID-000002) spans all classes.
               Class-scoped AUIDs (AUID-P-00001, AUID-REP-00001) fragment the sequence into
               per-class counters, making cross-class global ordering impossible.
  Impact:      Medium — the values are distinct (no collision), but the format violates the
               "global sequential" requirement. Future AUIDs will continue to fragment unless
               a global counter is adopted.
  Recommendation:
    For artifacts already assigned (AUID-P-00001, AUID-REP-00001): RETAIN. AUIDs are
    immutable once assigned. Do not change them.
    For all new artifacts going forward: use a global sequential format:
      AUID-000005, AUID-000006, ...
    with an explicit registry mapping AUID → artifact.
    Update Section 10 of L-00001_.md to reflect this decision once made by operator.
  Status:  OPEN — format decision required by operator; existing AUIDs unaffected

Finding COL-004 — PHANTOM AUID RESERVATION (MEDIUM)
  Source:      Prior session memory (agent context, not committed to repo)
  Issue:       A prior agent session generated memory claiming AUIDs MIG-00001 to MIG-00043
               were assigned to planned migration artifacts. No files bearing these AUIDs
               exist in dev.kabreneman.us, kabreneman.us, or KABDMSV2.
               The format "MIG-######" does not follow any established AUID pattern
               (AUID-P-00001, AUID-REP-00001, etc.) and appears to be a phantom assignment
               from a session that planned but did not execute a migration.
  Impact:      If a real migration artifact is later assigned AUID-MIG-00001 without
               knowledge of this phantom reservation, a conceptual collision exists in
               session memory. No file-level collision currently exists.
  Recommendation:
    Treat MIG-00001 through MIG-00043 as RESERVED identifiers.
    Do NOT assign any artifact these IDs until the phantom reservation is cleared.
    Clear the reservation by operator declaration when confirmed: either the migration
    was cancelled (release the IDs) or confirmed (assign to actual files).
    Document the clearing decision in a future revision of L-00001_.
  Status:  OPEN — requires operator declaration

Finding COL-005 — TSN FORMAT DIVERGENCE (LOW)
  Source:      kabreneman.us vs. dev.kabreneman.us
  Issue:       Two TSN formats are in use across the codespace:
               Format A (UNISYS):       TSN-YYYYMMDD-LABEL   (e.g., TSN-20260403-SECBAK)
               Format B (kabreneman.us): YYYYMMDD-XXXX        (e.g., 20251219-A5FA)
               These formats cannot be reliably distinguished by a parser. Format B could
               appear inside UNISYS content as a version number or other field.
               When kabreneman.us artifacts are migrated to dev.kabreneman.us, their
               Format B TSNs MUST be preserved (immutable per X-00002_ Section 5) but
               they will not be compatible with Format A expectations.
  Impact:      Low while the repos are separate. Escalates to HIGH at migration time.
  Recommendation:
    Document the TSN format divergence in the migration procedure for each artifact.
    When creating UNISYS_IMPORT_RECORD blocks for migrated artifacts, add field:
      OriginalTSNFormat: YYYYMMDD-XXXX
      UnisysTSN: TSN-YYYYMMDD-MIGRATE (assigned at migration time, does not replace original)
    The original TSN is preserved; the UNISYS TSN is the migration event TSN.
  Status:  DOCUMENTED — addressed at migration time per procedure in REP-00001

Finding COL-006 — GHOST CONSTITUTIONAL REFERENCES (LOW)
  Source:      UNISYS metadata standard.md (X-00002_)
  Issue:       X-00002_ declares two constitutional dependencies:
               — X-00001_ (Identity Constitution)
               — G-00001_ (Governance Overview)
               Neither X-00001_ nor G-00001_ exists in dev.kabreneman.us, kabreneman.us,
               or KABDMSV2. These may be:
               a) Planned artifacts not yet created, or
               b) Artifacts that exist only in conversational memory or local storage, or
               c) Deprecated labels from an earlier architecture iteration
  Impact:      Low currently — X-00002_ functions as written. If a tool tries to
               dereference X-00001_ or G-00001_, it will fail.
  Recommendation:
    If these constitute foundational architectural artifacts, they must be created and
    registered in dev.kabreneman.us.
    If they are obsolete references, the dependency block in X-00002_ should be amended
    via CR-Class change request to remove the ghost references.
    Operator to determine which scenario applies.
  Status:  OPEN — requires operator determination

Section 7 — Collision Summary Table

  Finding   Severity   Type                        Status   Immediate Action Required?
  ────────  ─────────  ──────────────────────────  ───────  ──────────────────────────
  COL-001   CRITICAL   Dual-class identity          OPEN    Yes — operator resolves G-00002 vs P-00000
  COL-002   HIGH       Missing AUID assignments     OPEN    Yes — retroactive AUID assignment needed
  COL-003   MEDIUM     Class-scoped AUID format     OPEN    No — existing AUIDs immutable; format decision for future
  COL-004   MEDIUM     Phantom AUID reservation     OPEN    No — reserve MIG-##### until cleared
  COL-005   LOW        TSN format divergence        NOTED   No — address at migration time
  COL-006   LOW        Ghost constitutional deps    OPEN    No — operator determines if X-00001_/G-00001_ needed

  Total findings: 6
  Critical:       1
  High:           1
  Medium:         2
  Low:            2

Section 8 — Cross-Repo Collision Status

  The following namespace collisions across repositories were checked and found CLEAR:

  Check                                         Result
  ────────────────────────────────────────────  ──────────────────────────────────────────
  AUID values: dev.kabreneman.us vs kab.us      CLEAR — kabreneman.us has no AUIDs
  AUID values: dev.kabreneman.us vs KABDMSV2    CLEAR — KABDMSV2 has no AUIDs
  TSN values: dev.kabreneman.us vs kab.us       CLEAR — different formats; no value overlap
  DOC IDs: dev.kabreneman.us vs kab.us          CLEAR — different ID systems
  DOC IDs: dev.kabreneman.us vs KABDMSV2        CLEAR — KABDMSV2 has no DOC IDs
  Page IDs within dev.kabreneman.us             COLLISION: COL-001 (G-00002 / P-00000)
  AUID uniqueness within dev.kabreneman.us      CLEAR — all 4 AUIDs are distinct

  Overall cross-repo collision status: NO CROSS-REPO COLLISIONS FOUND.
  Intra-repo collision: 1 (COL-001, within dev.kabreneman.us).

Section 9 — Recommended Actions by Priority

  Priority 1 — IMMEDIATE

    ACTION-001: Resolve COL-001 (Dual-class identity on DOCSYS governance file).
      Operator decides: retain G-00002 as primary and remove P-00000 claim from Section 9,
      OR formally declare a dual registration with CROSS-REGISTER annotation.

    ACTION-002: Begin retroactive AUID assignments (COL-002).
      Assign AUID-X-00002, AUID-G-00002, AUID-M-00001 to the three foundational artifacts.
      Assign matching TSNs (TSN-20260403-RETRO*).
      Update each file's header block.

  Priority 2 — SHORT TERM

    ACTION-003: Determine fate of COL-004 phantom reservations (MIG-00001 to MIG-00043).
      If migration is proceeding: start assigning real artifacts to these IDs as files are created.
      If migration approach changed: release the IDs; document the release in L-00001_.

    ACTION-004: Declare global AUID format for future artifacts (COL-003).
      Decide between continuing class-scoped format (AUID-P-00002, AUID-R-00002) or
      adopting a global sequential format (AUID-000005, AUID-000006). Update L-00001_
      Section 10 with the decision.

  Priority 3 — MEDIUM TERM

    ACTION-005: Determine status of ghost constitutional references (COL-006).
      Research whether X-00001_ (Identity Constitution) and G-00001_ (Governance Overview)
      should be created. If yes, create them. If no, file a CR-Class change request to amend
      the dependency block in X-00002_.

    ACTION-006: Document TSN divergence handling in migration procedures (COL-005).
      Update REP-00001 REC-003 / REC-008 to explicitly specify UNISYS_IMPORT_RECORD format
      for artifacts with Format B TSNs from kabreneman.us.

Section 10 — Cross-References

  L-00001_.md                                  AUID-indexed Outstanding Document Index
  docs/REP-00001_codespace-transfer-audit.md   Codespace migration status report
  docs/P-00001_security-and-backup-procedures.md   Security and backup procedures
  UNISYS metadata standard.md (X-00002_)       TSN/AUID/UDIS rules being audited
  DOCSYS document creation governance (G-00002/P-00000)   Subject of COL-001

Section 11 — Revision History

  2026-04-03   R-00001_   v1.0   Initial publication   Kyle Breneman / @copilot
               TSN-20260403-NSAUDIT
               Created in response to PR comment: "Index all identifiers based on AUID.
               Audit codespace to determine namespace collisions."

Unified System Architecture™   UNISYS™   ©2026 Kyle Breneman

R-00001_  |  Namespace Collision Audit  |  Status: ACTIVE  |  2026-04-03
