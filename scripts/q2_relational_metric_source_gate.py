#!/usr/bin/env python3
"""Exact projected relational metric-source / Gamma^(2) positive control.

Builds on the finite C8 combined-projector construction.  The invariant
physical subspace is embedded by the exact isometry

    V |psi> = 1/sqrt(8) sum_t |t> tensor R^t |psi>,

with R=J as the already-derived q=2 positive-control system step.  For any
system operator O define the relational Dirac observable

    O_rel = sum_t |t><t| tensor R^t O R^{-t}.

Then

    [O_rel,G]=0,
    O_rel V = V O,
    V^dagger O_rel V = O.

Therefore source insertions can be defined after the physical projector rather
than through a constraint spectral resolvent.

Using the q=2 shape operators X,Z and the already-derived linear shape-to-metric
Jacobians M_X,M_Z, this gate constructs an exact finite physical generating
functional, its connected quadratic response, and the Moore-Penrose inverse on
the two-dimensional metric-shape tangent space.  This is a formal positive
control for the arrow

    physical projector -> metric sources -> W[J] -> Gamma^(2)_metric,

not the physical graviton propagator of the full theory.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def shift(n: int) -> sp.Matrix:
    S = sp.zeros(n)
    for t in range(n):
        S[(t + 1) % n, t] = 1
    return S


def simplify_matrix(M: sp.Matrix) -> sp.Matrix:
    return M.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))


def zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in M)


def group_average(G: sp.Matrix, n: int) -> sp.Matrix:
    out = sp.zeros(G.rows)
    Gt = sp.eye(G.rows)
    for _ in range(n):
        out += Gt
        Gt *= G
    return simplify_matrix(out / n)


def history_isometry(R: sp.Matrix, n: int) -> sp.Matrix:
    # 2n x 2 matrix; t-th 2x2 block is R^t/sqrt(n).
    blocks = []
    Rt = sp.eye(R.rows)
    for _ in range(n):
        blocks.append(Rt / sp.sqrt(n))
        Rt *= R
    return sp.Matrix.vstack(*blocks)


def relationalize(O: sp.Matrix, R: sp.Matrix, n: int) -> sp.Matrix:
    out = sp.zeros(n * O.rows)
    Rt = sp.eye(R.rows)
    for t in range(n):
        block = simplify_matrix(Rt * O * Rt.inv())
        r0 = t * O.rows
        out[r0:r0 + O.rows, r0:r0 + O.rows] = block
        Rt *= R
    return simplify_matrix(out)


def vec9(M: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([M[i, j] for i in range(3) for j in range(3)])


def run() -> dict[str, object]:
    n = 8
    I2 = sp.eye(2)
    I16 = sp.eye(16)
    S = shift(n)
    J = sp.Matrix([[0, -1], [1, 0]])
    R = J
    G = sp.kronecker_product(S, R)

    V = simplify_matrix(history_isometry(R, n))
    Prel_from_V = simplify_matrix(V * V.H)
    Prel_group = group_average(G, n)

    checks = {
        "history_embedding_is_isometry": zero(V.H * V - I2),
        "VVdagger_equals_combined_group_projector": zero(Prel_from_V - Prel_group),
        "physical_projector_is_Hermitian": zero(Prel_group.H - Prel_group),
        "physical_projector_is_idempotent": zero(Prel_group * Prel_group - Prel_group),
        "physical_projector_rank_is_2": int(Prel_group.rank()) == 2,
        "combined_constraint_order_is_8": zero(G ** 8 - I16),
    }

    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.Matrix([[1, 0], [0, -1]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])

    Xrel = relationalize(X, R, n)
    Zrel = relationalize(Z, R, n)
    Yrel = relationalize(Y, R, n)

    checks.update({
        "Xrel_commutes_with_constraint": zero(Xrel * G - G * Xrel),
        "Zrel_commutes_with_constraint": zero(Zrel * G - G * Zrel),
        "Yrel_commutes_with_constraint": zero(Yrel * G - G * Yrel),
        "Xrel_intertwines_exactly": zero(Xrel * V - V * X),
        "Zrel_intertwines_exactly": zero(Zrel * V - V * Z),
        "Yrel_intertwines_exactly": zero(Yrel * V - V * Y),
        "compressed_Xrel_is_X": zero(V.H * Xrel * V - X),
        "compressed_Zrel_is_Z": zero(V.H * Zrel * V - Z),
        "compressed_Yrel_is_Y": zero(V.H * Yrel * V - Y),
        "relational_Pauli_XZ_anticommute_on_full_space": zero(Xrel * Zrel + Zrel * Xrel),
        "relational_X_squared_is_identity": zero(Xrel * Xrel - I16),
        "relational_Z_squared_is_identity": zero(Zrel * Zrel - I16),
    })

    # Exact physical source algebra. K=jx X+jz Z obeys K^2=r^2 I, so the
    # normalized physical trace of exp(K_rel) is cosh(r).
    jx, jz, eps, ax, az = sp.symbols("jx jz eps ax az", real=True)
    K = jx * X + jz * Z
    r2 = sp.expand(jx**2 + jz**2)
    checks["shape_source_square_is_r2_identity"] = zero(K * K - r2 * I2)

    # Rather than use a branch-sensitive symbolic sqrt at the origin, register
    # the analytic generating function and its directional Taylor series.
    r = sp.sqrt(jx**2 + jz**2)
    Zphys = sp.cosh(r)
    directional_W = sp.log(sp.cosh(eps * sp.sqrt(ax**2 + az**2)))
    Wseries = sp.series(directional_W, eps, 0, 6).removeO().expand()
    expected_Wseries = (
        sp.Rational(1, 2) * eps**2 * (ax**2 + az**2)
        - sp.Rational(1, 12) * eps**4 * (ax**2 + az**2)**2
    ).expand()
    checks["connected_W_directional_series_is_exact_to_quartic"] = sp.simplify(Wseries - expected_Wseries) == 0

    shape_connected_hessian = sp.eye(2)

    # Exact q=2 logical shape-to-metric Jacobians from the frozen bridge.
    s3 = sp.sqrt(3)
    MX = sp.Matrix([
        [s3/2, 0, s3/2],
        [0, -s3/2, -s3/2],
        [s3/2, -s3/2, 0],
    ])
    MZ = sp.Matrix([
        [sp.Rational(1,2), 1, -sp.Rational(1,2)],
        [1, sp.Rational(1,2), -sp.Rational(1,2)],
        [-sp.Rational(1,2), -sp.Rational(1,2), -1],
    ])

    bx = vec9(MX)
    bz = vec9(MZ)
    B = bx.row_join(bz)  # 9 x 2
    gram = simplify_matrix(B.T * B)
    expected_gram = sp.Rational(9, 2) * sp.eye(2)
    checks["metric_shape_Jacobian_columns_are_orthogonal_equal_norm"] = zero(gram - expected_gram)

    # Connected metric response at zero source: C_metric = B Sigma B^T with
    # Sigma=I in the normalized physical trace ensemble.
    Cmetric = simplify_matrix(B * shape_connected_hessian * B.T)
    Cplus = simplify_matrix(sp.Rational(4, 81) * Cmetric)
    Ptangent = simplify_matrix(sp.Rational(2, 9) * Cmetric)

    checks.update({
        "metric_connected_response_rank_is_2": int(Cmetric.rank()) == 2,
        "metric_tangent_projector_is_idempotent": zero(Ptangent * Ptangent - Ptangent),
        "metric_tangent_projector_is_Hermitian": zero(Ptangent.H - Ptangent),
        "metric_covariance_pseudoinverse_CCpC": zero(Cmetric * Cplus * Cmetric - Cmetric),
        "metric_covariance_pseudoinverse_CpCCp": zero(Cplus * Cmetric * Cplus - Cplus),
        "metric_covariance_pseudoinverse_projector_left": zero(Cmetric * Cplus - Ptangent),
        "metric_covariance_pseudoinverse_projector_right": zero(Cplus * Cmetric - Ptangent),
    })

    # Nonzero spectrum follows from B^T B=(9/2)I.
    nonzero_metric_response_eigenvalue = sp.Rational(9, 2)
    tangent_Gamma2_eigenvalue = sp.Rational(2, 9)

    # Direct source compression: any source insertion on the physical history
    # is exactly equivalent to the original two-dimensional geometry source.
    Krel = simplify_matrix(jx * Xrel + jz * Zrel)
    checks["source_operator_intertwines_exactly"] = zero(Krel * V - V * K)
    checks["source_operator_compresses_exactly"] = zero(V.H * Krel * V - K)

    passed = bool(all(checks.values()))
    return {
        "status": "exact projected relational metric-source generating-functional positive control",
        "passed": passed,
        "physical_subspace_dimension": int(Prel_group.rank()),
        "checks": checks,
        "source_generating_function": {
            "normalized_physical_trace": "Z(jx,jz)=cosh(sqrt(jx^2+jz^2))",
            "connected_function": "W=log Z",
            "zero_source_shape_connected_hessian": [[1,0],[0,1]],
            "directional_series_through_quartic": str(Wseries),
        },
        "shape_to_metric": {
            "MX": [[str(x) for x in row] for row in MX.tolist()],
            "MZ": [[str(x) for x in row] for row in MZ.tolist()],
            "B_transpose_B": [[str(x) for x in row] for row in gram.tolist()],
            "metric_response_rank": int(Cmetric.rank()),
            "nonzero_metric_connected_response_eigenvalue": str(nonzero_metric_response_eigenvalue),
            "tangent_Gamma2_pseudoinverse_eigenvalue": str(tangent_Gamma2_eigenvalue),
            "metric_Gamma2_positive_control": "C_metric^+ = (4/81) C_metric on the frozen 2D shape tangent",
        },
        "formal_bridge": (
            "The combined physical projector admits exact gauge-invariant relational source operators. Their compression to the physical history is unitarily equivalent to the original q=2 geometry operators. The connected source Hessian therefore pushes through the frozen shape-to-metric Jacobian, and its Moore-Penrose inverse is well-defined on the two-dimensional metric-shape tangent space."
        ),
        "next_physical_gate": (
            "Replace the positive-control system step R=J and normalized physical trace ensemble by the actual graph-changing gravitational combined rigging map/boundary amplitude. Then repeat the same metric-source construction over connected blocks/refinement levels and extract the physical TT Gamma^(2)(omega,k) before applying the frozen six-Wilson predictor."
        ),
        "claim_boundary": (
            "This is an exact finite relational-source and linearized metric-dictionary positive control. It is not the physical spacetime 1PI graviton kernel, does not identify the history label with physical time or omega, and does not freeze any of the six physical TT Wilson coefficients or g_YC^gravity."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
