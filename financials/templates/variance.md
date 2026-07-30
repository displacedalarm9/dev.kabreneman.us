<!--
UNISYS_IMPORT_RECORD
AUID: MIG-00010
TSN: TSN-20260404-WORKCAP
OriginalLocation: displacedalarm9/kabreneman.us/templates/variance.md
MigratedOn: 2026-04-04
-->
---
last_updated: 2026-04-04
version: 1.2.0
file_status: template
system: ACCTSYS
subsystem: WORKCAP
---

# Variance Report Templates

## References
[See: financials/allocation.md for tolerance ranges]
[See: financials/WorkingCapital.md for alert thresholds]

## Instructions
1. Copy appropriate template section below
2. Fill all fields marked [REQUIRED]
3. Store reports in `reviews/variance/[year]/[month]/`
4. Update reference documents after completion:
   - Daily variances update allocation.md
   - Weekly variances update cashflows_template.md
   - Monthly variances update WorkingCapital.md

---

## Daily Variance Report

| Category | Metric | Value | Status |
|----------|--------|-------|--------|
| **Header** [REQUIRED] | Date | [DATE] | — |
| | Reviewer | [NAME] | — |
| **Cash Position** | Target | $______ | [G/Y/R] |
| | Actual | $______ | [G/Y/R] |
| | Variance | $______ | [G/Y/R] |
| **Credit Status** | Target Usage | ___% | [G/Y/R] |
| | Actual Usage | ___% | [G/Y/R] |
| | Variance | ___% | [G/Y/R] |
| **Buffer Status** | Required | $[MIN] | [G/Y/R] |
| | Current | $______ | [G/Y/R] |
| | Variance | $______ | [G/Y/R] |

---

## Weekly/Monthly Reports

| Category | Target | Actual | Variance | Status |
|----------|--------|--------|----------|--------|
| Distribution | $______ | $______ | $______ | [G/Y/R] |
| Buffer | $______ | $______ | $______ | [G/Y/R] |
| Debt Reduction | $______ | $______ | ___% | [G/Y/R] |
| Credit Score | ______ | ______ | ±______ | [G/Y/R] |

---

## Status Definitions

| Color | Range | Required Action |
|-------|-------|----------------|
| GREEN | Within ±5% | Continue monitoring |
| YELLOW | ±5–10% | Review needed |
| RED | Beyond ±10% | Immediate action |

[See: financials/allocation.md for tolerance ranges]
[See: financials/WorkingCapital.md for recovery protocols]
