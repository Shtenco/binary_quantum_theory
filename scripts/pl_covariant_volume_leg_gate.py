#!/usr/bin/env python3
"""Regress the charged covariant volume leg on arbitrary PL dual complexes.

The gate proves that the historical K5 charged/all-J recoupling machinery can
be driven by the graph-independent PL backend without changing its SU(2)
algebra.  First the boundary-4-simplex PL backend is compared to the native K5
C(V) result.  Then the same two-hit identity and C(V) representation checks are
run on the independent 16-cell PL-S3 regulator.
"""
from __future__ import annotations
import argparse,json,math,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_covariant_volume_leg_gate as CV
from pl_dual_complex import DualComplex,boundary_4simplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean
from pl_covariant_backend import install_pl_graph

def diff(a,b):
    keys=set(a)|set(b)
    return math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys))

def matrix_diff(A,B):return math.sqrt(sum(diff(A[i][j],B[i][j])**2 for i in range(2) for j in range(2)))
def matrix_norm(A):return math.sqrt(sum(CV.covariant_state_norm2(A[i][j]) for i in range(2) for j in range(2)))
def cv_matrix(initial,v,w,Jmax2):
    Vgauss=dict(__import__('peter_weyl_lorentzian_K_block_gate').local_volume_column(initial,v))
    Vcov=CV.gauss_to_covariant(Vgauss,v);out=[[{} for _ in range(2)] for _ in range(2)];maxleak=0.0
    for i in range(2):
        for j in range(2):
            hVh,leak=CV.inverse_then_forward(initial,v,w,i,j,Jmax2,True);maxleak=max(maxleak,leak);s={}
            if i==j:PW.add_dict(s,Vcov,+1)
            PW.add_dict(s,hVh,-1);out[i][j]={k:a for k,a in s.items() if abs(a)>1e-10}
    return out,maxleak

def two_hit(initial,v,w,Jmax2):
    target=CV.gauss_to_covariant({initial:1+0j},v);mx=0.0;nonzeroJ=0.0
    for i in range(2):
        for j in range(2):
            s,_=CV.inverse_then_forward(initial,v,w,i,j,Jmax2,False)
            mx=max(mx,CV.diff_norm(s,target if i==j else {}))
            for key,a in s.items():
                if key[2]!=0:nonzeroJ+=abs(a)**2
    return mx,nonzeroJ

def run():
    JMAX2=3
    # Native K5 result.
    initial=PW.basis_full_jhalf()[0];v=0;w=PW.NEIG[v][0]
    native,nleak=cv_matrix(initial,v,w,JMAX2)

    # Same complex through PL boundary-4-simplex backend.
    KD=DualComplex(boundary_4simplex());KG=PLPeterWeylEuclidean(KD)
    with install_pl_graph(KG):
        pseed=((1,)*len(KG.EDGES),(0,)*KD.n_tets);pw=KD.neighbor[(0,0)]
        plk5,pleak=cv_matrix(pseed,0,pw,JMAX2)
        # Node ordering matches the historical K5 tetra labels on this seed.
        reduction=matrix_diff(plk5,native)/max(matrix_norm(native),1e-30)

    # Independent 16-cell charged identity and C(V).
    D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D)
    with install_pl_graph(G):
        seed=((1,)*len(G.EDGES),(0,)*D.n_tets);v=0;w=D.neighbor[(v,0)]
        ident_err,ident_J=two_hit(seed,v,w,JMAX2)
        C,cleak=cv_matrix(seed,v,w,JMAX2)
        Cnorm=matrix_norm(C);weights=CV.weight_by_J(C)
        high=sum(x for J,x in ((float(k),v) for k,v in weights.items()) if J>1+1e-15)
        total=sum(weights.values());j1=weights.get('1.0',0.0)
        supports=[[len(C[i][j]) for j in range(2)] for i in range(2)]

    checks={
      'K5_PL_backend_reduction':reduction<1e-10,
      'K5_native_charged_leakage':nleak<1e-10,
      'K5_PL_charged_leakage':pleak<1e-10,
      '16cell_two_hit_identity':ident_err<1e-10 and ident_J<1e-20,
      '16cell_complete_charged_volume_basis':cleak<1e-10,
      '16cell_CV_nonzero':Cnorm>1e-10 and j1>1e-14,
      '16cell_no_source_J_gt_1':high/max(total,1e-30)<1e-20,
    }
    return {'status':'PL backend regression for exact matrix-covariant C_e(V)',
            'passed':bool(all(checks.values())),'checks':checks,
            'K5_reduction_relative_error':reduction,
            'K5_native_max_charged_leakage':nleak,'K5_PL_max_charged_leakage':pleak,
            'sixteen_cell':{'edge':[v,w],'two_hit_identity_error':ident_err,'two_hit_nonzero_J_weight':ident_J,
                            'C_matrix_supports':supports,'C_matrix_norm':Cnorm,'C_weight_by_source_J':weights,
                            'C_J_greater_than_1_fraction':high/max(total,1e-30),
                            'max_charged_volume_basis_leakage':cleak},
            'interpretation':'The charged/all-J recoupling layer is graph-independent in practice: the PL backend reproduces K5 and remains complete on the square-plaquette 16-cell regulator. The remaining Lorentzian graph lift is therefore concentrated in physical-sine K and its C(K) actions, not in the charged volume representation theory.',
            'scope_note':'C(V) backend bridge only; C(K), full Hermitian S and collective HDA remain separate gates.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
