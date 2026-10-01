#!/usr/bin/env python3
import unittest
import numpy as np

import bqg_mixed_master_recovery as R


class RecoveryCertificateTests(unittest.TestCase):
    def test_unique_row_peeling_closes_without_structural_recompute(self):
        rec = {
            10: {"m": 1},
            11: {"m": 1},
        }
        maps = {
            10: {("v0", (1,)): np.array([[2.0]]), ("v0", (9,)): np.array([[1.0]])},
            11: {("v1", (2,)): np.array([[3.0]]), ("v0", (9,)): np.array([[1.0]])},
        }
        out = R.certify_loaded(rec, maps, target_columns=2, target_blocks=2, sigma_floor=1e-12)
        self.assertEqual(out["status"], "PASS_CLOSED_FINITE_NUMERICAL")
        self.assertEqual(out["peeled_columns"], 2)
        self.assertEqual(out["residual_columns"], 0)
        self.assertEqual(out["support_source"], "persisted_master_map_keys_only")

    def test_residual_gram_can_close_when_no_row_is_unique(self):
        rec = {
            20: {"m": 1},
            21: {"m": 1},
        }
        shared = ("v0", (7,))
        maps = {
            20: {shared: np.array([[1.0], [0.0]])},
            21: {shared: np.array([[0.0], [1.0]])},
        }
        out = R.certify_loaded(rec, maps, target_columns=2, target_blocks=2, sigma_floor=1e-12)
        self.assertEqual(out["status"], "PASS_CLOSED_FINITE_NUMERICAL")
        self.assertEqual(out["peeled_columns"], 0)
        self.assertEqual(out["residual_columns"], 2)
        self.assertGreater(out["residual_gram"]["lambda_min"], 0.9)
        self.assertEqual(out["kernel_dimension"], 0)

    def test_true_residual_null_never_promotes_to_pass(self):
        rec = {
            30: {"m": 1},
            31: {"m": 1},
        }
        shared = ("v0", (8,))
        maps = {
            30: {shared: np.array([[1.0]])},
            31: {shared: np.array([[1.0]])},
        }
        out = R.certify_loaded(rec, maps, target_columns=2, target_blocks=2, sigma_floor=1e-12)
        self.assertNotEqual(out["status"], "PASS_CLOSED_FINITE_NUMERICAL")
        self.assertIn(out["status"], {
            "RESIDUAL_NEAR_NULL_REQUIRES_INDEPENDENT_CHECK",
            "NUMERICAL_INCONCLUSIVE",
        })
        self.assertTrue(out["h2_null_lift_forbidden_without_independent_true_kernel_check"])


if __name__ == "__main__":
    unittest.main()
