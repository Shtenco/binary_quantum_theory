#!/usr/bin/env python3
"""Exact first Lorentzian covariant leg C_e(V)=h_e[h_e^-1,V_v].

This is the cheapest genuine factor appearing in Thiemann's Lorentzian kinetic
operator.  It uses the same Peter-Weyl holonomy hit matrices as the safe H_E
engine and the symmetry-adapted charged J=1/2 volume blocks from
charged_intertwiner_recoupling_gate.py.

For one oriented K5 radial edge e=(v,w), the matrix-valued operator is

    C_ij(V) = delta_ij V - sum_k h_ik V h^-1_kj.

Before evaluating C(V), the script checks the stronger two-hit identity

    sum_k h_ik h^-1_kj = delta_ij

on the same Gauss spin-network input, including all Peter-Weyl normalization,
endpoint orientation tensors and final Gauss projection.  Failure of that
identity is a hard implementation stop.

The intermediate state after h^-1 is charged.  Its endpoint tensor is projected
onto total J=1/2 recoupling blocks; V_J=sqrt(|Q_J|) acts there and the second
holonomy closes the state back to the Gauss sector.

This gate does not yet contain K=[V,H_E], the triple Lorentzian product or HDA.
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
import charged_intertwiner_recoupling_gate as CH


def project_factorized_branches(branches, tol=1e-11, return_leak=False):
    out = {}
    max_node_leak = 0.0
    for spins, tensors, amp in branches:
        local_opts = []
        ok = True
        for v in PW.VERT:
            ls = PW.local_spins(spins, v)
            opts = []
            recon = np.zeros_like(tensors[v])
            for K in PW.allowed_k2_t(*ls):
                B = PW.oriented_intertwiner(v, ls, K)
                c = np.vdot(B, tensors[v])
                if abs(c) > 1e-13:
                    opts.append((K, c))
                    recon += c * B
            nrm = float(np.linalg.norm(tensors[v]))
            leak = float(np.linalg.norm(tensors[v] - recon) / max(nrm, 1e-30))
            max_node_leak = max(max_node_leak, leak)
            if not opts:
                ok = False
                break
            local_opts.append(opts)
        if not ok:
            continue
        import itertools
        for ch in itertools.product(*local_opts):
            val = amp
            for _, c in ch:
                val *= c
            if abs(val) > tol:
                key = (spins, tuple(k for k, _ in ch))
                out[key] = out.get(key, 0j) + val
    out = PW.prune_state(out, tol)
    return (out, max_node_leak) if return_leak else out


def unorient_local(T, spins_local, v):
    X = T
    for leg, w in enumerate(PW.NEIG[v]):
        if w < v:
            X = PW.apply_axis_np(X, leg, PW.epsilon_j(spins_local[leg]).conj().T)
    return X


def orient_local(T, spins_local, v):
    X = T
    for leg, w in enumerate(PW.NEIG[v]):
        if w < v:
            X = PW.apply_axis_np(X, leg, PW.epsilon_j(spins_local[leg]))
    return X


def canonical_charged_volume(spins_local):
    Mp, Mm = PW.m2vals_t(1)
    bp, Qp, _, _ = CH.q_block(tuple(spins_local), 1, Mp)
    bm, Qm, _, _ = CH.q_block(tuple(spins_local), 1, Mm)
    Q = 0.5 * (Qp + Qm)
    Q = 0.5 * (Q + Q.conj().T)
    V = CH.canonical_volume_block(Q)
    return {Mp: bp, Mm: bm}, V


def apply_charged_volume_oriented(T, spins_local, v):
    X = unorient_local(T, spins_local, v)
    bases, V = canonical_charged_volume(tuple(spins_local))
    Y = np.zeros_like(X)
    recon = np.zeros_like(X)
    for M2, basis in bases.items():
        coeff = np.asarray([np.vdot(B, X) for B in basis], complex)
        for c, B in zip(coeff, basis):
            recon += c * B
        outc = V @ coeff
        for c, B in zip(outc, basis):
            Y += c * B
    leak = float(np.linalg.norm(X - recon) / max(np.linalg.norm(X), 1e-30))
    return orient_local(Y, spins_local, v), leak


def inverse_then_forward(initial, v, w, i, j, Jmax2, with_volume):
    total = {}
    max_charged_projection_leak = 0.0
    max_final_gauss_leak = 0.0
    for k in range(2):
        branches = [PW.initial_factorized_oriented(initial)]
        # h^{-1}_{k j}: reverse path w -> v.
        nb = []
        for br in branches:
            nb.extend(PW.apply_hit_branch(br, w, v, k, j, Jmax2))
        branches = nb
        if with_volume:
            vb = []
            for spins, tensors, amp in branches:
                t = list(tensors)
                ls = PW.local_spins(spins, v)
                t[v], leak = apply_charged_volume_oriented(t[v], ls, v)
                max_charged_projection_leak = max(max_charged_projection_leak, leak)
                vb.append((spins, tuple(t), amp))
            branches = vb
        # h_{i k}: forward path v -> w.
        nb = []
        for br in branches:
            nb.extend(PW.apply_hit_branch(br, v, w, i, k, Jmax2))
        branches = nb
        projected, gleak = project_factorized_branches(branches, return_leak=True)
        max_final_gauss_leak = max(max_final_gauss_leak, gleak)
        PW.add_dict(total, projected, +1)
    return PW.prune_state(total, 1e-10), max_charged_projection_leak, max_final_gauss_leak


def volume_on_gauss(initial, v):
    # Reuse exact local symmetry-preserving Gauss volume column from K gate.
    import peter_weyl_lorentzian_K_block_gate as KG
    return dict(KG.local_volume_column(initial, v))


def state_diff_norm(a, b):
    keys = set(a) | set(b)
    return math.sqrt(sum(abs(a.get(k, 0j) - b.get(k, 0j)) ** 2 for k in keys))


def matrix_state_norm(M):
    return math.sqrt(sum(PW.norm2_state(s) for row in M for s in row))


def run(v=0, w=1):
    # Two fundamental hits can reach j=3/2 from j=1/2.
    JMAX2 = 3
    initial = PW.basis_full_jhalf()[0]
    ket = {initial: 1 + 0j}

    ident = [[{} for _ in range(2)] for _ in range(2)]
    max_identity_error = 0.0
    max_final_gauss_leak_identity = 0.0
    for i in range(2):
        for j in range(2):
            s, _, gleak = inverse_then_forward(initial, v, w, i, j, JMAX2, False)
            ident[i][j] = s
            target = ket if i == j else {}
            max_identity_error = max(max_identity_error, state_diff_norm(s, target))
            max_final_gauss_leak_identity = max(max_final_gauss_leak_identity, gleak)

    Vstate = volume_on_gauss(initial, v)
    C = [[{} for _ in range(2)] for _ in range(2)]
    max_charged_leak = 0.0
    max_final_gauss_leak_volume = 0.0
    for i in range(2):
        for j in range(2):
            hVh, cleak, gleak = inverse_then_forward(initial, v, w, i, j, JMAX2, True)
            max_charged_leak = max(max_charged_leak, cleak)
            max_final_gauss_leak_volume = max(max_final_gauss_leak_volume, gleak)
            out = {}
            if i == j:
                PW.add_dict(out, Vstate, +1)
            PW.add_dict(out, hVh, -1)
            C[i][j] = PW.prune_state(out, 1e-10)

    Cnorm = matrix_state_norm(C)
    supports = [[len(C[i][j]) for j in range(2)] for i in range(2)]
    max_spin = max((max(k[0]) for row in C for s in row for k in s), default=0) / 2

    passed = (
        max_identity_error < 1e-10
        and max_final_gauss_leak_identity < 1e-10
        and max_charged_leak < 1e-10
        and max_final_gauss_leak_volume < 1e-10
        and Cnorm > 1e-10
        and max_spin <= 1.5 + 1e-12
    )
    return {
        "status": "exact Peter-Weyl covariantized volume leg C_e(V)=h[h^-1,V]",
        "passed": bool(passed),
        "edge": [v, w],
        "input": "all ten links j=1/2; all five K=0",
        "Jmax": 1.5,
        "two_hit_identity_max_state_error": max_identity_error,
        "two_hit_identity_max_final_Gauss_projection_leakage": max_final_gauss_leak_identity,
        "charged_volume_max_Jhalf_projection_leakage": max_charged_leak,
        "volume_leg_max_final_Gauss_projection_leakage": max_final_gauss_leak_volume,
        "C_matrix_supports": supports,
        "C_matrix_Frobenius_state_norm": Cnorm,
        "max_spin_reached": max_spin,
        "definition": "C_ij(V)=delta_ij V-sum_k h_ik V h^-1_kj",
        "next_use": "Replace V by K_v=[V_v,H_E,v] on the same charged layer to obtain C_e(K_v), then assemble the epsilon^{ijk} trace of two K legs and one V leg.",
        "scope_note": "One exact Lorentzian covariant volume factor only; K legs, triple H_L and HDA remain open.",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--v", type=int, default=0)
    ap.add_argument("--w", type=int, default=1)
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    out = run(a.v, a.w); text = json.dumps(out, indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
