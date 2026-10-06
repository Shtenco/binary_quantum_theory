from __future__ import annotations

import math
import random
import numpy as np
import networkx as nx
from scipy.special import i0e, i1e

GSTAR = 8.0 / (math.pi**2 + 4.0)


def spectral_curve(G, taus, g=GSTAR):
    L = nx.laplacian_matrix(G).astype(float).toarray() * g
    lam = np.linalg.eigvalsh(L)
    lam = np.clip(lam, 0.0, None)
    P = []
    ds = []
    for tau in taus:
        w = np.exp(-tau * lam)
        z = w.sum()
        P.append(z / len(lam))
        ds.append(2.0 * tau * float((lam * w).sum() / z))
    return np.asarray(P), np.asarray(ds), lam


def plateau_detect(taus, ds, min_decades=0.30, slope_tol=0.12,
                   relspread_tol=0.15, min_ds=0.50):
    x = np.log(taus)
    slope = np.gradient(ds, x)
    good = (np.abs(slope) < slope_tol) & (ds > min_ds)
    best = None
    i = 0
    while i < len(ds):
        if not good[i]:
            i += 1
            continue
        j = i
        while j + 1 < len(ds) and good[j + 1]:
            j += 1
        if j - i >= 5:
            decades = math.log10(float(taus[j] / taus[i]))
            vals = ds[i:j + 1]
            med = float(np.median(vals))
            relspread = float((np.percentile(vals, 90) - np.percentile(vals, 10)) / med)
            if decades >= min_decades and relspread < relspread_tol:
                score = decades * (1.0 - relspread)
                if best is None or score > best['score']:
                    best = dict(i=i, j=j, decades=decades, value=med,
                                relspread=relspread, score=score)
        i = j + 1
    return best


def weighted_choice(rng, items, weights):
    return rng.choices(items, weights=weights, k=1)[0]


def bqg_local_gluing_graph(n, seed, p_two=0.5, max_degree=4, radius=2):
    """Coordinate-free candidate gluing rule.

    Ingredients only:
      * four-valent capacity inherited from the four-spin physical node;
      * local free-valence preference;
      * local loop closure within graph distance <= radius;
      * no coordinate labels, target dimension, spectral feedback or ds fitting.

    This is a CANDIDATE surrogate rule, not fundamental BQG dynamics.
    """
    rng = random.Random(seed)
    G = nx.Graph()
    G.add_edge(0, 1)

    for v in range(2, n):
        G.add_node(v)
        eligible = [u for u in range(v) if G.degree[u] < max_degree]
        if not eligible:
            raise RuntimeError('no unsaturated node')

        free = [max_degree - G.degree[u] for u in eligible]
        a = weighted_choice(rng, eligible, free)
        G.add_edge(v, a)

        if rng.random() < p_two:
            lengths = nx.single_source_shortest_path_length(G, a, cutoff=radius)
            cand = [u for u, d in lengths.items()
                    if u != v and u != a and G.degree[u] < max_degree
                    and not G.has_edge(v, u)]
            if not cand:
                cand = [u for u in range(v)
                        if G.degree[u] < max_degree and not G.has_edge(v, u)]
            if cand:
                weights = []
                for u in cand:
                    d = lengths.get(u, radius + 1)
                    common = len(list(nx.common_neighbors(G, a, u)))
                    weights.append((max_degree - G.degree[u]) * (1 + common) / max(1, d))
                b = weighted_choice(rng, cand, weights)
                G.add_edge(v, b)

    return G


def random_stub_null(n, seed, p_two=0.5, max_degree=4):
    """Same valence budget and growth rate, but no local closure preference."""
    rng = random.Random(seed)
    G = nx.Graph()
    G.add_edge(0, 1)

    for v in range(2, n):
        G.add_node(v)
        eligible = [u for u in range(v) if G.degree[u] < max_degree]
        if not eligible:
            raise RuntimeError('no unsaturated node')
        a = weighted_choice(rng, eligible, [max_degree - G.degree[u] for u in eligible])
        G.add_edge(v, a)

        if rng.random() < p_two:
            cand = [u for u in range(v)
                    if G.degree[u] < max_degree and not G.has_edge(v, u)]
            if cand:
                b = weighted_choice(rng, cand, [max_degree - G.degree[u] for u in cand])
                G.add_edge(v, b)

    return G


def exact_ds_hypercubic(D, u):
    x = 2.0 * u
    return 2.0 * D * x * (1.0 - i1e(x) / i0e(x))


def ensemble_stats(gen, n, seeds, taus):
    vals = []
    gaps = []
    trans = []
    deg = []
    for seed in seeds:
        G = gen(n, seed)
        _, ds, lam = spectral_curve(G, taus)
        p = plateau_detect(taus, ds)
        vals.append(np.nan if p is None else p['value'])
        gaps.append(lam[1])
        trans.append(nx.transitivity(G))
        deg.append(np.mean([d for _, d in G.degree()]))

    vals = np.asarray(vals, float)
    return {
        'valid': int(np.isfinite(vals).sum()),
        'mean': float(np.nanmean(vals)) if np.isfinite(vals).any() else math.nan,
        'std': float(np.nanstd(vals)) if np.isfinite(vals).any() else math.nan,
        'gap': float(np.mean(gaps)),
        'transitivity': float(np.mean(trans)),
        'degree': float(np.mean(deg)),
    }


taus = np.logspace(-2, 3, 280)

# Calibration: detector recognizes known manifold-like dimensions.
cycle = nx.cycle_graph(400)
_, ds1, _ = spectral_curve(cycle, taus)
p1 = plateau_detect(taus, ds1)
assert p1 is not None and abs(p1['value'] - 1.0) < 0.05

grid = nx.convert_node_labels_to_integers(nx.grid_2d_graph(22, 22, periodic=True))
_, ds2, _ = spectral_curve(grid, taus)
p2 = plateau_detect(taus, ds2)
assert p2 is not None and abs(p2['value'] - 2.0) < 0.10

for D in (1, 2, 3):
    assert abs(exact_ds_hypercubic(D, 100.0) - D) < 0.01

# Size scaling of the coordinate-free BQG-inspired ensemble.
for n in (150, 300, 500):
    s = ensemble_stats(bqg_local_gluing_graph, n, range(6), taus)
    print('BQG', n, s)
    if n >= 300:
        assert s['valid'] >= 5
        assert 1.15 < s['mean'] < 1.35

# Matched null: same valence budget and second-edge rate, but globally random pairing.
null = ensemble_stats(random_stub_null, 300, range(12), taus)
print('NULL', null)
assert null['valid'] <= 1

# Robustness scan. This is not a fit to dimension: all values are accepted a priori.
for p_two in (0.25, 0.40, 0.50, 0.60, 0.75):
    def gen(n, seed, p=p_two):
        return bqg_local_gluing_graph(n, seed, p_two=p)
    s = ensemble_stats(gen, 250, range(6), taus)
    print('P2', p_two, s)
    if s['valid'] >= 3:
        assert s['mean'] < 1.6

print('NO-GO: valence-4 + local loop closure does not generate a robust ds~3 plateau')
print('PASS')
