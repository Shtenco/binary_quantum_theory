#!/usr/bin/env python3
"""Exact matrix-covariant C_e(V) on the independent 16-cell PL-S3 habitat.

This reuses the already validated charged/covariant local representation algebra
through `PLCompat`; it does not yet promote the full K-K-V Lorentzian operator.
The gate checks the exact two-hit identity, charged-volume leakage, J content and
nonzero C(V) on a genuine 16-cell dual edge.
"""
from __future__ import annotations
import argparse,json,math,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean
from pl_peter_weyl_covariant_compat import PLCompat,patched_pw
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_lorentzian_K_block_gate as KG


def run(v=0):
    D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D);P=PLCompat(G)
    w=P.NEIG[v][0];JMAX2=3
    initial=((1,)*len(P.EDGES),(0,)*len(P.VERT))
    with patched_pw(P,CV,KG):
        if hasattr(KG.local_volume_column,'cache_clear'):KG.local_volume_column.cache_clear()
        target_identity=CV.gauss_to_covariant({initial:1+0j},v)
        ident=[[{} for _ in range(2)] for _ in range(2)];maxerr=0.0
        for i in range(2):
            for j in range(2):
                s,_=CV.inverse_then_forward(initial,v,w,i,j,JMAX2,False);ident[i][j]=s
                maxerr=max(maxerr,CV.diff_norm(s,target_identity if i==j else {}))
        iw=CV.weight_by_J(ident);inon=sum(x for k,x in iw.items() if abs(float(k))>1e-15)
        Vgauss=dict(KG.local_volume_column(initial,v));Vcov=CV.gauss_to_covariant(Vgauss,v)
        C=[[{} for _ in range(2)] for _ in range(2)];maxleak=0.0
        for i in range(2):
            for j in range(2):
                hVh,leak=CV.inverse_then_forward(initial,v,w,i,j,JMAX2,True);maxleak=max(maxleak,leak);out={}
                if i==j:P.add_dict(out,Vcov,+1)
                P.add_dict(out,hVh,-1);C[i][j]={k:a for k,a in out.items() if abs(a)>1e-10}
        cnorm=CV.matrix_state_norm(C);cw=CV.weight_by_J(C);total=sum(cw.values())
        j1=cw.get('1.0',0.0);high=sum(x for k,x in cw.items() if float(k)>1+1e-15)/max(total,1e-30)
        supports=[[len(C[i][j]) for j in range(2)] for i in range(2)]
        maxspin=max((max(k[0]) for row in C for st in row for k in st),default=0)/2
        checks={'two_hit_identity':maxerr<1e-10,'identity_scalar_only':inon<1e-20,
                'charged_projection_leakage':maxleak<1e-10,'C_nonzero':cnorm>1e-10,
                'J1_present':j1>1e-14,'no_J_above_1':high<1e-20,'spin_wall':maxspin<=1.5+1e-12}
        return {'status':'exact covariant C_e(V) on independent 16-cell PL-S3 habitat','passed':all(checks.values()),
                'science_status':'PL_LORENTZIAN_PREREQUISITE_CV_ONLY','edge':[v,w],'nodes':len(P.VERT),'edges':len(P.EDGES),
                'Jmax':JMAX2/2,'two_hit_identity_max_error':maxerr,'two_hit_identity_weight_by_J':iw,
                'two_hit_identity_nonzero_J_weight':inon,'charged_volume_projection_leakage':maxleak,
                'C_matrix_supports':supports,'C_matrix_Frobenius_covariant_state_norm':cnorm,
                'C_weight_by_source_J':cw,'C_J1_weight':j1,'C_J_greater_than_1_weight_fraction':high,
                'max_spin_reached':maxspin,'checks':checks,
                'interpretation':'The charged matrix-covariant volume leg survives the first independent non-K5 PL habitat with exact h h^-1 closure and roundoff-level charged-volume leakage.',
                'scope_note':'C(V) prerequisite only. Full PL S requires graph-independent C(K), exact K5 equivalence and the 24-term K-K-V sum.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--node',type=int,default=0);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run(a.node);t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
