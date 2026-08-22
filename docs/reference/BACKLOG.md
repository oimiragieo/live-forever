# LIVE-FOREVER — FULL BACKLOG (2026-08-22 PM)

Living list. `open_gaps == 0` does **not** mean empty backlog. Source of truth for Ralph: this file + `docs/gap_register.json` + `scripts/ralph_tick.py` `NEXT_QUERIES`.

Last CEO update: [`ceo-update-2026-08-22-pm.md`](ceo-update-2026-08-22-pm.md).  
Paper / OSS moat (2026-08-22): [`../ideation/paper-l0-control-instrumentation.md`](../ideation/paper-l0-control-instrumentation.md) · [`related-open-tools.md`](related-open-tools.md) · [`../../design/gaps/geroscience-epistemics.md`](../../design/gaps/geroscience-epistemics.md).  
Snapshot: corpus climbs via Ralph; `GOAL_MET` is a floor; tests **42** green when suite passes.

---

## A. Deferred scientific dossiers (await clinical data)

From `docs/gap_register.json` — status `deferred_with_evidence`:

| ID | Dossier | Why still backlog |
|----|---------|-------------------|
| `human-osk-safety` | `design/gaps/human-osk-safety.md` | FIH ER-100 eye only; **systemic multi-organ OSK** not cleared |
| `nad-human-healthspan` | `design/gaps/nad-human-healthspan.md` | Target engagement yes; **causal healthspan hard endpoints** no |
| `senolytic-cart-human` | `design/gaps/senolytic-cart-human.md` | Mouse success; **human aging CAR-T** not published |
| `ab-trial-design` | `design/gaps/ab-trial-design.md` | CHIP/CHRS blueprints exist; **approved CH-directed drugs** + full A+B longevity RCT still missing |
| `age-matrix` | `design/gaps/age-matrix.md` | ALT-711 class PoC; **glucosepane-scale ECM Rx** still R&D |

Closed/mapped (not deferred unknowns): `thymic-restoration` → L3 addendum (TRIIM-X tracked elsewhere).

---

## B. Ultra-design deferred (clinical, not literature)

From `design/ultra-design.md` §4:

1. Systemic (multi-organ) human OSK beyond ocular ER-100  
2. Causal NAD healthspan RCTs with hard endpoints  
3. Human senolytic CAR-T aging indications  
4. Approved CH-directed drugs  
5. Glucosepane-scale ECM longevity Rx  

---

## C. Hallmark coverage seed

| Item | Status |
|------|--------|
| `dysbiosis` | Still in `algorithms.hallmarks_graph.uncovered()` — weak stack coverage; research seed until a second stack layer is earned by evidence |

---

## D. Unpublished trial / Finals pins (active research backlog)

Bank “still absent” every wake — do not invent.

### D1. Highest priority (L1 / current NEXT_QUERIES)

| # | Pin | Status |
|---|-----|--------|
| 1 | **EVERLAST NCT05835999 Results** | **COMPLETED 2026-07-22** (n=106 ACTUAL); **No Results Posted**; no Konopka preprint; Konopka lab **stale recruitment copy**; Syfrah Protocol Version bumps **≠ Results** |
| 2 | **VITAL-H NCT** | n≈726 four-arm oral hybrid; ARPA-H award Feb 2026; San Antonio Report **start later 2026/early 2027**; **recruitment not begun**; **no CT.gov NCT** |
| 3 | **VITAL-H arm milligrams** | Oral route; **OASIS 4 25 mg + OASIS 1 50 mg** obesity COMPLETED — **≠ VITAL-H arm mg** (still unpublished) |
| 4 | **RESTOR NCT06658093 OD mg** | **Started 2026-03-04**; RECRUITING adaptive PK/PD (MedPath Jun 2026) — **OD mg still unpublished** |
| 5 | **SHAPE NCT07275424 daily SC mg** | RECRUITING; CT.gov **2026-06-15**; vial **80 mg/mL** — **mg/day unpublished**; No Results; **Forzinity Barth 40 mg ≠ invent SHAPE** |

### D2. XPRIZE M2 / Finals dose & NCT gaps

| # | Pin |
|---|-----|
| 6 | Goda / NanoTitan / Relife **Finals EV particle counts** (+ jRCT1033250410 high/low still unpublished; recruitment suspended; press **>15y** vs NAD **~40y** scaling ≠ dose) |
| 7 | AgelessRx **Finals agent-mg** (incl. tirzepatide + sermorelin) + **Finals NCT** + IRB clearance (~Oct 2026 expected); **NCT07092605** sema microdose ≠ Finals |
| 8 | Longeveron **Finals cell dose** (Ph2b **25–200M** ≠ **ELPIS II 2.5×10⁵/kg** ≠ Finals) |
| 9 | Minicircle **Finals plasmid µg** / 1y schedule |
| 10 | NYC-Vita **Finals n** (Ph1b n≈22 << floors) |
| 11 | RETRO-EPIGERNA **KYN / queuine capsule human mg** + registry |
| 12 | Suninflam **SIF001 Finals MCI dose** (Ph1 10–80 mg/kg ≠ Finals) |
| 13 | Progerinin **Finals ordinary-aging dose** (HGPS **500–1500** ≠ Werner **NCT05847179 2400 mg/day** ≠ healthspan; Ph2a Results still absent) |
| 14 | TIME TRAVELER **UMIN000059942 Results** (COMPLETED; numbers unpublished) |
| 15 | Mighty **Finals n/dose** beyond SHAPE IIT |

### D3. Non-M2 Finalists / adjacency

| # | Pin |
|---|-----|
| 16 | **GIANTS-1 Results** + named **cognitive partner** (still RECRUITING; ProGen MOU ≠ NCT amendment) |
| 17 | **Lono LON301** human oral NCT / mg (patent-only EP4509119) |
| 18 | **Abe Yoando** Finals NMN+BHB+ginsenoside **drink mg** + Finals NCT (company PR still **NMN+kampo** only; 42 d semi-finals **unregistered**) |
| 19 | **Morinaga** Finals Passienol+niacin **NCT/mg** (company PR piceatannol-only; UMIN000018397 mg opaque; consumer 10+10 ≠ Finals) |
| 20 | **ASU** operating Finals **ATA / %O2** (Smart Fit PoC + NCT06734468 lifestyle ≠ setpoints; chamber 2.4 ATA / 0.356 ATM capability ≠ dose) |
| 21 | **GOQii Sanjeevini** Finals NCT / CogState / supplement IDs (PoC **unregistered**; Decode Age Longevian **≠** Finals; **MoCA ≠ CogState**) |
| 22 | **ANI Biome** Finals NCT (ELITE **8 wk unregistered**; **GlycanAge ≠ iAge/IMM-AGE**; SHARP **≠** ELITE) |
| 23 | **Boston Healthspan** ALG-801 Finals mg (**Justice combo pin**; ACTRN Ph1b **mg opaque**; **no Finals NCT**) |

### D4. PROSPR / disease-bridge / other clinical

| # | Pin |
|---|-----|
| 24 | LNS8801 **PROSPR healthy-older NCT/dose** (**Adis plans only**; oncology **125 mg ≠ invent**) |
| 25 | TPN-101 **aging / HEALEY RSA NCT** (**design n=200 ×48 wk**; disease **400 mg ≠ invent**; AD/HEALEY still unregistered) |
| 26 | Cyclarity **UDP-003 Ph2 NCT** + ACS **CCTA interim** (**7KC PD ≠ plaque**; Series B gated) |
| 27 | TRIIM-X **peer-reviewed package** (**RECRUITING past 2025-12**; **TRIIM 2019 ≠ TRIIM-X**; not M2 awardee) |
| 28 | XPRIZE **3rd immune response-to-challenge** assay vendor / SOP (**Rules pending proxy**; Stein live; Landscape silent) |
| 29 | Deciduous **iNKT IND** public filing (**still absent**; **US20250381206 Dec 2025 + US12655171 = IP ≠ IND**; **fobi Jul 2026 preclinical ~$6.5M**; MBC BioLabs Apr 2026; **2023 timeline missed**) |
| 30 | ER-100 **second-patient / DSMB** public update (**still absent**; first dose **2026-06-09** only; CT.gov **2026-05-15**; doses **2e11/6e11 vg/eye**; **NCT07290244**) |

### D5. Mechanism / assay tensions still open

| # | Pin |
|---|-----|
| 31 | Queuine / **STL-101** plasma age-decline **reconciliation** (**UNSETTLED**; bioRxiv **713446 drop claim** vs PLOS **2021 flat 50–90**; **PMC11493786** LOQ **0.3 nM** n=44 flat — **assay/cohort mismatch**) |
| 32 | Human **queuine longevity supplementation NCT/mg** (**still absent**; **bioRxiv 713446 Mar 2026 mouse +15.3% lifespan ≠ human NCT**; **Sapience ST101 ≠ STL-101**; **2021 timeline missed**) |
| 33 | Nitazoxanide **human aging / FOXN1** dose NCT (**still absent**; Genah 2026 post-IR mouse only; Immun Ageing Jul 2026 review ≠ NCT; **PCT/IT2025/050304** patent; Alinia 500 BID×3d / ELICIT pediatric / G1090N PK / oncology 200 mg/kg all ≠ aging) |
| 34 | Oral sema **25/50** vs VITAL-H | **Wegovy pill 25 mg** FDA+**EC approved** (Jul 2026); OASIS studied **25+50 mg** but only **25 marketed**; neither invents VITAL-H aging arm mg (**Coming Soon**, no NCT) |
| 35 | Selective **B2M / CCL11** aging depletion IND (**still absent**; **2025 review: CCL11 trials vacant**; **CAT-213 inflammatory only**; **NCT07713680** ESRD β2M observational **≠** depletion) |

---

## E. Ops / harness backlog (keep green)

| # | Item |
|---|------|
| 36 | Keep Ralph tick loop healthy (~600s; sentinel `AGENT_LOOP_TICK_liveforever`) |
| 37 | Refresh `NEXT_QUERIES` every wake toward highest-value absent pin |
| 38 | Append ≥3–5 corpus sources per wake; update hillclimb + ab-trial-design |
| 39 | Run `status.py` + `pytest tests -q --cache-clear` after corpus edits |
| 40 | Never commit unless CEO asks (repo historically non-git / no auto-commit) |
| 41 | Safety boundary: literature/systems only — no DIY biotech, synthesis, or personal dosing |
| 42 | **Dossier append hygiene** — unique `## Update (Ralph wake #N)` anchor or EOF append; never bare "negatives held" StrReplace; dedupe duplicates same turn |

---

## F. Explicitly NOT backlog (do not reopen as unknowns)

- Scaffold / two-pathway sim / ITP ingest / parabiosis ingest / pro-aging catalog v1 — **closed**  
- `thymic-restoration` as separate deferred gap — **mapped/closed** into L3  
- Inventing milligrams from adjacency ladders — **forbidden**, not a gap to “fill”

---

## Count

| Bucket | Count |
|--------|-------|
| Deferred dossiers | 5 |
| Ultra-design deferred bullets | 5 (overlap with dossiers) |
| Hallmark seeds | 1 |
| Research pins (D1–D5) | 35 |
| Ops items | 7 |
| **Enumerated backlog rows** | **~48 unique** (dossiers + seed + pins + ops; ultra-design overlaps dossiers) |
