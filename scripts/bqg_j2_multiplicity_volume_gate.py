#!/usr/bin/env python3
"""First multiplicity-space geometry gate at j=2.

At j=2 the four-valent singlet space has dimension 5 and contains two copies of
the S4 [2,2] irrep.  This gate asks whether the absolute volume operator,
already used throughout the BQG Peter-Weyl stack, resolves those two copies.

Because |Q|^(1/4) is S4 invariant, its restriction to the [2,2] isotypic sector
must have Schur form A_2 ⊗ I_2.  Therefore its nonzero isotypic eigenvalues must
come in exact pairs.  Distinct pairs imply that geometry itself selects a
preferred multiplicity eigenbasis.
"""
from __future__ import annotations
import argparse, itertools, json, math, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import peter_weyl_j1_s4_block_gate as J1
import k5_peter_weyl_safe_hda_column as PW

PERMS=tuple(itertools.permutations(range(4)))
CHAR22={
    (1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0,
}


def projector22(s2=4):
    d=s2+1
    P=np.zeros((d,d),dtype=complex)
    for p in PERMS:
        P += CHAR22[J1.cycle_type(p)]*J1.permutation_matrix(s2,p)
    P *= 2/24
    return (P+P.conj().T)/2


def volume_matrix(s2=4):
    ks,ts=J1.local_basis(s2)
    V=np.zeros((len(ks),len(ks)),dtype=complex)
    for j,T in enumerate(ts):
        VT=PW.apply_volume_tensor(T,(s2,s2,s2,s2))
        for i,S in enumerate(ts):
            V[i,j]=np.vdot(S,VT)
    return (V+V.conj().T)/2,ks


def run():
    s2=4
    V,ks=volume_matrix(s2)
    P=projector22(s2)
    rank=int(np.sum(np.linalg.eigvalsh(P)>0.5))
    assert rank==4

    comm=max(float(np.linalg.norm(V@J1.permutation_matrix(s2,p)-J1.permutation_matrix(s2,p)@V)) for p in PERMS)
    V22=P@V@P
    # Work on the image basis of P.
    evP,UP=np.linalg.eigh(P)
    B=UP[:,evP>0.5]
    R=(B.conj().T@V@B + (B.conj().T@V@B).conj().T)/2
    ev=np.linalg.eigvalsh(R).real
    ev.sort()

    pair1=ev[:2]
    pair2=ev[2:]
    pair_spread=max(float(np.ptp(pair1)),float(np.ptp(pair2)))
    pair_gap=float(abs(np.mean(pair2)-np.mean(pair1)))

    # An S4-invariant operator on 2 copies of [2,2] must yield paired spectrum.
    passed=(
        comm<2e-7
        and pair_spread<2e-7*max(float(np.max(np.abs(ev))),1.0)
        and pair_gap>1e-8
    )

    return {
        "status":"j=2 [2,2] multiplicity-space absolute-volume gate",
        "passed":bool(passed),
        "j":2.0,
        "singlet_K2_basis":list(ks),
        "singlet_dimension":len(ks),
        "P22_rank":rank,
        "S4_commutator_max":comm,
        "restricted_volume_eigenvalues":[float(x) for x in ev],
        "pair1_mean":float(np.mean(pair1)),
        "pair2_mean":float(np.mean(pair2)),
        "paired_degeneracy_spread_max":pair_spread,
        "multiplicity_channel_gap":pair_gap,
        "interpretation":(
            "If PASS, the first multiplicity-two [2,2] sector is resolved by the existing absolute-volume geometry: "
            "V|_[2,2] has two distinct eigenvalues, each exactly doubled by the irrep dimension. "
            "This supplies a symmetry-compatible multiplicity eigenbasis without adding a fitted projector."
        ),
        "claim_boundary":(
            "Absolute volume selects a geometric multiplicity basis only. "
            "The physical RG channel must still be selected by the full master/history dynamics."
        )
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run()
    txt=json.dumps(out,indent=2)
    print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 2

if __name__=="__main__":
    raise SystemExit(main())
