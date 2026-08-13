#!/usr/bin/env python3
"""Off-shell quantum-HDA killer gate for the current BCQG architecture.

The RHS of the desired algebra is already fixed independently by
  omega=N dM-M dN -> sharp_Eq(omega) -> D_path[beta].

This script composes the existing exact/finite RHS, path and Lorentzian gates,
then proves a structural no-go for any Hamiltonian that still factorises as

    H = H_geometry tensor I_path.

For nonconstant lapses D_path is nontrivial, whereas every commutator of such
factorised Hamiltonians is proportional to I_path. Therefore increasing the
Peter-Weyl cutoff cannot repair the off-shell HDA until controlled path
rerouting is part of H itself.

The script is a successful falsifier/architecture gate. It does NOT claim that
the full route-coupled Lorentzian Hamiltonian has already been constructed.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

from scripts.dual_k5_lapse_cochain_gate import run as run_cochain
from scripts.dual_cell_sharp_rt0_gate import run as run_sharp
from scripts.path_rerouting_diffeo_gate import run as run_reroute
from scripts.path_vector_diffeo_gate import run as run_path_lie
from scripts.lorentzian_beta_cancellation_gate import run as run_beta
from scripts.lorentzian_hit_depth_bound import run as run_wall


def centered(f,axis,a):
    return (np.roll(f,-1,axis=axis)-np.roll(f,1,axis=axis))/(2*a)


def path_factor_no_go(L=96):
    """Explicit nonconstant-lapse witness in a flat local sharp frame."""
    x=2*np.pi*np.arange(L)/L;X,Y=np.meshgrid(x,x,indexing="ij");a=2*np.pi/L
    N=np.sin(X)+0.17*np.cos(Y)
    M=np.sin(Y)+0.11*np.cos(X)
    dNx=np.cos(X);dNy=-0.17*np.sin(Y)
    dMx=-0.11*np.sin(X);dMy=np.cos(Y)
    # flat local q^{ab}: beta^a=N d^a M-M d^a N
    bx=N*dMx-M*dNx;by=N*dMy-M*dNy
    f=np.exp(1j*(2*X-Y))+0.31*np.cos(X+Y)
    rhs=bx*centered(f,0,a)+by*centered(f,1,a)
    rhs_norm=float(np.linalg.norm(rhs))
    # Path-traceless/proper-derivative component of C_geom tensor I_path is zero.
    lhs_path_component=np.zeros_like(rhs)
    residual=float(np.linalg.norm(lhs_path_component-rhs)/max(rhs_norm,1e-30))
    return {
      "L":L,"rhs_D_path_norm":rhs_norm,
      "factorized_lhs_path_component_norm":0.0,
      "normalized_path_channel_residual":residual,
      "nontrivial_rhs":bool(rhs_norm>1e-8),
      "exact_reason":"[H_g tensor I_p,H_g tensor I_p]=C_g tensor I_p has zero path-derivative component, while D_path[sharp(NdM-MdN)] is nonzero for this off-shell lapse pair."
    }


def run():
    cochain=run_cochain(seed=260813,samples=64)
    sharp=run_sharp(seed=260813,samples=128)
    reroute=run_reroute(seed=260813,samples=128)
    path_lie=run_path_lie()
    beta=run_beta(seed=260813,trials=24)
    wall=run_wall()
    nogo=path_factor_no_go()

    prereq=all(bool(x.get("passed",False)) for x in (cochain,sharp,reroute,path_lie,beta,wall))
    no_go_pass=(nogo["nontrivial_rhs"] and abs(nogo["normalized_path_channel_residual"]-1.0)<1e-12)
    return {
      "status":"off-shell HDA structural killer",
      "regression_passed":bool(prereq and no_go_pass),
      "full_quantum_HDA_closed":False,
      "current_factorized_hamiltonian_ruled_out":bool(no_go_pass),
      "target":"(3/2){V,-i[H[N],H[M]]} -> hbar D_path[sharp_Eq(N dM-M dN)]",
      "prerequisites":{
        "dual_K5_cochain_pass":cochain["passed"],
        "dual_cell_sharp_pass":sharp["passed"],
        "gauge_covariant_rerouting_pass":reroute["passed"],
        "path_vector_Lie_pass":path_lie["passed"],
        "Lorentzian_beta_classical_pass":beta["passed"],
        "Peter_Weyl_wall_pass":wall["passed"],
        "safe_Jmax_bound":wall["sufficient_Jmax_for_full_Lorentzian_HH"]
      },
      "factorization_no_go":nogo,
      "minimal_required_extension":{
        "operator":"H_geom+route[N]",
        "must_do":"Each local Hamiltonian move must carry a gauge-covariant controlled path/rerouting action on the same cylindrical domain used by D_path.",
        "must_preserve":"Peter-Weyl gauge covariance, fixed Lorentzian (1+beta^2) coefficient, regulator-safe hit bound, and nontrivial off-shell lapse dependence.",
        "next_falsifier":"After route coupling is implemented, evaluate the preregistered densitized HH-D residual on nonconstant off-shell probes; group-averaged zero is not a pass."
      },
      "scientific_verdict":"The RHS and all kinematic/Lorentzian prerequisites are executable, but the present geometry-only Hamiltonian cannot satisfy the nontrivial path-valued HDA by a tensor-factor theorem. Full HDA remains OPEN until H itself reroutes paths."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output",type=Path)
    ap.add_argument("--require-closure",action="store_true",help="Return failure until the full route-coupled HDA is actually closed")
    a=ap.parse_args();out=run();txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+"\n",encoding="utf-8")
    if a.require_closure:return 0 if out["full_quantum_HDA_closed"] else 2
    return 0 if out["regression_passed"] else 1


if __name__=="__main__":raise SystemExit(main())
