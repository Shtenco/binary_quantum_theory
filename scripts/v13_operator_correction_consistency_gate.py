#!/usr/bin/env python3
"""Canonical consistency gate for the v1.3 charged-volume correction frontier.

This gate intentionally does not rewrite the historical v1.2 ledger.  It checks
that the authoritative addendum scopes the superseded fixed-q123 finite
Lorentzian claims correctly while retaining Euclidean/route/HDA architecture
claims and an honest INCOMPLETE collective GR verdict.
"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def one(gs,i):
    x=[g for g in gs if g['id']==i]
    if len(x)!=1:raise RuntimeError((i,len(x)))
    return x[0]

def main():
    ledger=json.loads((ROOT/'theory_gates_v13.json').read_text())
    gs=ledger['gates'];status=(ROOT/'THEORY_STATUS.md').read_text();draft=(ROOT/'BCQG_CANDIDATE_THEORY_V1_3_DRAFT.md').read_text();pre=(ROOT/'PL_16CELL_HERMITIAN_LORENTZIAN_PREREGISTRATION_V2.md').read_text()
    ids={g['id'] for g in gs}
    required={'E_STABLE','TETRA_VOL','LOR_FINITE_V13','HERM_PROJECTION','LOR_NORMALIZATION','PARITY_SCOPE','ROUTE_MICRO','ROUTE_PL_E','CUTOFF_WALL','HDA_ARCHITECTURE','COLL_E_KRYLOV','COLL_XOR','COLL_PROTOCOL','COLL_GR'}
    evidence_paths=[]
    for g in gs:
        for p in g.get('evidence',[]):evidence_paths.append((g['id'],p,(ROOT/p).exists()))
    missing=[{'gate':g,'path':p} for g,p,ok in evidence_paths if not ok]
    checks={
      'all_required_v13_gates':required<=ids,
      'all_addendum_evidence_exists':not missing,
      'tetra_volume_tested':one(gs,'TETRA_VOL')['status']=='tested_finite',
      'historical_lorentzian_open':one(gs,'LOR_FINITE_V13')['status']=='open' and 'regression' in one(gs,'LOR_FINITE_V13')['claim'].lower(),
      'hermitian_projection_proved':one(gs,'HERM_PROJECTION')['status']=='proved',
      'collective_GR_open':one(gs,'COLL_GR')['status']=='open' and 'INCOMPLETE' in one(gs,'COLL_GR')['claim'],
      'route_PL_tested':one(gs,'ROUTE_PL_E')['status']=='tested_finite',
      'E_collective_tested':one(gs,'COLL_E_KRYLOV')['status']=='tested_finite',
      'status_marks_old_numbers_historical':'HISTORICAL / REQUIRES_TETRAHEDRAL_REAUDIT' in status,
      'status_contains_equal_slot_norms':'0.2513477706186925' in status,
      'draft_keeps_G_structural':'G_v=-\\frac23E_v-\\frac{32}{9}S_v' in draft,
      'draft_forbids_old_promotion':'historical regression anchors, not v1.3 predictions' in draft,
      'v2_prereg_keeps_24_plus_24':'24 forward + 24 direct-adjoint' in pre,
      'v2_prereg_no_nonzero_requirement':'no lower bound on `||S||`' in pre,
      'parity_regulator_scoped':'even-valence' in status and 'collective `E` **preserves**' in status,
    }
    out={'status':'BCQG v1.3 operator-correction canonical consistency','passed':bool(all(checks.values())),'gate_count':len(gs),'checks':checks,'missing_evidence':missing,
         'frontier':'corrected V_tet Lorentzian finite rerun -> held-out S XOR -> W_E+S+R -> direct collective GR AND gate'}
    print(json.dumps(out,indent=2,sort_keys=True));return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
