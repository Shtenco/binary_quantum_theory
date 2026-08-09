#!/usr/bin/env python3
"""Finite off-shell SU(2) frame-gauge/Ward check on one plaquette."""

from __future__ import annotations

import json
import math


Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]
I2: Matrix = ((1 + 0j, 0j), (0j, 1 + 0j))


def mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))  # type: ignore[return-value]


def dagger(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i].conjugate() for j in range(2))
                 for i in range(2))  # type: ignore[return-value]


def su2(axis: tuple[float, float, float], angle: float) -> Matrix:
    norm = math.sqrt(sum(x * x for x in axis))
    x, y, z = (value / norm for value in axis)
    c, s = math.cos(angle / 2), math.sin(angle / 2)
    return ((c - 1j * z * s, (-1j * x - y) * s),
            ((-1j * x + y) * s, c + 1j * z * s))


def plaquette(links: tuple[Matrix, Matrix, Matrix, Matrix]) -> Matrix:
    out = I2
    for link in links:
        out = mul(out, link)
    return out


def action(loop: Matrix) -> float:
    return 1.0 - 0.5 * (loop[0][0] + loop[1][1]).real


def bivector(axis: tuple[float, float, float]) -> Matrix:
    """Anti-Hermitian su(2) bivector i*n.sigma."""
    norm = math.sqrt(sum(x * x for x in axis))
    return bivector_raw(tuple(value / norm for value in axis))


def bivector_raw(vector: tuple[float, float, float]) -> Matrix:
    """Anti-Hermitian bivector with magnitude retained."""
    x, y, z = vector
    return ((1j * z, y + 1j * x), (-y + 1j * x, -1j * z))


def mixed_action(area_bivector: Matrix, loop: Matrix) -> float:
    curvature = ((1.0 - loop[0][0], -loop[0][1]),
                 (-loop[1][0], 1.0 - loop[1][1]))
    product = mul(area_bivector, curvature)
    return 0.5 * (product[0][0] + product[1][1]).real


def max_error(a: Matrix, b: Matrix) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))


def matrix_sum(values: tuple[Matrix, ...]) -> Matrix:
    return tuple(tuple(sum(value[i][j] for value in values) for j in range(2))
                 for i in range(2))  # type: ignore[return-value]


def transform(links: tuple[Matrix, Matrix, Matrix, Matrix],
              frames: tuple[Matrix, Matrix, Matrix, Matrix]) -> tuple[Matrix, ...]:
    # Oriented cycle 0->1->2->3->0.
    targets = (1, 2, 3, 0)
    return tuple(mul(mul(frames[i], links[i]), dagger(frames[targets[i]]))
                 for i in range(4))


def main() -> int:
    links = (
        su2((1.0, 0.2, -0.1), 0.37), su2((0.1, 1.0, 0.3), -0.51),
        su2((-0.2, 0.4, 1.0), 0.29), su2((0.7, -0.3, 0.5), 0.43),
    )
    frames = (
        su2((0.2, 1.0, 0.1), 0.61), su2((1.0, -0.1, 0.2), -0.32),
        su2((0.3, 0.5, 1.0), 0.47), su2((-0.4, 1.0, 0.2), -0.28),
    )
    loop = plaquette(links)
    transformed_loop = plaquette(transform(links, frames))
    expected_loop = mul(mul(frames[0], loop), dagger(frames[0]))
    covariance_error = max_error(transformed_loop, expected_loop)
    action_error = abs(action(transformed_loop) - action(loop))
    area = bivector((0.4, -0.2, 1.0))
    transformed_area = mul(mul(frames[0], area), dagger(frames[0]))
    mixed_error = abs(mixed_action(transformed_area, transformed_loop)
                      - mixed_action(area, loop))
    frozen_frame_error = abs(mixed_action(area, transformed_loop)
                             - mixed_action(area, loop))

    # A second loop shares U_12 and the frames at vertices 1 and 2.  This is
    # the smallest check that local cancellations survive gluing plaquettes.
    extra_frames = (su2((1.0, 0.4, -0.2), 0.36),
                    su2((-0.1, 0.7, 1.0), -0.41))
    second_links = (
        links[1], su2((0.6, 0.1, 1.0), -0.22),
        su2((1.0, -0.5, 0.3), 0.48), su2((0.2, 1.0, -0.4), 0.33),
    )
    second_frames = (frames[1], frames[2], extra_frames[0], extra_frames[1])
    second_loop = plaquette(second_links)
    transformed_second = plaquette(transform(second_links, second_frames))
    second_area = bivector((-0.3, 0.8, 0.5))
    transformed_second_area = mul(mul(frames[1], second_area), dagger(frames[1]))
    original_complex_action = mixed_action(area, loop) + mixed_action(second_area, second_loop)
    transformed_complex_action = (
        mixed_action(transformed_area, transformed_loop)
        + mixed_action(transformed_second_area, transformed_second)
    )
    complex_action_error = abs(transformed_complex_action - original_complex_action)

    # Minimal tetrahedral closure: four oriented face bivectors sum to zero.
    face_vectors = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0),
                    (0.0, 0.0, 1.0), (-1.0, -1.0, -1.0))
    face_bivectors = tuple(bivector_raw(vector) for vector in face_vectors)
    closure_error = max_error(matrix_sum(face_bivectors), ((0j, 0j), (0j, 0j)))
    closure_frame = frames[0]
    rotated_faces = tuple(mul(mul(closure_frame, face), dagger(closure_frame))
                          for face in face_bivectors)
    rotated_closure_error = max_error(matrix_sum(rotated_faces), ((0j, 0j), (0j, 0j)))
    open_boundary_error = max_error(matrix_sum(face_bivectors[:-1]), ((0j, 0j), (0j, 0j)))

    eps = 1e-4
    plus = list(frames)
    minus = list(frames)
    plus[0] = su2((0.3, -0.4, 1.0), eps)
    minus[0] = su2((0.3, -0.4, 1.0), -eps)
    ward_residual = abs(
        (action(plaquette(transform(links, tuple(plus))))
         - action(plaquette(transform(links, tuple(minus))))) / (2.0 * eps)
    )
    checks = {
        "off_shell_loop_covariance": covariance_error < 1e-12,
        "off_shell_action_invariance": action_error < 1e-12,
        "infinitesimal_ward_residual": ward_residual < 1e-10,
        "mixed_frame_connection_invariance": mixed_error < 1e-12,
        "frozen_frame_breaks_mixed_invariance": frozen_frame_error > 1e-4,
        "shared_multiloop_invariance": complex_action_error < 1e-12,
        "bivector_closure": closure_error < 1e-12,
        "closure_is_frame_covariant": rotated_closure_error < 1e-12,
        "missing_face_breaks_closure": open_boundary_error > 1e-3,
    }
    result = {
        "checks": checks,
        "passed": all(checks.values()),
        "original_action": action(loop),
        "loop_covariance_error": covariance_error,
        "action_invariance_error": action_error,
        "ward_residual": ward_residual,
        "mixed_action_invariance_error": mixed_error,
        "frozen_frame_action_change": frozen_frame_error,
        "shared_multiloop_action_error": complex_action_error,
        "closure_error": closure_error,
        "rotated_closure_error": rotated_closure_error,
        "missing_face_closure_error": open_boundary_error,
        "scope": "two glued SU(2) plaquettes and bivectors; not the full gravitational cubic Ward identity",
    }
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
