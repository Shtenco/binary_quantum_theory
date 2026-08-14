#!/usr/bin/env python3
"""Project Peter-Weyl Euclidean dynamics onto the logical geometry-qubit sector.

The gate tests whether the already existing Euclidean geometry dynamics can gap
the continuous Bell-gluing/Heisenberg mirror parent by generating logical
pseudospin anisotropy.

Two levels are kept sharply separate.

1. Exact first-order support no-go.
   On the all-j=1/2 K5 logical sector, every oriented Euclidean triangle term
   contains fundamental holonomy hits on loop edges. A single fundamental hit
   sends j -> j +/- 1/2, while V does not change spin. Therefore

       P H_E^sine P = 0.

2. Second-order structural return kernel.
   For H_01=H_E,0+H_E,1,

       K_return = P H_01^2 P,
       K_ij = <H_01 i | H_01 j>.

   The four-state pair kernel is decomposed into all Pauli tensors. Two versions
   are reported:

   (a) a shape-polarized control with the other three logical K5 qubits fixed
       to K=0;
   (b) the environment-unbiased pair kernel

       Kbar_01 = (1/2^3) Tr_{2,3,4} K_return,

       implemented by averaging the pair Gram matrix over all eight logical
       environment basis states. Because the traced environment is the identity,
       this result is basis independent and does not prefer K=0 by construction.

IMPORTANT: K_return is NOT a physical Schrieffer-Wolff Hamiltonian. A true
second-order effective Hamiltonian needs a justified constrained-theory
resolvent/energy denominator. This gate measures structural symmetry breaking
in the first nonzero return channel.
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
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_zeroaware_volume_migration_experiment as ZVM


JMAX2 = 3
TOL = 1e-11
PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}
LABELS = ("X", "Y", "Z")
RB = np.diag([-1.0, +1.0, -1.0])
PAIR_STATES = ((0, 0), (0, 2), (2, 0), (2, 2))
ENV_STATES = tuple(itertools.product((0, 2), repeat=3))


def sparse_add(dst, src, scale=1.0):
    for k, a in src.items():
        z = dst.get(k, 0j) + scale * a
        if abs(z) > TOL:
            dst[k] = z
        elif k in dst:
            del dst[k]


def sparse_inner(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(np.conj(v) * b.get(k, 0j) for k, v in a.items())


def sparse_norm(a):
    return math.sqrt(float(sum(abs(v) ** 2 for v in a.values())))


def logical_key(k0, k1, env=(0, 0, 0), v=0, w=1):
    spins = (1,) * len(PW.EDGES)
    Ks = [0] * len(PW.VERT)
    Ks[v] = int(k0)
    Ks[w] = int(k1)
    env_nodes = [u for u in PW.VERT if u not in (v, w)]
    for u, K in zip(env_nodes, env):
        Ks[u] = int(K)
    return spins, tuple(Ks)


def is_all_jhalf(key):
    return all(s == 1 for s in key[0])


def apply_pair_HE(key, v=0, w=1):
    state = {key: 1.0 + 0j}
    out = {}
    sparse_add(out, SINE.safe_H_sine(state, v, JMAX2))
    sparse_add(out, SINE.safe_H_sine(state, w, JMAX2))
    return out


def pauli_decompose(K):
    coeff = {}
    recon = np.zeros((4, 4), dtype=complex)
    for a, A in PAULI.items():
        for b, B in PAULI.items():
            P = np.kron(A, B)
            c = np.trace(P @ K) / 4.0
            coeff[f"{a}{b}"] = c
            recon += c * P
    return coeff, float(np.linalg.norm(recon - K))


def cjson(z):
    z = complex(z)
    return [float(z.real), float(z.imag)]


def kernel_from_images(images):
    K = np.zeros((4, 4), dtype=complex)
    for i in range(4):
        for j in range(4):
            K[i, j] = sparse_inner(images[i], images[j])
    return K


def analyze_kernel(K):
    herm_err = float(np.linalg.norm(K - K.conj().T))
    Kh = (K + K.conj().T) / 2
    evals = np.linalg.eigvalsh(Kh).real
    coeff, recon_err = pauli_decompose(K)

    J_orig = np.array([[coeff[a + b] for b in LABELS] for a in LABELS], dtype=complex)
    hA = np.array([coeff[a + "I"] for a in LABELS], dtype=complex)
    hB = np.array([coeff["I" + b] for b in LABELS], dtype=complex)
    J_rot = J_orig @ RB
    J_real = J_rot.real
    J_imag_norm = float(np.linalg.norm(J_rot.imag))
    j_iso = float(np.trace(J_real) / 3.0)
    anis = J_real - j_iso * np.eye(3)
    Jnorm = float(np.linalg.norm(J_real))
    anis_abs = float(np.linalg.norm(anis))
    anis_rel = anis_abs / max(Jnorm, 1e-30)
    offdiag = J_real - np.diag(np.diag(J_real))

    mirror_forbidden = ("IY", "YI", "XY", "YX", "YZ", "ZY")
    mirror_forbidden_norm = math.sqrt(sum(abs(coeff[x]) ** 2 for x in mirror_forbidden))
    allowed_norm = math.sqrt(sum(abs(v) ** 2 for k, v in coeff.items() if k not in mirror_forbidden))

    if Jnorm < 1e-14:
        classification = "no two-logical-qubit coupling resolved"
    elif anis_rel < 1e-8:
        classification = "Heisenberg-isotropic quadratic return kernel"
    else:
        classification = "anisotropic quadratic return kernel"

    return {
        "matrix": [[cjson(K[i, j]) for j in range(4)] for i in range(4)],
        "eigenvalues": [float(x) for x in evals],
        "hermiticity_error": herm_err,
        "pauli_reconstruction_error": recon_err,
        "pauli_coefficients": {k: cjson(v) for k, v in coeff.items()},
        "heisenberg_frame": {
            "B_sublattice_rotation": "diag(X,Y,Z)=(-1,+1,-1)",
            "coupling_tensor_XYZ": [[cjson(J_rot[i, j]) for j in range(3)] for i in range(3)],
            "local_field_A_XYZ": [cjson(x) for x in hA],
            "local_field_B_XYZ_before_rotation": [cjson(x) for x in hB],
            "isotropic_scalar": j_iso,
            "coupling_tensor_norm": Jnorm,
            "anisotropy_absolute_frobenius": anis_abs,
            "anisotropy_relative": anis_rel,
            "offdiagonal_norm": float(np.linalg.norm(offdiag)),
            "imaginary_norm": J_imag_norm,
            "classification": classification,
        },
        "mirror_selection": {
            "forbidden_coefficients": list(mirror_forbidden),
            "forbidden_norm": mirror_forbidden_norm,
            "allowed_norm": allowed_norm,
            "relative_forbidden_norm": mirror_forbidden_norm / max(allowed_norm, 1e-30),
        },
    }


def run():
    ZVM.patch_and_clear()

    environment_kernels = []
    environment_rows = []
    all_first_projection = []
    all_max_spin = []

    for env in ENV_STATES:
        images = []
        cols = []
        for pair in PAIR_STATES:
            key = logical_key(pair[0], pair[1], env)
            img = apply_pair_HE(key)
            projected = {k: v for k, v in img.items() if is_all_jhalf(k)}
            pnorm = sparse_norm(projected)
            all_first_projection.append(pnorm)
            max_spin = max((max(k[0]) / 2 for k in img), default=0.0)
            all_max_spin.append(max_spin)
            images.append(img)
            cols.append({
                "logical_K_pair": list(pair),
                "H01_support": len(img),
                "H01_norm": sparse_norm(img),
                "PH01P_norm": pnorm,
                "max_spin_after_one_hit": max_spin,
            })
        Kenv = kernel_from_images(images)
        environment_kernels.append(Kenv)
        environment_rows.append({
            "environment_K234": list(env),
            "columns": cols,
            "kernel_anisotropy_relative": analyze_kernel(Kenv)["heisenberg_frame"]["anisotropy_relative"],
        })

    fixed_K = environment_kernels[0]
    averaged_K = sum(environment_kernels) / len(environment_kernels)
    fixed = analyze_kernel(fixed_K)
    averaged = analyze_kernel(averaged_K)

    first_order_zero = max(all_first_projection, default=0.0) < 1e-12
    algebra_pass = (
        first_order_zero
        and fixed["hermiticity_error"] < 1e-9
        and averaged["hermiticity_error"] < 1e-9
        and fixed["pauli_reconstruction_error"] < 1e-8
        and averaged["pauli_reconstruction_error"] < 1e-8
        and min(fixed["eigenvalues"]) > -1e-8
        and min(averaged["eigenvalues"]) > -1e-8
        and fixed["heisenberg_frame"]["imaginary_norm"] < 1e-8
        and averaged["heisenberg_frame"]["imaginary_norm"] < 1e-8
    )

    return {
        "status": "Peter-Weyl logical pseudospin anisotropy gate",
        "passed": bool(algebra_pass),
        "scope": (
            "PASS certifies the projection, environment trace and Pauli decomposition. K_return=P(H_E0+H_E1)^2P "
            "is a structural return kernel, not a physical Schrieffer-Wolff Hamiltonian because no constrained-theory "
            "energy denominator/resolvent has been assumed."
        ),
        "ordering": "physical structural H_E^sine=(T-T^dagger)/(2i)",
        "Jmax_one_hit": JMAX2 / 2,
        "basis_order": ["K0K1=00", "02", "20", "22"],
        "first_order": {
            "claim": "P_all-jhalf (H_E0+H_E1) P_all-jhalf = 0",
            "passed": bool(first_order_zero),
            "max_projection_norm_over_all_32_logical_columns": max(all_first_projection, default=0.0),
            "max_spin_after_one_hit": max(all_max_spin, default=0.0),
            "support_reason": (
                "fundamental triangle holonomy hits change odd-hit loop-edge spins by +/-1/2 while V preserves spin"
            ),
        },
        "shape_polarized_environment_K234_000": fixed,
        "maximally_mixed_environment_partial_trace": {
            "definition": "(1/8) Tr_{logical nodes 2,3,4} P(H_E0+H_E1)^2P",
            "environment_dimension": 8,
            **averaged,
        },
        "environment_controls": environment_rows,
        "comparison": {
            "fixed_anisotropy_relative": fixed["heisenberg_frame"]["anisotropy_relative"],
            "traced_anisotropy_relative": averaged["heisenberg_frame"]["anisotropy_relative"],
            "traced_mirror_forbidden_relative_norm": averaged["mirror_selection"]["relative_forbidden_norm"],
        },
        "next_physics_gate": (
            "If the maximally mixed environment remains anisotropic, construct a justified constrained resolvent or "
            "RG/coarse-grained return kernel. If the trace restores isotropy, treat the K=0 result as environment-induced "
            "rather than intrinsic pseudospin breaking."
        ),
    }


def main():
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
