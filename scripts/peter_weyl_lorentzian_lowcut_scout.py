#!/usr/bin/env python3
"""Exploratory low-cutoff scout for a single Lorentzian logical return.

This intentionally lowers the global link wall of the single-triple probe from
the safe Jmax=7/2 to Jmax=3/2.  It is NOT a production/canonical amplitude gate:
high-spin intermediate channels are truncated.  A nonzero logical return is
useful positive evidence that the real K-K-V mechanism can return to P already
inside the low-spin subspace; a zero result is inconclusive.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import peter_weyl_lorentzian_logical_projection_gate as LP
import peter_weyl_lorentzian_single_logical_probe as PROBE


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    LP.JMAX2=3
    out=PROBE.run(0)
    out['exploratory_Jmax']=1.5
    out['canonical_safe_Jmax']=3.5
    out['canonical_status']=False
    out['interpretation_lowcut']=(
        'Nonzero logical return is positive mechanism evidence only. Zero is inconclusive because high-spin paths are truncated.'
    )
    txt=json.dumps(out,indent=2); print(txt)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(txt+'\n',encoding='utf-8')
    # Do not fail merely because logical return is zero; only internal physical
    # leakage/stack acceptance from the probe controls the exit status.
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
