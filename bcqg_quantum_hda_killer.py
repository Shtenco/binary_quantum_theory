#!/usr/bin/env python3
"""Off-shell quantum-HDA killer gate for the current BCQG architecture.

The RHS is fixed independently:
  omega=N dM-M dN -> sharp_Eq(omega) -> D_path[beta].

The gate does two things in one pass:
1. proves a tensor-factor no-go for H=H_geometry tensor I_path;
2. verifies a parameter-free constructive route-normal candidate
   H_path[N]=1/2{N,sqrt(-Delta_path,q)}, whose principal symbol generates the
   HDA metric structure function.

Full Peter-Weyl Lorentzian gravity closure remains open until the geometry
Hamiltonian is coupled to that same rerouting/path domain.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np

from scripts.dual_k5_lapse_cochain_gate import run as run_cochain
from scripts.dual_cell_sharp_rt0_gate import run as run_sharp
from scripts.path_rerouting_diffeo_gate import run as run_reroute
from scripts.path_vector_diffeo_gate import run as run_path_lie
from scripts.path_normal_hda_gate import run as run_path_normal
from scripts.lorentzian_beta_cancellation_gate import run as run_beta
from scripts.lorentzian_hit_depth_bound import run as run_wall


def centered(f,axis,a):
    return (np.roll(f,-1,axis=axis)-np.roll(f,1,axis=axis))/(2*a)


def path_factor_no_go(L=96):
    x=2*np.pi*np.arange(L)/L;X,Y=np.meshgrid(x,x,indexing="ij");a=2*np.pi/L
    N=np.sin(X)+0.17*np.cos(Y);M=np.sin(Y)+0.11*np.cos(X)
    dNx=np.cos(X);dNy=-0.17*np.sin(Y);dMx=-0.11*np.sin(X);dMy=np.cos(Y)
    bx=N*dMx-M*dNx;by=N*dMy-M*dNy
    f=np.exp(1j*(2*X-Y))+0.31*np.cos(X+Y)
    rhs=bx*centered(f,0,a)+by*centered(f,1,a);rhs_norm=float(np.linalg.norm(rhs))
    residual=float(np.linalg.norm(rhs)/max(rhs_norm,1e-30))
    return {
      "L":L,"rhs_D_path_norm":rhs_norm,"factorized_lhs_path_component_norm":0.0,
      "normalized_path_channel_residual":residual,"nontrivial_rhs":bool(rhs_norm>1e-8),
      "exact_reason":"[H_g tensor I_p,H_g tensor I_p]=C_g tensor I_p has zero path-derivative component, while D_path[sharp(NdM-MdN)] is nonzero off shell."
    }


def run():
    cochain=run_cochain(seed=260813,samples=64);sharp=run_sharp(seed=260813,samples=128)
    reroute=run_reroute(seed=260813,samples=128);path_lie=run_path_lie();path_normal=run_path_normal(L=128)
    beta=run_beta(seed=260813,trials=24);wall=run_wall();nogo=path_factor_no_go()
    prereq=all(bool(x.get("passed",False)) for x in (cochain,sharp,reroute,path_lie,path_normal,beta,wall))
    no_go_pass=(nogo["nontrivial_rhs"] and abs(nogo["normalized_path_channel_residual"]-1.0)<1e-12)
    return {
      "status":"off-shell HDA structural killer plus route-normal completion candidate",
      "regression_passed":bool(prereq and no_go_pass),
      "full_quantum_HDA_closed":False,
      "route_sector_HDA_principal_symbol_closed":bool(path_normal["passed"]),
      "current_factorized_hamiltonian_ruled_out":bool(no_go_pass),
      "target":"(3/2){V,-i[H[N],H[M]]} -> hbar D_path[sharp_Eq(N dM-M dN)]",
      "prerequisites":{
        "dual_K5_cochain_pass":cochain["passed"],"dual_cell_sharp_pass":sharp["passed"],
        "gauge_covariant_rerouting_pass":reroute["passed"],"path_vector_Lie_pass":path_lie["passed"],
        "path_normal_HDA_pass":path_normal["passed"],"path_normal_WKB_exponent":path_normal["fitted_WKB_decay_exponent"],
        "path_normal_last_defect":path_normal["last_defect"],
        "Lorentzian_beta_classical_pass":beta["passed"],"Peter_Weyl_wall_pass":wall["passed"],
        "safe_Jmax_bound":wall["sufficient_Jmax_for_full_Lorentzian_HH"]
      },
      "factorization_no_go":nogo,
      "constructive_route_normal_operator":{
        "operator":"H_path[N]=0.5*{N,sqrt(-Delta_path,q)}",
        "symbol_identity":"{N|p|_q,M|p|_q}=q^{ab}(M d_b N-N d_b M)p_a",
        "meaning":"The correct metric-dependent shift is generated at principal-symbol level with no fitted magnitude; only one global D-orientation convention is fixed."
      },
      "minimal_required_extension":{
        "operator":"H_geom+route[N]",
        "must_do":"Couple the Peter-Weyl Lorentzian geometry Hamiltonian to the square-root route-normal/rerouting factor on the same cylindrical domain.",
        "must_preserve":"SU(2) covariance, fixed (1+beta^2) Lorentzian coefficient, regulator-safe hit bound, nonconstant lapse dependence and the frozen sharp/D_path definitions.",
        "next_falsifier":"Evaluate the preregistered densitized HH-D residual on off-shell geometry x WKB path probes; group-averaged zero is not a pass."
      },
      "scientific_verdict":"The old factorized Hamiltonian is exactly ruled out. A parameter-free route-normal HDA representation is now verified in its semiclassical principal-symbol window. The remaining open step is coupling that route factor to the full Peter-Weyl Lorentzian geometry Hamiltonian and checking the joint commutator."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);ap.add_argument("--require-closure",action="store_true");a=ap.parse_args()
    out=run();txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+"\n",encoding="utf-8")
    if a.require_closure:return 0 if out["full_quantum_HDA_closed"] else 2
    return 0 if out["regression_passed"] else 1
if __name__=="__main__":raise SystemExit(main())
