#!/usr/bin/env python3
"""Deterministic 4D Freudenthal Regge lattice utility.

This module contains the geometric and mode-space operations required by the
canonical Regge/EH and directional Fierz-Pauli verification gates.  It is
independent of the retired monolithic verifier and makes no claim beyond finite
Euclidean Regge geometry on a periodic four-dimensional lattice.
"""
from __future__ import annotations

import itertools

import numpy as np


class FlatRegge4D:
    """Periodic 4D Freudenthal triangulation with Regge areas and deficits."""

    def __init__(self, L: int = 3):
        if L < 2:
            raise ValueError("L must be >= 2")
        self.L = int(L)
        self.d = 4
        self.pairs = list(itertools.combinations(range(5), 2))
        self.local_triangles = list(itertools.combinations(range(5), 3))
        self.opposite_pairs = [
            tuple(i for i in range(5) if i not in tri)
            for tri in self.local_triangles
        ]
        self._build()

    def vertex_id(self, coord) -> int:
        coord = np.asarray(coord, dtype=int) % self.L
        value = 0
        factor = 1
        for x in coord:
            value += int(x) * factor
            factor *= self.L
        return value

    def _build(self) -> None:
        edge_map = {}
        edge_dirs = []
        edge_mid = []
        sedges = []
        stris = []
        triangle_map = {}
        triangle_edges = []
        pairpos = {p: i for i, p in enumerate(self.pairs)}

        def canonical(a, b):
            a = np.asarray(a, int)
            b = np.asarray(b, int)
            delta = b - a
            if np.all(delta >= 0):
                start, direction = a, delta
            elif np.all(delta <= 0):
                start, direction = b, -delta
            else:
                raise RuntimeError("invalid Freudenthal edge")
            mask = sum((1 << i) for i in range(4) if direction[i])
            return (tuple((start % self.L).tolist()), mask), start, direction

        for bt in itertools.product(range(self.L), repeat=4):
            base = np.array(bt, int)
            for perm in itertools.permutations(range(4)):
                lifted = [base.copy()]
                cur = base.copy()
                for axis in perm:
                    cur = cur.copy()
                    cur[axis] += 1
                    lifted.append(cur)

                vids = [self.vertex_id(v) for v in lifted]
                local_e = np.empty(10, int)
                for pos, (i, j) in enumerate(self.pairs):
                    key, start, direction = canonical(lifted[i], lifted[j])
                    if key not in edge_map:
                        edge_map[key] = len(edge_dirs)
                        edge_dirs.append(direction.astype(float))
                        edge_mid.append(start.astype(float) + 0.5 * direction)
                    local_e[pos] = edge_map[key]

                tri_ids = []
                for tri in self.local_triangles:
                    key = tuple(sorted(vids[i] for i in tri))
                    eids = tuple(
                        sorted(
                            local_e[pairpos[tuple(sorted(p))]]
                            for p in itertools.combinations(tri, 2)
                        )
                    )
                    if key not in triangle_map:
                        triangle_map[key] = len(triangle_edges)
                        triangle_edges.append(eids)
                    tri_ids.append(triangle_map[key])

                sedges.append(local_e)
                stris.append(tri_ids)

        self.directions = np.asarray(edge_dirs)
        self.midpoints = np.asarray(edge_mid)
        self.simplex_edges = np.asarray(sedges)
        self.simplex_triangles = np.asarray(stris)
        self.triangle_edges = np.asarray(triangle_edges)
        self.background_q = np.sum(self.directions**2, axis=1)

        # The periodic Freudenthal lattice has fifteen nonzero positive binary
        # direction types.  The real Fourier mode has cosine and sine amplitudes
        # for each type, giving the canonical 30-dimensional mode space.
        self.direction_types = sorted({tuple(x.astype(int)) for x in self.directions})
        self.type_index = {x: i for i, x in enumerate(self.direction_types)}
        self.edge_type = np.array(
            [self.type_index[tuple(x.astype(int))] for x in self.directions],
            dtype=int,
        )
        if len(self.direction_types) != 15:
            raise RuntimeError(f"expected 15 edge direction types, got {len(self.direction_types)}")

    def deficits(self, q) -> np.ndarray:
        q = np.asarray(q, float)
        lq = q[self.simplex_edges]
        ns = len(lq)
        qmat = np.zeros((ns, 5, 5))
        for pos, (i, j) in enumerate(self.pairs):
            qmat[:, i, j] = qmat[:, j, i] = lq[:, pos]

        gram = np.empty((ns, 4, 4))
        for i in range(1, 5):
            for j in range(1, 5):
                gram[:, i - 1, j - 1] = (
                    qmat[:, 0, i] + qmat[:, 0, j] - qmat[:, i, j]
                ) / 2.0

        inv = np.linalg.inv(gram)
        bary = np.zeros((ns, 5, 5))
        bary[:, 1:, 1:] = inv
        sums = inv.sum(axis=2)
        bary[:, 0, 1:] = -sums
        bary[:, 1:, 0] = -sums
        bary[:, 0, 0] = inv.sum(axis=(1, 2))

        angles = np.empty((ns, 10))
        for idx, (a, b) in enumerate(self.opposite_pairs):
            cosang = -bary[:, a, b] / np.sqrt(
                bary[:, a, a] * bary[:, b, b]
            )
            angles[:, idx] = np.arccos(np.clip(cosang, -1.0, 1.0))

        angle_sum = np.zeros(len(self.triangle_edges))
        np.add.at(
            angle_sum,
            self.simplex_triangles.ravel(),
            angles.ravel(),
        )
        return 2.0 * np.pi - angle_sum

    def areas(self, q) -> np.ndarray:
        qe = np.asarray(q, float)[self.triangle_edges]
        qa, qb, qc = qe[:, 0], qe[:, 1], qe[:, 2]
        scalar = 0.5 * (qa + qb - qc)
        radicand = qa * qb - scalar**2
        if np.any(radicand < -1e-12):
            raise ValueError("triangle lost Euclidean nondegeneracy")
        return 0.5 * np.sqrt(np.maximum(radicand, 0.0))

    def action(self, q) -> float:
        """Return the unnormalised Euclidean Regge sum sum_h A_h delta_h."""
        return float(np.sum(self.areas(q) * self.deficits(q)))

    def q_from_mode(self, coeff, k) -> np.ndarray:
        """Map 15 cosine + 15 sine edge-type coefficients to squared lengths."""
        coeff = np.asarray(coeff, float)
        if coeff.shape != (30,):
            raise ValueError("mode coefficient vector must have length 30")
        k = np.asarray(k, float)
        phase = self.midpoints @ k
        return (
            self.background_q
            + coeff[:15][self.edge_type] * np.cos(phase)
            + coeff[15:][self.edge_type] * np.sin(phase)
        )

    def hessian(self, k, step: float = 2e-4) -> np.ndarray:
        """Central finite-difference Hessian of the Regge action in mode space.

        This is the mode-space method used by the previously successful
        directional Regge calculation.  It was lost when the monolithic verifier
        was split; keeping it here restores the same finite calculation without
        restoring the retired monolith.
        """
        if not np.isfinite(step) or step <= 0:
            raise ValueError("step must be finite and positive")
        n = 30
        z = np.zeros(n)
        f0 = self.action(self.q_from_mode(z, k))
        H = np.zeros((n, n))
        cache: dict[tuple[float, ...], float] = {}

        def f(x):
            key = tuple(np.round(x, 12))
            if key not in cache:
                cache[key] = self.action(self.q_from_mode(x, k))
            return cache[key]

        for i in range(n):
            ei = np.zeros(n)
            ei[i] = step
            H[i, i] = (f(ei) - 2.0 * f0 + f(-ei)) / step**2
        for i in range(n):
            ei = np.zeros(n)
            ei[i] = step
            for j in range(i + 1, n):
                ej = np.zeros(n)
                ej[j] = step
                H[i, j] = H[j, i] = (
                    f(ei + ej)
                    - f(ei - ej)
                    - f(-ei + ej)
                    + f(-ei - ej)
                ) / (4.0 * step**2)
        return 0.5 * (H + H.T)

    def gauge_basis(self, k) -> np.ndarray:
        """Orthonormal real Fourier basis of vertex-displacement gauge modes."""
        k = np.asarray(k, float)
        vecs = []
        for mu in range(4):
            vc = np.zeros(30)
            vs = np.zeros(30)
            for a, nt in enumerate(self.direction_types):
                n = np.asarray(nt, float)
                factor = 4.0 * n[mu] * np.sin(0.5 * float(k @ n))
                vc[15 + a] = -factor
                vs[a] = factor
            vecs.extend([vc, vs])
        G = np.column_stack(vecs)
        # SVD handles any accidental degeneracy at special lattice momenta and
        # returns only the actual gauge subspace rather than eight assumed modes.
        U, s, _ = np.linalg.svd(G, full_matrices=False)
        tol = 1e-12 * max(float(s[0]) if len(s) else 0.0, 1.0)
        rank = int(np.sum(s > tol))
        return U[:, :rank]
