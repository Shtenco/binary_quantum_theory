#!/usr/bin/env python3
"""Collect 128 ordered-path shards into the exact 32D j=1 higher-shell result."""
from __future__ import annotations
import argparse, json
from pathlib import Path

import peter_weyl_j1_higher_shell_lambda_gate as J1
import peter_weyl_higher_shell_lambda_gate as HS

TOL=2e-10

def add(dst,src,scale=1.0):
    J1.AN.sparse_add(dst,src,scale)

def diff_norm(a,b):
    d=dict(a); add(d,b,-1.0); return float(J1.AN.sparse_norm(d))

def load(root):
    rows={}
    for p in root.rglob('shard_*.json'):
        d=json.loads(p.read_text(encoding='utf-8'))
        key=(int(d['column']),int(d['first_node']),int(d['second_node']))
        if key in rows: raise RuntimeError(f'duplicate shard {key}')
        rows[key]=d
    expected={(c,s,r) for c in range(J1.NLOGICAL) for s in (0,1) for r in (0,1)}
    missing=sorted(expected-set(rows)); extra=sorted(set(rows)-expected)
    if missing or extra: raise RuntimeError(f'shard mismatch missing={missing} extra={extra}')
    return rows

def collect(root,out_columns):
    rows=load(root); out_columns.mkdir(parents=True,exist_ok=True)
    duplicate_first_max=0.0; first_proj_max=0.0; second_max=0.0
    for c in range(J1.NLOGICAL):
        first={};
        for s in (0,1):
            f0=HS.rows_to_state(rows[(c,s,0)]['first_state'])
            f1=HS.rows_to_state(rows[(c,s,1)]['first_state'])
            duplicate_first_max=max(duplicate_first_max,diff_norm(f0,f1)); first[s]=f0
        a={}; add(a,first[0]); add(a,first[1])
        b={}
        for s in (0,1):
            for r in (0,1): add(b,HS.rows_to_state(rows[(c,s,r)]['second_path_state']))
        all_j1={k:v for k,v in a.items() if all(sp==2 for sp in k[0])}
        fp=float(J1.AN.sparse_norm(all_j1)); first_proj_max=max(first_proj_max,fp)
        sm=J1.max_spin(b); second_max=max(second_max,sm)
        label=rows[(c,0,0)]['label']
        col={
          'status':'exact j=1 S4-doublet Peter-Weyl higher-shell logical column reconstructed from ordered paths',
          'column':c,'label':label,'coarse_face_spin':1.0,'coarse_local_irrep':'S4 [2,2] doublet in four-j=1 singlet',
          'Jmax_used':HS.JMAX2_SECOND_HIT_SAFE/2.0,'first_order_projection_norm':fp,
          'first_support':len(a),'second_support':len(b),'first_max_spin':J1.max_spin(a),'second_max_spin':sm,
          'first_state':HS.state_to_rows(a),'second_state':HS.state_to_rows(b)
        }
        (out_columns/f'column_{c}.json').write_text(json.dumps(col,indent=2)+'\n',encoding='utf-8')
    if duplicate_first_max>TOL: raise RuntimeError(f'duplicate first-hit mismatch {duplicate_first_max}')
    if first_proj_max>1e-12: raise RuntimeError(f'first projection parity failure {first_proj_max}')
    result=J1.assemble(out_columns)
    result['path_sharding']={
      'shard_count':len(rows),'ordered_paths_per_column':4,
      'identity':'(H0+H1)^2=sum_{r,s in {0,1}} H_r H_s',
      'duplicate_first_hit_max_norm_error':duplicate_first_max,
      'reconstructed_first_projection_max':first_proj_max,
      'reconstructed_second_max_spin':second_max,
      'computational_only':True
    }
    result['passed']=bool(result['passed'] and duplicate_first_max<TOL and first_proj_max<1e-12)
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--columns-dir',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    out=collect(a.root,a.columns_dir); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':out['passed'],'path_sharding':out['path_sharding'],'representation_RG':out.get('representation_RG'),'Lambda':{k:out['Lambda'][k] for k in ('eigenvalue_min','eigenvalue_max','distance_to_scalar_identity_relative')}},indent=2))
    return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
