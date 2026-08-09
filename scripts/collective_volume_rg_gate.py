#!/usr/bin/env python3
"""Gauge-invariant volume spectra for four equal collective SU(2) face spins.

Shows the exact obstruction at j=1/2 and the first collective scale j=1 at
which the absolute volume operator is no longer proportional to identity.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np


def spin_matrices(j: float):
    m=np.arange(j,-j-1,-1,dtype=float); d=len(m)
    Jz=np.diag(m); Jp=np.zeros((d,d),complex)
    for col,mm in enumerate(m):
        if mm+1<=j and col>0:
            Jp[col-1,col]=math.sqrt(j*(j+1)-mm*(mm+1))
    Jm=Jp.conj().T
    return [(Jp+Jm)/2,(Jp-Jm)/(2j),Jz]


def embed(op,site,d,n=4):
    out=np.array([[1]],complex); I=np.eye(d)
    for s in range(n): out=np.kron(out,op if s==site else I)
    return out


def spectrum(j: float):
    mats=spin_matrices(j); d=int(round(2*j+1)); D=d**4
    J=np.empty((4,3),dtype=object)
    for s in range(4):
        for a in range(3): J[s,a]=embed(mats[a],s,d)
    Jtot=[sum((J[s,a] for s in range(4)),np.zeros((D,D),complex)) for a in range(3)]
    G2=sum((x@x for x in Jtot),np.zeros((D,D),complex))
    ev,vec=np.linalg.eigh(G2); B=vec[:,np.abs(ev)<1e-8]
    eps=np.zeros((3,3,3),int)
    for p in itertools.permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        eps[p]=-1 if inv%2 else 1
    Q=np.zeros((D,D),complex)
    for a,b,c in itertools.product(range(3),repeat=3):
        Q += eps[a,b,c]*(J[0,a]@J[1,b]@J[2,c])
    QL=B.conj().T@Q@B
    q=np.linalg.eigvalsh(QL)
    v=np.sqrt(np.abs(q))
    return {
        "j":j,
        "microscopic_qubits_per_face_if_symmetric":int(round(2*j)),
        "intertwiner_dimension":int(B.shape[1]),
        "expected_dimension_2j_plus_1":int(round(2*j+1)),
        "oriented_Q_spectrum":q.tolist(),
        "absolute_volume_spectrum_up_to_scale":v.tolist(),
        "number_distinct_absolute_volumes":int(len(np.unique(np.round(v,10)))),
        "volume_is_scalar_on_intertwiner":bool(np.max(v)-np.min(v)<1e-10),
    }


def run():
    rows=[spectrum(j) for j in (0.5,1.0,1.5)]
    return {
        "status":"finite collective-volume RG control",
        "rows":rows,
        "minimal_nontrivial_volume_spin":1.0,
        "minimal_symmetric_micro_qubits_per_face":2,
        "conclusion":"j=1/2 has fixed absolute volume; j=1 is the first equal-spin four-valent intertwiner with nontrivial absolute-volume spectrum, so commutator-based gravity dynamics requires collective/representation growth beyond the microscopic single-qubit face sector."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); a=ap.parse_args()
    out=run(); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0

if __name__=="__main__": raise SystemExit(main())
