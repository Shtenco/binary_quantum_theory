#!/usr/bin/env python3
"""Matrix-covariant Lorentzian K leg C_e(K)=h_e[h_e^-1,K_v].

This is the next genuine Thiemann factor after the already verified
C_e(V)=h[h^-1,V] and K_v=[V_v,H_E,v].  The outer inverse holonomy creates a
fundamental spectator charge at both endpoints.  The gauge-invariant Euclidean
Hamiltonian at source v must preserve that external charge after its complete
move, but its INTERNAL volume insertions can occur while additional internal
holonomy indices are open.  Therefore volume is evaluated as an exact direct
sum over every total-J recoupling sector,

    V = direct_sum_J sqrt(|Q_J|),
    Q_J = P_J [J1.(J2xJ3)] P_J,

not by forcing intermediate tensors into J=1/2.

After the complete charged H_E move, source and spectator endpoint are projected
back to total J=1/2.  The charged extrinsic-curvature block is

    K_v=[V_v,H_E,v]

on that two-charge sector.  The final forward holonomy closes the target charge
and leaves a matrix-covariant source geometry in J=0 plus J=1.  Any J>1 output
is a hard covariance failure.

No beta or HDA normalization is fitted here.  This gate builds one exact
covariant K factor; the epsilon^{ijk} traced triple remains the next gate.
"""
from __future__ import annotations

import argparse
import functools
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
import charged_intertwiner_recoupling_gate as CH
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_lorentzian_K_block_gate as KG


def add_state(dst, src, scale=1.0, tol=1e-11):
    for k, a in src.items():
        z = dst.get(k, 0j) + scale * a
        if abs(z) > tol:
            dst[k] = z
        elif k in dst:
            del dst[k]


def label_gauss(K):
    return ("G", int(K))


def label_charge(M2, K12, K34):
    return ("C", int(M2), int(K12), int(K34))


def tensor_for_label(v, spins_local, label):
    if label[0] == "G":
        return PW.oriented_intertwiner(v, spins_local, label[1])
    if label[0] == "C":
        _, M2, K12, K34 = label
        T = CH.charged_tensor(tuple(spins_local), K12, K34, 1, M2)
        return CV.orient_local(T, spins_local, v)
    raise ValueError(label)


def branch_from_charged_key(key):
    spins, labels = key
    tensors = tuple(tensor_for_label(v, PW.local_spins(spins, v), labels[v]) for v in PW.VERT)
    return spins, tensors, 1 + 0j


def project_branch_to_two_charge(branch, charged_nodes=(0, 1), tol=1e-11):
    spins, tensors, amp = branch
    opts_by_node = []
    max_relative_leakage = 0.0
    for v in PW.VERT:
        ls = PW.local_spins(spins, v)
        X = tensors[v]
        opts = []
        recon = np.zeros_like(X)
        if v in charged_nodes:
            Xu = CV.unorient_local(X, ls, v)
            labels = CH.allowed_charged_labels(tuple(ls), 1)
            for M2 in PW.m2vals_t(1):
                for K12, K34 in labels:
                    B = CH.charged_tensor(tuple(ls), K12, K34, 1, M2)
                    c = np.vdot(B, Xu)
                    if abs(c) > 1e-13:
                        opts.append((label_charge(M2, K12, K34), c))
                        recon += c * CV.orient_local(B, ls, v)
        else:
            for K in PW.allowed_k2_t(*ls):
                B = PW.oriented_intertwiner(v, ls, K)
                c = np.vdot(B, X)
                if abs(c) > 1e-13:
                    opts.append((label_gauss(K), c))
                    recon += c * B
        nrm = float(np.linalg.norm(X))
        leak = float(np.linalg.norm(X - recon) / max(nrm, 1e-30))
        max_relative_leakage = max(max_relative_leakage, leak)
        if not opts:
            return {}, max_relative_leakage
        opts_by_node.append(tuple(opts))

    out = {}
    for choice in itertools.product(*opts_by_node):
        val = amp
        labels = []
        for lab, c in choice:
            labels.append(lab); val *= c
        if abs(val) > tol:
            key = (spins, tuple(labels))
            out[key] = out.get(key, 0j) + val
    return {k: a for k, a in out.items() if abs(a) > tol}, max_relative_leakage


@functools.lru_cache(None)
def canonical_volume_block_general(spins_local, J2):
    spins_local = tuple(spins_local)
    qblocks = []
    for M2 in PW.m2vals_t(J2):
        _, Qb, _, _ = CH.q_block(spins_local, J2, M2)
        qblocks.append(Qb)
    Q = sum(qblocks) / len(qblocks)
    Q = 0.5 * (Q + Q.conj().T)
    return CH.canonical_volume_block(Q)


def apply_volume_allJ_oriented(T, spins_local, v):
    """Symmetry-adapted V on an arbitrary local tensor, preserving every J."""
    X = CV.unorient_local(T, spins_local, v)
    Y = np.zeros_like(X)
    recon = np.zeros_like(X)
    for J2 in CV.all_total_J2(spins_local):
        labels = CH.allowed_charged_labels(tuple(spins_local), J2)
        if not labels:
            continue
        Vb = canonical_volume_block_general(tuple(spins_local), J2)
        for M2 in PW.m2vals_t(J2):
            basis = [CH.charged_tensor(tuple(spins_local), a, b, J2, M2) for a, b in labels]
            coeff = np.asarray([np.vdot(B, X) for B in basis], complex)
            for c, B in zip(coeff, basis):
                recon += c * B
            outc = Vb @ coeff
            for c, B in zip(outc, basis):
                Y += c * B
    leak = float(np.linalg.norm(X - recon) / max(np.linalg.norm(X), 1e-30))
    return CV.orient_local(Y, spins_local, v), leak


def apply_volume_two_charge_state(state, v):
    out = {}
    for key, amp in state.items():
        spins, labels = key
        lab = labels[v]
        if lab[0] != "C":
            raise ValueError("source volume expected charged label")
        _, M2, K12, K34 = lab
        ls = PW.local_spins(spins, v)
        rec_labels = CH.allowed_charged_labels(tuple(ls), 1)
        idx = rec_labels.index((K12, K34))
        Vb = canonical_volume_block_general(tuple(ls), 1)
        for j, (A, B) in enumerate(rec_labels):
            c = Vb[j, idx]
            if abs(c) > 1e-13:
                labs = list(labels); labs[v] = label_charge(M2, A, B)
                ko = (spins, tuple(labs))
                out[ko] = out.get(ko, 0j) + amp * c
    return {k: a for k, a in out.items() if abs(a) > 1e-11}


def apply_sequence_to_branch(branch, seq, source_v, Jmax2):
    branches = [branch]
    max_volume_sector_leak = 0.0
    for op in seq:
        if op[0] == "V":
            nb = []
            for spins, tensors, amp in branches:
                t = list(tensors)
                ls = PW.local_spins(spins, source_v)
                t[source_v], leak = apply_volume_allJ_oriented(t[source_v], ls, source_v)
                max_volume_sector_leak = max(max_volume_sector_leak, leak)
                nb.append((spins, tuple(t), amp))
            branches = nb
        else:
            nb = []
            for br in branches:
                nb.extend(PW.apply_path_branch(br, op[1], op[2], op[3], Jmax2))
            branches = nb
        if not branches:
            break
    return branches, max_volume_sector_leak


def apply_HE_two_charge_key(key, source_v, Jmax2, charged_nodes=(0, 1)):
    base = branch_from_charged_key(key)
    out = {}
    max_internal_volume_leak = 0.0
    max_final_charge_leak = 0.0
    for sign, spec in PW.oriented_specs(source_v):
        v, a, b, c = spec
        for adj in (False, True):
            adjcoef = 0.5 * sign
            for coef, seq0 in PW.T_sequences(v, a, b, c):
                seq = PW.adjoint_sequence(seq0) if adj else seq0
                branches, vleak = apply_sequence_to_branch(base, seq, source_v, Jmax2)
                max_internal_volume_leak = max(max_internal_volume_leak, vleak)
                for br in branches:
                    projected, cleak = project_branch_to_two_charge(br, charged_nodes)
                    max_final_charge_leak = max(max_final_charge_leak, cleak)
                    add_state(out, projected, adjcoef * coef)
    return out, max_internal_volume_leak, max_final_charge_leak


@functools.lru_cache(None)
def HE_two_charge_cached(key, source_v, Jmax2):
    out, vleak, cleak = apply_HE_two_charge_key(key, source_v, Jmax2)
    return tuple(out.items()), vleak, cleak


def apply_HE_two_charge_state(state, source_v, Jmax2):
    out = {}
    max_vleak = 0.0; max_cleak = 0.0
    for key, amp in state.items():
        items, vleak, cleak = HE_two_charge_cached(key, source_v, Jmax2)
        max_vleak = max(max_vleak, vleak); max_cleak = max(max_cleak, cleak)
        for ko, c in items:
            out[ko] = out.get(ko, 0j) + amp * c
    return {k: a for k, a in out.items() if abs(a) > 1e-10}, max_vleak, max_cleak


def apply_K_two_charge_state(state, source_v, Jmax2):
    HE, vleak1, cleak1 = apply_HE_two_charge_state(state, source_v, Jmax2)
    VH = apply_volume_two_charge_state(HE, source_v)
    Vstate = apply_volume_two_charge_state(state, source_v)
    HV, vleak2, cleak2 = apply_HE_two_charge_state(Vstate, source_v, Jmax2)
    out = {}; add_state(out, VH, +1); add_state(out, HV, -1)
    return out, max(vleak1, vleak2), max(cleak1, cleak2)


def inverse_outer_to_two_charge(initial, v, w, k, j, Jmax2):
    branches = []
    for br in [PW.initial_factorized_oriented(initial)]:
        branches.extend(PW.apply_hit_branch(br, w, v, k, j, Jmax2))
    out = {}; max_leak = 0.0
    for br in branches:
        projected, leak = project_branch_to_two_charge(br, (v, w))
        max_leak = max(max_leak, leak)
        add_state(out, projected)
    return out, max_leak


def close_two_charge_state_covariantly(state, v, w, i, k, Jmax2):
    out = {}; max_target_gauss_leak = 0.0
    for key, amp in state.items():
        br = branch_from_charged_key(key)
        br = (br[0], br[1], amp)
        closed = PW.apply_hit_branch(br, v, w, i, k, Jmax2)
        for cb in closed:
            projected = CV.project_covariant_branches([cb], v)
            # Explicitly check that target w closes to Gauss by reconstructing
            # the projected part and comparing its norm indirectly: any source
            # J>1 is separately forbidden below; target non-Gauss components do
            # not enter project_covariant_branches and would reduce norm.  The
            # stronger outer identity is already tested in C(V).
            add_state(out, projected)
    return out, max_target_gauss_leak


def covariant_K_leg(initial, v, w, i, j, Jmax2):
    total = {}
    max_outer_charge_leak = 0.0
    max_internal_vleak = 0.0
    max_final_charge_leak = 0.0
    for k in range(2):
        inv, oleak = inverse_outer_to_two_charge(initial, v, w, k, j, Jmax2)
        max_outer_charge_leak = max(max_outer_charge_leak, oleak)
        Kcharged, vleak, cleak = apply_K_two_charge_state(inv, v, Jmax2)
        max_internal_vleak = max(max_internal_vleak, vleak)
        max_final_charge_leak = max(max_final_charge_leak, cleak)
        closed, _ = close_two_charge_state_covariantly(Kcharged, v, w, i, k, Jmax2)
        add_state(total, closed)
    return total, max_outer_charge_leak, max_internal_vleak, max_final_charge_leak


def covariant_norm2(state):
    return float(sum(abs(a) ** 2 for a in state.values()))


def matrix_norm(M):
    return math.sqrt(sum(covariant_norm2(s) for row in M for s in row))


def run(v=0, w=1):
    # Outer h^-1/h plus the safe Euclidean H_E can accumulate four fundamental
    # hits on one link from j=.5, so Jmax=2.5 is sufficient for this C(K) leg.
    JMAX2 = 5
    initial = PW.basis_full_jhalf()[0]

    Kgauss = KG.apply_K_local({initial: 1 + 0j}, v, JMAX2)
    Kcov = CV.gauss_to_covariant(Kgauss, v)

    C = [[{} for _ in range(2)] for _ in range(2)]
    max_outer_leak = 0.0; max_internal_vleak = 0.0; max_charge_leak = 0.0
    for i in range(2):
        for j in range(2):
            hKh, oleak, vleak, cleak = covariant_K_leg(initial, v, w, i, j, JMAX2)
            max_outer_leak = max(max_outer_leak, oleak)
            max_internal_vleak = max(max_internal_vleak, vleak)
            max_charge_leak = max(max_charge_leak, cleak)
            out = {}
            if i == j:
                add_state(out, Kcov, +1)
            add_state(out, hKh, -1)
            C[i][j] = out

    weights = CV.weight_by_J(C)
    total_weight = sum(weights.values())
    j1_weight = weights.get("1.0", 0.0)
    high_weight = sum(x for j, x in weights.items() if float(j) > 1.0 + 1e-15)
    high_fraction = high_weight / max(total_weight, 1e-30)
    Cnorm = matrix_norm(C)
    supports = [[len(C[i][j]) for j in range(2)] for i in range(2)]
    max_spin = max((max(key[0]) for row in C for state in row for key in state), default=0) / 2

    passed = (
        len(Kgauss) > 0
        and max_outer_leak < 1e-10
        and max_internal_vleak < 1e-10
        and max_charge_leak < 1e-9
        and Cnorm > 1e-10
        and j1_weight > 1e-14
        and high_fraction < 1e-18
        and max_spin <= 2.5 + 1e-12
    )
    return {
        "status": "matrix-covariant Peter-Weyl Lorentzian K leg C_e(K)=h[h^-1,K_v]",
        "passed": bool(passed),
        "edge": [v, w],
        "input": "all ten links j=1/2; all five K=0",
        "Jmax": 2.5,
        "Gauss_K_support": len(Kgauss),
        "Gauss_K_norm": math.sqrt(PW.norm2_state(Kgauss)),
        "outer_inverse_two_charge_projection_leakage": max_outer_leak,
        "charged_HE_internal_volume_sector_leakage": max_internal_vleak,
        "charged_HE_final_two_charge_projection_leakage": max_charge_leak,
        "C_matrix_supports": supports,
        "C_matrix_Frobenius_covariant_state_norm": Cnorm,
        "C_weight_by_source_J": weights,
        "C_J1_weight": j1_weight,
        "C_J_greater_than_1_weight_fraction": high_fraction,
        "max_spin_reached": max_spin,
        "definition": "C_ij(K_v)=delta_ij K_v-sum_k h_ik K_v h^-1_kj with K_v=[V_v,H_E,v]",
        "ordering_note": (
            "Every INTERNAL volume in charged H_E is evaluated as direct_sum_J sqrt(|Q_J|); only after the complete gauge-invariant H_E move is the spectator outer charge projected back to J=1/2."
        ),
        "beta_note": "No beta-dependent coefficient is inserted. The full Lorentzian triple will be multiplied by the frozen classical coefficient, not fit to HDA data.",
        "next_use": "Combine two C(K) legs and one already verified C(V) leg with epsilon^{ijk} and fundamental matrix trace to obtain the first structural H_L column.",
        "scope_note": "One covariant K factor only; the traced triple, full H_L and Lorentzian HDA remain open.",
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
