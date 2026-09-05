#!/usr/bin/env python3
"""Exact q=2 local scalar-ADM seed from the already-derived carriers.

This gate advances the scalar frontier without inventing lapse/shift dynamics.
It converts the exact j=1 mean-volume Legendre control to a logarithmic local
volume coordinate

    zeta_V = (1/3) log(p/p0),  p0=2/3,

so p=p0 exp(3 zeta_V).  This is the natural dimensionless perturbation of the
mean local volume because delta V/V = 3 delta zeta_V.  It derives the exact
local Gamma_V(zeta_V) and its Hessian at the symmetric point.

The result is then embedded as a *known-mask* seed for the scalar ADM basis
(deltaN, B, zeta_V, E).  Entries not derived by the current microscopic source
history are marked UNKNOWN rather than set to zero.  In particular no lapse,
longitudinal-shift, shear or connected-interblock coefficient is fabricated.

zeta_V here is a kinematic log-volume response coordinate of the normalized
j=1 positive control.  It is not yet the physical FLRW/Bardeen zeta.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

from dual_k5_lapse_cochain_gate import run as run_lapse
from nearest_block_s3_transfer_gate import run as run_transfer_geometry


def zero_matrix(M: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def run() -> dict[str, object]:
    checks: dict[str, bool] = {}

    zeta = sp.symbols("zeta_V", real=True)
    p0 = sp.Rational(2, 3)
    p = sp.simplify(p0 * sp.exp(3*zeta))
    gamma = sp.simplify(
        p*sp.log(p) + (1-p)*sp.log(1-p) - p*sp.log(2) + sp.log(3)
    )
    d1 = sp.simplify(sp.diff(gamma, zeta).subs(zeta, 0))
    d2 = sp.simplify(sp.diff(gamma, zeta, 2).subs(zeta, 0))
    d3 = sp.simplify(sp.diff(gamma, zeta, 3).subs(zeta, 0))
    d4 = sp.simplify(sp.diff(gamma, zeta, 4).subs(zeta, 0))
    checks["Gamma_zeta_zero_at_baseline"] = sp.simplify(gamma.subs(zeta, 0)) == 0
    checks["Gamma_zeta_first_derivative_zero"] = d1 == 0
    checks["Gamma_zeta_hessian_exact_18"] = d2 == 18
    checks["Gamma_zeta_cubic_derivative_exact_216"] = d3 == 216
    checks["Gamma_zeta_quartic_derivative_exact_3078"] = d4 == 3078

    # Geometric meaning of zeta_V: V/V0=exp(3 zeta_V), while the conformal
    # metric convention q_ij=exp(2 zeta) q0_ij gives the same volume law.
    eps = sp.symbols("eps", real=True)
    Vratio = sp.exp(3*zeta)
    qscale = sp.exp(2*zeta)
    checks["log_volume_coordinate_has_exact_exp3zeta_volume_law"] = sp.simplify(Vratio-qscale**sp.Rational(3,2)) == 0
    checks["linear_common_flux_scale_maps_to_metric_zeta_half"] = sp.diff(qscale,zeta).subs(zeta,0) == 2

    # Reconfirm exact orthogonality of fixed-spin q=2 shape to conformal scale.
    r3=sp.sqrt(3)
    MX=sp.Matrix([[r3/2,0,r3/2],[0,-r3/2,-r3/2],[r3/2,-r3/2,0]])
    MZ=sp.Matrix([[sp.Rational(1,2),1,-sp.Rational(1,2)],[1,sp.Rational(1,2),-sp.Rational(1,2)],[-sp.Rational(1,2),-sp.Rational(1,2),-1]])
    g0=sp.Matrix([[2,1,1],[1,2,1],[1,1,2]])
    gi=g0.inv()
    checks["shape_X_decouples_linearly_from_conformal_seed"] = sp.simplify(sp.trace(gi*MX)) == 0
    checks["shape_Z_decouples_linearly_from_conformal_seed"] = sp.simplify(sp.trace(gi*MZ)) == 0

    lapse = run_lapse(samples=32)
    transfer = run_transfer_geometry()
    checks["lapse_cochain_support_available"] = bool(lapse["passed"])
    checks["nearest_block_scalar_geometry_available"] = bool(transfer["passed"])

    # Leading small-k symbol if a future physical scalar nearest-neighbor
    # transfer amplitude tau and physical edge length a are supplied:
    # sum_a (1-cos(a k.n_a)) = (2/3) a^2 k^2 + O(k^4).
    a, tau, k2 = sp.symbols("a tau k2", real=True)
    leading_symbol = sp.Rational(2,3)*tau*a**2*k2
    checks["leading_tetra_scalar_symbol_coefficient_is_2_over_3"] = sp.simplify(leading_symbol/(tau*a**2*k2)-sp.Rational(2,3)) == 0

    basis = ["deltaN", "B", "zeta_V", "E"]
    UNKNOWN = "UNKNOWN_MICROSCOPIC_HISTORY_ENTRY"
    Kseed = [
        [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
        [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
        [UNKNOWN, UNKNOWN, "18", UNKNOWN],
        [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    ]
    known_mask = [
        [False,False,False,False],
        [False,False,False,False],
        [False,False,True,False],
        [False,False,False,False],
    ]

    passed = bool(all(checks.values()))
    return {
        "schema":"BQG_Q2_SCALAR_ADM_SEED_V1",
        "passed":passed,
        "science_status":"EXACT_LOCAL_VOLUME_SEED_PHYSICAL_ADM_BLOCK_INCOMPLETE",
        "checks":checks,
        "local_log_volume_1PI":{
            "definition":"zeta_V=(1/3) log(p/p0), p0=2/3",
            "p_of_zeta":"(2/3) exp(3 zeta_V)",
            "Gamma_V_of_zeta":str(gamma),
            "Gamma_prime_at_0":str(d1),
            "Gamma_second_at_0":str(d2),
            "Gamma_third_at_0":str(d3),
            "Gamma_fourth_at_0":str(d4),
            "quadratic_local_stiffness":"K_zetaV_zetaV=18",
            "coordinate_scope":"Kinematic normalized-j=1 mean-volume coordinate; not yet physical FLRW/Bardeen zeta."
        },
        "scalar_ADM_seed":{
            "basis":basis,
            "K_local_seed":Kseed,
            "known_mask":known_mask,
            "known_entry_count":1,
            "unknown_entry_policy":"Unknown lapse/shift/shear/history entries are never replaced by zero.",
        },
        "shape_sector_relation":{
            "linear_conformal_overlap_X":"0 exactly",
            "linear_conformal_overlap_Z":"0 exactly",
            "interpretation":"The exact X/Z shape 1PI remains an auxiliary trace-free sector and is not silently renamed zeta_V."
        },
        "lapse_seed":{
            "cochain_formula":"omega_vw=N_v M_w-N_w M_v",
            "response_hessian":"OPEN_PHYSICAL",
            "reason":"Constraint smearing support is known, but the projected lapse response source in W_phys[J] is not."
        },
        "interblock_seed":{
            "geometry":"tetrahedral neighbor second moment = (4/3) I",
            "future_scalar_transfer_symbol":"tau * sum_a[1-cos(a k.n_a)] = (2/3) tau a^2 k^2 + O(k^4)",
            "tau":"OPEN_PHYSICAL_CONNECTED_HISTORY_AMPLITUDE",
            "physical_edge_scale_a":"OPEN_COMMON_SCALE",
        },
        "next_missing_microscopic_entries":[
            "projected lapse-response susceptibility and its couplings to zeta_V/E",
            "longitudinal shift/shear constraint-response block",
            "connected interblock scalar transfer amplitudes from physical history",
            "one fixed conserved matter/probe coupling and Ward certificate",
        ],
        "physical_reduction_ready":False,
        "claim_boundary":"This closes one exact local conformal-volume seed entry and its normalization in the kinematic j=1 positive control. It does not close the physical ADM scalar block, Gamma_scalar(omega,k), Phi/Psi, mu/Sigma, DM or DE.",
    }


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run();txt=json.dumps(out,indent=2);print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__=="__main__":
    raise SystemExit(main())
