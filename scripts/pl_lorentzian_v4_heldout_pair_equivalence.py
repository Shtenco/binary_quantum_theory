#!/usr/bin/env python3
"""Held-out implementation equivalence: one V4 physical pair vs four direct V2 primitives.

The frozen held-out pair is omit=0, cycle=0, i.e. permutations (1,2,3) and
(2,1,3), which are V2 ordered indices 0 and 2.  The reference physical pair is
assembled only from separately serialized V2 forward/adjoint NPZ+JSON files.
It is then compared with an independently executed V4 pair worker output.

No GR/HDA target enters this check.
"""
from __future__ import annotations
import argparse,json,math,traceback
from pathlib import Path
import numpy as np
import pl_lorentzian_48_collect as BASE

TOL=1e-10
PAIR=(0,0);INDICES=(0,2)

def add(dst,src,scale=1.0,tol=1e-12):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol:dst[k]=z
        elif k in dst:del dst[k]
def norm(s):return math.sqrt(sum(abs(a)**2 for a in s.values()))
def relerr(a,b):
    keys=set(a)|set(b);num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys));return num/max(norm(b),1e-300)

def one(root,mode,idx):
    js=list(Path(root).rglob(f'term_{mode}_{idx}.json'));ns=list(Path(root).rglob(f'term_{mode}_{idx}.npz'))
    if len(js)!=1 or len(ns)!=1:raise RuntimeError(f'need one direct V2 {mode} {idx}, got json={len(js)} npz={len(ns)}')
    d=json.loads(js[0].read_text(encoding='utf-8'))
    if not d.get('passed'):raise RuntimeError(f'direct V2 worker failed: {mode} {idx}')
    if d.get('operator_version')!='tetrahedral-charged-volume-v2':raise RuntimeError(f'wrong V2 provenance {mode} {idx}: {d.get("operator_version")}')
    return BASE.load_state(ns[0]),d

def run(root):
    fp,mp=one(root,'forward',0);fq,mq=one(root,'forward',2)
    ap,map_=one(root,'adjoint',0);aq,maq=one(root,'adjoint',2)
    cp=int(mp['PL_epsilon_coefficient']);cq=int(mq['PL_epsilon_coefficient'])
    if cp!=-cq:raise RuntimeError(f'held-out epsilon partners not opposite: {cp},{cq}')
    ref={};add(ref,fp,-0.5j*cp);add(ref,fq,-0.5j*cq);add(ref,ap,+0.5j*cp);add(ref,aq,+0.5j*cq)
    ref={k:a for k,a in ref.items() if abs(a)>TOL}

    vj=list(Path(root).rglob('pair_0_0.json'));vn=list(Path(root).rglob('pair_0_0.npz'))
    if len(vj)!=1 or len(vn)!=1:raise RuntimeError(f'need one V4 held-out pair, got json={len(vj)} npz={len(vn)}')
    vm=json.loads(vj[0].read_text(encoding='utf-8'));v4=BASE.load_state(vn[0])
    if not vm.get('passed'):raise RuntimeError('V4 held-out pair worker failed')
    if vm.get('operator_version')!='direct-hermitian-commutator-v4':raise RuntimeError(f'wrong V4 provenance {vm.get("operator_version")}')
    if tuple(vm.get('forward_indices',[]))!=INDICES or tuple(vm.get('adjoint_indices',[]))!=INDICES:raise RuntimeError('V4 held-out pair index mismatch')
    v4={k:a for k,a in v4.items() if abs(a)>TOL}
    err=relerr(v4,ref);support=set(v4)==set(ref)
    keys=set(v4)|set(ref);maxabs=max((abs(v4.get(k,0j)-ref.get(k,0j)) for k in keys),default=0.0)
    primitive_max_leak=max(float(x['physical_acceptance_max_leakage']) for x in (mp,mq,map_,maq))
    primitive_max_rej=max(float(x['nonscalar_rejected_norm']) for x in (mp,mq,map_,maq))
    checks={
      'four_direct_V2_primitives_pass':all(x['passed'] for x in (mp,mq,map_,maq)),
      'V4_pair_pass':bool(vm['passed']),
      'epsilon_partner_signs_opposite':cp==-cq,
      'exact_sparse_support_match':bool(support),
      'relative_amplitude_error_below_1e-10':bool(err<1e-10),
      'max_absolute_amplitude_error_below_1e-10':bool(maxabs<1e-10),
      'direct_primitive_leakage_below_1e-8':primitive_max_leak<1e-8,
      'direct_primitive_rejection_below_1e-8':primitive_max_rej<1e-8,
    }
    return {'status':'held-out V4 physical-pair equivalence against separately serialized V2 primitives',
      'passed':bool(all(checks.values())),'science_status':'IMPLEMENTATION_EQUIVALENCE_C1_GUARD',
      'heldout_pair':{'omit':0,'cycle':0,'indices':[0,2]},'checks':checks,
      'reference_support':len(ref),'v4_support':len(v4),'reference_norm':norm(ref),'v4_norm':norm(v4),
      'relative_amplitude_error':err,'max_absolute_amplitude_error':float(maxabs),
      'epsilon_coefficients':[cp,cq],'max_direct_primitive_physical_leakage':primitive_max_leak,
      'max_direct_primitive_nonscalar_rejected_norm':primitive_max_rej,
      'guard':'PASS certifies the V4 physical-pair implementation for one preregistered held-out pair. The full C1 result still requires all 12 V4 physical pairs and final collector PASS.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    try:o=run(a.root);code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'held-out V4/V2 equivalence exception','passed':False,'science_status':'INFRASTRUCTURE_DIAGNOSTIC','error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n',encoding='utf-8');print(json.dumps(o,indent=2,sort_keys=True));return code
if __name__=='__main__':raise SystemExit(main())
