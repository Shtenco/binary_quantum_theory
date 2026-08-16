#!/usr/bin/env python3
"""Exact first BCQG collective blocking map: two spin-1/2 qubits per face -> j=1.

Construct the symmetric triplet isometry W_face, its four-face node tensor W,
and verify W^dagger W=I, exact SU(2) flux intertwining, zero symmetric-subspace
leakage, Gauss compression, oriented-volume compression, and equality of the
gauge-invariant j=1 volume spectrum in microscopic and direct constructions.

This is a kinematic/operator blocking result, not yet a compressed H/D/H algebra.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np


def spin_matrices(j):
    m=np.arange(j,-j-1,-1,dtype=float); d=len(m)
    Jz=np.diag(m); Jp=np.zeros((d,d),complex)
    for col,mm in enumerate(m):
        if mm+1<=j and col>0:
            Jp[col-1,col]=math.sqrt(j*(j+1)-mm*(mm+1))
    Jm=Jp.conj().T
    return [(Jp+Jm)/2,(Jp-Jm)/(2j),Jz]


def kron_all(xs):
    z=np.array([[1]],complex)
    for x in xs:
        z=np.kron(z,x)
    return z


def embed(op,site,d,n):
    I=np.eye(d)
    return kron_all([op if i==site else I for i in range(n)])


def eps3(a,b,c):
    if len({a,b,c})<3:
        return 0
    p=(a,b,c)
    inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else 1


def run(tol=2e-12):
    h=spin_matrices(.5); one=spin_matrices(1.0)
    s2=1/math.sqrt(2)
    Wf=np.array([[1,0,0],[0,s2,0],[0,s2,0],[0,0,1]],complex)
    If=np.eye(4); Pf=Wf@Wf.conj().T
    face_rows=[]; max_inter=max_leak=0.0
    for a in range(3):
        Jm=np.kron(h[a],np.eye(2))+np.kron(np.eye(2),h[a])
        inter=np.linalg.norm(Wf.conj().T@Jm@Wf-one[a])
        leak=np.linalg.norm((If-Pf)@Jm@Wf)
        max_inter=max(max_inter,float(inter)); max_leak=max(max_leak,float(leak))
        face_rows.append({'axis':a,'intertwining_defect':float(inter),'leakage':float(leak)})

    W=kron_all([Wf]*4)  # 256 x 81
    iso=np.linalg.norm(W.conj().T@W-np.eye(81))

    Jc=np.empty((4,3),dtype=object)
    for f in range(4):
        for a in range(3):
            Jc[f,a]=embed(one[a],f,3,4)

    Jq=np.empty((4,3),dtype=object)
    for f in range(4):
        for a in range(3):
            Jq[f,a]=embed(h[a],2*f,2,8)+embed(h[a],2*f+1,2,8)

    flux_def=0.0; flux_leak=0.0
    P=W@W.conj().T; I256=np.eye(256)
    for f in range(4):
        for a in range(3):
            flux_def=max(flux_def,float(np.linalg.norm(W.conj().T@Jq[f,a]@W-Jc[f,a])))
            flux_leak=max(flux_leak,float(np.linalg.norm((I256-P)@Jq[f,a]@W)))

    Gc=sum((sum((Jc[f,a] for f in range(4)),np.zeros((81,81),complex)) @
            sum((Jc[f,a] for f in range(4)),np.zeros((81,81),complex))
            for a in range(3)),np.zeros((81,81),complex))
    Gq=sum((sum((Jq[f,a] for f in range(4)),np.zeros((256,256),complex)) @
            sum((Jq[f,a] for f in range(4)),np.zeros((256,256),complex))
            for a in range(3)),np.zeros((256,256),complex))
    gauss_def=float(np.linalg.norm(W.conj().T@Gq@W-Gc))

    Qc=np.zeros((81,81),complex); Qq=np.zeros((256,256),complex)
    for a,b,c in itertools.product(range(3),repeat=3):
        e=eps3(a,b,c)
        if not e:
            continue
        Qc += e*(Jc[0,a]@Jc[1,b]@Jc[2,c])
        Qq += e*(Jq[0,a]@Jq[1,b]@Jq[2,c])
    q_def=float(np.linalg.norm(W.conj().T@Qq@W-Qc))
    q_leak=float(np.linalg.norm((I256-P)@Qq@W))

    eg,B=np.linalg.eigh(Gc)
    sing=B[:,np.abs(eg)<1e-9]
    Qsing=sing.conj().T@Qc@sing
    Qsing=.5*(Qsing+Qsing.conj().T)
    qspec=np.linalg.eigvalsh(Qsing)
    vspec=np.sqrt(np.abs(qspec))
    Wg=W@sing
    micro_gauss_res=float(np.linalg.norm(Gq@Wg))
    micro_Q=Wg.conj().T@Qq@Wg
    gauge_q_def=float(np.linalg.norm(micro_Q-Qsing))

    passed=max(iso,max_inter,max_leak,flux_def,flux_leak,gauss_def,
               q_def,q_leak,micro_gauss_res,gauge_q_def)<tol and sing.shape[1]==3
    return {
      'status':'exact first collective j=1 block isometry',
      'passed':bool(passed),'tolerance':tol,
      'micro_qubits_per_face':2,'micro_qubits_per_node':8,
      'collective_face_spin':1.0,'collective_node_full_dimension':81,
      'microscopic_node_dimension':256,
      'collective_Gauss_intertwiner_dimension':int(sing.shape[1]),
      'W_node_isometry_defect':float(iso),'face_rows':face_rows,
      'max_node_flux_intertwining_defect':flux_def,
      'max_node_flux_leakage':flux_leak,
      'Gauss_Casimir_compression_defect':gauss_def,
      'oriented_volume_Q_compression_defect':q_def,
      'oriented_volume_Q_leakage':q_leak,
      'microscopic_Gauss_residual_on_blocked_singlet':micro_gauss_res,
      'gauge_volume_block_defect':gauge_q_def,
      'oriented_Q_spectrum_on_collective_singlet':qspec.tolist(),
      'absolute_volume_spectrum_up_to_scale':vspec.tolist(),
      'next_required_step':'Use this exact W_1 as the first boundary block map for compressed BCQG G,D,H and report operator leakage before any GR-target comparison.',
      'scope_note':'Exact kinematic/volume blocking only; no claim yet about collective HDA, DeWitt coefficient, constraint rank, or two graviton modes.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--tol',type=float,default=2e-12)
    a=ap.parse_args(); o=run(a.tol); t=json.dumps(o,indent=2); print(t)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
