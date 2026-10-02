#!/usr/bin/env python3
import unittest

import depth6_replay_readiness as R


def record(orbit=1, evidence=None):
    x = {'orbit_id': orbit, 'm': 10, 'rep': [1,2,3,4,3,2,3,4,3,2]}
    if evidence is not None:
        x['replay_evidence'] = evidence
    return x


class ReplayReadinessTests(unittest.TestCase):
    def test_assignment_identity_alone_is_not_replay_ready(self):
        got = R.assess_records([record()])
        self.assertEqual(0, got['replay_ready_blocks'])
        self.assertEqual([1], got['missing_selector_or_map_blocks'])
        self.assertFalse(got['canonical_compute_allowed'])

    def test_persisted_master_map_is_replay_ready_without_selector(self):
        ev = {
            'kind': 'PERSISTED_MASTER_MAP',
            'sha256': 'a'*64,
            'immutable_locator': 'artifact:123/digest:sha256:abc',
        }
        got = R.assess_records([record(evidence=ev)])
        self.assertEqual(1, got['replay_ready_blocks'])
        self.assertEqual([], got['missing_selector_or_map_blocks'])

    def test_persisted_selector_witness_is_replay_ready(self):
        ev = {
            'kind': 'PERSISTED_SELECTOR_WITNESS',
            'sha256': 'b'*64,
            'immutable_locator': 'git:deadbeef/path/to/selector.npz',
        }
        got = R.assess_records([record(evidence=ev)])
        self.assertEqual(1, got['replay_ready_blocks'])

    def test_source_artifact_metadata_alone_is_not_enough(self):
        x = record()
        x['source_raw_artifact_id'] = '123'
        x['source_raw_artifact_digest'] = 'sha256:'+'c'*64
        got = R.assess_records([x])
        self.assertEqual([1], got['missing_selector_or_map_blocks'])

    def test_malformed_replay_evidence_fails_closed(self):
        ev = {'kind': 'PERSISTED_MASTER_MAP', 'sha256': 'short', 'immutable_locator': 'x'}
        with self.assertRaisesRegex(RuntimeError, 'invalid replay evidence'):
            R.assess_records([record(evidence=ev)])


if __name__ == '__main__':
    unittest.main()
