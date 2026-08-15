#!/usr/bin/env python3
"""Collect preregistered EE/EL/LE/LL artifacts into the exact signed [G0,G1].

Frozen beta=hbar=1 raw-code coefficients:

    G_v = a E_v + b L_v,
    a   = -2/3,
    b   = 32 i / 9.

Hence

    [G0,G1] = a^2 EE + a b EL + a b LE + b^2 LL.

No normalization, sign, channel selection or subtraction is inferred from the
channel results; all weights are constants frozen upstream.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

CHANNELS=('EE','EL','LE','LL')
A=-2.0/3.0
B=32.0j/9.0
WEIGHTS={'EE':A*A,'EL':A*B,'LE':A*B,'LL':B*B}


def load_state(path):
    z=np.load(path,allow_pickle=False)
    out={}
    for spins,Ks,amp in zip(z['spins'],z['Ks'],z['amp']):
        key=(tuple(int(x) for x in spins),tuple(int(x) for x in Ks))
        out[key]=complex(amp)
    return out


def save_state(path,state):
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]))
    if rows:
        spins=np.asarray([k[0] for k,_ in rows],dtype=np.int16)
        Ks=np.asarray([k[1] for k,_ in rows],dtype=np.int16)
        amp=np.asarray([a for _,a in rows],dtype=np.complex128)
    else:
        spins=np.zeros((0,10),dtype=np.int16)
        Ks=np.zeros((0,5),dtype=np.int16)
        amp=np.zeros((0,),dtype=np.complex128)
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)


def add(dst,src,scale=1.0,tol=1e-10):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol:
            dst[k]=z
        elif k in dst:
            del dst[k]


def norm2(s):
    return float(sum(abs(a)**2 for a in s.values()))


def max_spin(s):
    return max((max(k[0]) for k in s),default=0)/2.0


def inner(a,b):
    if len(a)>len(b):
        return np.conj(inner(b,a))
    return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())


def run(input_dir):
    input_dir=Path(input_dir)
    states={}; meta={}
    for ch in CHANNELS:
        jp=input_dir/f'{ch}.json'
        sp=input_dir/f'{ch}.npz'
        if not jp.exists() or not sp.exists():
            raise FileNotFoundError(f'missing {ch} artifact under {input_dir}')
        meta[ch]=json.loads(jp.read_text(encoding='utf-8'))
        states[ch]=load_state(sp)

    total={}
    weighted={}
    for ch in CHANNELS:
        w=WEIGHTS[ch]
        st={k:w*a for k,a in states[ch].items()}
        weighted[ch]=st
        add(total,states[ch],w)

    # Channel Gram matrix exposes cancellation/interference rather than hiding it.
    gram={}
    for a in CHANNELS:
        gram[a]={}
        for b in CHANNELS:
            z=inner(weighted[a],weighted[b])
            gram[a][b]=[float(z.real),float(z.imag)]

    channel_summary={
        ch:{
            'raw_support':len(states[ch]),
            'raw_norm':math.sqrt(norm2(states[ch])),
            'weight':[float(WEIGHTS[ch].real),float(WEIGHTS[ch].imag)],
            'weighted_norm':math.sqrt(norm2(weighted[ch])),
            'max_spin':max_spin(states[ch]),
            'worker_passed':bool(meta[ch].get('passed',False)),
        }
        for ch in CHANNELS
    }

    checks={
        'all_workers_passed':all(meta[ch].get('passed',False) for ch in CHANNELS),
        'frozen_a':abs(A+2/3)<1e-15,
        'frozen_b':abs(B-32j/9)<1e-15,
        'frozen_EE_weight':abs(WEIGHTS['EE']-4/9)<1e-15,
        'frozen_mixed_weight':abs(WEIGHTS['EL']+64j/27)<1e-15 and abs(WEIGHTS['LE']+64j/27)<1e-15,
        'frozen_LL_weight':abs(WEIGHTS['LL']+1024/81)<1e-14,
        'finite_total_norm':math.isfinite(math.sqrt(norm2(total))),
        'finite_channel_gram':all(np.isfinite(x) for a in gram.values() for z in a.values() for x in z),
        'total_spin_within_LL_wall':max_spin(total)<=6.5+1e-12,
    }
    return total,{
        'status':'preregistered exact signed full Peter-Weyl geometry commutator collector',
        'passed':all(checks.values()),
        'preregistration':'PETER_WEYL_FULL_GEOMETRY_COMMUTATOR_PREREGISTRATION.md',
        'beta':1.0,'hbar':1.0,
        'raw_node_operator':'G_v=(-2/3) E_v + (32 i/9) L_raw,v',
        'weights':{ch:[float(w.real),float(w.imag)] for ch,w in WEIGHTS.items()},
        'channels':channel_summary,
        'weighted_channel_gram':gram,
        'full_commutator_support':len(total),
        'full_commutator_norm':math.sqrt(norm2(total)),
        'full_commutator_max_spin':max_spin(total),
        'checks':checks,
        'HDA_claim':False,
        'next_use':'Insert the antisymmetric nonconstant-lapse factor and the exact two-node operator-first route block, then test regulator scaling against the diffeomorphism target.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir',type=Path,required=True)
    p.add_argument('--json-output',type=Path,required=True)
    p.add_argument('--state-output',type=Path,required=True)
    a=p.parse_args(); state,out=run(a.input_dir)
    a.json_output.parent.mkdir(parents=True,exist_ok=True)
    a.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    save_state(a.state_output,state)
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
