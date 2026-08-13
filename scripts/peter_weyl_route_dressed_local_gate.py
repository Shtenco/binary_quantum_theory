#!/usr/bin/env python3
"""Regulator-safe Peter-Weyl H_E coupled to the route-normal generator.

This is the first joint geometry x route calculation that uses a genuine
Peter-Weyl Hamiltonian matrix element rather than an abstract geometry qubit.
It deliberately stays local (one K5 node) so that the geometry Hamiltonian is
needed only once; the expensive HH geometry composition is not required.

On a local route patch of physical size epsilon, write

    N(y)=N0+epsilon*n(y),   M(y)=M0+epsilon*m(y),
    P_phys=P_y/epsilon.

For every Gauss spin-network basis state g, reconstruct a positive densitized
2-metric Q_g^{ab}=<E^a_i E^b_i> from two non-collinear local flux legs and set

    Omega_g = sqrt(Q_g^{ab} P_a P_b),
    R_g[N]  = 1/2 {N, Omega_g}.

The local joint constraint is the embedding/habitat completion

    H_joint[N] = N0 H_E^safe + R[N;Q].

Because the same genuine H_E changes Q, [H_E,R] is nonzero.  The antisymmetric
cross term is nevertheless expected to be regulator suppressed: its constant
N0*M0 part cancels exactly, leaving O(epsilon) relative to the route HDA term.

The geometry operator is the Jmax=5/2, genuine-volume, orientation-covariant
Hamiltonian from k5_peter_weyl_safe_hda_column.py.  Thus this gate tests the
actual first safe Euclidean Peter-Weyl move.  It is not yet the full two-node
H_E+H_L commutator and therefore is not a full quantum-GR HDA closure claim.
"""
from __future__ import annotations

import argparse
import functools
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import k5_peter_weyl_safe_hda_column as PW


@functools.lru_cache(None)
def flux_gram2(key, v: int = 0, leg_a: int = 0, leg_b: int = 2):
    """Diagonal intertwiner expectation of a 2x2 densitized flux Gram matrix."""
    spins, Ks = key
    ls = PW.local_spins(spins, v)
    T = PW.oriented_intertwiner(v, ls, Ks[v])
    nrm = float(np.vdot(T, T).real)
    if nrm <= 1e-15:
        raise RuntimeError("zero-norm intertwiner")
    legs = (leg_a, leg_b)
    acted = {}
    for ia, leg in enumerate(legs):
        mats = PW.spin_mats_cached(ls[leg])
        for c in range(3):
            acted[(ia, c)] = PW.apply_axis_np(T, leg, mats[c])
    Q = np.zeros((2, 2), float)
    for a in range(2):
        for b in range(2):
            val = sum(np.vdot(acted[(a, c)], acted[(b, c)]) for c in range(3)) / nrm
            Q[a, b] = float(val.real)
    Q = 0.5 * (Q + Q.T)
    ev = np.linalg.eigvalsh(Q)
    if ev.min() < -1e-10:
        raise RuntimeError(f"flux Gram lost positivity: {ev}")
    return Q


def spectral_setup(L: int, epsilon: float):
    y = 2 * np.pi * np.arange(L) / L
    Y, Z = np.meshgrid(y, y, indexing="ij")
    k = np.fft.fftfreq(L, d=1.0 / L)
    KY, KZ = np.meshgrid(k, k, indexing="ij")

    def dphys(f, axis):
        K = KY if axis == 0 else KZ
        return np.fft.ifft2((1j * K / epsilon) * np.fft.fft2(f))

    return Y, Z, KY, KZ, dphys


def omega_apply(f, Q, KY, KZ, epsilon):
    symbol2 = Q[0, 0] * KY * KY + 2 * Q[0, 1] * KY * KZ + Q[1, 1] * KZ * KZ
    symbol = np.sqrt(np.maximum(symbol2, 0.0)) / epsilon
    return np.fft.ifft2(symbol * np.fft.fft2(f))


def route_apply(A, f, Q, KY, KZ, epsilon):
    Omf = omega_apply(f, Q, KY, KZ, epsilon)
    return 0.5 * (A * Omf + omega_apply(A * f, Q, KY, KZ, epsilon))


def route_target(N, M, f, Q, dphys):
    dN = np.stack([dphys(N, 0), dphys(N, 1)])
    dM = np.stack([dphys(M, 0), dphys(M, 1)])
    oneform = N[None, ...] * dM - M[None, ...] * dN
    beta = np.einsum("ab,bij->aij", Q, oneform)
    df = np.stack([dphys(f, 0), dphys(f, 1)])
    div = dphys(beta[0], 0) + dphys(beta[1], 1)
    # L_beta on half-densities.  The repository orientation has [R_N,R_M] -> -L_beta.
    return beta[0] * df[0] + beta[1] * df[1] + 0.5 * div * f


def sparse_norm2(state):
    return float(sum(np.vdot(v, v).real for v in state.values()))


def add_sparse(dst, key, val):
    if key in dst:
        dst[key] = dst[key] + val
    else:
        dst[key] = val.copy()


def one_epsilon(initial, h0, metrics, epsilon, L, carrier):
    Y, Z, KY, KZ, dphys = spectral_setup(L, epsilon)
    N0, M0 = 0.9, 1.1
    nvar = 0.13 * np.sin(Y) + 0.07 * np.cos(Z)
    mvar = 0.11 * np.cos(Y) + 0.09 * np.sin(Z)
    N = N0 + epsilon * nvar
    M = M0 + epsilon * mvar
    f = np.exp(1j * (carrier * Y + (carrier - 1) * Z))

    Q0 = metrics[initial]
    RN0 = route_apply(N, f, Q0, KY, KZ, epsilon)
    RM0 = route_apply(M, f, Q0, KY, KZ, epsilon)
    RR = route_apply(N, RM0, Q0, KY, KZ, epsilon) - route_apply(M, RN0, Q0, KY, KZ, epsilon)
    D = route_target(N, M, f, Q0, dphys)
    route_defect = float(np.linalg.norm(RR + D) / max(np.linalg.norm(D), 1e-30))

    # Exact cross action on |initial> tensor |f>, requiring H_E only once:
    # Cx = N0 [H_E,R_M] - M0 [H_E,R_N].
    cross = {}
    for ko, amp in h0.items():
        Qg = metrics[ko]
        RMg = route_apply(M, f, Qg, KY, KZ, epsilon)
        RNg = route_apply(N, f, Qg, KY, KZ, epsilon)
        val = amp * (N0 * (RM0 - RMg) - M0 * (RN0 - RNg))
        if np.linalg.norm(val) > 1e-12:
            add_sparse(cross, ko, val)

    target = {initial: -D}
    total = {initial: RR.copy()}
    for k, v in cross.items():
        add_sparse(total, k, v)
    residual = dict(total)
    add_sparse(residual, initial, D)  # total - (-D)

    cross_norm = math.sqrt(sparse_norm2(cross))
    Dnorm = float(np.linalg.norm(D))
    total_defect = math.sqrt(sparse_norm2(residual)) / max(Dnorm, 1e-30)
    cross_ratio = cross_norm / max(Dnorm, 1e-30)
    return {
        "epsilon": epsilon,
        "carrier": carrier,
        "route_only_defect": route_defect,
        "cross_anomaly_over_D": cross_ratio,
        "joint_defect_over_D": total_defect,
        "D_norm": Dnorm,
        "cross_support": len(cross),
    }


def run(L=48, carrier=8):
    JMAX2 = 5
    initial = PW.basis_full_jhalf()[0]
    psi0 = {initial: 1 + 0j}
    h0 = PW.prune_state(PW.apply_H_cached_state(psi0, 0, JMAX2), 1e-8)
    h0_norm = math.sqrt(PW.norm2_state(h0))

    metrics = {initial: flux_gram2(initial)}
    for key in h0:
        metrics[key] = flux_gram2(key)
    Q0 = metrics[initial]
    expected_Q0 = 0.75 * np.eye(2)
    initial_metric_error = float(np.linalg.norm(Q0 - expected_Q0))
    mineig = min(float(np.linalg.eigvalsh(Q).min()) for Q in metrics.values())
    metric_change = [float(np.linalg.norm(metrics[k] - Q0)) for k in h0]
    amps = np.asarray([abs(a) ** 2 for a in h0.values()], float)
    weighted_metric_change = float(np.dot(amps, metric_change) / max(amps.sum(), 1e-30))

    epsilons = np.asarray([0.5, 0.25, 0.125, 0.0625, 0.03125], float)
    rows = [one_epsilon(initial, h0, metrics, float(e), L, carrier) for e in epsilons]
    cross = np.asarray([r["cross_anomaly_over_D"] for r in rows])
    joint = np.asarray([r["joint_defect_over_D"] for r in rows])
    route = np.asarray([r["route_only_defect"] for r in rows])
    pcross = float(np.polyfit(np.log(epsilons), np.log(cross), 1)[0])
    pjoint = float(np.polyfit(np.log(epsilons), np.log(joint), 1)[0])

    passed = (
        len(h0) > 0
        and h0_norm > 1e-10
        and initial_metric_error < 1e-10
        and mineig > -1e-9
        and weighted_metric_change > 1e-6
        and 0.75 < pcross < 1.25
        and 0.75 < pjoint < 1.25
        and route[-1] < 2e-4
        and joint[-1] < 2e-2
    )
    return {
        "status": "regulator-safe Peter-Weyl H_E x route-normal local joint gate",
        "passed": bool(passed),
        "Jmax": 2.5,
        "node": 0,
        "input": "all ten links j=1/2; all five K=0",
        "H0_support": len(h0),
        "H0_norm": h0_norm,
        "metric_definition": "Q_ab=<J_leg_a dot J_leg_b>, local legs (0,2); densitized inverse-metric proxy with no inverse volume",
        "initial_Q": Q0.tolist(),
        "initial_Q_expected": expected_Q0.tolist(),
        "initial_Q_error": initial_metric_error,
        "minimum_metric_eigenvalue_over_reached_states": mineig,
        "weighted_metric_change_under_H0": weighted_metric_change,
        "L": L,
        "carrier": carrier,
        "rows": rows,
        "cross_anomaly_regulator_exponent": pcross,
        "joint_defect_regulator_exponent": pjoint,
        "last_route_only_defect": float(route[-1]),
        "last_cross_anomaly_over_D": float(cross[-1]),
        "last_joint_defect_over_D": float(joint[-1]),
        "operator": "H_joint[N]=N(v) H_E^safe + 1/2{N,sqrt(Q_g^{ab}P_aP_b)} on the local habitat patch",
        "interpretation": (
            "The genuine safe Euclidean Peter-Weyl move changes the local flux metric, so the geometry-route cross commutator is nonzero. "
            "Its antisymmetric constant-lapse part cancels and the remaining cross anomaly is regulator suppressed. "
            "This is the first real Peter-Weyl x route coupling gate, but it is local/Euclidean and uses diagonal intertwiner metric expectations; full two-node Lorentzian HH remains open."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--L", type=int, default=48)
    ap.add_argument("--carrier", type=int, default=8)
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    out = run(a.L, a.carrier)
    text = json.dumps(out, indent=2)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
