#!/usr/bin/env python3
"""Compatibility surface for reusing validated local covariant Peter-Weyl legs on a PL dual complex.

This module does not define new Lorentzian physics. It exposes the graph-dependent
objects expected by the existing charged/covariant leg algebra through the
already validated `PLPeterWeylEuclidean` engine. Full PL Lorentzian use remains
conditional on explicit K5-equivalence tests for each promoted layer.
"""
from __future__ import annotations
import contextlib
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as KPW
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

class PLCompat:
    def __init__(self,G:PLPeterWeylEuclidean):
        self.G=G;self.VERT=G.VERT;self.EDGES=G.EDGES
        self.NEIG={v:tuple(G.dual.neighbor[(v,r)] for r in range(4)) for v in self.VERT}
        for name in ('epsilon_j','apply_axis_np','m2vals_t','allowed_k2_t','hit_mats'):
            setattr(self,name,getattr(KPW,name))
    def local_spins(self,spins,v):return self.G.local_spins(spins,v)
    def oriented_intertwiner(self,v,spins_local,K):return self.G.oriented_intertwiner(v,tuple(spins_local),K)
    def initial_factorized_oriented(self,key):return self.G.initial_factorized_oriented(key)
    def apply_hit_branch(self,*args,**kwargs):return self.G.apply_hit_branch(*args,**kwargs)
    def apply_path_branch(self,*args,**kwargs):return self.G.apply_path_branch(*args,**kwargs)
    def apply_volume_tensor_oriented(self,*args,**kwargs):return self.G.apply_volume_tensor_oriented(*args,**kwargs)
    def basis_full_jhalf(self):return [((1,)*len(self.EDGES),(0,)*len(self.VERT))]
    @staticmethod
    def add_dict(dst,src,scale=1.0):
        for k,a in src.items():
            z=dst.get(k,0j)+scale*a
            if abs(z)>1e-13:dst[k]=z
            elif k in dst:del dst[k]
    @staticmethod
    def prune_state(st,tol=1e-8):return {k:v for k,v in st.items() if abs(v)>tol}
    @staticmethod
    def norm2_state(st):return float(sum(abs(v)**2 for v in st.values()))
    def oriented_specs(self,v):
        out=[];neigh=self.NEIG[v]
        for r in range(4):
            tri=tuple(neigh[i] for i in range(4) if i!=r);sign=self.G.dual.local_sign(v,r);a,b,c=tri
            out += [(sign,(v,a,b,c)),(sign,(v,b,c,a)),(sign,(v,c,a,b))]
        return tuple(out)
    def T_sequences(self,v,a,b,c):
        return self.G.T_sequences(v,self.G.LEGIDX[(v,a)],self.G.LEGIDX[(v,b)],self.G.LEGIDX[(v,c)])
    def adjoint_sequence(self,seq):return self.G.adjoint_sequence(seq)
    def apply_T_cached_state(self,state,spec,Jmax2,adj=False):
        v,a,b,c=spec;ra=self.G.LEGIDX[(v,a)];rb=self.G.LEGIDX[(v,b)];rc=self.G.LEGIDX[(v,c)];out={}
        for key,amp0 in state.items():
            for ko,z in self.G.T_items(key,v,ra,rb,rc,Jmax2,adj):out[ko]=out.get(ko,0j)+amp0*z
        return {k:v for k,v in out.items() if abs(v)>1e-10}
    def apply_H_cached_state(self,state,v,Jmax2):return self.G.H_sine_state(state,v,Jmax2,1e-10)

@contextlib.contextmanager
def patched_pw(compat,*modules):
    old=[]
    try:
        for module in modules:
            if hasattr(module,'PW'):
                old.append((module,module.PW));module.PW=compat
        yield compat
    finally:
        for module,pw in reversed(old):module.PW=pw
