#!/usr/bin/env python3
"""Exact finite SU(2) quantum-link curvature/volume composability test.

Two four-valent nodes are connected by four parallel minimal SO(5)-spinor
quantum links.  The full 4^4=256 Hilbert space is projected by exact left/right
Gauss constraints.  A gauge-invariant two-link Wilson loop is then tested
against node occupancy/volume sectors.

The multigraph is an algebraic stress test, not a spatial triangulation.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
from su2_quantum_link_two_qubit_gate import build


def emb(op,l,n=4):
    out=np.array([[1]],complex); I4=np.eye(4)
    for m in range(n):out=np.kron(out,op if m==l else I4)
    return out


def run():
    L,R,U=build(); n=4; D=4**n
    LE=[[emb(L[a],l) for a in range(3)] for l in range(n)]
    RE=[[emb(R[a],l) for a in range(3)] for l in range(n)]
    UE=[]
    for l in range(n):
        um=np.empty((2,2),dtype=object)
        for i in range(2):
            for j in range(2):um[i,j]=emb(U[i,j],l)
        UE.append(um)

    G2=np.zeros((D,D),complex)
    GL=[];GR=[]
    for a in range(3):
        gl=sum((LE[l][a] for l in range(n)),np.zeros((D,D),complex))
        gr=sum((RE[l][a] for l in range(n)),np.zeros((D,D),complex))
        GL.append(gl);GR.append(gr);G2+=gl@gl+gr@gr
    ev,B=np.linalg.eigh(G2); phys=np.abs(ev)<1e-9; P=B[:,phys]

    # Left endpoint occupancy on one link is 4/3 L^2: eigenvalues 0 or 1.
    K=np.zeros((D,D),complex)
    for l in range(n):
        cas=sum((LE[l][a]@LE[l][a] for a in range(3)),np.zeros((D,D),complex))
        K+=(4/3)*cas
    Kp=P.conj().T@K@P
    kv,Q=np.linalg.eigh(Kp)
    projectors={}
    for k in (0,2,4):
        mask=np.abs(kv-k)<1e-8
        projectors[k]=Q[:,mask]@Q[:,mask].conj().T

    # Closed two-link loop: go left->right on link0 and right->left on link1.
    W=np.zeros((D,D),complex)
    for i in range(2):
        for j in range(2):W+=UE[0][i,j]@UE[1][i,j].conj().T
    gauge=max(np.linalg.norm(g@W-W@g) for g in GL+GR)
    Wp=P.conj().T@W@P

    blocks={}
    for k in (0,2,4):
        blocks[str(k)]={}
        for kp in (0,2,4):
            blocks[str(k)][str(kp)]=float(np.linalg.norm(projectors[kp]@Wp@projectors[k]))

    VL=projectors[4]; VR=projectors[0]; VT=VL+VR
    data={}
    for name,V in (("left_volume",VL),("right_volume",VR),("total_nondegenerate_volume",VT)):
        C=Wp@V-V@Wp; H=1j*C
        data[name]={"commutator_norm":float(np.linalg.norm(C)),"commutator_rank":int(np.linalg.matrix_rank(C,1e-10)),"i_commutator_spectrum":np.linalg.eigvalsh(H).tolist()}

    ggap=float(np.min(ev[~phys]))
    passed=(int(np.sum(phys))==10 and abs(ggap-1.5)<1e-10 and gauge<1e-12 and
            abs(data["total_nondegenerate_volume"]["commutator_norm"]-4)<1e-10)
    return {"status":"exact finite curvature-volume quantum-link gate","passed":bool(passed),"full_hilbert_dimension":D,"Gauss_physical_dimension":int(np.sum(phys)),"Gauss_penalty_gap":ggap,"left_occupancy_spectrum":np.linalg.eigvalsh(Kp).tolist(),"Wilson_gauge_commutator_max":float(gauge),"Wilson_sector_block_norms":blocks,"volume_commutators":data,"interpretation":"The minimal finite quantum-link truncation does not kill volume-changing curvature dynamics: the gauge-invariant loop connects k=0<->2<->4 singlet sectors and has a nonzero commutator with the nondegenerate-volume projector.","scope_note":"The two-node four-parallel-link graph is an algebraic control, not a continuum spatial geometry or a full Hamiltonian-constraint test."}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);a=ap.parse_args();out=run();txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1
if __name__=="__main__":raise SystemExit(main())
