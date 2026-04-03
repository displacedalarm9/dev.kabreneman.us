<!-- UNISYS_IMPORT_RECORD
AUID: MIG-00028
TSN: TSN-20260403-MIGRATE
Class: DOC
Lifecycle: Active
Title: Accordion Decision Flowchart
CreatedBy: Kyle Breneman
OriginalRepo: displacedalarm9/kabreneman.us
OriginalPath: 2025-11-25_accordion-decision-flowchart.md
OriginalLocation: github:displacedalarm9/kabreneman.us/2025-11-25_accordion-decision-flowchart.md
MigratedOn: 2026-04-03
-->
```mermaid
flowchart TD
    A[Do you already play accordion or similar instrument?] -->|Yes| B[Define your music style: Folk, Classical, Jazz, Pop, etc.]
    A -->|No| C[Decide learning path: Self-taught or Lessons]
    
    B --> D[Choose type: Piano / Button / Diatonic / Chromatic / Digital]
    C --> D
    
    D --> E[Initial comfort check: Weight, size, strap fit, reach]
    E -->|Uncomfortable| F[Downsize model, adjust straps, or change type]
    E -->|Comfortable| G[Set budget range]
    
    G --> H[New or Used?]
    H -->|New| I[Shop at reputable dealer; test multiple models]
    H -->|Used| J[Inspect for: Bellows leaks, reed tuning, keyboard action, cosmetic condition]
    
    I --> K[Match features to needs: Registers, reeds, tuning style]
    J --> K
    
    K --> L[Final comfort check: Play for 10–15 min seated & standing]
    L -->|Uncomfortable| F
    L -->|Comfortable| M[Purchase & arrange maintenance plan]
```