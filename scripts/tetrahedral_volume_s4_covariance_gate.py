#!/usr/bin/env python3
"""Full local S4 covariance audit of the tetrahedral grasping Q_tet.

For deterministic generic magnetic tensors and several unequal spin quartets,
verify all 24 local-leg permutations:

  Q_tet(pi.j) U_pi = sgn(pi) U_pi Q_tet(j).

Thus Q_tet is a local tetrahedral pseudoscalar before taking V=sqrt(abs(Q)).
The test is independent of GR, HDA and Lorentzian amplitude targets.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import numpy as np
from tetrahedral_volume_backend import apply_q_tetra

def sign(p):return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def run(seed=20260816):
    rg=np.random.default_rng(seed)
    spin_sets=[(1,1,1,1),(0,1,1,2),(1,2,2,3),(0,2,1,3),(2,3,1,2)]
    rows=[];worst=0.0
    for sp in spin_sets:
        T=rg.normal(size=tuple(s+1 for s in sp))+1j*rg.normal(size=tuple(s+1 for s in sp))
        Q=apply_q_tetra(T,sp);per=[]
        for p in itertools.permutations(range(4)):
            spp=tuple(sp[i] for i in p);Tp=np.transpose(T,axes=p)
            lhs=apply_q_tetra(Tp,spp);rhs=sign(p)*np.transpose(Q,axes=p)
            err=float(np.linalg.norm(lhs-rhs)/max(np.linalg.norm(rhs),1e-30));worst=max(worst,err)
            per.append({'permutation':list(p),'sign':sign(p),'relative_defect':err})
        rows.append({'doubled_spins':list(sp),'input_shape':[s+1 for s in sp],'Q_norm':float(np.linalg.norm(Q)),'max_relative_defect':max(x['relative_defect'] for x in per),'permutations':per})
    checks={'all_24_permutations_each_quartet':all(len(r['permutations'])==24 for r in rows),
            'pseudoscalar_covariance_roundoff':worst<1e-12}
    return {'status':'full local S4 covariance of tetrahedral charged-volume grasping','passed':bool(all(checks.values())),'seed':seed,
            'spin_quartets':len(rows),'permutations_per_quartet':24,'maximum_relative_covariance_defect':worst,'checks':checks,'rows':rows,
            'identity':'Q_tet(pi.j) U_pi = sgn(pi) U_pi Q_tet(j)',
            'consequence':'V_tet=sqrt(abs(Q_tet)) is permutation-even while Q_tet carries the tetrahedral orientation character; no local leg is preferred on charged sectors.',
            'scope_note':'Local representation/covariance theorem regression only; it does not supply a Lorentzian amplitude or GR target.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
