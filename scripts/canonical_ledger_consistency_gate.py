#!/usr/bin/env python3
"""Cross-check BCQG v1.2 canonical human/machine ledgers against frozen evidence."""
from __future__ import annotations
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/'THEORY_STATUS.md'; CAND=ROOT/'BCQG_CANDIDATE_THEORY_V1_2.md'; CORE=ROOT/'BCQG_CORE_CANDIDATE_V1_2.md'; START=ROOT/'START_HERE.md'; LEDGER=ROOT/'theory_gates.json'
SINE=ROOT/'verification_results/PETER_WEYL_TWO_NODE_SINE_HDA.json'
LOR=ROOT/'verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json'
MULTI=ROOT/'verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_WALSH_NODE012.json'
HERM=ROOT/'verification_results/LORENTZIAN_HERMITIAN_COMPLETION.json'
ROUTE=ROOT/'verification_results/PETER_WEYL_OPERATOR_ROUTE_ALL_REACHED.json'
SAT=ROOT/'verification_results/BCQG_V12_CUTOFF_SATURATED_HDA.json'
HIT=ROOT/'verification_results/LORENTZIAN_HIT_DEPTH_BOUND.json'
HUNIQ=ROOT/'verification_results/LORENTZIAN_HERMITIAN_PROJECTION_UNIQUENESS.json'

def gate(gs,i):
    x=[g for g in gs if g['id']==i]
    if len(x)!=1: raise RuntimeError(f'expected one gate {i}, got {len(x)}')
    return x[0]

def main():
    status=STATUS.read_text(); cand=CAND.read_text(); core=CORE.read_text(); start=START.read_text(); ledger_text=LEDGER.read_text(); d=json.loads(ledger_text); gs=d['gates']
    sine=json.loads(SINE.read_text()); lor=json.loads(LOR.read_text()); multi=json.loads(MULTI.read_text()); herm=json.loads(HERM.read_text()); route=json.loads(ROUTE.read_text()); sat=json.loads(SAT.read_text()); hit=json.loads(HIT.read_text()); huniq=json.loads(HUNIQ.read_text())
    ids={g['id'] for g in gs}
    checks={
      'v12_named_everywhere':all('v1.2' in x for x in (status,cand,core,start)),
      'required_gates':{'ROUTE_ALL','PARITY','CUTOFF_SAT','FULLHDA_OP','LOR_HERM','HERM_UNIQ','LORORDER','CORECERT'}<=ids,
      'statuses':gate(gs,'ROUTE_ALL')['status']=='tested_finite' and gate(gs,'PARITY')['status']=='proved' and gate(gs,'CUTOFF_SAT')['status']=='proved' and gate(gs,'FULLHDA_OP')['status']=='conditional' and gate(gs,'LOR_HERM')['status']=='tested_finite' and gate(gs,'HERM_UNIQ')['status']=='proved' and gate(gs,'LORORDER')['status']=='open',
      'production_hermitian_G':all('G=-\\frac23E-\\frac{32}{9}S' in x or 'G_v=-\\frac23E_v-\\frac{32}{9}S_v' in x or 'G = -2/3 E -32/9 S' in x for x in (status,cand,core,start)),
      'old_raw_formula_explicitly_nonproduction':all(('only' in x[x.find('historical'):].lower()) if 'historical' in x else ('not' in x.lower()) for x in (status,cand,core,start)),
      'hermitian_evidence':bool(herm['passed']) and herm['definition']=='H_phase_sym=-i/2 (L_raw-L_raw^dagger)',
      'hermitian_projection_unique':bool(huniq['passed']) and 'unique linear Hermitian projection' in huniq['status'] and huniq['closest_point_identity_defect']<1e-10,
      'raw_onebody_preserved':abs(math.hypot(*lor['onebody_Y_coefficient_raw'])-1.3389293521464034)<1e-12 and abs(float(herm['environment_unbiased_onebody_signed_Y'])+4.760637696520545)<1e-12,
      'multi_evidence':bool(multi['passed']) and int(multi['triple_count'])==24 and float(multi['max_leakage'])<1e-12,
      'route_all_pass':bool(route['passed']) and int(route['distinct_reached_sectors'])==33 and int(route['nonzero_powerlaw_sectors'])==30 and int(route['numerical_zero_sectors'])==3,
      'route_scaling':0.99<float(route['nonzero_exponent_min'])<float(route['nonzero_exponent_max'])<1.01 and float(route['endpoint_max'])<2e-5 and float(route['minimum_symbol_eigenvalue'])>-1e-8,
      'hit_wall':bool(hit['passed']) and int(hit['max_hits_per_link_HH'])==12 and abs(float(hit['sufficient_Jmax_for_full_Lorentzian_HH'])-6.5)<1e-15,
      'sat_pass':bool(sat['passed']) and sat['physical_geometry']['G']=='(-2/3) E_sine -(32/9) S' and float(sat['spin_cutoff_saturation']['sufficient_Jmax'])==6.5,
      'sat_weights':sat['physical_geometry']['channel_weights']=={'EE':'4/9','ES':'64/27','SE':'64/27','SS':'1024/81'},
      'sat_parity':sat['parity_decomposition']['operator_parities']=={'D':1,'E':-1,'R':1,'S':1},
      'sine_anchor':bool(sine['passed']) and abs(float(sine['last_joint_defect_over_D'])-0.020030338775070305)<1e-15,
      'jointdiag_is_extension':'extension' in gate(gs,'JOINTDIAG')['claim'].lower() and all('not required' in x.lower() for x in (cand,core,start)),
      'finite_falsifier_still_open':'ES/SE/SS' in gate(gs,'LORORDER')['claim'] and 'finite' in gate(gs,'LORORDER')['claim'].lower(),
      'ir_scope_not_overclaimed':all('not experimentally' in x.lower() for x in (status,cand,core,start)),
    }
    out={'status':'BCQG v1.2 canonical consistency','passed':all(checks.values()),'gate_count':len(gs),'checks':checks,'anchors':{'Jmax_safe':'13/2','route_sectors':33,'route_p_min':route['nonzero_exponent_min'],'route_p_max':route['nonzero_exponent_max'],'onebody_raw_Y':1.3389293521464034,'onebody_signed_Y':-4.760637696520545}}
    print(json.dumps(out,indent=2,sort_keys=True)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
