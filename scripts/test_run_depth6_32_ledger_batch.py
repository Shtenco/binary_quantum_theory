#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

import run_depth6_32_ledger_batch as R


class FakeKM:
    calls=[]
    @staticmethod
    def compute_and_persist_block(record, selector_backend, master_backend, basis_backend, *, keymeta_path, raw_path=None, tol=1e-8):
        FakeKM.calls.append(int(record['orbit_id']))
        p=Path(keymeta_path); p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b'km')
        return {'orbit_id':int(record['orbit_id']),'m':int(record['m']),'q_key_count':2,'rows':8,'rank_certified':False,'numerical_closure_claimed':False}


class BatchTests(unittest.TestCase):
    def setUp(self): FakeKM.calls=[]

    def test_requested_shard_only(self):
        records=[
            {'orbit_id':1,'rep':[0]*10,'m':2,'coord_dim':8,'source_shard':3},
            {'orbit_id':2,'rep':[0]*10,'m':5,'coord_dim':20,'source_shard':4},
            {'orbit_id':3,'rep':[0]*10,'m':7,'coord_dim':28,'source_shard':3},
        ]
        with tempfile.TemporaryDirectory() as td:
            got=R.run_batch(records,shard=3,nshards=112,out_dir=Path(td),keymeta_backend=FakeKM,selector_backend=object(),master_backend=object(),basis_backend=object())
        self.assertEqual([1,3],FakeKM.calls)
        self.assertEqual(2,got['completed_blocks'])
        self.assertEqual(9,got['completed_columns'])
        self.assertFalse(got['rank_certified'])
        self.assertFalse(got['numerical_closure_claimed'])

    def test_duplicate_orbit_fails(self):
        records=[{'orbit_id':1,'rep':[0]*10,'m':2,'coord_dim':8,'source_shard':3}]*2
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaisesRegex(RuntimeError,'duplicate orbit'):
                R.run_batch(records,shard=3,nshards=112,out_dir=Path(td),keymeta_backend=FakeKM,selector_backend=object(),master_backend=object(),basis_backend=object())

    def test_empty_shard_fails(self):
        records=[{'orbit_id':1,'rep':[0]*10,'m':2,'coord_dim':8,'source_shard':3}]
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaisesRegex(RuntimeError,'no records'):
                R.run_batch(records,shard=9,nshards=112,out_dir=Path(td),keymeta_backend=FakeKM,selector_backend=object(),master_backend=object(),basis_backend=object())


if __name__=='__main__': unittest.main()
