#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

import run_depth6_32_orbit_chunk as R


class FakeKeymeta:
    calls=[]

    @classmethod
    def compute_and_persist_block(cls, rec, *args, keymeta_path, raw_path, tol):
        cls.calls.append(int(rec['orbit_id']))
        keymeta_path.write_bytes(b'x')
        return {'orbit_id':int(rec['orbit_id']), 'm':int(rec['m']), 'q_key_count':2, 'rows':3}


class OrbitChunkTests(unittest.TestCase):
    def setUp(self):
        FakeKeymeta.calls=[]
        self.records=[
            {'orbit_id':1,'m':2}, {'orbit_id':2,'m':3}, {'orbit_id':3,'m':5}
        ]

    def test_runs_only_explicit_ids_once(self):
        with tempfile.TemporaryDirectory() as d:
            out=R.run_chunk(
                self.records,[3,1],chunk=7,out_dir=Path(d),keymeta_backend=FakeKeymeta,
                selector_backend=object(),master_backend=object(),basis_backend=object())
            self.assertEqual(FakeKeymeta.calls,[1,3])
            self.assertEqual(out['completed_blocks'],2)
            self.assertEqual(out['completed_columns'],7)
            self.assertEqual(out['orbit_ids'],[1,3])
            self.assertTrue((Path(d)/'chunk-0007-manifest.json').exists())

    def test_unknown_id_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(RuntimeError):
                R.run_chunk(
                    self.records,[9],chunk=0,out_dir=Path(d),keymeta_backend=FakeKeymeta,
                    selector_backend=object(),master_backend=object(),basis_backend=object())

    def test_duplicate_requested_id_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(RuntimeError):
                R.run_chunk(
                    self.records,[1,1],chunk=0,out_dir=Path(d),keymeta_backend=FakeKeymeta,
                    selector_backend=object(),master_backend=object(),basis_backend=object())


if __name__=='__main__':
    unittest.main()
