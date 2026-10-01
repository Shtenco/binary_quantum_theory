#!/usr/bin/env python3
import unittest
import numpy as np

import compress_master_map_qr as C
import aggregate_compact_master_qr as A


class CompactQRTests(unittest.TestCase):
    def test_reduced_qr_preserves_stacked_singular_values(self):
        rng = np.random.default_rng(12345)
        blocks = [
            rng.normal(size=(7, 4)),
            rng.normal(size=(2, 4)),
            rng.normal(size=(9, 4)),
        ]
        rs = [C.canonical_reduced_r(x) for x in blocks]
        s0 = np.linalg.svd(np.vstack(blocks), compute_uv=False)
        s1 = np.linalg.svd(np.vstack(rs), compute_uv=False)
        np.testing.assert_allclose(s1, s0, rtol=2e-12, atol=2e-12)

    def test_unique_q_qr_peeling_closes(self):
        def item(a):
            a = np.asarray(a, dtype=float)
            return {'rows': a.shape[0], 'R': C.canonical_reduced_r(a)}
        blocks = {
            10: {'m': 1, 'qfactors': {
                ('a',): item([[2.0]]),
                ('shared',): item([[1.0]]),
            }},
            11: {'m': 1, 'qfactors': {
                ('b',): item([[3.0]]),
                ('shared',): item([[1.0]]),
            }},
        }
        out = A.certify_blocks(blocks, target_columns=2, target_blocks=2, sigma_floor=1e-12)
        self.assertEqual(out['status'], 'PASS_CLOSED_FINITE_NUMERICAL')
        self.assertEqual(out['certified_blocks'], 2)
        self.assertEqual(out['certified_columns'], 2)
        self.assertEqual(out['remaining_columns'], 0)
        self.assertFalse(out['structural_recompute_performed'])

    def test_shared_q_is_residual_not_false_pass(self):
        def item(a):
            a = np.asarray(a, dtype=float)
            return {'rows': a.shape[0], 'R': C.canonical_reduced_r(a)}
        shared = ('shared',)
        blocks = {
            20: {'m': 1, 'qfactors': {shared: item([[1.0], [0.0]])}},
            21: {'m': 1, 'qfactors': {shared: item([[0.0], [1.0]])}},
        }
        out = A.certify_blocks(blocks, target_columns=2, target_blocks=2, sigma_floor=1e-12)
        self.assertEqual(out['status'], 'RESIDUAL_RAW_COUPLED_CHECK_REQUIRED')
        self.assertEqual(out['remaining_ids'], [20, 21])
        self.assertEqual(out['remaining_columns'], 2)
        self.assertIsNone(out['kernel_dimension'])
        self.assertTrue(out['h2_null_lift_forbidden_without_independent_true_kernel_check'])

    def test_input_coverage_failure_is_fail_closed(self):
        blocks = {
            1: {'m': 2, 'qfactors': {}},
        }
        out = A.certify_blocks(blocks, target_columns=3, target_blocks=2)
        self.assertEqual(out['status'], 'INPUT_COVERAGE_FAILURE')
        self.assertEqual(out['recovered_blocks'], 1)
        self.assertEqual(out['recovered_columns'], 2)
        self.assertFalse(out['structural_recompute_performed'])


if __name__ == '__main__':
    unittest.main()
