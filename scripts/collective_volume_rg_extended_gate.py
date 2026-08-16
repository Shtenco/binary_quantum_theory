#!/usr/bin/env python3
"""Extended equal-spin collective volume ladder for BCQG.

The microscopic j=1/2 face sector has scalar |V| on the 4-valent singlet
intertwiner. This gate verifies that nontrivial volume branches persist along
the first symmetric blocking ladder j=1,3/2,2,5/2 rather than appearing only
at one accidental representation.
"""
from __future__ import annotations
import argparse,json,sys,math
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))
from collective_volume_rg_gate import spectrum


def run():
    spins=(0.5,1.0,1.5,2.0,2.5)
    rows=[]
    for j in spins:
        r=spectrum(j)
        v=np.asarray(r['absolute_volume_spectrum_up_to_scale'],float)
        r['volume_mean']=float(v.mean())
        r['volume_rms']=float(np.sqrt(np.mean(v*v)))
        r['volume_max']=float(v.max())
        rows.append(r)
    persistent=all(not r['volume_is_scalar_on_intertwiner'] for r in rows[1:])
    dims=all(r['intertwiner_dimension']==r['expected_dimension_2j_plus_1'] for r in rows)
    branches=[r['number_distinct_absolute_volumes'] for r in rows]
    x=np.log([r['j'] for r in rows[1:]])
    y=np.log([r['volume_rms'] for r in rows[1:]])
    p,b=np.polyfit(x,y,1)
    return {
      'status':'extended collective volume representation ladder',
      'passed':bool(persistent and dims),
      'rows':rows,
      'distinct_volume_branches':branches,
      'finite_ladder_rms_power_fit':{'power_in_j':float(p),'prefactor':float(math.exp(b))},
      'conclusion':'The j=1/2 fixed-volume obstruction is removed at j=1 and nontrivial absolute-volume branches persist through j=5/2.',
      'scope_note':'The fitted small-j power is descriptive only and is not claimed as a large-j continuum critical exponent.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    o=run(); t=json.dumps(o,indent=2); print(t)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
