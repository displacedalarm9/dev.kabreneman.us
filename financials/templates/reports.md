<!--
UNISYS_IMPORT_RECORD
AUID: MIG-00018
TSN: TSN-20260404-WORKCAP
OriginalLocation: displacedalarm9/kabreneman.us/templates/reports.md
MigratedOn: 2026-04-04
-->
---
last_updated: 2026-04-04
version: 1.0.0
file_status: template
system: ACCTSYS
subsystem: WORKCAP
---

# Report Generation Guide

## File Structure

```
reviews/
  {type}/           — variance, obligations, etc.
    {year}-{month}/
      {date}-{report}.md
```

## Report Types

### 1. Daily Reviews
- Location: `reviews/daily/YYYY-MM/DD.md`
- Template: `financials/templates/daily.md`
- Updates: `financials/templates/accounts.md`, `financials/allocation.md`

### 2. Variance Reports
- Location: `reviews/variance/YYYY-MM/DD.md`
- Template: `financials/templates/variance.md`
- Updates: `financials/WorkingCapital.md` if threshold exceeded

### 3. Utility Reports
- Location: `reviews/utilities/YYYY-MM/provider.md`
- Template: `financials/templates/utilities.md`
- Updates: `financials/allocation.md` for budget adjustments

## Related Documents

[See: financials/templates/index.md for full template list]
[See: financials/WorkingCapital.md for naming conventions]
