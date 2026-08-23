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
algorithms/      # damage-control, saturating-removal, portfolio-optimizer, trial-transparency
scripts/         # ingest + ralph loop helpers + validators
docs/            # loop status / hill-climb logs / ideation blueprints
```

## Quick start

```powershell
cd C:\dev\projects\live-forever
pip install -r requirements-dev.txt

# Run two-pathway damage control simulation
python -m algorithms.damage_control --years 120 --plot-ascii

# Run multi-species saturating removal & morbidity compression calculus
python -m algorithms.saturating_removal --compare --species human

# Evaluate or optimize intervention cocktail hallmark coverage
python -m algorithms.portfolio_optimizer --eval vital_h_triad laromestrocel_msc sif001_gal3_mab progerinin
python -m algorithms.portfolio_optimizer --optimize --max-size 4

# Run clinical trial transparency & evidence delay audit
python -m algorithms.trial_transparency --audit

# Validate corpus, exit criteria, and test suite
python scripts\status.py
python scripts\validate_corpus.py
pytest -q --cache-clear
```

Jr analysts: start at [`docs/reference/JR_ANALYST_RUNBOOK.md`](docs/reference/JR_ANALYST_RUNBOOK.md). Sentinel pins (not closable by code): [`docs/reference/SENTINEL_BOARD.md`](docs/reference/SENTINEL_BOARD.md).

## Research focus (2026-08-22)

Paper spine + open-science computational engine (not another molecule review):

| Doc | Path |
|-----|------|
| **L0 control / instrumentation paper brief** | [`docs/ideation/paper-l0-control-instrumentation.md`](docs/ideation/paper-l0-control-instrumentation.md) |
| **Computational engine architecture** | [`docs/ideation/geroscience-computational-engine-architecture.md`](docs/ideation/geroscience-computational-engine-architecture.md) |
| **Related open tools** (pyaging, HAGR, ITP, …) — what we are **not** | [`docs/reference/related-open-tools.md`](docs/reference/related-open-tools.md) |
| **Geroscience epistemics / negatives-bank seed** | [`design/gaps/geroscience-epistemics.md`](design/gaps/geroscience-epistemics.md) |
| **Design + plan** | [`docs/superpowers/specs/2026-08-22-l0-paper-oss-design.md`](docs/superpowers/specs/2026-08-22-l0-paper-oss-design.md) |

Honesty: \(D(t)\) is an **operational model**; sex-split simulator \(D\) values are **illustrative** (not ITP-calibrated); `DRIVER_EDGES` are adjacency hypotheses, not a proven causal DAG; **COMPLETED ≠ Results**.

## Ralph loop

A monitored shell loop wakes the agent periodically to fill corpus gaps, re-score the design, and re-run simulations until exit criteria are green. **`GOAL_MET` is a floor** — keep climbing unpublished NCT/mg/Results (see backlog).

Agent rules: `AGENTS.md` · skill `live-forever-ralph-hillclimb`.

## CEO / backlog / lessons

| Doc | Path |
|-----|------|
| Latest CEO update | [`docs/reference/ceo-update-2026-08-22-night.md`](docs/reference/ceo-update-2026-08-22-night.md) (eve / PM / AM siblings in same folder) |
| Full backlog | [`docs/reference/BACKLOG.md`](docs/reference/BACKLOG.md) |
| Sentinel board | [`docs/reference/SENTINEL_BOARD.md`](docs/reference/SENTINEL_BOARD.md) |
| Lessons retained | night (L33–L39) + eve (L26–L32) + PM (L19–L25) + AM (L11–L18) + foundation (L1–L10) under `docs/reference/lessons-learned-*.md` |
| Contributing | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
