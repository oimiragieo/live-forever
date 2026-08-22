# ULTRA-DESIGN: Theoretical Path to Extreme Longevity / Boundedness of Aging

**Status:** Living design (Ralph-loop hill-climbed)  
**Date:** 2026-08-20  
**Constraint:** Literature-grounded systems architecture. Not medical advice. Not a DIY protocol. Translational work requires IND → GMP → clinical trials.

---

## 0. Formal problem

Define organismal damage burden \(D(t) = A(t) + B(t)\):

- **\(A(t)\)** — *regulatable* lesions (proteostasis load, NAD deficit, SASP flux, reversible epigenetic drift, mito quality lag). Endogenous clearance rate \(R_A\) can be raised by systemic setpoints.
- **\(B(t)\)** — *information-limited* lesions (oncogenic clones, fixed somatic mutations, permanent cell loss, AGE crosslinks, mtDNA heteroplasmy past observability). Require engineered detection + correction/replacement.

**Operational boundedness condition (control model — proposed decomposition, not a validated biological law):**  
In this repo’s model, \(D(t)\) stays bounded ∀t **iff** sustained \(R_A >\) production of A **and** engineered \(R_B\) bounds B. Either alone fails asymptotically **in simulation**. See paper brief: [`docs/ideation/paper-l0-control-instrumentation.md`](../docs/ideation/paper-l0-control-instrumentation.md).

**Immortality (operational definition used here):** keep \(D(t)\) below a morbidity threshold indefinitely with acceptable cancer risk — not “zero death,” but **damage boundedness**.

---

## 1. The 6-Layer Longevity Stack

```
┌─────────────────────────────────────────────────────────────┐
│ L6  REPLACEMENT     organs / cells / extracellular matrix   │
│ L5  INFORMATION     base/epigenetic editors, clone purge    │  ← Pathway B
│ L4  REPROGRAM       pulsed partial OSK(M), clock reset      │
│ L3  CLEARANCE       senolytics / CAR-T / immune restore     │
│ L2  REPAIR ECONOMY  NAD–PARP–sirtuin, BER/NER/HR balance    │  ← Pathway A
│ L1  DAMAGE INPUT    metabolism, inflammation, environment   │
└─────────────────────────────────────────────────────────────┘
         ↑ biomarkers + adaptive control loop (L0)
```

### L0 — Sensing & control (always on)
| Biomarker class | Examples | Controls |
|-----------------|----------|----------|
| Epigenetic age | Horvath / multi-clock panel | L4 dose/schedule |
| Senescence burden | p16/p21, SA-β-gal, SASP panel | L3 pulses |
| Genome mosaicism | ctDNA VAF, single-cell mut load | L5 de-risk |
| NAD / PAR economy | NAD+/NADH, PARylation | L2 |
| Immune resilience | TCR diversity, thymus proxies | L3 immune |
| Function | VO2, grip, cognition, vascular | global stop/go |

#### L0 external endpoint map — PROSPR-IC vs XPRIZE Finals (wake #63)

| Domain | PROSPR / IC Version-1 (regulatory learning) | XPRIZE Healthspan Finals (competition oracle) | Ultra-design use |
|--------|-----------------------------------------------|-----------------------------------------------|------------------|
| Muscle / locomotor | Gait speed; SPPB (continuous preferred) | 6MWT endurance + knee extensor/leg-press power | Primary L0 function gate |
| Cognition | MoCA + processing speed / executive task | **CogState** battery (Rules V1.0 Apr 2026; DET/IDN/OCL/ONB/GMLT/IDSSTS; supersedes Guidelines V2.2 CANTAB) | Prefer CogState for Finals parity; MoCA/Trails/Stroop OK for pilots (e.g. SHAPE) but **not** Finals substitutes |
| Immune | Not a dedicated IC domain (vitality/psych overlap) | iAge + IMM-AGE + **immune cell response-to-challenge** (pending; named category, assay TBD before ~2030) — need 2 of 3 | Keep immune as L3-specific L0 channel — XPRIZE is stricter here |
| Psychological | Depression + anxiety/distress | Not a prize domain | Monitor for GH/rapa stacks; not a prize stop |
| Sensory | Visual acuity + hearing | Not a prize domain | Relevant to ER-100 ocular path only |
| Vitality | Grip, respiratory, appetite/nutrition, fatigue | Folded into muscle/immune/cognition responders | Use as enrichment, not sole go/no-go |
| Composite | PROSPR-IC score (THRIVE; de novo kit goal) — **not yet validated surrogate** | Global responder = all 3 prize domains + 20pp/CI rule | Never treat either composite as immortality proof |

**Design rule:** Dual-track L0 — (1) IC domain measures for FDA-facing programs (VITAL-H/PROSPR); (2) XPRIZE muscle+cognitive+immune triad for modality bake-offs. Molecular clocks/SASP/clone VAF remain internal control layers neither program fully replaces. Finals FAQ/Application floors: **≥40 participants per arm**, **≥100 total** recruit/retain essential (scale language ~100–150), 6-visit schedule, Rules supersede Guidelines (no crossover).

**Safe sequencing (from control theory + oncology risk):**  
1. Surveillance & clonal de-risk (B)  
2. Immune restoration  
3. Pulsed systemic repair / reprogramming (A)  
4. Ongoing engineered maintenance of residual B  

Repair-first without de-risking can expand clones (simulations favor de-risk-first).

---

### L1 — Reduce damage input (Pathway A foundation)
- Metabolic load: nutrient sensing (mTOR/AMPK/insulin). **NIA ITP gold standards:** rapamycin (both sexes, late-life works), acarbose (males≫females), 17α-estradiol (males), canagliflozin, glycine, aspirin, NDGA, Protandim, captopril; **rapa+acarbose** can beat rapa alone in males.
- Systemic milieu: heterochronic parabiosis / young circulation shifts multi-omic age and can extend mouse lifespan; old blood accelerates aging — design for *pro-youthful factor restoration* **and** *pro-aging factor removal* (not transfusions as product).
- Chronic inflammation / inflammaging (cGAS–STING from cytosolic DNA).
- Environmental genotoxins (Misrepair theory: reduce exposure beats heroic repair).
- Extracellular matrix / AGE crosslinks (glucosepane class) — Pathway-B-adjacent structural damage; organism-scale clearance still an open gap.
- **Dysbiosis (L1-only hallmark):** `hallmarks_graph.INTERVENTION_EDGES` maps fiber/prebiotic, polyphenol diet, chronic-ABX avoidance, and caloric patterning → dysbiosis (± inflammation). These are L1 levers, **not** a second stack layer — dysbiosis stays an `uncovered()` research seed until a distinct L2+/L3 mechanism earns coverage.

**When dysbiosis earns a second stack layer (gate — all required):**
1. A **non-diet** mechanism with human causal evidence (e.g. engineered consortia / phage / metabolite replacement) that moves a hard outcome (infection, vaccine response, IC domain, or morbidity) — not only 16S shifts.
2. That mechanism is classifiable as L2 (repair economy), L3 (clearance/immune restore), or L5 (engineered maintenance) without collapsing into “eat more fiber.”
3. Bidirectional oracle: intervention ON improves the outcome AND withholding/placebo does not; diet-only arms must not be relabeled as L2+.
Until then: keep `stack_layers=("L1",)` and `uncovered()` includes `dysbiosis`.

#### L1 stack comparison — AgelessRx Finals vs VITAL-H (wake #59)

| Axis | VITAL-H (PROSPR) | AgelessRx Finals | Prefer for immortality design |
|------|------------------|------------------|-------------------------------|
| Core nutrient sensing | Low-dose **rapamycin** alone arm | Low-dose rapamycin **inside** 9-agent stack | VITAL-H for causal attribution; AgelessRx for combinatorial feasibility |
| Metabolic / glycemic | **Dapagliflozin** + **semaglutide** arms | Metformin + compounded **tirzepatide** | VITAL-H closer to ITP SGLT2 + GLP-1 outcomes; watch sex-PK on SGLT2 |
| Design | 4-arm PBO-controlled; n≈726; IC domains | 2-arm stack vs control; n≈186 ages 50–90; XPRIZE 3-domain responders; pilot doses public (**≠ Finals mg**) | VITAL-H = regulatory learning; AgelessRx = competition oracle |
| Extra agents | None (clean factorial) | LDN, NAD nasal, GSH patch, sermorelin, B12, supp + RT/coaching; public **sema microdose 0.1–0.5 mg/wk** (separate AgelessRx trial ≠ Finals tirzepatide mg) | Treat extras as hypothesis generators, not L1 defaults |
| Missing vs catalog | No selective B2M/CCL11/LINE-1/7KC/Gal-3 | Same neutralization gaps | Neither replaces Pathway-B removal |

**Design rule:** Anchor L1 on VITAL-H-class single/few-agent RCTs for what works; use AgelessRx-class stacks only after components survive attribution tests — never invert that order for the ultra-design default.

### L2 — Supercharge DNA repair economy
Published levers (conceptual targets, not recipes):
- **NAD+ pool** shared by PARP1 and sirtuins (SIRT1/6/7 genome stability themes); CD38 rises with age → NAD sink.
- **PARP signaling without chronic hyper-PARylation** (balance: PARPi cancer paradigm vs repair enhancement for aging — dual-use tension).
- **E2F-linked DNA repair gene programs** without forcing S-phase (Nat Comm 2024 mTORC1–E2F uncoupling).
- **p53-supported repair** suppressing CCF → SASP (Nat Comm 2025).
- **tRNA manQ / queuine repletion (Pathway A — emerging):** age-conserved loss of mannosyl-queuosine on tRNAAsp impairs translational fidelity → proteostasis collapse + senescence programs (GPNMB, p16/p21). Circulating queuine **may** decline with age (rodents/humans; bioRxiv 2026 preprint) — **but** PLOS One STL-101 plasma (healthy 50–90, n=160) found **no significant age decline** and higher levels in women; treat plasma-age association as **unsettled**. Healthy means ~**7–8 nM** (AgeCoDe; LOQ 0.3 nM). **Preclinical dose pin (bioRxiv 2026, not peer-reviewed):** C57BL/6 males from 16 mo, **10 μg/kg oral every 3 days** → mean lifespan **+15.3%**, DNAm age↓, cognition/motor↑, p16/p21/IL-6↓; paraquat ladder **25 / 200 μg/kg**; cells **10 / 50 ng/mL**. Drosophila median **+47%** at 50 ng/bottle. In-vitro neuroprotection **~0.1–1+ μM** (STL-101); oncology screen IC50 **~5.95 μM** (PANC-1) flags a non-trivial window. **Name collision:** Sapience **ST101** oncology peptide **≠** Stellate **STL-101** queuine. **Human Finals (RETRO-EPIGERNA KYN capsule) milligrams still unpublished** — do not invent clinical mg from mouse μg/kg. Place as L2 *fidelity restoration* adjunct after L1 metabolic setpoints, not as a solo immortality agent; require plasma+manQ assay before any translational escalation.
- **Bioinspiration:** tardigrade radiation tolerance (protective proteins, phase-separated repair hubs, NAD resupply) as *engineering motifs*, not copy-paste transgenes without oncology gates.
- Pathway coverage matrix: BER / NER / MMR / HR / cNHEJ — age shifts toward error-prone joiners; goal is **fidelity restoration**, not blanket NHEJ boost.

### L3 — Clearance of irreparable cells + immune youth
- Senolytics (D+Q, fisetin, navitoclax lineage) — intermittent “hit-and-run”; early human pilots only.
- Senomorphics (SASP quieting) when killing is risky.
- Next-gen: senolytic CAR-T (uPAR/NKG2D), ADCs, vaccines — **mouse aged + prophylactic single-dose persistence shown (Amor 2024)**; human aging trials not yet published; enter via fibrosis/oncology.
- Platelet-sparing Bcl-xL path: DT2216 PROTAC FIH done (oncology); Nav-Gal still preclinical; UNITY UBX1325 franchise wound down.
- Immune-endogenous: Deciduous iNKT restore (pre-IND, fibrosis-first); prefer over nonspecific Bcl toxics for chronic use.
- Damage-removal adjuncts on L3/L1 border: Cyclarity UDP-003 / **CTx-001** (7KC excretion PoC; ACS Part3 **25 mg/kg ×6 over 6 wk**, plaque interim pending through ~2026-12 primary); Gal-3 mAbs (TB006/SIF001).
- Thymic / immune repertoire restoration (FOXN1/IL-7/KGF/Myc-TEC preclinical; adult clinical benefit unproven) so clearance is endogenous long-term. **Adjacent pharmacologic FOXN1 lever (2026):** nitazoxanide (NTZ) via proteasome/ER-stress/UPR → FOXN1↑ in murine/human TECs and faster post-irradiation thymic recovery in mice — **≠** human aging dose/NCT; FDA infection label is **500 mg BID ×3 days** only — do **not** invent chronic rejuvenation milligrams. Keep as L3 research seed beside TRIIM-X / Deciduous.
- Mitochondrial quality (cardiolipin binders / elamipretide) — L2/L3 border: restores A-type mito capacity; not a senescent-cell kill.
- **Caution:** senescent cells aid wound healing in youth — age- and indication-gated.

#### L3 modality ranking — thymic vs mito (wake #53; refreshed #73)

| Rank | Modality | Why now | Limit |
|------|----------|---------|-------|
| 1 | **Mito / elamipretide** | FORZINITY **40 mg SC daily** (≥30 kg; **20 mg** if eGFR <30, not dialysis); label RCT (n=12, 12 wk) **missed primary 6MWT/fatigue** — accelerated approval on knee-extensor intermediate; **4TAZPower** confirmatory (n=48; Bristol-only recruiting); Landscape Semi-Finals **N=23** (65–79, 4 wk) trends claimed; SHAPE ~n=30 still RECRUITING — **mg/day unpublished**; SC exposure studied **2–80 mg/day** (proportional PK) — **≠ invent SHAPE mg**; secondaries **6MWT + knee extensor** but cognition = MoCA/Trails/Stroop (**≠ CogState**); do **not** equate 40 mg / prior IV **0.25 mg/kg/hr×2h** with SHAPE/Finals | Functional PoC thin in Barth randomized data; **hold L3 #1 only as modality lead pending SHAPE/Finals/4TAZPower** |
| 2 | **Thymic / TRIIM-X** | Only human thymus-regen clinical franchise; Nature 2026 field heat (thymectomy/size ↔ mortality); **Immortal Thymus** transgenic lifespan study fundraising (~$250k Y1 / 110 mice) | Not XPRIZE M2-funded; TRIIM-X still no peer-reviewed package; GH-class oncology surveillance |
| 3 | **Senolytic clearance** | DT2216 RP2D; D+Q / AFFIRM disease pilots | No healthy-aging registration path; UNITY wind-down caution |

**Design rule:** Prefer mito peptide for near-term L3 *function* (muscle domain) under disease + Finals oracles; keep thymic restore as the endogenous *immune surveillance* bet that unlocks safer chronic clearance — do not collapse them into one stack layer without separate IND logic. Rank order **unchanged** this wake because SHAPE has not read out.

### L3 medicine-path alignment (2026) — PROSPR × XPRIZE
- **PROSPR** builds FDA-facing IC/domain endpoints + first large gerotherapeutic RCTs (VITAL-H rapa/dapa/sema; Rochester TPN-101; Cambrian mTORC1-sel; Linnaeus GPER; Nula nuclear-envelope).
- **XPRIZE Healthspan Finals** runs parallel 1-year muscle/cognition/immune RCTs (MSC, multi-agent stacks, EVs, elamipretide, Gal-3, plasmids) — competition oracles, not registration endpoints.
- Design rule: use XPRIZE for modality diversity signal; use PROSPR/VITAL-H for regulatory endpoint learning; disease-anchored Phase II remains the truth-teller before any “aging” claim.

### L4 — Epigenetic rejuvenation (partial reprogramming)
- Cyclic / pulsed OSK(M) or OSK (omit c-Myc when possible); chemical / mRNA / AAV delivery research paths.
- Goal: reset clocks + transcriptomes **without** identity loss / teratoma.
- Safety: continuous OSKM lethal in mice; maturation-phase windows; tissue-restricted delivery.
- **Human status (2026):** Life Biosciences **ER-100** — first-in-human inducible AAV-OSK in one eye (glaucoma/NAION Phase 1, doxycycline on-switch ~8 weeks). This is the empirical safety window for OSK: local + timed, not systemic.
- Measure with multiple independent clocks + function; clock move ≠ healthspan.

### L5 — Information-limited lesion control (Pathway B — required for immortality)
- Base editing for *known* pathogenic alleles (HGPS LMNA ABE proof-of-concept: large mouse lifespan gain).
- Epigenetic editors for durable expression control (PCSK9-class platform maturity ≠ aging gene yet).
- **Clonal hematopoiesis surveillance** using CHRS + CBC cadence + CV risk mitigation (CHIP clinic blueprints) before intensifying Pathway A.
- Pro-aging factor removal (B2M, CCL11, TGF-β niche signaling, sVCAM1, IL-1β axis) complementary to young-factor restoration.
- mtDNA heteroplasmy strategies (replacement / allotopic — early).
- AGE / matrix clearance (ALT-711-class proof-of-concept; glucosepane-selective longevity Rx still open R&D).

### L6 — Replacement
- Stem cell / niche rejuvenation; organoids → GMP cell therapies; eventual organ replacement / xeno / bioengineered tissues.
- When repair cannot restore structure, replace the module.

---

## 2. “DNA repair recipe” (systems recipe — NOT a lab protocol)

A **recipe** here means an ordered R&D program:

| Step | Intent | Success oracle |
|------|--------|----------------|
| R1 | Map tissue lesion spectrum (oxidative, bulky, DSB, mismatch) | Assay battery bidirectional |
| R2 | Restore NAD–PARP–sirtuin economy | NAD↑ without oncogenic proliferation |
| R3 | Restore E2F repair transcriptome without forced mitosis | γH2AX clearance kinetics ↑ |
| R4 | Keep p53 DNA-repair arm active; limit CCF/SASP | SASP↓, genome diploidy preserved |
| R5 | Prefer HR fidelity in cycling stem cells; avoid mutagenic alt-EJ dominance | Mutation rate / clone VAF↓ |
| R6 | Clear cells past repair (L3) | Senescence markers↓ |
| R7 | Epigenetic reset (L4) after de-risk | Multi-clock↓ + identity retained |
| R8 | Edit only defined causal alleles (L5) | Allele correction % + phenotype |
| R9 | Replace failed tissues (L6) | Organ function restored |

**Medicine manufacturing path for any molecule/modality in R2–R8:**  
Target ID → validation → HTS/design → ADMET → GLP tox → IND → GMP clinical supply → Phase I–III → Phase IV oncology surveillance.  
Aging targets are *speculative* — Phase II disease utility is the truth-teller (Knowles & Gromo).

---

## 3. Ultra-design thesis (one paragraph)

**To live forever in the control-theoretic sense, humanity must run a closed-loop geroscience system that (1) continuously measures multi-omic damage, (2) first de-risks information-limited clones, (3) restores DNA-repair economy and clears senescent cells, (4) periodically resets epigenetic age without erasing identity, and (5) replaces what cannot be repaired — with every modality forced through the same drug-development gates that make modern medicine.** No single pill, gene, or lifestyle hack bounds \(B(t)\). Immortality is an **engineered maintenance regime**, not a discovery of one molecule.

---

## 4. Open gaps (Ralph loop backlog)

None open in `docs/gap_register.json`. Prior scientific gaps are **deferred_with_evidence** with dossiers under `design/gaps/`.

**Full enumerated backlog** (deferred dossiers + hallmark seed + unpublished NCT/mg/Results pins + ops): [`docs/reference/BACKLOG.md`](../docs/reference/BACKLOG.md).  
CEO snapshot: [`docs/reference/ceo-update-2026-08-21.md`](../docs/reference/ceo-update-2026-08-21.md).  
Lessons: [`docs/reference/lessons-learned-2026-08-21.md`](../docs/reference/lessons-learned-2026-08-21.md).

Deferred (await clinical data, not literature):
- Systemic (multi-organ) human OSK beyond ocular ER-100
- Causal NAD healthspan RCTs with hard endpoints
- Human senolytic CAR-T aging indications
- Approved CH-directed drugs + glucosepane-scale ECM Rx

Active research climb (not register “open”): EVERLAST Results; VITAL-H NCT/arm mg; RESTOR OD mg; SHAPE daily SC mg; Finals team doses (Goda/AgelessRx/Abe/Morinaga/Lono/RETRO/…); GIANTS Results; dysbiosis hallmark seed.

See also: `design/pro-aging-factor-catalog.md` (v1 catalog closed).

---

## 5. What this repo will never ship

- DIY CRISPR / base-editor recipes
- Synthesis instructions for experimental drugs
- Personalized dosing for unapproved gerotherapeutics
- Claims that any stack is proven to confer immortality in humans


## Update — Ralph wake #5 (human mTOR)
- **PEARL (2025):** intermittent low-dose rapamycin ~1y relatively safe in normative-aging adults; primary visceral adiposity null; notable sex-specific lean-mass/pain signals in women (10 mg/wk).
- **RESTOR NCT06658093 (Barshop, recruiting):** rapamycin **or** everolimus PK/PD dose-finding ages **65–90** (adaptive daily + intermittent → 6-mo PBO); sex-split OD; EARLY_PHASE1 **n≈194**; young untreated **20–30** reference for youthful mTOR targets — L1 adjacency while **VITAL-H** remains Coming Soon / no NCT / no arm mg.
- **UTSW NCT06727305 (Timofte, recruiting):** sirolimus **or** everolimus start **0.5 / 1 / 2 mg** PO daily then titrate to trough **5–7 ng/ml** (ages ≥65; n≈60) — explicit starting-mg ladder beside RESTOR's unpublished adaptive OD; **≠** invent RESTOR/VITAL-H milligrams.
- **EVERLAST NCT05835999 (UW, COMPLETED 2026-07):** everolimus **0.5 mg/day** or **5 mg/week** ×24 wk in insulin-resistant ages 55–80 — **Results still unposted**; Cap Times (Jan 2026) places analysis in **summer 2026** after late-2025 recruitment close (**>84** enrolled; press “rapamycin” wording ≠ everolimus drug); fixed-dose twin to UTSW titration / RESTOR adaptive OD.
- **VITAL-H route:** sponsor press states rapa / dapagliflozin / semaglutide are **orally administered**; participants take **one pill daily** (+ wearable ring; hybrid decentralized SA sites; Stanford IC validation) → oral-sema adjacency: **Rybelsus R1 3→7→14 mg**; **R2/Ozempic tablets 1.5/4/9 mg** bioeq; **Wegovy pill** FDA Dec 2025 / CHMP May 2026 oral **25 mg** maintenance (start **1.5 mg**; tablets **1.5/4/9/25**) for **obesity/weight** — **≠** invent VITAL-H aging arm mg; **OASIS 1 oral 50 mg** efficacy published but **not FDA-approved**; injectable Ozempic/Wegovy not assumed. Ops: **five-year** ARPA-H contract; enroll framed **~2027**; NCT still absent.
- **TRIAD (dogs):** lifespan-primary rapamycin RCT underway — bridge species for L1 evidence.
- L1 rule unchanged: rapamycin-class remains strongest mammalian Pathway-A lever, but human healthspan claims stay provisional.



## Update — Ralph wake #9 (chemical reprogramming)
- L4 alternative to genetic OSK: **small-molecule partial chemical reprogramming** (Yang 2023; EMBO Mol Med 2025 lifespan signals).
- Safety flag: in vivo chemical regimens can drive **toxic lipid-droplet accumulation** that blocks rejuvenation — schedule/dose still first-class risks, same as pulsed OSK.



## Update — Ralph wake #10 (mitochondria transplant)
- L2/L6 bridge: **mitochondria transplantation/transfer** (Nature 2023; Nat Metab 2025 nomenclature) — organelle replacement for information-limited mito damage.
- Human foothold is acute ischemic/cardiac settings, not elective longevity; still maps to Pathway B when mtDNA/quality cannot be repaired in situ.



### L1/L3 note — EV messengers + clock editing (Ralph wake #13)
- **Young sEV / CDC-EV** therapies sit between L1 (systemic circulating factors) and L3 (mitochondrial/metabolic repair via PGC-1α). Prefer defined cargo or GMP EV products over wholesale plasma.
- **CRISPR epigenetic clock editing** (Nat Aging 2025) shows network bystander effects at age CpGs — useful for mapping the clock network, not yet a directed rejuvenation dial. Partial OSK/chemical reprogramming remains the primary L4 epigenetic reset path.



### L1 note — VITAL-H drug triad evidence (Ralph wake #20)
- **Semaglutide (SELECT)**: 20% MACE reduction in obese CVD without diabetes; partial mediation via waist circumference.
- **SGLT2i**: indirect senolysis (Nat Aging 2024) + dapagliflozin IL-1β drop in T2D RCT — calorie-restriction-mimetic / inflammaging lever.
- **Rapamycin (PEARL)**: already logged — 48-wk intermittent low-dose relatively safe; sex-specific lean-mass signals.

