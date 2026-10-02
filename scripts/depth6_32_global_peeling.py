#!/usr/bin/env python3
"""Fail-closed global unique-q peeling helpers for depth-6 [3,2].

This module deliberately separates three statements that must never be
conflated:

1. complete KEYMETA coverage authorizes global occupancy analysis;
2. a block with enough globally unique q rows is only a *candidate*;
3. the candidate peels only after an explicit numerical full-column-rank
   certificate for the stack of those unique-q matrices.

No function in this module claims global rank or numerical closure.
"""
from __future__ import annotations

from typing import Any, Iterable

import numpy as np


def _validate_exact_keymeta(blocks, *, target_blocks: int, target_columns: int):
    target_blocks = int(target_blocks)
    target_columns = int(target_columns)
    if target_blocks <= 0 or target_columns <= 0:
        raise RuntimeError('positive KEYMETA targets required')

    by_orbit = {}
    columns = 0
    for block in blocks:
        oid = int(block['orbit_id'])
        if oid in by_orbit:
            raise RuntimeError(f'duplicate orbit {oid}')
        m = int(block['m'])
        if m <= 0:
            raise RuntimeError(f'orbit {oid}: non-positive m')
        q_rows = block.get('q_rows')
        if not isinstance(q_rows, dict):
            raise RuntimeError(f'orbit {oid}: q_rows must be a dict')
        for q, n0 in q_rows.items():
            n = int(n0)
            if n <= 0:
                raise RuntimeError(f'orbit {oid}: q={q!r} has non-positive rows')
        by_orbit[oid] = block
        columns += m

    if len(by_orbit) != target_blocks or columns != target_columns:
        raise RuntimeError(
            'exact KEYMETA coverage required before global peeling: '
            f'blocks={len(by_orbit)}/{target_blocks} columns={columns}/{target_columns}'
        )
    return by_orbit


def plan_peeling_wave(
    blocks,
    *,
    target_blocks: int,
    target_columns: int,
    active_orbit_ids: Iterable[int] | None = None,
) -> dict:
    """Find candidate blocks using q occupancy among the current active set.

    A candidate has at least ``m`` rows coming from q sectors occupied by that
    block alone in the active set.  This is only a row-count precondition; it is
    never a rank certificate.
    """
    by_orbit = _validate_exact_keymeta(
        blocks, target_blocks=target_blocks, target_columns=target_columns
    )

    if active_orbit_ids is None:
        active = set(by_orbit)
    else:
        active = {int(x) for x in active_orbit_ids}
        unknown = active.difference(by_orbit)
        if unknown:
            raise RuntimeError(f'active set contains unknown frozen orbits: {sorted(unknown)}')

    q_owners: dict[Any, list[int]] = {}
    for oid in sorted(active):
        for q in by_orbit[oid]['q_rows']:
            q_owners.setdefault(q, []).append(oid)

    candidates = []
    for oid in sorted(active):
        block = by_orbit[oid]
        unique_qs = [q for q in block['q_rows'] if len(q_owners.get(q, ())) == 1]
        unique_rows = sum(int(block['q_rows'][q]) for q in unique_qs)
        m = int(block['m'])
        if unique_rows >= m:
            candidates.append({
                'orbit_id': oid,
                'm': m,
                'unique_qs': unique_qs,
                'unique_q_count': len(unique_qs),
                'unique_rows': unique_rows,
                'rank_certified': False,
                'peel_authorized': False,
            })

    return {
        'schema_version': 1,
        'kind': 'BQG_DEPTH6_32_GLOBAL_PEELING_WAVE_PLAN',
        'active_blocks': len(active),
        'active_columns': sum(int(by_orbit[oid]['m']) for oid in active),
        'candidate_blocks': len(candidates),
        'candidates': candidates,
        'exact_keymeta_coverage': True,
        'rank_certified': False,
        'numerical_closure_claimed': False,
        'claim_boundary': (
            'Candidate status follows only from globally unique q-row counts. '
            'Each candidate still requires an explicit full-column-rank '
            'numerical certificate before it can be peeled.'
        ),
    }


def certify_unique_q_stack(
    block: dict,
    master_map: dict,
    unique_qs: Iterable[Any],
    *,
    rtol: float = 1e-10,
    atol: float = 1e-12,
) -> dict:
    """Numerically certify one candidate using only its currently unique q rows."""
    oid = int(block['orbit_id'])
    m = int(block['m'])
    if m <= 0:
        raise RuntimeError(f'orbit {oid}: non-positive m')
    if not isinstance(master_map, dict):
        raise RuntimeError('master_map must be a dict')
    rtol = float(rtol)
    atol = float(atol)
    if rtol < 0 or atol < 0 or not np.isfinite(rtol) or not np.isfinite(atol):
        raise RuntimeError('finite non-negative SVD tolerances required')

    qs = list(unique_qs)
    if not qs:
        raise RuntimeError(f'orbit {oid}: no unique q sectors supplied')

    pieces = []
    for q in qs:
        if q not in master_map:
            raise RuntimeError(f'orbit {oid}: missing unique q matrix {q!r}')
        M = np.asarray(master_map[q], dtype=complex)
        if M.ndim != 2 or M.shape[1] != m:
            raise RuntimeError(
                f'orbit {oid}: bad unique q matrix {q!r} shape={tuple(M.shape)} expected_columns={m}'
            )
        if M.shape[0] <= 0:
            raise RuntimeError(f'orbit {oid}: empty unique q matrix {q!r}')
        if not np.all(np.isfinite(M.real)) or not np.all(np.isfinite(M.imag)):
            raise RuntimeError(f'orbit {oid}: non-finite unique q matrix {q!r}')
        pieces.append(M)

    stack = np.vstack(pieces)
    s = np.linalg.svd(stack, compute_uv=False)
    sigma_max = float(s[0]) if s.size else 0.0
    sigma_min = float(s[-1]) if s.size else 0.0
    threshold = float(max(atol, rtol * sigma_max))
    rank = int(np.count_nonzero(s > threshold))
    full = rank == m

    return {
        'schema_version': 1,
        'kind': 'BQG_DEPTH6_32_UNIQUE_Q_BLOCK_RANK_CERTIFICATE',
        'orbit_id': oid,
        'm': m,
        'unique_q_count': len(qs),
        'rows': int(stack.shape[0]),
        'rank': rank,
        'sigma_max': sigma_max,
        'sigma_min': sigma_min,
        'threshold': threshold,
        'rtol': rtol,
        'atol': atol,
        'rank_certified': bool(full),
        'peel_authorized': bool(full),
        'numerical_closure_claimed': False,
        'claim_boundary': (
            'This certificate proves full column rank only for this frozen '
            'block on its supplied globally unique q-row stack.  It does not '
            'by itself prove global [3,2] rank or numerical closure.'
        ),
    }
