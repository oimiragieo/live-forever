"""Bidirectional tests for status.corpus_count / corpus_ok gate."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from status import (  # noqa: E402
    CORPUS_FLOOR,
    FINALS_MIN_N_PER_ARM,
    FINALS_MIN_TOTAL_N,
    corpus_count,
    exit_criteria,
    load_sources,
)

class TestCorpusCountOracle(unittest.TestCase):
    def test_live_corpus_count_matches_yaml_len(self) -> None:
        """Positive: exit_criteria corpus_count equals len(load_sources())."""
        sources = load_sources()
        self.assertGreaterEqual(len(sources), CORPUS_FLOOR)
        self.assertEqual(corpus_count(sources), len(sources))
        self.assertEqual(exit_criteria()["corpus_count"], len(sources))
        self.assertTrue(exit_criteria()["corpus_ok"])

    def test_empty_list_is_not_ok(self) -> None:
        """Negative control: empty corpus must fail corpus_ok threshold logic."""
        self.assertEqual(corpus_count([]), 0)
        self.assertFalse(corpus_count([]) >= CORPUS_FLOOR)

    def test_under_threshold_fails_ok_gate(self) -> None:
        """Bidirectional: CORPUS_FLOOR-1 entries must not pass; floor entries must."""
        stub = [{"id": f"x{i}"} for i in range(CORPUS_FLOOR - 1)]
        self.assertEqual(corpus_count(stub), CORPUS_FLOOR - 1)
        self.assertFalse(corpus_count(stub) >= CORPUS_FLOOR)
        stub.append({"id": "x_floor"})
        self.assertTrue(corpus_count(stub) >= CORPUS_FLOOR)

    def test_count_ignores_extra_keys_shape(self) -> None:
        """Count is len only - malformed-but-present rows still count (honest length)."""
        self.assertEqual(corpus_count([{}, {"id": "a"}, "not-a-dict"]), 3)

    def test_corpus_floor_constant_is_fifty(self) -> None:
        """Regression pin: floor must stay an explicit constant (wake #70)."""
        self.assertEqual(CORPUS_FLOOR, 50)

    def test_finals_min_n_per_arm_is_forty(self) -> None:
        """Wake #81: XPRIZE Finals FAQ minimum sample size pin (design parity)."""
        self.assertEqual(FINALS_MIN_N_PER_ARM, 40)
        # AgelessRx planned analyze n=186 / 2 arms exceeds floor (positive control)
        ageless_analyze_per_arm = 186 // 2
        self.assertGreaterEqual(ageless_analyze_per_arm, FINALS_MIN_N_PER_ARM)
        # Negative: under-powered arm fails the FAQ floor
        self.assertLess(39, FINALS_MIN_N_PER_ARM)
        # Wake #82: SHAPE pilot target n=30 is below Finals per-arm floor (pilot != Finals)
        shape_pilot_n = 30
        self.assertLess(shape_pilot_n, FINALS_MIN_N_PER_ARM)
        # Wake #84: SHAPE cognition battery is MoCA-class, not CogState Finals set
        shape_cog = {"MoCA", "Trails", "Stroop"}
        finals_cogstate = {"DET", "IDN", "OCL", "ONB", "GMLT", "IDSSTS"}
        self.assertTrue(shape_cog.isdisjoint(finals_cogstate))

    def test_finals_min_total_n_is_one_hundred(self) -> None:
        """Wake #85: Finals Application template recruit/retain >=100 essential."""
        self.assertEqual(FINALS_MIN_TOTAL_N, 100)
        # 40/arm * 2 arms is the FAQ hard floor; template urges >=100 total
        self.assertGreaterEqual(FINALS_MIN_TOTAL_N, 2 * FINALS_MIN_N_PER_ARM)
        # Positive: AgelessRx enroll 235 / analyze 186 both exceed total floor
        self.assertGreaterEqual(235, FINALS_MIN_TOTAL_N)
        self.assertGreaterEqual(186, FINALS_MIN_TOTAL_N)
        # Negative: NYC-Vita Ph1b n~22 / SHAPE pilot n=30 are below Finals total floor
        self.assertLess(22, FINALS_MIN_TOTAL_N)
        self.assertLess(30, FINALS_MIN_TOTAL_N)
        # Wake #86: GIANTS-1 PoC n=15 is far below both Finals floors
        giants1_n = 15
        self.assertLess(giants1_n, FINALS_MIN_N_PER_ARM)
        self.assertLess(giants1_n, FINALS_MIN_TOTAL_N)
        # NYC-Vita team Finals n still unpublished — must not treat Ph1b as Finals n
        nyc_vita_ph1b_n = 22
        self.assertNotEqual(nyc_vita_ph1b_n, FINALS_MIN_TOTAL_N)
        self.assertNotEqual(FINALS_MIN_TOTAL_N, 0)

    def test_exit_criteria_corpus_ok_false_when_sources_empty(self) -> None:
        """Bidirectional via exit_criteria: empty load_sources must fail corpus_ok."""
        import status as status_mod
        from unittest import mock

        with mock.patch.object(status_mod, "load_sources", return_value=[]):
            c = status_mod.exit_criteria()
        self.assertEqual(c["corpus_count"], 0)
        self.assertFalse(c["corpus_ok"])
        self.assertFalse(c["goal_met"])

    def test_goal_met_false_when_deferred_empty(self) -> None:
        """Wake #76: goal_met requires deferred_with_evidence >= 1 (bidirectional)."""
        import status as status_mod
        from unittest import mock

        live = status_mod.exit_criteria()
        self.assertGreaterEqual(live["deferred_gaps"], 1)
        self.assertTrue(live["goal_met"])

        empty_register = {
            "open": [],
            "deferred_with_evidence": [],
            "closed": [],
        }
        with mock.patch.object(
            status_mod.json,
            "loads",
            return_value=empty_register,
        ):
            # Still need gap_register path to exist - patch Path.read_text on gaps file
            real_read = status_mod.Path.read_text

            def fake_read(self, *args, **kwargs):
                if self.name == "gap_register.json":
                    return status_mod.json.dumps(empty_register)
                return real_read(self, *args, **kwargs)

            with mock.patch.object(status_mod.Path, "read_text", fake_read):
                c = status_mod.exit_criteria()
        self.assertEqual(c["deferred_gaps"], 0)
        self.assertFalse(c["goal_met"])


if __name__ == "__main__":
    unittest.main()
