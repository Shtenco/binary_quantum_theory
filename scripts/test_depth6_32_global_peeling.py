#!/usr/bin/env python3
import unittest

import numpy as np

import depth6_32_global_peeling as P


class GlobalPeelingContractTests(unittest.TestCase):
    def setUp(self):
        self.blocks = [
            {
                'orbit_id': 1,
                'm': 2,
                'q_rows': {
                    ('unique-a',): 1,
                    ('shared',): 1,
                },
            },
            {
                'orbit_id': 2,
                'm': 1,
                'q_rows': {
                    ('unique-b',): 1,
                    ('shared',): 1,
                },
            },
        ]

    def test_exact_coverage_is_required_before_any_global_peeling_plan(self):
        with self.assertRaisesRegex(RuntimeError, 'exact KEYMETA coverage required'):
            P.plan_peeling_wave(
                self.blocks[:1],
                target_blocks=2,
                target_columns=3,
            )

    def test_candidate_is_not_rank_certificate_and_wave_is_iterative(self):
        wave0 = P.plan_peeling_wave(
            self.blocks,
            target_blocks=2,
            target_columns=3,
        )
        self.assertEqual([c['orbit_id'] for c in wave0['candidates']], [2])
        c = wave0['candidates'][0]
        self.assertEqual(c['m'], 1)
        self.assertEqual(c['unique_rows'], 1)
        self.assertFalse(c['rank_certified'])
        self.assertFalse(wave0['rank_certified'])
        self.assertFalse(wave0['numerical_closure_claimed'])

        # If orbit 2 is later certified and peeled, the previously shared q
        # becomes unique to orbit 1.  Orbit 1 then has 2 exclusive rows for m=2.
        wave1 = P.plan_peeling_wave(
            self.blocks,
            target_blocks=2,
            target_columns=3,
            active_orbit_ids={1},
        )
        self.assertEqual([c['orbit_id'] for c in wave1['candidates']], [1])
        self.assertEqual(wave1['candidates'][0]['unique_rows'], 2)
        self.assertEqual(
            set(wave1['candidates'][0]['unique_qs']),
            {('unique-a',), ('shared',)},
        )

    def test_full_rank_unique_q_stack_certifies_one_block(self):
        block = self.blocks[0]
        master_map = {
            ('unique-a',): np.array([[1.0, 0.0]]),
            ('shared',): np.array([[0.0, 1.0]]),
        }
        cert = P.certify_unique_q_stack(
            block,
            master_map,
            [('unique-a',), ('shared',)],
            rtol=1e-12,
            atol=1e-14,
        )
        self.assertEqual(cert['rank'], 2)
        self.assertTrue(cert['rank_certified'])
        self.assertGreater(cert['sigma_min'], cert['threshold'])
        self.assertFalse(cert['numerical_closure_claimed'])

    def test_rank_deficient_unique_q_stack_does_not_peel(self):
        block = self.blocks[0]
        master_map = {
            ('unique-a',): np.array([[1.0, 0.0]]),
            ('shared',): np.array([[2.0, 0.0]]),
        }
        cert = P.certify_unique_q_stack(
            block,
            master_map,
            [('unique-a',), ('shared',)],
            rtol=1e-12,
            atol=1e-14,
        )
        self.assertEqual(cert['rank'], 1)
        self.assertFalse(cert['rank_certified'])
        self.assertFalse(cert['numerical_closure_claimed'])

    def test_missing_unique_q_matrix_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, 'missing unique q matrix'):
            P.certify_unique_q_stack(
                self.blocks[0],
                {('unique-a',): np.array([[1.0, 0.0]])},
                [('unique-a',), ('shared',)],
            )


if __name__ == '__main__':
    unittest.main()
