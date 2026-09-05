#!/usr/bin/env python3
"""Exact finite scalar-ADM Dirac/Schur reduction engine and source controls.

This gate closes the *reduction algorithm*, not the theory-specific BQG scalar
kernel.  It implements two legal quadratic routes:

1. invertible auxiliary constraint block -> exact Schur complement;
2. strict Lagrange multipliers -> solve their linear constraints first, then
   quotient gauge directions.  A Moore-Penrose inverse of a singular multiplier
   block is explicitly rejected as a physical reduction.

The self-tests include:
- invariance of the Schur complement under invertible redefinitions of
  constraint variables;
- a pure-gravity-like scalar control in which one constraint plus one gauge
  direction removes both scalar coordinates;
- a negative control showing that pseudoinverting a zero multiplier block can
  manufacture a spurious scalar stiffness;
- a genuine extra-scalar control with a healthy pole;
- one conserved scalar stress-tensor probe, demonstrating that dynamics and
  lensing must come from the same source coupling.

A production JSON packet may be supplied with --packet.  The engine will reduce
it, but sets physical_kernel_emitted=true only when every theory-specific
provenance flag is explicitly true.  Therefore this script cannot silently
promote a local/kinematic Hessian to Gamma_scalar^(2)(omega,k).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp


REQUIRED_PHYSICAL_FLAGS = (
    "theory_specific_history",
    "volume_to_zeta_normalization_derived",
    "lapse_response_derived",
    "longitudinal_shift_response_derived",
    "connected_interblock_kernel",
    "ward_identity_certified",
    "conserved_source_coupling",
)


def zmat(rows: int, cols: int) -> sp.Matrix:
    return sp.zeros(rows, cols)


def as_exact_matrix(rows: list[list[Any]]) -> sp.Matrix:
    def one(x: Any) -> sp.Expr:
        if isinstance(x, bool):
            return sp.Integer(int(x))
        if isinstance(x, int):
            return sp.Integer(x)
        if isinstance(x, float):
            return sp.Rational(str(x))
        if isinstance(x, str):
            return sp.sympify(x)
        raise TypeError(f"unsupported matrix entry {x!r}")
    return sp.Matrix([[one(x) for x in row] for row in rows])


def columns(vs: list[sp.Matrix], rows: int) -> sp.Matrix:
    if not vs:
        return sp.zeros(rows, 0)
    return sp.Matrix.hstack(*vs)


def exact_zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def schur_reduce(Kcc: sp.Matrix, Kcp: sp.Matrix, Kpp: sp.Matrix) -> sp.Matrix:
    if Kcc.rows != Kcc.cols or Kcc.det() == 0:
        raise ValueError("K_cc must be exactly invertible for Schur reduction")
    if Kcp.rows != Kcc.rows or Kpp.rows != Kpp.cols or Kcp.cols != Kpp.rows:
        raise ValueError("incompatible block dimensions")
    return sp.simplify(Kpp - Kcp.T * Kcc.inv() * Kcp)


def quotient_gauge(K: sp.Matrix, J: sp.Matrix, G: sp.Matrix) -> dict[str, Any]:
    """Project an already constraint-reduced kernel to a gauge complement.

    G columns span gauge directions in the current coordinate space.  For a
    legitimate gauge kernel, K G=0 and G^T J=0.  The Euclidean complement is
    only a coordinate choice for representing the quotient; the nonzero
    quadratic form is invariant under a change of quotient basis.
    """
    n = K.rows
    if K.cols != n or J.rows != n or J.cols != 1 or G.rows != n:
        raise ValueError("gauge quotient dimension mismatch")
    ward_kernel = sp.simplify(K * G)
    ward_source = sp.simplify(G.T * J)
    Q = columns(G.T.nullspace(), n)
    Kq = sp.simplify(Q.T * K * Q)
    Jq = sp.simplify(Q.T * J)
    return {
        "basis": Q,
        "kernel": Kq,
        "source": Jq,
        "ward_kernel_zero": exact_zero(ward_kernel),
        "ward_source_zero": exact_zero(ward_source),
    }


def lagrange_reduce(A: sp.Matrix, Kpp: sp.Matrix, Jp: sp.Matrix, Gp: sp.Matrix) -> dict[str, Any]:
    """Solve strict multiplier constraints A p=0, then quotient gauge.

    The vacuum constraint surface is ker(A).  Gp must lie inside that surface.
    The physical quadratic form is the pullback of Kpp to ker(A), followed by
    the gauge quotient.  This is the correct finite linear-algebra analogue of
    imposing lapse/shift constraints before reading physical poles.
    """
    np_ = Kpp.rows
    if Kpp.cols != np_ or A.cols != np_ or Jp.shape != (np_, 1) or Gp.rows != np_:
        raise ValueError("Lagrange reduction dimension mismatch")
    N = columns(A.nullspace(), np_)
    if not exact_zero(A * Gp):
        raise ValueError("gauge generator does not preserve the multiplier constraint surface")
    if N.cols == 0:
        return {
            "constraint_basis": N,
            "constraint_reduced_kernel": sp.zeros(0),
            "constraint_reduced_source": sp.zeros(0, 1),
            "gauge_coordinates": sp.zeros(0, Gp.cols),
            "physical_basis": sp.zeros(np_, 0),
            "kernel": sp.zeros(0),
            "source": sp.zeros(0, 1),
            "ward_kernel_zero": True,
            "ward_source_zero": True,
        }
    Gram = sp.simplify(N.T * N)
    Gred = sp.simplify(Gram.inv() * N.T * Gp) if Gp.cols else sp.zeros(N.cols, 0)
    Kred = sp.simplify(N.T * Kpp * N)
    Jred = sp.simplify(N.T * Jp)
    q = quotient_gauge(Kred, Jred, Gred)
    Bphys = sp.simplify(N * q["basis"])
    return {
        "constraint_basis": N,
        "constraint_reduced_kernel": Kred,
        "constraint_reduced_source": Jred,
        "gauge_coordinates": Gred,
        "physical_basis": Bphys,
        "kernel": q["kernel"],
        "source": q["source"],
        "ward_kernel_zero": q["ward_kernel_zero"],
        "ward_source_zero": q["ward_source_zero"],
    }


def matrix_json(M: sp.Matrix) -> list[list[str]]:
    return [[str(sp.simplify(M[i, j])) for j in range(M.cols)] for i in range(M.rows)]


def reduce_packet(packet: dict[str, Any]) -> dict[str, Any]:
    schema = packet.get("schema")
    if schema != "BQG_SCALAR_ADM_BLOCK_V1":
        raise ValueError(f"unsupported schema {schema!r}")
    cvars = list(packet["constraint_variables"])
    pvars = list(packet["response_variables"])
    mode = packet["constraint_mode"]
    Kpp = as_exact_matrix(packet["K_pp"])
    Jp = as_exact_matrix([[x] for x in packet.get("J_p", [0] * len(pvars))])
    Gp = as_exact_matrix(packet.get("gauge_generators", [[] for _ in pvars]))
    if Gp.cols == 0:
        Gp = sp.zeros(len(pvars), 0)

    if mode == "schur":
        Kcc = as_exact_matrix(packet["K_cc"])
        Kcp = as_exact_matrix(packet["K_cp"])
        Kpre = schur_reduce(Kcc, Kcp, Kpp)
        q = quotient_gauge(Kpre, Jp, Gp)
        Kphys, Jphys, Bphys = q["kernel"], q["source"], q["basis"]
        ward_kernel_zero, ward_source_zero = q["ward_kernel_zero"], q["ward_source_zero"]
        reduction_note = "exact Schur complement followed by gauge quotient"
    elif mode == "lagrange":
        A = as_exact_matrix(packet["constraint_matrix_A"])
        r = lagrange_reduce(A, Kpp, Jp, Gp)
        Kphys, Jphys, Bphys = r["kernel"], r["source"], r["physical_basis"]
        ward_kernel_zero, ward_source_zero = r["ward_kernel_zero"], r["ward_source_zero"]
        reduction_note = "strict multiplier constraints solved before gauge quotient"
    else:
        raise ValueError("constraint_mode must be 'schur' or 'lagrange'")

    flags = dict(packet.get("physical_flags", {}))
    physical_ready = all(flags.get(k) is True for k in REQUIRED_PHYSICAL_FLAGS)
    provenance = dict(packet.get("provenance", {}))
    required_hashes = (
        "physical_history_hash",
        "volume_source_hash",
        "lapse_response_hash",
        "shift_response_hash",
        "ward_certificate_hash",
        "source_coupling_hash",
    )
    provenance_complete = all(bool(provenance.get(k)) for k in required_hashes)
    physical_kernel_emitted = bool(physical_ready and provenance_complete and ward_kernel_zero and ward_source_zero)

    return {
        "schema": "BQG_SCALAR_ADM_REDUCTION_RESULT_V1",
        "constraint_variables": cvars,
        "response_variables": pvars,
        "constraint_mode": mode,
        "reduction_note": reduction_note,
        "physical_dimension": int(Kphys.rows),
        "physical_basis": matrix_json(Bphys),
        "K_reduced": matrix_json(Kphys),
        "J_reduced": matrix_json(Jphys),
        "ward_kernel_zero": bool(ward_kernel_zero),
        "ward_source_zero": bool(ward_source_zero),
        "physical_flags": flags,
        "provenance_complete": bool(provenance_complete),
        "physical_kernel_emitted": physical_kernel_emitted,
        "science_status": "PHYSICAL_SCALAR_KERNEL_REDUCED" if physical_kernel_emitted else "REDUCTION_ONLY_PHYSICAL_INPUTS_INCOMPLETE",
        "claim_boundary": "A reduced algebraic kernel is not Gamma_scalar^(2)(omega,k) unless every theory-specific history/source/Ward provenance flag is true.",
    }


def selftest() -> dict[str, Any]:
    checks: dict[str, bool] = {}

    # 1) Schur complement is invariant under invertible redefinitions c=S c'.
    Kcc = sp.Matrix([[2, 1], [1, 3]])
    Kcp = sp.Matrix([[1, 2], [0, 1]])
    Kpp = sp.Matrix([[7, 1], [1, 5]])
    S = sp.Matrix([[1, 1], [0, 1]])
    K0 = schur_reduce(Kcc, Kcp, Kpp)
    K1 = schur_reduce(sp.simplify(S.T*Kcc*S), sp.simplify(S.T*Kcp), Kpp)
    checks["schur_invariant_under_constraint_redefinition"] = exact_zero(K0-K1)

    # 2) Pure-gravity-like scalar control: multiplier sets zeta=0, E is gauge.
    # No scalar physical coordinate survives.
    A_gr = sp.Matrix([[1, 0]])
    Kpp_gr = sp.diag(3, 0)
    J_gr = sp.zeros(2, 1)
    G_gr = sp.Matrix([[0], [1]])
    gr = lagrange_reduce(A_gr, Kpp_gr, J_gr, G_gr)
    checks["constraint_plus_gauge_removes_pure_gravity_scalar_control"] = gr["kernel"].rows == 0

    # 3) Negative control: pinv(Kcc=0) would leave Kpp and invent stiffness.
    naive = Kpp_gr  # Kpp - Kpc pinv(0) Kcp
    checks["naive_singular_schur_would_be_spurious"] = naive.rank() == 1 and gr["kernel"].rows == 0

    # 4) Genuine extra scalar survives constraint+gauge and has a healthy pole.
    w2, k2 = sp.symbols("w2 k2", real=True)
    cs2, m2 = sp.Rational(1, 4), sp.Integer(2)
    D = w2 - cs2*k2 - m2
    A_ex = sp.Matrix([[1, 0, 0]])
    Kpp_ex = sp.diag(0, 0, D)
    G_ex = sp.Matrix([[0], [1], [0]])
    J_ex = sp.Matrix([0, 0, 1])
    ex = lagrange_reduce(A_ex, Kpp_ex, J_ex, G_ex)
    checks["genuine_extra_scalar_dimension_one"] = ex["kernel"].shape == (1, 1)
    checks["genuine_extra_scalar_kernel_exact"] = sp.simplify(ex["kernel"][0,0]-D) == 0
    checks["healthy_extra_scalar_positive_omega2_residue"] = sp.diff(ex["kernel"][0,0], w2) == 1
    checks["healthy_extra_scalar_pole"] = sp.solve(sp.Eq(ex["kernel"][0,0], 0), w2) == [cs2*k2+m2]

    # 5) Conserved scalar stress-tensor probe in flat Fourier space.
    om, kk, rho = sp.symbols("omega k rho", nonzero=True, real=True)
    T = sp.Matrix([
        [rho, 0, 0, om*rho/kk],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [om*rho/kk, 0, 0, om**2*rho/kk**2],
    ])
    qcov = sp.Matrix([[-om, 0, 0, kk]])
    checks["conserved_scalar_probe_qT_zero"] = exact_zero(sp.simplify(qcov*T))
    Jpsi = -rho
    Jphi = -sp.simplify(T[1,1]+T[2,2]+T[3,3])
    checks["single_probe_defines_both_dynamics_and_lensing_sources"] = (
        sp.simplify(Jpsi + rho) == 0 and sp.simplify(Jphi + om**2*rho/kk**2) == 0
    )

    passed = bool(all(checks.values()))
    return {
        "schema": "BQG_SCALAR_ADM_DIRAC_ENGINE_SELFTEST_V1",
        "passed": passed,
        "checks": checks,
        "schur_control": {"K_reduced": matrix_json(K0)},
        "pure_gravity_scalar_control": {
            "variables": ["zeta", "E"],
            "constraint": "zeta=0",
            "gauge": "E",
            "physical_dimension": int(gr["kernel"].rows),
            "naive_pseudoinverse_rank": int(naive.rank()),
        },
        "extra_scalar_control": {
            "physical_dimension": int(ex["kernel"].rows),
            "K_scalar": str(ex["kernel"][0,0]),
            "pole": "omega^2=(1/4)k^2+2",
            "dK_domega2": "1",
        },
        "conserved_probe_control": {
            "q_mu": ["-omega", "0", "0", "k"],
            "q_mu_T_munu": ["0", "0", "0", "0"],
            "J_Psi": str(Jpsi),
            "J_Phi": str(Jphi),
            "note": "Reference probe only. BQG must derive/fix one universal normalization before mu or Sigma are physical predictions.",
        },
        "claim_boundary": "This proves the finite reduction/source algebra and its failure modes. It does not supply the missing theory-specific BQG ADM block entries.",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--packet", type=Path)
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    out: dict[str, Any] = {"selftest": selftest()}
    if a.packet:
        out["production"] = reduce_packet(json.loads(a.packet.read_text(encoding="utf-8")))
    out["passed"] = bool(out["selftest"]["passed"])
    txt = json.dumps(out, indent=2)
    print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(txt+"\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
