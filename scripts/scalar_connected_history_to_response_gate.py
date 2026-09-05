#!/usr/bin/env python3
"""End-to-end scalar connected-history -> Ward response closure gate.

This gate composes two already-registered exact contracts without adding a new
physical ansatz:

  G_conn(Q,zeta; omega,k)
    -> scalar_connected_history_extractor_gate.extract
    -> BQG_SCALAR_WARD_KERNEL_V1(A,B,C)
    -> scalar_ward_kernel_response_gate.analyze
    -> Psi, Phi, determinant, poles, residues and stability diagnostics.

The algebraic consumer pipeline is considered closed when this composition is
exact and fail-closed.  It is NOT a substitute for computing the three
BQG theory-specific connected physical cumulants G_QQ, G_Qzeta, G_zetazeta.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scalar_connected_history_extractor_gate import extract
from scalar_ward_kernel_response_gate import analyze


def run_pipeline(packet: dict[str, Any]) -> dict[str, Any]:
    extracted = extract(packet)
    if not extracted.get('ward_kernel_emitted'):
        return {
            'schema': 'BQG_SCALAR_CONNECTED_HISTORY_TO_RESPONSE_V1',
            'science_status': 'CONNECTED_HISTORY_REQUIRES_FURTHER_REDUCTION',
            'extractor': extracted,
            'response_emitted': False,
            'physical_interpretation_allowed': False,
            'claim_boundary': 'A singular or unreduced connected source Hessian is not converted into a physical scalar response.'
        }

    response = analyze(extracted['ward_kernel_packet'])
    physical = bool(
        extracted.get('physical_interpretation_allowed')
        and response.get('physical_interpretation_allowed')
    )
    return {
        'schema': 'BQG_SCALAR_CONNECTED_HISTORY_TO_RESPONSE_V1',
        'science_status': (
            'PHYSICAL_CONNECTED_HISTORY_RESPONSE_ANALYZED'
            if physical else
            'ALGEBRAIC_CONNECTED_HISTORY_RESPONSE_PIPELINE_PHYSICAL_INPUT_INCOMPLETE'
        ),
        'extractor': extracted,
        'response': response,
        'response_emitted': True,
        'physical_interpretation_allowed': physical,
        'microscopic_open_input': [
            'G_QQ(omega,k)',
            'G_Qzeta(omega,k)',
            'G_zetazeta(omega,k)',
        ],
        'closed_algebraic_chain': 'G_conn -> (A,B,C) -> det -> (Psi,Phi) -> poles/residues/stability',
        'claim_boundary': 'GREEN closes only the algebraic consumer chain. BQG physics still requires the three cumulants from one theory-specific connected physical history with certified physical omega.'
    }


def _flags(value: bool) -> dict[str, bool]:
    return {
        'theory_specific_connected_history': value,
        'vacuum_disconnected_pieces_removed': value,
        'physical_omega_certified': value,
        'ward_source_basis_certified': value,
        'legendre_hessian_convention_certified': value,
    }


def _prov(value: str | None) -> dict[str, str]:
    if not value:
        return {}
    return {
        'connected_history_hash': value,
        'ward_basis_hash': value,
        'history_convention_hash': value,
    }


def packet_for_kernel(A: str, B: str, C: str, *, physical: bool) -> dict[str, Any]:
    """Construct a connected Hessian equal to inverse([[A,B],[B,C]]).

    This helper is used only for synthetic selftests so the expected 1PI
    kernel is known before the extractor is called.
    """
    # For the selftests below B=0.  Keep construction explicit/frozen rather
    # than introducing a generic symbolic inversion helper into production.
    if B != '0':
        raise ValueError('selftest packet_for_kernel currently freezes B=0 controls')
    tag = 'synthetic-e2e' if physical else None
    return {
        'schema': 'BQG_CONNECTED_SCALAR_HISTORY_V1',
        'G_QQ': f'1/({A})',
        'G_Qzeta': '0',
        'G_zetazeta': f'1/({C})',
        'j_Q': 1,
        'j_zeta': 1,
        'conserved_probe_frozen': physical,
        'background_and_scale_convention_frozen': physical,
        'source_convention_hash': tag,
        'background_convention_hash': tag,
        'physical_flags': _flags(physical),
        'provenance': _prov(tag),
    }


def selftest() -> dict[str, Any]:
    tests: dict[str, bool] = {}

    # Static GR-like control: exact inverse recovers A=k2, B=0, C=2*k2,
    # and the response layer must find no omega^2 pole.
    static = run_pipeline(packet_for_kernel('k2', '0', '2*k2', physical=False))
    ek = static['extractor']['ward_kernel_packet']
    tests['static_exact_A'] = ek['A'] == 'k2'
    tests['static_exact_B'] = ek['B'] == '0'
    tests['static_exact_C'] = ek['C'] == '2*k2'
    tests['static_no_omega2_pole'] = static['response']['omega2_pole_count'] == 0
    tests['static_fail_closed_without_physical_history'] = static['physical_interpretation_allowed'] is False

    # Healthy extra-scalar control.  The connected Hessian is chosen as the
    # exact inverse of diag(k2, w2-k2/4-2).  The full chain must reconstruct
    # the registered healthy pole diagnostics.
    healthy = run_pipeline(packet_for_kernel('k2', '0', 'w2-k2/4-2', physical=True))
    hk = healthy['extractor']['ward_kernel_packet']
    tests['healthy_exact_A'] = hk['A'] == 'k2'
    tests['healthy_exact_B'] = hk['B'] == '0'
    tests['healthy_exact_C'] = hk['C'] in {'-(k2 - 4*w2 + 8)/4', 'w2 - k2/4 - 2'}
    tests['healthy_physical_chain_allowed'] = healthy['physical_interpretation_allowed'] is True
    tests['healthy_one_omega2_pole'] = healthy['response']['omega2_pole_count'] == 1
    pole = healthy['response']['omega2_poles'][0]
    tests['healthy_positive_residue'] = pole['ghost_test'] == 'POSITIVE_NONZERO_RESIDUES'
    tests['healthy_no_tachyon'] = pole['tachyon_test'] == 'NO_NEGATIVE_MASS2_AT_K0'
    tests['healthy_mass2_two'] = pole['mass2'] == '2'
    tests['healthy_cs2_one_quarter'] = pole['cs2'] == '1/4'

    # Singular connected source Hessian must stop before response analysis.
    singular_packet = {
        'schema': 'BQG_CONNECTED_SCALAR_HISTORY_V1',
        'G_QQ': 1,
        'G_Qzeta': 1,
        'G_zetazeta': 1,
        'physical_flags': _flags(True),
        'provenance': _prov('synthetic-singular'),
        'conserved_probe_frozen': True,
        'background_and_scale_convention_frozen': True,
        'source_convention_hash': 'synthetic-singular',
        'background_convention_hash': 'synthetic-singular',
    }
    singular = run_pipeline(singular_packet)
    tests['singular_stops_before_response'] = singular['response_emitted'] is False
    tests['singular_never_allows_physical_interpretation'] = singular['physical_interpretation_allowed'] is False

    return {
        'schema': 'BQG_SCALAR_CONNECTED_HISTORY_TO_RESPONSE_SELFTEST_V1',
        'passed': bool(all(tests.values())),
        'tests': tests,
        'controls': {
            'static': static,
            'healthy_extra_scalar': healthy,
            'singular': singular,
        },
        'algebraic_pipeline_closed': bool(all(tests.values())),
        'remaining_microscopic_input': [
            'G_QQ(omega,k)',
            'G_Qzeta(omega,k)',
            'G_zetazeta(omega,k)',
        ],
        'claim_boundary': 'Synthetic controls certify composition, exact inversion, pole classification and fail-closed behavior only.'
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--packet', type=Path)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()

    out: dict[str, Any] = {'selftest': selftest()}
    if args.packet:
        out['production'] = run_pipeline(json.loads(args.packet.read_text(encoding='utf-8')))
    out['passed'] = bool(out['selftest']['passed'])

    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + '\n', encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
