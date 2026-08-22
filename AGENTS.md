# AGENTS.md — live-forever

Longevity research engine. Literature + systems design only. **Not** medical advice. **Not** DIY biotech.

## Before non-trivial work

1. Read `docs/reference/BACKLOG.md` and `scripts/ralph_tick.py` `NEXT_QUERIES`.
2. Read latest CEO update under `docs/reference/ceo-update-*.md` (prefer newest date/suffix).
3. Load skill **`live-forever-ralph-hillclimb`** (project + `~/.claude/skills/`).
4. For paper / OSS positioning: `docs/ideation/paper-l0-control-instrumentation.md` + `docs/reference/related-open-tools.md` + `design/gaps/geroscience-epistemics.md`.

## Ralph wake checklist

```powershell
cd C:\dev\projects\live-forever
python scripts\ralph_tick.py
# Exa/Web research NEXT_QUERIES → append ≥3–5 sources to corpus\sources.yaml
# Update docs\hillclimb.md + design\gaps\ab-trial-design.md (+ ultra-design / medicine-pipeline when load-bearing)
# Append dossier after unique ## Update (Ralph wake #N) or EOF — never bare "negatives held" StrReplace
python scripts\status.py
# Refresh NEXT_QUERIES in scripts\ralph_tick.py
python -m pytest tests -q --cache-clear
```

## Hard rules (CEO lessons — L1–L25)

**Foundation (2026-08-21):**

1. **GOAL_MET is a floor** — keep climbing unpublished NCT/mg/Results.
2. **COMPLETED ≠ Results** — hunt tables/manuscripts after registry COMPLETED.
3. **Adjacency ≠ invention** — never invent arm/Finals milligrams from labels or sister trials.
4. **Concentration ≠ daily dose**; **route text is load-bearing**.
5. **Name-collision filter** before banking any NCT/drug pin.
6. **Disease / commercial / patent ≠ Finals / PROSPR healthy-aging protocol**.
7. **Bank negatives** (“still absent”) every wake; rotate queries.
8. **Windows YAML/pytest hygiene** (ASCII appends, quote summaries with `:`, `--cache-clear`).
9. **Bidirectional oracles** — do not trust prose-only checks.
10. **Safety boundary** — no DIY gene editing, synthesis, or personal dosing.

**Added 2026-08-22 AM (wakes #160–#218):**

11. **Stale lab/recruitment pages ≠ Results** — consumer copy can lag CT.gov COMPLETED.
12. **Patent/IP ≠ IND filed** — bibliographic IP is not clinical progress.
13. **OASIS obesity sema 25/50 mg ≠ VITAL-H healthy-older arm mg**.
14. **Queuine flat vs drop = assay/cohort mismatch** — UNSETTLED until harmonized.
15. **Mouse lifespan preprint ≠ human supplementation NCT**.
16. **Intravitreal ER-100 OSK ≠ systemic OSK dossier clearance**.
17. **CCL11 trials vacant** — mechanism hot; human longevity depletion IND absent.
18. **Oracle last** — run `status.py` + pytest before claiming wake complete.

**Added 2026-08-22 PM (wakes #219–#246):**

19. **Disease-label dose ≠ healthy-aging pilot** — Forzinity Barth 40 mg ≠ invent SHAPE.
20. **Press timeline ≠ CT.gov NCT** — "start later 2026" journalism ≠ registry ID.
21. **Non-unique StrReplace inserts mid-file** — unique wake header or EOF only.
22. **Duplicate wake sections = same-turn cleanup**.
23. **Estimated primary completion past ≠ Results Posted**.
24. **Protocol Version / aggregator metadata ≠ Results tables**.
25. **Review "not demonstrated" corroborates absence** — does not invent a trial.

## Do not

- Commit unless the user explicitly asks.
- Equate CogState with Creyos / Cognitrax / NIH Toolbox / MoCA.
- Treat consumer EV counts, trademark ingredient lists, or patent grants as clinical protocol doses.
- Infer EVERLAST readout from Konopka lab recruitment copy when CT.gov says COMPLETED + No Results.
- Invent SHAPE daily mg from Forzinity Barth label.
- StrReplace on bare "negatives held" lines in `ab-trial-design.md`.

## Pointers

| Artifact | Path |
|----------|------|
| Full backlog | `docs/reference/BACKLOG.md` |
| Lessons (latest PM) | `docs/reference/lessons-learned-2026-08-22-pm.md` |
| Lessons (AM L11–L18) | `docs/reference/lessons-learned-2026-08-22.md` |
| Lessons (foundation) | `docs/reference/lessons-learned-2026-08-21.md` |
| CEO update (latest) | `docs/reference/ceo-update-2026-08-22-pm.md` |
| Gap register | `docs/gap_register.json` |
| Cursor rule | `.cursor/rules/live-forever-ralph.mdc` |
