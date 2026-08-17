#!/usr/bin/env python3
"""Exact one-node shard of the full-E L1 coarse-metric depth-two response.

For one coarse parent edge e construct the *same* normalized source used by the
unsharded production worker,

    u_e = (1/2) sum_{4 chambers c -> e} H_c |Omega>.

For one parent-block fine chamber w compute only

    v_{e,w} = H_w u_e.

The exact block result is reconstructed linearly by the collector,

    v_e = sum_{w=0}^{23} v_{e,w} = H_B u_e.

This is a computational factorization only: it changes neither the
physical-sine Euclidean operator, the closed 384-node/768-link L1 habitat nor
the exact second-hit wall Jmax=5/2.
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
REPRESENTATIVES = (0, 1, 5)


def add(dst, src, scale=1.0):
    for k, a in src.items():
        z = dst.get(k, 0j) + scale * a
        if abs(z) > TOL:
            dst[k] = z
        elif k in dst:
            del dst[k]


def norm(state):
    return math.sqrt(sum(abs(a) ** 2 for a in state.values()))


def maxspin(state):
    return max((max(k[0]) for k in state), default=0) / 2.0


def save(path, state, nedges, nverts):
    rows = sorted(state.items(), key=lambda kv: repr(kv[0]))
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        spins = np.asarray([k[0] for k, _ in rows], np.int16)
        Ks = np.asarray([k[1] for k, _ in rows], np.int16)
        amp = np.asarray([a for _, a in rows], np.complex128)
    else:
        spins = np.zeros((0, nedges), np.int16)
        Ks = np.zeros((0, nverts), np.int16)
        amp = np.zeros((0,), np.complex128)
    np.savez_compressed(path, spins=spins, Ks=Ks, amp=amp)


def diag(state, seed):
    changed = Counter(sum(a != b for a, b in zip(key[0], seed[0])) for key in state)
    parity = Counter(sum(key[0]) % 2 for key in state)
    return {
        'support': len(state),
        'norm': norm(state),
        'max_spin': maxspin(state),
        'changed_edge_count_distribution': {str(k): v for k, v in sorted(changed.items())},
        'sum_doubled_spin_parity_distribution': {str(k): v for k, v in sorted(parity.items())},
    }


def run(edge_index, node_index, parent_id=0):
    if edge_index not in REPRESENTATIVES:
        raise ValueError(edge_index)
    if not 0 <= node_index < 24:
        raise ValueError(node_index)

    ZVM.patch_and_clear()
    coarse = seed_16cell_boundary()
    fine, parent = barycentric_with_parent(coarse)
    D = DualComplex(fine)
    G = PLPeterWeylEuclidean(D)

    inside = sorted(v for v, p in enumerate(parent) if p == parent_id)
    if len(inside) != 24:
        raise RuntimeError(('parent block size', len(inside)))

    edge = EDGES[edge_index]
    local = [i for i, p in enumerate(PERMS) if tuple(sorted(p[:2])) == edge]
    if len(local) != 4:
        raise RuntimeError(('chambers per edge', edge, local))

    seed = ((1,) * len(G.EDGES), (0,) * D.n_tets)

    t0 = time.time()
    u = {}
    first = []
    for li in local:
        node = inside[li]
        col = G.H_sine_basis(seed, node, JMAX2, TOL)
        first.append({'local_index': li, 'global_node': node, 'support': len(col), 'norm': norm(col)})
        add(u, col, 0.5)
    t_first = time.time() - t0

    global_node = inside[node_index]
    t1 = time.time()
    v = G.H_sine_state(u, global_node, JMAX2, TOL)
    t_second = time.time() - t1

    finite = all(np.isfinite([z.real, z.imag]).all() for st in (u, v) for z in st.values())
    seedpar = sum(seed[0]) % 2
    wrong = sum(1 for key in v if sum(key[0]) % 2 != seedpar)

    checks = {
        'L1_nodes_384': D.n_tets == 384,
        'L1_dual_links_768': len(G.EDGES) == 768,
        'parent_has_24_fine_nodes': len(inside) == 24,
        'edge_has_four_barycentric_chambers': len(local) == 4,
        'first_edge_state_nonzero': len(u) > 0 and norm(u) > TOL,
        'one_node_depth2_state_nonzero': len(v) > 0 and norm(v) > TOL,
        'finite_amplitudes': finite,
        'depth2_spin_wall_j_le_5_over_2': maxspin(v) <= 2.5 + 1e-12,
        'depth2_seed_parity_restored': wrong == 0,
        'node_index_valid': 0 <= node_index < 24,
    }

    meta = {
        'status': 'exact one-node shard of L1 full-E coarse-edge depth-two response',
        'passed': bool(all(checks.values())),
        'science_status': 'L1_METRIC_EDGE_DEPTH2_FULL_E_SHARD',
        'parent_coarse_tetra': parent_id,
        'edge_index': edge_index,
        'edge': list(edge),
        'node_index': node_index,
        'global_second_action_node': global_node,
        'local_chamber_indices': local,
        'global_chamber_nodes': [inside[i] for i in local],
        'Jmax': JMAX2 / 2,
        'first_columns': first,
        'first_edge_state': diag(u, seed),
        'depth2_shard_state': diag(v, seed),
        'first_seconds': t_first,
        'second_seconds': t_second,
        'second_wrong_seed_parity_outputs': wrong,
        'checks': checks,
        'definition': 'u_e=(1/2) sum_{4 chambers->e} H_c|Omega>; v_e,w=H_w u_e; collector sums w=0..23',
        'scope_note': 'Exact computational sharding of full physical-sine Euclidean E. No q4/strict projection, Lorentzian term, energy denominator, TT projection or external datum.',
    }
    return D, u, v, meta


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--edge-index', type=int, choices=REPRESENTATIVES, required=True)
    p.add_argument('--node-index', type=int, choices=range(24), required=True)
    p.add_argument('--out-dir', type=Path, required=True)
    a = p.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)

    try:
        D, u, v, out = run(a.edge_index, a.node_index)
        code = 0 if out['passed'] else 1
        save(a.out_dir / f'u_{a.edge_index}_node_{a.node_index}.npz', u, len(D.dual_edges()), D.n_tets)
        save(a.out_dir / f'v_{a.edge_index}_node_{a.node_index}.npz', v, len(D.dual_edges()), D.n_tets)
    except Exception as exc:
        out = {
            'status': 'full-E depth-two shard worker exception',
            'passed': False,
            'science_status': 'INFRASTRUCTURE_DIAGNOSTIC',
            'edge_index': a.edge_index,
            'node_index': a.node_index,
            'error_type': type(exc).__name__,
            'error': str(exc),
            'traceback': traceback.format_exc(),
        }
        code = 1

    (a.out_dir / f'edge_{a.edge_index}_node_{a.node_index}.json').write_text(
        json.dumps(out, indent=2) + '\n', encoding='utf-8'
    )
    print(json.dumps(out, indent=2))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
