#!/usr/bin/env python3
"""Exact S4 symmetry reduction of operators on the six coarse tetrahedral edges."""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import sympy as sp

def run():
    edges=list(itertools.combinations(range(4),2));idx={e:i for i,e in enumerate(edges)};A=sp.zeros(6);O=sp.zeros(6)
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if i==j:continue
            if len(set(e)&set(f))==1:A[i,j]=1
            elif len(set(e)&set(f))==0:O[i,j]=1
    I=sp.eye(6);J=sp.ones(6);P1=J/6
    PE=sp.simplify((A-4*I)*A/12);PT=sp.simplify((A-4*I)*(A+2*I)/(-8))
    a,b,c=sp.symbols('a b c',real=True);M=a*I+b*A+c*O
    checks={'octahedral_relation':O==J-I-A,'rank_A1':P1.rank()==1,'rank_E':PE.rank()==2,'rank_T2':PT.rank()==3,'projectors_sum_I':sp.simplify(P1+PE+PT)==I,'projectors_orthogonal':all(sp.simplify(X*Y)==sp.zeros(6) for X,Y in [(P1,PE),(P1,PT),(PE,PT)]),'lambda_A1':sp.simplify(M*P1-(a+4*b+c)*P1)==sp.zeros(6),'lambda_E':sp.simplify(M*PE-(a-2*b+c)*PE)==sp.zeros(6),'lambda_T2':sp.simplify(M*PT-(a-c)*PT)==sp.zeros(6)}
    cov=True
    for p in itertools.permutations(range(4)):
        R=sp.zeros(6)
        for i,e in enumerate(edges):R[idx[tuple(sorted((p[e[0]],p[e[1]])))],i]=1
        cov &= R.T*A*R==A and R.T*O*R==O
    checks['all_24_S4_covariant']=cov
    return {'status':'exact S4 six-edge commutant reduction','passed':all(checks.values()),'science_status':'COLLECTIVE_SYMMETRY_THEOREM','edge_order':[list(e) for e in edges],'decomposition':'6=A1(1)+E(2)+T2(3)','generic_invariant_operator':'M=a I+b A_adj+c O_opposite','eigenvalues':{'A1':'a+4b+c','E':'a-2b+c','T2':'a-c'},'representative_elements_required':3,'checks':checks,'interpretation':'Any exactly tetrahedrally invariant effective scalar or equivariant edge-response map on the six-edge carrier is fixed by three channel coefficients. SO(3) continuum isotropy additionally requires the E and T2 channels to merge.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())