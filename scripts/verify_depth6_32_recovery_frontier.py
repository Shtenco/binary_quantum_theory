#!/usr/bin/env python3
"""Fail-closed integrity verifier for the canonical depth-6 [3,2] recovery frontier.

Passing this verifier certifies recovery-state consistency only.  It never
certifies numerical rank closure of [3,2].  Schema 7 additionally permits a
complete deterministic assignment-identity snapshot while keeping actual-q,
replay-basis and rank gates closed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from depth6_assignment_ledger import verify_assignment_ledger
from depth6_replay_readiness import assess_records
from depth6_32_rematerialized_identity import verify_snapshot

EXPECTED_SHARDS=[0,6,8,11,12,13,14,17,18,19,20,21,22,23,24]
ASSIGNMENT_LEDGER='BQG_DEPTH6_32_ASSIGNMENT_LEDGER_2026-10-02.json'
STAGEA_SALVAGE='BQG_DEPTH6_32_STAGEA_LOG_SALVAGE_2026-10-02.json'
REQUIRED_FILES=(
    'scripts/depth6_keymeta_coverage.py',
    'scripts/inventory_depth6_32_keymeta.py',
    'scripts/depth6_assignment_ledger.py',
    'scripts/depth6_replay_readiness.py',
)


def _require(cond: bool,msg: str)->None:
    if not cond: raise RuntimeError(msg)


def _canonical_json_sha_without_field(payload: dict,field: str)->str:
    q=dict(payload); q.pop(field,None)
    raw=json.dumps(q,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()


def _verify_schema6_extensions(recovery:dict,root:Path,assignment:dict)->dict:
    pal=recovery.get('persisted_assignment_ledger',{})
    _require(pal.get('path')==ASSIGNMENT_LEDGER,'schema6 persisted assignment ledger path mismatch')
    _require(pal.get('status')=='INCOMPLETE_PERSISTED_ASSIGNMENT_LEDGER','schema6 assignment status drifted')
    _require(pal.get('persisted_blocks')==15 and pal.get('persisted_columns')==7749,'schema6 assignment coverage mismatch')
    _require(pal.get('missing_blocks')==2740 and pal.get('missing_columns')==123154,'schema6 assignment missing coverage mismatch')
    _require(pal.get('retry_allowed') is False and pal.get('rank_certified') is False,'schema6 assignment boundary must remain fail-closed')
    _require(pal.get('ledger_sha256')==assignment['ledger_sha256'],'schema6 assignment ledger SHA mismatch')

    salvage_path=root/STAGEA_SALVAGE
    _require(salvage_path.is_file(),f'missing canonical Stage-A salvage: {STAGEA_SALVAGE}')
    salvage=json.loads(salvage_path.read_text())
    _require(salvage.get('kind')=='BQG_DEPTH6_32_STAGEA_LOG_SALVAGE_CANONICAL','wrong Stage-A salvage kind')
    _require(salvage.get('source_run_id')==36899125190,'wrong Stage-A source run')
    _require(salvage.get('target')==[112,2755,130903],'Stage-A salvage target drifted')
    _require(len(salvage.get('rows',[]))==112,'Stage-A salvage must contain all 112 shard identities')
    _require(salvage.get('logs_available_count')==102,'Stage-A surviving log count drifted')
    _require(salvage.get('ledger_lines_recovered')==102,'Stage-A recovered ledger-line count drifted')
    _require(salvage.get('recovered_ledger_totals')==[2530,118883],'Stage-A recovered batch totals drifted')
    _require(salvage.get('completed_lost_shards')==[5],'Stage-A completed-but-lost shard set drifted')
    _require(salvage.get('log_unavailable_shards')==[1,2,4,36,59,73,85,88,90,104],'Stage-A unavailable-log set drifted')
    _require(salvage.get('persisted_raw_shards')==EXPECTED_SHARDS,'Stage-A persisted raw shard set mismatch')
    _require(salvage.get('summary_sha256')==_canonical_json_sha_without_field(salvage,'summary_sha256'),'Stage-A canonical summary SHA mismatch')
    _require(salvage.get('structural_recompute_performed') is False,'Stage-A salvage must remain provenance-only')

    sf=recovery.get('stage_a_log_salvage',{})
    _require(sf.get('path')==STAGEA_SALVAGE,'recovery frontier Stage-A salvage path mismatch')
    _require(sf.get('salvage_run_id')==salvage.get('salvage_run_id'),'recovery frontier salvage run mismatch')
    _require(sf.get('salvage_artifact_id')==salvage.get('salvage_artifact_id'),'recovery frontier salvage artifact mismatch')
    _require(sf.get('salvage_artifact_digest')==salvage.get('salvage_artifact_digest'),'recovery frontier salvage digest mismatch')
    _require(sf.get('summary_sha256')==salvage.get('summary_sha256'),'recovery frontier salvage summary SHA mismatch')
    _require(sf.get('logs_available')==102 and sf.get('logs_unavailable')==10,'recovery frontier log availability mismatch')
    _require(sf.get('batch_schedule_blocks_recovered')==2530,'recovery frontier batch block salvage mismatch')
    _require(sf.get('batch_schedule_columns_recovered')==118883,'recovery frontier batch column salvage mismatch')
    _require(sf.get('scientific_boundary')=='BATCH_LEVEL_LEDGER_TOTALS_ARE_NOT_PER_ORBIT_ASSIGNMENT_IDENTITY','batch/assignment boundary drifted')

    replay=assess_records(assignment['records']); rr=recovery.get('replay_readiness',{})
    _require(rr.get('status')=='MISSING_SELECTOR_OR_MASTER_MAP_PROVENANCE','replay-readiness status drifted')
    _require(rr.get('assignment_identity_is_not_replay_readiness') is True,'assignment/replay boundary missing')
    _require(rr.get('source_raw_artifact_metadata_alone_is_not_enough') is True,'raw metadata replay boundary missing')
    _require(rr.get('canonical_compute_allowed') is False,'canonical compute cannot be enabled without persisted replay evidence')
    _require(rr.get('rank_certified') is False,'replay-readiness must not claim rank')
    _require(replay['canonical_compute_allowed'] is False,'current persisted assignments unexpectedly became replay-ready')
    _require(replay['replay_ready_blocks']==0,'current canonical ledger must not infer replay-readiness from source metadata')
    rules=recovery.get('rules',{})
    for key in ('batch_schedule_is_not_assignment_identity','assignment_identity_is_not_replay_readiness','replay_requires_persisted_master_map_or_selector_witness','unavailable_log_is_unknown_not_failure'):
        _require(rules.get(key) is True,f'schema6 rule missing: {key}')
    return {'stagea_logs_available':102,'stagea_batch_blocks_recovered':2530,'stagea_batch_columns_recovered':118883,'replay_ready_blocks':0,'replay_compute_allowed':False,'stagea_summary_sha256':salvage['summary_sha256']}


def verify(recovery:dict,depth6:dict,root:Path)->dict:
    schema=int(recovery.get('schema_version',-1)); _require(schema>=5,'recovery frontier schema must be >= 5')
    _require(recovery.get('irrep')=='[3,2]','recovery frontier irrep must be [3,2]')
    _require(recovery.get('structural_status')=='CLOSED_IMMUTABLE_INPUT','structural input must remain immutable')
    _require(recovery.get('numerical_status')=='RECOVER_OR_FINISH','[3,2] numerical status must remain RECOVER_OR_FINISH')
    _require(int(recovery.get('target_blocks',-1))==2755,'target blocks drifted from 2755')
    _require(int(recovery.get('target_columns',-1))==130903,'target columns drifted from 130903')

    _require(depth6.get('multiplicities',{}).get('[3,2]')==130903,'depth6 [3,2] multiplicity mismatch')
    ss=depth6.get('structural_support',{}).get('[3,2]',{})
    _require(ss.get('status')=='CLOSED','depth6 [3,2] structural support must remain CLOSED')
    _require(ss.get('blocks')=='2755/2755','depth6 [3,2] structural block target mismatch')
    _require(ss.get('columns')=='130903/130903','depth6 [3,2] structural column target mismatch')
    nw=depth6.get('numerical_master_witnesses',{}).get('[3,2]',{})
    _require(nw.get('status')=='RECOVER_OR_FINISH','depth6 [3,2] numerical frontier was unexpectedly promoted')
    _require(nw.get('dimension')==130903 and nw.get('blocks')==2755,'depth6 [3,2] witness dimensions drifted')
    _require(depth6.get('current_numerical_witness')=='[3,2]','current numerical witness must remain [3,2]')
    _require(depth6.get('finite_depth6_theorem_status')=='NOT_YET_PROVED','finite depth-6 theorem cannot be promoted while [3,2] is incomplete')

    _require(recovery.get('raw_present_shards',[])==EXPECTED_SHARDS,'raw shard frontier mismatch')
    _require(recovery.get('keymeta_preserved_shards',[])==EXPECTED_SHARDS,'keymeta shard frontier mismatch')
    _require(recovery.get('raw_present_count')==15 and recovery.get('keymeta_preserved_count')==15,'persisted shard count must remain 15')
    cov=recovery.get('coverage_inventory',{})
    _require(cov.get('status')=='INCOMPLETE_KEYMETA_COVERAGE','coverage must still be explicitly incomplete')
    _require(cov.get('recovered_shards')==15 and cov.get('recovered_blocks')==15 and cov.get('recovered_columns')==7749,'coverage persisted totals drifted')
    _require(cov.get('schedule_allowed') is False,'schedule_allowed must remain false until exact complete coverage')
    _require(cov.get('next_action')=='RECOVER_MISSING_KEYMETA_SHARDS_ONLY','coverage next action drifted')
    exact=recovery.get('exact_recovered_identity',{}); _require(exact.get('blocks')==15 and exact.get('columns')==7749,'exact recovered identity mismatch')
    retry=recovery.get('targeted_retry',{})
    _require(retry.get('disposition')=='QUARANTINED_NONCANONICAL_FOR_RECOVERY','targeted retry must remain quarantined')
    _require(retry.get('required_replacement')=='LEDGER_DRIVEN_NUMERICAL_RETRY_FROM_PERSISTED_FROZEN_ASSIGNMENTS_ONLY','targeted retry replacement contract drifted')

    rules=recovery.get('rules',{})
    for k in ('structural_recompute_performed','multiplicity_recompute_performed','jucys_recompute_performed'): _require(rules.get(k) is False,f'{k} must remain false')
    for k in ('forbid_future_recovery_bootstrap_of_shell_orbits_multiplicity_or_jucys','canonical_retry_requires_persisted_assignment_ledger','raw_artifact_presence_is_not_rank_evidence','keymeta_is_not_rank_evidence','subset_q_uniqueness_is_not_rank_evidence','global_candidate_schedule_requires_112_of_112_actual_q_occupancy','svd_removal_requires_full_column_rank_and_sigma_min_threshold','failed_svd_candidate_remains_present_during_fail_closed_replay'): _require(rules.get(k) is True,f'{k} must remain true')
    for rel in REQUIRED_FILES: _require((root/rel).is_file(),f'missing canonical recovery implementation: {rel}')

    assignment_path=root/ASSIGNMENT_LEDGER; _require(assignment_path.is_file(),f'missing persisted assignment ledger: {ASSIGNMENT_LEDGER}')
    try: assignment=verify_assignment_ledger(json.loads(assignment_path.read_text()))
    except Exception as exc: raise RuntimeError(f'assignment ledger integrity failure: {exc}') from exc
    acov=assignment['coverage']
    _require(acov['persisted_blocks']==exact['blocks'] and acov['persisted_columns']==exact['columns'],'assignment ledger coverage disagrees with recovery identity')
    _require(acov['status']=='INCOMPLETE_PERSISTED_ASSIGNMENT_LEDGER','assignment ledger must remain explicitly incomplete')
    _require(acov['retry_allowed'] is False,'assignment retry must remain disabled while persisted ledger is incomplete')
    _require(acov['rank_certified'] is False,'assignment ledger must never claim rank certification')

    extension={}
    if schema>=6 and recovery.get('persisted_assignment_ledger'):
        extension.update(_verify_schema6_extensions(recovery,root,assignment))
    if schema>=7:
        _require((root/'scripts/depth6_32_identity_rematerialization.py').is_file(),'missing canonical recovery implementation: scripts/depth6_32_identity_rematerialization.py')
        _require((root/'scripts/depth6_32_rematerialized_identity.py').is_file(),'missing canonical recovery implementation: scripts/depth6_32_rematerialized_identity.py')
        extension.update(verify_snapshot(root,recovery))
        _require(rules.get('rematerialized_identity_is_not_rank_evidence') is True,'schema7 rematerialized identity/rank boundary missing')
        _require(rules.get('rematerialized_identity_does_not_bypass_replay_readiness') is True,'schema7 rematerialized identity/replay boundary missing')
        extension.setdefault('replay_compute_allowed',False)

    claim=str(recovery.get('claim_boundary',''))
    _require('does not certify rank(C_32)=130903' in claim,'claim boundary must deny [3,2] rank certification')
    _require('does not close [3,2] numerically' in claim,'claim boundary must deny [3,2] numerical closure')
    return {'status':'PASS_CANONICAL_RECOVERY_FRONTIER_INCOMPLETE','schema_version':schema,'numerical_closure_claimed':False,'schedule_allowed':False,'assignment_retry_allowed':False,'recovered_shards':15,'recovered_blocks':15,'recovered_columns':7749,'assignment_ledger_sha256':assignment['ledger_sha256'],'target_blocks':2755,'target_columns':130903,**extension}


def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--recovery',type=Path,default=Path('BQG_DEPTH6_32_RECOVERY_FRONTIER_2026-10-02.json')); ap.add_argument('--depth6',type=Path,default=Path('depth6_frontier.json')); ap.add_argument('--root',type=Path,default=Path('.')); a=ap.parse_args()
    print(json.dumps(verify(json.loads(a.recovery.read_text()),json.loads(a.depth6.read_text()),a.root),sort_keys=True)); return 0


if __name__=='__main__': raise SystemExit(main())
