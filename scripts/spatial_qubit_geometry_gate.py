#!/usr/bin/env python3
"""Exact canonical 3+1 geometry controls from spin-1/2 face qubits.

This script tests a Lorentzian-safe spatial route:

  4 face qubits --SU(2) Gauss closure--> 1 logical geometry qubit
      --> tetrahedral flux reconstruction --> Bell gluing.

It is a finite algebraic/control calculation. It does not define the full
microscopic topology-changing rule or prove a 3+1 continuum limit.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)
PAULI=[X,Y,Z]


def kron_all(ops):
    out=np.array([[1]],complex)
    for op in ops:
        out=np.kron(out,op)
    return out


def one_site(op,site,n=4):
    return kron_all([op if q==site else I2 for q in range(n)])


def logical_basis():
    z=np.array([1,0],complex); o=np.array([0,1],complex)
    s=(np.kron(z,o)-np.kron(o,z))/math.sqrt(2)
    L0=np.kron(s,s)
    tp=np.kron(z,z); t0=(np.kron(z,o)+np.kron(o,z))/math.sqrt(2); tm=np.kron(o,o)
    L1=(np.kron(tp,tm)-np.kron(t0,t0)+np.kron(tm,tp))/math.sqrt(3)
    return np.column_stack([L0,L1])


def quantum_geometry_exact():
    J=np.empty((4,3),dtype=object)
    for i in range(4):
        for a,p in enumerate(PAULI):
            J[i,a]=0.5*one_site(p,i)
    Jtot=[sum((J[i,a] for i in range(4)),np.zeros((16,16),complex)) for a in range(3)]
    G2=sum((g@g for g in Jtot),np.zeros((16,16),complex))
    eig=np.linalg.eigvalsh(G2)
    vals,counts=np.unique(np.round(eig,12),return_counts=True)
    B=logical_basis()

    def pair(i,j):
        return sum((J[i,a]@J[j,a] for a in range(3)),np.zeros((16,16),complex))
    eps=np.zeros((3,3,3),int)
    for p in itertools.permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        eps[p]=-1 if inv%2 else 1
    Q=np.zeros((16,16),complex)
    for a,b,c in itertools.product(range(3),repeat=3):
        Q+=eps[a,b,c]*(J[0,a]@J[1,b]@J[2,c])

    K12=B.conj().T@pair(0,1)@B
    K13=B.conj().T@pair(0,2)@B
    QL=B.conj().T@Q@B
    targets={
        "K12":-0.25*I2-0.5*Z,
        "K13":-0.25*I2+0.25*Z-math.sqrt(3)/4*X,
        "Q":math.sqrt(3)/4*Y,
    }
    errors={
        "K12":float(np.linalg.norm(K12-targets["K12"])),
        "K13":float(np.linalg.norm(K13-targets["K13"])),
        "Q":float(np.linalg.norm(QL-targets["Q"])),
    }
    return {
        "Gauss_G2_spectrum":[[float(v),int(c)] for v,c in zip(vals,counts)],
        "singlet_dimension":int(np.sum(np.abs(eig)<1e-10)),
        "logical_operator_errors":errors,
        "oriented_volume_eigenvalues":np.linalg.eigvalsh(QL).tolist(),
    }


def face_vectors(vertices):
    v0,v1,v2,v3=np.asarray(vertices,float)
    a=v1-v0; b=v2-v0; c=v3-v0
    E1=0.5*np.cross(b,c)
    E2=0.5*np.cross(c,a)
    E3=0.5*np.cross(a,b)
    E0=-(E1+E2+E3)
    return np.array([E0,E1,E2,E3]),np.column_stack([a,b,c])


def reconstruct_edges(E):
    C=np.column_stack([2*E[1],2*E[2],2*E[3]])
    detC=float(np.linalg.det(C))
    if abs(detC)<1e-14:
        raise ValueError("degenerate flux triple")
    detA=math.sqrt(abs(detC))
    return detA*np.linalg.inv(C).T


def closure_defect(E):
    return float(np.linalg.norm(E.sum(axis=0))/max(np.linalg.norm(E),1e-30))


def gram_shape(A):
    G=A.T@A
    return G/(abs(np.linalg.det(G))**(1/3))


def metric_shape_error(Arec,A):
    return float(np.linalg.norm(gram_shape(Arec)-gram_shape(A))/np.linalg.norm(gram_shape(A)))


def rho_from_vec(v,scale):
    r=np.asarray(v,float)/scale
    if np.linalg.norm(r)>1+1e-12:
        raise ValueError("Bloch vector outside unit ball")
    return 0.5*(I2+sum((r[i]*PAULI[i] for i in range(3)),np.zeros((2,2),complex)))


def vec_from_rho(rho,scale):
    return scale*np.array([np.trace(rho@p).real for p in PAULI])


def tetra_controls(seed=260809,trials=100):
    rng=np.random.default_rng(seed)
    exact=[]
    for _ in range(trials):
        while True:
            V=rng.normal(size=(4,3))
            E,A=face_vectors(V)
            if np.linalg.det(A)>0.2 and np.linalg.cond(A)<12:
                break
        scale=1.01*max(np.linalg.norm(E,axis=1))
        rhos=[rho_from_vec(e,scale) for e in E]
        Ed=np.array([vec_from_rho(r,scale) for r in rhos])
        Ar=reconstruct_edges(Ed)
        exact.append((closure_defect(Ed),metric_shape_error(Ar,A)))

    noise_rows=[]
    for sig in (1e-5,1e-4,1e-3,1e-2):
        cd=[]; ge=[]
        for _ in range(trials):
            while True:
                V=rng.normal(size=(4,3)); E,A=face_vectors(V)
                if np.linalg.det(A)>0.2 and np.linalg.cond(A)<12: break
            s=max(np.linalg.norm(E,axis=1))
            En=E+sig*s*rng.normal(size=E.shape)
            cd.append(closure_defect(En))
            ge.append(metric_shape_error(reconstruct_edges(En),A))
        noise_rows.append({"relative_noise":sig,"mean_closure_defect":float(np.mean(cd)),"mean_shape_error":float(np.mean(ge))})
    return {
        "trials":trials,
        "max_exact_closure_defect":float(max(x[0] for x in exact)),
        "max_exact_shape_error":float(max(x[1] for x in exact)),
        "noise":noise_rows,
    }


def triangle_shape(tri):
    tri=np.asarray(tri,float)
    l=[]
    for i,j in ((0,1),(1,2),(2,0)):
        l.append(float(np.linalg.norm(tri[j]-tri[i])**2))
    a=np.sort(np.asarray(l))
    return a/a.sum()


def gluing_controls():
    phi=np.array([1,0,0,1],complex)/math.sqrt(2)
    H=-(np.kron(X,X)-np.kron(Y,Y)+np.kron(Z,Z))
    spectrum=np.linalg.eigvalsh(H)
    corr={
        "XX":float(np.vdot(phi,np.kron(X,X)@phi).real),
        "YY":float(np.vdot(phi,np.kron(Y,Y)@phi).real),
        "ZZ":float(np.vdot(phi,np.kron(Z,Z)@phi).real),
    }
    T1=np.array([[0.,0,0],[1.,0,0],[0.2,0.8,0]])
    T2=np.array([[0.,0,0],[2.,0,0],[0.1,0.4,0]])
    area1=0.5*np.linalg.norm(np.cross(T1[1]-T1[0],T1[2]-T1[0]))
    area2=0.5*np.linalg.norm(np.cross(T2[1]-T2[0],T2[2]-T2[0]))
    twist=float(np.linalg.norm(triangle_shape(T1)-triangle_shape(T2)))
    return {
        "bell_correlations":corr,
        "H_glue_J1_spectrum":spectrum.tolist(),
        "gluing_gap":float(spectrum[1]-spectrum[0]),
        "twisted_geometry_negative_control":{
            "shared_face_area_1":float(area1),
            "shared_face_area_2":float(area2),
            "area_match_error":float(abs(area1-area2)),
            "shape_match_defect":twist,
        },
    }


def run(seed=260809,trials=100):
    q=quantum_geometry_exact(); t=tetra_controls(seed,trials); g=gluing_controls()
    passed=(q["singlet_dimension"]==2 and max(q["logical_operator_errors"].values())<1e-12 and
            t["max_exact_closure_defect"]<1e-12 and t["max_exact_shape_error"]<1e-12 and
            abs(g["gluing_gap"]-4.0)<1e-12 and g["twisted_geometry_negative_control"]["shape_match_defect"]>0.1)
    return {
        "status":"finite canonical qubit->3D quantum-geometry control",
        "passed":bool(passed),
        "quantum_cell":q,
        "tetrahedron_reconstruction":t,
        "gluing":g,
        "dimension_principle":"conditional: dim_R su(2)=3 supplies spatial flux-normal space; causal rewrite time must independently satisfy z->1 to yield 3+1",
        "scope_note":"No frozen topology-changing microscopic rule, Lorentzian Hamiltonian-constraint closure, or continuum limit is proved here."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--seed",type=int,default=260809)
    ap.add_argument("--trials",type=int,default=100)
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    out=run(args.seed,args.trials)
    txt=json.dumps(out,ensure_ascii=False,indent=2)
    print(txt)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__":
    raise SystemExit(main())
