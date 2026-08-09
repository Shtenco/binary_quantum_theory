#!/usr/bin/env python3
"""Classical real-Ashtekar-Barbero Lorentzian cancellation regression gate.

For random nondegenerate spatial triads and symmetric extrinsic curvature,
separate the homogeneous K^2 contribution of the Euclidean EEF constraint
from the Lorentzian correction.  With A=Gamma+beta K and derivative terms
switched off, F(A)=beta^2 K wedge K.  The two beta-dependent pieces must add
to the ADM/DeWitt kinetic form independently of real beta.

This is an exact classical target for a future finite Peter-Weyl quantum
operator.  It is not itself a quantum constraint or HDA calculation.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import numpy as np


def levi3():
    e=np.zeros((3,3,3),float)
    for p in itertools.permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        e[p]=-1.0 if inv%2 else 1.0
    return e

EPS=levi3()


def sample(rng):
    for _ in range(1000):
        e=np.eye(3)+0.35*rng.normal(size=(3,3))
        if np.linalg.det(e)>0.15 and np.linalg.cond(e)<12:
            break
    else:
        raise RuntimeError("failed to generate a nondegenerate triad")
    K=rng.normal(size=(3,3)); K=0.5*(K+K.T)
    return e,K


def pieces(e,K,beta):
    # e[a,i] is a co-triad.  q_ab=e_a^i e_b^i.
    q=e@e.T; qi=np.linalg.inv(q); sqrtq=float(np.linalg.det(e))
    einv=np.linalg.inv(e).T          # e^a_i
    E=sqrtq*einv                    # densitized triad E^a_i
    Kai=K@einv                      # K_a^i=K_ab e^{bi}

    # Homogeneous curvature term of A=Gamma+beta K:
    # F_ab^k = beta^2 eps^k_lm K_a^l K_b^m.
    F=beta**2*np.einsum('klm,al,bm->abk',EPS,Kai,Kai)
    H_E=float(np.einsum('ijk,ai,bj,abk',EPS,E,E,F)/sqrtq)

    # -2(1+beta^2) E_i^[a E_j^b] K_a^i K_b^j / sqrt(q).
    term1=float(np.einsum('ai,bj,ai,bj->',E,E,Kai,Kai))
    term2=float(np.einsum('bi,aj,ai,bj->',E,E,Kai,Kai))
    H_L=float(-(1.0+beta**2)*(term1-term2)/sqrtq)

    Kup=qi@K@qi
    K2=float(np.einsum('ab,ab->',K,Kup))
    trK=float(np.einsum('ab,ab->',qi,K))
    H_DW=float(sqrtq*(K2-trK**2))
    return H_E,H_L,H_DW


def run(seed=260809,trials=64,betas=(0.0,0.2,1/np.sqrt(3),1.0,2.0,5.0)):
    rng=np.random.default_rng(seed)
    rows=[]; max_cancel=0.0; max_euclid=0.0; max_lor=0.0
    for t in range(trials):
        e,K=sample(rng)
        for beta in betas:
            HE,HL,HDW=pieces(e,K,float(beta))
            scale=max(abs(HDW),1e-14)
            cancel=abs(HE+HL-HDW)/scale
            # Exact coefficient targets: HE=-beta^2 HDW; HL=(1+beta^2) HDW.
            eu=abs(HE+beta**2*HDW)/scale
            lo=abs(HL-(1+beta**2)*HDW)/scale
            max_cancel=max(max_cancel,cancel);max_euclid=max(max_euclid,eu);max_lor=max(max_lor,lo)
            if t<3:
                rows.append({"trial":t,"beta":float(beta),"H_E_kin":HE,"H_L_corr":HL,"H_DeWitt":HDW,"relative_cancellation_error":cancel})
    passed=max(max_cancel,max_euclid,max_lor)<2e-11
    return {
        "status":"exact classical Lorentzian beta-cancellation target",
        "passed":bool(passed),
        "seed":seed,
        "trials":trials,
        "betas":[float(x) for x in betas],
        "max_relative_errors":{
            "HE_plus_beta2_HDW":float(max_euclid),
            "HL_minus_1plusbeta2_HDW":float(max_lor),
            "HE_plus_HL_minus_HDW":float(max_cancel)
        },
        "identities":{
            "Euclidean_kinetic":"H_E^kin = - beta^2 H_DW",
            "Lorentzian_correction":"H_L^corr = (1+beta^2) H_DW",
            "full":"H_E^kin + H_L^corr = H_DW = sqrt(q)(K_ab K^ab - K^2)"
        },
        "sample_rows":rows,
        "microscopic_target":"At fixed coarse geometry, the finite quantum-link kinetic form must approach the same beta-independent DeWitt bilinear through cancellation between Euclidean-curvature and extrinsic-curvature sectors, while retaining inertia (5+,1-,3 gauge zeros) in flux variables.",
        "scope_note":"Derivative/spatial-curvature terms are deliberately absent here to isolate the Lorentzian kinetic coefficient. This is a classical identity/regression target, not a proof of the quantum Hamiltonian constraint or HDA closure."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--seed",type=int,default=260809)
    ap.add_argument("--trials",type=int,default=64)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args(); out=run(a.seed,a.trials); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__": raise SystemExit(main())
