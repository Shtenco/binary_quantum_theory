#!/usr/bin/env python3
"""Exact full-E depth-two worker for one coarse metric edge of an L1 block.

The first barycentric refinement of one parent tetrahedron contains 24 fine
chambers, indexed by S4 permutations.  For one unordered parent edge e, define

    |u_e> = (1/2) sum_{chambers c with first pair=e} H_c |Omega>.

The factor 1/2 is the normalized four-chamber S4-equivariant compression.
Unlike the q4 lower-bound projection, H_c here is the full production
physical-sine Euclidean operator with all plaquette lengths.

Then act with the full parent-block Hamiltonian

    H_B = sum_{w in the 24 fine chambers} H_w

and save

    |v_e> = H_B |u_e>.

Three directly computed edge representatives (01), (02), (23) determine the
same/adjacent/opposite S4 orbits.  No amplitude covariance is substituted.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import time
import traceback
from collections import Counter
from pathlib import Path

import numpy as np

import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from pl_dual_complex import DualComplex, seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean
from collective_barycentric_E_boundary_support_gate import barycentric_with_parent


JMAX2 = 5
TOL = 1e-10
PERMS = list(itertools.permutations(range(4)))
EDGES = list(itertools.combinations(range(4), 2))
REPRESENTATIVES = (0, 1, 5)  # 01, 02, 23 => same / adjacent / opposite


def add(dst, src, scale=1.0):
    for k, a in src.items():
        z = dst.get(k, 0j) + scale * a
        if abs(z) > TOL:
            dst[k] = z
        elif k in dst:
            del dst[k]


def norm(state):
    return math.sqrt(sum(abs(a) ** 2 for a in state.values()))


def max_spin(state):
    return max((max(k[0]) for k in state), default=0) / 2.0


def save_state(path: Path, state, nedges: int, nverts: int):
    rows = sorted(state.items(), key=lambda kv: repr(kv[0]))
    if rows:
        spins = np.asarray([k[0] for k, _ in rows], np.int16)
        Ks = np.asarray([k[1] for k, _ in rows], np.int16)
        amp = np.asarray([a for _, a in rows], np.complex128)
    else:
        spins = np.zeros((0, nedges), np.int16)
        Ks = np.zeros((0, nverts), np.int16)
        amp = np.zeros((0,), np.complex128)
    np.savez_compressed(path, spins=spins, Ks=Ks, amp=amp)


def diagnostics(state, seed):
    changed = Counter(sum(a != b for a, b in zip(key[0], seed[0])) for key in state)
    parity = Counter(sum(key[0]) % 2 for key in state)
    return {
        "support": len(state),
        "norm": norm(state),
        "max_spin": max_spin(state),
        "changed_edge_count_distribution": {str(k): v for k, v in sorted(changed.items())},
        "sum_doubled_spin_parity_distribution": {str(k): v for k, v in sorted(parity.items())},
    }


def run(edge_index: int, parent_id: int = 0):
    if edge_index not in REPRESENTATIVES:
        raise ValueError(f"pilot representative must be one of {REPRESENTATIVES}")

    ZVM.patch_and_clear()
    coarse = seed_16cell_boundary()
    fine, parent = barycentric_with_parent(coarse)
    D = DualComplex(fine)
    G = PLPeterWeylEuclidean(D)
    inside = sorted(v for v, p in enumerate(parent) if p == parent_id)
    if len(inside) != 24:
        raise RuntimeError(("parent block size", len(inside)))

    edge = EDGES[edge_index]
    local_indices = [i for i, p in enumerate(PERMS) if tuple(sorted(p[:2])) == edge]
    if len(local_indices) != 4:
        raise RuntimeError(("chambers per coarse edge", edge, local_indices))

    seed = ((1,) * len(G.EDGES), (0,) * D.n_tets)

    t0 = time.time()
    u = {}
    first_columns = []
    for li in local_indices:
        node = inside[li]
        col = G.H_sine_basis(seed, node, JMAX2, TOL)
        first_columns.append({"local_index": li, "global_node": node, "support": len(col), "norm": norm(col)})
        add(u, col, 0.5)
    first_seconds = time.time() - t0

    t1 = time.time()
    v = {}
    per_node_second_support = []
    for node in inside:
        col = G.H_sine_state(u, node, JMAX2, TOL)
        per_node_second_support.append(len(col))
        add(v, col, 1.0)
    second_seconds = time.time() - t1

    finite = all(
        np.isfinite([z.real, z.imag]).all()
        for state in (u, v)
        for z in state.values()
    )
    seed_parity = sum(seed[0]) % 2
    second_wrong_parity = sum(1 for key in v if sum(key[0]) % 2 != seed_parity)

    checks = {
        "L1_nodes_384": D.n_tets == 384,
        "L1_dual_links_768": len(G.EDGES) == 768,
        "parent_has_24_fine_nodes": len(inside) == 24,
        "edge_has_four_barycentric_chambers": len(local_indices) == 4,
        "first_edge_state_nonzero": len(u) > 0 and norm(u) > TOL,
        "depth2_block_state_nonzero": len(v) > 0 and norm(v) > TOL,
        "finite_amplitudes": finite,
        "depth2_spin_wall_j_le_5_over_2": max_spin(v) <= 2.5 + 1e-12,
        "depth2_seed_parity_restored": second_wrong_parity == 0,
    }

    meta = {
        "status": "exact L1 full-E coarse-edge depth-two block column",
        "passed": bool(all(checks.values())),
        "science_status": "L1_METRIC_EDGE_DEPTH2_PILOT",
        "parent_coarse_tetra": parent_id,
        "edge_index": edge_index,
        "edge": list(edge),
        "representative_role": "same-anchor" if edge_index == 0 else ("adjacent" if edge_index == 1 else "opposite"),
        "local_chamber_indices": local_indices,
        "global_chamber_nodes": [inside[i] for i in local_indices],
        "Jmax": JMAX2 / 2.0,
        "first_columns": first_columns,
        "first_edge_state": diagnostics(u, seed),
        "depth2_block_state": diagnostics(v, seed),
        "second_action_support_by_block_node": per_node_second_support,
        "first_seconds": first_seconds,
        "second_seconds": second_seconds,
        "second_wrong_seed_parity_outputs": second_wrong_parity,
        "checks": checks,
        "definition": "u_e=(1/2) sum_{4 chambers->e} H_c|Omega>; v_e=(sum_{w in parent block} H_w)u_e",
        "scope_note": "Full Euclidean E on the closed L1 habitat. No Lorentzian term, energy denominator, TT projector or external datum is used.",
    }
    return u, v, meta


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--edge-index", type=int, choices=REPRESENTATIVES, required=True)
    p.add_argument("--out-dir", type=Path, required=True)
    a = p.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    try:
        u, v, meta = run(a.edge_index)
        code = 0 if meta["passed"] else 1
    except Exception as exc:
        u = v = {}
        meta = {
            "status": "worker exception",
            "passed": False,
            "science_status": "INFRASTRUCTURE_DIAGNOSTIC",
            "edge_index": a.edge_index,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "traceback": traceback.format_exc(),
        }
        code = 1

    D = DualComplex(barycentric_with_parent(seed_16cell_boundary())[0])
    save_state(a.out_dir / f"u_{a.edge_index}.npz", u, len(D.dual_edges()), D.n_tets)
    save_state(a.out_dir / f"v_{a.edge_index}.npz", v, len(D.dual_edges()), D.n_tets)
    (a.out_dir / f"edge_{a.edge_index}.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
