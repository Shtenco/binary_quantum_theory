#!/usr/bin/env python3
import unittest

import inventory_depth6_32_stagea_jobs as I


class StageALogInventoryTests(unittest.TestCase):
    def test_parse_successful_numerical_then_pack_lost(self):
        log = '''
SHELL 6 264962
LEDGER 32 2755 130903 SHARD 5 N 1 COLS 720 PROXY 2073600.0
PREWARM 55 331 sec 2.3
DONE 1 / 1 ok 1 sec 7078.4
##[error]The operation was canceled.
'''
        got = I.parse_worker_log(log, expected_shard=5)
        self.assertEqual(1, got['assigned_blocks'])
        self.assertEqual(720, got['assigned_columns'])
        self.assertTrue(got['numerical_complete'])
        self.assertEqual(1, got['done_blocks'])
        self.assertEqual(1, got['ok_blocks'])

    def test_partial_done_is_not_complete(self):
        log = '''
LEDGER 32 2755 130903 SHARD 9 N 12 COLS 401 PROXY 1234.5
DONE 5 / 12 ok 5 sec 3000.0
DONE 10 / 12 ok 10 sec 6000.0
'''
        got = I.parse_worker_log(log, expected_shard=9)
        self.assertFalse(got['numerical_complete'])
        self.assertEqual(10, got['done_blocks'])
        self.assertEqual(10, got['ok_blocks'])

    def test_wrong_shard_in_log_fails_closed(self):
        log = 'LEDGER 32 2755 130903 SHARD 4 N 1 COLS 10 PROXY 1.0\n'
        with self.assertRaisesRegex(RuntimeError, 'shard mismatch'):
            I.parse_worker_log(log, expected_shard=5)

    def test_classification_prefers_persisted_artifact(self):
        parsed = {'assigned_blocks': 1, 'assigned_columns': 720, 'numerical_complete': True, 'done_blocks': 1, 'ok_blocks': 1}
        self.assertEqual('RAW_PERSISTED', I.classify(parsed, artifact_present=True))
        self.assertEqual('NUMERICAL_COMPLETE_BUT_ARTIFACT_LOST', I.classify(parsed, artifact_present=False))

    def test_partial_and_not_started_classification(self):
        partial = {'assigned_blocks': 12, 'assigned_columns': 401, 'numerical_complete': False, 'done_blocks': 5, 'ok_blocks': 5}
        none = {'assigned_blocks': 12, 'assigned_columns': 401, 'numerical_complete': False, 'done_blocks': 0, 'ok_blocks': 0}
        self.assertEqual('PARTIAL_NUMERICAL', I.classify(partial, artifact_present=False))
        self.assertEqual('NOT_COMPLETED', I.classify(none, artifact_present=False))


if __name__ == '__main__':
    unittest.main()
