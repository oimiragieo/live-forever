# How Medicine Is Made — Map for Longevity Interventions

Conceptual pipeline only. Any longevity modality (small molecule, AAV, CAR-T, cell therapy) must traverse this path to become real medicine.

## Cascade

```
Target ID → Target Validation → Hit ID (HTS/VS/fragments)
    → Hit-to-Lead → Lead Optimization (SAR + ADMET)
    → Candidate Selection → IND-enabling (GLP tox, CMC)
    → IND → Phase 0/I (safety) → Phase II (efficacy)
    → Phase III (outcomes) → NDA/BLA → Phase IV surveillance
```

Typical: **12–15 years**, **>$1B**, ~1 in 10,000 screened compounds reaches market (classic small-molecule stats).

## Stages (NIH Clinical Center + Hughes 2011 + Frontiers 2023)

| Stage | Longevity-specific note |
|-------|-------------------------|
| Target ID | Hallmarks nodes (mTOR, SCAP, OSK circuits, PARP/NAD, uPAR) — speculative biology |
| Validation | KO/KI, antisense, antibodies, organoid aging assays |
| HTS | Need senescence-selective or repair-fidelity assays — hard |
| ADMET | Tissue delivery (brain, stem niches) is the failure mode |
| GLP tox | Genotoxicity package critical for DNA-repair modulators & editors |
| GMP | Viral vectors / LNPs / cells — CMC is often the bottleneck |
| Phase I | Safety in older adults; oncology signals watched early |
| Phase II | Pick a **disease** endpoint (CKD, AD feasibility, osteoarthritis) not “aging” alone |
| Phase III | Hard outcomes: mortality, disability-free survival |
| Phase IV | Lifetime cancer / clonal evolution surveillance |

## Modality map

| Modality | Example in corpus | Extra gates |
|----------|-------------------|-------------|
| Small molecule | Rapamycin, D+Q, SIRT6 activators | Classic IND |
| Gene therapy / OSK | AAV-OSK vision | Shedding, integration, teratoma |
| Base editor | HGPS ABE | Off-target edits, delivery |
| Cell therapy | Senolytic CAR-T | CRS, on-target off-tumor |
| Organoid/cell replace | Clinical organoids | Identity, scale, GMP grade |

## Implication for “live forever”

A longevity **recipe** that never specifies its IND/GMP path is fiction. This repo’s ultra-design treats L2–L6 as a **portfolio of R&D programs**, each with its own CMC and trial plan, coordinated by L0 biomarkers.

## 2026 external trial infrastructure (map into cascade)

| Program | Role in cascade | Longevity note |
|---------|-----------------|----------------|
| ARPA-H PROSPR / VITAL-H | Phase II–III style outcomes + IC validation | Sex-stratified PK for SGLT2 (ITP cana lesson); IC domain endpoints near-term |
| XPRIZE Healthspan Finals | Parallel RCT feasibility / modality bake-off | Not a surrogate for NDA; useful for L3 modality ranking |
| NIA ITP | Preclinical lifespan oracle | Age-windowed + sex-dimorphic effects must gate human dose/start-age |
| Disease IND (AD, PSP, fibrosis, DSP ACM) | Classic Phase I–II truth | Prefer disease PoC before healthspan expansion (TPN-101, ER-100, RJB-0402) |

### PROSPR performer map (refresh wake #52)

| Performer | Modality / thesis | Cascade position | Watch |
|-----------|-------------------|------------------|-------|
| VITAL-H (Barshop) | Rapa / dapa / sema vs PBO; n=726 ages ~60–65 | Hybrid Ph3 + IC validation | NCT still absent; enroll ~2027 |
| Stanford PROSPR-IC / THRIVE | IC score + OpenCures kit | Endpoint infrastructure | Domain-first regulatory path |
| Cambrian TORnado | mTORC1-selective | Pre-FIH (public) | vs low-dose rapa in VITAL-H |
| Linnaeus LNS8801 | GPER agonist (+ ITP) | Oncology RP2D **125 mg PO daily** (NCT06624644 / NCT04130516; orphan uveal melanoma); **>100** oncology pts; ITP 2026 + PROSPR IC; AdisInsight **plans** elderly-volunteer healthspan RCT (PO) — **no CT.gov NCT/dose** (wake #180 recheck; IC-titled unrelated trials **≠** LNS8801) | Do not equate oncology 125 mg with PROSPR healthspan dose |
| Rochester / Transposon TPN-101 | LINE-1 RT inhibitor | Disease PoC done (**PSP 100/200/400 mg**; **C9-ALS 400 mg**; AGS weight-adjusted); PROSPR aging RCT **n=200 ages 60–65 ×48 wk IC** (Rochester/UConn/UTMB) — **no CT.gov NCT/dose** (wake #181); AD Ph2 + HEALEY RSA still unregistered | Do not equate disease 400 mg with PROSPR healthy-older dose |
| Nula NLT-101 | Nuclear-envelope SM (17αE2-inspired) | Metabolic Ph1 aim 2026; PROSPR IC preclinical→possible healthy-older RCT | MoA details sparse; AASLD abstract expected |
| Columbia FAST | Biomarker mining | Assay / endpoint | Feeds IC composites |

### XPRIZE Healthspan Milestone-2 awardees ($1M each; Finals RCT through ~2029)

| Team | Modality | Design note |
|------|----------|-------------|
| Mitochondrial All Stars (Mighty + UW Marcinek) | Elamipretide (cardiolipin) | FORZINITY **40 mg/day** Barth ≥30 kg (**20 mg** if eGFR <30); Barth RCT missed 6MWT/fatigue; Landscape Semi-Finals **N=23** ages 65–79 ×4 wk (trends claimed); CT.gov **SHAPE** still **RECRUITING** ~30; vial **80 mg/mL**; **mg/day unpublished**; FORZINITY **0.5 mL = 40 mg** same conc. family **≠** invent SHAPE dose; Campbell/Marcinek mice **3 mg/kg IP 2×/wk** **≠** human daily SC — do not equate Barth 40 mg or mouse 3 mg/kg with SHAPE/Finals |
| Longeveron | MSC (laromestrocel) | Ph2b frailty N=148 IV **25/50/100/200M** (ages **70–85**, TNF-α ≥2.5); CSC **+63.4m@9mo** (200M) / **+49.2m** (50M); **ELPIS II NCT04925024** **2.5×10⁵ cells/kg** IM Stage II (infants; DB lock **Aug 31 2026** / topline **mid-Sep**; **HLHS ≠ Finals**); Bahamas ~200 pts / 350+ doses; **XPRIZE Finals cell dose unpublished** |
| AgelessRx | Multi-agent stack | Pilot NCT07475546: **n=26 / 18 analyzed**; IRB **IRCM-2025-437**; pilot doses ≠ Finals; Finals 9-agent + Infinite — **14-mo / 12-component**, enroll **186 over 22 mo** (~235 w/ dropouts), ages 50–90; **progressive RT + coaching**; separate **NCT07092605** Semaglutide microdose (ages **18–65**; page **0.1–0.5 mg/wk**; **≠** Finals tirzepatide); IRB still ~Oct 2026, **no Finals NCT/agent-mg** |
| Johns Hopkins–Suninflam | Gal-3 mAb (SIF001) | NCT07051629 est. **n=88**; SAD/MAD **10/20/50/80 mg/kg IV** (**Q2W** MAD, 1h; PK/ADA →D75); epilepsy ages **18–70** (≥4 seizures/4 wk); ChiCTR DRE **50 mg/kg** ≠ Finals; Landscape Finals Ph2a **N=100** MCI — **Finals dose still private** |
| Minicircle | FST+Klotho plasmid SC | Landscape GARM FST+KL **n=14 / 10 completed**; NCT07285629 est. **n=30** ages 50–80 SC abdominal fat (Rx outside US; still RECRUITING past Jun 2026); cognition ≠ CogState; **Finals plasmid µg / 1y schedule unpublished** |
| Goda Lab / NanoTitan | Super exosomes (europium-ion SHT → senescent/target cells) | Preclinical mouse frailty; FIH via **SiRIUS / Tohoku Healthspan Research Center** (+ **Tokyo Relife** on XPRIZE M2 card / PR TIMES); **NanoTitan KK** (corp **9010401195917**, Roppongi, reg. **2026-01-23**); adjacent **jRCT1033250410** iPS-exosome **nasal** DB-PBO high/low/PBO QD×4 wk n=45 MCI (**≠** lanthanide super-EV; particle counts unpublished; still **募集中断** 2026-01-30; **Reprocell RCEV002** 2 mL / NTA 50–150 nm ≠ arm dose); Guidon **2/6/18 μg** + Ruijin **5/10/20 μg** nasal ug ladders **≠** Relife; Nature Eu/Tb sEV prep **~4e7/ml** (method ≠ Finals/jRCT); press scaling conflict (official **>15y** vs NAD.com **~40y**) **≠** Finals particles; **Finals n/dose unpublished** |
| NYC-Vita (Mount Sinai) | Combo | Ph1b NCT07058974 **n≈22**: spermidine **2 mg/day** + HIIT/RT + rapa **or** lamivudine; Landscape Finals card: **rapa + spermidine + HIIT/RT** ages 50–90 (+ Chrysea Sprevive dose-escalation); **Finals n still unpublished** |
| RETRO-EPIGERNA | tRNA/queuine (KYN) capsule | Landscape: DB-PBO **n=12 (6:6)** ages 50–80 ×1 mo; muscle/immune up, MoCA flat; **unregistered grade D**; M2 press: judges noted **p16/p21 −40–60%** (unauditable); **preclinical queuine** **10 μg/kg q3d** oral (+15.3% mouse mean LS; **≠** Finals capsule mg); **Finals dose/NCT opaque** |
| RPRGAON-Progeria (Progerinin) | HGPS Ph2a lineage | NCT06775041: **500–1500 mg/day BID** (+ lonafarnib), n=10, still **ACTIVE_NOT_RECRUITING** / **No Results** (Sentynl 1H2026 window missed); **NCT05847179** Werner BMD **2400 mg/day (1200 mg BID)** ×1 y n=5 **NOT_YET_RECRUITING** (**Werner ≠ HGPS ≠ Finals**); topical **1%** ×4 wk claimed **+23.6%** dermal density ≠ oral; **Finals ordinary-aging NCT/mg unpublished** |
| TIME TRAVELER | Plant-EVs (parsley; FROZEN-TT01) | M2 Finalist; **UMIN000059942** COMPLETED — **1 cap QD × 8 wk** DB-PBO ages **55–<70**, n=40 / 39; endpoint map grip/TUG/NK/**Cognitrax** (≠ CogState); **results unpublished** (grade D); Finals dose/NCT thin (exofull 50B ≠ protocol without EV count) |

**Not among $1M M2 awardees (still Finals-eligible / adjacent):** Intervene Immune (TRIIM-X still **RECRUITING** past est. 2025-12); **GI Innovation / GI Longevity** (top-20 Finalist) — GIANTS-1 NCT07363057: **GI-102 (efzilonkofusp alfa) 0.02 mg/kg IV Q4W** + **GIB-7** 4-strain synbiotic QD (**5×10⁸ CFU/day** from prior NCT05735418 Biome #7; B2/ginseng prebiotics; grip primary COMPLETED but public Results still thin), Ph2a n≈15 still RECRUITING; endpoints NK/CD8 + grip/6MWT; cognition = **NIH Toolbox ≠ CogState**; oncology KEYNOTE-G08 **NCT05824975** IV **0.06–0.45 mg/kg Q3W** / SC **0.12–0.24 mg/kg Q3W** (**≠** GIANTS aging dose/schedule); **ProGen MOU** (May 2025) names **PG-102** (GLP-1/GLP-2) for cognition alongside GI-102+GIB-7 (**≠** signed Finals partner / NCT amendment; GIANTS still GI-102+GIB-7 only); PG-102 disease Ph2 **NCT06712615** SC obesity/T2D + **NCT07187856** SC QW vs sema **1.0 mg**; Ph1 MAD **15 / 30 / 30–60 mg** SC QW (NCT06309667) (**≠** GIANTS cognition dose); **GI Cell autologous NK ≠** GIANTS protocol. **Boston Healthspan** — semaglutide (SELECT disease-path **2.4 mg QW** ≠ Finals pin) + **ALG-801** (AliveGen ActRIIA/IIB ligand trap; Justice interview combo pin); Ph1b MAD **ACTRN12623000204640** COMPLETED **n=32** postmenopausal (**mg unpublished**); **no Finals NCT**; Bhasin/Manson Brigham M1 pilot only. **Abe Yoando** — Justice Finals approach: **NMN + β-hydroxybutyrate + ginsenosides**; company Aug 12 PR still **NMN + kampo** only (**no BHB/ginsenoside mg**); semi-finals drink **42 d** ages **47–65** (**no public UMIN/jRCT/CT.gov**); Finals plan **n≈100 ×1 y** from **Oct 2026**; **YOANDO TM** manufacturing triad **≠** clinical mg; safety pin **NMN 3000 mg QD ×28 d** (≠ Finals mg); **GS-Rb1 500 mg CKD ≠** Finals; **KRGE / RG PK ≠** Finals; commercial **SHIN-ZAN** / **Chouyu ≠** Finals; **D-BHB 1.5–10 g** RCTs **≠** Finals BHB mg; Finals NCT/drink mg unpublished. **ASU Team Healthspan** — **4-component** multibaric (**15 min hypoxia + 1 h HBOT**; chamber **≤2.4 ATA / 0.356 ATM**) + Smart Fit + Theriome; Finals **~200 ×1 y**; Smart Fit Jul 2026 PoC press (**no ATA/%**); **NCT06734468** lifestyle-only (**≠** Finals chamber); operating ATA/%O2 unpublished. **GOQii Sanjeevini** — biomarker-gated stack + PRT + yoga (Justice); PoC **60 d n=40/39** (**no public CT.gov/CTRI ID**); Finals **12-mo** 4-city; **MoCA ≠ CogState**; Decode Age Longevian commercial mg **≠** Finals supplement IDs; NCT unpublished (**≠ GPLIFE NCT07534878**). **NUS PROMETHEUS** NCT07451496 — whey/creatine/fucoidan + conditional UA/NMN/ergo; **NIH Toolbox ≠ CogState**; primary completion **ACTUAL 2026-02-23**. **Japan Longevity Consortium** — Flow / Scientific Zen; TEAS cite likely Lishui **n=300** post-stroke ICU (**≠ Finals**). **Lono Jaeyak** — Gunsan QT / **Jeonju** registry (**2024-08-26**); **3** staff; **LON301/KUYACHEON** (Justice); **≠ HL301** (Hanlim bronchitis **600 mg/day** botanical — name collision); **≠ KIO-301** (Kiora ocular RP — name collision); **EP4509119**: ATM (**KU60019**/AZ32) + ROCK (**Y27632**) + Bcl-2 (**ABT263**/737/**linderalactone**) ± RSV ± metformin; mechanism **Yang Comm Biol 2022** FOXM1→E2F1 (in vitro µM ≠ oral Finals mg); **US12258578** KU-60019 can **accelerate** fibroblast aging in vitro (**≠** FOXM1-up Finals claim; bidirectional ATM risk); **FOXM1 dual**: SnC-survival/senolysis (**STTT 2025**) **≠** FOXM1-up revitalization; **AZ32** oral **200 mg/kg** mice glioma only; **AZD1390** oral ATM + RT glioma Ph1 MTD **400 mg/d** recurrent / **300 mg/d** newly diagnosed (**≠** Finals); **Y-27632** human = corneal (**≠** oral Finals); **lonitoclax** HV **≤800 mg** oral Bcl-2 / **venetoclax** HV **≤400 mg** (B-cell PD) (**≠** Finals); **KINE-101** Treg peptide MAD **≠** Lono. **ANI Biome** — ELITE Sheba **n=31/30 ×8 wk** (**no CT.gov**); **AB-01/AB-02** mg unpublished; **GlycanAge ≠ iAge/IMM-AGE**; **NCT07596576 SHARP ≠ ELITE**; Gladyshev/Snyder collaborators; Finals NCT absent. **Morinaga** — Passienol dose ladder **10/20/30/100 mg** piceatannol (Kitada **20 mg** metabolic; SIRT1 **UMIN000052082** n=281; fat-ox **10 mg ×7 d** n=9; sleep **UMIN000056168** **10 mg ×4 wk**); **UMIN000018397** glucose/vascular **4 caps/d ×2 mo** (**mg opaque** on registry); consumer tablets **10 mg PIC + 10 mg niacin/day** (**≠** Finals triad); company XPRIZE PR still **piceatannol-only** (Justice Passienol+niacin ≠ published Finals mg); C2C12 **10–50 µM** Ho-1/Sod1 (**≠** oral Finals); PD **niacin 250 mg** / **Niaspan 1–2 g** **≠** Finals; triad NCT absent. **GI Innovation** — Samsung **Lee Woo-yong**; GIANTS-1 ISRCTN endpoints (knee/BIA/ISI/NIH Toolbox); still RECRUITING; seeking cognitive partner.

### XPRIZE M2 modality camps (wake #58 refresh)

| Camp | Teams | Design implication |
|------|-------|-------------------|
| Combo L1 pharmacologic + lifestyle | AgelessRx; NYC-Vita | Breadth vs depth; hard to attribute; still useful IC-domain signal |
| EV / cell regenerative | Goda/NanoTitan; Longeveron MSC; TIME TRAVELER plant-EVs | CMC/GMP is the bottleneck; consumer EV doses ≠ Finals therapeutic doses |
| Single-driver molecular | Suninflam Gal-3; Progerinin; Minicircle FST/Klotho; Mighty elamipretide; RETRO-EPIGERNA tRNA/queuine | Cleaner causal claim; disease or opaque pilots often precede healthspan RCT |

### XPRIZE Utah DCC Finals SOPs (wake #64)

| Domain | Required / named measure | Notes |
|--------|--------------------------|-------|
| Muscle | 6MWT mandatory; lower-body power; peak VO2 optional | Muscle mass (D3-creatine/imaging) strongly recommended, not mandatory |
| Cognition | **CogState** (Rules V1.0; DET/IDN/OCL/ONB/GMLT/IDSSTS) | Guidelines V2.2 still say CANTAB — **Rules supersede** for Finalists |
| Immune | iAge + IMM-AGE + **response-to-challenge** (pending assay; Rules Table 8e **Immune Response Proxy** still TBD; Stein UCSD central lab Aug 2026) — need 2 of 3 | Category named in Rules V1.0; Landscape Aug 2026 omits vendor; Finalist-gated SOPs expected |
| Visits | 2 baselines (~1 mo apart) → randomize; midpoints 6/9 mo (minimal); FU 11+12 mo | 6 required visits; responder = avg baseline vs avg FU |
| Sample size | **≥40 per arm** (Finals FAQ); **≥100 total** recruit/retain essential (Finals Application template; scale ~100–150) | Strongly encourage larger; AgelessRx plan ~235 enroll / 186 analyze exceeds both floors; NYC-Vita Finals n still unpublished |
| Adjudication | Utah DCC + personalized 10/15/20y thresholds; global responder all 3 domains | Rx−control ≥20pp; one-sided 90% CI LB >15% |

Full visit-level biospecimen SOPs remain Finalist-gated; public floor is Guidelines V2.2 + Finals Rules V1.0 (Rules win on conflicts). **Cognition conflict resolved:** Rules V1.0 select **CogState** (supersedes Guidelines V2.2 CANTAB line).
