#!/usr/bin/env python3
"""Assemble the frozen signed BQG gravitational operator for a centered five-block patch.

This is an operator/provenance bridge, not a new microscopic dynamics model.
It consumes exact action-column matrices for the already frozen Hermitian pieces

    H_E^sine
    S = -i/2 (L_raw - L_raw^dagger)

on one common closed finite basis and forms only

    G_frozen = -(2/3) H_E^sine -(32/9) S .

The route operator R_op is deliberately forbidden in this gravitational TT
precursor.  The output is the NPZ contract consumed by
`bqg_multiblock_tt_wilson_extractor.py`.

Input NPZ (allow_pickle=False) must contain

    E_columns       NxN complex matrix, column j = H_E^sine |j>
    S_columns       NxN complex matrix, column j = S |j>
    p_indices       30 retained metric-carrier indices
    p_block         30 block ids, exactly five blocks x six coordinates
    p_coord         30 coordinate ids 0..5
    block_positions 5x3 positions ordered by sorted block id
    central_block   scalar block id
    C00_E            <0|H_E^sine|0>
    C00_S            <0|S|0>
    metadata_json   provenance JSON string

Optional:

    basis_ids       N unique string ids for auditability
    metric_map      frozen/production 6x6 q->h map

The producer that creates E_columns/S_columns must already have completed the
chosen cutoff/reachable-basis closure.  This assembler never fills missing
columns, invents shared-face amplitudes, adds an i*eta regulator, or fits a
transfer coefficient.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import tempfile

import numpy as np

RTOL = 1e-10
HERM_TOL = 5e-9
GEOM_TOL = 2e-9
E_COEFF = -2.0 / 3.0
S_COEFF = -32.0 / 9.0


def hermitian_defect(A: np.ndarray) -> float:
    return float(np.linalg.norm(A - A.conj().T) / max(np.linalg.norm(A), 1e-300))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_array(A: np.ndarray) -> str:
    A = np.ascontiguousarray(A)
    h = hashlib.sha256()
    h.update(str(A.dtype).encode())
    h.update(str(A.shape).encode())
    h.update(A.view(np.uint8))
    return h.hexdigest()


def load_metadata(z) -> dict:
    if 'metadata_json' not in z.files:
        return {}
    raw = z['metadata_json']
    if np.ndim(raw) == 0:
        raw = raw.item()
    if isinstance(raw, bytes):
        raw = raw.decode('utf-8')
    return json.loads(str(raw))


def rational_pair(value, expected: tuple[int, int]) -> bool:
    try:
        a, b = value
        return int(a) == expected[0] and int(b) == expected[1]
    except Exception:
        return False


def validate_source_provenance(meta: dict) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if meta.get('synthetic') is not False:
        errors.append('metadata.synthetic must be false')
    if meta.get('target_fitting_used') is not False:
        errors.append('metadata.target_fitting_used must be false')
    if meta.get('basis_closure_complete') is not True:
        errors.append('metadata.basis_closure_complete must be true')
    if not str(meta.get('source_commit', '')).strip():
        errors.append('metadata.source_commit is required')
    if not meta.get('regulator'):
        errors.append('metadata.regulator is required')
    comps = set(meta.get('operator_components', []))
    if not {'H_E_sine', 'S'} <= comps:
        errors.append('operator_components must contain H_E_sine and S')
    if 'R_op' in comps or meta.get('route_operator_included') is not False:
        errors.append('R_op/route operator is forbidden in the signed gravitational precursor')
    defs = meta.get('component_definitions', {})
    if defs.get('H_E_sine') not in ('physical-sine Euclidean Hamiltonian', 'H_E_sine'):
        errors.append('component_definitions.H_E_sine is not frozen')
    if defs.get('S') not in ('-i/2*(L_raw-L_raw_dagger)', '-i/2(L_raw-L_raw_dagger)'):
        errors.append('component_definitions.S must be Hermitian completion -i/2(L_raw-L_raw_dagger)')
    return not errors, errors


def validate_p_layout(pidx: np.ndarray, pblock: np.ndarray, pcoord: np.ndarray,
                      positions: np.ndarray, central: int, n: int) -> dict:
    pidx = np.asarray(pidx, int).ravel()
    pblock = np.asarray(pblock, int).ravel()
    pcoord = np.asarray(pcoord, int).ravel()
    if pidx.size != 30 or pblock.size != 30 or pcoord.size != 30:
        raise RuntimeError('five-block metric carrier must contain exactly 30 P vectors')
    if len(set(map(int, pidx))) != 30 or np.any(pidx < 0) or np.any(pidx >= n):
        raise RuntimeError('p_indices must be 30 unique in-range basis indices')
    blocks = sorted(set(map(int, pblock)))
    if len(blocks) != 5 or central not in blocks:
        raise RuntimeError('p_block must contain exactly five blocks including central_block')
    for b in blocks:
        got = sorted(map(int, pcoord[pblock == b]))
        if got != list(range(6)):
            raise RuntimeError(f'block {b} must contain each q coordinate 0..5 exactly once; got {got}')
    positions = np.asarray(positions, float)
    if positions.shape != (5, 3):
        raise RuntimeError('block_positions must have shape (5,3) ordered by sorted block id')
    pos = {b: positions[i] for i, b in enumerate(blocks)}
    offs = np.asarray([pos[b] - pos[central] for b in blocks if b != central], float)
    lens = np.linalg.norm(offs, axis=1)
    if np.min(lens) <= 0:
        raise RuntimeError('zero neighbor displacement')
    unit = offs / lens[:, None]
    a = float(np.mean(lens))
    defects = {
        'sum_defect': float(np.linalg.norm(np.sum(unit, axis=0))),
        'second_moment_defect': float(np.linalg.norm(unit.T @ unit - (4.0/3.0)*np.eye(3))),
        'equal_length_defect': float(np.max(np.abs(lens/a - 1.0))),
    }
    if max(defects.values()) > GEOM_TOL:
        raise RuntimeError('center+four-neighbor geometry is not the frozen tetrahedral shell: '+json.dumps(defects))
    return {'blocks': blocks, 'a_star': a, **defects}


def assemble(input_path: Path, output_path: Path, summary_path: Path | None = None) -> dict:
    with np.load(input_path, allow_pickle=False) as z:
        required = {
            'E_columns','S_columns','p_indices','p_block','p_coord',
            'block_positions','central_block','C00_E','C00_S','metadata_json'
        }
        missing = sorted(required - set(z.files))
        if missing:
            raise RuntimeError(f'missing source arrays: {missing}')
        E = np.asarray(z['E_columns'], complex)
        S = np.asarray(z['S_columns'], complex)
        pidx = np.asarray(z['p_indices'], int)
        pblock = np.asarray(z['p_block'], int)
        pcoord = np.asarray(z['p_coord'], int)
        positions = np.asarray(z['block_positions'], float)
        central = int(np.asarray(z['central_block']).item())
        c00e = complex(np.asarray(z['C00_E']).item())
        c00s = complex(np.asarray(z['C00_S']).item())
        meta = load_metadata(z)
        metric_map = np.asarray(z['metric_map'], float) if 'metric_map' in z.files else None
        basis_ids = np.asarray(z['basis_ids']).astype(str) if 'basis_ids' in z.files else None

    ok, errors = validate_source_provenance(meta)
    if not ok:
        raise RuntimeError('SOURCE_PROVENANCE_REJECTED: ' + '; '.join(errors))
    if E.ndim != 2 or E.shape[0] != E.shape[1] or S.shape != E.shape:
        raise RuntimeError('E_columns and S_columns must be square matrices of the same shape')
    n = E.shape[0]
    if basis_ids is not None:
        if basis_ids.shape != (n,) or len(set(map(str, basis_ids))) != n:
            raise RuntimeError('basis_ids must contain N unique state ids')
    edef = hermitian_defect(E)
    sdef = hermitian_defect(S)
    if edef > HERM_TOL:
        raise RuntimeError(f'H_E_sine column matrix is not Hermitian: defect={edef:.3e}')
    if sdef > HERM_TOL:
        raise RuntimeError(f'S column matrix is not Hermitian: defect={sdef:.3e}')
    if abs(c00e.imag) > HERM_TOL or abs(c00s.imag) > HERM_TOL:
        raise RuntimeError('C00_E and C00_S must be real for Hermitian components')
    layout = validate_p_layout(pidx, pblock, pcoord, positions, central, n)
    if metric_map is not None and (metric_map.shape != (6,6) or np.linalg.matrix_rank(metric_map, RTOL) != 6):
        raise RuntimeError('metric_map must be an invertible 6x6 matrix')

    G = E_COEFF * E + S_COEFF * S
    G = (G + G.conj().T) / 2.0
    gdef = hermitian_defect(G)
    if gdef > HERM_TOL:
        raise RuntimeError(f'signed G is not Hermitian: defect={gdef:.3e}')
    C00 = E_COEFF * c00e.real + S_COEFF * c00s.real

    out_meta = {
        'actual_bqg_operator': True,
        'synthetic': False,
        'provenance_level': 'microscopic_constraint',
        'physical_history_1pi': False,
        'operator_family': 'frozen_signed_gravitational_constraint',
        'operator_components': ['H_E_sine','S'],
        'operator_coefficients_exact': {'H_E_sine': [-2,3], 'S': [-32,9]},
        'operator_formula': 'G=-(2/3)H_E_sine-(32/9)S',
        'route_operator_included': False,
        'source_commit': meta['source_commit'],
        'regulator': meta['regulator'],
        'basis_closure_complete': True,
        'target_fitting_used': False,
        'source_bundle_sha256': sha256_file(input_path),
        'E_matrix_sha256': sha256_array(E),
        'S_matrix_sha256': sha256_array(S),
        'G_matrix_sha256': sha256_array(G),
        'source_component_metadata': meta,
    }

    kwargs = dict(
        C_full=G,
        p_indices=np.asarray(pidx, int),
        p_block=np.asarray(pblock, int),
        p_coord=np.asarray(pcoord, int),
        block_positions=np.asarray(positions, float),
        central_block=np.asarray(central, int),
        C00=np.asarray(C00, float),
        metadata_json=np.asarray(json.dumps(out_meta, sort_keys=True)),
    )
    if metric_map is not None:
        kwargs['metric_map'] = metric_map
    if basis_ids is not None:
        kwargs['basis_ids'] = basis_ids
    output_path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(output_path, **kwargs)

    out = {
        'status': 'assembled frozen signed gravitational five-block operator',
        'science_status': 'MICROSCOPIC_SIGNED_G_OPERATOR_READY_FOR_SCHUR',
        'passed': True,
        'dimension': n,
        'P_dimension': int(np.asarray(pidx).size),
        'Q_dimension': int(n - np.asarray(pidx).size),
        'E_coefficient': E_COEFF,
        'S_coefficient': S_COEFF,
        'E_hermitian_defect': edef,
        'S_hermitian_defect': sdef,
        'G_hermitian_defect': gdef,
        'C00_signed_G': float(C00),
        'geometry': layout,
        'source_bundle_sha256': out_meta['source_bundle_sha256'],
        'G_matrix_sha256': out_meta['G_matrix_sha256'],
        'output': str(output_path),
        'hard_scope_guard': (
            'This is the frozen microscopic signed-constraint spatial precursor only. '
            'It is not Z_phys, W_phys, Gamma_phys, a physical omega kernel, or a frozen physical c_BQG_IR vector.'
        ),
    }
    if summary_path is not None:
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    return out


def selftest() -> dict:
    rng = np.random.default_rng(20260907)
    n = 34
    X = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    E = (X + X.conj().T) / 2
    Y = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    S = (Y + Y.conj().T) / 2
    pidx = np.arange(30, dtype=int)
    pblock = np.repeat(np.arange(5), 6)
    pcoord = np.tile(np.arange(6), 5)
    normals = np.asarray([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)], float)/math.sqrt(3)
    positions = np.vstack([np.zeros(3), normals])
    meta = {
        'synthetic': False,
        'target_fitting_used': False,
        'basis_closure_complete': True,
        'source_commit': 'SELFTEST_COMMIT',
        'regulator': {'Jmax': 'selftest'},
        'operator_components': ['H_E_sine','S'],
        'route_operator_included': False,
        'component_definitions': {
            'H_E_sine': 'H_E_sine',
            'S': '-i/2(L_raw-L_raw_dagger)',
        },
    }
    ok, errs = validate_source_provenance(meta)
    layout = validate_p_layout(pidx, pblock, pcoord, positions, 0, n)
    G = E_COEFF*E + S_COEFF*S
    coeff_ok = np.linalg.norm(G - (-(2/3)*E -(32/9)*S)) < 1e-12*np.linalg.norm(G)
    bad = dict(meta)
    bad['operator_components'] = ['H_E_sine','S','R_op']
    bad['route_operator_included'] = True
    bad_ok, _ = validate_source_provenance(bad)
    nonherm_rejected = hermitian_defect(E + np.triu(np.ones_like(E),1)) > HERM_TOL
    checks = {
        'valid_signed_source_provenance': ok and not errs,
        'route_operator_rejected': not bad_ok,
        'exact_signed_coefficients': bool(coeff_ok),
        'tetrahedral_five_block_layout': max(layout[k] for k in ('sum_defect','second_moment_defect','equal_length_defect')) < GEOM_TOL,
        'Hermitian_components': hermitian_defect(E) < HERM_TOL and hermitian_defect(S) < HERM_TOL,
        'nonhermitian_control_detected': bool(nonherm_rejected),
    }
    return {
        'status': 'signed five-block assembler infrastructure selftest',
        'science_status': 'INFRASTRUCTURE_SELFTEST_NOT_BQG_EVIDENCE',
        'passed': bool(all(checks.values())),
        'checks': checks,
        'hard_scope_guard': 'Synthetic algebra/provenance test only; no BQG Wilson coefficient is computed.',
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path)
    p.add_argument('--output', type=Path)
    p.add_argument('--summary', type=Path)
    p.add_argument('--selftest', action='store_true')
    a = p.parse_args()
    if a.selftest:
        out = selftest()
    else:
        if a.input is None or a.output is None:
            p.error('--input and --output are required unless --selftest is used')
        try:
            out = assemble(a.input, a.output, a.summary)
        except Exception as exc:
            out = {
                'status': 'STOP',
                'science_status': 'MISSING_OR_INVALID_SIGNED_OPERATOR_SOURCE',
                'passed': False,
                'error': str(exc),
                'hard_scope_guard': 'No matrix is emitted from incomplete, fitted, route-mixed, non-Hermitian, or non-closed input.',
            }
            if a.summary is not None:
                a.summary.parent.mkdir(parents=True, exist_ok=True)
                a.summary.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(out, indent=2))
    return 0 if out.get('passed') else 2


if __name__ == '__main__':
    raise SystemExit(main())
