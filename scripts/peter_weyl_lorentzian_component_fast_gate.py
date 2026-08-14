#!/usr/bin/env python3
"""Fastest safe-cutoff nonzero test for one Lorentzian logical auxiliary path.

Evaluate

  <K=0| C_a(K)_{00} C_b(K)_{00} C_c(V)_{00} |K=0>

with one heavy generalized middle C(K) at Jmax=7/2.  The outer bra C_a(K) acts
on an ordinary Gauss logical state, so use the already independently validated
reference C(K) column at its sufficient Jmax=5/2 wall.  Likewise use the
validated reference C(V) column for the first leg.  The sine-ordered K stack is
installed before both reference and generalized calls.

The meet-in-the-middle identity is

  amplitude = - < C_a(K)_{00} f | C_b(K)_{00} C_c(V)_{00} q >

because raw K=[V,H_E^sine] is anti-Hermitian and therefore
C(K)_ij^dagger=-C(K)_ji.

Nonzero proves a genuine Peter-Weyl logical return amplitude entirely inside the
preregistered safe walls.  It is only one auxiliary path, not an auxiliary
trace or epsilon sum.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_lorentzian_logical_projection_gate as LP

def inner(a,b):
    if len(a)>len(b): return np.conj(inner(b,a))
    return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())
def cp(z): z=complex(z); return [float(z.real),float(z.imag)]

def run():
    source=0; Jmid=7; LP.JMAX2=Jmid
    restore,_=LP.install_sine_cached_stack()
    try:
        a,b,c=PW.NEIG[source][:3]
        initial=PW.basis_full_jhalf()[0]
        # Independent validated Gauss C(K) reference. Jmax2=5 is the frozen
        # sufficient wall used by the composition-equivalence gate.
        CKref,ckdiag=LP.KC.reference_CK_matrix(initial,source,a,5)
        bra=CKref[0][0]
        # Independent validated C(V) reference matrix; component [k][i]=[0][0].
        CVref=LP.RAW.COMP.reference_CV_matrix(initial,source,c,3)
        s1=CVref[0][0]
        # Only genuinely heavy operation: C_b(K) on the non-Gauss C(V) state.
        s2,d2=LP.RAW.KCOMP.C_K_component(s1,source,b,0,0,Jmid)
        s2_scalar={k:v for k,v in s2.items() if k[2] in (0,2)}
        amp=-inner(bra,s2_scalar) if bra and s2_scalar else 0j
        physical=max(
            float(d2['outer_complete_basis_leakage']),
            float(d2['internal_volume_sector_leakage']),
            float(ckdiag.get('outer_wrong_charge_fraction',0.0)),
            float(ckdiag.get('HE_wrong_charge_fraction',0.0)),
            float(ckdiag.get('K_wrong_charge_fraction',0.0)),
        )
        return {
          'status':'fast safe-cutoff one-path Lorentzian logical-return gate',
          'passed':bool(physical<1e-8 and np.isfinite(amp.real) and np.isfinite(amp.imag)),
          'source_node':source,'ordered_edges':[a,b,c],'auxiliary_indices':[0,0,0],
          'input_target_logical_K2':0,
          'outer_reference_CK_Jmax':2.5,'middle_generalized_CK_Jmax':3.5,'reference_CV_Jmax':1.5,
          'outer_CK_support':len(bra),'CV_support':len(s1),
          'middle_CK_support_before_scalar_prune':len(s2),'middle_CK_scalar_support':len(s2_scalar),
          'logical_component_amplitude':cp(amp),'logical_component_abs':float(abs(amp)),
          'nonzero':bool(abs(amp)>1e-12),
          'physical_acceptance_max_leakage':physical,
          'middle_CK_diagnostics':d2,
          'outer_reference_CK_diagnostics':ckdiag,
          'historical_middle_charge_diagnostic_is_hard_acceptance':False,
          'scope':'One safe auxiliary path only. Nonzero proves a return mechanism, not a nonzero auxiliary trace, epsilon sum, Hermitian H_L, mass or force.'
        }
    finally: restore()

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path); a=ap.parse_args(); o=run(); t=json.dumps(o,indent=2); print(t)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
