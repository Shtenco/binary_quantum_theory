#!/usr/bin/env python3
import json
import tempfile
import unittest
from pathlib import Path

import depth6_32_replay_authorization as A
import test_verify_depth6_32_recovery_frontier as T
import verify_depth6_32_recovery_frontier as V


def add_schema8(root: Path, r: dict) -> None:
    T.add_schema7(root,r)
    ledger=json.loads((root/'BQG_DEPTH6_32_REMATERIALIZED_ASSIGNMENT_LEDGER_2026-10-02.json').read_text())
    gate=json.loads((root/'BQG_DEPTH6_32_IDENTITY_REMATERIALIZATION_GATE_2026-10-02.json').read_text())
    # Upgrade the schema-7 fixture to the exact provenance now required by the
    # replay authorization layer.
    ledger['source_stage_a_run_id']=A.SOURCE_STAGE_A_RUN_ID
    ledger['frozen_engine_commit']=A.FROZEN_ENGINE_COMMIT
    ledger['frozen_bundle_blob_sha']=A.FROZEN_ENGINE_BLOB_SHA
    for rec in ledger['records']:
        rec['identity_source']=A.IDENTITY_SOURCE
        rec['frozen_engine_commit']=A.FROZEN_ENGINE_COMMIT
        rec['frozen_bundle_blob_sha']=A.FROZEN_ENGINE_BLOB_SHA
        rec['source_stage_a_run_id']=A.SOURCE_STAGE_A_RUN_ID
    import hashlib
    ledger['identity_sha256']=hashlib.sha256(json.dumps(ledger['records'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
    (root/'BQG_DEPTH6_32_REMATERIALIZED_ASSIGNMENT_LEDGER_2026-10-02.json').write_text(json.dumps(ledger))
    r['rematerialized_assignment_ledger']['identity_sha256']=ledger['identity_sha256']
    auth=A.authorize_replay(ledger,gate)
    auth_path=root/'BQG_DEPTH6_32_REPLAY_AUTHORIZATION_2026-10-03.json'
    auth_path.write_text(json.dumps(auth))
    for rel in ('depth6_32_replay_authorization.py','run_depth6_32_ledger_batch.py','depth6_32_frozen_m_basis.py','depth6_32_keymeta_first.py'):
        (root/'scripts'/rel).write_text('# canonical\n')
    (root/'.github'/'workflows').mkdir(parents=True)
    (root/'.github'/'workflows'/'bqg-depth6-32-ledger-keymeta-first.yml').write_text('# canonical\n')
    r['schema_version']=8
    r['replay_authorization']={
        'path':auth_path.name,
        'status':'AUTHORIZED_NUMERICAL_REPLAY_ATTEMPT',
        'blocks':2755,
        'columns':130903,
        'nshards':112,
        'identity_sha256':ledger['identity_sha256'],
        'frozen_engine_commit':A.FROZEN_ENGINE_COMMIT,
        'frozen_bundle_blob_sha':A.FROZEN_ENGINE_BLOB_SHA,
        'frozen_basis_contract':A.FROZEN_BASIS_CONTRACT,
        'keymeta_first_contract':A.KEYMETA_CONTRACT,
        'canonical_numerical_compute_allowed':True,
        'actual_q_coverage_certified':False,
        'rank_certified':False,
        'numerical_closure_claimed':False,
    }
    r['rules']['authorized_replay_attempt_is_not_rank_evidence']=True
    r['rules']['full_keymeta_coverage_required_before_global_peeling']=True


class Schema8FrontierTests(unittest.TestCase):
    def test_schema8_authorizes_replay_but_not_peeling_or_rank(self):
        r=T.recovery()
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); T.setup_root(root); add_schema8(root,r)
            got=V.verify(r,T.depth6(),root)
            self.assertEqual('PASS_CANONICAL_RECOVERY_FRONTIER_REPLAY_AUTHORIZED',got['status'])
            self.assertTrue(got['replay_compute_allowed'])
            self.assertTrue(got['authorized_numerical_replay_attempt'])
            self.assertFalse(got['schedule_allowed'])
            self.assertFalse(got['numerical_closure_claimed'])

    def test_schema8_tampered_authorization_certificate_fails_closed(self):
        r=T.recovery()
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); T.setup_root(root); add_schema8(root,r)
            p=root/'BQG_DEPTH6_32_REPLAY_AUTHORIZATION_2026-10-03.json'
            auth=json.loads(p.read_text()); auth['columns']=130902; p.write_text(json.dumps(auth))
            with self.assertRaisesRegex(RuntimeError,'replay authorization'):
                V.verify(r,T.depth6(),root)


if __name__=='__main__': unittest.main()
