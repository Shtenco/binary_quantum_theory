#!/usr/bin/env python3
import unittest

import build_master_key_peeling_schedule as S


class MasterKeyScheduleTests(unittest.TestCase):
    def test_candidate_schedule_peels_actual_key_graph(self):
        blocks = {
            1: {'m': 2, 'q_rows': {('a',): 2, ('s',): 1}, 'source_shard': 0},
            2: {'m': 3, 'q_rows': {('s',): 2}, 'source_shard': 1},
        }
        x = S.build_schedule(blocks)
        self.assertEqual(len(x['rounds']), 2)
        self.assertEqual(set(x['rounds'][0]['blocks']), {1})
        self.assertEqual(set(x['rounds'][1]['blocks']), {2})
        self.assertEqual(x['proposal_blocks'], 2)
        self.assertEqual(x['proposal_columns'], 5)
        self.assertEqual(x['proposal_remaining_ids'], [])

    def test_candidate_schedule_can_leave_residual(self):
        blocks = {
            1: {'m': 1, 'q_rows': {('s',): 1}, 'source_shard': 0},
            2: {'m': 1, 'q_rows': {('s',): 1}, 'source_shard': 1},
        }
        x = S.build_schedule(blocks)
        self.assertEqual(x['proposal_blocks'], 0)
        self.assertEqual(x['proposal_remaining_ids'], [1, 2])
        self.assertEqual(x['proposal_remaining_columns'], 2)

    def test_schedule_is_only_candidate_not_rank_proof(self):
        blocks = {
            3: {'m': 4, 'q_rows': {('u',): 1}, 'source_shard': 0},
        }
        x = S.build_schedule(blocks)
        self.assertEqual(x['proposal_blocks'], 1)
        self.assertEqual(x['rounds'][0]['blocks'][3]['unique_rows'], 1)
        self.assertEqual(x['rounds'][0]['blocks'][3]['m'], 4)

    def test_coverage_gate_reports_missing_and_blocks_schedule(self):
        records = [
            {'shard': 0, 'shards': 3, 'irrep': '32', 'engine_git_blob_sha': 'E',
             'blocks': {10: {'m': 2}}},
            {'shard': 2, 'shards': 3, 'irrep': '32', 'engine_git_blob_sha': 'E',
             'blocks': {12: {'m': 3}}},
        ]
        x = S.validate_keymeta_coverage(
            records, irrep='32', expected_shards=3,
            target_blocks=3, target_columns=6,
        )
        self.assertEqual(x['status'], 'INCOMPLETE_KEYMETA_COVERAGE')
        self.assertEqual(x['missing_shards'], [1])
        self.assertFalse(x['schedule_allowed'])
        self.assertEqual(x['recovered_blocks'], 2)
        self.assertEqual(x['recovered_columns'], 5)

    def test_coverage_gate_rejects_duplicate_shard(self):
        records = [
            {'shard': 0, 'shards': 2, 'irrep': '32', 'engine_git_blob_sha': 'E', 'blocks': {}},
            {'shard': 0, 'shards': 2, 'irrep': '32', 'engine_git_blob_sha': 'E', 'blocks': {}},
        ]
        with self.assertRaisesRegex(RuntimeError, 'duplicate shard'):
            S.validate_keymeta_coverage(
                records, irrep='32', expected_shards=2,
                target_blocks=0, target_columns=0,
            )

    def test_coverage_gate_rejects_mixed_engine_hashes(self):
        records = [
            {'shard': 0, 'shards': 2, 'irrep': '32', 'engine_git_blob_sha': 'E1', 'blocks': {}},
            {'shard': 1, 'shards': 2, 'irrep': '32', 'engine_git_blob_sha': 'E2', 'blocks': {}},
        ]
        with self.assertRaisesRegex(RuntimeError, 'multiple proof-engine blobs'):
            S.validate_keymeta_coverage(
                records, irrep='32', expected_shards=2,
                target_blocks=0, target_columns=0,
            )

    def test_coverage_gate_allows_schedule_only_at_exact_full_coverage(self):
        records = [
            {'shard': 0, 'shards': 2, 'irrep': '32', 'engine_git_blob_sha': 'E',
             'blocks': {10: {'m': 2}}},
            {'shard': 1, 'shards': 2, 'irrep': '32', 'engine_git_blob_sha': 'E',
             'blocks': {11: {'m': 3}}},
        ]
        x = S.validate_keymeta_coverage(
            records, irrep='32', expected_shards=2,
            target_blocks=2, target_columns=5,
        )
        self.assertEqual(x['status'], 'FULL_KEYMETA_COVERAGE')
        self.assertEqual(x['missing_shards'], [])
        self.assertTrue(x['schedule_allowed'])
        self.assertEqual(x['engine_git_blob_shas'], ['E'])


if __name__ == '__main__':
    unittest.main()
