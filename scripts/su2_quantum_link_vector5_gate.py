#!/usr/bin/env python3
"""Exact five-state SO(5) vector SU(2) quantum-link representation.

The representation decomposes under SU(2)_L x SU(2)_R as
    5 = (2,2) + (1,1).
The rank-4 bi-doublet is interpreted as an active geometric spin-1/2 link and
the singlet as an inactive/defect link state. The quantum transporter toggles
between these sectors exactly.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import numpy as np
I2=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.array([[1,0],[0,-1]],complex);SIG=[X,Y,Z]

def eps3():
    e=np.zeros((3,3,3),int)
    for p in itertools.permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3));e[p]=-1 if inv%2 else 1
    return e
EPS=eps3()

def M(a,b):
    if a==b:return np.zeros((5,5),complex)
    if a>b:return -M(b,a)
    A=np.zeros((5,5),complex);A[a,b]=1;A[b,a]=-1
    return -1j*A

def build():
    J=[]
    for a in range(3):
        op=np.zeros((5,5),complex)
        for b in range(3):
            for c in range(3):op+=0.5*EPS[a,b,c]*M(b,c)
        J.append(op)
    K=[M(a,3) for a in range(3)]
    L=[0.5*(J[a]+K[a]) for a in range(3)];R=[0.5*(J[a]-K[a]) for a in range(3)]
    U0=M(3,4);Ua=[M(a,4) for a in range(3)]
    U=np.empty((2,2),dtype=object)
    for i in range(2):
        for j in range(2):
            op=(1 if i==j else 0)*U0
            for a in range(3):op=op+1j*SIG[a][i,j]*Ua[a]
            U[i,j]=op
    return L,R,U

def run():
    L,R,U=build();CL=sum(x@x for x in L);CR=sum(x@x for x in R);Pg=(4/3)*CL;Ps=np.eye(5)-Pg
    su=lambda A:max(np.linalg.norm(A[a]@A[b]-A[b]@A[a]-1j*sum(EPS[a,b,c]*A[c] for c in range(3))) for a in range(3) for b in range(3))
    lr=max(np.linalg.norm(L[a]@R[b]-R[b]@L[a]) for a in range(3) for b in range(3))
    toggle=[]
    comps=[M(3,4)]+[M(a,4) for a in range(3)]
    for u in comps:toggle.append({"PgUPg":float(np.linalg.norm(Pg@u@Pg)),"PsUPs":float(np.linalg.norm(Ps@u@Ps)),"PgUPs":float(np.linalg.norm(Pg@u@Ps)),"PsUPg":float(np.linalg.norm(Ps@u@Pg))})
    passed=su(L)<1e-12 and su(R)<1e-12 and lr<1e-12 and np.linalg.norm(Pg@Pg-Pg)<1e-12 and all(x["PgUPg"]<1e-12 and x["PsUPs"]<1e-12 and abs(x["PgUPs"]-1)<1e-12 and abs(x["PsUPg"]-1)<1e-12 for x in toggle)
    return {"status":"exact five-state SO(5) vector quantum link","passed":bool(passed),"hilbert_dimension":5,"decomposition":"(2,2) + (1,1)","left_Casimir_spectrum":np.linalg.eigvalsh(CL).tolist(),"right_Casimir_spectrum":np.linalg.eigvalsh(CR).tolist(),"geometric_projector_eigenvalues":np.linalg.eigvalsh(Pg).tolist(),"transporter_sector_blocks":toggle,"interpretation":"The four-dimensional bi-doublet supplies spin-1/2 at both link endpoints; the fifth state is a gauge singlet. Every transporter component toggles active geometric link <-> singlet defect exactly.","binary_encoding_note":"A generic 5-state code needs 3 qubits, while the natural two-rishon construction starts from four binary fermionic occupation modes and selects the SO(5) vector subspace."}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+"\n",encoding="utf-8")
    return 0 if o["passed"] else 1
if __name__=="__main__":raise SystemExit(main())
