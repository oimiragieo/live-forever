# Live Forever — Longevity Research Engine

A research codebase that ingests biology literature (Exa / arXiv / clinical geroscience / community signals), models organismal damage as a **control problem**, and maintains an evolving ultra-design for extreme healthspan / theoretical immortality.

> **Safety boundary:** This repo is literature synthesis + systems/algorithms design. It does **not** provide DIY gene therapy, drug synthesis recipes, or lab protocols. Any translational path runs through standard medicine discovery (target → IND → GMP → trials).

## Goal (Ralph loop exit criteria)

1. **Corpus** ≥ 50 curated sources with summaries + topic tags
2. **Ultra-design** for multi-pathway longevity (DNA repair, senescence, epigenome, mito, immune, replacement)
3. **Algorithms** simulating damage boundedness (Pathway A repair + Pathway B engineered correction)
4. **Medicine map** of how interventions become real drugs
5. **Gap register** closed or explicitly deferred with evidence

## Layout

```
corpus/          # papers, sources.yaml, reddit signals
design/          # ultra-design + medicine pipeline + DNA-repair stack
algorithms/      # damage-control simulators
scripts/         # ingest + ralph loop helpers
docs/            # loop status / hill-climb logs
```

## Quick start

```powershell
cd C:\dev\projects\live-forever
python -m algorithms.damage_control --years 120 --plot-ascii
python scripts\status.py
```

## Research focus (2026-08-22)

Paper spine + open-science moat (not another molecule review):

| Doc | Path |
|-----|------|
| **L0 control / instrumentation paper brief** | [`docs/ideation/paper-l0-control-instrumentation.md`](docs/ideation/paper-l0-control-instrumentation.md) |
| **Related open tools** (pyaging, HAGR, ITP, …) — what we are **not** | [`docs/reference/related-open-tools.md`](docs/reference/related-open-tools.md) |
| **Geroscience epistemics / negatives-bank seed** | [`design/gaps/geroscience-epistemics.md`](design/gaps/geroscience-epistemics.md) |
| Design + plan | [`docs/superpowers/specs/2026-08-22-l0-paper-oss-design.md`](docs/superpowers/specs/2026-08-22-l0-paper-oss-design.md) |

Honesty: \(D(t)\) is an **operational model**; sex-split simulator \(D\) values are **illustrative** (not ITP-calibrated); `DRIVER_EDGES` are adjacency hypotheses, not a proven causal DAG; **COMPLETED ≠ Results**.

## Ralph loop

A monitored shell loop wakes the agent periodically to fill corpus gaps, re-score the design, and re-run simulations until exit criteria are green. **`GOAL_MET` is a floor** — keep climbing unpublished NCT/mg/Results (see backlog).

Agent rules: `AGENTS.md` · skill `live-forever-ralph-hillclimb`.

## CEO / backlog / lessons

| Doc | Path |
|-----|------|
| Latest CEO update | [`docs/reference/ceo-update-2026-08-22-pm.md`](docs/reference/ceo-update-2026-08-22-pm.md) (AM: [`ceo-update-2026-08-22.md`](docs/reference/ceo-update-2026-08-22.md)) |
| Full backlog | [`docs/reference/BACKLOG.md`](docs/reference/BACKLOG.md) |
| Lessons retained | [`docs/reference/lessons-learned-2026-08-22-pm.md`](docs/reference/lessons-learned-2026-08-22-pm.md) (L19–L25) + [`2026-08-22`](docs/reference/lessons-learned-2026-08-22.md) (L11–L18) + [`2026-08-21`](docs/reference/lessons-learned-2026-08-21.md) foundation |