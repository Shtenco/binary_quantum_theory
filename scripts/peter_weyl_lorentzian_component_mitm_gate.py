#!/usr/bin/env python3
"""Minimal safe-cutoff Peter-Weyl Lorentzian logical-return component.

Evaluate one genuine auxiliary-index contribution of one ordered triple,

    <K=0| C_a(K)_{00} C_b(K)_{00} C_c(V)_{00} |K=0>,

at the preregistered single-H_L wall Jmax=7/2.  Using
C(K)_{ij}^dagger=-C(K)_{ji}, contract the last C(K) meet-in-the-middle:

    amplitude = - < C_a(K)_{00} f | C_b(K)_{00} C_c(V)_{00} q >.

This is a positive-only mechanism probe.  Nonzero proves a real logical return
path with nonzero recoupling amplitude inside the safe cutoff.  Zero is only a
statement about this one component and does not imply the full triple vanishes.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_lorentzian_logical_projection_gate as LP

def inner(a,b): return sum(np.conj(x)*b.get(k,0j) for k,x in a.items())

def cp(z): z=complex(z); return [float(z.real),float(z.imag)]

def run():
    Jmax2=7; source=0; LP.JMAX2=Jmax2
    restore,_=LP.install_sine_cached_stack()
    try:
        a,b,c=PW.NEIG[source][:3]
        spins=(1,)*len(PW.EDGES); Ks=(0,)*len(PW.VERT); key=(spins,Ks)
        psi=LP.CV.gauss_to_covariant({key:1+0j},source)
        s1,lv=LP.RAW.COMP.C_volume_component(psi,source,c,0,0,Jmax2)
        s2,d2=LP.RAW.KCOMP.C_K_component(s1,source,b,0,0,Jmax2) if s1 else ({},{'outer_complete_basis_leakage':0.0,'internal_volume_sector_leakage':0.0,'complete_charge_basis_leakage':0.0})
        s2={k:v for k,v in s2.items() if k[2] in (0,2)}
        bra,dA=LP.RAW.KCOMP.C_K_component(psi,source,a,0,0,Jmax2)
        amp=-inner(bra,s2) if bra and s2 else 0j
        physical=max(float(lv),float(d2['outer_complete_basis_leakage']),float(d2['internal_volume_sector_leakage']),float(dA['outer_complete_basis_leakage']),float(dA['internal_volume_sector_leakage']))
        return {
          'status':'safe-cutoff single auxiliary Lorentzian MITM component',
          'passed':bool(physical<1e-8 and np.isfinite(amp.real) and np.isfinite(amp.imag)),
          'Jmax':3.5,'source_node':0,'ordered_edges':[a,b,c],'auxiliary_indices':[0,0,0],
          'input_source_K2':0,'target_source_K2':0,
          'after_CV_support':len(s1),'after_middle_CK_scalar_support':len(s2),'backward_CK_support':len(bra),
          'logical_component_amplitude':cp(amp),'logical_component_abs':float(abs(amp)),
          'nonzero':bool(abs(amp)>1e-12),'physical_acceptance_max_leakage':physical,
          'historical_charge_diagnostics':[float(d2['complete_charge_basis_leakage']),float(dA['complete_charge_basis_leakage'])],
          'historical_charge_is_hard_acceptance':False,
          'scope':'One auxiliary path only. Nonzero proves a safe-cutoff return mechanism but not a nonzero auxiliary trace, epsilon sum, final Hermitian H_L, mass or force.'
        }
    finally: restore()

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path); a=ap.parse_args(); o=run(); t=json.dumps(o,indent=2); print(t)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
