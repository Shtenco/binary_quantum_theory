from __future__ import annotations

import math
import numpy as np
from scipy.special import i0e, i1e


def spectral_dimension_hypercubic(D: int, g: float, tau: float) -> float:
    """Exact infinite D-dimensional hypercubic QFI-weighted result."""
    x = 2.0 * g * tau
    ratio = i1e(x) / i0e(x)
    return 4.0 * D * g * tau * (1.0 - ratio)


def return_probability_hypercubic(D: int, g: float, tau: float) -> float:
    # Stable form: exp(-2g tau) I0(2g tau) = i0e(2g tau)
    return float(i0e(2.0 * g * tau) ** D)


# Exact critical QFI conductance from previous gate.
g_critical = 8.0 / (math.pi**2 + 4.0)
# Representative gapped QFI conductance (m=1) from the local-response gate.
g_gapped = 0.99942 / 4.0

# Phase robustness: curves collapse exactly when expressed in u=g*tau.
for D in (1, 2, 3):
    for u in (10.0, 100.0):
        ds_c = spectral_dimension_hypercubic(D, g_critical, u / g_critical)
        ds_g = spectral_dimension_hypercubic(D, g_gapped, u / g_gapped)
        assert abs(ds_c - ds_g) < 1e-12
        target_tol = 0.05 if u == 10.0 else 0.01
        assert abs(ds_c - D) < target_tol

# Direct asymptotic calibration.
for D in (1, 2, 3):
    ds = spectral_dimension_hypercubic(D, g_critical, 100.0 / g_critical)
    assert abs(ds - D) < 0.01

# Non-manifold branching reference: infinite 3-regular Bethe lattice has
# spectral bottom lambda0 = 3 - 2 sqrt(2) > 0. With
# P(tau) ~ exp(-g lambda0 tau) tau^{-3/2}, one gets
# d_s(tau) ~ 2 g lambda0 tau + 3, so there is no finite IR plateau.
lambda0_bethe = 3.0 - 2.0 * math.sqrt(2.0)
for tau in (10.0, 50.0, 100.0):
    ds_tree = 2.0 * g_critical * lambda0_bethe * tau + 3.0
    assert ds_tree > 3.0

print('critical g =', g_critical)
print('gapped g =', g_gapped)
for D in (1, 2, 3):
    for u in (10.0, 100.0):
        ds = spectral_dimension_hypercubic(D, g_critical, u / g_critical)
        print(f'D={D} u={u:g} ds={ds:.12f}')
print('Bethe lambda0 =', lambda0_bethe)
print('PASS')
