# Q‑DOC: CAR THING (SPOTIFY) — OBSERVED BEHAVIOR & VARIATION LOG

**Document Type:** Q (Qualifier / Observed Behavior)  
**Domain:** Hardware → LifeArtifact → Repurpose Candidate  
**Artifact:** Spotify Car Thing  
**Source Provenance:** Official discontinuation notice (Spotify Support), physical unit in possession  
**Status:** Active Observation  
**Edition:** 1  
**Lifecycle:** Fragment → Draft

---

## 1. PURPOSE
Capture all observed behavior, constraints, anomalies, and variation patterns of the discontinued Spotify Car Thing to support:
- Repurpose feasibility analysis  
- Hardware mapping  
- Firmware behavior characterization  
- UNISYS integration planning  
- Restoration or bypass attempts  

This Q‑doc records what *is*, not what should be.

---

## 2. OBSERVED BASELINE BEHAVIOR

### 2.1 Power Behavior
- Device powers on normally via USB‑C when supplied with 5V.  
- Boot animation appears consistently.  
- Device attempts to reach Spotify servers during startup.  
- After discontinuation window, device fails handshake and becomes nonfunctional.

### 2.2 UI Behavior
- Touchscreen responds to input.  
- Rotary knob registers rotation and press events.  
- UI stalls at "connecting" or "update required" depending on firmware version.  
- No local/offline/bypass mode observed.

### 2.3 Connectivity Behavior
- Wi‑Fi module activates and scans for networks.  
- Bluetooth module activates but cannot complete pairing without server validation.  
- USB‑C does not expose mass‑storage or ADB‑like interfaces by default.

### 2.4 Audio Behavior
- No audio output without successful Spotify handshake.  
- No system tones or internal speaker activity observed.

---

## 3. VARIATION LOG

### 3.1 Firmware Version Differences
- **Early firmware:** stalls at "connecting".  
- **Later firmware:** displays discontinuation or "update required".  
- **Unknown firmware:** may enter boot loop if update endpoint unreachable.

### 3.2 Network Environment Variations
- **Open Wi‑Fi:** attempts connection → fails at handshake.  
- **Mobile hotspot:** same behavior.  
- **No network:** remains in offline error state; still nonfunctional.

### 3.3 Power Source Variations
- Car USB, wall adapter, and battery bank all produce stable boot.  
- No behavioral differences observed across power sources.

### 3.4 Physical Condition Variations
- Worn knobs may misregister rotation.  
- Touchscreen sensitivity varies slightly between units.

---

## 4. FAILURE MODES

### 4.1 Hard Failure
- Device permanently nonfunctional due to server shutdown.  
- No fallback or local playback mode.

### 4.2 Soft Failure
- UI freezes on connection screen.  
- Bluetooth pairing fails silently.  
- Wi‑Fi connection loops.

### 4.3 Potential Hidden Modes (Unconfirmed)
- Recovery mode via button combination.  
- USB debug mode.  
- Firmware update mode.  
*(None yet observed.)*

---

## 5. REPURPOSE SIGNALS (NON‑CONCLUSIVE)

### 5.1 Hardware Signals
- Screen, knob, Wi‑Fi, Bluetooth, and SoC appear functional.  
- Device boots reliably → bootloader intact.  
- USB‑C power delivery stable.

### 5.2 Software Signals
- Bootloader likely locked.  
- OS likely Linux‑based (community teardown inference).  
- No exposed debug interfaces in normal boot.

### 5.3 Physical Access Signals
- Backplate removable with heat + pry tools.  
- Internal board accessible.  
- Visible test pads (mapping required).

---

## 6. OPEN QUESTIONS
- Are UART pads present on the PCB?  
- Can firmware be dumped via hardware interface?  
- Does the bootloader accept unsigned images?  
- Is there a hidden recovery mode?  
- Can touchscreen/knob be accessed via GPIO?  
- Can the device act as a dumb display via USB?  
- Can the SoC boot from external storage?

---

## 7. NEXT ACTIONS (DOCUMENT POINTERS)
- **HARDMAP‑CarThing‑01** — hardware map  
- **TEARDOWN‑CarThing‑01** — teardown steps  
- **EVAL‑CarThing‑Repurpose‑01** — feasibility matrix  
- **SCHM‑CarThing‑01** — pinout schema  
- **HIST‑CarThing‑01** — provenance record  

---
