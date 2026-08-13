#!/usr/bin/env python3
"""Open-charge SU(2) intertwiner basis needed by h[h^-1,K] Lorentzian legs.

The existing Peter-Weyl engine projects every completed primitive back to a
four-valent Gauss singlet.  A Lorentzian factor

    C_e(K)=h_e [h_e^-1,K]

cannot be evaluated that way because after the first h_e^-1 the two endpoints
carry an open fundamental charge.  At such a node the four geometric legs must
couple to total J=1/2; the external fundamental then closes it to a singlet.

This gate constructs the exact recoupling tensors

    ((j1 j2)->K12, (j3 j4)->K34) -> J,M

for arbitrary total J, verifies their orthonormality, closes the J=1/2 sector
with an external spin-1/2 to five-valent singlets, and verifies that the genuine
four-valent volume V=sqrt(|J1.(J2xJ3)|) preserves the charged J,M sector.

Important numerical point: some charged columns are annihilated by the exact
volume.  The eigensolver then leaves O(1e-16) eigenvalue roundoff, and taking a
square root produces an artificial O(1e-8) output norm.  A relative projection
error is ill-conditioned on those zero-volume columns.  Therefore this gate
uses relative leakage only for numerically nonzero volume columns and absolute
leakage for annihilated columns.  No representation-theory threshold is
weakened.

It is a representation-theory prerequisite for Lorentzian amplitudes, not an
H_L or HDA result by itself.
"""
from __future__ import annotations

import argparse
import functools
import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import k5_peter_weyl_safe_hda_column as PW


def allowed_pair2(sa, sb):
    return tuple(range(abs(sa - sb), sa + sb + 1, 2))


def allowed_charged_labels(spins, J2):
    s1, s2, s3, s4 = spins
    out = []
    for K12 in allowed_pair2(s1, s2):
        for K34 in allowed_pair2(s3, s4):
            if abs(K12 - K34) <= J2 <= K12 + K34 and (K12 + K34 + J2) % 2 == 0:
                out.append((K12, K34))
    return tuple(out)


@functools.lru_cache(None)
def charged_tensor(spins, K12, K34, J2, M2):
    spins = tuple(spins)
    dims = tuple(s + 1 for s in spins)
    T = np.zeros(dims, complex)
    msets = [PW.m2vals_t(s) for s in spins]
    for inds in itertools.product(*[range(d) for d in dims]):
        m1, m2, m3, m4 = [msets[a][inds[a]] for a in range(4)]
        val = 0.0
        for MK in PW.m2vals_t(K12):
            ML = M2 - MK
            if ML not in PW.m2vals_t(K34):
                continue
            val += (
                PW.cg2(spins[0], spins[1], K12, m1, m2, MK)
                * PW.cg2(spins[2], spins[3], K34, m3, m4, ML)
                * PW.cg2(K12, K34, J2, MK, ML, M2)
            )
        T[inds] = val
    return T


def close_with_external_half(TJM, J2, M2):
    if J2 != 1:
        raise ValueError("a single external fundamental closes only J=1/2")
    ext_ms = PW.m2vals_t(1)
    out = np.zeros(TJM.shape + (2,), complex)
    for ie, me in enumerate(ext_ms):
        c = PW.cg2(J2, 1, 0, M2, me, 0)
        if c:
            out[..., ie] += c * TJM
    return out


def apply_volume_four(T, spins):
    d1, d2, d3, d4 = [s + 1 for s in spins]
    V = PW.volume123_matrix(spins[0], spins[1], spins[2])
    return (V @ T.reshape(d1 * d2 * d3, d4)).reshape(d1, d2, d3, d4)


def sector_projection_diagnostics(X, spins, J2, M2, nonzero_floor=1e-7):
    recon = np.zeros_like(X)
    for K12, K34 in allowed_charged_labels(spins, J2):
        B = charged_tensor(tuple(spins), K12, K34, J2, M2)
        recon += np.vdot(B, X) * B
    abs_leak = float(np.linalg.norm(X - recon))
    xnorm = float(np.linalg.norm(X))
    rel = None if xnorm <= nonzero_floor else abs_leak / xnorm
    return abs_leak, xnorm, rel


def run():
    # One fundamental hit from an all-j=1/2 four-valent node changes exactly one
    # doubled spin 1 -> 0 or 2.  Test all 8 resulting quartets.
    one_hit = []
    base = [1, 1, 1, 1]
    for leg in range(4):
        for so in (0, 2):
            q = base.copy(); q[leg] = so
            one_hit.append(tuple(q))
    one_hit = tuple(dict.fromkeys(one_hit))

    max_orth_error = 0.0
    max_five_singlet_orth_error = 0.0
    max_volume_abs_leakage = 0.0
    max_volume_rel_leakage_nonzero = 0.0
    near_zero_volume_columns = 0
    nonzero_volume_columns = 0
    min_nonzero_volume_column_norm = float("inf")
    max_near_zero_volume_column_norm = 0.0
    rows = []

    for spins in one_hit:
        labels = allowed_charged_labels(spins, 1)
        basis_by_M = {}
        row_abs = 0.0
        row_rel = 0.0
        row_zero = 0
        row_nonzero = 0
        for M2 in PW.m2vals_t(1):
            basis = [charged_tensor(spins, a, b, 1, M2) for a, b in labels]
            G = np.array([[np.vdot(A, B) for B in basis] for A in basis], complex)
            err = float(np.linalg.norm(G - np.eye(len(basis)))) if basis else 0.0
            max_orth_error = max(max_orth_error, err)
            basis_by_M[M2] = basis
            for B in basis:
                VB = apply_volume_four(B, spins)
                abs_leak, vnorm, rel = sector_projection_diagnostics(VB, spins, 1, M2)
                row_abs = max(row_abs, abs_leak)
                max_volume_abs_leakage = max(max_volume_abs_leakage, abs_leak)
                if rel is None:
                    row_zero += 1
                    near_zero_volume_columns += 1
                    max_near_zero_volume_column_norm = max(max_near_zero_volume_column_norm, vnorm)
                else:
                    row_nonzero += 1
                    nonzero_volume_columns += 1
                    min_nonzero_volume_column_norm = min(min_nonzero_volume_column_norm, vnorm)
                    row_rel = max(row_rel, rel)
                    max_volume_rel_leakage_nonzero = max(max_volume_rel_leakage_nonzero, rel)

        # Couple each recoupling label to one external fundamental and sum over
        # M.  These are genuine five-valent singlets.
        closed = []
        for ilabel, _ in enumerate(labels):
            S = np.zeros(tuple(s + 1 for s in spins) + (2,), complex)
            for M2 in PW.m2vals_t(1):
                S += close_with_external_half(basis_by_M[M2][ilabel], 1, M2)
            closed.append(S)
        G5 = np.array([[np.vdot(A, B) for B in closed] for A in closed], complex)
        err5 = float(np.linalg.norm(G5 - np.eye(len(closed)))) if closed else 0.0
        max_five_singlet_orth_error = max(max_five_singlet_orth_error, err5)
        rows.append({
            "spins": [s / 2 for s in spins],
            "charged_J": 0.5,
            "charged_dimension": len(labels),
            "labels_doubled": [list(x) for x in labels],
            "max_4leg_orth_error": max(
                float(np.linalg.norm(
                    np.array([[np.vdot(A, B) for B in basis_by_M[M]] for A in basis_by_M[M]])
                    - np.eye(len(labels))
                )) for M in PW.m2vals_t(1)
            ) if labels else 0.0,
            "5valent_singlet_orth_error": err5,
            "volume_near_zero_columns": row_zero,
            "volume_nonzero_columns": row_nonzero,
            "max_volume_absolute_sector_leakage": row_abs,
            "max_volume_relative_sector_leakage_nonzero": row_rel,
        })

    dims = sorted({r["charged_dimension"] for r in rows})
    if nonzero_volume_columns == 0:
        min_nonzero_volume_column_norm = 0.0
    # Absolute leakage is the correct test on all columns; relative leakage is
    # additionally required only when the volume output is numerically nonzero.
    passed = (
        len(one_hit) == 8
        and dims == [2, 3]
        and max_orth_error < 1e-11
        and max_five_singlet_orth_error < 1e-11
        and max_volume_abs_leakage < 1e-10
        and max_volume_rel_leakage_nonzero < 1e-10
        and nonzero_volume_columns > 0
    )
    return {
        "status": "charged-intertwiner recoupling prerequisite for Lorentzian holonomy commutators",
        "passed": bool(passed),
        "one_fundamental_hit_quartets": len(one_hit),
        "charged_dimensions_observed": dims,
        "rows": rows,
        "max_four_leg_orthonormality_error": max_orth_error,
        "max_five_valent_singlet_orthonormality_error": max_five_singlet_orth_error,
        "volume_nonzero_floor": 1e-7,
        "near_zero_volume_columns": near_zero_volume_columns,
        "nonzero_volume_columns": nonzero_volume_columns,
        "max_near_zero_volume_column_norm": max_near_zero_volume_column_norm,
        "min_nonzero_volume_column_norm": min_nonzero_volume_column_norm,
        "max_volume_absolute_JM_sector_leakage": max_volume_abs_leakage,
        "max_volume_relative_JM_sector_leakage_nonzero": max_volume_rel_leakage_nonzero,
        "representation_statement": (
            "After one fundamental holonomy hit, each affected endpoint is represented by a four-leg total-J=1/2 charged intertwiner; coupling the external fundamental closes a gauge singlet."
        ),
        "conditioning_note": (
            "Relative leakage is not evaluated on exact-zero volume columns because sqrt of eigensolver roundoff turns O(1e-16) Q eigenvalues into artificial O(1e-8) V norms. Those columns are tested by absolute leakage instead."
        ),
        "next_use": (
            "Use this charged basis as the intermediate compression layer for h_e^-1|Gauss>, apply V_v and H_E,v/K_v without raw magnetic blowup, then close with h_e to obtain C_e(K_v)=h_e[h_e^-1,K_v]."
        ),
        "scope_note": "Exact SU(2) representation/volume gate only; it does not yet evaluate C_e(K), the Lorentzian kinetic triple, or HDA closure.",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    out = run(); text = json.dumps(out, indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
