<!-- UNISYS_IMPORT_RECORD
AUID: MIG-00020
TSN: TSN-20260403-MIGRATE
Class: DOC
Lifecycle: Active
Title: Report Generation Guide
CreatedBy: Kyle Breneman
OriginalRepo: displacedalarm9/kabreneman.us
OriginalPath: templates/reports.md
OriginalLocation: github:displacedalarm9/kabreneman.us/templates/reports.md
MigratedOn: 2026-04-03
-->
---
last_updated: 2025-06-06
version: 1.0.0
file_status: template
---

# Report Generation Guide

## File Structure
/reviews/
  /{type}/      # variance, obligations, etc.
    /{year}-{month}/
      {date}-{report}.md

## Report Types
1. Daily Reviews
   - Location: reviews/daily/YYYY-MM/DD.md
   - Template: templates/daily.md
   - Updates: accounts.md, matrix.md

2. Variance Reports
   - Location: reviews/variance/YYYY-MM/DD.md
   - Template: templates/variance.md
   - Updates: emergency.md if needed

3. Utility Reports
   - Location: utilities/YYYY-MM/provider.md
   - Template: templates/utilities.md
   - Updates: progress.md for budgets

[See: standards.md for naming conventions]
[See: templates/index.md for template list]
