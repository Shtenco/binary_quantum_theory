#!/usr/bin/env python3
"""Metric content of the rank-one canonical barycentric j=3 background.

The first barycentric tetra block selects one projective vector in the seven
four-j=3 singlets.  This gate asks what geometry that vector carries.  It
computes the exact face-flux Gram matrix and the absolute-volume fluctuations.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW

TARGET=np.array([7*math.sqrt(5),0,-24,0,22*math.sqrt(5),0,0],float)/math.sqrt(3241)


def eps3(a,b,c):
    if len({a,b,c})<3:return 0
    p=(a,b,c);inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else 1


def run(tol=1e-12):
    psi=np.zeros((7,7,7,7),complex)
    for a,K2 in zip(TARGET,range(0,13,2)):
        psi+=a*PW.intertwiner_tensor_cached((6,6,6,6),K2)
    psi/=np.linalg.norm(psi)
    mats=PW.spin_mats_cached(6)
    gram=np.zeros((4,4),float)
    for f in range(4):
        for g in range(4):
            z=0j
            for c in range(3):
                x=PW.apply_axis_np(psi,g,mats[c])
                x=PW.apply_axis_np(x,f,mats[c])
                z+=np.vdot(psi,x)
            gram[f,g]=float(z.real)
    regular=16*np.eye(4)-4*np.ones((4,4))
    rel=float(np.linalg.norm(gram-regular)/np.linalg.norm(regular))
    eig=np.linalg.eigvalsh(gram)
    closure=float(np.linalg.norm(gram@np.ones(4)))

    V=PW.volume123_matrix(6,6,6)
    A=psi.reshape(7**3,7); Vpsi=(V@A).reshape(7,7,7,7)
    mean=float(np.vdot(psi,Vpsi).real)
    second=float(np.vdot(Vpsi,Vpsi).real)
    sigma=math.sqrt(max(0.0,second-mean*mean))

    qpsi=np.zeros_like(psi)
    for a,b,c in itertools.product(range(3),repeat=3):
        e=eps3(a,b,c)
        if not e:continue
        x=PW.apply_axis_np(psi,2,mats[c]);x=PW.apply_axis_np(x,1,mats[b]);x=PW.apply_axis_np(x,0,mats[a])
        qpsi+=e*x
    qmean=float(np.vdot(psi,qpsi).real)
    qsecond=float(np.vdot(qpsi,qpsi).real)

    passed=(rel<tol and closure<tol and abs(eig[0])<tol and
            max(abs(eig[i]-16) for i in (1,2,3))<tol and mean>0)
    return {
      'status':'metric content of canonical barycentric rank-one j=3 background',
      'passed':bool(passed),'tolerance':tol,
      'coarse_face_spin':3.0,
      'selected_intertwiner_vector_K2_0_to_12':TARGET.tolist(),
      'flux_Gram':gram.tolist(),'regular_tetrahedron_target':regular.tolist(),
      'relative_regular_Gram_defect':rel,'Gram_eigenvalues':eig.tolist(),
      'closure_residual':closure,
      'absolute_volume_mean_up_to_scale':mean,
      'absolute_volume_sigma_up_to_scale':sigma,
      'absolute_volume_relative_fluctuation':sigma/mean,
      'oriented_volume_mean':qmean,'oriented_volume_second_moment':qsecond,
      'conclusion':'The static rank-one spatial block selects an exactly isotropic nondegenerate regular-tetrahedron flux background, but its single-block volume fluctuation is still large; shape/kinetic tangent directions must come from enlarged dynamical sectors.',
      'scope_note':'Finite one-block geometry expectation. It is not yet a continuum metric-dimension or semiclassical-fluctuation scaling result.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);ap.add_argument('--tol',type=float,default=1e-12)
    a=ap.parse_args();o=run(a.tol);t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
