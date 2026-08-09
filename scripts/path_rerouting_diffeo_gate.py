#!/usr/bin/env python3
"""Minimal gauge-covariant path/rerouting register for an embedded-LQG route.

Two coarse routes connect the same endpoints through a plaquette/diamond,

    p_A: 0 -> 1 -> 2
    p_B: 0 -> 3 -> 2.

Their holonomies transform with exactly the same endpoint frames, while the
relative route holonomy C=h_B h_A^dag transforms by conjugation at the start
vertex.  A separate two-state path qubit can therefore be flipped/rotated
without changing the SU(2) representation carried at the endpoints.

The path qubit is a gauge/embedding/rerouting register, not the tetrahedral
geometry qubit.  It is the minimal extra variable needed if one wants the
canonical diffeomorphism to act by actual edge rerouting rather than only by an
intrinsic Regge-effective transformation of spin/shape data.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)
SIG=(X,Y,Z)


def random_su2(rng):
    q=rng.normal(size=4);q/=np.linalg.norm(q)
    return q[0]*I2+1j*(q[1]*X+q[2]*Y+q[3]*Z)


def run(seed=260809,samples=1000):
    rng=np.random.default_rng(seed)
    max_endpoint_covariance_error=0.0
    max_loop_trace_error=0.0
    for _ in range(samples):
        U01,U12,U03,U32=[random_su2(rng) for _ in range(4)]
        g=[random_su2(rng) for _ in range(4)]
        hA=U01@U12
        hB=U03@U32
        U01p=g[0]@U01@g[1].conj().T
        U12p=g[1]@U12@g[2].conj().T
        U03p=g[0]@U03@g[3].conj().T
        U32p=g[3]@U32@g[2].conj().T
        hAp=U01p@U12p
        hBp=U03p@U32p
        max_endpoint_covariance_error=max(
            max_endpoint_covariance_error,
            float(np.linalg.norm(hAp-g[0]@hA@g[2].conj().T)),
            float(np.linalg.norm(hBp-g[0]@hB@g[2].conj().T)))
        C=hB@hA.conj().T
        Cp=hBp@hAp.conj().T
        max_loop_trace_error=max(max_loop_trace_error,float(abs(np.trace(Cp)-np.trace(C))))

    # Continuous unitary on the path qubit.  A refined path is moved by local
    # plaquette reroutings; this two-state block is the elementary carrier.
    max_reroute_unitarity=0.0
    for theta in np.linspace(-3.0,3.0,31):
        R=math.cos(theta/2)*I2-1j*math.sin(theta/2)*Y
        max_reroute_unitarity=max(max_reroute_unitarity,float(np.linalg.norm(R.conj().T@R-I2)))

    # Small-curvature route difference regression: h_A=I,
    # h_B=exp(i eps Z/2).  The relative loop trace is 2 cos(eps/2), and
    # ||h_B-h_A||_F = 2 sqrt(2) |sin(eps/4)|.
    max_small_curvature_error=0.0
    for eps in np.geomspace(1e-5,0.5,30):
        hB=math.cos(eps/2)*I2+1j*math.sin(eps/2)*Z
        tr=float(np.trace(hB).real)
        diff=float(np.linalg.norm(hB-I2))
        max_small_curvature_error=max(
            max_small_curvature_error,
            abs(tr-2*math.cos(eps/2)),
            abs(diff-2*math.sqrt(2)*abs(math.sin(eps/4))))

    # Exact combinatorial fact: Aut(K5)=S5 has 5!=120 elements.  Any continuous
    # homomorphism from a connected one-parameter diffeomorphism subgroup into
    # this finite/discrete group has constant image.  Thus abstract relabeling
    # alone cannot carry a nontrivial infinitesimal D generator.
    automorphism_count=math.factorial(5)

    passed=(max_endpoint_covariance_error<1e-12
            and max_loop_trace_error<1e-12
            and max_reroute_unitarity<1e-12
            and max_small_curvature_error<1e-12
            and automorphism_count==120)
    return {
      'status':'gauge-covariant path/rerouting register','passed':bool(passed),
      'samples':samples,'seed':seed,
      'max_endpoint_covariance_error':max_endpoint_covariance_error,
      'max_relative_loop_trace_gauge_error':max_loop_trace_error,
      'max_path_qubit_unitarity_error':max_reroute_unitarity,
      'max_small_curvature_identity_error':max_small_curvature_error,
      'K5_automorphism_count':automorphism_count,
      'exact_group_theory_note':(
        'A model in which connected spatial diffeomorphisms act only by K5 '
        'combinatorial automorphisms has a trivial connected action because '
        'Aut(K5)=S5 is finite/discrete. A nontrivial exact embedded-LQG D action '
        'therefore needs path/embedding/rerouting data (or a different intrinsic '
        'Regge-effective representation of D).'
      ),
      'scope_note':(
        'Kinematic gauge/path gate only. It does not define the Hamiltonian '
        'constraint or prove HDA closure. The path qubit is gauge/rerouting data, '
        'not an additional physical graviton degree of freedom.'
      )
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--samples',type=int,default=1000);ap.add_argument('--seed',type=int,default=260809);ap.add_argument('--output',type=Path);a=ap.parse_args()
    out=run(a.seed,a.samples);txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
