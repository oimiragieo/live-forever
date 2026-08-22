"""Bidirectional tests for docs/gap_register.json deferred dossiers."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs" / "gap_register.json"
MIN_DOSSIER_BYTES = 200


class TestGapRegisterFreshness(unittest.TestCase):
    def test_register_loads_and_open_empty(self) -> None:
        data = json.loads(REGISTER.read_text(encoding="utf-8"))
        self.assertEqual(data.get("open"), [])
        deferred = data.get("deferred_with_evidence", [])
        self.assertGreaterEqual(len(deferred), 1)

    def test_every_deferred_dossier_exists_and_nontrivial(self) -> None:
        """Positive: each deferred entry points at a real, non-empty dossier."""
        data = json.loads(REGISTER.read_text(encoding="utf-8"))
        for entry in data["deferred_with_evidence"]:
            path = ROOT / entry["dossier"]
            self.assertTrue(path.is_file(), f"missing dossier for {entry['id']}: {path}")
            self.assertGreater(
                path.stat().st_size,
                MIN_DOSSIER_BYTES,
                f"dossier too thin for {entry['id']}",
            )
            text = path.read_text(encoding="utf-8").lower()
            # Dossier should name the gap (hyphen or space form) somewhere in body.
            token = entry["id"].split("-")[0]
            self.assertTrue(
                entry["id"] in text or token in text,
                f"dossier {path} does not mention gap id/token {entry['id']}",
            )

    def test_missing_dossier_path_would_fail_existence(self) -> None:
        """Negative control: fabricated path must not exist (instrument works)."""
        fake = ROOT / "design" / "gaps" / "not-a-real-dossier-xyz.md"
        self.assertFalse(fake.exists())

    def test_closed_thymic_addendum_exists(self) -> None:
        """Wake #72 disposition: thymic-restoration is closed/mapped, file present."""
        data = json.loads(REGISTER.read_text(encoding="utf-8"))
        closed_ids = {c["id"] for c in data.get("closed", [])}
        self.assertIn("thymic-restoration", closed_ids)
        entry = next(c for c in data["closed"] if c["id"] == "thymic-restoration")
        path = ROOT / entry["dossier"]
        self.assertTrue(path.is_file())
        self.assertNotIn(
            "thymic-restoration",
            {d["id"] for d in data["deferred_with_evidence"]},
        )

    def test_deferred_ids_are_unique(self) -> None:
        data = json.loads(REGISTER.read_text(encoding="utf-8"))
        ids = [d["id"] for d in data["deferred_with_evidence"]]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
