#!/usr/bin/env python3
"""Cross-check BCQG v1.1 human/machine ledgers against frozen evidence.

The gate intentionally checks numerical/status anchors rather than brittle prose.
It distinguishes tested finite evidence, conditional closure statements, and open
finite falsifiers.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/'THEORY_STATUS.md'
CANDIDATE=ROOT/'BCQG_CANDIDATE_THEORY_V1_1.md'
CORE=ROOT/'BCQG_CORE_CANDIDATE_V1.md'
START=ROOT/'START_HERE.md'
LEDGER=ROOT/'theory_gates.json'
LOR_EVIDENCE=ROOT/'verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json'
SINE_EVIDENCE=ROOT/'verification_results/PETER_WEYL_TWO_NODE_SINE_HDA.json'
SIGN_EVIDENCE=ROOT/'verification_results/LORENTZIAN_REPO_SIGN.json'
ROUTE_SPIN=ROOT/'verification_results/PETER_WEYL_OPERATOR_ROUTE_SPINCHANGED_BLOCKS.json'
LOR_MULTI=ROOT/'verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_WALSH_NODE012.json'

DELTA_ANISO=2.738458660882762
RETIRED_DELTA=3.6832250321658044
RAW_Y=1.3389293521464034
SINE_ENDPOINT=0.020030338775070305
SINE_PCROSS=1.0056948923496356
SINE_PGG=2.007490390559045
SINE_PJOINT=1.0076444430189475
SINE_RUN=31855735615
SINE_DIGEST='sha256:21e2da508fd583d9007a5bd400d074e8cee39990656e6c75e5968d2601323526'
ROUTE_SPIN_RUN=31858615323
ROUTE_SPIN_DIGEST='sha256:c1af8de00183fddf328f6bdfba386e2320b842e10d3de98d90ad150b0876213c'


def find_gate(gates,gid):
    x=[g for g in gates if g.get('id')==gid]
    if len(x)!=1:
        raise RuntimeError(f'expected one {gid}, got {len(x)}')
    return x[0]


def main():
    status=STATUS.read_text(encoding='utf-8')
    candidate=CANDIDATE.read_text(encoding='utf-8')
    core_text=CORE.read_text(encoding='utf-8')
    start=START.read_text(encoding='utf-8')
    ledger_text=LEDGER.read_text(encoding='utf-8')
    ledger=json.loads(ledger_text)
    lor=json.loads(LOR_EVIDENCE.read_text(encoding='utf-8'))
    sine=json.loads(SINE_EVIDENCE.read_text(encoding='utf-8'))
    sign=json.loads(SIGN_EVIDENCE.read_text(encoding='utf-8'))
    route_spin=json.loads(ROUTE_SPIN.read_text(encoding='utf-8'))
    multi=json.loads(LOR_MULTI.read_text(encoding='utf-8'))
    gates=ledger['gates']

    ids={g['id'] for g in gates}
    pw=find_gate(gates,'PWLOGANISO')
    lamp=find_gate(gates,'LORAMPRAW')
    lmulti=find_gate(gates,'LOR_MULTI')
    phase=find_gate(gates,'LORPHASE')
    eunorm=find_gate(gates,'EUNORM')
    lnorm=find_gate(gates,'LORNORM')
    lroute=find_gate(gates,'LOR_ROUTE_X')
    order=find_gate(gates,'LORORDER')
    route=find_gate(gates,'ROUTE_OP')
    sgate=find_gate(gates,'E2NODE_SINE')
    fullhda=find_gate(gates,'FULLHDA_OP')
    joint=find_gate(gates,'JOINTDIAG')
    core=find_gate(gates,'CORECERT')

    y=lor['onebody_Y_coefficient_raw']
    yabs=math.hypot(float(y[0]),float(y[1]))
    spin_exponents=[float(x['epsilon_exponent']) for x in route_spin['sector_summary']]
    spin_endpoints=[float(x['endpoint']) for x in route_spin['sector_summary']]
    multi_norms=multi['group_norms']

    checks={
        'required_gate_ids_present':{'ROUTE_OP','E2NODE_SINE','FULLHDA_OP','LORAMPRAW','LOR_MULTI','LORNORM','LORORDER','CORECERT'}<=ids,
        'canonical_statuses':(
            pw['status']=='tested_finite' and lamp['status']=='tested_finite' and
            lmulti['status']=='tested_finite' and phase['status']=='conditional' and
            eunorm['status']=='conditional' and lnorm['status']=='conditional' and
            lroute['status']=='tested_finite' and order['status']=='open' and
            route['status']=='tested_finite' and sgate['status']=='tested_finite' and
            fullhda['status']=='conditional' and joint['status']=='conditional' and
            core['status']=='conditional'
        ),

        'anisotropy_machine':str(DELTA_ANISO) in pw['claim'],
        'retired_delta_absent_from_machine':str(RETIRED_DELTA) not in ledger_text,
        'legacy_core_marks_retired_delta':str(RETIRED_DELTA) in core_text and 'retired' in core_text.lower(),

        'raw_lorentzian_passed':bool(lor.get('passed',False)),
        'raw_lorentzian_decision':lor.get('decision')=='NONZERO_TRUE_ONE_BODY_RAW_Y',
        'raw_lorentzian_y':abs(yabs-RAW_Y)<1e-12,
        'raw_lorentzian_covariance':float(lor['T132_covariance_relative_error'])<1e-12,
        'raw_lorentzian_leakage':float(lor['max_physical_basis_volume_leakage'])<1e-12,
        'raw_lorentzian_human':str(RAW_Y) in status and str(RAW_Y) in candidate,

        'phase_machine':'five Poisson brackets' in phase['claim'] and '(1/i)^5=-i' in phase['claim'],
        'phase_human':'(1/i)^5=-i' in status and '(1/i)^5=-i' in candidate,

        'sine_evidence_passed':bool(sine.get('passed',False)),
        'sine_endpoint':abs(float(sine['last_joint_defect_over_D'])-SINE_ENDPOINT)<1e-15,
        'sine_pcross':abs(float(sine['fitted_cross_exponent'])-SINE_PCROSS)<1e-14,
        'sine_pgg':abs(float(sine['fitted_pure_GG_relative_exponent'])-SINE_PGG)<1e-14,
        'sine_pjoint':abs(float(sine['fitted_joint_exponent'])-SINE_PJOINT)<1e-14,
        'sine_provenance':int(sine['provenance']['workflow_run_id'])==SINE_RUN and sine['provenance']['artifact_digest']==SINE_DIGEST,
        'sine_human':str(SINE_ENDPOINT) in status and str(SINE_ENDPOINT) in candidate and str(SINE_ENDPOINT) in start,

        'signed_evidence_passed':bool(sign.get('passed',False)),
        'signed_evidence_no_fit':sign.get('fitting_used') is False,
        'signed_evidence_full':abs(float(sign['Hcorr_over_Hphase'])+32/9)<1e-14,
        'signed_evidence_bare':abs(float(sign['bare_HL_over_Hphase'])+16/9)<1e-14,
        'signed_evidence_raw':abs(complex(*sign['Hcorr_over_Lraw'])-32j/9)<1e-14,
        'signed_machine_full':'Hcorr/Hphase=-32/(9 hbar^7)' in lnorm['claim'],
        'signed_machine_raw':'G_v=(-2/3)E_raw+(32 i/9)L_raw' in lnorm['claim'],

        'spinchanged_route_passed':bool(route_spin.get('passed',False)),
        'spinchanged_route_provenance':int(route_spin['provenance']['workflow_run_id'])==ROUTE_SPIN_RUN and route_spin['provenance']['artifact_digest']==ROUTE_SPIN_DIGEST,
        'spinchanged_route_count':int(route_spin['checked_distinct_higher_spin_sectors'])>=5,
        'spinchanged_route_scaling':min(spin_exponents)>0.99 and max(spin_exponents)<1.01,
        'spinchanged_route_endpoints':max(spin_endpoints)<5e-6,
        'spinchanged_route_machine':'five genuine H_E^sine-reached higher-spin sectors' in route['claim'],

        'fullhda_machine_signed':'G_v=(-2/3)E_sine,v+(32 i/9)L_raw,v' in fullhda['claim'],
        'fullhda_machine_scaling':'Delta_full=Delta_R,op+O(epsilon)+O(epsilon^2)->0' in fullhda['claim'],
        'fullhda_human':('Delta_{full}' in status and 'Delta_{R,op}' in status and 'FULL_OPERATOR_FIRST_HDA_CERTIFICATE.md' in start),

        'multi_passed':bool(multi.get('passed',False)),
        'multi_24_terms':int(multi.get('triple_count',0))==24,
        'multi_reconstruction':max(map(float,multi['reconstruction_errors']))<2e-16,
        'multi_leakage':float(multi['max_leakage'])<1e-12,
        'multi_local_norm':abs(float(multi_norms['onebody_local'])-0.33709171624286727)<1e-14,
        'multi_threebody_norm':abs(float(multi_norms['source_x_node1node2'])-0.01396705295732858)<1e-14,
        'multi_machine_scope':'off-diagonal environment transitions remain unmeasured' in lmulti['claim'],
        'multi_human':'0.01396705295732858' in status and 'Prediction J' in candidate and 'LORENTZIAN_MULTI_NODE_ENVIRONMENT_CORRELATION.md' in start,

        'finite_falsifier_remains_open':'finite' in order['claim'].lower() and 'timeout' in order['claim'].lower(),
        'joint_path_human':('epsilon^-1/8' in start or 'epsilon^{-1/8}' in status or 'epsilon^{-1/8}' in candidate),
        'candidate_v11_named':('BCQG Candidate Theory v1.1' in status and 'BCQG Candidate Theory v1.1' in candidate and 'BCQG Candidate Theory v1.1' in start),
    }

    out={
        'status':'BCQG v1.1 canonical human/machine/evidence consistency',
        'passed':all(checks.values()),
        'anchors':{
            'Lorentzian_raw_Y_abs':RAW_Y,
            'physical_sine_joint_endpoint':SINE_ENDPOINT,
            'signed_full_beta1_Hcorr_over_Hphase':-32/9,
            'signed_bare_beta1_HL_over_Hphase':-16/9,
            'spinchanged_route_max_endpoint':max(spin_endpoints),
            'multi_node1_norm':float(multi_norms['source_x_node1']),
            'multi_threebody_diagonal_norm':float(multi_norms['source_x_node1node2']),
            'joint_cutoff_alpha':'1/8',
        },
        'checks':checks,
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
