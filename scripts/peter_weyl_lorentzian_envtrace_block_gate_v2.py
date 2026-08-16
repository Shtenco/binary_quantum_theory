#!/usr/bin/env python3
"""V2 diagonal-environment Lorentzian block with tetrahedral charged volume.

Reuses the historical exact MITM environment block and changes only the
charged/intermediate volume continuation.  The v1.3 tetrahedral backend is
installed before the old worker constructs its sine/covariant caches.
"""
from __future__ import annotations
import argparse,json,traceback
from pathlib import Path
import peter_weyl_lorentzian_envtrace_block_gate as OLD
from tetrahedral_volume_backend import install_tetrahedral_volume_backend
VERSION='tetrahedral-charged-volume-v2'

def run(a,b,c,env_start,env_stop,coefficient=1,source=0,jmax2=7):
    with install_tetrahedral_volume_backend():
        out=OLD.run(a,b,c,env_start,env_stop,coefficient,source,jmax2)
    out['operator_version']=VERSION
    out['volume_definition']='V_tet=sqrt(abs((1/4) sum_r (-1)^r q_hat_r)) with production zero-aware spectrum'
    out['supersedes']='historical fixed-q123 charged continuation'
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--c',type=int,required=True);p.add_argument('--coefficient',type=int,required=True);p.add_argument('--env-start',type=int,required=True);p.add_argument('--env-stop',type=int,required=True);p.add_argument('--output',type=Path,required=True);x=p.parse_args()
    try:o=run(x.a,x.b,x.c,x.env_start,x.env_stop,x.coefficient);code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'V2 envtrace worker exception','passed':False,'operator_version':VERSION,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    x.output.parent.mkdir(parents=True,exist_ok=True);x.output.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8');print(json.dumps(o,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
