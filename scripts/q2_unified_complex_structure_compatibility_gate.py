#!/usr/bin/env python3
"""Cross-layer exact compatibility audit for the q=2 real complex structure J.

The repository now contains several independently motivated appearances of

    J = [[0,-1],[1,0]],  J^2=-I:

1. oriented q=2/C4 arithmetic-complex bridge;
2. history Fourier phase W(theta)=exp(-theta J);
3. unique positive quadratic phase invariant Q(v)=v^T v;
4. realification of complex Hermitian quantum dynamics;
5. directed history difference Delta_W=W-I.

This gate checks that the same real matrix is used across these layers and
makes the remaining sign convention explicit. Standard realification of the
complex scalar exp(+i theta) is exp(+theta J), whereas the current history
forward convention gives exp(-theta J), i.e. the conjugate phase. Reversing the
history orientation U<->U^dagger flips that sign. No physical observable is
changed by this convention.

This is a compatibility theorem only. It does not derive the Born rule,
physical time, a physical Hamiltonian, or a matter equation.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

import q2_history_fourier_real_complex_structure_gate as HF
import phase_invariant_quadratic_weight_gate as QW
import realification_quantum_dynamics_gate as RQ


def zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in M)


def fraction_matrix_to_sympy(A) -> sp.Matrix:
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])


def parse_history_J() -> sp.Matrix:
    out = HF.run()
    if not out.get("passed", False):
        raise RuntimeError("history Fourier gate is not green")
    return sp.Matrix([[sp.sympify(x) for x in row] for row in out["J"]])


def run() -> dict[str, object]:
    I = sp.eye(2)
    Jcanonical = sp.Matrix([[0, -1], [1, 0]])
    Jhistory = parse_history_J()
    Jrealification = fraction_matrix_to_sympy(RQ.Jn(1))

    qweight_symbolic = QW.check_symbolic_coefficient_map()
    qweight_grid = QW.check_exhaustive_rational_grid()
    qweight_phase = QW.check_phase_rotation_invariance()
    qweight_positive = QW.check_positivity_normalization()

    checks = {
        "canonical_J_squared_is_minus_I": zero(Jcanonical * Jcanonical + I),
        "history_J_matches_canonical_exactly": zero(Jhistory - Jcanonical),
        "realification_J_matches_canonical_exactly": zero(Jrealification - Jcanonical),
        "quadratic_weight_symbolic_gate_green": bool(qweight_symbolic["pass"]),
        "quadratic_weight_rational_grid_green": bool(qweight_grid["pass"]),
        "quadratic_weight_mu4_phase_gate_green": bool(qweight_phase["pass"]),
        "quadratic_weight_positivity_normalization_green": bool(qweight_positive["pass"]),
    }

    # Reflection/conjugation convention.
    R = sp.diag(1, -1)
    checks["reflection_conjugates_J_to_minus_J"] = zero(R * Jcanonical * R + Jcanonical)

    # Standard complex scalar realification.  Multiplication by exp(+i theta)
    # on (Re z, Im z) is exp(+theta J).
    t = sp.symbols("t", real=True)
    Rplus = sp.cos(t) * I + sp.sin(t) * Jcanonical
    Rminus = sp.cos(t) * I - sp.sin(t) * Jcanonical
    realify_e_plus = sp.Matrix([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])
    checks["standard_realification_e_plus_itheta_is_exp_plus_theta_J"] = zero(Rplus - realify_e_plus)

    # Current history convention from HF is exp(-theta J), hence it is the
    # realification of exp(-i theta).  History reversal swaps the sign.
    realify_e_minus = sp.Matrix([[sp.cos(t), sp.sin(t)], [-sp.sin(t), sp.cos(t)]])
    checks["current_history_forward_is_conjugate_phase_exp_minus_itheta"] = zero(Rminus - realify_e_minus)
    checks["history_reversal_restores_plus_phase_convention"] = zero(R * Rminus * R - Rplus)

    # The same unique quadratic form is preserved by both sign conventions.
    checks["plus_rotation_preserves_euclidean_quadratic_form"] = zero(sp.trigsimp(Rplus.T * Rplus - I))
    checks["minus_rotation_preserves_euclidean_quadratic_form"] = zero(sp.trigsimp(Rminus.T * Rminus - I))

    # Re-derive uniqueness of a symmetric quadratic invariant from the same J.
    a, b, c = sp.symbols("a b c", real=True)
    A = sp.Matrix([[a, b], [b, c]])
    defect = sp.simplify(Jcanonical.T * A * Jcanonical - A)
    eqs = [sp.Eq(x, 0) for x in defect]
    sol = sp.solve(eqs, (b, c), dict=True)
    unique_form = bool(sol and sol[0].get(b) == 0 and sp.simplify(sol[0].get(c) - a) == 0)
    checks["same_J_forces_quadratic_form_A_lambda_I"] = unique_form

    # Cross-check the realified Schrodinger representation uses the same J.
    dyn = RQ.check_hermitian_dynamics()
    alg = RQ.check_algebra_homomorphism()
    checks["realification_star_algebra_gate_green"] = bool(alg["pass"])
    checks["realified_Hermitian_dynamics_gate_green"] = bool(dyn["pass"])

    # Directed history step uses exactly the same J in its character form.
    Delta_minus = (sp.cos(t) - 1) * I - sp.sin(t) * Jcanonical
    Delta_plus = (sp.cos(t) - 1) * I + sp.sin(t) * Jcanonical
    lap = 4 * sp.sin(t / 2) ** 2 * I
    checks["directed_minus_difference_square_is_scalar_laplacian"] = zero(
        (Delta_minus.T * Delta_minus - lap).applyfunc(sp.trigsimp)
    )
    checks["directed_plus_difference_square_is_same_scalar_laplacian"] = zero(
        (Delta_plus.T * Delta_plus - lap).applyfunc(sp.trigsimp)
    )

    # Generator signs are convention data; the carrier J itself is common.
    generator_history_forward = sp.simplify(Rminus.diff(t).subs(t, 0))
    generator_standard_complex = sp.simplify(Rplus.diff(t).subs(t, 0))
    checks["history_forward_generator_is_minus_J"] = zero(generator_history_forward + Jcanonical)
    checks["standard_complex_generator_is_plus_J"] = zero(generator_standard_complex - Jcanonical)

    passed = bool(all(checks.values()))
    return {
        "status": "exact cross-layer q=2 real-complex-structure compatibility audit",
        "passed": passed,
        "canonical_J": [[str(x) for x in row] for row in Jcanonical.tolist()],
        "checks": checks,
        "phase_convention": {
            "standard_complex_realification": "e^{+i theta} <-> exp(+theta J)",
            "current_history_forward": "W(theta)=exp(-theta J) <-> e^{-i theta}",
            "history_reversal": "U <-> U^dagger sends theta -> -theta and exp(-theta J) -> exp(+theta J)",
            "physical_status": "global orientation/forward convention only; no physical sign observable has been fixed here",
        },
        "quadratic_weight": {
            "same_J_invariance_equation": "J^T A J=A",
            "solution": "A=lambda I",
            "positive_normalized_solution": "A=I and Q(v)=v^T v=|z|^2",
            "claim": "Born-weight precursor only",
        },
        "dynamics_compatibility": {
            "complex_realification": "Jn(1) equals the same canonical J exactly",
            "history_directed_difference": "Delta_+/-=(cos theta-1)I +/- sin theta J have the same scalar positive square",
        },
        "main_result": (
            "The arithmetic C4 quarter-turn, history Fourier generator, phase-invariant quadratic norm, realification complex structure and directed-history lattice factor all use one exact real matrix J. The only sign mismatch is the already-unfixed choice of history-forward orientation, which exchanges a phase with its complex conjugate."
        ),
        "claim_boundary": (
            "Exact representation/convention compatibility only. This does not derive the physical Born rule, a physical time variable, a physical Hamiltonian, a Dirac equation, matter content, or an experimentally validated quantum theory from the information graph."
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
