#!/usr/bin/env python3
"""Collect three directly computed L1 metric-edge depth-two representatives.

Edges 01, 02 and 23 contain: one diagonal anchor, two independent adjacent
pairs and one opposite pair.  They therefore determine and internally test the
three S4 orbit coefficients of K=<u|u>, A=<u|H_B u> and
B=<H_B u|H_B u> without a generic 6x6 fit.

For each metric irrep X=A1,E,T2 define

    h1_X = A_X/K_X,
    h2_X = B_X/K_X,
    Sigma2_X = h2_X-h1_X^2.

Sigma2 is the normalized depth-two Krylov leakage/variance after the first
metric tangent shell.  E-T2 splitting is a dynamical tetrahedral anisotropy
diagnostic, not yet the physical Lorentzian zeta4 coefficient.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


REPS = (0, 1, 5)
TOL = 3e-7


def load_state(path: Path):
    z = np.load(path)
    spins = z["spins"]
    Ks = z["Ks"]
    amp = z["amp"]
    out = {}
    for i in range(len(amp)):
        key = spins[i].tobytes() + Ks[i].tobytes()
        out[key] = complex(amp[i])
    return out


def inner(a, b):
    if len(a) <= len(b):
        return sum(np.conj(v) * b.get(k, 0j) for k, v in a.items())
    return sum(np.conj(a.get(k, 0j)) * v for k, v in b.items())


def matrix(left, right):
    M = np.zeros((3, 3), complex)
    for i in range(3):
        for j in range(3):
            M[i, j] = inner(left[i], right[j])
    return M


def orbit_fit(M):
    norm = max(float(np.linalg.norm(M)), 1e-30)
    herm = float(np.linalg.norm(M - M.conj().T) / norm)
    imag = float(np.max(np.abs(M.imag)))
    diag = [M[i, i].real for i in range(3)]
    adj = [M[0,1].real, M[1,0].real, M[1,2].real, M[2,1].real]
    opp = [M[0,2].real, M[2,0].real]
    a = float(np.mean(diag)); b = float(np.mean(adj)); c = float(np.mean(opp))
    fit = np.array([[a,b,c],[b,a,b],[c,b,a]], dtype=float)
    residual = float(np.linalg.norm(M.real - fit) / max(np.linalg.norm(M.real), 1e-30))
    return {
        "a_same": a,
        "b_adjacent": b,
        "c_opposite": c,
        "hermiticity_relative_defect": herm,
        "max_imaginary_entry": imag,
        "diagonal_spread": float(max(diag)-min(diag)),
        "adjacent_spread": float(max(adj)-min(adj)),
        "opposite_spread": float(max(opp)-min(opp)),
        "three_representative_orbit_residual": residual,
        "lambda_A1": a + 4*b + c,
        "lambda_E": a - 2*b + c,
        "lambda_T2": a - c,
    }


def run(root: Path):
    meta = []
    U = []
    V = []
    for e in REPS:
        m = json.loads((root / f"edge_{e}.json").read_text(encoding="utf-8"))
        if not m.get("passed"):
            raise RuntimeError(f"edge worker {e} did not pass")
        meta.append(m)
        U.append(load_state(root / f"u_{e}.npz"))
        V.append(load_state(root / f"v_{e}.npz"))

    K = matrix(U, U)
    A = matrix(U, V)
    B = matrix(V, V)
    kfit = orbit_fit(K)
    afit = orbit_fit(A)
    bfit = orbit_fit(B)

    dynamic = {}
    for ir in ("A1", "E", "T2"):
        k = kfit[f"lambda_{ir}"]
        a = afit[f"lambda_{ir}"]
        b = bfit[f"lambda_{ir}"]
        if k <= 1e-12:
            raise RuntimeError(f"nonpositive first-shell Gram eigenvalue in {ir}: {k}")
        h1 = a / k
        h2 = b / k
        var = h2 - h1*h1
        dynamic[ir] = {
            "K": k,
            "A": a,
            "B": b,
            "h1_normalized": h1,
            "h2_normalized": h2,
            "Sigma2_depth2": var,
        }

    d_h2 = dynamic["E"]["h2_normalized"] - dynamic["T2"]["h2_normalized"]
    d_var = dynamic["E"]["Sigma2_depth2"] - dynamic["T2"]["Sigma2_depth2"]
    mean_h2 = 0.5*(dynamic["E"]["h2_normalized"] + dynamic["T2"]["h2_normalized"])
    mean_var = 0.5*(dynamic["E"]["Sigma2_depth2"] + dynamic["T2"]["Sigma2_depth2"])

    finite = all(np.isfinite(x) for M in (K,A,B) for x in (M.real.ravel().tolist()+M.imag.ravel().tolist()))
    variance_ok = min(v["Sigma2_depth2"] for v in dynamic.values()) > -3e-6
    symmetry_ok = all(
        f["hermiticity_relative_defect"] < TOL
        and f["three_representative_orbit_residual"] < TOL
        for f in (kfit, afit, bfit)
    )
    passed = bool(finite and variance_ok and symmetry_ok)

    return {
        "status": "exact symmetry-reduced L1 metric-edge depth-two Euclidean Krylov response",
        "passed": passed,
        "science_status": "L1_METRIC_EDGE_DEPTH2_KRYLOV",
        "source_branch": "research/physicalization-l1-depth2-metric",
        "edge_representatives": [m["edge"] for m in meta],
        "definition": {
            "u_e": "(1/2) sum_{4 chambers->e} H_c|Omega>",
            "H_B": "sum of H_w over all 24 chambers in parent block",
            "v_e": "H_B u_e",
            "K": "<u_e|u_f>",
            "A": "<u_e|H_B u_f>",
            "B": "<H_B u_e|H_B u_f>",
        },
        "K_three_representatives": [[ [float(z.real),float(z.imag)] for z in row] for row in K],
        "A_three_representatives": [[ [float(z.real),float(z.imag)] for z in row] for row in A],
        "B_three_representatives": [[ [float(z.real),float(z.imag)] for z in row] for row in B],
        "K_orbit": kfit,
        "A_orbit": afit,
        "B_orbit": bfit,
        "dynamic_irreps": dynamic,
        "Delta_ET_h2": d_h2,
        "relative_ET_h2_split": d_h2/mean_h2 if abs(mean_h2)>1e-30 else None,
        "Delta_ET_Sigma2": d_var,
        "relative_ET_Sigma2_split": d_var/mean_var if abs(mean_var)>1e-30 else None,
        "checks": {
            "finite": finite,
            "S4_three_orbit_consistency": symmetry_ok,
            "nonnegative_depth2_variance_with_tolerance": variance_ok,
        },
        "worker_diagnostics": meta,
        "interpretation": (
            "This is a genuine full-E, depth-two dynamical response on the first refined six-edge metric carrier. "
            "Its E-T2 split tests whether tetrahedral metric anisotropy is enhanced or suppressed by the next Krylov shell. "
            "It is not yet a Lorentzian pole coefficient and must not be named zeta4 until the effective-action/TT propagator bridge is completed."
        ),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    out = run(a.root)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k not in ("worker_diagnostics","K_three_representatives","A_three_representatives","B_three_representatives")}, indent=2))
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
