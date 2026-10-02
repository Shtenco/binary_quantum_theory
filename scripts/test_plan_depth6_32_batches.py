#!/usr/bin/env python3
import copy
import unittest

import depth6_assignment_ledger as L
import plan_depth6_32_batches as P


def rec(orbit, m, sec=None, coord=100):
    x = {
        'orbit_id': orbit,
        'rep': [1,2,3,4,3,2,3,4,3,2],
        'm': m,
        'coord_dim': coord,
        'source_shard': orbit,
        'source_keymeta_payload_sha256': f'{orbit:064x}',
        'source_raw_run_id': 'run',
        'source_raw_artifact_id': f'a{orbit}',
        'source_raw_artifact_digest': 'sha256:' + f'{orbit+10:064x}',
        'source_tar_sha256': f'{orbit+20:064x}',
        'engine_git_blob_sha': 'd'*40,
    }
    if sec is not None:
        x['observed_sec'] = sec
    return x


def ledger(records, target_blocks=None, target_columns=None):
    if target_blocks is None:
        target_blocks = len(records)
    if target_columns is None:
        target_columns = sum(r['m'] for r in records)
    return L.build_assignment_ledger(records, target_blocks=target_blocks, target_columns=target_columns)


class BatchPlannerTests(unittest.TestCase):
    def test_incomplete_ledger_refuses_canonical_planning(self):
        lg = ledger([rec(1, 5, 10.0)], target_blocks=2, target_columns=10)
        with self.assertRaisesRegex(RuntimeError, 'incomplete persisted assignment ledger'):
            P.plan_batches(lg, batch_count=2)

    def test_incomplete_ledger_can_be_planned_only_in_diagnostic_mode(self):
        lg = ledger([rec(1, 5, 10.0)], target_blocks=2, target_columns=10)
        got = P.plan_batches(lg, batch_count=2, diagnostic=True)
        self.assertEqual('DIAGNOSTIC_ONLY_INCOMPLETE_LEDGER', got['mode'])
        self.assertFalse(got['canonical_compute_allowed'])

    def test_deterministic_greedy_balancing_uses_observed_seconds(self):
        lg = ledger([
            rec(1, 1, 10.0), rec(2, 1, 8.0), rec(3, 1, 7.0), rec(4, 1, 5.0),
        ])
        a = P.plan_batches(lg, batch_count=2)
        b = P.plan_batches(copy.deepcopy(lg), batch_count=2)
        self.assertEqual(a['manifest_sha256'], b['manifest_sha256'])
        loads = sorted(round(x['estimated_cost'], 8) for x in a['batches'])
        self.assertEqual([15.0, 15.0], loads)

    def test_union_is_exact_and_batches_do_not_overlap(self):
        lg = ledger([rec(i, 1, float(i)) for i in range(1, 8)])
        got = P.plan_batches(lg, batch_count=3)
        ids = [oid for b in got['batches'] for oid in b['orbit_ids']]
        self.assertEqual(list(range(1, 8)), sorted(ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_planner_does_not_mutate_ledger_or_records(self):
        lg = ledger([rec(1, 2, 3.0), rec(2, 2, 4.0)])
        before = copy.deepcopy(lg)
        P.plan_batches(lg, batch_count=2)
        self.assertEqual(before, lg)

    def test_fallback_cost_uses_persisted_fields_only(self):
        r = rec(1, 7, None, coord=123)
        self.assertEqual(P.persisted_cost(r), 861.0)

    def test_manifest_carries_assignment_ledger_hash_and_exact_records(self):
        lg = ledger([rec(1, 2, 3.0), rec(2, 2, 4.0)])
        got = P.plan_batches(lg, batch_count=2)
        self.assertEqual(lg['ledger_sha256'], got['assignment_ledger_sha256'])
        by_id = {r['orbit_id']: r for b in got['batches'] for r in b['records']}
        self.assertEqual({1,2}, set(by_id))
        self.assertEqual(lg['records'], [by_id[1], by_id[2]])
        self.assertRegex(got['manifest_sha256'], r'^[0-9a-f]{64}$')


if __name__ == '__main__':
    unittest.main()
