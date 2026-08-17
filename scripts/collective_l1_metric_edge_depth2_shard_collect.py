#!/usr/bin/env python3
"""Reconstruct the exact full-E L1 metric depth-two kernel from 72 node shards.

For each S4 representative e in {01,02,23}, load the 24 independently computed
states v_{e,w}=H_w u_e and form the exact linear block sum

    v_e = sum_w v_{e,w} = H_B u_e.

Then construct the three small Gram matrices

    K_ef = <u_e|u_f>,
    A_ef = <u_e|v_f>,
    B_ef = <v_e|v_f>,

reduce each by the S4 same/adjacent/opposite orbit, and report the A1/E/T2
Krylov moments.  The calculation is target-independent: no GR value, TT
coefficient, experimental datum or fitted anisotropy enters the assembly.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

REPS = (0, 1, 5)
NODES = tuple(range(24))
TOL = 3e-7
SUM_TOL = 1e-10


def load_state(path):
    z = np.load(path)
    out = {}
    for i, a in enumerate(z['amp']):
        key = z['spins'][i].tobytes() + z['Ks'][i].tobytes()
        out[key] = complex(a)
    return out


def inner(a, b):
    if len(a) <= len(b):
        return sum(np.conj(v) * b.get(k, 0j) for k, v in a.items())
    return sum(np.conj(a.get(k, 0j)) * v for k, v in b.items())


def norm(a):
    return math.sqrt(max(float(inner(a, a).real), 0.0))


def relerr(a, b):
    keys = set(a) | set(b)
    num = math.sqrt(sum(abs(a.get(k, 0j) - b.get(k, 0j)) ** 2 for k in keys))
    return num / max(norm(b), 1e-300)


def add(dst, src):
    for k, a in src.items():
        z = dst.get(k, 0j) + a
        if abs(z) > SUM_TOL:
            dst[k] = z
        elif k in dst:
            del dst[k]


def mat(left, right):
    return np.asarray([[inner(left[i], right[j]) for j in range(3)] for i in range(3)], complex)


def orbit(M):
    n = max(float(np.linalg.norm(M)), 1e-30)
    diag = [M[i, i].real for i in range(3)]
    adj = [M[0, 1].real, M[1, 0].real, M[1, 2].real, M[2, 1].real]
    opp = [M[0, 2].real, M[2, 0].real]
    a = float(np.mean(diag))
    b = float(np.mean(adj))
    c = float(np.mean(opp))
    fit = np.array([[a, b, c], [b, a, b], [c, b, a]])
    return {
        'a_same': a,
        'b_adjacent': b,
        'c_opposite': c,
        'hermiticity_relative_defect': float(np.linalg.norm(M - M.conj().T) / n),
        'max_imaginary_entry': float(np.max(np.abs(M.imag))),
        'diagonal_spread': float(max(diag) - min(diag)),
        'adjacent_spread': float(max(adj) - min(adj)),
        'opposite_spread': float(max(opp) - min(opp)),
        'three_representative_orbit_residual': float(np.linalg.norm(M.real - fit) / max(np.linalg.norm(M.real), 1e-30)),
        'lambda_A1': a + 4 * b + c,
        'lambda_E': a - 2 * b + c,
        'lambda_T2': a - c,
        'Delta_ET': 2 * (c - b),
    }


def run(root):
    root = Path(root)
    metas = {}
    U = []
    V = []
    source_consistency = {}
    shard_diagnostics = {}

    for e in REPS:
        rows = []
        for w in NODES:
            mp = root / f'edge_{e}_node_{w}.json'
            if not mp.exists():
                raise RuntimeError(f'missing shard metadata {mp}')
            m = json.loads(mp.read_text(encoding='utf-8'))
            if not m.get('passed'):
                raise RuntimeError(f'edge {e} node {w} failed: {m.get("error", "") or m.get("checks", {})}')
            if m.get('science_status') != 'L1_METRIC_EDGE_DEPTH2_FULL_E_SHARD':
                raise RuntimeError(f'wrong shard science status edge={e} node={w}: {m.get("science_status")}')
            rows.append(m)
        metas[e] = rows

        u0 = load_state(root / f'u_{e}_node_0.npz')
        max_u_rel = 0.0
        # The source is recomputed independently in every shard.  Compare it
        # explicitly so sharding cannot silently alter the first-hit carrier.
        for w in NODES[1:]:
            uw = load_state(root / f'u_{e}_node_{w}.npz')
            max_u_rel = max(max_u_rel, relerr(uw, u0))
        source_consistency[str(e)] = {
            'support': len(u0),
            'norm': norm(u0),
            'max_relative_source_mismatch_across_24_shards': max_u_rel,
        }
        U.append(u0)

        ve = {}
        supports = []
        norms = []
        for w in NODES:
            vw = load_state(root / f'v_{e}_node_{w}.npz')
            supports.append(len(vw))
            norms.append(norm(vw))
            add(ve, vw)
        V.append(ve)
        shard_diagnostics[str(e)] = {
            'shard_support_min': int(min(supports)),
            'shard_support_max': int(max(supports)),
            'shard_norm_min': float(min(norms)),
            'shard_norm_max': float(max(norms)),
            'reconstructed_block_support': len(ve),
            'reconstructed_block_norm': norm(ve),
            'sum_of_shard_runtimes_seconds': float(sum(float(m['second_seconds']) for m in rows)),
            'max_single_shard_runtime_seconds': float(max(float(m['second_seconds']) for m in rows)),
        }

    K = mat(U, U)
    A = mat(U, V)
    B = mat(V, V)
    ko = orbit(K)
    ao = orbit(A)
    bo = orbit(B)

    dyn = {}
    for ir in ('A1', 'E', 'T2'):
        k = ko[f'lambda_{ir}']
        aa = ao[f'lambda_{ir}']
        bb = bo[f'lambda_{ir}']
        if k <= 1e-12:
            raise RuntimeError(f'nonpositive K_{ir}={k}')
        h1 = aa / k
        h2 = bb / k
        dyn[ir] = {
            'K': k,
            'A': aa,
            'B': bb,
            'h1_normalized': h1,
            'h2_normalized': h2,
            'Sigma2_depth2': h2 - h1 * h1,
        }

    dh2 = dyn['E']['h2_normalized'] - dyn['T2']['h2_normalized']
    dvar = dyn['E']['Sigma2_depth2'] - dyn['T2']['Sigma2_depth2']
    mh2 = (2 * dyn['E']['h2_normalized'] + 3 * dyn['T2']['h2_normalized']) / 5
    mvar = (2 * dyn['E']['Sigma2_depth2'] + 3 * dyn['T2']['Sigma2_depth2']) / 5

    symmetry = all(
        x['hermiticity_relative_defect'] < TOL and x['three_representative_orbit_residual'] < TOL
        for x in (ko, ao, bo)
    )
    variance = min(x['Sigma2_depth2'] for x in dyn.values()) > -3e-6
    finite = all(np.isfinite(M.real).all() and np.isfinite(M.imag).all() for M in (K, A, B))
    sources_equal = all(v['max_relative_source_mismatch_across_24_shards'] < 1e-12 for v in source_consistency.values())

    checks = {
        'all_72_full_E_shards_present_and_passed': True,
        'independently_recomputed_sources_identical': sources_equal,
        'finite': finite,
        'S4_three_orbit_consistency': symmetry,
        'nonnegative_depth2_variance_with_tolerance': variance,
    }

    return {
        'status': 'exact sharded full-E L1 metric-edge depth-two Euclidean Krylov response',
        'passed': bool(all(checks.values())),
        'science_status': 'L1_METRIC_EDGE_DEPTH2_KRYLOV',
        'computational_factorization': 'H_B u_e = sum_{w=0}^{23} H_w u_e, with each term computed independently',
        'edge_representatives': [list(metas[e][0]['edge']) for e in REPS],
        'definition': {
            'u_e': '(1/2) sum_{4 chambers->e} H_c|Omega>',
            'H_B': 'sum H_w over 24 parent-block chambers',
            'v_e': 'sum_w v_e,w = H_B u_e',
            'K': '<u_e|u_f>',
            'A': '<u_e|H_B u_f>',
            'B': '<H_Bu_e|H_Bu_f>',
        },
        'K_matrix': [[[float(z.real), float(z.imag)] for z in row] for row in K],
        'A_matrix': [[[float(z.real), float(z.imag)] for z in row] for row in A],
        'B_matrix': [[[float(z.real), float(z.imag)] for z in row] for row in B],
        'K_orbit': ko,
        'A_orbit': ao,
        'B_orbit': bo,
        'dynamic_irreps': dyn,
        'Delta_ET_h2': dh2,
        'weighted_isotropic_h2': mh2,
        'relative_ET_h2_split': dh2 / mh2 if abs(mh2) > 1e-30 else None,
        'Delta_ET_Sigma2': dvar,
        'weighted_isotropic_Sigma2': mvar,
        'relative_ET_Sigma2_split': dvar / mvar if abs(mvar) > 1e-30 else None,
        'source_consistency': source_consistency,
        'shard_diagnostics': shard_diagnostics,
        'checks': checks,
        'interpretation': 'Genuine full physical-sine Euclidean depth-two dynamics on the first refined six-edge metric carrier. Its E-T2 split is a microscopic dynamical tetrahedral anisotropy diagnostic. It becomes a physical eta2/zeta4 only after the momentum-dependent effective kernel and TT pole bridge are applied.',
        'hard_scope_guard': 'Do not rename local h2 or Sigma2 E-T2 splitting as zeta4. Physical zeta4 is extracted only from the quartic directional TT pole coefficients of C6(omega,k).',
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    out = run(a.root)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    slim = {k: v for k, v in out.items() if k not in ('K_matrix', 'A_matrix', 'B_matrix', 'shard_diagnostics')}
    print(json.dumps(slim, indent=2))
    return 0 if out['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
