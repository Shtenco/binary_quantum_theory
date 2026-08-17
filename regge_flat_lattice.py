#!/usr/bin/env python3
"""Minimal deterministic 4D Freudenthal Regge lattice utility.

This module contains only the geometric data required by the retained
Regge-to-Einstein-Hilbert continuum bridge.  It is intentionally independent of
the deleted monolithic BCQG verifier and makes no claim beyond finite Euclidean
Regge geometry on a periodic four-dimensional lattice.
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
