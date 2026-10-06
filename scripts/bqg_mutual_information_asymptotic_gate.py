from __future__ import annotations

import math
import numpy as np


def fermion_correlation(r: int) -> float:
    """Infinite half-filled XX-chain <c_0^† c_r>."""
    if r == 0:
        return 0.5
    return math.sin(math.pi * r / 2.0) / (math.pi * r)


def majorana_g(n: int) -> float:
    """G_n = 2 <c_0^†c_n> - delta_{n0}."""
    if n == 0:
        return 0.0
    return 2.0 * math.sin(math.pi * n / 2.0) / (math.pi * n)


def cxx(r: int) -> float:
    """Exact thermodynamic-limit Toeplitz determinant for <X_0 X_r>."""
    m = np.array(
        [[majorana_g(j - k - 1) for k in range(r)] for j in range(r)],
        dtype=float,
    )
    return float(np.linalg.det(m))


def czz(r: int) -> float:
    """Exact <Z_0 Z_r> at half filling for r>0."""
    c = fermion_correlation(r)
    return -4.0 * c * c


def pair_eigenvalues(r: int) -> np.ndarray:
    """Two-logical-spin density-matrix eigenvalues in the XX basis."""
    x = cxx(r)
    z = czz(r)
    vals = np.array(
        [
            (1.0 + z) / 4.0,
            (1.0 + z) / 4.0,
            (1.0 - z + 2.0 * x) / 4.0,
            (1.0 - z - 2.0 * x) / 4.0,
        ],
        dtype=float,
    )
    return vals


def mutual_information_bits(r: int) -> float:
    vals = pair_eigenvalues(r)
    assert np.min(vals) > -1e-12
    vals = vals[vals > 1e-15]
    entropy = -float(np.sum(vals * np.log2(vals)))
    # Each one-site reduced state is I/2, so S(A)=S(B)=1 bit.
    return 2.0 - entropy


# Cheap asymptotic certification: selected separations only.
rs = np.array([16, 24, 32, 48, 64, 96, 128], dtype=int)
mis = np.array([mutual_information_bits(int(r)) for r in rs])
xs = np.array([cxx(int(r)) for r in rs])

# Fit log I = const - eta log r and log Cxx = const - eta_x log r.
eta_I = -float(np.polyfit(np.log(rs), np.log(mis), 1)[0])
eta_x = -float(np.polyfit(np.log(rs), np.log(np.abs(xs)), 1)[0])

# Fisher-Hartwig prediction for the critical XX chain:
# Cxx(r) ~ A_x r^{-1/2}; therefore I(r) ~ A_x^2/(ln 2) r^{-1}.
assert abs(eta_x - 0.5) < 0.01, eta_x
assert abs(eta_I - 1.0) < 0.03, eta_I

# The product r*I(r) approaches a nonzero constant.
scaled = rs * mis
assert scaled[-1] > 0.45
assert scaled[-1] < 0.55
assert abs(scaled[-1] - scaled[-2]) < 0.01

# Exact longitudinal decay law: Czz=0 for even r and -4/(pi^2 r^2) for odd r.
for r in (17, 33, 65):
    assert abs(czz(r) + 4.0 / (math.pi**2 * r**2)) < 1e-14
for r in (16, 32, 64):
    assert abs(czz(r)) < 1e-28

print("eta_x fit =", eta_x)
print("eta_I fit =", eta_I)
print("r * I(r) at selected r:")
for r, mi, sx in zip(rs, mis, scaled):
    print(f"  r={r:3d} I={mi:.12f} rI={sx:.12f}")
print("asymptotic law: I(r) ~ kappa/r")
print("negative-log distance: -log I(r) = log r + const + o(1)")
print("PASS")
