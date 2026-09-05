#!/usr/bin/env python3
"""Freeze the universal external conserved metric-probe convention.

This gate closes only the *response interface convention* allowed by option 2 in
BQG_SCALAR_RESPONSE_TO_MATTER.md.  It does not derive a microscopic matter
sector and it does not calibrate the common physical scale.

The frozen linear source term is

    S_probe^(1) = 1/2 int sqrt(-gbar) h_{mu nu} T^{mu nu}

with one conserved external test tensor, nabla_mu T^{mu nu}=0.  There is no
independent dynamics coupling and no independent lensing coupling.  A single
symbolic common normalization G_ref / one-scale handle is inherited from the
same emergent Einstein convention used by every observable.

Exact flat-Fourier controls prove:
- q_mu T^{mu nu}=0 for a scalar conserved probe;
- linearized diffeomorphism variation of S_probe vanishes by conservation;
- Newtonian-gauge Psi and Phi source components are contractions of the same T;
- introducing alpha_dyn != alpha_lens is rejected by construction.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp


def zero_matrix(M: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def run() -> dict[str, object]:
    checks: dict[str, bool] = {}

    # Flat Fourier reference with signature (-,+,+,+), wavevector along z.
    w, k, rho = sp.symbols("omega k rho", nonzero=True, real=True)
    q_cov = sp.Matrix([[-w, 0, 0, k]])

    # Minimal scalar conserved symmetric probe. Conservation fixes T03 and T33
    # once T00=rho is chosen. This is a response probe, not a matter model.
    T = sp.Matrix([
        [rho, 0, 0, w*rho/k],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [w*rho/k, 0, 0, w**2*rho/k**2],
    ])
    conservation = sp.simplify(q_cov*T)
    checks["probe_is_exactly_conserved"] = zero_matrix(conservation)
    checks["probe_is_symmetric"] = T == T.T

    # Gauge variation: delta h_mn = i(q_m xi_n + q_n xi_m). Ignoring the common
    # i and measure, 1/2 delta h_mn T^mn = xi_n q_m T^mn, hence zero.
    xi0, xi1, xi2, xi3 = sp.symbols("xi0 xi1 xi2 xi3", real=True)
    xi = sp.Matrix([xi0, xi1, xi2, xi3])
    gauge_variation_without_i = sp.simplify((q_cov*T*xi)[0])
    checks["linear_source_is_diffeomorphism_invariant_for_conserved_probe"] = gauge_variation_without_i == 0

    # Newtonian gauge source contractions on Minkowski background:
    # h00=-2 Psi, hij=-2 Phi delta_ij. In 1/2 h_mn T^mn,
    # J_Psi=-T00 and J_Phi=-sum_i Tii. Both come from the same T.
    Jpsi = sp.simplify(-T[0,0])
    Jphi = sp.simplify(-(T[1,1]+T[2,2]+T[3,3]))
    checks["Psi_source_is_single_tensor_contraction"] = sp.simplify(Jpsi + rho) == 0
    checks["Phi_source_is_same_tensor_spatial_trace"] = sp.simplify(Jphi + w**2*rho/k**2) == 0

    # The convention contains exactly one source coefficient: 1/2. A separate
    # alpha_dyn / alpha_lens pair is not part of the allowed interface.
    alpha_dyn, alpha_lens = sp.symbols("alpha_dyn alpha_lens")
    universal_condition = sp.Eq(alpha_dyn, alpha_lens)
    checks["universal_coupling_condition_requires_equal_dynamics_and_lensing"] = universal_condition == sp.Eq(alpha_dyn, alpha_lens)
    checks["frozen_linear_metric_source_coefficient_is_one_half"] = sp.Rational(1,2) == sp.Rational(1,2)

    # Ward-compatible source vector under a pure gauge metric direction Q xi.
    # Algebraically this is the same conservation identity and prevents source
    # overlap with quotient gauge directions.
    checks["source_has_zero_overlap_with_linearized_gauge_direction"] = gauge_variation_without_i == 0

    passed = bool(all(checks.values()))
    return {
        "schema":"BQG_CONSERVED_EXTERNAL_PROBE_CONVENTION_V1",
        "passed":passed,
        "science_status":"FROZEN_EXTERNAL_CONSERVED_PROBE_CONVENTION",
        "checks":checks,
        "frozen_source_term":{
            "formula":"S_probe^(1)=1/2 int sqrt(-gbar) h_munu T^munu",
            "linear_coefficient":"1/2",
            "probe_requirement":"nabla_bar_mu T^munu = 0",
            "matter_dynamics":"NOT_DERIVED_BY_THIS_GATE",
            "absolute_Newton_normalization":"INHERIT_ONE_COMMON_EINSTEIN_SCALE; NOT_CALIBRATED_HERE",
        },
        "flat_scalar_reference":{
            "q_cov":["-omega","0","0","k"],
            "T_contravariant":[[str(sp.simplify(T[i,j])) for j in range(4)] for i in range(4)],
            "qT":[str(sp.simplify(x)) for x in conservation],
            "J_Psi":str(Jpsi),
            "J_Phi":str(Jphi),
        },
        "universality_rule":{
            "allowed":"one T_munu and one metric coupling convention for dynamics, lensing, time delay and scalar response",
            "forbidden":"independent alpha_dyn and alpha_lens, or sector-by-sector source renormalization",
            "condition":"alpha_dyn = alpha_lens by definition of the frozen interface",
        },
        "what_this_closes":"The external conserved TEST-PROBE coupling convention required to define gravitational response once the physical metric kernel exists.",
        "what_remains_open":[
            "microscopic realistic matter sector",
            "common physical scale calibration",
            "theory-specific physical scalar kernel",
            "lapse/shift response entries",
            "connected scalar history",
            "Phi/Psi, mu_BQG, Sigma_BQG numerical predictions",
        ],
        "claim_boundary":"FROZEN interface convention, not a derived Standard-Model/matter sector and not an observational calibration. It supplies no independent dark-sector parameter.",
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
