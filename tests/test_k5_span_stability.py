"""Scale invariance and null-direction controls for finite K5 rank estimates."""
import sys,unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from k5_quantum_geometry_bridge import stable_span,cyclic_depth

class SpanStability(unittest.TestCase):
    def test_rescaling_preserves_independent_geometry_channels(self):
        e=np.eye(3,dtype=complex)
        q,res=stable_span([1e-48*e[0],1e48*e[1]],e[2])
        self.assertEqual(len(q),2)
        self.assertAlmostEqual(res,1.)
    def test_large_near_collinear_vectors_do_not_create_channel(self):
        e=np.eye(3,dtype=complex)
        q,res=stable_span([e[0],1e48*(e[0]+1e-14*e[1])],e[1])
        self.assertEqual(len(q),1)
        self.assertAlmostEqual(res,1.)
    def test_cyclic_residual_does_not_round_away_small_channel(self):
        target=np.array([1.,1e-8,0.],complex)
        _,rows=cyclic_depth([],np.array([1.,0.,0.],complex),target,maxdepth=1)
        self.assertGreater(rows[-1]['target_defect'],0.)
        self.assertAlmostEqual(rows[-1]['target_defect']/1e-16,1.)

    def test_zero_vectors_do_not_create_rank(self):
        q,res=stable_span([np.zeros(3),np.zeros(3)],np.array([1.,0.,0.]))
        self.assertEqual(len(q),0)
        self.assertAlmostEqual(res,1.)
if __name__=='__main__':unittest.main()
