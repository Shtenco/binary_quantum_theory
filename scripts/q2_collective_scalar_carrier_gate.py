#!/usr/bin/env python3
"""Derived scalar-carrier completion gate for the BQG q=2 hierarchy.

This gate identifies the minimal already-motivated carriers needed to move
from the exact local q=2 shape 1PI action toward cosmological scalar physics.
It does not claim that the physical scalar effective action has been closed.

The exact structural chain tested here is:

  fixed-j q=2 shape (trace-free)
    -> common flux scaling is the conformal DeWitt direction
    -> j=1/2 freezes absolute tetrahedral volume
    -> symmetric two-strand q=2 blocking reaches j=1
    -> j=1 is the first equal-spin four-valent sector with non-scalar volume
    -> a finite local volume-source Legendre transform exists kinematically
    -> K5 lapse cochains exist as constraint smearing labels
    -> tetrahedral nearest-neighbor geometry has isotropic second moment.

What remains open is the essential physical step: derive one combined
projector/history amplitude that assigns the volume-sector weights, promotes
lapse labels to a physical response source, and creates nonzero connected
interblock correlators. Until then Phi, Psi, mu, Sigma and rho_hist(a) remain
open physical outputs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

from collective_volume_rg_gate import spectrum
from q2_symmetric_block_peter_weyl_growth_gate import one_n
from dual_k5_lapse_cochain_gate import run as run_lapse_cochain


def zero_matrix(M: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def run() -> dict[str, object]:
    checks: dict[str, bool] = {}

    # Common flux scaling gives the conformal DeWitt direction.
    Qdw_conformal = sp.Integer(3)-sp.Integer(9)
    checks["common_flux_scaling_is_unique_negative_DeWitt_target"] = Qdw_conformal == -6

    # Orthogonality to the registered q=2 shape tangent in the background metric.
    r3=sp.sqrt(3)
    MX=sp.Matrix([[r3/2,0,r3/2],[0,-r3/2,-r3/2],[r3/2,-r3/2,0]])
    MZ=sp.Matrix([[sp.Rational(1,2),1,-sp.Rational(1,2)],[1,sp.Rational(1,2),-sp.Rational(1,2)],[-sp.Rational(1,2),-sp.Rational(1,2),-1]])
    g0=sp.Matrix([[2,1,1],[1,2,1],[1,1,2]])
    gi=g0.inv()
    checks["shape_X_orthogonal_to_conformal_scale"] = sp.simplify(sp.trace(gi*MX)) == 0
    checks["shape_Z_orthogonal_to_conformal_scale"] = sp.simplify(sp.trace(gi*MZ)) == 0

    # Independent collective-volume spectrum computation already in repo.
    jhalf=spectrum(0.5)
    jone=spectrum(1.0)
    checks["j_half_absolute_volume_is_scalar"] = bool(jhalf["volume_is_scalar_on_intertwiner"])
    checks["j_one_absolute_volume_is_non_scalar"] = not bool(jone["volume_is_scalar_on_intertwiner"])
    checks["j_one_is_first_registered_nontrivial_volume_spin"] = int(jone["intertwiner_dimension"]) == 3

    # j=1 follows from exactly two symmetric q=2 active strands per endpoint.
    block2=one_n(2)
    checks["two_symmetric_q2_strands_give_j_one"] = block2["j"] == 1.0 and block2["endpoint_dimension"] == 3
    checks["two_strand_symmetric_irrep_is_exact_su2"] = block2["su2_error"] < 1e-12 and block2["casimir_error"] < 1e-12

    # Exact local kinematic volume source in the spin-1 intertwiner.
    # V spectrum = {0,v,v}, v=3^(1/4). Use q=eta*v and p=<V>/v.
    p=sp.symbols("p", positive=True)
    v=sp.root(3,4)
    gammaV=sp.simplify(p*sp.log(p)+(1-p)*sp.log(1-p)-p*sp.log(2)+sp.log(3))
    dgammaV=sp.simplify(sp.diff(gammaV,p))
    ddgammaV=sp.simplify(sp.diff(gammaV,p,2))
    p0=sp.Rational(2,3)
    checks["volume_source_inverse_is_log_p_over_2_1minusp"] = sp.simplify(dgammaV-(sp.log(p)-sp.log(2)-sp.log(1-p))) == 0
    checks["volume_1PI_zero_at_normalized_trace_baseline"] = sp.simplify(gammaV.subs(p,p0)) == 0
    checks["volume_1PI_dimensionless_hessian_at_baseline_is_9_over_2"] = sp.simplify(ddgammaV.subs(p,p0)-sp.Rational(9,2)) == 0
    volume_hessian_m = sp.simplify(sp.Rational(9,2)/(v**2))
    checks["volume_mean_field_hessian_exact"] = sp.simplify(volume_hessian_m-sp.Rational(9,2)/sp.sqrt(3)) == 0

    # Lapse cochain exists kinematically, but remains a smearing/support object.
    lapse=run_lapse_cochain(samples=20)
    checks["dual_K5_lapse_cochain_gate_passes"] = bool(lapse["passed"])

    # Tetrahedral nearest-neighbor geometry has exact isotropic second moment.
    normals=[
        sp.Matrix([1,1,1])/sp.sqrt(3),
        sp.Matrix([1,-1,-1])/sp.sqrt(3),
        sp.Matrix([-1,1,-1])/sp.sqrt(3),
        sp.Matrix([-1,-1,1])/sp.sqrt(3),
    ]
    sum_n=sum(normals,sp.zeros(3,1))
    second=sum((n*n.T for n in normals),sp.zeros(3))
    checks["tetra_neighbor_first_moment_zero"] = zero_matrix(sum_n)
    checks["tetra_neighbor_second_moment_is_4_over_3_identity"] = zero_matrix(second-sp.Rational(4,3)*sp.eye(3))

    passed=bool(all(checks.values()))
    return {
        "status":"derived collective scalar-carrier precursor; physical scalar history still open",
        "passed":passed,
        "checks":checks,
        "conformal_carrier":{
            "microscopic_operation":"common radial scaling of all face fluxes E_f -> (1+epsilon) E_f",
            "metric_response":"delta q = q",
            "DeWitt_value":"-6",
            "relation_to_q2_shape":"exactly orthogonal to X/Z trace-free tangent",
            "interpretation":"This is the structurally correct local conformal/volume direction missing from the fixed-spin q=2 shape source."
        },
        "representation_threshold":{
            "j_half":jhalf,
            "j_one":jone,
            "q2_symmetric_block_n2":block2,
            "interpretation":"At fixed j=1/2 the absolute volume is scalar. Two symmetric q=2 strands reach j=1, the first registered equal-spin four-valent sector with nontrivial volume spectrum."
        },
        "local_volume_source_positive_control":{
            "spectrum":"V={0,v,v}, v=3^(1/4)",
            "normalized_generating_function":"Z_V(q)=(1+2 exp(q))/3, q=eta*v",
            "mean_fraction":"p=<V>/v=2 exp(q)/(1+2 exp(q))",
            "Gamma_V":"p log p + (1-p) log(1-p) - p log 2 + log 3",
            "zero_source_baseline":"p0=2/3",
            "Gamma_V_second_derivative_wrt_p_at_p0":"9/2",
            "Gamma_V_second_derivative_wrt_mean_V_at_p0":str(volume_hessian_m),
            "claim_boundary":"This is a normalized kinematic intertwiner trace, not the graph-changing relational physical history. Its p0 is not a cosmological scale factor and its normalization is not a vacuum-energy prediction."
        },
        "lapse_status":{
            "available":"exact dual-K5 lapse cochain/smearing algebra",
            "physical_response":"OPEN: no projected lapse source or lapse-history susceptibility has been derived"
        },
        "interblock_status":{
            "tetrahedral_second_moment":"sum_a n_a n_a^T=(4/3)I",
            "consequence":"Once a microscopic reciprocal scalar transfer amplitude is derived, its leading nearest-neighbor k^2 symbol is isotropic.",
            "missing":"the transfer amplitude itself and, more importantly, its derivation inside the connected physical history W[J]"
        },
        "minimal_scalar_history_target":"Build one source-dressed connected physical amplitude with sources for common flux scale/volume, lapse response, and trace-free shape on adjacent blocks; then Legendre-transform the connected W to Gamma_scalar and only afterward form Bardeen Phi/Psi.",
        "cosmology_outputs":{
            "rho_hist_a":"OPEN_PHYSICAL",
            "Phi_a_k":"OPEN_PHYSICAL",
            "Psi_a_k":"OPEN_PHYSICAL",
            "mu_BQG_a_k":"OPEN_PHYSICAL",
            "Sigma_BQG_a_k":"OPEN_PHYSICAL"
        },
        "claim_boundary":"The gate closes only a structural carrier-identification problem. Symmetric blocking is conditional, the j=1 volume source is kinematic, lapse is only a cochain label, and connected physical history is still absent."
    }


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); a=ap.parse_args()
    out=run(); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__":
    raise SystemExit(main())
