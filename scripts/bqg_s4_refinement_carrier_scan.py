#!/usr/bin/env python3
"""Scan the four-equal-spin singlet spaces under S4 and track the [2,2] carrier.

Uses the same exact intertwiner tensors and permutation action as the canonical
j=1/2 -> j=1 gate.  For each doubled spin s2=1..s2_max, the four-valent singlet
space has basis K2=0,2,...,2*s2 and dimension s2+1.  We compute S4 characters
numerically from exact recoupling tensors and decompose against the five S4
irreps.

The key RG question is whether [2,2] appears with multiplicity one at every
representation scale.  If yes, the logical geometry qubit has a unique
symmetry-selected continuation across the entire tested Peter-Weyl tower.
"""
from __future__ import annotations
import argparse, itertools, json, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import peter_weyl_j1_s4_block_gate as J1

PERMS=tuple(itertools.permutations(range(4)))

# S4 character table indexed by cycle type in our convention.
CHAR_TABLE={
    "[4]": {
        (1,1,1,1):1,(2,1,1):1,(2,2):1,(3,1):1,(4,):1,
    },
    "[3,1]": {
        (1,1,1,1):3,(2,1,1):1,(2,2):-1,(3,1):0,(4,):-1,
    },
    "[2,2]": {
        (1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0,
    },
    "[2,1,1]": {
        (1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1,
    },
    "[1^4]": {
        (1,1,1,1):1,(2,1,1):-1,(2,2):1,(3,1):1,(4,):-1,
    },
}
CLASS_SIZE={(1,1,1,1):1,(2,1,1):6,(2,2):3,(3,1):8,(4,):6}


def decompose(s2:int):
    chars={}
    spread={}
    grouped={}
    for p in PERMS:
        ct=J1.cycle_type(p)
        grouped.setdefault(ct,[]).append(complex(np.trace(J1.permutation_matrix(s2,p))))
    for ct,vals in grouped.items():
        chars[ct]=float(np.mean(vals).real)
        spread[ct]=float(np.max(np.abs(np.array(vals)-np.mean(vals))))
    mult={}
    for ir,chi in CHAR_TABLE.items():
        val=sum(CLASS_SIZE[ct]*chars[ct]*chi[ct] for ct in CLASS_SIZE)/24.0
        mult[ir]=int(round(val))
        assert abs(val-mult[ir])<2e-8,(s2,ir,val)
    dim=sum(mult[ir]*CHAR_TABLE[ir][(1,1,1,1)] for ir in mult)
    assert dim==s2+1,(s2,dim)
    return {
        "s2":s2,
        "j":s2/2,
        "singlet_dimension":s2+1,
        "characters":{str(k):v for k,v in chars.items()},
        "character_class_spread_max":max(spread.values()),
        "multiplicities":mult,
        "logical_22_multiplicity":mult["[2,2]"],
    }


def projector_22(s2:int):
    d=s2+1
    P=np.zeros((d,d),dtype=complex)
    # Central idempotent P_lambda=d_lambda/|G| sum chi_lambda(g)^* U(g)
    for p in PERMS:
        ct=J1.cycle_type(p)
        P += CHAR_TABLE["[2,2]"][ct]*J1.permutation_matrix(s2,p)
    P *= 2/24
    P=(P+P.conj().T)/2
    ev=np.linalg.eigvalsh(P).real
    return P,ev


def run(s2_max=8):
    rows=[]
    for s2 in range(1,s2_max+1):
        row=decompose(s2)
        P,ev=projector_22(s2)
        rank=int(np.sum(ev>0.5))
        row["P22_rank"]=rank
        row["P22_projector_error"]=float(np.linalg.norm(P@P-P))
        row["P22_eigenvalues"]=[float(x) for x in ev]
        rows.append(row)
    unique_all=all(r["logical_22_multiplicity"]==1 for r in rows)
    return {
        "status":"S4 equal-spin refinement carrier scan",
        "passed":bool(unique_all and all(r["P22_rank"]==2 for r in rows)),
        "s2_max":s2_max,
        "rows":rows,
        "theorem_tested":"multiplicity of S4 [2,2] in Inv_SU2(V_j^⊗4) across equal-spin j",
        "conclusion":(
            "The [2,2] logical geometry carrier is multiplicity-one at every tested equal-spin scale."
            if unique_all else
            "Multiplicity-one [2,2] fails at at least one tested scale; canonical RG chain requires refinement."
        ),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--s2-max",type=int,default=8)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run(a.s2_max)
    txt=json.dumps(out,indent=2)
    print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 2

if __name__=="__main__":
    raise SystemExit(main())
