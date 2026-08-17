#!/usr/bin/env python3
"""Reference-vs-local exact equivalence gate for the PL Peter-Weyl E backend.

The optimized ``LocalPLPeterWeylEuclidean`` changes only how untouched Gauss
intertwiners are represented/projected.  Before production uses it, compare its
actual sparse amplitudes with the reference global-projection engine at two
levels:

1. complete first- and second-hit full-sine action on the unrefined 16-cell;
2. representative first-hit full-sine columns on the real L1 384-node habitat.

The gate compares exact global spin-network keys, support, and complex
amplitudes.  It is an implementation-equivalence certificate, not a physics
approximation.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np

import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from pl_dual_complex import DualComplex, seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean
from pl_peter_weyl_euclidean_local import LocalPLPeterWeylEuclidean
from collective_barycentric_E_boundary_support_gate import barycentric_with_parent

JMAX2 = 5
TOL = 1e-10
PASS_REL = 3e-10
PASS_ABS = 3e-10


def state_norm(a):
    return math.sqrt(sum(abs(z) ** 2 for z in a.values()))


def compare(a, b):
    ka = set(a)
    kb = set(b)
    keys = ka | kb
    diffs = {k: a.get(k, 0j) - b.get(k, 0j) for k in keys}
    num = math.sqrt(sum(abs(z) ** 2 for z in diffs.values()))
    den = max(state_norm(a), state_norm(b), 1e-300)
    max_abs = max((abs(z) for z in diffs.values()), default=0.0)
    return {
        'support_reference': len(a),
        'support_local': len(b),
        'support_exact_match': ka == kb,
        'only_reference': len(ka-kb),
        'only_local': len(kb-ka),
        'relative_l2_error': num / den,
        'max_abs_amplitude_error': max_abs,
        'norm_reference': state_norm(a),
        'norm_local': state_norm(b),
    }


def ok(c):
    return (
        c['support_exact_match']
        and c['relative_l2_error'] < PASS_REL
        and c['max_abs_amplitude_error'] < PASS_ABS
    )


def seed_key(G):
    return ((1,) * len(G.EDGES), (0,) * G.dual.n_tets)


def run():
    ZVM.patch_and_clear()
    out = {
        'status': 'reference-vs-active-cone PL Peter-Weyl full-E equivalence',
        'science_status': 'IMPLEMENTATION_EQUIVALENCE',
        'Jmax': JMAX2 / 2,
        'comparisons': {},
    }

    # A. Unrefined 16-cell: compare a complete first and second full-sine hit.
    D0 = DualComplex(seed_16cell_boundary())
    R0 = PLPeterWeylEuclidean(D0)
    L0 = LocalPLPeterWeylEuclidean(D0)
    s0 = seed_key(R0)

    t = time.time()
    r1 = R0.H_sine_basis(s0, 0, JMAX2, TOL)
    tr1 = time.time() - t
    t = time.time()
    l1 = L0.H_sine_basis(s0, 0, JMAX2, TOL)
    tl1 = time.time() - t
    c1 = compare(r1, l1)
    c1.update({'reference_seconds': tr1, 'local_seconds': tl1})
    out['comparisons']['seed16_first_hit_node0'] = c1

    # Use the same reference first-hit state as input to both engines.  This
    # isolates equivalence of the second action rather than compounding errors.
    t = time.time()
    r2 = R0.H_sine_state(r1, 0, JMAX2, TOL)
    tr2 = time.time() - t
    t = time.time()
    l2 = L0.H_sine_state(r1, 0, JMAX2, TOL)
    tl2 = time.time() - t
    c2 = compare(r2, l2)
    c2.update({'reference_seconds': tr2, 'local_seconds': tl2})
    out['comparisons']['seed16_second_hit_node0'] = c2

    # B. Real L1 habitat: compare representative full-sine first-hit columns.
    coarse = seed_16cell_boundary()
    fine, parent = barycentric_with_parent(coarse)
    D1 = DualComplex(fine)
    R1 = PLPeterWeylEuclidean(D1)
    L1 = LocalPLPeterWeylEuclidean(D1)
    s1 = seed_key(R1)
    inside = sorted(v for v, p in enumerate(parent) if p == 0)
    if len(inside) != 24:
        raise RuntimeError(('expected 24 L1 chambers in parent 0', len(inside)))

    # Two inequivalent-looking local positions are enough as a production
    # regression because both backends use the same generic operator code and
    # the seed branch is S4-related.  The small-complex second-hit check above
    # exercises the nontrivial state action explicitly.
    for li in (0, 7):
        node = inside[li]
        t = time.time()
        rr = R1.H_sine_basis(s1, node, JMAX2, TOL)
        tr = time.time() - t
        t = time.time()
        ll = L1.H_sine_basis(s1, node, JMAX2, TOL)
        tl = time.time() - t
        cc = compare(rr, ll)
        cc.update({'local_chamber_index': li, 'global_node': node,
                   'reference_seconds': tr, 'local_seconds': tl})
        out['comparisons'][f'L1_first_hit_local_{li}'] = cc

    checks = {name: ok(c) for name, c in out['comparisons'].items()}
    speedups = {
        name: (c['reference_seconds'] / c['local_seconds'] if c['local_seconds'] > 0 else None)
        for name, c in out['comparisons'].items()
    }
    out['checks'] = checks
    out['speedup_reference_over_local'] = speedups
    out['max_relative_l2_error'] = max(c['relative_l2_error'] for c in out['comparisons'].values())
    out['max_abs_amplitude_error'] = max(c['max_abs_amplitude_error'] for c in out['comparisons'].values())
    out['passed'] = bool(all(checks.values()))
    out['scope_note'] = (
        'Certifies implementation equivalence on a complete two-hit seed-16-cell '
        'test and representative real-L1 first-hit columns. The local backend '
        'does not alter cutoff, support, sign, ordering, or physical operator.'
    )
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path)
    a = p.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + '\n', encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
