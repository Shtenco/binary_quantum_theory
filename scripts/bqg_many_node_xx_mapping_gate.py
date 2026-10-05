from __future__ import annotations

import numpy as np


def spin_hamiltonian(M: int) -> np.ndarray:
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    dim = 2**M
    H = np.zeros((dim, dim), dtype=complex)

    def op_on_pair(A, B, i):
        out = np.array([[1.0 + 0j]])
        for site in range(M):
            if site == i:
                factor = A
            elif site == i + 1:
                factor = B
            else:
                factor = I
            out = np.kron(out, factor)
        return out

    for i in range(M - 1):
        H += 1.5 * np.eye(dim)
        H -= 0.75 * (op_on_pair(X, X, i) + op_on_pair(Z, Z, i))
    return H


def free_fermion_many_body_energies(M: int) -> np.ndarray:
    # After a global pi/2 rotation about X:
    # H = 3/2(M-1) - 3/4 sum(XX+YY)
    #   = 3/2(M-1) - 3/2 sum(c_i^† c_{i+1}+h.c.)
    k = np.arange(1, M + 1) * np.pi / (M + 1)
    eps = -3.0 * np.cos(k)
    const = 1.5 * (M - 1)
    energies = []
    for mask in range(2**M):
        occ = np.array([(mask >> j) & 1 for j in range(M)], dtype=float)
        energies.append(const + float(np.dot(eps, occ)))
    return np.sort(np.array(energies))


def predicted_gap(M: int) -> float:
    if M % 2 == 0:
        return 3.0 * np.sin(np.pi / (2 * (M + 1)))
    return 3.0 * np.sin(np.pi / (M + 1))


for M in range(2, 7):
    e_spin = np.linalg.eigvalsh(spin_hamiltonian(M))
    e_ff = free_fermion_many_body_energies(M)
    assert np.allclose(e_spin, e_ff, atol=1e-10)

    e0 = e_spin[0]
    ground_deg = int(np.sum(np.isclose(e_spin, e0, atol=1e-10)))
    expected_deg = 1 if M % 2 == 0 else 2
    assert ground_deg == expected_deg

    excited = e_spin[~np.isclose(e_spin, e0, atol=1e-10)]
    gap = float(excited[0] - e0)
    assert np.isclose(gap, predicted_gap(M), atol=1e-10)

    print(
        f"M={M}: ground_deg={ground_deg}, gap={gap:.12f}, "
        f"predicted={predicted_gap(M):.12f}"
    )

print("single-particle dispersion: epsilon_n=-3 cos(n*pi/(M+1))")
print("even M gap = 3 sin(pi/[2(M+1)])")
print("odd M: exact zero mode, ground degeneracy 2")
print("odd M nonzero gap = 3 sin(pi/(M+1))")
print("thermodynamic limit: gap -> 0 as O(1/M)")
print("PASS")
