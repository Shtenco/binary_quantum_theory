#!/usr/bin/env python3
"""Exact runtime-cache wrapper for the first real Peter-Weyl K-K-V triple.

The structural amplitude and all thresholds remain in
peter_weyl_lorentzian_ordered_triple_gate.py.  This wrapper memoizes only exact
deterministic sparse-state maps used repeatedly across the eight auxiliary
index paths.  Cache keys include every discrete label and exact complex
amplitude; no rounding, pruning, fitting or reduced-representation shortcut is
introduced.
"""
from __future__ import annotations

import argparse
import functools
import json
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import peter_weyl_lorentzian_ordered_triple_gate as TRIPLE


def freeze_state(state):
    return tuple(sorted(state.items(),key=lambda kv:repr(kv[0])))


def run(v=0,a=None,b=None,c=None):
    KC=TRIPLE.KCOMP
    CV=TRIPLE.COMP

    orig_he=KC.CK.apply_HE_complete_key
    orig_k=KC.apply_K_complete_custom
    orig_inv=KC.COMP.inverse_complete
    orig_direct=KC.direct_K_covariant
    orig_close=KC.COMP.close_complete
    orig_ck=KC.C_K_component
    orig_cv=CV.C_volume_component

    cached_he=functools.lru_cache(maxsize=None)(orig_he)

    @functools.lru_cache(maxsize=None)
    def k_frozen(frozen,source_v,Jmax2,charged_nodes):
        out,x,y=orig_k(dict(frozen),source_v,Jmax2,tuple(charged_nodes))
        return tuple(out.items()),float(x),float(y)
    def k_cached(state,source_v,Jmax2,charged_nodes):
        items,x,y=k_frozen(freeze_state(state),source_v,Jmax2,tuple(charged_nodes))
        return dict(items),x,y

    @functools.lru_cache(maxsize=None)
    def inv_frozen(frozen,source_v,target_v,i,j,Jmax2):
        out,x=orig_inv(dict(frozen),source_v,target_v,i,j,Jmax2)
        return tuple(out.items()),float(x)
    def inv_cached(state,source_v,target_v,i,j,Jmax2):
        items,x=inv_frozen(freeze_state(state),source_v,target_v,i,j,Jmax2)
        return dict(items),x

    @functools.lru_cache(maxsize=None)
    def direct_frozen(frozen,source_v,Jmax2):
        out,x,y=orig_direct(dict(frozen),source_v,Jmax2)
        return tuple(out.items()),float(x),float(y)
    def direct_cached(state,source_v,Jmax2):
        items,x,y=direct_frozen(freeze_state(state),source_v,Jmax2)
        return dict(items),x,y

    @functools.lru_cache(maxsize=None)
    def close_frozen(frozen,source_v,target_v,i,k,Jmax2):
        out=orig_close(dict(frozen),source_v,target_v,i,k,Jmax2)
        return tuple(out.items())
    def close_cached(state,source_v,target_v,i,k,Jmax2):
        return dict(close_frozen(freeze_state(state),source_v,target_v,i,k,Jmax2))

    @functools.lru_cache(maxsize=None)
    def ck_frozen(frozen,source_v,target_v,i,j,Jmax2):
        out,diag=orig_ck(dict(frozen),source_v,target_v,i,j,Jmax2)
        return tuple(out.items()),tuple(sorted(diag.items()))
    def ck_cached(state,source_v,target_v,i,j,Jmax2):
        items,diag=ck_frozen(freeze_state(state),source_v,target_v,i,j,Jmax2)
        return dict(items),dict(diag)

    @functools.lru_cache(maxsize=None)
    def cv_frozen(frozen,source_v,target_v,i,j,Jmax2):
        out,leak=orig_cv(dict(frozen),source_v,target_v,i,j,Jmax2)
        return tuple(out.items()),float(leak)
    def cv_cached(state,source_v,target_v,i,j,Jmax2):
        items,leak=cv_frozen(freeze_state(state),source_v,target_v,i,j,Jmax2)
        return dict(items),leak

    KC.CK.apply_HE_complete_key=cached_he
    KC.apply_K_complete_custom=k_cached
    KC.COMP.inverse_complete=inv_cached
    KC.direct_K_covariant=direct_cached
    KC.COMP.close_complete=close_cached
    KC.C_K_component=ck_cached
    CV.C_volume_component=cv_cached
    try:
        out=TRIPLE.run(v,a,b,c)
        infos={
            'HE_key':cached_he.cache_info(),
            'K_state':k_frozen.cache_info(),
            'inverse_state':inv_frozen.cache_info(),
            'direct_K_state':direct_frozen.cache_info(),
            'close_state':close_frozen.cache_info(),
            'C_K_component':ck_frozen.cache_info(),
            'C_V_component':cv_frozen.cache_info(),
        }
    finally:
        KC.CK.apply_HE_complete_key=orig_he
        KC.apply_K_complete_custom=orig_k
        KC.COMP.inverse_complete=orig_inv
        KC.direct_K_covariant=orig_direct
        KC.COMP.close_complete=orig_close
        KC.C_K_component=orig_ck
        CV.C_volume_component=orig_cv

    out['runtime_memoization']={
        name:{'hits':x.hits,'misses':x.misses,'currsize':x.currsize}
        for name,x in infos.items()
    }
    out['runtime_memoization']['cache_keys_use_full_exact_sparse_states']=True
    out['runtime_memoization']['physics_changed']=False
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--v',type=int,default=0)
    ap.add_argument('--a',type=int)
    ap.add_argument('--b',type=int)
    ap.add_argument('--c',type=int)
    ap.add_argument('--output',type=Path)
    x=ap.parse_args(); out=run(x.v,x.a,x.b,x.c); text=json.dumps(out,indent=2); print(text)
    if x.output:
        x.output.parent.mkdir(parents=True,exist_ok=True)
        x.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out.get('passed',False) else 1

if __name__=='__main__':
    raise SystemExit(main())
