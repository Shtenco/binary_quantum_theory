from __future__ import annotations

import math
import numpy as np

T = 1.5  # free-fermion hopping inherited from the reduced BQG chain


def single_particle_spectrum(k: float, m: float) -> tuple[float, float]:
    """Two-band spectrum of the staggered-mass deformation."""
    e = math.sqrt((2.0 * m) ** 2 + 9.0 * math.cos(k) ** 2)
    return -e, e


def correlation_length(m: float) -> float:
    """Exact branch-point correlation length in lattice-site units."""
    if m == 0:
        return math.inf
    return 1.0 / math.asinh(2.0 * abs(m) / 3.0)


def finite_chain_ground_correlation(L: int, m: float) -> tuple[np.ndarray, np.ndarray]:
    """Open-chain one-body spectrum and ground-state correlation matrix."""
    h = np.zeros((L, L), dtype=float)
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -T
    # In the rotated XX frame, H_m = m sum (-1)^j Z_j.
    # With Z_j = 1 - 2 n_j, this gives onsite potential -2m(-1)^j.
    for i in range(L):
        h[i, i] += -2.0 * m * ((-1) ** i)
    vals, vecs = np.linalg.eigh(h)
    occ = vals < 0.0
    C = vecs[:, occ] @ vecs[:, occ].T
    return vals, C


def spin_correlators(C: np.ndarray, i: int, j: int) -> tuple[float, float, float, float]:
    """Return <Zi>, <Zj>, <ZiZj>, <XiXj> for the number-conserving free-fermion ground state."""
    zi = 1.0 - 2.0 * C[i, i]
    zj = 1.0 - 2.0 * C[j, j]
    zz = zi * zj - 4.0 * C[i, j] ** 2

    # Jordan-Wigner string is essential. For i<j,
    # <Xi Xj> is a determinant of the Majorana contraction block.
    G = np.eye(C.shape[0]) - 2.0 * C
    block = G[i:j, i + 1 : j + 1]
    xx = float(np.linalg.det(block))
    return zi, zj, zz, xx


def entropy_bits(p: np.ndarray) -> float:
    q = p[p > 1e-15]
    return -float(np.sum(q * np.log2(q)))


def mutual_information_bits(C: np.ndarray, i: int, j: int) -> float:
    zi, zj, zz, xx = spin_correlators(C, i, j)
    rho = np.zeros((4, 4), dtype=float)
    rho[0, 0] = (1 + zi + zj + zz) / 4
    rho[1, 1] = (1 + zi - zj - zz) / 4
    rho[2, 2] = (1 - zi + zj - zz) / 4
    rho[3, 3] = (1 - zi - zj + zz) / 4
    rho[1, 2] = rho[2, 1] = xx / 2
    ev = np.linalg.eigvalsh(rho)
    pa = np.array([(1 + zi) / 2, (1 - zi) / 2])
    pb = np.array([(1 + zj) / 2, (1 - zj) / 2])
    return entropy_bits(pa) + entropy_bits(pb) - entropy_bits(ev)


# Exact analytic checks.
for m in (0.1, 0.2, 0.5):
    em, ep = single_particle_spectrum(math.pi / 2, m)
    assert abs(ep - 2.0 * m) < 1e-14
    assert abs(em + 2.0 * m) < 1e-14
    assert correlation_length(m) > 0

# Numerical independent check of the asymptotic law in a weakly gapped phase.
m = 0.2
L = 500
vals, C = finite_chain_ground_correlation(L, m)
expected_gap = 2.0 * m
observed_gap = float(np.min(np.abs(vals)))
assert abs(observed_gap - expected_gap) < 2e-3

xi = correlation_length(m)
i0 = 200
rs = np.arange(20, 81, 4)
xx = []
mi = []
for r in rs:
    _, _, _, x = spin_correlators(C, i0, i0 + int(r))
    xx.append(abs(x))
    mi.append(mutual_information_bits(C, i0, i0 + int(r)))
xx = np.array(xx)
mi = np.array(mi)

# Expected asymptotics:
# Cxx(r) ~ A r^{-1/2} exp(-r/xi)
# I(r)   ~ B r^{-1}   exp(-2r/xi)
fit_x = np.polyfit(rs, np.log(xx) + 0.5 * np.log(rs), 1)
xi_x = -1.0 / float(fit_x[0])
fit_i = np.polyfit(rs, np.log(mi) + np.log(rs), 1)
xi_i = -1.0 / float(fit_i[0])

assert abs(xi_x / xi - 1.0) < 0.03
assert abs(xi_i / (xi / 2.0) - 1.0) < 0.04

# Universal scalar distance no-go:
# critical phase: I_c(r) ~ kappa/r -> linear d requires f(x) ~ const/x;
# gapped phase: I_g(r) ~ B r^{-1} exp(-2r/xi) -> linear d requires
# f(x) ~ const*log(1/x). These x->0 asymptotics are incompatible.
print("staggered-mass deformation")
print("single-particle gap =", expected_gap)
print("exact xi =", xi)
print("fitted xi from Cxx =", xi_x)
print("fitted xi from MI =", xi_i, "expected", xi / 2.0)
print("critical: I(r) ~ kappa/r")
print("gapped:   I(r) ~ B*r^{-1}*exp(-2r/xi)")
print("NO-GO: no phase-independent scalar d=f(I) is asymptotically linear in both phases")
print("PASS")
