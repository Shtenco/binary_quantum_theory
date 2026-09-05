#!/usr/bin/env python3
"""Fail-closed truth verifier for the q=2 scalar/background frontier.

GREEN means the projected-source/history seam and every deterministic downstream
measurement/consumer layer are closed while the actual theory-specific physical
inputs remain open:
  physical projector/history,
  W_phys[J_Q,J_zeta;tau,r],
  Gamma_FLRW[a,N].
It never means DM, DE, Phi/Psi, mu/Sigma or the BQG scalar kernel were derived.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'q2_scalar_frontier.json'
PARENT=ROOT/'physicalization_gates.json'

ALLOWED={
    'positive_control':{'tested_finite'},
    'physical':{'open_physical','frozen'},
}
REQUIRED_LOCAL={'Q2_LOCAL_SHAPE_1PI','Q2_COLLECTIVE_CONFORMAL_VOLUME_CARRIER'}
FROZEN_PHYSICAL={
    'PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING',
    'SCALAR_PROJECTED_SOURCE_HISTORY_BRIDGE',
    'SCALAR_PHYSICAL_W_HISTORY_MEASUREMENT_PIPELINE',
    'SCALAR_CONNECTED_HISTORY_TO_RESPONSE_PIPELINE',
    'FLRW_HISTORY_EFFECTIVE_ACTION_RESPONSE_PIPELINE',
}
OPEN_PHYSICAL={
    'PHYSICAL_VOLUME_HISTORY_SOURCE',
    'PHYSICAL_LAPSE_RESPONSE_SOURCE',
    'PHYSICAL_SCALAR_GAUGE_REDUCTION',
    'CONNECTED_SCALAR_INTERBLOCK_HISTORY',
    'PHYSICAL_BQG_SCALAR_KERNEL',
}
REQUIRED_PHYSICAL=OPEN_PHYSICAL|FROZEN_PHYSICAL
PARENT_MUST_REMAIN_OPEN={
    'PHYSICAL_PROJECTOR_HISTORY',
    'CONNECTED_INTERBLOCK_HISTORY',
    'PHYSICAL_BACKGROUND_COSMOLOGY',
    'PHYSICAL_SCALAR_COSMOLOGY',
    'LENSING_DYNAMICS_CLOSURE',
}


def load(path:Path,errors:list[str])->dict:
    try:
        x=json.loads(path.read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as exc:
        errors.append(f'{path.name}: {exc}'); return {}
    if not isinstance(x,dict): errors.append(f'{path.name}: root must be object'); return {}
    return x


def safe_path(s:str)->bool:
    p=PurePosixPath(s)
    return bool(s) and not p.is_absolute() and '..' not in p.parts


def evidence_set(row:dict)->set[str]:
    x=row.get('evidence',[])
    return set(x) if isinstance(x,list) else set()


def require_phrases(text:str,phrases:list[str],label:str,errors:list[str])->None:
    low=text.lower()
    for p in phrases:
        if p.lower() not in low: errors.append(f'{label} missing boundary phrase: {p}')


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path); args=ap.parse_args()
    errors:list[str]=[]
    data=load(LEDGER,errors); parent=load(PARENT,errors)
    if data.get('schema_version')!=1: errors.append('q2 scalar schema_version must equal 1')
    if data.get('parent_physicalization_ledger')!='physicalization_gates.json': errors.append('parent ledger path mismatch')

    gates=data.get('gates',[])
    if not isinstance(gates,list): errors.append('gates must be list'); gates=[]
    rows={}
    for i,g in enumerate(gates):
        if not isinstance(g,dict): errors.append(f'gate[{i}] must be object'); continue
        gid=g.get('id'); role=g.get('closure_role'); status=g.get('status')
        if not isinstance(gid,str) or not gid: errors.append(f'gate[{i}] invalid id'); continue
        if gid in rows: errors.append(f'duplicate gate id {gid}'); continue
        rows[gid]=g
        if role not in ALLOWED: errors.append(f'{gid}: invalid role {role!r}')
        elif status not in ALLOWED[role]: errors.append(f'{gid}: illegal status {status!r} for {role}')
        for key in ('claim','hard_scope'):
            if not isinstance(g.get(key),str) or not g[key].strip(): errors.append(f'{gid}: missing {key}')
        ev=g.get('evidence',[])
        if not isinstance(ev,list) or not ev: errors.append(f'{gid}: evidence must be nonempty list'); ev=[]
        for rel in ev:
            if not isinstance(rel,str) or not safe_path(rel): errors.append(f'{gid}: unsafe evidence {rel!r}')
            elif not (ROOT/rel).is_file(): errors.append(f'{gid}: missing evidence {rel}')

    if not REQUIRED_LOCAL<=set(rows): errors.append(f'missing local gates {sorted(REQUIRED_LOCAL-set(rows))}')
    if not REQUIRED_PHYSICAL<=set(rows): errors.append(f'missing physical gates {sorted(REQUIRED_PHYSICAL-set(rows))}')
    for gid in REQUIRED_LOCAL&set(rows):
        if rows[gid].get('status')!='tested_finite' or rows[gid].get('closure_role')!='positive_control':
            errors.append(f'{gid}: local result must remain tested_finite positive_control')
    for gid in OPEN_PHYSICAL&set(rows):
        if rows[gid].get('status')!='open_physical' or rows[gid].get('closure_role')!='physical':
            errors.append(f'{gid}: unresolved physical gate must remain open_physical')
    for gid in FROZEN_PHYSICAL&set(rows):
        if rows[gid].get('status')!='frozen' or rows[gid].get('closure_role')!='physical':
            errors.append(f'{gid}: frozen interface/pipeline status mismatch')

    outputs=data.get('current_outputs',{})
    expected_open=('rho_hist_a','Phi_a_k','Psi_a_k','mu_BQG_a_k','Sigma_BQG_a_k')
    for key in expected_open:
        if outputs.get(key)!='OPEN_PHYSICAL': errors.append(f'{key}: must remain OPEN_PHYSICAL')
    expected_frozen={
        'conserved_external_probe_interface':'FROZEN_UNIVERSAL_CONVENTION',
        'scalar_projected_source_history_bridge':'FROZEN_PROJECTED_SOURCE_TO_W_HISTORY_SEAM',
        'scalar_physical_W_history_measurement_pipeline':'FROZEN_W_TO_GCONN',
        'scalar_connected_history_consumer_pipeline':'FROZEN_GCONN_TO_RESPONSE',
        'flrw_history_effective_action_response_pipeline':'FROZEN_GAMMA_FLRW_TO_RHO_P_W',
    }
    for key,val in expected_frozen.items():
        if outputs.get(key)!=val: errors.append(f'{key}: expected {val}')
    expected_cumulants=['G_QQ(omega,k)','G_Qzeta(omega,k)','G_zetazeta(omega,k)']
    if outputs.get('remaining_scalar_microscopic_inputs')!=expected_cumulants:
        errors.append('remaining scalar microscopic outputs must be exactly the three connected Ward cumulants')
    if outputs.get('upstream_projector_history_input')!='OPEN_PHYSICAL_PROJECTOR_HISTORY':
        errors.append('upstream projector/history input must remain OPEN_PHYSICAL_PROJECTOR_HISTORY')
    if outputs.get('upstream_scalar_history_input')!='OPEN_PHYSICAL_W_phys[J_Q,J_zeta;tau,r]':
        errors.append('upstream scalar input must remain source-dressed W_phys')
    if outputs.get('upstream_background_input')!='OPEN_PHYSICAL_Gamma_FLRW[a,N]':
        errors.append('upstream background input must remain theory-specific Gamma_FLRW')
    if outputs.get('scalar_ADM_log_volume_seed_K_zetaV_zetaV')!='18_EXACT_KINEMATIC_POSITIVE_CONTROL':
        errors.append('exact scalar ADM zeta_V seed must remain 18 kinematic positive control')
    if outputs.get('flat_scalar_Ward_parameter_count')!=3: errors.append('flat Ward quotient must have exactly three functions')
    if outputs.get('flat_scalar_Ward_quotient')!='EXACT_TWO_GAUGE_INVARIANTS_THREE_KERNEL_FUNCTIONS':
        errors.append('flat scalar Ward quotient status mismatch')

    pgates=parent.get('gates',[]) if isinstance(parent.get('gates',[]),list) else []
    prows={g.get('id'):g for g in pgates if isinstance(g,dict) and isinstance(g.get('id'),str)}
    for gid in PARENT_MUST_REMAIN_OPEN:
        if prows.get(gid,{}).get('status')!='open_physical': errors.append(f'parent {gid} must remain open_physical')

    source=rows.get('PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING',{})
    if not {'CONSERVED_SCALAR_PROBE_CONVENTION.md','scripts/conserved_scalar_probe_convention_gate.py'}<=evidence_set(source):
        errors.append('frozen conserved probe missing dedicated evidence')
    require_phrases(source.get('hard_scope',''),['does not derive','matter sector','common physical scale'],'conserved probe hard_scope',errors)

    bridge=rows.get('SCALAR_PROJECTED_SOURCE_HISTORY_BRIDGE',{})
    if not {
        'PROJECTED_SOURCE_PHYSICAL_HISTORY_BRIDGE.md',
        'scripts/boundary_projector_source_dressing_gate.py',
        'scripts/bqg_physical_history_adapter_gate.py',
        'scripts/near_zero_rigging_limit_gate.py',
        'scripts/projected_source_history_bridge_gate.py',
        '.github/workflows/scalar-projected-source-history-bridge.yml',
    }<=evidence_set(bridge): errors.append('frozen projected-source history bridge missing dedicated evidence')
    require_phrases(bridge.get('hard_scope',''),['does not generate','physical projector/history','heat tau','physical omega','static equal-history covariance'],'projected-source history bridge hard_scope',errors)

    gauge=rows.get('PHYSICAL_SCALAR_GAUGE_REDUCTION',{})
    if not {'SCALAR_ADM_DIRAC_REDUCTION.md','scripts/scalar_adm_dirac_response_gate.py','SCALAR_ADM_WARD_QUOTIENT.md','scripts/scalar_adm_ward_basis_gate.py'}<=evidence_set(gauge):
        errors.append('scalar gauge-reduction gate missing exact Dirac/Ward evidence')
    if 'flrw' not in gauge.get('hard_scope','').lower() or 'three functions' not in gauge.get('claim','').lower():
        errors.append('scalar gauge boundary must separate exact flat three-function quotient from open FLRW reduction')

    measure=rows.get('SCALAR_PHYSICAL_W_HISTORY_MEASUREMENT_PIPELINE',{})
    if not {
        'PHYSICAL_SCALAR_W_HISTORY_MEASUREMENT.md',
        'scripts/scalar_physical_history_cumulant_gate.py',
        'scripts/scalar_connected_history_numeric_inversion_gate.py',
        '.github/workflows/scalar-physical-history-measurement.yml',
    }<=evidence_set(measure): errors.append('frozen W-history measurement pipeline missing dedicated evidence')
    require_phrases(measure.get('hard_scope',''),['does not generate','raw Z','pseudoinverse'],'W-history measurement hard_scope',errors)
    mscope=measure.get('hard_scope','').lower()
    if 'does not infer' not in mscope or 'sampled mode' not in mscope:
        errors.append('W-history measurement hard_scope must forbid pole inference from an isolated sampled mode')

    pipe=rows.get('SCALAR_CONNECTED_HISTORY_TO_RESPONSE_PIPELINE',{})
    if not {
        'CONNECTED_SCALAR_HISTORY_EXTRACTION.md','SCALAR_WARD_KERNEL_RESPONSE.md',
        'scripts/scalar_connected_history_extractor_gate.py','scripts/scalar_connected_history_to_response_gate.py',
        'scripts/scalar_ward_kernel_response_gate.py','.github/workflows/scalar-connected-history-closure.yml',
    }<=evidence_set(pipe): errors.append('frozen connected-history consumer missing end-to-end evidence')
    require_phrases(pipe.get('hard_scope',''),['does not compute','pseudoinverse','physical omega','synthetic'],'connected-history hard_scope',errors)

    flrw=rows.get('FLRW_HISTORY_EFFECTIVE_ACTION_RESPONSE_PIPELINE',{})
    if not {
        'FLRW_HISTORY_EFFECTIVE_ACTION_RESPONSE.md','scripts/flrw_history_effective_action_gate.py',
        'scripts/physical_cosmology_background_scalar_gate.py','.github/workflows/flrw-history-effective-action-response.yml',
    }<=evidence_set(flrw): errors.append('frozen FLRW response pipeline missing dedicated evidence')
    require_phrases(flrw.get('hard_scope',''),['does not generate','W(0)=0','dark energy'],'FLRW response hard_scope',errors)

    hist=rows.get('CONNECTED_SCALAR_INTERBLOCK_HISTORY',{})
    for token in ('W_phys','G_QQ','G_Qzeta','G_zetazeta'):
        if token not in hist.get('claim',''): errors.append(f'connected scalar history claim must name {token}')

    closed={
        'flat_Ward_parameter_count':outputs.get('flat_scalar_Ward_parameter_count'),
        'log_volume_seed':outputs.get('scalar_ADM_log_volume_seed_K_zetaV_zetaV'),
        'projected_source_history_bridge':outputs.get('scalar_projected_source_history_bridge'),
        'W_history_measurement':outputs.get('scalar_physical_W_history_measurement_pipeline'),
        'connected_history_consumer':outputs.get('scalar_connected_history_consumer_pipeline'),
        'FLRW_response_consumer':outputs.get('flrw_history_effective_action_response_pipeline'),
    }
    remaining={
        'projector_history':outputs.get('upstream_projector_history_input'),
        'scalar':outputs.get('upstream_scalar_history_input'),
        'background':outputs.get('upstream_background_input'),
        'scalar_connected_outputs':outputs.get('remaining_scalar_microscopic_inputs'),
    }
    exact_alias={
        'flat_Ward_parameter_count':outputs.get('flat_scalar_Ward_parameter_count'),
        'connected_history_consumer_pipeline':outputs.get('scalar_connected_history_consumer_pipeline'),
        'remaining_microscopic_inputs':outputs.get('remaining_scalar_microscopic_inputs'),
    }
    result={
        'schema_version':data.get('schema_version'),
        'valid':not errors,
        'gate_count':len(gates),
        'local_positive_controls':{gid:rows.get(gid,{}).get('status') for gid in sorted(REQUIRED_LOCAL)},
        'closed_downstream_machinery':closed,
        'remaining_physical_inputs':remaining,
        'exact_scalar_algebra':exact_alias,
        'frozen_scalar_interfaces':{gid:rows.get(gid,{}).get('status') for gid in sorted(FROZEN_PHYSICAL)},
        'open_scalar_physical_gates':{gid:rows.get(gid,{}).get('status') for gid in sorted(OPEN_PHYSICAL)},
        'required_scalar_physical_gates':{gid:rows.get(gid,{}).get('status') for gid in sorted(REQUIRED_PHYSICAL)},
        'parent_open_guards':{gid:prows.get(gid,{}).get('status') for gid in sorted(PARENT_MUST_REMAIN_OPEN)},
        'cosmology_outputs':{key:outputs.get(key) for key in expected_open},
        'scientific_interpretation':'GREEN means the projected-source/history seam and all deterministic downstream scalar/background machinery are closed. The actual BQG physical projector/history, W_phys and Gamma_FLRW remain missing; all dark-sector outputs stay open.',
        'errors':errors,
    }
    txt=json.dumps(result,indent=2); print(txt)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if not errors else 1

if __name__=='__main__': raise SystemExit(main())
