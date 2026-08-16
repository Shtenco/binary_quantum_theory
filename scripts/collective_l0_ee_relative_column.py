#!/usr/bin/env python3
"""Exact relative depth-2 Euclidean columns on the 16-cell collective seed.

For one relative XOR mask r compute both operator orders directly:

  A_r = E_r E_0 |Omega>
  B_r = E_0 E_r |Omega>

using the production physical-sine PL Peter-Weyl engine and zero-aware volume.
No translation identity is substituted for B_r.  The worker also reports the
exact commutator C_r=B_r-A_r and its support/norm.

The 16 masks exhaust node0 against every node.  A separate collector may use
the already proved XOR structural automorphism to organize all translated
pairs, but this worker itself makes no amplitude covariance assumption.
"""
from __future__ import annotations
import argparse,json,math,traceback
from collections import Counter
from pathlib import Path
import numpy as np
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

JMAX2=5
TOL=1e-10

def add(dst,src,scale=1):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL:dst[k]=z
        elif k in dst:del dst[k]
def norm(s):return math.sqrt(sum(abs(a)**2 for a in s.values()))
def maxspin(s):return max((max(k[0]) for k in s),default=0)/2
def save(path,state,nedges,nverts):
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]));path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    if rows:
        spins=np.asarray([k[0] for k,_ in rows],np.int16);Ks=np.asarray([k[1] for k,_ in rows],np.int16);amp=np.asarray([a for _,a in rows],np.complex128)
    else:
        spins=np.zeros((0,nedges),np.int16);Ks=np.zeros((0,nverts),np.int16);amp=np.zeros((0,),np.complex128)
    np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)
def diag(state,seed):
    return {'support':len(state),'norm':norm(state),'max_spin':maxspin(state),
            'changed_edge_count_distribution':{str(k):v for k,v in sorted(Counter(sum(a!=b for a,b in zip(key[0],seed[0])) for key in state).items())},
            'sum_doubled_spin_parity_distribution':{str(k):v for k,v in sorted(Counter(sum(key[0])%2 for key in state).items())}}

def run(mask):
    ZVM.patch_and_clear();D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D);seed=((1,)*len(G.EDGES),(0,)*D.n_tets)
    E0=G.H_sine_basis(seed,0,JMAX2)
    Er=G.H_sine_basis(seed,mask,JMAX2)
    A=G.H_sine_state(E0,mask,JMAX2,TOL)
    B=G.H_sine_state(Er,0,JMAX2,TOL)
    C={};add(C,B,+1);add(C,A,-1)
    finite=all(np.isfinite([z.real,z.imag]).all() for st in (A,B,C) for z in st.values())
    seedpar=sum(seed[0])%2;wrong=sum(1 for st in (A,B,C) for key in st if sum(key[0])%2!=seedpar)
    checks={'first_E_columns_nonzero':len(E0)>0 and len(Er)>0,
            'finite_depth2_amplitudes':finite,
            'depth2_spin_wall_j_le_5_over_2':max(maxspin(A),maxspin(B),maxspin(C))<=2.5+1e-12,
            'even_valence_parity_preserved':wrong==0,
            'self_commutator_zero_when_mask0':(norm(C)<1e-10) if mask==0 else True}
    return A,B,C,{'status':'exact 16-cell relative Euclidean depth-2 columns','passed':bool(all(checks.values())),'science_status':'E_DEPTH2_PRECURSOR',
                  'relative_mask':mask,'source_nodes':[0,mask],'Jmax':JMAX2/2,'checks':checks,
                  'E0_support':len(E0),'Er_support':len(Er),'A_Er_E0':diag(A,seed),'B_E0_Er':diag(B,seed),'commutator_B_minus_A':diag(C,seed),
                  'wrong_seed_parity_outputs':wrong,
                  'interpretation':'Both operator orders are computed directly on the same exact PL Peter-Weyl habitat. The commutator is an amplitude result, not an XOR-inferred quantity.',
                  'scope_note':'Euclidean E-depth2 only. No Lorentzian S, route or diffeomorphism target is used here.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--mask',type=int,choices=range(16),required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True)
    try:A,B,C,o=run(a.mask);code=0 if o['passed'] else 1
    except Exception as exc:A=B=C={};o={'status':'worker exception','passed':False,'relative_mask':a.mask,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    D=DualComplex(seed_16cell_boundary());save(a.out_dir/f'A_{a.mask}.npz',A,len(D.dual_edges()),D.n_tets);save(a.out_dir/f'B_{a.mask}.npz',B,len(D.dual_edges()),D.n_tets);save(a.out_dir/f'C_{a.mask}.npz',C,len(D.dual_edges()),D.n_tets);(a.out_dir/f'mask_{a.mask}.json').write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(json.dumps(o,indent=2,sort_keys=True));return code
if __name__=='__main__':raise SystemExit(main())
