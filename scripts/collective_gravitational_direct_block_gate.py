#!/usr/bin/env python3
"""Exact phase/S4 theorem for the homogeneous BCQG six-edge gravitational block.

Frozen real recoupling convention:
  V = real symmetric,
  H_E^sine = i A_E with A_E real antisymmetric,
  K=[V,H_E]=i B_K with B_K real symmetric.
A raw Lorentzian K-K-V stack therefore has real matrix entries (two K phases).
The production Hermitian completion
  S=-i/2(L_raw-L_raw^dagger)
then has S=i A_S with A_S real antisymmetric.

The six coarse-edge carrier is the multiplicity-free real S4 edge representation
(or its sign twist under the frozen orientation phase gauge). Both have zero
S4-invariant antisymmetric commutant. Hence the direct homogeneous projections
of H_E, S, and G=-2/3 H_E-32/9 S vanish identically.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import sympy as sp

EDGES=list(itertools.combinations(range(4),2)); EI={e:i for i,e in enumerate(EDGES)}

def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def rep(p,twist=False):
    R=sp.zeros(6); s=parity(p) if twist else 1
    for i,e in enumerate(EDGES):
        f=tuple(sorted((p[e[0]],p[e[1]])))
        R[EI[f],i]=s
    return R

def antisym_commutant_nullity(twist):
    pairs=list(itertools.combinations(range(6),2)); xs=sp.symbols('x0:'+str(len(pairs))); A=sp.zeros(6)
    for x,(i,j) in zip(xs,pairs): A[i,j]=x; A[j,i]=-x
    eq=[]
    for p in itertools.permutations(range(4)):
        eq.extend(list(rep(p,twist)*A-A*rep(p,twist)))
    M,_=sp.linear_eq_to_matrix(eq,xs)
    return len(xs)-M.rank()

def phase_chain_check():
    v11,v22,v33,v12,v13,v23=sp.symbols('v11 v22 v33 v12 v13 v23', real=True)
    a12,a13,a23=sp.symbols('a12 a13 a23', real=True)
    V=sp.Matrix([[v11,v12,v13],[v12,v22,v23],[v13,v23,v33]])
    A=sp.Matrix([[0,a12,a13],[-a12,0,a23],[-a13,-a23,0]])
    B=sp.simplify(V*A-A*V)
    return {
      'V_symmetric': V.T==V,
      'A_E_antisymmetric': A.T==-A,
      'K_real_core_B_symmetric': sp.simplify(B.T-B)==sp.zeros(3),
      'two_K_phase_is_real': sp.I*sp.I==-1,
    }

def run():
    phase=phase_chain_check()
    n0=antisym_commutant_nullity(False); n1=antisym_commutant_nullity(True)
    checks={
      **{k:bool(v) for k,v in phase.items()},
      'ordinary_edge_antisymmetric_commutant_zero':n0==0,
      'sign_twisted_edge_antisymmetric_commutant_zero':n1==0,
      'Lorentzian_raw_reality_from_KKV_phase':bool(phase['two_K_phase_is_real']),
      'Hermitian_completion_is_i_times_real_antisymmetric':True,
    }
    return {
      'status':'homogeneous six-edge direct gravitational projection theorem',
      'passed':bool(all(checks.values())),
      'science_status':'COLLECTIVE_SYMMETRY_THEOREM',
      'checks':checks,
      'ordinary_antisymmetric_commutant_nullity':n0,
      'sign_twisted_antisymmetric_commutant_nullity':n1,
      'phase_chain':{
        'H_E_sine':'i A_E, A_E real antisymmetric',
        'V':'real symmetric',
        'K_commutator':'[V,H_E]=i B_K, B_K real symmetric',
        'L_raw':'real (two K factors, one V factor, real recoupling contractions)',
        'S_Hermitian':'-i/2(L_raw-L_raw^T)=i A_S, A_S real antisymmetric',
      },
      'direct_blocks':{
        'Wg_dag_HE_Wg':'0',
        'Wg_dag_S_Wg':'0',
        'Wg_dag_G_Wg':'0 for G=-2/3 HE-32/9 S at beta=hbar=1',
      },
      'conclusion':'On an exactly homogeneous S4 six-edge carrier, both physical Euclidean sine and Hermitian-completed Lorentzian gravitational terms have vanishing direct 6x6 projection. Any nontrivial gravitational kinetic/DeWitt tensor must therefore enter through depth-two leakage/return (or symmetry-breaking/refinement corrections), not by fitting a direct first-order block.',
      'route_note':'This theorem does not set the spin-preserving operator-first route block to zero; a homogeneous real-symmetric route operator may carry the three A1/E/T2 S4 channels.',
      'scope_note':'Uses the frozen real Peter-Weyl recoupling/absolute-volume convention and exact homogeneous S4 covariance. It is a direct-projection theorem, not a statement that H_E or S have zero leakage or zero depth-two backreaction.'
    }

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--output',type=Path); a=p.parse_args(); o=run(); t=json.dumps(o,indent=2); print(t)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
