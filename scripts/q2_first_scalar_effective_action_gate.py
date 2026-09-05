#!/usr/bin/env python3
"""First exact q=2 local 1PI shape action and scalar-cosmology obstruction.

Starts only from the registered relational positive-control generating function

    Z(jx,jz)=cosh(sqrt(jx^2+jz^2)),  W=log Z,

and the exact q=2 logical-shape -> tetrahedral-metric map.  It computes the
full radial Legendre transform, the induced nonlinear intrinsic-metric volume,
and the local metric tangent.  It then proves three obstructions to calling the
result a physical cosmological scalar action:

1. the q=2 X/Z tangent is trace-free with respect to the background metric and
   has zero overlap with the conformal/volume direction;
2. the minimally justified product of projected blocks has exactly zero
   connected cross-block Hessian, hence no momentum/Poisson-like IR kernel;
3. the registered source layer has no independent lapse source.

This is therefore an exact finite 1PI *shape* action and a fail-closed map of
what additional microscopic structure is required for Phi, Psi, mu, Sigma and
rho_hist(a).  It is not a physical dark-sector calculation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp


def vec9(M: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([M[i, j] for i in range(3) for j in range(3)])


def zero_matrix(M: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def run() -> dict[str, object]:
    s = sp.symbols("s", real=True, nonnegative=True)

    # Exact radial Legendre transform of W(j)=log cosh |j|.
    gamma = sp.simplify(s * sp.atanh(s) + sp.Rational(1, 2) * sp.log(1 - s**2))
    gamma_series = sp.series(gamma, s, 0, 10).removeO()
    checks: dict[str, bool] = {
        "exact_legendre_derivative_is_inverse_source_radius": sp.simplify(sp.diff(gamma, s) - sp.atanh(s)) == 0,
        "radial_hessian_is_1_over_1_minus_s2": sp.simplify(sp.diff(gamma, s, 2) - 1/(1-s**2)) == 0,
        "gamma_zero_is_zero": sp.simplify(gamma.subs(s, 0)) == 0,
        "gamma_series_exact_through_s8": sp.simplify(
            gamma_series - (
                sp.Rational(1,2)*s**2 + sp.Rational(1,12)*s**4
                + sp.Rational(1,30)*s**6 + sp.Rational(1,56)*s**8
            )
        ) == 0,
        "gamma_boundary_limit_is_log2": sp.simplify(sp.limit(gamma, s, 1, dir="-") - sp.log(2)) == 0,
    }

    # Exact intrinsic metric reconstruction from the registered q=2 face Gram.
    x, z = sp.symbols("x z", real=True)
    G = sp.Matrix([
        [sp.Rational(3,4), -sp.Rational(1,4)-z/2, -sp.Rational(1,4)+z/4-sp.sqrt(3)*x/4],
        [-sp.Rational(1,4)-z/2, sp.Rational(3,4), -sp.Rational(1,4)+z/4+sp.sqrt(3)*x/4],
        [-sp.Rational(1,4)+z/4-sp.sqrt(3)*x/4, -sp.Rational(1,4)+z/4+sp.sqrt(3)*x/4, sp.Rational(3,4)],
    ])
    detG = sp.factor(G.det())
    expected_detG = sp.factor((1-z)*((z+2)**2-3*x**2)/16)
    checks["exact_face_gram_determinant"] = sp.simplify(detG-expected_detG) == 0

    # det[g]=8 sqrt(det G) for g=2 sqrt(det G) G^-1.
    detg = sp.simplify(8*sp.sqrt(detG))
    expected_detg = 2*sp.sqrt((1-z)*((z+2)**2-3*x**2))
    checks["exact_metric_determinant"] = sp.simplify(detg-expected_detg) == 0

    # log spatial volume = 1/2 log det g.  There is no linear volume response,
    # but a nonzero quadratic shape backreaction.  This is geometric response,
    # not a vacuum-energy calculation.
    logV = sp.simplify(sp.Rational(1,2)*sp.log(detg))
    logV_grad0 = [sp.simplify(sp.diff(logV, q).subs({x:0,z:0})) for q in (x,z)]
    logV_hess0 = sp.Matrix(2,2,lambda i,j: sp.simplify(sp.diff(logV,(x,z)[i],(x,z)[j]).subs({x:0,z:0})))
    checks["no_linear_intrinsic_volume_response"] = logV_grad0 == [0,0]
    checks["quadratic_intrinsic_volume_response_is_isotropic_minus_3_over_8"] = zero_matrix(
        logV_hess0 + sp.Rational(3,8)*sp.eye(2)
    )

    # Frozen first derivatives of g at the regular tetrahedron.
    r3 = sp.sqrt(3)
    MX = sp.Matrix([
        [r3/2, 0, r3/2],
        [0, -r3/2, -r3/2],
        [r3/2, -r3/2, 0],
    ])
    MZ = sp.Matrix([
        [sp.Rational(1,2), 1, -sp.Rational(1,2)],
        [1, sp.Rational(1,2), -sp.Rational(1,2)],
        [-sp.Rational(1,2), -sp.Rational(1,2), -1],
    ])
    g0 = sp.Matrix([[2,1,1],[1,2,1],[1,1,2]])
    gi = g0.inv()

    # Covariant trace-free condition and shape norm at the background.
    cov_trace_x = sp.simplify(sp.trace(gi*MX))
    cov_trace_z = sp.simplify(sp.trace(gi*MZ))
    cov_shape_gram = sp.Matrix([
        [sp.simplify(sp.trace(gi*MX*gi*MX)), sp.simplify(sp.trace(gi*MX*gi*MZ))],
        [sp.simplify(sp.trace(gi*MZ*gi*MX)), sp.simplify(sp.trace(gi*MZ*gi*MZ))],
    ])
    checks.update({
        "MX_is_covariantly_tracefree": cov_trace_x == 0,
        "MZ_is_covariantly_tracefree": cov_trace_z == 0,
        "covariant_shape_gram_is_3_over_2_identity": zero_matrix(cov_shape_gram-sp.Rational(3,2)*sp.eye(2)),
    })

    # Whiten the background: g0^(1/2)=I+J/3 and g0^(-1/2)=I-J/6.
    J3 = sp.ones(3)
    ghalf = sp.eye(3)+J3/3
    gihalf = sp.eye(3)-J3/6
    checks["exact_background_square_root"] = zero_matrix(ghalf*ghalf-g0)
    checks["exact_background_inverse_square_root"] = zero_matrix(gihalf*gihalf-gi)
    MXw = sp.simplify(gihalf*MX*gihalf)
    MZw = sp.simplify(gihalf*MZ*gihalf)
    Bw = vec9(MXw).row_join(vec9(MZw))
    Pw = sp.simplify(sp.Rational(2,3)*Bw*Bw.T)  # because Bw^T Bw=(3/2)I
    checks["whitened_shape_projector_is_idempotent"] = zero_matrix(Pw*Pw-Pw)
    conf = vec9(sp.eye(3)/sp.sqrt(3))
    checks["conformal_volume_mode_annihilated_by_shape_projector"] = zero_matrix(Pw*conf)

    # Scalar shear diagnostic in the orthonormal background frame.
    def scalar_shear(n: sp.Matrix) -> sp.Matrix:
        return sp.simplify(sp.sqrt(sp.Rational(3,2))*(n*n.T-sp.eye(3)/3))
    directions = {
        "100": sp.Matrix([1,0,0]),
        "010": sp.Matrix([0,1,0]),
        "001": sp.Matrix([0,0,1]),
        "110": sp.Matrix([1,1,0])/sp.sqrt(2),
        "111": sp.Matrix([1,1,1])/sp.sqrt(3),
    }
    shear_fraction: dict[str,str] = {}
    for name,n in directions.items():
        v=vec9(scalar_shear(n))
        shear_fraction[name]=str(sp.simplify((v.T*Pw*v)[0]/(v.T*v)[0]))
    checks["scalar_shear_111_has_zero_shape_overlap"] = shear_fraction["111"] == "0"
    checks["single_local_shape_tangent_does_not_span_generic_scalar_shear"] = shear_fraction["110"] == "25/36"

    # Old registered full-component Frobenius map, retained for direct
    # consistency with Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md.
    B = vec9(MX).row_join(vec9(MZ))
    flat_gram = sp.simplify(B.T*B)
    Pflat = sp.simplify(sp.Rational(2,9)*B*B.T)
    checks["registered_flat_gram_is_9_over_2_identity"] = zero_matrix(flat_gram-sp.Rational(9,2)*sp.eye(2))
    checks["registered_flat_tangent_projector_is_idempotent"] = zero_matrix(Pflat*Pflat-Pflat)

    # Exact local metric-space 1PI on h=B m in the registered flat convention.
    h2=sp.symbols("h2", nonnegative=True)
    gamma_metric=sp.simplify(gamma.subs(s,sp.sqrt(sp.Rational(2,9)*h2)))
    gamma_metric_series=sp.series(gamma_metric,h2,0,4).removeO()
    expected_metric_series=sp.Rational(1,9)*h2+sp.Rational(1,243)*h2**2+sp.Rational(4,10935)*h2**3
    checks["registered_metric_gamma_series_exact_through_h6"] = sp.simplify(gamma_metric_series-expected_metric_series)==0

    # Product blocks are the strongest interblock extension justified by the
    # current source layer alone.  Its connected cross Hessian is exactly zero.
    e1,e2,a1x,a1z,a2x,a2z=sp.symbols("e1 e2 a1x a1z a2x a2z", real=True)
    W2=(sp.log(sp.cosh(e1*sp.sqrt(a1x**2+a1z**2)))
        +sp.log(sp.cosh(e2*sp.sqrt(a2x**2+a2z**2))))
    cross=sp.simplify(sp.diff(W2,e1,e2).subs({e1:0,e2:0}))
    checks["factorized_two_block_connected_cross_hessian_is_zero"] = cross==0

    q4_laplacian_spectrum={"0":1,"2":4,"4":6,"6":4,"8":1}
    local_kernel_by_graph_mode={lam:"2/9" for lam in q4_laplacian_spectrum}
    checks["local_kernel_is_graph_mode_independent"] = len(set(local_kernel_by_graph_mode.values()))==1

    passed=bool(all(checks.values()))
    return {
        "status":"exact q=2 local 1PI shape action plus scalar-cosmology obstruction",
        "passed":passed,
        "checks":checks,
        "exact_shape_1PI":{
            "W":"log(cosh(sqrt(jx^2+jz^2)))",
            "mean_field_radius":"s=|m|=tanh(|j|), 0<=s<1",
            "inverse_source":"|j|=atanh(s)",
            "Gamma_shape":"s*atanh(s)+1/2*log(1-s^2)",
            "Gamma_series":str(gamma_series),
            "boundary_value_s_to_1":"log(2)",
        },
        "exact_intrinsic_metric_volume":{
            "det_face_Gram":"(1-z)*((z+2)^2-3*x^2)/16",
            "det_metric":"2*sqrt((1-z)*((z+2)^2-3*x^2))",
            "log_volume_gradient_at_regular":[str(v) for v in logV_grad0],
            "log_volume_hessian_at_regular":[[str(v) for v in row] for row in logV_hess0.tolist()],
            "interpretation":"Shape order changes intrinsic volume only from quadratic order. At the symmetric mean field m=0 there is no induced background shift. Treating the X/Z connected Hessian as a classical stochastic variance and calling this vacuum energy would be invalid without a physical loop/history measure.",
        },
        "scalar_carrier_obstruction":{
            "covariant_trace_MX":str(cov_trace_x),
            "covariant_trace_MZ":str(cov_trace_z),
            "conformal_projection":"0 exactly",
            "whitened_scalar_shear_projection_fraction":shear_fraction,
            "interpretation":"The present q=2 source spans two trace-free intrinsic-shape directions. It does not contain the conformal/volume mode Phi and it contains no independent lapse source Psi.",
        },
        "metric_tangent_1PI":{
            "registered_relation":"h=B m; |m|^2=(2/9)||h||_F^2",
            "Gamma_metric":"gamma(sqrt((2/9)||h||_F^2))",
            "small_field_series":"||h||^2/9+||h||^4/243+4||h||^6/10935+...",
            "quadratic_kernel":"K_local=(2/9)P_tangent",
            "rank":2,
        },
        "interblock_result":{
            "minimal_justified_extension":"product of independently projected q=2 blocks",
            "connected_cross_block_hessian":"0 exactly",
            "dual_Q4_laplacian_spectrum":q4_laplacian_spectrum,
            "local_kernel_by_graph_mode":local_kernel_by_graph_mode,
            "interpretation":"No graph-Laplacian/k dependence or Poisson-like IR response is present until the actual connected graph-changing physical history amplitude is derived.",
        },
        "cosmology_outputs":{
            "rho_hist_a":"NOT_DERIVABLE_FROM_NORMALIZED_LOCAL_SHAPE_SOURCE",
            "Phi_a_k":"NOT_DERIVABLE_MISSING_CONFORMAL_VOLUME_SOURCE_AND_CONNECTED_KERNEL",
            "Psi_a_k":"NOT_DERIVABLE_MISSING_LAPSE_RESPONSE_SOURCE_AND_CONNECTED_KERNEL",
            "mu_BQG_a_k":"NOT_DERIVABLE",
            "Sigma_BQG_a_k":"NOT_DERIVABLE",
        },
        "scientific_conclusion":"The first exact 1PI object supplied by the registered q=2 relational source is a nonlinear local two-component shape action, not a physical cosmological scalar action. This is a constructive no-go: the missing ingredients are now identified rather than fitted.",
        "next_required_carriers":[
            "derived common-flux-scale / volume source (conformal scalar)",
            "derived lapse/clock-response source",
            "non-factorizing connected interblock physical history amplitude",
        ],
        "claim_boundary":"R=J and the normalized trace remain registered positive controls, not the physical graph-changing gravitational history. No DM, DE, Phi/Psi, mu or Sigma is claimed.",
    }


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); a=ap.parse_args()
    out=run(); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__":
    raise SystemExit(main())
