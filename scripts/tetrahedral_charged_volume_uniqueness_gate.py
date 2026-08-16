#!/usr/bin/env python3
"""Linear-algebra uniqueness of the tetrahedral pseudoscalar triple-grasping sum.

In the coefficient space (q_hat0,...,q_hat3), construct the exact S4 action and
solve R(pi)c=sgn(pi)c for all 24 permutations.  The solution must be one
dimensional and proportional to (1,-1,1,-1).  This is target-independent and
precedes the corrected Lorentzian science result.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np

def sgn(seq):return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def action(p):
    R=np.zeros((4,4),int)
    for r in range(4):
        comp=[i for i in range(4) if i!=r];mapped=[p[i] for i in comp]
        R[p[r],r]=sgn(mapped)
    return R

def run():
    rows=[];constraints=[]
    c=np.array([1.,-1.,1.,-1.])
    worst=0.0
    for p in itertools.permutations(range(4)):
        R=action(p);sp=sgn(p);A=R-sp*np.eye(4);constraints.append(A)
        defect=float(np.linalg.norm(R@c-sp*c));worst=max(worst,defect)
        rows.append({'permutation':list(p),'sign':sp,'action':R.tolist(),'generator_defect':defect})
    M=np.vstack(constraints);u,s,vh=np.linalg.svd(M);rank=int(np.sum(s>1e-12));nullity=4-rank;v=vh[-1];v/=np.linalg.norm(v)
    target=c/np.linalg.norm(c);overlap=abs(float(np.dot(v,target)));projdef=float(math.sqrt(max(0.0,1-overlap*overlap)))
    checks={'all_24_generator_identities_exact':worst==0.0,'constraint_rank_three':rank==3,'sign_eigenspace_nullity_one':nullity==1,'unique_vector_alternating':projdef<1e-12}
    return {'status':'uniqueness of tetrahedral charged-volume pseudoscalar linear completion','passed':bool(all(checks.values())),'checks':checks,
            'constraint_matrix_shape':list(M.shape),'singular_values':[float(x) for x in s],'constraint_rank':rank,'sign_eigenspace_nullity':nullity,
            'normalized_null_vector':[float(x) for x in v],'alternating_target_normalized':[float(x) for x in target],
            'projective_defect_vs_alternating_vector':projdef,'maximum_exact_generator_defect':worst,
            'result':'Q is unique up to scale in span{q_hat_r}: Q proportional to sum_r (-1)^r q_hat_r. Gauss-sector absolute-volume continuity fixes scale 1/4.',
            'scope_note':'Uniqueness within the linear four-triple-grasping S4-pseudoscalar ansatz only.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
