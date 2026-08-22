# AGENTS.md — live-forever

Longevity research engine. Literature + systems design only. **Not** medical advice. **Not** DIY biotech.

## Before non-trivial work

1. Read `docs/reference/BACKLOG.md` and `scripts/ralph_tick.py` `NEXT_QUERIES`.
2. Read latest CEO update under `docs/reference/ceo-update-*.md` (prefer newest date/suffix — currently **night**).
3. Load skill **`live-forever-ralph-hillclimb`** (`~/.claude/skills/`).
4. For paper / OSS positioning: `docs/ideation/paper-l0-control-instrumentation.md` + `docs/reference/related-open-tools.md` + `design/gaps/geroscience-epistemics.md`.
5. Jr handoff: `docs/reference/JR_ANALYST_RUNBOOK.md` + `SENTINEL_BOARD.md`.

## Ralph wake checklist

```powershell
cd C:\dev\projects\live-forever
python scripts\ralph_tick.py
# Exa/Web research NEXT_QUERIES → write $env:TEMP\lf_wakeN.py → append ≥3–5 sources
# Update docs\hillclimb.md (unique ## Tick N) + design\gaps\ab-trial-design.md (EOF or unique wake header)
python scripts\validate_corpus.py
python scripts\status.py
# Refresh NEXT_QUERIES in scripts\ralph_tick.py
python -m pytest tests -q --cache-clear
# Public repo: git add (4 files) → $msg="…"; git commit -m $msg → git push
# If ticks stacked while busy: multi-wake catch-up same turn (L37)
```

## Hard rules (CEO lessons — L1–L39)

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

11. **Stale lab/recruitment pages ≠ Results**.
12. **Patent/IP ≠ IND filed**.
13. **OASIS obesity sema 25/50 mg ≠ VITAL-H healthy-older arm mg**.
14. **Queuine flat vs drop = assay/cohort mismatch** — UNSETTLED until harmonized.
15. **Mouse lifespan preprint ≠ human supplementation NCT**.
16. **Intravitreal ER-100 OSK ≠ systemic OSK dossier clearance**.
17. **CCL11 trials vacant** — mechanism hot; human longevity depletion IND absent.
18. **Oracle last** — run `status.py` + pytest before claiming wake complete.

**Added 2026-08-22 PM (wakes #219–#246):**

19. **Disease-label dose ≠ healthy-aging pilot** — Forzinity Barth 40 mg ≠ invent SHAPE.
20. **Press timeline ≠ CT.gov NCT**.
21. **Non-unique StrReplace inserts mid-file** — unique wake header or EOF only.
22. **Duplicate wake sections = same-turn cleanup**.
23. **Estimated primary completion past ≠ Results Posted**.
24. **Protocol Version / aggregator metadata ≠ Results tables**.
25. **Review "not demonstrated" corroborates absence** — does not invent a trial.

**Added 2026-08-22 evening (wakes #247–#275):**

26. **PowerShell inline Python mangles** — use `$env:TEMP\lf_wakeN.py`.
27. **Corpus settle before status/pytest**.
28. **Unique hillclimb `## Tick N` headers** every wake.
29. **Absence = searched sources as of DATE** — not universal nonexistence (VITAL-H pattern).
30. **Public git → commit+push** each wake (PowerShell `$msg`; no bash heredoc; no secrets).
31. **MCP tool drift** — rediscover tools; don’t stall the wake.
32. **Paper honesty** — operational \(D(t)\); sex sim illustrative ≠ ITP; don’t re-litigate Barkman.

**Added 2026-08-22 night (wakes #276–#281 + Wave-1):**

33. **Software closes software; clinics close clinical pins** — never invent mg to “finish” backlog.
34. **WSL free cursor-agent still needs login** (`agent login` / `CURSOR_API_KEY`).
35. **Thinktank/codex may deny file reads** — self-chair with security must-fixes; don’t stall forever.
36. **Corpus dogfood before CORPUS_OK brag** — unique ids, non-null `year`, `med`→medium.
37. **Stacked Ralph ticks → multi-wake catch-up** same turn when notifications pile.
38. **Enterprise wave = branch → TDD → merge --no-ff → dogfood → BACKLOG findings**.
39. **arXiv grounds patterns, not doses** — EligMeta/Samyama inspire gates/KG; never invent milligrams.

## Do not

- Equate CogState with Creyos / Cognitrax / NIH Toolbox / MoCA.
- Treat consumer EV counts, trademark ingredient lists, or patent grants as clinical protocol doses.
- Infer EVERLAST readout from Konopka lab recruitment copy when CT.gov says COMPLETED + No Results.
- Invent SHAPE daily mg from Forzinity Barth label.
- StrReplace on bare "negatives held" lines in `ab-trial-design.md`.
- Claim absolute nonexistence of a NCT from a finite search.
- Skip commit+push on a completed wake while `origin/master` tracks (unless CEO says stop).
- Claim clinical backlog closed because CI is green (L33).

## Pointers

| Artifact | Path |
|----------|------|
| Full backlog | `docs/reference/BACKLOG.md` |
| Lessons (latest night) | `docs/reference/lessons-learned-2026-08-22-night.md` |
| Lessons (eve L26–L32) | `docs/reference/lessons-learned-2026-08-22-eve.md` |
| Lessons (PM L19–L25) | `docs/reference/lessons-learned-2026-08-22-pm.md` |
| Lessons (AM L11–L18) | `docs/reference/lessons-learned-2026-08-22.md` |
| Lessons (foundation) | `docs/reference/lessons-learned-2026-08-21.md` |
| CEO update (latest) | `docs/reference/ceo-update-2026-08-22-night.md` |
| Gap register | `docs/gap_register.json` |
| Cursor rule | `.cursor/rules/live-forever-ralph.mdc` |
| Guardian agent | `~/.claude/agents/live-forever-ralph-guardian.md` |
| Jr runbook | `docs/reference/JR_ANALYST_RUNBOOK.md` |
| Sentinel board | `docs/reference/SENTINEL_BOARD.md` |
