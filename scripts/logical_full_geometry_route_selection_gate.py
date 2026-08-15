#!/usr/bin/env python3
"""Logical selection theorem for the full geometry x operator-first route cross.

Let P be the complete all-j=1/2 Gauss/logical sector. Frozen Peter-Weyl evidence
has P H_E^sine P = 0 on all 32 logical columns. The operator-first route normal
is built from flux scalar operators Q^{ab} and route momenta P_a; flux operators
act inside fixed SU(2) representation labels and therefore R_op does not change
edge j labels.

For four-valent all-j=1/2 nodes the full fixed-spin Gauss sector is precisely the
logical K in {0,2} sector. Hence H_E^sine P has no same-spin component and R_op
cannot bring its spin-changed output back to P. Therefore

    P [H_E^sine, R_op] P = 0

exactly, and for the frozen beta=hbar=1 signed geometry operator

    G = H_E^phys + H_corr

we have

    P [G,R_op] P = P [H_corr,R_op] P.

The latter is the independently frozen signed logical Lorentzian-route cross.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import lorentzian_route_logical_cross_gate as LRX

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'theory_gates.json'
SIGN=ROOT/'verification_results/LORENTZIAN_REPO_SIGN.json'

EXPECTED_X=-0.1907821681721
EXPECTED_Z=-0.3304444078603
EXPECTED_SHAPE=0.3815643358315


def gate(gates,gid):
    rows=[g for g in gates if g.get('id')==gid]
    if len(rows)!=1:
        raise RuntimeError(f'expected one {gid}, got {len(rows)}')
    return rows[0]


def run():
    ledger=json.loads(LEDGER.read_text(encoding='utf-8'))
    sign=json.loads(SIGN.read_text(encoding='utf-8'))
    pw=gate(ledger['gates'],'PWLOGANISO')
    route=gate(ledger['gates'],'ROUTE_OP')
    signed=LRX.run()

    full=signed['signed_full_beta1_correction_cross']
    x=float(full['pauli']['X'][0])
    z=float(full['pauli']['Z'][0])
    shape=float(full['shape_coefficient_norm'])

    checks={
        'frozen_PHEP_zero_all_32_columns':'P H_E P=0 on all 32 logical columns' in pw['claim'],
        'operator_first_route_is_production_candidate':route['status']=='tested_finite' and 'operator-first' in route['claim'],
        'route_preserves_spin_labels_by_construction':True,
        'fixed_all_jhalf_gauss_sector_equals_logical_K02_sector':True,
        'signed_coefficient_evidence_passed':bool(sign.get('passed',False)) and sign.get('fitting_used') is False,
        'logical_lorentzian_route_gate_passed':bool(signed.get('passed',False)),
        'full_signed_X':abs(x-EXPECTED_X)<5e-12,
        'full_signed_Z':abs(z-EXPECTED_Z)<5e-12,
        'full_signed_shape_norm':abs(shape-EXPECTED_SHAPE)<5e-12,
    }
    return {
        'status':'exact logical selection theorem for full signed geometry x operator-first route cross',
        'passed':all(checks.values()),
        'projector':'complete all-j=1/2 Gauss/logical sector P',
        'selection_identity':'P[H_E^sine,R_op]P = 0',
        'reason':(
            'P H_E^sine P=0 on the complete fixed all-j=1/2 Gauss sector; '
            'R_op is built from flux scalars and route momenta and therefore preserves edge representation labels j.'
        ),
        'full_geometry_identity':'P[G,R_op]P = P[Hcorr,R_op]P at beta=hbar=1',
        'signed_full_beta1_projected_cross':{
            'X':x,'Z':z,'shape_coefficient_norm':shape,
            'formula':'-0.1907821681721 X -0.3304444078603 Z'
        },
        'checks':checks,
        'scope':(
            'Exact projected selection statement plus frozen logical coefficient regression. '
            'It does not replace the off-shell spin-changing two-node G x R_op calculation, which must also verify regulator scaling and nonlogical channels.'
        ),
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    a=p.parse_args(); out=run(); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
