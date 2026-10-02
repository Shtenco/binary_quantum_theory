#!/usr/bin/env python3
import unittest
import numpy as np

import depth6_32_keymeta_first as K


class FakeBasis:
    @staticmethod
    def build_frozen_m_basis(rep,key,m,d,backend,tol=1e-8):
        return np.eye(d,m,dtype=complex), {'status':'PASS_FROZEN_M_NUMERICAL_BASIS_ONLY','max_residual':1e-14,'multiplicity_recomputed':False}


class FakeMaster:
    @staticmethod
    def master_map(rep,key,W):
        m=W.shape[1]
        return {('v0',(1,2)):np.ones((3,m),complex),('v2',(3,4)):np.ones((5,m),complex)},W


class KeymetaFirstTests(unittest.TestCase):
    def test_builds_exact_per_orbit_keymeta_without_rank_claim(self):
        r={'orbit_id':351,'rep':[0,0,0,0,0,0,0,2,2,2],'m':1,'coord_dim':4,'proxy':4}
        got=K.compute_block_keymeta(r,object(),FakeMaster,FakeBasis)
        self.assertEqual('BQG_DEPTH6_32_KEYMETA_FIRST_BLOCK',got['kind'])
        self.assertEqual(351,got['orbit_id'])
        self.assertEqual(1,got['m'])
        self.assertEqual({('v0',(1,2)):3,('v2',(3,4)):5},got['q_rows'])
        self.assertEqual(2,got['q_key_count'])
        self.assertEqual(8,got['rows'])
        self.assertFalse(got['rank_certified'])
        self.assertFalse(got['global_uniqueness_certified'])
        self.assertFalse(got['numerical_closure_claimed'])

    def test_bad_master_column_shape_fails_closed(self):
        class BadMaster:
            @staticmethod
            def master_map(rep,key,W):
                return {('q',):np.ones((2,2),complex)},W
        r={'orbit_id':1,'rep':[0]*10,'m':1,'coord_dim':4,'proxy':4}
        with self.assertRaisesRegex(RuntimeError,'bad master-map shape'):
            K.compute_block_keymeta(r,object(),BadMaster,FakeBasis)

    def test_duplicate_orbit_union_fails_closed(self):
        a={'orbit_id':1,'m':2,'q_rows':{('q',):3}}
        with self.assertRaisesRegex(RuntimeError,'duplicate orbit'):
            K.validate_keymeta_union([a,a],target_blocks=2,target_columns=4)

    def test_partial_union_never_allows_global_peeling(self):
        a={'orbit_id':1,'m':2,'q_rows':{('q',):3}}
        got=K.validate_keymeta_union([a],target_blocks=2,target_columns=4)
        self.assertEqual(1,got['blocks'])
        self.assertEqual(2,got['columns'])
        self.assertFalse(got['global_peeling_allowed'])


if __name__=='__main__': unittest.main()
