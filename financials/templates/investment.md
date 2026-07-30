<!--
UNISYS_IMPORT_RECORD
AUID: MIG-00014
TSN: TSN-20260404-WORKCAP
OriginalLocation: displacedalarm9/kabreneman.us/templates/investment.md
MigratedOn: 2026-04-04
-->
---
last_updated: 2026-04-04
version: 1.1.0
file_status: template
system: ACCTSYS
subsystem: WORKCAP
---

# Investment Tracking Template

## Instructions
1. Use monthly form for regular tracking
2. Use quarterly form for rebalancing
3. Store in `investments/[year]/[quarter]/`
4. Update WorkingCapital.md after quarterly reviews

---

## Monthly Investment Log

| Category | Item | Value | Status |
|----------|------|-------|--------|
| **Header** | Month | [MONTH] [YEAR] | — |
| **New Investments** | Date | [DATE] | — |
| | Amount | $______ | — |
| | Asset Class | [TYPE] | — |
| | Expected Return | ___% | — |
| **Performance** | Starting Value | $______ | [ON/OFF] Track |
| | Ending Value | $______ | [ON/OFF] Track |
| | Return | ___% | [ON/OFF] Track |
| | YTD Return | ___% | [ON/OFF] Track |

---

## Quarterly Review Form

| Category | Metric | Current | Target |
|----------|--------|---------|--------|
| **Header** | Quarter | [Q#] [YEAR] | — |
| **Portfolio** | Total Invested | $______ | $______ |
| | Total Return | ___% | ___% |
| | Risk Level | [L/M/H] | [L/M/H] |
| **Allocation** | Stocks | ___% | ___% |
| | Bonds | ___% | ___% |
| | Cash | ___% | ___% |

---

## WorkingCapital.md Update Checklist

| Section | Data to Update | Source |
|---------|---------------|---------|
| Phase Progress | Investment Returns | Quarterly Form |
| Risk Profile | Asset Allocation | Quarterly Form |
| Next Targets | Quarter Projections | Action Items |

[See: financials/WorkingCapital.md Phase 3 section]
[See: financials/allocation.md for performance targets]

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 2026-04-04 | Migrated to UNISYS/WORKCAP; updated references |
| 1.0.0 | 2025-06-01 | Initial investment template |
