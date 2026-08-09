#!/usr/bin/env python3
"""Check four linked geometric invariants of one 4D-embedded tetrahedral cell."""

from __future__ import annotations

import itertools
import json
import math


Vector = tuple[float, float, float, float]
Matrix = tuple[tuple[float, ...], ...]
ZERO: Matrix = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))


def sub(a: Vector, b: Vector) -> Vector:
    return tuple(a[i] - b[i] for i in range(4))  # type: ignore[return-value]


def wedge(a: Vector, b: Vector, scale: float = 0.5) -> Matrix:
    return tuple(tuple(scale * (a[i] * b[j] - a[j] * b[i]) for j in range(4))
                 for i in range(4))


def add(values: tuple[Matrix, ...]) -> Matrix:
    return tuple(tuple(sum(value[i][j] for value in values) for j in range(4))
                 for i in range(4))


def scale(matrix: Matrix, factor: float) -> Matrix:
    return tuple(tuple(factor * value for value in row) for row in matrix)


def epsilon(indices: tuple[int, int, int, int]) -> int:
    if len(set(indices)) < 4:
        return 0
    inversions = sum(indices[i] > indices[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inversions % 2 else 1


def plucker(a: Matrix, b: Matrix) -> float:
    return sum(epsilon((i, j, k, l)) * a[i][j] * b[k][l]
               for i, j, k, l in itertools.product(range(4), repeat=4))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4))
                 for i in range(4))


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(4)) for i in range(4))


def max_abs(a: Matrix) -> float:
    return max(abs(value) for row in a for value in row)


def rotation(i: int, j: int, angle: float) -> Matrix:
    out = [list(row) for row in ZERO]
    for k in range(4):
        out[k][k] = 1.0
    c, s = math.cos(angle), math.sin(angle)
    out[i][i] = out[j][j] = c
    out[i][j], out[j][i] = -s, s
    return tuple(tuple(row) for row in out)


def determinant3(gram: tuple[tuple[float, ...], ...]) -> float:
    a, b, c = gram
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def main() -> int:
    vertices: tuple[Vector, ...] = (
        (0.0, 0.0, 0.0, 0.0), (1.0, 0.0, 0.0, 0.0),
        (0.2, 1.1, 0.0, 0.0), (0.1, 0.3, 0.9, 0.0),
    )
    faces = []
    for omitted in range(4):
        ids = [index for index in range(4) if index != omitted]
        face = wedge(sub(vertices[ids[1]], vertices[ids[0]]),
                     sub(vertices[ids[2]], vertices[ids[0]]))
        faces.append(scale(face, -1.0 if omitted % 2 else 1.0))
    face_tuple = tuple(faces)
    closure_error = max_abs(add(face_tuple))
    simplicity_error = max(abs(plucker(face, face)) for face in face_tuple)
    cross_simplicity_error = max(abs(plucker(face_tuple[i], face_tuple[j]))
                                 for i in range(4) for j in range(i + 1, 4))

    edges = tuple(sub(vertices[i], vertices[0]) for i in (1, 2, 3))
    gram = tuple(tuple(sum(edges[i][k] * edges[j][k] for k in range(4))
                       for j in range(3)) for i in range(3))
    volume_squared = determinant3(gram) / 36.0

    transform = matmul(rotation(0, 3, 0.43), rotation(1, 2, -0.31))
    rotated = tuple(matmul(matmul(transform, face), transpose(transform)) for face in face_tuple)
    rotated_closure_error = max_abs(add(rotated))
    rotated_cross_error = max(abs(plucker(rotated[i], rotated[j]))
                              for i in range(4) for j in range(i + 1, 4))

    broken = add((wedge((1, 0, 0, 0), (0, 1, 0, 0), 1.0),
                  wedge((0, 0, 1, 0), (0, 0, 0, 1), 1.0)))
    broken_plucker = abs(plucker(broken, broken))
    checks = {
        "closure": closure_error < 1e-12,
        "diagonal_simplicity": simplicity_error < 1e-12,
        "cross_simplicity": cross_simplicity_error < 1e-12,
        "nondegenerate_volume": volume_squared > 1e-6,
        "frame_covariance": rotated_closure_error < 1e-12 and rotated_cross_error < 1e-12,
        "nonsimple_control_rejected": broken_plucker > 1.0,
    }
    result = {
        "checks": checks,
        "passed": all(checks.values()),
        "closure_error": closure_error,
        "simplicity_error": simplicity_error,
        "cross_simplicity_error": cross_simplicity_error,
        "tetrahedron_volume_squared": volume_squared,
        "rotated_closure_error": rotated_closure_error,
        "rotated_cross_simplicity_error": rotated_cross_error,
        "nonsimple_control_plucker": broken_plucker,
        "scope": "one nondegenerate tetrahedral cell; finite precursor only",
    }
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
