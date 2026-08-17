#!/usr/bin/env python3
"""Exact local K=0 pairing-stabilizer reduction of the 24 Lorentzian slot orbit.

This is a structural execution theorem only.  It identifies the largest slot
permutation subgroup that keeps the frozen all-j=1/2 K=0 seed in the same local
intertwiner line.  It does NOT yet replace production ordered terms: the global
oriented Peter-Weyl recoupling action on output states must be validated on
held-out direct terms before orbit reconstruction is allowed.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np


def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def singlet_pair_tensor():
    s=np.array([[0,1],[-1,0]],complex)/math.sqrt(2)
    return np.einsum('ab,cd->abcd',s,s)

def permuted(T,p):return np.transpose(T,axes=p)

def worker_specs():
    out=[]
    for omit in range(4):
        base=tuple(r for r in range(4) if r!=omit)
        for perm in itertools.permutations(base):
            idx=tuple(base.index(x) for x in perm)
            coef=((-1)**omit)*parity(idx)
            full=perm+(omit,)
            out.append({'index':len(out),'omit':omit,'perm':perm,'full':full,'coef':int(coef),'full_parity':parity(full)})
    return out

def run():
    T=singlet_pair_tensor();H=[];rows=[]
    for p in itertools.permutations(range(4)):
        U=permuted(T,p);ov=np.vdot(T,U);leak=float(np.linalg.norm(U-ov*T))
        exact=leak<1e-12 and abs(abs(ov)-1)<1e-12
        if exact:H.append(p)
        rows.append({'permutation':list(p),'parity':parity(p),'K0_line_overlap':[float(ov.real),float(ov.imag)],'orthogonal_leakage':leak,'preserves_K0_line':exact})
    specs=worker_specs();idx={x['full']:x['index'] for x in specs}
    unused=set(range(24));orbits=[]
    while unused:
        i=min(unused);f=specs[i]['full']
        orb=sorted({idx[tuple(h[x] for x in f)] for h in H})
        orbits.append(orb);unused-=set(orb)
    # Alternating PL epsilon coefficient transforms by det(h).
    coeff_ok=True
    for h in H:
        for s in specs:
            j=idx[tuple(h[x] for x in s['full'])]
            coeff_ok &= specs[j]['coef']==parity(h)*s['coef']
    phases=sorted(set(round(np.vdot(T,permuted(T,h)).real) for h in H))
    # The 16-node homogeneous product seed has phase chi(h)^16=+1 for every H element.
    global_seed_phase_ok=all(abs(np.vdot(T,permuted(T,h)))**16>1-1e-12 and abs((np.vdot(T,permuted(T,h)))**16-1)<1e-12 for h in H)
    checks={
      'exact_pairing_stabilizer_order8':len(H)==8,
      'three_free_orbits_of_size8':len(orbits)==3 and all(len(o)==8 for o in orbits),
      'worker_epsilon_transforms_by_permutation_parity':bool(coeff_ok),
      'local_K0_character_is_plus_minus_one':phases==[-1,1],
      'sixteen_node_product_seed_character_trivial':bool(global_seed_phase_ok),
      'full_S4_not_seed_stabilizer':sum(r['preserves_K0_line'] for r in rows)==8,
    }
    return {
      'status':'frozen K0 seed pairing-stabilizer decomposition of 24 Lorentzian slot orbit',
      'passed':bool(all(checks.values())),
      'science_status':'STRUCTURAL_ORBIT_REDUCTION_PREREQUISITE',
      'pairing':'(01)(23)',
      'stabilizer_group':'(S2 x S2) semidirect S2, order 8',
      'stabilizer_permutations':[list(h) for h in H],
      'local_seed_character_values':phases,
      'worker_orbits':orbits,
      'heavy_representative_indices_per_mode':[o[0] for o in orbits],
      'potential_heavy_term_reduction':'24 -> 3 per forward/adjoint mode; 48 -> 6 total only after global oriented-output covariance validation',
      'checks':checks,'permutation_rows':rows,
      'operator_covariance_note':'Structurally Q_tet is an alternating four-leg pseudoscalar, V_tet=sqrt(abs(Q_tet)) is invariant, E_sine and K=[V,E] are pseudoscalar, and two K legs make the unweighted K-K-V ordered word slot-covariant. The collector epsilon coefficient carries the remaining permutation parity.',
      'hard_guard':'DO NOT reconstruct production Lorentzian terms from these orbits until an exact global oriented Peter-Weyl state-action U_h is implemented and independently checked against held-out direct V2 ordered terms.',
    }

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
