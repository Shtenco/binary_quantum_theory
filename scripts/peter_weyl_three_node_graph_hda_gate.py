#!/usr/bin/env python3
"""Three-node graph-changing Peter-Weyl x route HDA scaling gate.

This extends the frozen two-node Euclidean calculation to three distinct K5
nodes without projecting the Hamiltonian outputs back to the all-j=1/2 sector.
States with j=0 links are retained, so cylindrical graph reduction is visible
inside the same sparse Peter-Weyl supergraph representation.

For nodes i in {0,1,2}, define

    H_g[N] = sum_i N_i H_i^E
    H_joint[N] = H_g[N] + R[N;Q]

with the same square-root route-normal operator used by the existing HDA gates.
On the frozen initial state the commutator decomposes exactly into

    [R_N,R_M] + C_cross
      + sum_{i<j}(N_i M_j-N_j M_i)[H_i^E,H_j^E].

The target D[Q^(ab)(N d_b M-M d_b N)] is fixed independently.  The test keeps
all graph/spin-changing Peter-Weyl outputs and asks whether cross and pure
geometry channels become regulator-suppressed relative to D on one common
off-shell WKB habitat family.

This is a genuine three-node finite graph-changing scaling control, not a proof
for arbitrary graphs, the Lorentzian H_L amplitudes or an already-removed
continuum regulator.
"""
from __future__ import annotations

import argparse
import itertools
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

NODES = (0, 1, 2)
NODE_COORDS = {
    0: (0.0, 0.0),
    1: (2.0 * math.pi / 3.0, 0.0),
    2: (0.0, 2.0 * math.pi / 3.0),
}


def sparse_array_norm2(state: dict) -> float:
    return float(sum(np.vdot(v, v).real for v in state.values()))


def add_array(dst: dict, key, arr) -> None:
    if key in dst:
        dst[key] = dst[key] + arr
    else:
        dst[key] = arr.copy()


def add_scalar(dst: dict, src: dict, scale: complex = 1.0) -> None:
    for key, amp in src.items():
        val = dst.get(key, 0j) + scale * amp
        if abs(val) > 1e-11:
            dst[key] = val
        elif key in dst:
            del dst[key]


def shared_metric(key) -> np.ndarray:
    # Same local-leg prescription at all three nodes; averaging makes one
    # positive route metric without selecting a preferred node.
    mats = [LOCAL.flux_gram2(key, v, 1, 2) for v in NODES]
    Q = sum(mats) / len(mats)
    return 0.5 * (Q + Q.T)


def geometry_data(initial, JMAX2=5):
    psi0 = {initial: 1 + 0j}
    h = {
        v: PW.prune_state(PW.apply_H_cached_state(psi0, v, JMAX2), 1e-8)
        for v in NODES
    }
    comm = {}
    for i, j in itertools.combinations(NODES, 2):
        hi_hj = PW.compose_on_sparse(h[j], i, JMAX2)  # H_i H_j
        hj_hi = PW.compose_on_sparse(h[i], j, JMAX2)  # H_j H_i
        cij = {}
        PW.add_dict(cij, hi_hj, +1)
        PW.add_dict(cij, hj_hi, -1)
        comm[(i, j)] = PW.prune_state(cij, 1e-8)
    return h, comm


def node_weights(epsilon: float) -> tuple[dict[int, float], dict[int, float]]:
    N0, M0 = 0.9, 1.1
    n = {}
    m = {}
    for v, (y, z) in NODE_COORDS.items():
        nvar = 0.13 * math.sin(y) + 0.07 * math.cos(z)
        mvar = 0.11 * math.cos(y) + 0.09 * math.sin(z)
        n[v] = N0 + epsilon * nvar
        m[v] = M0 + epsilon * mvar
    return n, m


def canonical_reduced_spin_graph(spins: tuple[int, ...]) -> tuple:
    """Exact colored-graph isomorphism signature after deleting j=0 links."""
    nonzero = [(u, v, spins[PW.EIDX[(u, v)]]) for u, v in PW.EDGES if spins[PW.EIDX[(u, v)]] > 0]
    if not nonzero:
        return tuple()
    active = sorted({x for u, v, _ in nonzero for x in (u, v)})
    best = None
    for perm in itertools.permutations(range(len(active))):
        relabel = {old: perm[k] for k, old in enumerate(active)}
        sig = tuple(sorted(
            (min(relabel[u], relabel[v]), max(relabel[u], relabel[v]), int(s))
            for u, v, s in nonzero
        ))
        if best is None or sig < best:
            best = sig
    return best


def graph_diagnostics(comm: dict) -> dict[str, object]:
    pair_rows = []
    orbit_union = set()
    for pair, state in comm.items():
        total = PW.norm2_state(state)
        changed = sum(abs(a) ** 2 for k, a in state.items() if any(s == 0 for s in k[0]))
        orbits = {canonical_reduced_spin_graph(k[0]) for k in state}
        orbit_union.update(orbits)
        pair_rows.append({
            "nodes": list(pair),
            "support": len(state),
            "norm": math.sqrt(total),
            "j0_cylindrical_graph_change_norm2_fraction": float(changed / total) if total else 0.0,
            "reduced_colored_graph_orbits": len(orbits),
        })
    return {
        "pairs": pair_rows,
        "union_reduced_colored_graph_orbits": len(orbit_union),
        "minimum_pair_graph_change_fraction": min(r["j0_cylindrical_graph_change_norm2_fraction"] for r in pair_rows),
    }


def one_epsilon(initial, h, comm, metrics, epsilon, L=48, carrier=8):
    Y, Z, KY, KZ, dphys = LOCAL.spectral_setup(L, epsilon)
    N = 0.9 + epsilon * (0.13 * np.sin(Y) + 0.07 * np.cos(Z))
    M = 1.1 + epsilon * (0.11 * np.cos(Y) + 0.09 * np.sin(Z))
    f = np.exp(1j * (carrier * Y + (carrier - 1) * Z))
    nw, mw = node_weights(epsilon)

    Q0 = metrics[initial]
    RN0 = LOCAL.route_apply(N, f, Q0, KY, KZ, epsilon)
    RM0 = LOCAL.route_apply(M, f, Q0, KY, KZ, epsilon)
    RR = LOCAL.route_apply(N, RM0, Q0, KY, KZ, epsilon) - LOCAL.route_apply(M, RN0, Q0, KY, KZ, epsilon)
    D = LOCAL.route_target(N, M, f, Q0, dphys)
    Dnorm = float(np.linalg.norm(D))
    route_residual = RR + D

    cross = {}
    for v in NODES:
        for ko, amp in h[v].items():
            Qg = metrics[ko]
            RMg = LOCAL.route_apply(M, f, Qg, KY, KZ, epsilon)
            RNg = LOCAL.route_apply(N, f, Qg, KY, KZ, epsilon)
            val = amp * (
                nw[v] * (RM0 - RMg)
                + mw[v] * (RNg - RN0)
            )
            if np.linalg.norm(val) > 1e-12:
                add_array(cross, ko, val)

    gg = {}
    pair_smears = {}
    for (i, j), cij in comm.items():
        smear = nw[i] * mw[j] - nw[j] * mw[i]
        pair_smears[f"{i}-{j}"] = smear
        for ko, amp in cij.items():
            val = (smear * amp) * f
            if np.linalg.norm(val) > 1e-12:
                add_array(gg, ko, val)

    residual = {initial: route_residual.copy()}
    for key, val in cross.items():
        add_array(residual, key, val)
    for key, val in gg.items():
        add_array(residual, key, val)

    route_ratio = float(np.linalg.norm(route_residual) / max(Dnorm, 1e-30))
    cross_ratio = math.sqrt(sparse_array_norm2(cross)) / max(Dnorm, 1e-30)
    gg_ratio = math.sqrt(sparse_array_norm2(gg)) / max(Dnorm, 1e-30)
    joint_ratio = math.sqrt(sparse_array_norm2(residual)) / max(Dnorm, 1e-30)

    gg_total = sparse_array_norm2(gg)
    gg_changed = sum(
        float(np.vdot(val, val).real)
        for key, val in gg.items()
        if any(s == 0 for s in key[0])
    )
    return {
        "epsilon": epsilon,
        "node_N": {str(k): v for k, v in nw.items()},
        "node_M": {str(k): v for k, v in mw.items()},
        "pair_geometry_smears": pair_smears,
        "route_only_defect": route_ratio,
        "cross_over_D": cross_ratio,
        "pure_geometry_over_D": gg_ratio,
        "joint_defect_over_D": joint_ratio,
        "D_norm": Dnorm,
        "cross_support": len(cross),
        "pure_geometry_support": len(gg),
        "pure_geometry_j0_graph_change_fraction": float(gg_changed / gg_total) if gg_total else 0.0,
    }


def fit_power(eps, values) -> float:
    return float(np.polyfit(np.log(np.asarray(eps, float)), np.log(np.asarray(values, float)), 1)[0])


def run(L=48, carrier=8):
    JMAX2 = 5
    initial = PW.basis_full_jhalf()[0]
    h, comm = geometry_data(initial, JMAX2)

    metric_keys = {initial}
    for state in h.values():
        metric_keys.update(state.keys())
    metrics = {key: shared_metric(key) for key in metric_keys}
    min_metric_eig = min(float(np.linalg.eigvalsh(Q).min()) for Q in metrics.values())

    eps = [0.25, 0.125, 0.0625, 0.03125, 0.015625]
    rows = [one_epsilon(initial, h, comm, metrics, e, L, carrier) for e in eps]
    route = [r["route_only_defect"] for r in rows]
    cross = [r["cross_over_D"] for r in rows]
    geom = [r["pure_geometry_over_D"] for r in rows]
    joint = [r["joint_defect_over_D"] for r in rows]

    p_route = fit_power(eps, route)
    p_cross = fit_power(eps, cross)
    p_geom = fit_power(eps, geom)
    p_joint = fit_power(eps, joint)
    graphs = graph_diagnostics(comm)

    checks = {
        "three_distinct_nodes": len(NODES) == 3,
        "all_single_node_actions_nonzero": all(len(h[v]) > 0 for v in NODES),
        "all_three_pair_commutators_nonzero": all(len(comm[p]) > 0 for p in comm),
        "metric_positive_on_one_hit_space": min_metric_eig > -1e-9,
        "cylindrical_graph_change_present": graphs["minimum_pair_graph_change_fraction"] > 0.30,
        "multiple_reduced_graph_orbits": graphs["union_reduced_colored_graph_orbits"] >= 10,
        "route_scaling": 0.70 <= p_route <= 1.35 and route[-1] < 1e-4,
        "cross_scaling": 0.70 <= p_cross <= 1.35,
        "geometry_scaling": 1.60 <= p_geom <= 2.40,
        "joint_scaling": 0.70 <= p_joint <= 1.35,
        "joint_smallest_regulator": joint[-1] < 0.05,
        "graph_change_survives_geometry_channel": rows[-1]["pure_geometry_j0_graph_change_fraction"] > 0.20,
    }

    return {
        "status": "three-node graph-changing Euclidean Peter-Weyl x route HDA scaling control",
        "passed": bool(all(checks.values())),
        "Jmax": 2.5,
        "nodes": list(NODES),
        "node_coordinates": {str(k): list(v) for k, v in NODE_COORDS.items()},
        "input": "all ten K5 links j=1/2; all five K=0; no projection after H actions",
        "single_node_support": {str(v): len(h[v]) for v in NODES},
        "pair_commutator_support": {f"{i}-{j}": len(comm[(i, j)]) for i, j in itertools.combinations(NODES, 2)},
        "graph_change": graphs,
        "minimum_metric_eigenvalue": min_metric_eig,
        "L": L,
        "carrier": carrier,
        "rows": rows,
        "fitted_route_exponent": p_route,
        "fitted_cross_exponent": p_cross,
        "fitted_pure_geometry_exponent": p_geom,
        "fitted_joint_exponent": p_joint,
        "checks": checks,
        "claim_boundary": (
            "This is the first >=3-node off-shell finite control that retains j=0/reduced-graph outputs instead of projecting to the original spin sector. "
            "A PASS establishes the predicted regulator hierarchy on this frozen Euclidean K5 habitat family. It is not arbitrary-graph Lorentzian HDA closure and does not by itself justify status 'proved'."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--L", type=int, default=48)
    ap.add_argument("--carrier", type=int, default=8)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.L, args.carrier)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
