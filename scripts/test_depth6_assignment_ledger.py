#!/usr/bin/env python3
import copy
import unittest

import depth6_assignment_ledger as L


def rec(orbit=10, m=5, rep=None, shard=1):
    return {
        'orbit_id': orbit,
        'rep': rep or [1,2,3,4,5,6,7,1,2,3],
        'm': m,
        'coord_dim': 20,
        'source_shard': shard,
        'source_keymeta_payload_sha256': 'a'*64,
        'source_raw_run_id': '36899125190',
        'source_raw_artifact_id': str(1000+shard),
        'source_raw_artifact_digest': 'sha256:'+'b'*64,
        'source_tar_sha256': 'c'*64,
        'engine_git_blob_sha': 'd'*40,
        'observed_sec': 12.5,
        'observed_rows': 100,
        'observed_row_blocks': 3,
    }


class AssignmentLedgerTests(unittest.TestCase):
    def test_incomplete_persisted_ledger_never_authorizes_retry(self):
        got = L.build_assignment_ledger([rec()], target_blocks=2, target_columns=10)
        self.assertEqual('INCOMPLETE_PERSISTED_ASSIGNMENT_LEDGER', got['coverage']['status'])
        self.assertFalse(got['coverage']['retry_allowed'])
        self.assertEqual(1, got['coverage']['persisted_blocks'])
        self.assertEqual(5, got['coverage']['persisted_columns'])
        self.assertRegex(got['ledger_sha256'], r'^[0-9a-f]{64}$')

    def test_complete_exact_ledger_authorizes_only_assignment_retry(self):
        got = L.build_assignment_ledger([rec(10,5,shard=1), rec(11,5,shard=2)], target_blocks=2, target_columns=10)
        self.assertEqual('COMPLETE_PERSISTED_ASSIGNMENT_LEDGER', got['coverage']['status'])
        self.assertTrue(got['coverage']['retry_allowed'])
        self.assertFalse(got['coverage']['rank_certified'])

    def test_duplicate_orbit_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, 'duplicate orbit_id'):
            L.build_assignment_ledger([rec(), rec()], target_blocks=2, target_columns=10)

    def test_missing_provenance_is_rejected(self):
        x = rec(); del x['source_tar_sha256']
        with self.assertRaisesRegex(RuntimeError, 'missing provenance'):
            L.build_assignment_ledger([x], target_blocks=2, target_columns=10)

    def test_hash_is_stable_and_sensitive_to_assignment(self):
        a = L.build_assignment_ledger([rec()], target_blocks=2, target_columns=10)
        b = L.build_assignment_ledger([copy.deepcopy(rec())], target_blocks=2, target_columns=10)
        c = L.build_assignment_ledger([rec(rep=[1,1,3,4,5,6,7,1,2,3])], target_blocks=2, target_columns=10)
        self.assertEqual(a['ledger_sha256'], b['ledger_sha256'])
        self.assertNotEqual(a['ledger_sha256'], c['ledger_sha256'])

    def test_full_record_count_with_wrong_column_total_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, 'complete block count but target column mismatch'):
            L.build_assignment_ledger([rec(10,4), rec(11,4,shard=2)], target_blocks=2, target_columns=10)


if __name__ == '__main__':
    unittest.main()
