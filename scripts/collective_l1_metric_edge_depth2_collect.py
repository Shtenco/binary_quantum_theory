#!/usr/bin/env python3
"""Collect exact same/adjacent/opposite L1 metric depth-two representatives.

For edges 01,02,23 load u_e and v_e=H_B u_e and form
K=<u|u>, A=<u|v>, B=<v|v>.  S4 reduces each six-edge kernel to orbit
coefficients (same, adjacent, opposite), hence to A1, E and T2 eigenvalues.
The normalized Krylov moments are h1=A/K, h2=B/K and Sigma2=h2-h1^2.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np

REPS=(0,1,5)
TOL=3e-7

def load_state(path):
    z=np.load(path); out={}
    for i,a in enumerate(z['amp']): out[z['spins'][i].tobytes()+z['Ks'][i].tobytes()]=complex(a)
    return out

def inner(a,b):
    if len(a)<=len(b): return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())
    return sum(np.conj(a.get(k,0j))*v for k,v in b.items())
def mat(L,R): return np.asarray([[inner(L[i],R[j]) for j in range(3)] for i in range(3)],complex)

def orbit(M):
    n=max(float(np.linalg.norm(M)),1e-30); diag=[M[i,i].real for i in range(3)]; adj=[M[0,1].real,M[1,0].real,M[1,2].real,M[2,1].real]; opp=[M[0,2].real,M[2,0].real]
    a=float(np.mean(diag)); b=float(np.mean(adj)); c=float(np.mean(opp)); fit=np.array([[a,b,c],[b,a,b],[c,b,a]])
    return {'a_same':a,'b_adjacent':b,'c_opposite':c,'hermiticity_relative_defect':float(np.linalg.norm(M-M.conj().T)/n),
            'max_imaginary_entry':float(np.max(np.abs(M.imag))),'diagonal_spread':float(max(diag)-min(diag)),'adjacent_spread':float(max(adj)-min(adj)),
            'opposite_spread':float(max(opp)-min(opp)),'three_representative_orbit_residual':float(np.linalg.norm(M.real-fit)/max(np.linalg.norm(M.real),1e-30)),
            'lambda_A1':a+4*b+c,'lambda_E':a-2*b+c,'lambda_T2':a-c}

def run(root):
    meta=[]; U=[]; V=[]
    for e in REPS:
        m=json.loads((root/f'edge_{e}.json').read_text())
        if not m.get('passed'): raise RuntimeError(f'edge {e} failed: {m.get("error","")}')
        meta.append(m); U.append(load_state(root/f'u_{e}.npz')); V.append(load_state(root/f'v_{e}.npz'))
    K=mat(U,U); A=mat(U,V); B=mat(V,V); ko=orbit(K); ao=orbit(A); bo=orbit(B)
    dyn={}
    for ir in ('A1','E','T2'):
        k=ko[f'lambda_{ir}']; aa=ao[f'lambda_{ir}']; bb=bo[f'lambda_{ir}']
        if k<=1e-12: raise RuntimeError(f'nonpositive K_{ir}={k}')
        h1=aa/k; h2=bb/k; dyn[ir]={'K':k,'A':aa,'B':bb,'h1_normalized':h1,'h2_normalized':h2,'Sigma2_depth2':h2-h1*h1}
    dh2=dyn['E']['h2_normalized']-dyn['T2']['h2_normalized']; dvar=dyn['E']['Sigma2_depth2']-dyn['T2']['Sigma2_depth2']
    mh2=.5*(dyn['E']['h2_normalized']+dyn['T2']['h2_normalized']); mvar=.5*(dyn['E']['Sigma2_depth2']+dyn['T2']['Sigma2_depth2'])
    symmetry=all(x['hermiticity_relative_defect']<TOL and x['three_representative_orbit_residual']<TOL for x in (ko,ao,bo))
    variance=min(x['Sigma2_depth2'] for x in dyn.values())>-3e-6
    finite=all(np.isfinite(np.asarray(M.real)).all() and np.isfinite(np.asarray(M.imag)).all() for M in (K,A,B))
    return {'status':'exact symmetry-reduced L1 metric-edge depth-two Euclidean Krylov response','passed':bool(symmetry and variance and finite),'science_status':'L1_METRIC_EDGE_DEPTH2_KRYLOV',
            'edge_representatives':[m['edge'] for m in meta],'definition':{'u_e':'(1/2) sum_{4 chambers->e} H_c|Omega>','H_B':'sum H_w over 24 parent-block chambers','v_e':'H_B u_e','K':'<u_e|u_f>','A':'<u_e|H_B u_f>','B':'<H_Bu_e|H_Bu_f>'},
            'K_orbit':ko,'A_orbit':ao,'B_orbit':bo,'dynamic_irreps':dyn,'Delta_ET_h2':dh2,'relative_ET_h2_split':dh2/mh2 if abs(mh2)>1e-30 else None,
            'Delta_ET_Sigma2':dvar,'relative_ET_Sigma2_split':dvar/mvar if abs(mvar)>1e-30 else None,
            'checks':{'finite':finite,'S4_three_orbit_consistency':symmetry,'nonnegative_depth2_variance_with_tolerance':variance},'worker_diagnostics':meta,
            'interpretation':'Genuine full-E depth-two dynamics on the first refined metric carrier. E-T2 splitting is a dynamical tetrahedral anisotropy diagnostic, not yet a Lorentzian TT pole coefficient or zeta4.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=run(a.root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items() if k!='worker_diagnostics'},indent=2));return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
