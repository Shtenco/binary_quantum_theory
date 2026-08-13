#!/usr/bin/env python3
"""Preregistered two-node Peter-Weyl Euclidean x route HDA scaling gate.

The protocol is frozen in PETER_WEYL_TWO_NODE_EUCLIDEAN_PREREGISTRATION.md.
It evaluates the actual regulator-safe Jmax=5/2 [H0^E,H1^E] vector and couples
both nodes to the same geometry-dependent square-root route-normal generator.

The exact decomposition on the frozen input is

  [H[N],H[M]] = [R_N,R_M] + C_cross
                 + (a d-b c)[H0^E,H1^E],

where a=N(x0), b=N(x1), c=M(x0), d=M(x1).
No channel-dependent normalization or subtraction is allowed.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_route_dressed_local_gate as LOCAL


def shared_metric(key):
    # Frozen in preregistration: non-shared local legs (1,2) at nodes 0 and 1.
    q0 = LOCAL.flux_gram2(key, 0, 1, 2)
    q1 = LOCAL.flux_gram2(key, 1, 1, 2)
    return 0.5 * (q0 + q1)


def add_array(dst, key, arr):
    if key in dst:
        dst[key] = dst[key] + arr
    else:
        dst[key] = arr.copy()


def sparse_array_norm2(state):
    return float(sum(np.vdot(v, v).real for v in state.values()))


def commutator_geometry(initial, JMAX2=5):
    psi0 = {initial: 1 + 0j}
    h0 = PW.prune_state(PW.apply_H_cached_state(psi0, 0, JMAX2), 1e-8)
    h1 = PW.prune_state(PW.apply_H_cached_state(psi0, 1, JMAX2), 1e-8)
    h1h0 = PW.compose_on_sparse(h0, 1, JMAX2)  # H1 H0
    h0h1 = PW.compose_on_sparse(h1, 0, JMAX2)  # H0 H1
    comm = {}
    PW.add_dict(comm, h0h1, +1)
    PW.add_dict(comm, h1h0, -1)
    comm = PW.prune_state(comm, 1e-8)
    return h0, h1, comm


def analytic_node_weights(epsilon):
    # Frozen node positions: x0=(0,0), x1=(1,0) in dimensionless route coords.
    def nvar(y, z):
        return 0.13 * math.sin(y) + 0.07 * math.cos(z)
    def mvar(y, z):
        return 0.11 * math.cos(y) + 0.09 * math.sin(z)
    a = 0.9 + epsilon * nvar(0.0, 0.0)
    b = 0.9 + epsilon * nvar(1.0, 0.0)
    c = 1.1 + epsilon * mvar(0.0, 0.0)
    d = 1.1 + epsilon * mvar(1.0, 0.0)
    return a, b, c, d


def one_epsilon(initial, h0, h1, geom_comm, metrics, epsilon, L=48, carrier=8):
    Y, Z, KY, KZ, dphys = LOCAL.spectral_setup(L, epsilon)
    N = 0.9 + epsilon * (0.13 * np.sin(Y) + 0.07 * np.cos(Z))
    M = 1.1 + epsilon * (0.11 * np.cos(Y) + 0.09 * np.sin(Z))
    f = np.exp(1j * (carrier * Y + (carrier - 1) * Z))
    a, b, c, d = analytic_node_weights(epsilon)

    Q0 = metrics[initial]
    RN0 = LOCAL.route_apply(N, f, Q0, KY, KZ, epsilon)
    RM0 = LOCAL.route_apply(M, f, Q0, KY, KZ, epsilon)
    RR = (
        LOCAL.route_apply(N, RM0, Q0, KY, KZ, epsilon)
        - LOCAL.route_apply(M, RN0, Q0, KY, KZ, epsilon)
    )
    D = LOCAL.route_target(N, M, f, Q0, dphys)
    Dnorm = float(np.linalg.norm(D))

    route_residual = RR + D  # repository orientation: RR -> -D
    route_ratio = float(np.linalg.norm(route_residual) / max(Dnorm, 1e-30))

    cross = {}
    for ko, amp in h0.items():
        Qg = metrics[ko]
        RMg = LOCAL.route_apply(M, f, Qg, KY, KZ, epsilon)
        RNg = LOCAL.route_apply(N, f, Qg, KY, KZ, epsilon)
        val = amp * (a * (RM0 - RMg) + c * (RNg - RN0))
        if np.linalg.norm(val) > 1e-12:
            add_array(cross, ko, val)
    for ko, amp in h1.items():
        Qg = metrics[ko]
        RMg = LOCAL.route_apply(M, f, Qg, KY, KZ, epsilon)
        RNg = LOCAL.route_apply(N, f, Qg, KY, KZ, epsilon)
        val = amp * (b * (RM0 - RMg) + d * (RNg - RN0))
        if np.linalg.norm(val) > 1e-12:
            add_array(cross, ko, val)

    smear = a * d - b * c
    gg = {}
    for ko, amp in geom_comm.items():
        val = (smear * amp) * f
        if np.linalg.norm(val) > 1e-12:
            add_array(gg, ko, val)

    residual = {initial: route_residual.copy()}
    for k, v in cross.items():
        add_array(residual, k, v)
    for k, v in gg.items():
        add_array(residual, k, v)

    cross_ratio = math.sqrt(sparse_array_norm2(cross)) / max(Dnorm, 1e-30)
    gg_ratio = math.sqrt(sparse_array_norm2(gg)) / max(Dnorm, 1e-30)
    joint_ratio = math.sqrt(sparse_array_norm2(residual)) / max(Dnorm, 1e-30)
    return {
        "epsilon": epsilon,
        "node_lapse_weights": {"a_N0": a, "b_N1": b, "c_M0": c, "d_M1": d},
        "antisymmetric_geometry_smear": smear,
        "route_only_defect": route_ratio,
        "cross_over_D": cross_ratio,
        "pure_EE_over_D": gg_ratio,
        "joint_defect_over_D": joint_ratio,
        "D_norm": Dnorm,
        "cross_support": len(cross),
        "EE_support": len(gg),
        "residual_support": len(residual),
    }


def fit_power(eps, vals):
    return float(np.polyfit(np.log(np.asarray(eps, float)), np.log(np.asarray(vals, float)), 1)[0])


def run(L=48, carrier=8):
    JMAX2 = 5
    initial = PW.basis_full_jhalf()[0]
    h0, h1, geom_comm = commutator_geometry(initial, JMAX2)
    comm_norm = math.sqrt(PW.norm2_state(geom_comm))
    comm_regression_error = abs(comm_norm - 1.681559985798016)

    metric_keys = {initial, *h0.keys(), *h1.keys()}
    metrics = {key: shared_metric(key) for key in metric_keys}
    Q0 = metrics[initial]
    eigmins = [float(np.linalg.eigvalsh(Q).min()) for Q in metrics.values()]

    eps = [0.25, 0.125, 0.0625, 0.03125, 0.015625]
    rows = [one_epsilon(initial, h0, h1, geom_comm, metrics, e, L, carrier) for e in eps]
    route = [r["route_only_defect"] for r in rows]
    cross = [r["cross_over_D"] for r in rows]
    gee = [r["pure_EE_over_D"] for r in rows]
    joint = [r["joint_defect_over_D"] for r in rows]
    p_cross = fit_power(eps, cross)
    p_ee = fit_power(eps, gee)
    p_joint = fit_power(eps, joint)

    passed = (
        comm_regression_error < 5e-8
        and route[-1] < 1e-4
        and 0.75 <= p_cross <= 1.25
        and 1.75 <= p_ee <= 2.25
        and 0.75 <= p_joint <= 1.25
        and joint[-1] < 0.02
    )
    return {
        "status": "preregistered two-node regulator-safe Euclidean Peter-Weyl x route HDA gate",
        "passed": bool(passed),
        "Jmax": 2.5,
        "nodes": [0, 1],
        "input": "all ten links j=1/2; all five K=0",
        "H0_support": len(h0),
        "H1_support": len(h1),
        "raw_EE_commutator_support": len(geom_comm),
        "raw_EE_commutator_norm": comm_norm,
        "raw_EE_commutator_norm_regression_error": comm_regression_error,
        "shared_initial_Q": Q0.tolist(),
        "minimum_shared_metric_eigenvalue": min(eigmins),
        "L": L,
        "carrier": carrier,
        "rows": rows,
        "fitted_cross_exponent": p_cross,
        "fitted_pure_EE_relative_exponent": p_ee,
        "fitted_joint_exponent": p_joint,
        "last_route_only_defect": route[-1],
        "last_cross_over_D": cross[-1],
        "last_pure_EE_over_D": gee[-1],
        "last_joint_defect_over_D": joint[-1],
        "exact_decomposition": "[H[N],H[M]]=[R_N,R_M]+C_cross+(ad-bc)[H0^E,H1^E]",
        "scope_note": (
            "Two-node Euclidean off-shell scaling control on one frozen WKB route probe. "
            "It uses actual safe Peter-Weyl H0/H1 amplitudes and no fitted channel normalization. "
            "It does not include Lorentzian H_L amplitudes, the full operator-valued flux metric, multiple habitat probes or collective-spin scaling."
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
