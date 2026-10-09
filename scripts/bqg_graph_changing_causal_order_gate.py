#!/usr/bin/env python3
"""Regression gate for the BQG graph-changing causal-order theorem."""
from __future__ import annotations

import math
import numpy as np


def sl(nsec, d, s):
    return slice(s*d, (s+1)*d)


def make_local_constraints(rng, nsec, d, ncon):
    N = nsec*d
    out = []
    for _ in range(ncon):
        C = np.zeros((N,N), dtype=complex)
        for s in range(nsec):
            C[sl(nsec,d,s), sl(nsec,d,s)] = (
                rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
            )
            if s+1 < nsec:
                C[sl(nsec,d,s+1), sl(nsec,d,s)] = (
                    rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
                )
                C[sl(nsec,d,s), sl(nsec,d,s+1)] = (
                    rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
                )
        out.append(C)
    return out


def positive_metric(rng, n):
    A = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    return A.conj().T @ A + np.eye(n)


def master(Cs, G):
    M = np.zeros_like(Cs[0])
    for a,Ca in enumerate(Cs):
        for b,Cb in enumerate(Cs):
            M += G[a,b] * Ca.conj().T @ Cb
    return (M + M.conj().T)/2


def block(A, nsec, d, src, dst):
    return A[sl(nsec,d,dst), sl(nsec,d,src)]


def first_order(M, nsec, d, src, dst, maxn=16, tol=1e-9):
    P = np.eye(M.shape[0], dtype=complex)
    for n in range(maxn+1):
        if np.linalg.norm(block(P,nsec,d,src,dst)) > tol:
            return n
        P = P @ M
    return None


def test_master_flow():
    rng = np.random.default_rng(20261009)
    total_pairs = 0
    saturated = 0

    for nsec in (5,6,7,8):
        d = 2
        for _ in range(8):
            Cs = make_local_constraints(rng,nsec,d,3)
            G = positive_metric(rng,3)
            M = master(Cs,G)

            # One master factor has elementary radius <=2.
            for a in range(nsec):
                for b in range(nsec):
                    dist = abs(a-b)
                    if dist > 2:
                        assert np.linalg.norm(block(M,nsec,d,a,b)) < 1e-8

            # Powers obey radius <=2n.
            P = np.eye(M.shape[0],dtype=complex)
            for n in range(5):
                for a in range(nsec):
                    for b in range(nsec):
                        if abs(a-b) > 2*n:
                            assert np.linalg.norm(block(P,nsec,d,a,b)) < 1e-7
                P = P @ M

            for a in range(nsec):
                for b in range(nsec):
                    dist = abs(a-b)
                    k = first_order(M,nsec,d,a,b)
                    lower = math.ceil(dist/2)
                    assert k is not None and k >= lower, (a,b,k,lower)
                    if k == lower:
                        saturated += 1
                    total_pairs += 1

    return total_pairs, saturated


def test_relational_step():
    # A strictly one-sector-local system step on a line:
    # powers cannot cross more than t graph edges in t clock ticks.
    nsec = 9
    d = 1
    R = np.zeros((nsec,nsec),dtype=complex)
    # Nonunitary support-control matrix is sufficient for the algebraic
    # locality regression; the theorem applies equally to a unitary local R.
    for s in range(nsec):
        R[s,s] = 0.3
        if s+1<nsec:
            R[s+1,s] = 0.7
    P = np.eye(nsec,dtype=complex)
    checks = 0
    for t in range(nsec):
        for a in range(nsec):
            for b in range(nsec):
                if b-a > t:
                    assert abs(P[b,a]) < 1e-12
                    checks += 1
        P = R @ P
    return checks


def run():
    pairs, saturated = test_master_flow()
    relchecks = test_relational_step()

    print("master sector-pair checks =", pairs)
    print("generic lower-bound saturations =", saturated)
    print("relational locality zero checks =", relchecks)
    print("MASTER RADIUS <= 2 ELEMENTARY CONSTRAINT MOVES PASS")
    print("M^n RADIUS <= 2n PASS")
    print("d_M >= CEIL(d_C/2) PASS")
    print("RELATIONAL GRAPH-HISTORY LOCALITY PASS")
    print("PASS")


if __name__ == "__main__":
    run()
