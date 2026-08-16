#!/usr/bin/env python3
"""Exact structural bridge from the BCQG six-edge metric carrier to photon interferometry.

No physical scale or GR target is inserted. The gate uses only the regular
coarse tetrahedron, the exact six-edge -> Sym^2(R^3) linearization, and
balanced differential optical phases.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sympy as sp

def run():
    V=[sp.Matrix([1,1,1]),sp.Matrix([1,-1,-1]),sp.Matrix([-1,1,-1]),sp.Matrix([-1,-1,1])]
    labels=[];ns=[]
    for i in range(4):
        for j in range(i+1,4):
            x=V[j]-V[i]; n=sp.simplify(x/sp.sqrt(x.dot(x)))
            labels.append((i,j));ns.append(n)
    J=sp.Matrix([[n[0]**2,n[1]**2,n[2]**2,sp.sqrt(2)*n[0]*n[1],sp.sqrt(2)*n[0]*n[2],sp.sqrt(2)*n[1]*n[2]] for n in ns])
    J=sp.simplify(J)
    one=sp.ones(6,1)
    D=sp.zeros(5,6)
    for i in range(5):D[i,i]=1;D[i,5]=-1
    R=sp.simplify(D*J)
    t=sp.Matrix([1,1,1,0,0,0])/sp.sqrt(3)
    T=sp.Matrix.hstack(
      sp.Matrix([1,-1,0,0,0,0])/sp.sqrt(2),
      sp.Matrix([1,1,-2,0,0,0])/sp.sqrt(6),
      sp.Matrix([0,0,0,1,0,0]),sp.Matrix([0,0,0,0,1,0]),sp.Matrix([0,0,0,0,0,1]))
    RT=sp.simplify(R*T);gram=sp.simplify(RT.T*RT)
    checks={
      'edge_metric_map_rank_6':J.rank()==6,
      'edge_metric_map_exact_det':sp.simplify(J.det()+sp.sqrt(2)/2)==0,
      'tetrahedral_isotropy_sum_nnT_2I':sp.simplify(sum((n*n.T for n in ns),sp.zeros(3,3))-2*sp.eye(3))==sp.zeros(3,3),
      'five_balanced_phase_channels':D.rank()==5,
      'balanced_common_mode_null':D*one==sp.zeros(5,1),
      'trace_mode_null':R*t==sp.zeros(5,1),
      'traceless_response_rank_5':RT.rank()==5,
      'traceless_response_exact_det':sp.simplify(RT.det()-sp.sqrt(6)/2)==0}
    return {
      'status':'exact BCQG metric-to-photon-interference structural bridge','passed':bool(all(checks.values())),
      'science_status':'STRUCTURAL_OPTICAL_BRIDGE','edge_order':[list(e) for e in labels],
      'metric_basis':['xx','yy','zz','sqrt2_xy','sqrt2_xz','sqrt2_yz'],
      'edge_to_metric_response_J':[[str(sp.simplify(x)) for x in row] for row in J.tolist()],
      'det_J':str(sp.factor(J.det())),'rank_J':J.rank(),'balanced_difference_rank':D.rank(),
      'balanced_difference_common_mode':[str(x) for x in D*one],'rank_DJ':R.rank(),
      'trace_response':[str(sp.simplify(x)) for x in R*t],
      'traceless_response_det':str(sp.factor(RT.det())),'traceless_response_rank':RT.rank(),
      'traceless_response_gram_eigenvalues':{str(sp.simplify(k)):int(v) for k,v in gram.eigenvals().items()},
      'checks':checks,
      'phase_map':'For y=J h with y_e=delta(ell_e^2)/ell_star^2, delta_phi=(k ell_star/2)y. Five balanced channels give Delta_phi=(k ell_star/2) D J h.',
      'single_photon_map':'For (|gamma1>+|gamma2>)/sqrt(2), geometry enters the relative optical phase. Ideal outputs are P_+/-=(1+/-cos Delta_phi)/2; quantum-geometry visibility needs a separate coupled-state calculation.',
      'interpretation':'Balanced equal-arm edge interferometry removes the common six-edge mode exactly. Under the exact six-edge/Sym^2 isomorphism this is the trace mode, while the five differential channels are injective on the full traceless metric tangent space.',
      'scope_note':'Structural linear response only. Absolute radians require ell_star and collective-to-physical metric normalization. Visibility loss requires explicit Maxwell/photon coupling and a geometry state.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())