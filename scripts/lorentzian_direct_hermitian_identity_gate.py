#!/usr/bin/env python3
"""Algebraic certificate for the direct-Hermitian Lorentzian commutator form.

Uses genuinely operator-valued 2x2 auxiliary matrices: every block is a
noncommuting graph-space matrix.  K legs are anti-Hermitian and V legs
Hermitian.  The gate compares the historical 6 forward + 6 adjoint physical
completion with the 3 commutator-anticommutator form for one omitted slot.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np

def psgn(p):
    return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1

def ptr_aux(X,na,ng):
    Y=X.reshape(na,ng,na,ng)
    out=np.zeros((ng,ng),complex)
    for i in range(na):out+=Y[i,:,i,:]
    return out

def run(seed=271828):
    rng=np.random.default_rng(seed);na=2;ng=5;n=na*ng
    K=[];V=[]
    for _ in range(3):
        X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));K.append(X-X.conj().T)
        Y=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));V.append((Y+Y.conj().T)/2)
    L=np.zeros((ng,ng),complex)
    for p in itertools.permutations(range(3)):
        L+=psgn(p)*ptr_aux(K[p[0]]@K[p[1]]@V[p[2]],na,ng)
    Sold=-0.5j*(L-L.conj().T)
    Snew=np.zeros_like(Sold);term_def=[]
    for a,b,c in ((0,1,2),(1,2,0),(2,0,1)):
        C=K[a]@K[b]-K[b]@K[a]
        Y=C@V[c]+V[c]@C
        term=ptr_aux(Y,na,ng)
        anti=float(np.linalg.norm(term+term.conj().T)/max(np.linalg.norm(term),1e-300));term_def.append(anti)
        Snew+=-0.5j*term
    den=max(np.linalg.norm(Sold),1e-300);rel=float(np.linalg.norm(Snew-Sold)/den)
    herm_old=float(np.linalg.norm(Sold-Sold.conj().T)/den);herm_new=float(np.linalg.norm(Snew-Snew.conj().T)/max(np.linalg.norm(Snew),1e-300))
    # Also verify raw six-to-three pairing separately.
    L3=np.zeros_like(L)
    for a,b,c in ((0,1,2),(1,2,0),(2,0,1)):
        L3+=ptr_aux((K[a]@K[b]-K[b]@K[a])@V[c],na,ng)
    rawrel=float(np.linalg.norm(L3-L)/max(np.linalg.norm(L),1e-300))
    checks={'K_antihermitian':all(np.linalg.norm(x+x.conj().T)<1e-12 for x in K),
            'V_hermitian':all(np.linalg.norm(x-x.conj().T)<1e-12 for x in V),
            'six_to_three_raw_identity':rawrel<1e-12,
            'each_anticommutator_word_antihermitian':max(term_def)<1e-12,
            'old_new_physical_S_equal':rel<1e-12,
            'old_S_hermitian':herm_old<1e-12,'new_S_hermitian':herm_new<1e-12}
    return {'status':'direct-Hermitian Lorentzian commutator identity certificate','passed':bool(all(checks.values())),
      'science_status':'EXACT_OPERATOR_IDENTITY_CONTROL','checks':checks,'seed':seed,'aux_dim':na,'graph_dim':ng,
      'raw_six_to_three_relative_error':rawrel,'physical_old_new_relative_error':rel,
      'old_hermiticity_defect':herm_old,'new_hermiticity_defect':herm_new,
      'max_term_antihermiticity_defect':max(term_def),
      'identity':'S=-i/2 sum_cyclic Tr_aux({[C_a(K),C_b(K)],C_c(V)})',
      'scope_note':'Noncommuting operator-valued auxiliary control. BCQG production promotion separately requires finite Peter-Weyl pair equivalence and unchanged V2 hard guards.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
