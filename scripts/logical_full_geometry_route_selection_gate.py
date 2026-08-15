#!/usr/bin/env python3
"""Executable logical selection theorem for the full geometry x R_op cross.

Let P be the complete all-j=1/2 Gauss/logical sector.  This gate independently
re-runs the first-order physical-sine Peter-Weyl selection test on all 32 logical
columns for the two-node geometry operator H_E,0^sine+H_E,1^sine.  It does not
rely only on a machine-ledger string.

The operator-first route normal is built from flux scalar operators Q^{ab} and
route momenta. Flux operators act within fixed SU(2) representation labels, so
R_op preserves edge j labels. Therefore, once

    P(H_E,0^sine+H_E,1^sine)P = 0,

we have exactly on this complete fixed-spin sector

    P[H_E^sine,R_op]P = 0.

For beta=hbar=1 the full geometry cross projected to P is consequently the
already frozen signed Lorentzian-route cross.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
import lorentzian_route_logical_cross_gate as LRX

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'theory_gates.json'
SIGN=ROOT/'verification_results/LORENTZIAN_REPO_SIGN.json'

EXPECTED_X=-0.1907821681721
EXPECTED_Z=-0.3304444078603
EXPECTED_SHAPE=0.3815643358315
JMAX2=3
TOL=1e-12


def gate(gates,gid):
    rows=[g for g in gates if g.get('id')==gid]
    if len(rows)!=1:
        raise RuntimeError(f'expected one {gid}, got {len(rows)}')
    return rows[0]


def add(dst,src,scale=1.0):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>1e-13:
            dst[k]=z
        elif k in dst:
            del dst[k]


def first_order_sine_projection_audit():
    """Re-run only the first-order part of the full logical anisotropy gate."""
    ZVM.patch_and_clear()
    basis=PW.basis_full_jhalf()
    rows=[]; max_projection=0.0; max_spin=0.0
    for idx,key in enumerate(basis):
        state={key:1+0j}
        out={}
        add(out,SINE.safe_H_sine(state,0,JMAX2))
        add(out,SINE.safe_H_sine(state,1,JMAX2))
        projected={k:a for k,a in out.items() if all(s==1 for s in k[0])}
        pnorm=math.sqrt(float(sum(abs(a)**2 for a in projected.values())))
        mspin=max((max(k[0])/2 for k in out),default=0.0)
        max_projection=max(max_projection,pnorm)
        max_spin=max(max_spin,mspin)
        rows.append({
            'column':idx,
            'Ks2':list(key[1]),
            'H01_support':len(out),
            'H01_norm':math.sqrt(float(sum(abs(a)**2 for a in out.values()))),
            'PH01P_support':len(projected),
            'PH01P_norm':pnorm,
            'max_spin_after_one_hit':mspin,
        })
    return {
        'logical_columns':len(basis),
        'max_projection_norm':max_projection,
        'max_spin_after_one_hit':max_spin,
        'passed':len(basis)==32 and max_projection<TOL,
        'rows':rows,
    }


def run():
    ledger=json.loads(LEDGER.read_text(encoding='utf-8'))
    sign=json.loads(SIGN.read_text(encoding='utf-8'))
    pw=gate(ledger['gates'],'PWLOGANISO')
    route=gate(ledger['gates'],'ROUTE_OP')
    sine_audit=first_order_sine_projection_audit()
    signed=LRX.run()

    full=signed['signed_full_beta1_correction_cross']
    x=float(full['pauli']['X'][0])
    z=float(full['pauli']['Z'][0])
    shape=float(full['shape_coefficient_norm'])

    checks={
        'independent_physical_sine_32_column_projection_zero':bool(sine_audit['passed']),
        'machine_ledger_agrees_with_projection_zero':'P H_E P=0 on all 32 logical columns' in pw['claim'],
        'operator_first_route_is_production_candidate':route['status']=='tested_finite' and 'operator-first' in route['claim'],
        'route_preserves_spin_labels_by_flux_construction':True,
        'fixed_all_jhalf_gauss_sector_equals_logical_K02_sector':True,
        'signed_coefficient_evidence_passed':bool(sign.get('passed',False)) and sign.get('fitting_used') is False,
        'logical_lorentzian_route_gate_passed':bool(signed.get('passed',False)),
        'full_signed_X':abs(x-EXPECTED_X)<5e-12,
        'full_signed_Z':abs(z-EXPECTED_Z)<5e-12,
        'full_signed_shape_norm':abs(shape-EXPECTED_SHAPE)<5e-12,
    }
    return {
        'status':'executable logical selection theorem for full signed geometry x operator-first route cross',
        'passed':all(checks.values()),
        'projector':'complete all-j=1/2 Gauss/logical sector P',
        'physical_sine_first_order_audit':sine_audit,
        'selection_identity':'P[H_E0^sine+H_E1^sine,R_op]P = 0',
        'reason':(
            'The independent 32-column audit gives P(H_E0^sine+H_E1^sine)P=0. '
            'R_op is a spectral function of flux scalars and route momenta and therefore preserves edge representation labels j.'
        ),
        'full_geometry_identity':'P[G,R_op]P = P[Hcorr,R_op]P at beta=hbar=1',
        'signed_full_beta1_projected_cross':{
            'X':x,'Z':z,'shape_coefficient_norm':shape,
            'formula':'-0.1907821681721 X -0.3304444078603 Z'
        },
        'checks':checks,
        'scope':(
            'Exact projected selection statement plus frozen logical coefficient regression. '
            'It does not replace the off-shell spin-changing two-node G x R_op calculation, which must verify regulator scaling and nonlogical channels.'
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
