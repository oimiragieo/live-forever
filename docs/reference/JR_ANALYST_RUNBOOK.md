# Jr analyst runbook — live-forever

Audience: someone picking up this repo cold. Read this before inventing anything.

## What this product is

A **longevity research engine**: curated literature corpus + control-theoretic design + Ralph hill-climb loop that banks honest “still missing” clinical pins.

It is **not** medical advice. It is **not** a place to invent trial milligrams.

## Safety (non-negotiable)

- Literature + systems design only.
- No DIY gene editing, synthesis recipes, or personal dosing.
- Never fill unpublished NCT / arm / Finals milligrams from adjacency (OASIS ≠ VITAL-H, Forzinity ≠ SHAPE, etc.).

## First 15 minutes

```powershell
cd C:\dev\projects\live-forever
pip install -r requirements-dev.txt
python scripts\status.py
python scripts\validate_corpus.py
pytest -q --cache-clear
```

Expect: `GOAL_MET`, `CORPUS_OK`, tests green.

## How Ralph wakes work

1. Read `scripts/ralph_tick.py` → `NEXT_QUERIES` (top 3).
2. Search Exa / ClinicalTrials.gov.
3. Append ≥3–5 entries to `corpus/sources.yaml` (unique `id`, quote `summary:` if it contains `:`).
4. Append `## Tick N` to `docs/hillclimb.md` and `## Update (Ralph wake #N)` to `design/gaps/ab-trial-design.md` (**EOF only**).
5. Rotate top 3 queries to the bottom of `NEXT_QUERIES`.
6. `status.py` → `validate_corpus.py` → `pytest`.
7. If public git: commit+push the four wake files (PowerShell `$msg=…`; no bash heredoc).

Skill: `live-forever-ralph-hillclimb`. Rules: `AGENTS.md`.

## Banking a negative (this is progress)

If Results / NCT / dose still absent, write an explicit negative corpus entry and dossier update. Do **not** invent numbers to “close” the pin.

Absence wording for registry vacuums: **“no matching NCT in searched sources as of DATE”** — not absolute nonexistence.

## What is still open forever (until clinic publishes)

See `docs/reference/SENTINEL_BOARD.md` and BACKLOG sections D1–D5. Those stay **OPEN** under Ralph sentinel — software cannot close them.

## Docs map

| Need | File |
|------|------|
| Full backlog | `docs/reference/BACKLOG.md` |
| Latest CEO update | `docs/reference/ceo-update-2026-08-22-night.md` |
| Lessons L1–L39 | `docs/reference/lessons-learned-*.md` (night = L33–L39) |
| Paper brief | `docs/ideation/paper-l0-control-instrumentation.md` |
| This wave plan | `docs/superpowers/plans/2026-08-22-enterprise-hardening-wave1.md` |

## Ops findings (2026-08-22 evening)

- WSL `cursor-agent` / `agent` requires `agent login` (or `CURSOR_API_KEY`) before free micro-subagents work.
- External thinktank seats may fail to read repo files under policy; use in-session review fallback and keep shipping closable software.
