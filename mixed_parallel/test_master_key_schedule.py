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
        # Key uniqueness alone says nothing about enough rows/rank. The later
        # raw SVD certifier must reject this 1-row / 4-column proposal.
        self.assertEqual(x['proposal_blocks'], 1)
        self.assertEqual(x['rounds'][0]['blocks'][3]['unique_rows'], 1)
        self.assertEqual(x['rounds'][0]['blocks'][3]['m'], 4)


if __name__ == '__main__':
    unittest.main()
