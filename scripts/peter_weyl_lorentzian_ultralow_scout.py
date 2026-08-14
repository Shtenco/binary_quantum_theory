#!/usr/bin/env python3
"""Exploratory Jmax=1 positive-only scout for one Lorentzian ordered triple.

This lowers the single-triple wall to doubled JMAX2=2 (j<=1).  It is deliberately
noncanonical.  A nonzero logical return proves that at least one genuine return
path exists entirely inside j<=1; a zero result is inconclusive.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import peter_weyl_lorentzian_logical_projection_gate as LP
import peter_weyl_lorentzian_single_logical_probe as PROBE

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path); a=ap.parse_args()
    LP.JMAX2=2
    out=PROBE.run(0)
    out['exploratory_Jmax']=1.0
    out['canonical_safe_Jmax']=3.5
    out['canonical_status']=False
    out['interpretation_ultralow']='Nonzero is positive return-path evidence; zero is inconclusive under this truncated wall.'
    txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
