#!/usr/bin/env python3
import unittest
import numpy as np

import depth6_32_frozen_m_basis as B
import bqg_depth6_generic_jucys_selector as J


class FrozenMBasisTests(unittest.TestCase):
    def test_real_small_orbit_uses_frozen_m_without_exact_mult(self):
        rep=(0,0,0,0,0,0,0,2,2,2)
        frozen_m=1
        frozen_coord_dim=4
        old=J.exact_mult
        def forbidden(*args,**kwargs):
            raise AssertionError('exact_mult must not be called by frozen-m basis construction')
        J.exact_mult=forbidden
        try:
            Q,cert=B.build_frozen_m_basis(rep,'32',frozen_m,frozen_coord_dim,J,tol=1e-8)
        finally:
            J.exact_mult=old
        self.assertEqual((4,1),Q.shape)
        self.assertEqual('PASS_FROZEN_M_NUMERICAL_BASIS_ONLY',cert['status'])
        self.assertFalse(cert['multiplicity_recomputed'])
        self.assertFalse(cert['structural_closure_claimed'])
        self.assertLessEqual(cert['max_residual'],1e-8)

    def test_frozen_coord_dim_mismatch_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError,'coord_dim mismatch'):
            B.build_frozen_m_basis((0,0,0,0,0,0,0,2,2,2),'32',1,999,J,tol=1e-8)

    def test_nonpositive_frozen_m_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError,'frozen m must be positive'):
            B.build_frozen_m_basis((0,0,0,0,0,0,0,2,2,2),'32',0,4,J,tol=1e-8)


if __name__=='__main__': unittest.main()
