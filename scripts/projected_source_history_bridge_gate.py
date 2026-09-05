#!/usr/bin/env python3
"""Bridge the existing projected-boundary source dressing controls to the physical W-history consumer.

This gate closes an integration seam, not the BQG physical-history physics.
It verifies simultaneously that:

1. the enlarged-projector source-dressing control is reproducible;
2. the finite constraint->history adapter control is reproducible;
3. the asymptotic near-zero rigging-limit control is reproducible;
4. a static/projector-depth source Hessian can be handed to the W-history
   measurement schema algebraically but MUST remain nonphysical because
   projection heat depth is not physical time;
5. an independently certified synthetic physical-history packet is accepted by
   the same downstream measurement interface.

Therefore the missing production input after GREEN is exactly a theory-specific
source-dressed BQG physical history with geometric/relational time and spatial
separation.  No constraint spectral z or master heat depth is promoted to omega.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from boundary_projector_source_dressing_gate import run as source_dressing_control
from bqg_physical_history_adapter_gate import run as history_adapter_control
from near_zero_rigging_limit_gate import run as rigging_limit_control
from scalar_physical_history_cumulant_gate import measure


def _base_flags(value: bool) -> dict[str, bool]:
    return {
        'theory_specific_physical_history': value,
        'connected_functional_W_not_raw_Z': value,
        'physical_tau_certified': value,
        'physical_spatial_separation_certified': value,
        'ward_source_insertions_certified': value,
        'same_history_normalization_across_sources': value,
        'legendre_hessian_convention_certified': value,
        'conserved_probe_frozen': value,
        'background_and_scale_convention_frozen': value,
    }


def _prov(tag: str) -> dict[str, str]:
    return {
        'physical_history_hash': tag,
        'ward_source_hash': tag,
        'time_space_convention_hash': tag,
        'history_normalization_hash': tag,
        'source_convention_hash': tag,
        'background_convention_hash': tag,
    }


def static_projector_control_packet(source: dict[str, Any]) -> dict[str, Any]:
    """Use the converged projected source Hessian as a NONPHYSICAL seam test.

    The source-control heat `tau` is deliberately NOT copied into the physical
    history `tau` field.  We set a dummy separation 0 only to test the downstream
    data contract and explicitly leave all physical-history flags false.
    """
    h = source['heat_kernel_staircase'][-1]['source_Hessian']
    return {
        'schema': 'BQG_PHYSICAL_SCALAR_W_HISTORY_V1',
        'points': [{
            'tau': 0.0,
            'r': [0.0, 0.0, 0.0],
            'weight': 1.0,
            'derivative_mode': 'provided_connected_hessian',
            'connected_hessian': {
                'G_QQ': h[0][0],
                'G_Qzeta': h[0][1],
                'G_zetazeta': h[1][1],
            },
        }],
        'modes': [{'omega': 0.0, 'k': [0.0, 0.0, 0.0]}],
        'physical_flags': _base_flags(False),
        'provenance': {},
        'source_step_scan_certified': False,
        'seam_note': 'Data-contract test only. Master heat depth is not physical tau and is intentionally not propagated.',
    }


def synthetic_physical_history_packet() -> dict[str, Any]:
    """Complete synthetic provenance control for the downstream physical seam."""
    return {
        'schema': 'BQG_PHYSICAL_SCALAR_W_HISTORY_V1',
        'points': [
            {'tau': 0.0, 'r': [0.0,0.0,0.0], 'weight': 1.0,
             'derivative_mode': 'provided_connected_hessian',
             'connected_hessian': {'G_QQ': 2.0, 'G_Qzeta': 0.5, 'G_zetazeta': 3.0}},
            {'tau': 1.0, 'r': [1.0,0.0,0.0], 'weight': 0.5,
             'derivative_mode': 'provided_connected_hessian',
             'connected_hessian': {'G_QQ': 0.25, 'G_Qzeta': 0.1, 'G_zetazeta': 0.4}},
        ],
        'modes': [
            {'omega': 0.0, 'k': [0.0,0.0,0.0]},
            {'omega': 0.7, 'k': [0.2,0.0,0.0]},
        ],
        'physical_flags': _base_flags(True),
        'provenance': _prov('synthetic-projected-source-history-seam'),
        'source_step_scan_certified': True,
    }


def run() -> dict[str, Any]:
    src = source_dressing_control()
    adapter = history_adapter_control()
    rig = rigging_limit_control()

    nonphysical = measure(static_projector_control_packet(src))
    synthetic = measure(synthetic_physical_history_packet())

    nm = nonphysical['fourier_modes'][0]
    sh = src['heat_kernel_staircase'][-1]['source_Hessian']
    tests = {
        'source_dressing_control_passes': src['passed'] is True,
        'history_adapter_control_passes': adapter['passed'] is True,
        'rigging_limit_control_passes': rig['passed'] is True,
        'projected_static_hessian_passes_schema': nonphysical['passed'] is True,
        'projected_static_hessian_preserved_QQ': abs(nm['G_QQ']['re'] - sh[0][0]) < 1e-12,
        'projected_static_hessian_preserved_Qzeta': abs(nm['G_Qzeta']['re'] - sh[0][1]) < 1e-12,
        'projected_static_hessian_preserved_zetazeta': abs(nm['G_zetazeta']['re'] - sh[1][1]) < 1e-12,
        'master_heat_depth_never_becomes_physical_time': nonphysical['physical_interpretation_allowed'] is False,
        'static_control_reports_missing_physical_history_flags': 'physical_tau_certified' in nonphysical['missing_required_flags'],
        'synthetic_certified_history_is_accepted': synthetic['physical_interpretation_allowed'] is True,
        'synthetic_history_emits_two_fourier_modes': len(synthetic['fourier_modes']) == 2,
    }

    return {
        'schema': 'BQG_PROJECTED_SOURCE_HISTORY_BRIDGE_V1',
        'passed': bool(all(tests.values())),
        'science_status': 'PROJECTED_SOURCE_TO_PHYSICAL_HISTORY_INTERFACE_FROZEN',
        'tests': tests,
        'source_dressing_control_summary': {
            'science_status': src['science_status'],
            'master_gap': src['master_gap'],
            'boundary_physical_Gram_G0': src['boundary_physical_Gram_G0'],
            'final_source_Hessian': sh,
        },
        'history_adapter_control_summary': {
            'science_status': adapter['science_status'],
            'physical_dimension': adapter['physical_dimension'],
            'projector_error_to_existing_relational_projector': adapter['projector_error_to_existing_relational_projector'],
        },
        'rigging_limit_control_summary': {
            'science_status': rig['science_status'],
            'final_heat_error': rig['positive_separated_low_cluster']['final_heat_error'],
            'final_boundary_error': rig['positive_separated_low_cluster']['final_boundary_error'],
        },
        'nonphysical_static_seam_result': {
            'science_status': nonphysical['science_status'],
            'physical_interpretation_allowed': nonphysical['physical_interpretation_allowed'],
            'missing_required_flags': nonphysical['missing_required_flags'],
        },
        'synthetic_physical_seam_result': {
            'science_status': synthetic['science_status'],
            'physical_interpretation_allowed': synthetic['physical_interpretation_allowed'],
            'fourier_mode_count': len(synthetic['fourier_modes']),
        },
        'remaining_open_physics_input': 'Actual theory-specific source-dressed connected BQG W[J_Q,J_zeta; Delta t_rel, r] on a certified physical projector/history sequence.',
        'forbidden_shortcuts': [
            'master heat tau -> physical Delta t or omega',
            'constraint/Feshbach z -> physical omega',
            'positive-control maximally mixed density matrix -> cosmological vacuum',
            'static equal-history covariance -> separated-time physical propagator',
        ],
        'claim_boundary': 'GREEN freezes the seam between projector/source dressing and the already-closed W-history measurement consumer. It does not close PHYSICAL_PROJECTOR_HISTORY or CONNECTED_INTERBLOCK_HISTORY and does not produce a BQG dark-sector prediction.',
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + '\n', encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
