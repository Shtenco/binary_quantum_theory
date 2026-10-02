#!/usr/bin/env python3
import unittest

import depth6_32_identity_rematerialization as R


def rec(oid: int, m: int, d: int, proxy: int | None = None) -> dict:
    return {
        'orbit_id': oid,
        'rep': [oid % 4 + 1] * 10,
        'm': m,
        'coord_dim': d,
        'proxy': int(proxy if proxy is not None else d * m),
    }


class IdentityRematerializationTests(unittest.TestCase):
    def test_full_identity_matches_persisted_and_historical_batches(self):
        records = [rec(0, 3, 4), rec(1, 2, 5), rec(2, 4, 2)]
        persisted = [dict(records[1], source_shard=0)]
        expected_batches = R.cost_balanced(records, 2)[1]
        observed = {
            str(i): {
                'assigned_blocks': len(batch),
                'assigned_columns': sum(x['m'] for x in batch),
                'proxy': expected_batches[i],
            }
            for i, batch in enumerate(R.cost_balanced(records, 2)[0])
        }
        got = R.validate_rematerialized_identity(
            records,
            persisted_records=persisted,
            historical_batches=observed,
            expected_shell_states=12,
            observed_shell_states=12,
            expected_s5_orbits=5,
            observed_s5_orbits=5,
            target_blocks=3,
            target_columns=9,
            nshards=2,
        )
        self.assertEqual('PASS_IDENTITY_REMATERIALIZATION_ONLY', got['status'])
        self.assertEqual(3, got['blocks'])
        self.assertEqual(9, got['columns'])
        self.assertEqual(1, got['persisted_identity_matches'])
        self.assertEqual(2, got['historical_batch_matches'])
        self.assertFalse(got['rank_certified'])
        self.assertFalse(got['actual_q_coverage_certified'])

    def test_persisted_identity_mismatch_fails_closed(self):
        records = [rec(0, 3, 4), rec(1, 2, 5)]
        persisted = [dict(rec(1, 99, 5), source_shard=0)]
        with self.assertRaisesRegex(RuntimeError, 'persisted identity mismatch'):
            R.validate_rematerialized_identity(
                records,
                persisted_records=persisted,
                historical_batches={},
                expected_shell_states=12,
                observed_shell_states=12,
                expected_s5_orbits=5,
                observed_s5_orbits=5,
                target_blocks=2,
                target_columns=5,
                nshards=2,
            )

    def test_historical_batch_mismatch_fails_closed(self):
        records = [rec(0, 3, 4), rec(1, 2, 5), rec(2, 4, 2)]
        observed = {'0': {'assigned_blocks': 999, 'assigned_columns': 999, 'proxy': 999.0}}
        with self.assertRaisesRegex(RuntimeError, 'historical batch mismatch'):
            R.validate_rematerialized_identity(
                records,
                persisted_records=[],
                historical_batches=observed,
                expected_shell_states=12,
                observed_shell_states=12,
                expected_s5_orbits=5,
                observed_s5_orbits=5,
                target_blocks=3,
                target_columns=9,
                nshards=2,
            )

    def test_count_match_is_not_enough_when_shell_or_orbit_count_differs(self):
        records = [rec(0, 3, 4), rec(1, 2, 5)]
        with self.assertRaisesRegex(RuntimeError, 'frozen shell/orbit count mismatch'):
            R.validate_rematerialized_identity(
                records,
                persisted_records=[],
                historical_batches={},
                expected_shell_states=12,
                observed_shell_states=11,
                expected_s5_orbits=5,
                observed_s5_orbits=5,
                target_blocks=2,
                target_columns=5,
                nshards=2,
            )


if __name__ == '__main__':
    unittest.main()
