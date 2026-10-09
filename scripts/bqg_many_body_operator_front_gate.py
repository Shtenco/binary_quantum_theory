#!/usr/bin/env python3
"""Regression gate for many-body support order and exact gapped front velocity."""
from __future__ import annotations

import math
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]], dtype=complex)
Z = np.array([[1,0],[0,-1]], dtype=complex)


def kron_op(n, mapping):
    out = np.array([[1.0+0j]])
    for q in range(n):
        out = np.kron(out, mapping.get(q, I))
    return out


def xx_chain(n, weights, fields):
    H = np.zeros((2**n, 2**n), dtype=complex)
    for i, J in enumerate(weights):
        H += J/2 * (
            kron_op(n, {i:X, i+1:X})
            + kron_op(n, {i:Y, i+1:Y})
        )
    for i, h in enumerate(fields):
        H += h * kron_op(n, {i:Z})
    return H


def comm(A,B):
    return A@B-B@A


def first_commutator_order(H, A, B, max_order, tol=1e-9):
    C = A.copy()
    for n in range(max_order+1):
        if np.linalg.norm(comm(C,B)) > tol:
            return n
        C = comm(H,C)
    return None


def vmax_exact(m):
    return math.sqrt(4*m*m+9)-2*abs(m)


def xi_exact(m):
    if m == 0:
        return math.inf
    return 1/math.asinh(2*abs(m)/3)


def vmax_grid(m, n=200001):
    k = np.linspace(0, math.pi/2, n)
    E = np.sqrt(4*m*m+9*np.cos(k)**2)
    v = 9*np.abs(np.sin(k)*np.cos(k))/E
    return float(np.max(v))


def run():
    rng = np.random.default_rng(7)

    chain_tests = 0
    for n in range(2, 7):
        for _ in range(4):
            weights = rng.uniform(0.15, 1.3, n-1)
            fields = rng.normal(0, 1.5, n)
            H = xx_chain(n, weights, fields)
            A = kron_op(n, {0:Z})
            for j in range(1,n):
                B = kron_op(n, {j:Z})
                found = first_commutator_order(H,A,B,j+1)
                assert found == j, (n,j,found)
                chain_tests += 1

    masses = [0.0,0.2,0.5,1.0,2.0,5.0]
    for m in masses:
        vg = vmax_grid(m)
        ve = vmax_exact(m)
        assert abs(vg-ve) < 3e-5, (m,vg,ve)
        if m == 0:
            assert abs(ve-3.0) < 1e-14
        else:
            xi = xi_exact(m)
            assert abs(ve/3-math.exp(-1/xi)) < 1e-13
            gap = 2*abs(m)
            assert abs(ve-(math.sqrt(gap*gap+9)-gap)) < 1e-13

    print("many_body_chain_endpoint_tests =", chain_tests)
    print("vmax(0) =", vmax_exact(0))
    for m in masses[1:]:
        print(
            f"m={m:g}",
            "xi=", xi_exact(m),
            "vmax=", vmax_exact(m),
            "vmax/3=", vmax_exact(m)/3,
        )
    print("NESTED COMMUTATOR DISTANCE ORDER PASS")
    print("EXACT GAPPED VMAX PASS")
    print("VMAX / 3 = EXP(-1/XI) PASS")
    print("PASS")


if __name__ == "__main__":
    run()
