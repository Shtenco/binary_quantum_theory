#!/usr/bin/env python3
"""
Finite-size Monte Carlo demonstration of a continuous critical phase
in the reduced two-polarization binary TT sector.

Model:
    Z_L(beta) = sum_{s^+,s^x=+-1}
                exp[ beta sum_{<xy>,a=+,x} s_x^a s_y^a ]

The two copies represent the two physical TT polarizations after
metric compatibility and gauge reduction. This script does NOT prove
that the original binary edge-Regge sum flows to this fixed point.
"""
import math
import numpy as np
import pandas as pd
from numba import njit

@njit
def make_neighbors_coords(L):
    N = L**4
    neigh = np.empty((N, 8), np.int64)
    coords = np.empty((N, 4), np.int64)
    strides = np.array([1, L, L*L, L*L*L], dtype=np.int64)
    for idx in range(N):
        for mu in range(4):
            st = strides[mu]
            c = (idx // st) % L
            coords[idx, mu] = c
            neigh[idx, 2*mu] = idx + st if c < L-1 else idx - (L-1)*st
            neigh[idx, 2*mu+1] = idx - st if c > 0 else idx + (L-1)*st
    return neigh, coords

@njit
def wolff(spins, neigh, beta, stack, cluster, marks, mark_id):
    N = spins.size
    p_add = 1.0 - math.exp(-2.0*beta)
    seed = np.random.randint(N)
    target = spins[seed]
    stack[0] = seed
    top = 1
    marks[seed] = mark_id
    size = 0
    while top:
        top -= 1
        site = stack[top]
        cluster[size] = site
        size += 1
        for a in range(8):
            nb = neigh[site, a]
            if marks[nb] != mark_id and spins[nb] == target:
                if np.random.random() < p_add:
                    marks[nb] = mark_id
                    stack[top] = nb
                    top += 1
    for i in range(size):
        spins[cluster[i]] = -spins[cluster[i]]
    return size

@njit
def measure(spins, coords, L, cos_table, sin_table):
    N = spins.size
    M = 0.0
    for i in range(N):
        M += spins[i]
    Sk = 0.0
    for mu in range(4):
        re = 0.0
        im = 0.0
        for i in range(N):
            c = coords[i, mu]
            re += spins[i] * cos_table[c]
            im += spins[i] * sin_table[c]
        Sk += (re*re + im*im) / N
    Sk /= 4.0
    m = M / N
    return m, M*M/N, Sk

@njit
def simulate(L, beta, n_therm, n_meas, clusters_per_measurement, seed):
    np.random.seed(seed)
    neigh, coords = make_neighbors_coords(L)
    N = L**4
    s1 = np.where(np.random.random(N) < 0.5, -1, 1).astype(np.int8)
    s2 = np.where(np.random.random(N) < 0.5, -1, 1).astype(np.int8)
    stack = np.empty(N, np.int64)
    cluster = np.empty(N, np.int64)
    mark1 = np.zeros(N, np.int64)
    mark2 = np.zeros(N, np.int64)
    id1 = 1
    id2 = 1
    cos_table = np.empty(L)
    sin_table = np.empty(L)
    for c in range(L):
        angle = 2.0*math.pi*c/L
        cos_table[c] = math.cos(angle)
        sin_table[c] = math.sin(angle)

    for _ in range(n_therm):
        wolff(s1, neigh, beta, stack, cluster, mark1, id1); id1 += 1
        wolff(s2, neigh, beta, stack, cluster, mark2, id2); id2 += 1

    m2_sum = m4_sum = abs_sum = S0_sum = Sk_sum = 0.0
    for _ in range(n_meas):
        for _ in range(clusters_per_measurement):
            wolff(s1, neigh, beta, stack, cluster, mark1, id1); id1 += 1
            wolff(s2, neigh, beta, stack, cluster, mark2, id2); id2 += 1
        a, A0, Ak = measure(s1, coords, L, cos_table, sin_table)
        b, B0, Bk = measure(s2, coords, L, cos_table, sin_table)
        m2_sum += 0.5*(a*a + b*b)
        m4_sum += 0.5*(a**4 + b**4)
        abs_sum += 0.5*(abs(a) + abs(b))
        S0_sum += 0.5*(A0 + B0)
        Sk_sum += 0.5*(Ak + Bk)

    inv = 1.0/n_meas
    m2 = m2_sum*inv
    m4 = m4_sum*inv
    mean_abs = abs_sum*inv
    S0 = S0_sum*inv
    Sk = Sk_sum*inv
    binder = 1.0 - m4/(3.0*m2*m2)
    susceptibility = N*(m2 - mean_abs*mean_abs)
    xi = 0.5/math.sin(math.pi/L)*math.sqrt(max(S0/Sk - 1.0, 0.0))
    return binder, susceptibility, xi/L, m2

def main():
    betas = [0.14930, 0.14950, 0.14965, 0.14980, 0.15000]
    rows = []
    for L in [6, 8, 10, 12]:
        for j, beta in enumerate(betas):
            result = simulate(
                L, beta,
                n_therm=1600,
                n_meas=6500 if L <= 10 else 5000,
                clusters_per_measurement=2,
                seed=270000 + 100*L + j,
            )
            rows.append({
                "L": L,
                "beta": beta,
                "Binder_U": result[0],
                "susceptibility": result[1],
                "xi_over_L": result[2],
                "mean_m2": result[3],
            })
    frame = pd.DataFrame(rows)
    frame.to_csv("bcqg_critical_scan.csv", index=False)
    print(frame.to_string(index=False))

if __name__ == "__main__":
    main()
