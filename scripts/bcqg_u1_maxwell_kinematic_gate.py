#!/usr/bin/env python3
"""Exact U(1) Maxwell kinematic gate on the BCQG 16-cell S3 carrier."""
from __future__ import annotations
import argparse,json,itertools
from pathlib import Path
import sympy as sp

def seed_16cell_boundary():return sorted(tuple(2*i+b for i,b in enumerate(bits)) for bits in itertools.product((0,1),repeat=4))
def run():
    tets=seed_16cell_boundary();verts=sorted(set().union(*(set(t) for t in tets)));edges=sorted(set(e for t in tets for e in itertools.combinations(sorted(t),2)));tris=sorted(set(f for t in tets for f in itertools.combinations(sorted(t),3)))
    vi={v:i for i,v in enumerate(verts)};ei={e:i for i,e in enumerate(edges)};d0=sp.zeros(len(edges),len(verts));d1=sp.zeros(len(tris),len(edges))
    for r,(a,b) in enumerate(edges):d0[r,vi[a]]=-1;d0[r,vi[b]]=1
    for r,(a,b,c) in enumerate(tris):d1[r,ei[(b,c)]]=1;d1[r,ei[(a,c)]]=-1;d1[r,ei[(a,b)]]=1
    H2=sp.diag(*[sp.Rational(i+1,17) for i in range(len(tris))]);K=sp.simplify(d1.T*H2*d1)
    A=sp.Matrix([((7*i+3)%11)-5 for i in range(len(edges))]);lam=sp.Matrix([((5*i+2)%7)-3 for i in range(len(verts))]);F=d1*A;Fp=d1*(A+d0*lam);S=sp.simplify((F.T*H2*F)[0]/2);Sp=sp.simplify((Fp.T*H2*Fp)[0]/2)
    checks={'f_vector_seed':(len(verts),len(edges),len(tris),len(tets))==(8,24,32,16),'d1_d0_exact_zero':d1*d0==sp.zeros(len(tris),len(verts)),'gauge_curvature_exact':Fp==F,'gauge_action_exact':sp.simplify(Sp-S)==0,'rank_d0_Vminus1':d0.rank()==7,'rank_d1_17':d1.rank()==17,'weighted_Maxwell_rank_17':K.rank()==17,'Maxwell_kernel_equals_gradient_dim':len(edges)-K.rank()==d0.rank(),'gradient_annihilated_by_K':K*d0==sp.zeros(len(edges),len(verts))}
    return {'status':'exact U(1) Maxwell kinematic gate on BCQG 16-cell S3','passed':all(checks.values()),'science_status':'MATTER_KINEMATIC_PRECURSOR','counts':{'V':len(verts),'E':len(edges),'F':len(tris),'T':len(tets)},'rank_d0':d0.rank(),'rank_d1':d1.rank(),'rank_weighted_Maxwell':K.rank(),'Maxwell_nullity':len(edges)-K.rank(),'sample_action':str(S),'gauge_shift_action_change':str(sp.simplify(Sp-S)),'checks':checks,'identity':'F=d1 A; A->A+d0 lambda; d1 d0=0; S=1/2 F^T *_2 F; K=d1^T *_2 d1','interpretation':'The BCQG simplicial carrier supports an exact gauge-invariant U(1) curvature/action for arbitrary positive nonuniform face Hodge weights. Metric dependence can therefore enter through the Hodge star without breaking U(1) gauge invariance.','scope_note':'Spatial/kinematic Maxwell precursor only. A physical photon requires Lorentzian history dynamics, electric sector/Gauss law, a BCQG-derived metric Hodge star, and normalization.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())