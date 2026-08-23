"""
Ralph loop tick helper: report status, list next research gaps, suggest Exa queries.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from status import exit_criteria  # noqa: E402

NEXT_QUERIES = [
    "VITAL-H ClinicalTrials.gov NCT registered OR protocol milligrams Volpi Barshop 2026",
    "Nitazoxanide human aging FOXN1 thymus NCT milligrams Genah post-IR mouse",
    "Selective B2M CCL11 aging depletion human IND ClinicalTrials 2026",
    "Oral semaglutide 25 mg 50 mg OASIS vs VITAL-H aging arm milligrams recheck 2026",
    "ER-100 NCT07290244 second patient DSMB outcome OR cohort expansion 2026",
    "Deciduous iNKT IND public filing OR ClinicalTrials.gov 2026",
    "Human queuine longevity supplementation NCT milligrams Stellate STL-101 2026",
    "Queuine STL-101 plasma age-decline OR Sapience ST101 name collision reconciliation 2026",
    "RESTOR NCT06658093 first enrolled cohort milligrams OR adaptive dose published 2026",
    "SHAPE NCT07275424 Results posted OR daily elamipretide mg Marcinek 2026",
    "EVERLAST NCT05835999 Results posted OR Konopka preprint OR abstract everolimus 2026",
]


def main() -> None:
    c = exit_criteria()
    gaps = json.loads((ROOT / "docs" / "gap_register.json").read_text(encoding="utf-8"))
    print("=== LIVE-FOREVER RALPH TICK ===")
    print(json.dumps(c, indent=2))
    print("\nOpen gaps:")
    for g in gaps.get("open", []) or ["(none)"]:
        if isinstance(g, dict):
            print(f"  - [{g['priority']}] {g['id']}: {g['title']}")
        else:
            print(f"  - {g}")
    print("\nDeferred with evidence:")
    for g in gaps.get("deferred_with_evidence", []):
        print(f"  - {g['id']} -> {g.get('dossier')}")
    print("\nSuggested Exa queries:")
    for q in NEXT_QUERIES:
        print(f"  - {q}")
    print("\nGOAL_MET" if c["goal_met"] else "GOAL_OPEN — continue research")


if __name__ == "__main__":
    main()
