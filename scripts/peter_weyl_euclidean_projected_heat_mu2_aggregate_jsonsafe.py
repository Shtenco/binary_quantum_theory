#!/usr/bin/env python3
"""JSON-safe CLI wrapper for the actual Euclidean mu2/Q1 aggregator.

Scientific computation is delegated unchanged to
peter_weyl_euclidean_projected_heat_mu2_aggregate.run().  This wrapper only
normalizes NumPy scalar containers before JSON serialization, fixing the old
Actions failure caused by numpy.bool_.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import peter_weyl_euclidean_projected_heat_mu2_aggregate as CORE


def native(x):
    if isinstance(x, np.generic):
        return x.item()
    if isinstance(x, dict):
        return {str(k): native(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [native(v) for v in x]
    return x


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--master-images', type=Path, required=True)
    ap.add_argument('--euclidean-packet', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--spectral-packet', type=Path, required=True)
    ap.add_argument('--q1-dir', type=Path)
    a = ap.parse_args()

    result, packet, q1_states = CORE.run(a.master_images, a.euclidean_packet)
    result = native(result)
    packet = native(packet)

    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    a.spectral_packet.parent.mkdir(parents=True, exist_ok=True)
    a.spectral_packet.write_text(json.dumps(packet, indent=2) + '\n', encoding='utf-8')

    if a.q1_dir is not None:
        a.q1_dir.mkdir(parents=True, exist_ok=True)
        meta = native({
            'schema': 'BQG_EUCLIDEAN_MASTER_LANCZOS_Q1_V1',
            'rank': len(q1_states),
            'B1_matrix': result['first_master_lanczos_residual_gram']['B1_matrix'],
            'operator_source_sha256': result['operator_source_sha256'],
            'claim_boundary': 'First Euclidean master-Lanczos block only; no full history/projector claim.'
        })
        (a.q1_dir / 'q1_manifest.json').write_text(json.dumps(meta, indent=2) + '\n', encoding='utf-8')
        for i, st in enumerate(q1_states):
            payload = native({
                'schema': 'BQG_EUCLIDEAN_MASTER_LANCZOS_Q1_COLUMN_V1',
                'q1_index': i,
                'support': len(st),
                'state': CORE.encode_state(st),
            })
            (a.q1_dir / f'q1_{i:02d}.json').write_text(json.dumps(payload, separators=(',', ':')) + '\n', encoding='utf-8')

    print(json.dumps({
        'schema': result['schema'],
        'passed': result['passed'],
        'mu1_min': result['mu1']['eigenvalue_min'],
        'mu1_max': result['mu1']['eigenvalue_max'],
        'mu2_min': result['mu2']['eigenvalue_min'],
        'mu2_max': result['mu2']['eigenvalue_max'],
        'R1_rank': result['first_master_lanczos_residual_gram']['rank'],
        'R1_min': result['first_master_lanczos_residual_gram']['eigenvalue_min'],
        'R1_max': result['first_master_lanczos_residual_gram']['eigenvalue_max'],
        'Q1_rank': result['first_master_lanczos_residual_gram']['Q1_rank'],
    }, indent=2))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
