#!/usr/bin/env python3
import unittest
import numpy as np

import certify_master_schedule_shard as S
import replay_master_numerical_certificates as R


class DistributedScheduleCertificationTests(unittest.TestCase):
    def test_raw_master_svd_full_rank_passes(self):
        maps = {
            ('u1',): np.array([[2.0, 0.0], [0.0, 3.0]]),
            ('other',): np.array([[1.0, 1.0]]),
        }
        cert = S.certify_one_block(
            orbit_index=7,
            m=2,
            master_maps=maps,
            q_keys=[('u1',)],
            sigma_floor=1e-12,
        )
        self.assertTrue(cert['pass'])
        self.assertEqual(cert['rank'], 2)
        self.assertEqual(cert['target'], 2)
        self.assertGreater(cert['sigma_min'], cert['threshold'])

    def test_raw_master_svd_rank_deficit_fails(self):
        maps = {('u1',): np.array([[1.0, 0.0], [2.0, 0.0]])}
        cert = S.certify_one_block(
            orbit_index=8,
            m=2,
            master_maps=maps,
            q_keys=[('u1',)],
            sigma_floor=1e-12,
        )
        self.assertFalse(cert['pass'])
        self.assertEqual(cert['rank'], 1)
        self.assertIsNone(cert['kernel_dimension_claim'])

    def test_missing_scheduled_q_fails_closed(self):
        with self.assertRaises(KeyError):
            S.certify_one_block(
                orbit_index=9,
                m=1,
                master_maps={('present',): np.array([[1.0]])},
                q_keys=[('missing',)],
            )

    def test_replay_keeps_failed_block_and_invalidates_later_uniqueness(self):
        # A and B share q=s. A also has unique a and is proposed first. B is
        # proposed in round 1 only because the candidate schedule assumes A was
        # removed. If A fails numerically, B's s is NOT unique and B must not be
        # accepted merely because a precomputed schedule listed it later.
        metadata = {
            1: {'m': 1, 'q_rows': {('a',): 1, ('s',): 1}, 'source_shard': 0},
            2: {'m': 1, 'q_rows': {('s',): 1}, 'source_shard': 1},
        }
        certs = {
            1: {'pass': False, 'rank': 0, 'target': 1, 'q_keys': [('a',)]},
            2: {'pass': True, 'rank': 1, 'target': 1, 'q_keys': [('s',)]},
        }
        out = R.replay(metadata, certs, sigma_floor=1e-12)
        self.assertEqual(out['accepted_ids'], [])
        self.assertEqual(out['remaining_ids'], [1, 2])
        self.assertEqual(out['status'], 'NUMERICAL_RESIDUAL_REQUIRES_FURTHER_CHECK')
        self.assertFalse(out['kernel_claim'])

    def test_replay_accepts_new_uniqueness_after_real_pass(self):
        metadata = {
            1: {'m': 1, 'q_rows': {('a',): 1, ('s',): 1}, 'source_shard': 0},
            2: {'m': 1, 'q_rows': {('s',): 1}, 'source_shard': 1},
        }
        certs = {
            1: {'pass': True, 'rank': 1, 'target': 1, 'q_keys': [('a',)]},
            2: {'pass': True, 'rank': 1, 'target': 1, 'q_keys': [('s',)]},
        }
        out = R.replay(metadata, certs, sigma_floor=1e-12)
        self.assertEqual(out['accepted_ids'], [1, 2])
        self.assertEqual(out['remaining_ids'], [])
        self.assertEqual(out['status'], 'PASS_CLOSED_FINITE_NUMERICAL')
        self.assertEqual(out['kernel_dimension'], 0)


if __name__ == '__main__':
    unittest.main()
