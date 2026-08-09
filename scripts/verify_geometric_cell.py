#!/usr/bin/env python3
"""Check linked geometric invariants of one 4D-embedded tetrahedral cell.

The positive control is deliberately edge-generated, so its simplicity
relations are reconstruction identities rather than evidence that a microscopic
dynamics has generated simplicity. Two adversarial controls separate closure,
diagonal simplicity and cross-simplicity logically:

* four individually simple bivectors with exact closure but violated
  cross-simplicity;
* a closure-preserving set containing a nonsimple bivector, hence violating
  diagonal simplicity.
"""

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
    inversions = sum(indices[i] > indices[j]
                     for i in range(4) for j in range(i + 1, 4))
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


def simplicity_diagnostics(faces: tuple[Matrix, ...]) -> tuple[float, float, float]:
    closure = max_abs(add(faces))
    diagonal = max(abs(plucker(face, face)) for face in faces)
    cross = max(abs(plucker(faces[i], faces[j]))
                for i in range(len(faces)) for j in range(i + 1, len(faces)))
    return closure, diagonal, cross


def main() -> int:
    # Positive reconstruction control: one nondegenerate tetrahedron embedded in
    # R^4. Since every face is explicitly a wedge of edge vectors, simplicity
    # here is an exact geometric reconstruction identity, not an emergence test.
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
    closure_error, simplicity_error, cross_simplicity_error = simplicity_diagnostics(face_tuple)

    edges = tuple(sub(vertices[i], vertices[0]) for i in (1, 2, 3))
    gram = tuple(tuple(sum(edges[i][k] * edges[j][k] for k in range(4))
                       for j in range(3)) for i in range(3))
    volume_squared = determinant3(gram) / 36.0

    transform = matmul(rotation(0, 3, 0.43), rotation(1, 2, -0.31))
    rotated = tuple(matmul(matmul(transform, face), transpose(transform)) for face in face_tuple)
    rotated_closure_error, rotated_diagonal_error, rotated_cross_error = simplicity_diagnostics(rotated)

    # Adversarial control A: every bivector is simple and the four bivectors
    # close exactly, but the set does not share a common tetrahedral 3-plane.
    # Therefore cross-simplicity must fail while closure and diagonal simplicity
    # still pass.
    e0: Vector = (1.0, 0.0, 0.0, 0.0)
    e1: Vector = (0.0, 1.0, 0.0, 0.0)
    e2: Vector = (0.0, 0.0, 1.0, 0.0)
    e3: Vector = (0.0, 0.0, 0.0, 1.0)
    a = wedge(e0, e1, 1.0)
    b = wedge(e2, e3, 1.0)
    cross_bad = (a, b, scale(a, -1.0), scale(b, -1.0))
    cb_closure, cb_diagonal, cb_cross = simplicity_diagnostics(cross_bad)

    # Adversarial control B: closure is exact but B=a+b is nonsimple because
    # B wedge B != 0. This separates diagonal simplicity from closure.
    nonsimple = add((a, b))
    diagonal_bad = (nonsimple, scale(nonsimple, -1.0), a, scale(a, -1.0))
    db_closure, db_diagonal, db_cross = simplicity_diagnostics(diagonal_bad)

    checks = {
        "positive_closure": closure_error < 1e-12,
        "positive_diagonal_simplicity": simplicity_error < 1e-12,
        "positive_cross_simplicity": cross_simplicity_error < 1e-12,
        "positive_nondegenerate_volume": volume_squared > 1e-6,
        "positive_frame_covariance": (
            rotated_closure_error < 1e-12
            and rotated_diagonal_error < 1e-12
            and rotated_cross_error < 1e-12
        ),
        "cross_bad_still_closes": cb_closure < 1e-12,
        "cross_bad_each_face_simple": cb_diagonal < 1e-12,
        "cross_bad_rejected": cb_cross > 1.0,
        "diagonal_bad_still_closes": db_closure < 1e-12,
        "diagonal_bad_rejected": db_diagonal > 1.0,
    }
    result = {
        "checks": checks,
        "passed": all(checks.values()),
        "positive": {
            "closure_error": closure_error,
            "diagonal_simplicity_error": simplicity_error,
            "cross_simplicity_error": cross_simplicity_error,
            "tetrahedron_volume_squared": volume_squared,
            "rotated_closure_error": rotated_closure_error,
            "rotated_diagonal_simplicity_error": rotated_diagonal_error,
            "rotated_cross_simplicity_error": rotated_cross_error,
        },
        "closure_preserving_cross_simplicity_negative_control": {
            "closure_error": cb_closure,
            "diagonal_simplicity_error": cb_diagonal,
            "cross_simplicity_error": cb_cross,
        },
        "closure_preserving_diagonal_simplicity_negative_control": {
            "closure_error": db_closure,
            "diagonal_simplicity_error": db_diagonal,
            "cross_simplicity_error": db_cross,
        },
        "scope": (
            "finite algebraic/reconstruction gate. The positive bivectors are edge-generated; "
            "this does not show that simplicity emerges dynamically from the microscopic rule."
        ),
    }
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
