#!/usr/bin/env python3
import hashlib
import json
import unittest

import depth6_32_replay_authorization as A


def complete_fixture():
    records=[]
    for i in range(2755):
        m=47 if i<2754 else 1465
        records.append({
            'orbit_id':i,
            'rep':[1]*10,
            'm':m,
            'coord_dim':4*m,
            'proxy':4*m*m,
            'source_shard':i%112,
            'identity_source':'DETERMINISTIC_REMATERIALIZATION_FROM_FROZEN_STAGE_A_ENGINE',
            'frozen_engine_commit':A.FROZEN_ENGINE_COMMIT,
            'frozen_bundle_blob_sha':A.FROZEN_ENGINE_BLOB_SHA,
            'source_stage_a_run_id':A.SOURCE_STAGE_A_RUN_ID,
        })
    identity_sha=hashlib.sha256(
        json.dumps(records,sort_keys=True,separators=(',',':')).encode()
    ).hexdigest()
    ledger={
        'schema_version':1,
        'kind':'BQG_DEPTH6_32_REMATERIALIZED_ASSIGNMENT_LEDGER',
        'status':'COMPLETE_IDENTITY_REMATERIALIZATION_ONLY',
        'target_blocks':2755,
        'target_columns':130903,
        'source_stage_a_run_id':A.SOURCE_STAGE_A_RUN_ID,
        'frozen_engine_commit':A.FROZEN_ENGINE_COMMIT,
        'frozen_bundle_blob_sha':A.FROZEN_ENGINE_BLOB_SHA,
        'records':records,
        'identity_sha256':identity_sha,
        'rank_certified':False,
        'actual_q_coverage_certified':False,
        'numerical_closure_claimed':False,
    }
    gate={
        'schema_version':1,
        'kind':'BQG_DEPTH6_32_IDENTITY_REMATERIALIZATION_GATE',
        'status':'PASS_IDENTITY_REMATERIALIZATION_ONLY',
        'blocks':2755,
        'columns':130903,
        'identity_sha256':identity_sha,
        'persisted_identity_matches':15,
        'historical_batch_matches':102,
        'rank_certified':False,
        'actual_q_coverage_certified':False,
        'numerical_closure_claimed':False,
    }
    return ledger,gate


class ReplayAuthorizationTests(unittest.TestCase):
    def test_complete_frozen_identity_authorizes_attempt_without_rank_claim(self):
        ledger,gate=complete_fixture()
        got=A.authorize_replay(ledger,gate)
        self.assertEqual('AUTHORIZED_NUMERICAL_REPLAY_ATTEMPT',got['status'])
        self.assertTrue(got['numerical_replay_authorized'])
        self.assertEqual(2755,got['blocks'])
        self.assertEqual(130903,got['columns'])
        self.assertEqual(112,got['covered_shards'])
        self.assertFalse(got['rank_certified'])
        self.assertFalse(got['actual_q_coverage_certified'])
        self.assertFalse(got['numerical_closure_claimed'])

    def test_record_engine_blob_drift_fails_closed(self):
        ledger,gate=complete_fixture()
        ledger['records'][100]['frozen_bundle_blob_sha']='0'*40
        with self.assertRaisesRegex(RuntimeError,'frozen bundle blob'):
            A.authorize_replay(ledger,gate)

    def test_missing_shard_coverage_fails_closed(self):
        ledger,gate=complete_fixture()
        for r in ledger['records']:
            if r['source_shard']==111:
                r['source_shard']=110
        ledger['identity_sha256']=hashlib.sha256(
            json.dumps(ledger['records'],sort_keys=True,separators=(',',':')).encode()
        ).hexdigest()
        gate['identity_sha256']=ledger['identity_sha256']
        with self.assertRaisesRegex(RuntimeError,'112-shard'):
            A.authorize_replay(ledger,gate)

    def test_identity_gate_must_not_claim_rank(self):
        ledger,gate=complete_fixture()
        gate['rank_certified']=True
        with self.assertRaisesRegex(RuntimeError,'rank'):
            A.authorize_replay(ledger,gate)


if __name__=='__main__':
    unittest.main()
