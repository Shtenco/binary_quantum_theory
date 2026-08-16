#!/usr/bin/env python3
"""Complete target-independent SU(2) recoupling basis for one coarse face.

A canonical barycentric coarse triangular face contains six fine boundary
links.  The old static block retained only the maximal symmetric all-j=1/2
channel J=3.  The dynamical producer must instead retain a complete unitary
basis, including total-J and multiplicity labels, for every fine-spin pattern
reached by the production operator.

This gate uses a frozen left-associated coupling tree

  (((((j1 j2)J12 j3)J123 j4)J1234 j5)J12345 j6)J,M

and verifies exact numerical unitarity for all ordered q4 one-E boundary spin
patterns: the all-j=1/2 baseline and every pattern with two of six links changed
to doubled spin 0 or 2.  It also proves the historical Dicke J=3 isometry is
exactly the maximal-J subblock of this complete basis.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW

TOL=1e-10


def allowed(a,b):
    return tuple(range(abs(a-b),a+b+1,2))


def coupled_rows(spins):
    s=tuple(spins);out=[]
    for J12 in allowed(s[0],s[1]):
      for J123 in allowed(J12,s[2]):
       for J1234 in allowed(J123,s[3]):
        for J12345 in allowed(J1234,s[4]):
         for J in allowed(J12345,s[5]):
          for M in PW.m2vals_t(J):
           out.append((J12,J123,J1234,J12345,J,M))
    return out


def recoupling_matrix(spins):
    s=tuple(spins)
    mvals=[PW.m2vals_t(x) for x in s]
    cols=list(itertools.product(*mvals));rows=coupled_rows(s)
    U=np.zeros((len(rows),len(cols)),complex)
    for ri,(J12,J123,J1234,J12345,J,M) in enumerate(rows):
      for ci,ms in enumerate(cols):
        m1,m2,m3,m4,m5,m6=ms
        M12=m1+m2;M123=M12+m3;M1234=M123+m4;M12345=M1234+m5
        if M12345+m6!=M:continue
        z=PW.cg2(s[0],s[1],J12,m1,m2,M12)
        z*=PW.cg2(J12,s[2],J123,M12,m3,M123)
        z*=PW.cg2(J123,s[3],J1234,M123,m4,M1234)
        z*=PW.cg2(J1234,s[4],J12345,M1234,m5,M12345)
        z*=PW.cg2(J12345,s[5],J,M12345,m6,M)
        U[ri,ci]=z
    return rows,cols,U


def dicke6():
    W=np.zeros((64,7),complex)
    for k in range(7):
        states=[b for b in itertools.product((0,1),repeat=6) if sum(b)==k]
        a=1/math.sqrt(len(states))
        for bits in states:
            idx=0
            for x in bits:idx=(idx<<1)|x
            W[idx,k]=a
    return W


def patterns():
    out={(1,1,1,1,1,1)}
    for i,j in itertools.combinations(range(6),2):
        for a,b in itertools.product((0,2),repeat=2):
            x=[1]*6;x[i]=a;x[j]=b;out.add(tuple(x))
    return sorted(out)


def run():
    rows=[];worst=0.0;Js=set();dims=[]
    for p in patterns():
        labels,cols,U=recoupling_matrix(p)
        defect=float(np.linalg.norm(U@U.conj().T-np.eye(len(labels))))
        back=float(np.linalg.norm(U.conj().T@U-np.eye(len(cols))))
        worst=max(worst,defect,back);dims.append(len(labels));Js.update(r[4] for r in labels)
        rows.append({'spins2':list(p),'dimension':len(labels),'unitarity_left_defect':defect,'unitarity_right_defect':back,'total_J2_support':sorted(set(r[4] for r in labels))})

    labels,cols,U=recoupling_matrix((1,1,1,1,1,1))
    idx=[i for i,r in enumerate(labels) if r[4]==6]
    U6=U[idx,:];W=dicke6();dicke=float(np.max(np.abs(U6-W.T)))
    checks={
        'all_q4_ordered_patterns_tested':len(rows)==61,
        'every_recoupling_square_complete':all(r['dimension'] in (16,48,64,144) for r in rows),
        'worst_unitarity_below_1e-10':worst<TOL,
        'q4_face_total_J2_union_0_2_4_6_8':sorted(Js)==[0,2,4,6,8],
        'historical_J3_Dicke_exact_subblock':dicke<TOL,
    }
    return {
        'status':'complete six-link coarse-face SU(2) recoupling isometry',
        'passed':bool(all(checks.values())),
        'coupling_tree':'(((((j1 j2)J12 j3)J123 j4)J1234 j5)J12345 j6)J,M',
        'patterns_tested':len(rows),
        'dimension_min':min(dims),'dimension_max':max(dims),
        'worst_unitarity_defect':worst,
        'maximal_J3_Dicke_max_abs_defect':dicke,
        'total_J2_support_union':sorted(Js),
        'checks':checks,'rows':rows,
        'interpretation':'The old fully symmetric j=3 face projection is one exact subblock of a complete target-independent boundary recoupling basis. Dynamic one-E sectors require the full J=0,1,2,3,4 support with multiplicity labels; retaining them introduces no GR target information.',
        'next_step':'Use these complete face labels when contracting the 36 internal links of the 24-chamber block and build the amplitude-level W_block from the actual E/S/R operator image.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
