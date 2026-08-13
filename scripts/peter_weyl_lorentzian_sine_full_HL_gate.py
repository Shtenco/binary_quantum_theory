#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import k5_peter_weyl_safe_hda_column as PW
from peter_weyl_sine_scalar_runtime import SineScalarRuntime,add,state_norm,max_spin

def run(v=0):
    total={}; rows=[]
    with SineScalarRuntime(v,7) as rt:
        psi=rt.initial_covariant()
        specs=PW.oriented_specs(v)
        for sign,spec in specs:
            _,a,b,c=spec
            abc,_=rt.ordered_triple(a,b,c,psi)
            bac,_=rt.ordered_triple(b,a,c,psi)
            add(total,abc,+sign); add(total,bac,-sign)
            rows.append({'sign':int(sign),'abc':[a,b,c],'abc_norm':state_norm(abc),'bac_norm':state_norm(bac)})
        diag=dict(rt.diag); cache=rt.cache_info()
    badJ=sum(abs(x)**2 for k,x in total.items() if k[2]!=0)
    norm=state_norm(total); support=len(total); mspin=max_spin(total)
    passed=(len(rows)==12 and support>0 and norm>1e-10 and badJ<1e-20
            and diag['CV_complete_basis_leakage']<1e-9
            and diag['CK_outer_complete_basis_leakage']<1e-9
            and diag['CK_internal_volume_sector_leakage']<1e-9
            and mspin<=3.5+1e-12)
    return {'status':'full 24-term epsilon-oriented raw sine H_L column','passed':bool(passed),
            'source_node':v,'Jmax':3.5,'cyclic_specs':12,'ordered_terms':24,
            'definition':'sum sign*(T_abc-T_bac), T=Tr_aux[C(K_sine)C(K_sine)C(V)]',
            'output_support':support,'output_norm':norm,'forbidden_final_J_weight':badJ,
            'max_spin_reached':mspin,'diagnostics':diag,'term_rows':rows,'runtime_cache':cache,
            'primitive_charge_diagnostic_hard_acceptance':False,
            'normalization':'raw core only: no beta, kappa or fitted coefficient',
            'reference_requirement':'accelerated ordered triple must match unrestricted sine reference first',
            'next':'audit Hermitian ordering, then mixed [H_E^sine,H_L] at Jmax=9/2'}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--v',type=int,default=0); p.add_argument('--output',type=Path); a=p.parse_args()
    out=run(a.v); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
