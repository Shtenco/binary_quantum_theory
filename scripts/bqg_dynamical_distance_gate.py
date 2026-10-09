#!/usr/bin/env python3
"""Regression gate for the BQG dynamical graph-distance theorem."""
from __future__ import annotations

from collections import deque
import numpy as np


def distances(n: int, edges):
    adj = [[] for _ in range(n)]
    for i, j, _ in edges:
        adj[i].append(j)
        adj[j].append(i)
    D = np.full((n, n), 10**9, dtype=int)
    for s in range(n):
        D[s, s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if D[s, v] == 10**9:
                    D[s, v] = D[s, u] + 1
                    q.append(v)
    return D


def hamiltonian(n: int, edges, diagonal):
    H = np.diag(np.asarray(diagonal, dtype=float))
    for i, j, g in edges:
        assert g > 0
        H[i, j] = -g
        H[j, i] = -g
    return H


def first_nonzero_power(H, i: int, j: int, tol: float = 1e-11):
    P = np.eye(H.shape[0])
    for k in range(H.shape[0] + 1):
        if abs(P[i, j]) > tol:
            return k
        P = P @ H
    return None


def shortest_path_weight_sum(n: int, edges, i: int, j: int, d: int):
    adj = [[] for _ in range(n)]
    for a, b, g in edges:
        adj[a].append((b, g))
        adj[b].append((a, g))

    total = 0.0

    def walk(u, depth, visited, prod):
        nonlocal total
        if depth == d:
            if u == j:
                total += prod
            return
        for v, g in adj[u]:
            if v in visited:
                continue
            visited.add(v)
            walk(v, depth + 1, visited, prod * g)
            visited.remove(v)

    walk(i, 0, {i}, 1.0)
    return total


def run():
    rng = np.random.default_rng(0)
    total_graphs = 0
    total_pairs = 0

    for N in (6, 8, 10):
        for _ in range(10):
            edges = []
            present = set()

            # Connected random tree backbone.
            for v in range(1, N):
                u = int(rng.integers(v))
                g = float(rng.uniform(0.1, 1.0))
                edges.append((u, v, g))
                present.add(tuple(sorted((u, v))))

            # Extra local/nonlocal edges.
            for i in range(N):
                for j in range(i + 1, N):
                    if (i, j) not in present and rng.random() < 0.12:
                        edges.append((i, j, float(rng.uniform(0.1, 1.0))))

            diagonal = rng.normal(0.0, 2.0, N)
            H = hamiltonian(N, edges, diagonal)
            D = distances(N, edges)

            for i in range(N):
                for j in range(N):
                    d = int(D[i, j])
                    k = first_nonzero_power(H, i, j)
                    assert k == d, (N, i, j, k, d)

                    if i != j:
                        P = np.linalg.matrix_power(H, d)
                        S = shortest_path_weight_sum(N, edges, i, j, d)
                        expected = ((-1) ** d) * S
                        assert abs(P[i, j] - expected) < 1e-8, (
                            N, i, j, d, P[i, j], expected
                        )
                    total_pairs += 1
            total_graphs += 1

    print(f"graphs={total_graphs}")
    print(f"ordered_pairs={total_pairs}")
    print("DYNAMIC_DISTANCE == GRAPH_DISTANCE")
    print("SHORTEST_PATH_WEIGHT COEFFICIENT IDENTITY PASS")
    print("PASS")


if __name__ == "__main__":
    run()
