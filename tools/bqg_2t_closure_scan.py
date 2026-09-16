#!/usr/bin/env python3
"""Generic falsification-first scanner for a candidate BQG -> Sp(2,R) closure.

Input: JSON containing square matrices under `generators`, e.g.
{"generators": {"C1": [[...]], "C2": [[...]], "C3": [[...]]}}

The scanner never manufactures physical BQG generators. It only tests matrices
that have already been derived elsewhere. It reports commutator residuals,
least-squares structure constants, Jacobi residual, and the Killing form.

Dependencies: Python 3 + NumPy.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np


def comm(a, b):
    return a @ b - b @ a


def frob(a):
    return float(np.linalg.norm(a, "fro"))


def fit_structure(gens):
    names = list(gens)
    basis = [gens[n] for n in names]
    A = np.column_stack([x.reshape(-1) for x in basis])
    coeff = np.zeros((len(names), len(names), len(names)), dtype=np.complex128)
    residual = np.zeros((len(names), len(names)), dtype=float)
    for i in range(len(names)):
        for j in range(len(names)):
            cij = comm(basis[i], basis[j]).reshape(-1)
            x, *_ = np.linalg.lstsq(A, cij, rcond=None)
            fit = A @ x
            denom = max(float(np.linalg.norm(cij)), frob(basis[i]) * frob(basis[j]), 1e-15)
            residual[i, j] = float(np.linalg.norm(cij - fit) / denom)
            coeff[i, j, :] = x
    return names, coeff, residual


def jacobi_residual(gens):
    names = list(gens)
    vals = []
    for a in names:
        for b in names:
            for c in names:
                j = comm(gens[a], comm(gens[b], gens[c]))
                j += comm(gens[b], comm(gens[c], gens[a]))
                j += comm(gens[c], comm(gens[a], gens[b]))
                denom = max(frob(gens[a]) * frob(gens[b]) * frob(gens[c]), 1e-15)
                vals.append(frob(j) / denom)
    return max(vals) if vals else 0.0


def killing_form(coeff):
    # ad_i has entries (ad_i)_j^k = f_{ij}^k.
    n = coeff.shape[0]
    ad = np.empty((n, n, n), dtype=np.complex128)
    for i in range(n):
        ad[i] = coeff[i]
    K = np.empty((n, n), dtype=np.complex128)
    for i in range(n):
        for j in range(n):
            K[i, j] = np.trace(ad[i] @ ad[j])
    return K


def main():
    p = argparse.ArgumentParser()
    p.add_argument("json_file", type=Path)
    p.add_argument("--tol", type=float, default=1e-8)
    args = p.parse_args()

    data = json.loads(args.json_file.read_text(encoding="utf-8"))
    raw = data["generators"]
    gens = {k: np.asarray(v, dtype=np.complex128) for k, v in raw.items()}
    if len(gens) != 3:
        raise SystemExit("This gate expects exactly three candidate generators.")
    shapes = {m.shape for m in gens.values()}
    if len(shapes) != 1 or next(iter(shapes))[0] != next(iter(shapes))[1]:
        raise SystemExit("All generators must be square matrices of the same dimension.")

    names, f, r = fit_structure(gens)
    K = killing_form(f)
    eig = np.linalg.eigvals(K)
    print("BQG -> 2T closure scan")
    print("generators:", names)
    print("max commutator closure residual:", float(r.max()))
    print("Jacobi residual:", jacobi_residual(gens))
    print("Killing eigenvalues:", [complex(x) for x in eig])
    print("structure constants f[i,j,k] (rows i,j; components k):")
    for i, ni in enumerate(names):
        for j, nj in enumerate(names):
            print(ni, nj, [complex(x) for x in f[i, j]])

    passed = bool(r.max() <= args.tol and jacobi_residual(gens) <= args.tol)
    print("finite closure:", "PASS" if passed else "FAIL")
    print("NOTE: closure is necessary, not sufficient, for Sp(2,R). Canonical two-time and (d,2) signature gates remain separate.")


if __name__ == "__main__":
    main()
