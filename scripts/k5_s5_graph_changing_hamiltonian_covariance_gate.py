#!/usr/bin/env python3
"""Safe-cutoff S5 covariance of the graph-changing K5 Peter-Weyl Hamiltonian.

Implements K5_S5_GRAPH_CHANGING_HAMILTONIAN_COVARIANCE_PREREGISTRATION.md.
All 160 H_v columns on the 32D all-j=1/2 input sector are computed at Jmax=5/2.
Full graph-changing outputs are transported by exact edge relabelling plus a
complete local recoupling-basis transformation; no projection back to 32D is
used in the covariance comparison.
"""
from __future__ import annotations

import argparse
import functools
import itertools
import json
import math
from pathlib import Path

import numpy as np

import k5_peter_weyl_safe_hda_column as PW

JMAX2 = 5
COV_TOL = 5e-9
TRANSPORT_TOL = 5e-9
LOCAL_BASIS_TOL = 5e-10
SPARSE_DROP = 1e-12
PERMS5 = tuple(itertools.permutations(range(5)))
GENERATORS = (
    (1, 0, 2, 3, 4),
    (0, 2, 1, 3, 4),
    (0, 1, 3, 2, 4),
    (0, 1, 2, 4, 3),
)

Sparse = dict[tuple, complex]


def compose(g: tuple[int, ...], h: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(g[h[v]] for v in range(5))


def inverse(g: tuple[int, ...]) -> tuple[int, ...]:
    q = [0] * 5
    for v, w in enumerate(g):
        q[w] = v
    return tuple(q)


def parity(p: tuple[int, ...]) -> int:
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 else 1


def induced_local_axis_perm(g: tuple[int, ...], v: int) -> tuple[int, ...]:
    old_neigh = list(PW.NEIG[v])
    nv = g[v]
    new_neigh = list(PW.NEIG[nv])
    inv = inverse(g)
    return tuple(old_neigh.index(inv[nnew]) for nnew in new_neigh)


def eta(g: tuple[int, ...], v: int) -> int:
    return parity(induced_local_axis_perm(g, v))


def eta_closed(g: tuple[int, ...], v: int) -> int:
    return parity(g) * ((-1) ** (v + g[v]))


def map_spins(spins: tuple[int, ...], g: tuple[int, ...]) -> tuple[int, ...]:
    out = [None] * len(PW.EDGES)
    for ei, (u, v) in enumerate(PW.EDGES):
        ne = tuple(sorted((g[u], g[v])))
        out[PW.EIDX[ne]] = int(spins[ei])
    if any(x is None for x in out):
        raise AssertionError("incomplete mapped edge-spin tuple")
    return tuple(int(x) for x in out)


def state_norm(st: Sparse) -> float:
    return math.sqrt(sum(abs(a) ** 2 for a in st.values()))


def inner(a: Sparse, b: Sparse) -> complex:
    if len(a) <= len(b):
        return sum(np.conj(x) * b.get(k, 0j) for k, x in a.items())
    return sum(np.conj(a.get(k, 0j)) * x for k, x in b.items())


def add_scaled(dst: Sparse, src: Sparse, scale: complex = 1.0) -> None:
    if abs(scale) == 0:
        return
    for k, a in src.items():
        z = dst.get(k, 0j) + scale * a
        if abs(z) > SPARSE_DROP:
            dst[k] = z
        elif k in dst:
            del dst[k]


def state_difference_norm(a: Sparse, b: Sparse) -> float:
    keys = set(a) | set(b)
    return math.sqrt(sum(abs(a.get(k, 0j) - b.get(k, 0j)) ** 2 for k in keys))


def relative_state_defect(a: Sparse, b: Sparse) -> float:
    return state_difference_norm(a, b) / max(state_norm(a), state_norm(b), 1e-30)


@functools.lru_cache(None)
def transport_key_cached(key: tuple, g: tuple[int, ...]):
    spins, Ks = key
    new_spins = map_spins(tuple(spins), g)
    local_opts: list[tuple[tuple[tuple[int, complex], ...], int, float]] = []
    max_local_leak = 0.0

    for v in PW.VERT:
        nv = g[v]
        old_ls = tuple(PW.local_spins(tuple(spins), v))
        new_ls = tuple(PW.local_spins(new_spins, nv))
        p = induced_local_axis_perm(g, v)
        old_tensor = PW.intertwiner_tensor_cached(old_ls, int(Ks[v]))
        permuted = np.transpose(old_tensor, axes=p)
        expected_shape = tuple(s + 1 for s in new_ls)
        if permuted.shape != expected_shape:
            raise AssertionError((v, nv, old_ls, new_ls, p, permuted.shape, expected_shape))

        opts = []
        recon = np.zeros_like(permuted)
        for Knew in PW.allowed_k2_t(*new_ls):
            B = PW.intertwiner_tensor_cached(new_ls, Knew)
            c = np.vdot(B, permuted)
            if abs(c) > 1e-14:
                opts.append((int(Knew), complex(c)))
                recon += c * B
        local_leak = float(np.linalg.norm(permuted - recon) / max(np.linalg.norm(permuted), 1e-30))
        max_local_leak = max(max_local_leak, local_leak)
        if not opts:
            raise AssertionError(f"empty transported recoupling basis at v={v}")
        local_opts.append((tuple(opts), nv, local_leak))

    out: Sparse = {}
    for choices in itertools.product(*[x[0] for x in local_opts]):
        new_K = [None] * 5
        amp = 1.0 + 0j
        for v, (Knew, c) in enumerate(choices):
            nv = local_opts[v][1]
            new_K[nv] = int(Knew)
            amp *= c
        ko = (new_spins, tuple(int(x) for x in new_K))
        out[ko] = out.get(ko, 0j) + amp

    out = {k: a for k, a in out.items() if abs(a) > SPARSE_DROP}
    return tuple(out.items()), float(max_local_leak)


def transport_key(key: tuple, g: tuple[int, ...]) -> tuple[Sparse, float]:
    items, leak = transport_key_cached(key, g)
    return dict(items), float(leak)


def transport_state(st: Sparse, g: tuple[int, ...]) -> Sparse:
    out: Sparse = {}
    for key, amp in st.items():
        mapped, _ = transport_key(key, g)
        add_scaled(out, mapped, amp)
    return out


def input_rep(g: tuple[int, ...], basis: list[tuple], index: dict[tuple, int]) -> np.ndarray:
    U = np.zeros((len(basis), len(basis)), complex)
    for j, key in enumerate(basis):
        mapped, leak = transport_key(key, g)
        if leak > LOCAL_BASIS_TOL:
            raise AssertionError(f"input local recoupling leak {leak}")
        for ko, a in mapped.items():
            if ko not in index:
                raise AssertionError("all-j=1/2 input transport left the frozen 32D sector")
            U[index[ko], j] += a
    return U


def build_master(columns: dict[tuple[int, int], Sparse], n: int) -> np.ndarray:
    M = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(i, n):
            z = sum(inner(columns[(v, i)], columns[(v, j)]) for v in PW.VERT)
            M[i, j] = z
            M[j, i] = np.conj(z)
    return 0.5 * (M + M.conj().T)


def run() -> dict[str, object]:
    basis = list(PW.basis_full_jhalf())
    index = {key: i for i, key in enumerate(basis)}
    if len(basis) != 32:
        raise AssertionError("expected 32 all-j=1/2 K5 inputs")

    # Exact combinatorial orientation identity and cocycle.
    orientation_mismatch = 0
    for g in PERMS5:
        for v in PW.VERT:
            if eta(g, v) != eta_closed(g, v):
                orientation_mismatch += 1
    eta_cocycle_mismatch = 0
    for g in PERMS5:
        for h in PERMS5:
            gh = compose(g, h)
            for v in PW.VERT:
                if eta(gh, v) != eta(g, h[v]) * eta(h, v):
                    eta_cocycle_mismatch += 1

    # Full input representation for the master-invariance cross-check.
    Uall = {g: input_rep(g, basis, index) for g in PERMS5}
    max_input_unitarity = max(float(np.linalg.norm(U.conj().T @ U - np.eye(32), 2)) for U in Uall.values())
    max_input_generator_group_error = 0.0
    for g in PERMS5:
        for s in GENERATORS:
            max_input_generator_group_error = max(
                max_input_generator_group_error,
                float(np.linalg.norm(Uall[s] @ Uall[g] - Uall[compose(s, g)], 2)),
            )

    # Precompute the complete 160 safe-cutoff graph-changing columns.
    columns: dict[tuple[int, int], Sparse] = {}
    unique_output_keys: set[tuple] = set()
    column_rows = []
    for v in PW.VERT:
        for j, key in enumerate(basis):
            out = PW.apply_H_cached_state({key: 1.0 + 0j}, v, JMAX2)
            columns[(v, j)] = out
            unique_output_keys.update(out)
            column_rows.append({
                "node": int(v),
                "input_index": int(j),
                "support": len(out),
                "norm": state_norm(out),
            })

    # Transport integrity on every state key actually reached by H.
    max_output_transport_norm_error = 0.0
    max_output_inverse_roundtrip = 0.0
    max_output_local_basis_leak = 0.0
    output_spin_mapping_failures = 0
    output_transport_checks = 0
    for key in sorted(unique_output_keys, key=repr):
        for g in GENERATORS:
            mapped, leak = transport_key(key, g)
            output_transport_checks += 1
            max_output_local_basis_leak = max(max_output_local_basis_leak, leak)
            max_output_transport_norm_error = max(max_output_transport_norm_error, abs(state_norm(mapped) - 1.0))
            expected_spins = map_spins(tuple(key[0]), g)
            if any(tuple(ko[0]) != expected_spins for ko in mapped):
                output_spin_mapping_failures += 1
            back = transport_state(mapped, inverse(g))
            target = {key: 1.0 + 0j}
            max_output_inverse_roundtrip = max(max_output_inverse_roundtrip, relative_state_defect(back, target))

    # Full state-level covariance on all 640 generator/node/input triples.
    covariance_rows = []
    max_raw_covariance_defect = 0.0
    max_boundary_covariance_defect = 0.0
    for g in GENERATORS:
        U = Uall[g]
        for v in PW.VERT:
            nv = g[v]
            sign_raw = eta(g, v)
            for j in range(32):
                lhs = transport_state(columns[(v, j)], g)
                rhs0: Sparse = {}
                for k in range(32):
                    c = U[k, j]
                    if abs(c) > 1e-14:
                        add_scaled(rhs0, columns[(nv, k)], c)
                rhs: Sparse = {}
                add_scaled(rhs, rhs0, sign_raw)
                raw_def = relative_state_defect(lhs, rhs)

                lhs_b: Sparse = {}
                add_scaled(lhs_b, lhs, (-1) ** v)
                rhs_b: Sparse = {}
                add_scaled(rhs_b, rhs0, parity(g) * ((-1) ** nv))
                boundary_def = relative_state_defect(lhs_b, rhs_b)

                max_raw_covariance_defect = max(max_raw_covariance_defect, raw_def)
                max_boundary_covariance_defect = max(max_boundary_covariance_defect, boundary_def)
                covariance_rows.append({
                    "generator": list(g),
                    "node": int(v),
                    "mapped_node": int(nv),
                    "input_index": int(j),
                    "eta": int(sign_raw),
                    "raw_relative_state_defect": float(raw_def),
                    "boundary_relative_state_defect": float(boundary_def),
                    "lhs_support": len(lhs),
                    "rhs_support": len(rhs),
                })

    # Independent full-image master-form symmetry check.
    M = build_master(columns, 32)
    scale = max(float(np.linalg.norm(M, 2)), 1e-30)
    hermitian_defect = float(np.linalg.norm(M - M.conj().T, 2) / scale)
    evals = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
    min_eval = float(evals[0])
    max_eval = float(evals[-1])
    psd_relative_floor = min_eval / max(abs(max_eval), 1e-30)
    max_master_S5_defect = max(
        float(np.linalg.norm(U.conj().T @ M @ U - M, 2) / scale)
        for U in Uall.values()
    )

    # Multiplying each node column by (-1)^v cannot change the Gram sum; build
    # it independently instead of assuming the algebraic identity.
    M_boundary = np.zeros_like(M)
    for i in range(32):
        for j in range(i, 32):
            z = sum(
                inner(
                    {k: ((-1) ** v) * a for k, a in columns[(v, i)].items()},
                    {k: ((-1) ** v) * a for k, a in columns[(v, j)].items()},
                )
                for v in PW.VERT
            )
            M_boundary[i, j] = z
            M_boundary[j, i] = np.conj(z)
    master_boundary_identity_error = float(np.linalg.norm(M_boundary - M, 2) / scale)

    checks = {
        "orientation_cofactor_identity_all_600_pairs": orientation_mismatch == 0,
        "orientation_eta_is_group_cocycle": eta_cocycle_mismatch == 0,
        "input_S5_transport_unitary": bool(max_input_unitarity < TRANSPORT_TOL),
        "input_transport_generator_group_law": bool(max_input_generator_group_error < TRANSPORT_TOL),
        "all_reached_output_keys_transport_norm_preserved": bool(max_output_transport_norm_error < TRANSPORT_TOL),
        "all_reached_output_keys_inverse_roundtrip": bool(max_output_inverse_roundtrip < TRANSPORT_TOL),
        "all_reached_output_local_recoupling_decompositions_complete": bool(max_output_local_basis_leak < LOCAL_BASIS_TOL),
        "all_reached_output_spins_map_exactly": output_spin_mapping_failures == 0,
        "raw_graph_changing_H_covariant_on_all_640_tests": bool(max_raw_covariance_defect < COV_TOL),
        "boundary_oriented_H_is_S5_pseudoscalar_vector_on_all_640_tests": bool(max_boundary_covariance_defect < COV_TOL),
        "full_image_master_Hermitian": bool(hermitian_defect < COV_TOL),
        "full_image_master_positive_semidefinite": bool(psd_relative_floor > -COV_TOL),
        "full_image_master_invariant_under_all_120_S5_elements": bool(max_master_S5_defect < COV_TOL),
        "boundary_orientation_leaves_master_exactly_unchanged": bool(master_boundary_identity_error < COV_TOL),
    }
    passed = bool(all(checks.values()))

    return {
        "status": "safe Jmax=5/2 S5 covariance diagnostic for the full graph-changing K5 H action on the complete 32D j=1/2 input sector",
        "science_status": "K5_SAFE_GRAPH_CHANGING_H_S5_COVARIANT" if passed else "K5_SAFE_GRAPH_CHANGING_H_S5_COVARIANCE_FAIL",
        "passed": passed,
        "Jmax": JMAX2 / 2,
        "input_dimension": 32,
        "number_H_columns": len(columns),
        "unique_graph_changing_output_keys": len(unique_output_keys),
        "number_output_transport_checks": output_transport_checks,
        "number_state_level_covariance_tests": len(covariance_rows),
        "orientation_cofactor_mismatches": orientation_mismatch,
        "orientation_cocycle_mismatches": eta_cocycle_mismatch,
        "max_input_unitarity_defect": max_input_unitarity,
        "max_input_generator_group_law_error": max_input_generator_group_error,
        "max_output_transport_norm_error": max_output_transport_norm_error,
        "max_output_inverse_roundtrip_relative_error": max_output_inverse_roundtrip,
        "max_output_local_basis_leakage": max_output_local_basis_leak,
        "output_spin_mapping_failures": output_spin_mapping_failures,
        "max_raw_H_covariance_relative_state_defect": max_raw_covariance_defect,
        "max_boundary_H_covariance_relative_state_defect": max_boundary_covariance_defect,
        "master_min_eigenvalue": min_eval,
        "master_max_eigenvalue": max_eval,
        "master_psd_relative_floor": psd_relative_floor,
        "master_Hermiticity_relative_defect": hermitian_defect,
        "max_master_S5_invariance_relative_defect": max_master_S5_defect,
        "boundary_vs_raw_master_relative_error": master_boundary_identity_error,
        "checks": checks,
        "column_rows": column_rows,
        "covariance_rows": covariance_rows,
        "orientation_theorem": (
            "The induced parity of the four legs at boundary tetrahedron v is eta(g,v)=sgn(g)(-1)^(v+g(v)). "
            "Therefore Hhat_v=(-1)^v H_v is the natural boundary-oriented convention and should transform as an S5 pseudoscalar node vector."
        ),
        "interpretation": (
            "A PASS establishes state-level automorphism covariance of the safe graph-changing Euclidean K5 Hamiltonian on the entire 32D all-j=1/2 input sector, without projecting its outputs back into that sector. "
            "The boundary sign convention changes neither individual constraint kernels nor the full-image master quadratic form."
        ),
        "claim_boundary": (
            "Finite safe-cutoff Euclidean operator-covariance theorem on one complete input shell only. It does not prove HDA closure, a nontrivial constraint kernel, Lorentzian covariance, covariance on every higher-spin input shell, Q4-K5 global equivalence, a rigging map or continuum diffeomorphism invariance."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
