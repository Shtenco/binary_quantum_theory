#!/usr/bin/env python3
"""Write the frozen all-j=1/2, all-K=0 Gauss seed as sparse NPZ."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state-output',type=Path,required=True)
    p.add_argument('--json-output',type=Path,required=True)
    a=p.parse_args()
    key=PW.basis_full_jhalf()[0]
    a.state_output.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(
        a.state_output,
        spins=np.asarray([key[0]],dtype=np.int16),
        Ks=np.asarray([key[1]],dtype=np.int16),
        amp=np.asarray([1+0j],dtype=np.complex128),
    )
    out={
        'status':'frozen all-j=1/2 all-K=0 Gauss seed',
        'passed':tuple(key[0])==(1,)*len(PW.EDGES) and tuple(key[1])==(0,)*len(PW.VERT),
        'spins2':list(key[0]),'Ks2':list(key[1]),'support':1,'norm':1.0,
    }
    a.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
