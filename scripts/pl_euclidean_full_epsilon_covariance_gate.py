#!/usr/bin/env python3
"""Experimental full-epsilon Euclidean regulator covariance gate.

The production PL Euclidean engine currently uses 12 cyclic representatives of
the local four-slot epsilon contraction.  That is equivalent to the full 24
ordered permutations only when reversing the ordered curvature pair is already
an exact minus operation at finite regulator.

This target-independent experiment constructs instead

  E_full24 = (1/2) * sum_{p=(d,a,b,c) in S4} sgn(p) E_term(a,b,c)

with the same tetrahedral charged-volume backend and physical-sine ordering.
The factor 1/2 preserves the historical normalization when the missing 12 odd
triple permutations are exactly redundant.

The gate asks only:
  * does the 24-term antisymmetrization restore exact pairing-stabilizer
    pseudoscalar covariance on the 16-cell seed?
  * how far is it from the currently frozen 12-term E column?

No GR/HDA target or fitted coefficient enters this experiment.  A PASS here is
not permission to replace production E; all normalization/HDA regressions must
be rerun before promotion.
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

import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from tetrahedral_volume_backend import install_tetrahedral_volume_backend
from pl_dual_complex import DualComplex, seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

TOL = 1e-9


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 else 1


def pairing_stabilizer():
    pairs = {frozenset((0, 1)), frozenset((2, 3))}
    return tuple(
        p
        for p in itertools.permutations(range(4))
        if {frozenset((p[0], p[1])), frozenset((p[2], p[3]))} == pairs
    )


def map_node(v, h):
    bits = [(v >> (3 - i)) & 1 for i in range(4)]
    nb = [0] * 4
    for i in range(4):
        nb[h[i]] = bits[i]
    out = 0
    for i, b in enumerate(nb):
        out |= b << (3 - i)
    return out


def inverse_perm(h):
    q = [0] * 4
    for i, x in enumerate(h):
        q[x] = i
    return tuple(q)


def mapped_spins(spins, edges, ei, h):
    ns = [0] * len(edges)
    for old, (a, b) in enumerate(edges):
        e = tuple(sorted((map_node(a, h), map_node(b, h))))
        ns[ei[e]] = spins[old]
    return tuple(ns)


def state_rel(a, b):
    keys = set(a) | set(b)
    num = math.sqrt(sum(abs(a.get(k, 0j) - b.get(k, 0j)) ** 2 for k in keys))
    den = math.sqrt(sum(abs(z) ** 2 for z in b.values()))
    return num / max(den, 1e-300)


def inner(a, b):
    return sum(np.conjugate(a.get(k, 0j)) * b.get(k, 0j) for k in set(a) | set(b))


class HTransport:
    def __init__(self, D, G):
        self.D = D
        self.G = G
        self.edges = list(G.EDGES)
        self.ei = {e: i for i, e in enumerate(self.edges)}
        self.local_cache = {}
        self.max_local_leak = 0.0
        self.max_phase_mod = 0.0

    def local_phase(self, v, spins, K, h, newspins):
        key = (v, spins, K, h, newspins)
        if key in self.local_cache:
            return self.local_cache[key]
        t = map_node(v, h)
        oldls = self.G.local_spins(spins, v)
        newls = self.G.local_spins(newspins, t)
        expected = [None] * 4
        for r in range(4):
            expected[h[r]] = oldls[r]
        if tuple(expected) != tuple(newls):
            raise RuntimeError(("local spin permutation mismatch", v, h, oldls, newls, expected))
        T = self.G.oriented_intertwiner(v, oldls, K)
        Tp = np.transpose(T, axes=inverse_perm(h))
        U = self.G.oriented_intertwiner(t, newls, K)
        z = np.vdot(U, Tp)
        leak = float(np.linalg.norm(Tp - z * U))
        mod = float(abs(abs(z) - 1.0))
        self.max_local_leak = max(self.max_local_leak, leak)
        self.max_phase_mod = max(self.max_phase_mod, mod)
        if leak > TOL or mod > TOL:
            raise RuntimeError(("H failed to preserve K line", v, h, oldls, K, complex(z), leak, mod))
        self.local_cache[key] = z
        return z

    def map_state(self, state, h):
        out = {}
        for (spins, Ks), amp in state.items():
            ns = mapped_spins(spins, self.edges, self.ei, h)
            nk = [None] * 16
            phase = 1 + 0j
            for v, K in enumerate(Ks):
                t = map_node(v, h)
                nk[t] = K
                phase *= self.local_phase(v, spins, K, h, ns)
            key = (ns, tuple(nk))
            out[key] = out.get(key, 0j) + amp * phase
        return {k: a for k, a in out.items() if abs(a) > 1e-11}


def full24_E(G, D, key, v, Jmax2, tol=1e-10):
    out = {}
    # p=(d,a,b,c): d is the omitted slot.  parity(p) is exactly (-1)^d
    # on the three cyclic representatives already used by oriented_specs().
    # We include all 24 p and multiply the old per-term sine coefficient by 1/2.
    for p in itertools.permutations(range(4)):
        d, a, b, c = p
        sign = D.orientation[v] * parity(p)
        rr = dict(G.T_items(key, v, a, b, c, Jmax2, False))
        aa = dict(G.T_items(key, v, a, b, c, Jmax2, True))
        G.add(out, rr, -0.25j * sign)
        G.add(out, aa, +0.25j * sign)
    return {k: a for k, a in out.items() if abs(a) > tol}


def run():
    ZVM.patch_and_clear()
    D = DualComplex(seed_16cell_boundary())
    G = PLPeterWeylEuclidean(D)
    seed = ((1,) * len(G.EDGES), (0,) * D.n_tets)

    with install_tetrahedral_volume_backend():
        G.primitive_items.cache_clear()
        old12 = G.H_sine_basis(seed, 0, 5, 1e-10)
        full24 = full24_E(G, D, seed, 0, 5, 1e-10)
    G.primitive_items.cache_clear()

    transport = HTransport(D, G)
    H = pairing_stabilizer()
    rows = []
    maxerr = 0.0
    support = True
    normdef = 0.0
    n24 = G.norm(full24)
    for h in H:
        mapped = transport.map_state(full24, h)
        target = {k: parity(h) * a for k, a in full24.items()}
        err = float(state_rel(mapped, target))
        support_equal = set(mapped) == set(target)
        maxerr = max(maxerr, err)
        support = bool(support and support_equal)
        normdef = max(normdef, float(abs(G.norm(mapped) - n24)))
        rows.append(
            {
                "permutation": list(h),
                "parity": parity(h),
                "support_identical": support_equal,
                "relative_full24_covariance_error": err,
                "mapped_norm": float(G.norm(mapped)),
            }
        )

    overlap = inner(old12, full24)
    n12 = G.norm(old12)
    rel = float(state_rel(full24, old12))
    cos = float((overlap.real) / max(n12 * n24, 1e-300))

    checks = {
        "full24_nonzero": bool(n24 > 1e-10),
        "full24_sparse_support_H_covariant": bool(support),
        "full24_pseudoscalar_H_covariance": bool(maxerr < TOL),
        "full24_norm_H_invariant": bool(normdef < TOL),
        "local_K_line_transport_exact": bool(
            transport.max_local_leak < TOL and transport.max_phase_mod < TOL
        ),
    }

    return {
        "status": "experimental fully antisymmetrized 24-term PL Euclidean regulator covariance",
        "passed": bool(all(checks.values())),
        "science_status": "TARGET_INDEPENDENT_REGULATOR_COVARIANCE_EXPERIMENT",
        "checks": checks,
        "definition": "E_full24=(1/2) sum_{(d,a,b,c) in S4} sgn(d,a,b,c) E_sine_term(a,b,c), with the tetrahedral charged-volume backend",
        "old12_support": len(old12),
        "old12_norm": float(n12),
        "full24_support": len(full24),
        "full24_norm": float(n24),
        "full24_vs_old12_relative_state_error": rel,
        "normalized_real_overlap_full24_old12": cos,
        "full24_vs_old12_support_identical": bool(set(full24) == set(old12)),
        "H_covariance_rows": rows,
        "max_full24_H_relative_covariance_error": float(maxerr),
        "max_full24_H_norm_defect": float(normdef),
        "max_local_intertwiner_line_leakage": float(transport.max_local_leak),
        "max_local_phase_modulus_defect": float(transport.max_phase_mod),
        "promotion_guard": "Even if this gate passes, E_full24 is not production until Euclidean normalization, two-node HDA, route, Lorentzian and collective regressions are rerun under a separately frozen operator-correction addendum.",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    out = run()
    text = json.dumps(out, indent=2, sort_keys=True)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
