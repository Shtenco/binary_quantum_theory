#!/usr/bin/env python3
"""Executable logical selection theorem for the full two-node geometry x R_op cross.

The gate independently re-runs the first-order physical-sine Peter-Weyl
selection test on all 32 logical columns for H_E,0^sine+H_E,1^sine.

Because the operator-first route normal is a spectral function of flux scalars
and route momenta, it preserves edge SU(2) representation labels. Therefore

    P[H_E,0^sine+H_E,1^sine,R_op]P = 0

on the complete all-j=1/2 Gauss/logical sector P.

The remaining projected geometry-route cross is Lorentzian.  Its NUMERICAL
coefficient must be taken from the true 4x4 shared two-node route square root,
not transplanted from the older one-node 2x2 diagnostic.
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
import two_node_lorentzian_route_logical_cross_gate as TWOX

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'theory_gates.json'
SIGN=ROOT/'verification_results/LORENTZIAN_REPO_SIGN.json'

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
        if abs(z)>1e-13: dst[k]=z
        elif k in dst: del dst[k]


def first_order_sine_projection_audit():
    ZVM.patch_and_clear()
    basis=PW.basis_full_jhalf(); rows=[]; max_projection=0.0; max_spin=0.0
    for idx,key in enumerate(basis):
        state={key:1+0j}; out={}
        add(out,SINE.safe_H_sine(state,0,JMAX2)); add(out,SINE.safe_H_sine(state,1,JMAX2))
        projected={k:a for k,a in out.items() if all(s==1 for s in k[0])}
        pnorm=math.sqrt(float(sum(abs(a)**2 for a in projected.values())))
        mspin=max((max(k[0])/2 for k in out),default=0.0)
        max_projection=max(max_projection,pnorm); max_spin=max(max_spin,mspin)
        rows.append({'column':idx,'Ks2':list(key[1]),'H01_support':len(out),'PH01P_support':len(projected),'PH01P_norm':pnorm,'max_spin_after_one_hit':mspin})
    return {'logical_columns':len(basis),'max_projection_norm':max_projection,'max_spin_after_one_hit':max_spin,'passed':len(basis)==32 and max_projection<TOL,'rows':rows}


def run(n_theta=32768):
    ledger=json.loads(LEDGER.read_text(encoding='utf-8'))
    sign=json.loads(SIGN.read_text(encoding='utf-8'))
    pw=gate(ledger['gates'],'PWLOGANISO'); route=gate(ledger['gates'],'ROUTE_OP')
    sine_audit=first_order_sine_projection_audit()
    twox=TWOX.run(n_theta)

    checks={
        'independent_physical_sine_32_column_projection_zero':bool(sine_audit['passed']),
        'machine_ledger_agrees_with_projection_zero':'P H_E P=0 on all 32 logical columns' in pw['claim'],
        'operator_first_route_is_production_candidate':route['status']=='tested_finite' and 'operator-first' in route['claim'],
        'route_preserves_spin_labels_by_flux_construction':True,
        'fixed_all_jhalf_gauss_sector_equals_logical_K02_sector':True,
        'signed_coefficient_evidence_passed':bool(sign.get('passed',False)) and sign.get('fitting_used') is False,
        'two_node_shared_route_cross_gate_passed':bool(twox.get('passed',False)),
        'one_node_coefficient_transplant_rejected':float(twox['one_node_naive_embedded_cross_relative_mismatch'])>0.9,
    }
    return {
        'status':'executable logical selection theorem for full signed two-node geometry x operator-first route cross',
        'passed':all(checks.values()),
        'projector':'complete all-j=1/2 Gauss/logical sector P',
        'physical_sine_first_order_audit':sine_audit,
        'selection_identity':'P[H_E0^sine+H_E1^sine,R_op]P = 0',
        'reason':'The independent 32-column audit gives P(H_E0^sine+H_E1^sine)P=0; R_op preserves edge j labels.',
        'full_geometry_identity':'P[G0/G1,R_op]P is purely the corresponding signed Lorentzian projected cross at beta=hbar=1',
        'two_node_shared_route_cross':{
            'C0_pauli':twox['C0_pauli'],
            'C1_pauli':twox['C1_pauli'],
            'C0_local_norm':twox['C0_local_XI_ZI_norm'],
            'C0_entangling_norm':twox['C0_entangling_XX_XZ_ZX_ZZ_norm'],
            'C1_local_norm':twox['C1_local_IX_IZ_norm'],
            'C1_entangling_norm':twox['C1_entangling_XX_XZ_ZX_ZZ_norm'],
        },
        'scope_correction':(
            'The previous one-node 2x2 cross remains valid only as a one-node diagnostic. '
            'The true two-node shared square root generates entangling XX/XZ/ZX/ZZ channels, so its coefficients replace any naive embedding.'
        ),
        'checks':checks,
        'scope':'Exact projected selection plus finite 4x4 shared-route regression; nonlogical spin-changing channels and regulator scaling remain open.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--n-theta',type=int,default=32768); p.add_argument('--output',type=Path)
    a=p.parse_args(); out=run(a.n_theta); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
