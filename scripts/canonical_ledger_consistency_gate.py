#!/usr/bin/env python3
"""Cross-check canonical human/machine ledgers against frozen evidence.

High-value anchors:
- corrected Euclidean return anisotropy;
- exact Lorentzian raw Y amplitude;
- five-bracket phase;
- preregistered physical H_E^sine two-node HDA PASS;
- operator-first quantum route selection;
- Euclidean normalization;
- CI-verified signed Lorentzian relative coefficient;
- explicit alpha=1/8 joint-cutoff path.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/'THEORY_STATUS.md'
CANDIDATE=ROOT/'BCQG_CORE_CANDIDATE_V1.md'
START=ROOT/'START_HERE.md'
LEDGER=ROOT/'theory_gates.json'
LOR_EVIDENCE=ROOT/'verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json'
SINE_EVIDENCE=ROOT/'verification_results/PETER_WEYL_TWO_NODE_SINE_HDA.json'
SIGN_EVIDENCE=ROOT/'verification_results/LORENTZIAN_REPO_SIGN.json'

DELTA_ANISO=2.738458660882762
RETIRED_DELTA=3.6832250321658044
RAW_Y=1.3389293521464034
SINE_ENDPOINT=0.020030338775070305
SINE_PCROSS=1.0056948923496356
SINE_PGG=2.007490390559045
SINE_PJOINT=1.0076444430189475
SINE_RUN=31855735615
SINE_DIGEST='sha256:21e2da508fd583d9007a5bd400d074e8cee39990656e6c75e5968d2601323526'
SIGN_RUN=31857722477
SIGN_DIGEST='sha256:10f538abd68dc8945a46ec03410b5e4490a5d8e1fbbb05d56a10a56fd6220101'


def find_gate(gates,gid):
    x=[g for g in gates if g.get('id')==gid]
    if len(x)!=1:
        raise RuntimeError(f'expected one {gid}, got {len(x)}')
    return x[0]


def main():
    status=STATUS.read_text(encoding='utf-8')
    candidate=CANDIDATE.read_text(encoding='utf-8')
    start=START.read_text(encoding='utf-8')
    ledger_text=LEDGER.read_text(encoding='utf-8')
    ledger=json.loads(ledger_text)
    lor=json.loads(LOR_EVIDENCE.read_text(encoding='utf-8'))
    sine=json.loads(SINE_EVIDENCE.read_text(encoding='utf-8'))
    sign=json.loads(SIGN_EVIDENCE.read_text(encoding='utf-8'))
    gates=ledger['gates']

    pw=find_gate(gates,'PWLOGANISO')
    lamp=find_gate(gates,'LORAMPRAW')
    phase=find_gate(gates,'LORPHASE')
    eunorm=find_gate(gates,'EUNORM')
    lnorm=find_gate(gates,'LORNORM')
    lroute=find_gate(gates,'LOR_ROUTE_X')
    order=find_gate(gates,'LORORDER')
    route=find_gate(gates,'ROUTE_OP')
    sgate=find_gate(gates,'E2NODE_SINE')
    joint=find_gate(gates,'JOINTDIAG')
    core=find_gate(gates,'CORECERT')

    y=lor['onebody_Y_coefficient_raw']
    yabs=math.hypot(float(y[0]),float(y[1]))

    checks={
        'canonical_statuses':(
            pw['status']=='tested_finite' and lamp['status']=='tested_finite' and
            phase['status']=='conditional' and eunorm['status']=='conditional' and
            lnorm['status']=='conditional' and lroute['status']=='tested_finite' and
            order['status']=='open' and route['status']=='tested_finite' and
            sgate['status']=='tested_finite' and joint['status']=='conditional' and
            core['status']=='conditional'
        ),
        'anisotropy_machine':str(DELTA_ANISO) in pw['claim'],
        'retired_delta_absent_from_machine':str(RETIRED_DELTA) not in ledger_text,
        'anisotropy_human':all(str(DELTA_ANISO) in x for x in (status,candidate,start)),
        'retired_delta_marked':all(str(RETIRED_DELTA) in x and 'retired' in x.lower() for x in (status,candidate,start)),

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
        'sine_human':all(str(SINE_ENDPOINT) in x for x in (status,candidate,start)),

        'signed_evidence_passed':bool(sign.get('passed',False)),
        'signed_evidence_no_fit':sign.get('fitting_used') is False,
        'signed_evidence_full':abs(float(sign['Hcorr_over_Hphase'])+32/9)<1e-14,
        'signed_evidence_bare':abs(float(sign['bare_HL_over_Hphase'])+16/9)<1e-14,
        'signed_evidence_raw':abs(complex(*sign['Hcorr_over_Lraw'])-32j/9)<1e-14,
        'signed_provenance':int(sign['provenance']['workflow_run_id'])==SIGN_RUN and sign['provenance']['artifact_digest']==SIGN_DIGEST,
        'signed_machine_full':'Hcorr/Hphase=-32/(9 hbar^7)' in lnorm['claim'],
        'signed_machine_bare':'bare H_L/Hphase=-16/(9 hbar^7)' in lnorm['claim'],
        'signed_machine_raw':'G_v=(-2/3)E_raw+(32 i/9)L_raw' in lnorm['claim'],
        'sign_no_longer_open_machine':'relative sign are fixed upstream' in order['claim'],
        'sign_no_longer_open_human':(
            'relative sign is no longer open' in status.lower() and
            'neither lorentzian magnitude nor relative sign is an hda tuning parameter' in candidate.lower() and
            'relative lorentzian sign and magnitude are no longer open tuning parameters' in start.lower()
        ),

        'signed_route_cross_machine':'-0.1907821681721 X-0.3304444078603 Z' in lroute['claim'],
        'signed_route_cross_human':'-0.1907821681721' in status and '-0.3304444078603' in status,

        'operator_first_human':('R_{op}' in status and 'R_{op}' in candidate and 'R_op' in start),
        'joint_path_human':(('epsilon^-1/8' in status or 'epsilon^{-1/8}' in status) and ('epsilon^-1/8' in start or 'epsilon^{-1/8}' in start)),
        'full_frontier_human':('H_E^{sine}' in status and 'H_L' in status and 'R_{op}' in status and 'H_E^{sine}' in candidate and 'R_{op}' in candidate),
    }

    out={
        'status':'canonical human/machine/evidence consistency',
        'passed':all(checks.values()),
        'anchors':{
            'Delta_aniso_ret':DELTA_ANISO,
            'Lorentzian_raw_Y_abs':RAW_Y,
            'physical_sine_joint_endpoint':SINE_ENDPOINT,
            'signed_full_beta1_Hcorr_over_Hphase':-32/9,
            'signed_bare_beta1_HL_over_Hphase':-16/9,
            'signed_full_beta1_Hcorr_over_Lraw':'32 i/9',
            'joint_cutoff_alpha':'1/8',
        },
        'checks':checks,
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
