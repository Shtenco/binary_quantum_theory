#!/usr/bin/env python3
"""Operator-valued frame-sign covariance of the 24-term Lorentzian epsilon assembler.

Using deterministic noncommuting geometry matrices for the four covariant K legs
and V legs, evaluate exactly the same oriented 24-term sum used by the existing
Lorentzian triple algebra gate, but with every possible ordering of the local
four-neighbor frame. With the physical edge operators held fixed, an odd frame
permutation must reverse the oriented epsilon sum:

    L_eps(frame_p)=sgn(p) L_eps(frame).

No cyclicity of the auxiliary partial trace is used.
"""
from __future__ import annotations
import itertools,json,numpy as np
import peter_weyl_lorentzian_triple_algebra_gate as ALG

SEED=20260814

def raw_for_frame(frame,K,V):
    out=np.zeros((ALG.GEOM_DIM,ALG.GEOM_DIM),complex)
    for r,omit in enumerate(frame):
        base=tuple(x for x in frame if x!=omit)
        face=(-1)**r
        for perm in itertools.permutations(base):
            a,b,c=perm
            out += face*ALG.parity(base,perm)*ALG.partial_trace_aux(K[a][0]@K[b][0]@V[c][0])
    return out

def sign_of_reordering(base,frame):
    idx=[base.index(x) for x in frame]
    inv=sum(idx[i]>idx[j] for i in range(4) for j in range(i+1,4))
    return -1 if inv%2 else +1

def run():
    rng=np.random.default_rng(SEED)
    K={e:ALG.covariant_operator(rng) for e in (1,2,3,4)}
    V={e:ALG.covariant_operator(rng) for e in (1,2,3,4)}
    base=(1,2,3,4)
    ref=raw_for_frame(base,K,V)
    refn=float(np.linalg.norm(ref))
    rows=[]; max_rel=0.0
    for frame in itertools.permutations(base):
        s=sign_of_reordering(base,frame)
        cur=raw_for_frame(frame,K,V)
        rel=float(np.linalg.norm(cur-s*ref)/max(refn,1e-30))
        max_rel=max(max_rel,rel)
        rows.append({'frame':list(frame),'sign':s,'relative_error':rel})
    passed=(refn>1e-8 and len(rows)==24 and max_rel<1e-12)
    return {
      'status':'operator-valued Lorentzian epsilon frame-sign gate',
      'passed':bool(passed),
      'seed':SEED,
      'reference_norm':refn,
      'frame_count':len(rows),
      'max_sign_covariance_relative_error':max_rel,
      'identity':'L_epsilon(frame_p)=sgn(p)L_epsilon(frame)',
      'rows':rows,
      'consequence':'The declared 24-term oriented assembler is an alternating/sign-character object under reversal of the local four-face frame. Combined with the logical S4 sign twirl, its symmetry-restored one-cell logical channel can only be proportional to Y.',
      'scope':'Synthetic noncommuting operator algebra only; this proves covariance of the assembler, not a nonzero Peter-Weyl amplitude, additional particle content, or a new interaction.'
    }
if __name__=='__main__':
    o=run(); print(json.dumps(o,indent=2)); raise SystemExit(0 if o['passed'] else 1)
