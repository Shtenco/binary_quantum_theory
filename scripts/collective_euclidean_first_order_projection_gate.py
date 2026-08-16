#!/usr/bin/env python3
"""S4/chiral theorem: the homogeneous direct Euclidean 6x6 carrier block vanishes.

In the real Peter-Weyl recoupling convention the primitive T stack is real:
CG coefficients and epsilon intertwiners are real and |Q| for Q=i A with A
real antisymmetric is sqrt(-A^2), hence real symmetric. Therefore physical
E_sine=(T-T^T)/(2i)=i A_E with A_E real antisymmetric.

The six coarse-edge carrier is a multiplicity-free real S4 representation.
Depending on orientation phase gauge it is either the ordinary edge
representation or its sign twist.  This gate proves that BOTH representations
have no nonzero invariant real antisymmetric 6x6 matrix. Thus an exactly
homogeneous S4-scalar E has W^dagger E W=0 on the direct six-edge block. Its
metric effect must enter through leakage/depth-two excursions.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import sympy as sp
EDGES=list(itertools.combinations(range(4),2));EI={e:i for i,e in enumerate(EDGES)}
def parity(p):return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1
def rep(p,twist=False):
    R=sp.zeros(6);s=parity(p) if twist else 1
    for i,e in enumerate(EDGES):R[EI[tuple(sorted((p[e[0]],p[e[1]])))],i]=s
    return R
def antisym_commutant_nullity(twist):
    pairs=list(itertools.combinations(range(6),2));vars=sp.symbols('x0:'+str(len(pairs)));A=sp.zeros(6)
    for x,(i,j) in zip(vars,pairs):A[i,j]=x;A[j,i]=-x
    eq=[]
    for p in itertools.permutations(range(4)):
        C=rep(p,twist)*A-A*rep(p,twist);eq.extend(list(C))
    M,_=sp.linear_eq_to_matrix(eq,vars);return len(vars)-M.rank(),M.rank()
def full_commutant_dimension(twist):
    vars=sp.symbols('y0:36');M0=sp.Matrix(6,6,vars);eq=[]
    for p in itertools.permutations(range(4)):
        C=rep(p,twist)*M0-M0*rep(p,twist);eq.extend(list(C))
    A,_=sp.linear_eq_to_matrix(eq,vars);return 36-A.rank()
def run():
    n0,r0=antisym_commutant_nullity(False);n1,r1=antisym_commutant_nullity(True);c0=full_commutant_dimension(False);c1=full_commutant_dimension(True)
    checks={'ordinary_edge_antisymmetric_commutant_zero':n0==0,'sign_twisted_edge_antisymmetric_commutant_zero':n1==0,'ordinary_complex_commutant_dimension3':c0==3,'sign_twisted_complex_commutant_dimension3':c1==3}
    return {'status':'homogeneous Euclidean first-order six-edge projection theorem','passed':all(checks.values()),'science_status':'COLLECTIVE_SYMMETRY_THEOREM','ordinary_edge_antisymmetric_commutant_nullity':n0,'sign_twisted_edge_antisymmetric_commutant_nullity':n1,'ordinary_full_commutant_dimension':c0,'sign_twisted_full_commutant_dimension':c1,'checks':checks,'conclusion':'For either orientation phase convention, an S4-invariant pure-imaginary Hermitian operator i*A with A real antisymmetric has zero direct matrix on the six-edge carrier. Therefore the homogeneous W^dagger E_sine W block vanishes; Euclidean metric dynamics first appears through depth-two/leakage or through other sectors, not a fitted direct 6x6 term.','scope_note':'The theorem assumes exact homogeneous S4 covariance and the frozen real recoupling/absolute-volume convention. It does not say E has zero leakage; in fact that leakage is the required depth-two backreaction channel.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())