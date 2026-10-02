#!/usr/bin/env python3
import unittest

import depth6_keymeta_coverage as C


def payload(shard: int, orbit: int, m: int = 10, *, shards: int = 2,
            engine: str = 'engine-a', irrep: str = '32') -> dict:
    return {
        'kind': 'BQG_MIXED_MASTER_KEY_METADATA',
        'schema_version': 1,
        'irrep': irrep,
        'shard': shard,
        'shards': shards,
        'engine_git_blob_sha': engine,
        'blocks': {
            str(orbit): {
                'm': m,
                'q_rows': {'q0': m},
            }
        },
    }


class CoverageTests(unittest.TestCase):
    def test_partial_coverage_never_allows_global_schedule(self):
        got = C.validate_keymeta_coverage(
            [payload(0, 100)],
            irrep='32', expected_shards=2,
            target_blocks=2, target_columns=20,
        )
        self.assertEqual('INCOMPLETE_KEYMETA_COVERAGE', got['status'])
        self.assertEqual([1], got['missing_shards'])
        self.assertEqual(1, got['recovered_blocks'])
        self.assertEqual(10, got['recovered_columns'])
        self.assertFalse(got['schedule_allowed'])
        self.assertEqual('COVERAGE_GATE_ONLY_NOT_A_RANK_CERTIFICATE', got['proof_status'])

    def test_duplicate_shard_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, 'duplicate shard'):
            C.validate_keymeta_coverage(
                [payload(0, 100), payload(0, 101)],
                irrep='32', expected_shards=2,
                target_blocks=2, target_columns=20,
            )

    def test_duplicate_orbit_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, 'duplicate orbit block'):
            C.validate_keymeta_coverage(
                [payload(0, 100), payload(1, 100)],
                irrep='32', expected_shards=2,
                target_blocks=2, target_columns=20,
            )

    def test_mixed_engine_hashes_fail_closed(self):
        with self.assertRaisesRegex(RuntimeError, 'multiple proof-engine blobs'):
            C.validate_keymeta_coverage(
                [payload(0, 100, engine='engine-a'), payload(1, 101, engine='engine-b')],
                irrep='32', expected_shards=2,
                target_blocks=2, target_columns=20,
            )

    def test_complete_shard_ids_with_wrong_totals_fail_closed(self):
        with self.assertRaisesRegex(RuntimeError, 'full shard coverage but target mismatch'):
            C.validate_keymeta_coverage(
                [payload(0, 100), payload(1, 101)],
                irrep='32', expected_shards=2,
                target_blocks=2, target_columns=21,
            )

    def test_full_exact_coverage_allows_schedule_but_is_not_rank_certificate(self):
        got = C.validate_keymeta_coverage(
            [payload(0, 100), payload(1, 101)],
            irrep='32', expected_shards=2,
            target_blocks=2, target_columns=20,
        )
        self.assertEqual('FULL_KEYMETA_COVERAGE', got['status'])
        self.assertTrue(got['schedule_allowed'])
        self.assertEqual([], got['missing_shards'])
        self.assertEqual('COVERAGE_GATE_ONLY_NOT_A_RANK_CERTIFICATE', got['proof_status'])


if __name__ == '__main__':
    unittest.main()
