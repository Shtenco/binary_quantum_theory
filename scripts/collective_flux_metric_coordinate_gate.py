#!/usr/bin/env python3
"""Exact regular-tetrahedron face-flux Gram -> metric linearization."""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import sympy as sp

def run():
    normals=[sp.Matrix(v)/sp.sqrt(3) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]];pairs=list(itertools.combinations(range(4),2));Bs=[sp.diag(1,0,0),sp.diag(0,1,0),sp.diag(0,0,1)]
    M=sp.zeros(3);M[0,1]=M[1,0]=1/sp.sqrt(2);Bs.append(M);M=sp.zeros(3);M[0,2]=M[2,0]=1/sp.sqrt(2);Bs.append(M);M=sp.zeros(3);M[1,2]=M[2,1]=1/sp.sqrt(2);Bs.append(M)
    rows=[]
    for f,g in pairs:
        nf,ng=normals[f],normals[g];q0=sp.simplify(nf.dot(ng));rows.append([sp.simplify(q0*sp.trace(B)-(nf.T*B*ng)[0]) for B in Bs])
    JF=sp.Matrix(rows);t=sp.Matrix([1,1,1,0,0,0])/sp.sqrt(3)
    checks={'regular_face_normal_pair_dot_minus_third':all(sp.simplify(normals[f].dot(normals[g])+sp.Rational(1,3))==0 for f,g in pairs),'flux_metric_rank_6':JF.rank()==6,'flux_metric_det_exact':sp.simplify(JF.det()-128*sp.sqrt(2)/729)==0,'uniform_trace_flux_response':len(set(map(str,sp.simplify(JF*t))))==1}
    return {'status':'exact face-flux Gram coordinates for regular tetrahedral metric','passed':all(checks.values()),'science_status':'COLLECTIVE_METRIC_COORDINATE_THEOREM','face_pair_order':[list(x) for x in pairs],'metric_basis':['xx','yy','zz','sqrt2_xy','sqrt2_xz','sqrt2_yz'],'J_flux':[[str(sp.simplify(x)) for x in row] for row in JF.tolist()],'det_J_flux':str(sp.factor(JF.det())),'rank_J_flux':JF.rank(),'J_flux_Gram_eigenvalues':{str(sp.simplify(k)):int(v) for k,v in (JF.T*JF).eigenvals().items()},'trace_response':[str(sp.simplify(x)) for x in JF*t],'checks':checks,'derivation':'For fixed coordinate face covectors n_f and metric g, densitized face fluxes obey X_f ~ sqrt(det g) g^{-1} n_f, so Z_fg ~ det(g) n_f^T g^{-1} n_g and delta Z_fg=(n_f.n_g)tr(h)-n_f^T h n_g at g=I.','interpretation':'The six pairwise coarse-face flux Gram observables are an invertible linear coordinate system on Sym^2(R^3), providing a BCQG-native metric calibration route without a separate edge-length operator.','scope_note':'Classical linearization of the coarse observable. Its quantum response B_F must be measured on the coherent/refinement BCQG background.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())