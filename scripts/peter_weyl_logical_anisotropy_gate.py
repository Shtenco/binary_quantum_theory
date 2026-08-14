#!/usr/bin/env python3
"""Project Peter-Weyl Euclidean dynamics onto the logical geometry-qubit sector.

Goal: test whether the already existing Euclidean geometry dynamics can gap the
continuous Bell-gluing/Heisenberg mirror parent by generating logical
pseudospin anisotropy.

Two levels are kept sharply separate.

1. Exact first-order support no-go.
   On the all-j=1/2 K5 logical sector, every oriented Euclidean triangle term
   contains fundamental holonomy hits on loop edges. A single fundamental hit
   sends j -> j +/- 1/2, while V does not change spin. Therefore one H_E action
   cannot return to the all-j=1/2 sector. The executable gate checks

       P H_E^sine P = 0

   on the four two-logical-qubit basis states used below.

2. Second-order structural return kernel.
   Since H_E^sine is Hermitian, for H_01=H_E,0+H_E,1,

       K_return = P H_01^2 P

   has matrix elements

       K_ij = <H_01 i | H_01 j>.

   This requires only first-action states and no arbitrary energy denominator.
   K_return is decomposed exactly into the 16 Pauli tensors

       I,X,Y,Z tensor I,X,Y,Z.

   The 3x3 two-qubit coupling tensor is then transformed by the same B-sublattice
   pi rotation around Y that maps the frozen Bell gluing to the AF Heisenberg
   parent. Its traceless/off-diagonal part is the finite structural anisotropy
   diagnostic.

IMPORTANT: K_return is NOT claimed to be a physical Schrieffer-Wolff effective
Hamiltonian. A true effective Hamiltonian needs a justified dynamical
resolvent/energy denominator in the constrained theory. This gate answers the
more primitive question: does the first nonzero return channel already carry
logical-axis anisotropy?
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
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_zeroaware_volume_migration_experiment as ZVM


JMAX2 = 3  # j<=3/2 is the complete support wall for one H_E hit from all-j=1/2.
TOL = 1e-11
PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


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


def logical_key(k0, k1, v=0, w=1):
    spins = (1,) * len(PW.EDGES)
    Ks = [0] * len(PW.VERT)
    Ks[v] = int(k0)
    Ks[w] = int(k1)
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


def run():
    ZVM.patch_and_clear()

    # Basis order |00>,|01>,|10>,|11>, with K=0/2 as logical 0/1.
    logical_pairs = [(0, 0), (0, 2), (2, 0), (2, 2)]
    keys = [logical_key(a, b) for a, b in logical_pairs]
    images = []
    first_order_projection_norms = []
    image_rows = []

    for pair, key in zip(logical_pairs, keys):
        img = apply_pair_HE(key)
        projected = {k: v for k, v in img.items() if is_all_jhalf(k)}
        pnorm = sparse_norm(projected)
        first_order_projection_norms.append(pnorm)
        images.append(img)
        image_rows.append({
            "logical_K_pair": list(pair),
            "H01_support": len(img),
            "H01_norm": sparse_norm(img),
            "PH01P_norm": pnorm,
            "max_spin_after_one_hit": max((max(k[0]) / 2 for k in img), default=0.0),
        })

    K = np.zeros((4, 4), dtype=complex)
    for i in range(4):
        for j in range(4):
            K[i, j] = sparse_inner(images[i], images[j])

    herm_err = float(np.linalg.norm(K - K.conj().T))
    evals = np.linalg.eigvalsh((K + K.conj().T) / 2).real
    coeff, recon_err = pauli_decompose(K)

    labels = ("X", "Y", "Z")
    J_orig = np.array([[coeff[a + b] for b in labels] for a in labels], dtype=complex)
    hA = np.array([coeff[a + "I"] for a in labels], dtype=complex)
    hB = np.array([coeff["I" + b] for b in labels], dtype=complex)

    # Same B-sublattice pi rotation around Y used in MIRRORHEIS.
    Rb = np.diag([-1.0, +1.0, -1.0])
    J_rot = J_orig @ Rb
    J_real = J_rot.real
    J_imag_norm = float(np.linalg.norm(J_rot.imag))
    j_iso = float(np.trace(J_real) / 3.0)
    anis = J_real - j_iso * np.eye(3)
    Jnorm = float(np.linalg.norm(J_real))
    anis_abs = float(np.linalg.norm(anis))
    anis_rel = anis_abs / max(Jnorm, 1e-30)
    offdiag = J_real - np.diag(np.diag(J_real))

    first_order_zero = max(first_order_projection_norms, default=0.0) < 1e-12
    algebra_pass = (
        first_order_zero
        and herm_err < 1e-9
        and recon_err < 1e-8
        and float(np.min(evals)) > -1e-8
        and J_imag_norm < 1e-8
    )

    if Jnorm < 1e-14:
        classification = "no two-logical-qubit coupling resolved in the quadratic return kernel"
    elif anis_rel < 1e-8:
        classification = "Heisenberg-isotropic quadratic return kernel"
    else:
        classification = "anisotropic quadratic return kernel"

    return {
        "status": "Peter-Weyl logical pseudospin anisotropy gate",
        "passed": bool(algebra_pass),
        "scope": (
            "PASS certifies the projection/decomposition computation, not isotropy. Anisotropy is a physical "
            "measurement reported separately. K_return=P(H_E0+H_E1)^2P is a structural return kernel, not a "
            "Schrieffer-Wolff Hamiltonian because no constrained-theory energy denominator has been assumed."
        ),
        "ordering": "physical structural H_E^sine=(T-T^dagger)/(2i)",
        "Jmax_one_hit": JMAX2 / 2,
        "basis_order": ["K0K1=00", "02", "20", "22"],
        "first_order": {
            "claim": "P_all-jhalf (H_E0+H_E1) P_all-jhalf = 0",
            "passed": bool(first_order_zero),
            "max_projection_norm": max(first_order_projection_norms, default=0.0),
            "columns": image_rows,
            "support_reason": (
                "fundamental triangle holonomy hits change odd-hit loop-edge spins by +/-1/2 while V preserves spin"
            ),
        },
        "quadratic_return_kernel": {
            "matrix": [[cjson(K[i, j]) for j in range(4)] for i in range(4)],
            "eigenvalues": [float(x) for x in evals],
            "hermiticity_error": herm_err,
            "pauli_reconstruction_error": recon_err,
            "pauli_coefficients": {k: cjson(v) for k, v in coeff.items()},
        },
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
        "next_physics_gate": (
            "If anisotropic, derive the correct constrained second-order/resolvent effective kernel and its RG "
            "scaling under PL refinement. If isotropic, test the Lorentzian and route-dressed return channels next."
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
