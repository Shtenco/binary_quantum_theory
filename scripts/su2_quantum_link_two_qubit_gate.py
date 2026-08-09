#!/usr/bin/env python3
"""Exact two-qubit spinor representation of an SU(2) quantum link.

Five 4x4 Clifford matrices generate so(5).  The so(4) subalgebra splits into
commuting su(2)_L + su(2)_R generators, while the remaining four generators
form an operator-valued SU(2) link transporter.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)
SIG=[X,Y,Z]
GAMMA=[np.kron(X,X),np.kron(X,Y),np.kron(X,Z),np.kron(Y,I),np.kron(Z,I)]


def eps3():
    e=np.zeros((3,3,3),int)
    for p in itertools.permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        e[p]=-1 if inv%2 else 1
    return e
EPS=eps3()


def Mab(a,b):
    if a==b:return np.zeros((4,4),complex)
    if a>b:return -Mab(b,a)
    return (-1j/4)*(GAMMA[a]@GAMMA[b]-GAMMA[b]@GAMMA[a])


def build():
    J=[]
    for a in range(3):
        op=np.zeros((4,4),complex)
        for b in range(3):
            for c in range(3):op+=0.5*EPS[a,b,c]*Mab(b,c)
        J.append(op)
    K=[Mab(a,3) for a in range(3)]
    L=[0.5*(J[a]+K[a]) for a in range(3)]
    R=[0.5*(J[a]-K[a]) for a in range(3)]
    U0=Mab(3,4); Ua=[Mab(a,4) for a in range(3)]
    U=np.empty((2,2),dtype=object)
    for i in range(2):
        for j in range(2):
            op=(1.0 if i==j else 0.0)*U0
            for a in range(3):op=op+1j*SIG[a][i,j]*Ua[a]
            U[i,j]=op
    return L,R,U


def run():
    L,R,U=build(); I4=np.eye(4)
    cliff=max(np.linalg.norm(GAMMA[a]@GAMMA[b]+GAMMA[b]@GAMMA[a]-2*(1 if a==b else 0)*I4) for a in range(5) for b in range(5))
    def rhs_so(a,b,c,d):
        return 1j*((1 if a==c else 0)*Mab(b,d)-(1 if a==d else 0)*Mab(b,c)-(1 if b==c else 0)*Mab(a,d)+(1 if b==d else 0)*Mab(a,c))
    so5=max(np.linalg.norm(Mab(a,b)@Mab(c,d)-Mab(c,d)@Mab(a,b)-rhs_so(a,b,c,d)) for a in range(5) for b in range(a+1,5) for c in range(5) for d in range(c+1,5))
    suL=max(np.linalg.norm(L[a]@L[b]-L[b]@L[a]-1j*sum(EPS[a,b,c]*L[c] for c in range(3))) for a in range(3) for b in range(3))
    suR=max(np.linalg.norm(R[a]@R[b]-R[b]@R[a]-1j*sum(EPS[a,b,c]*R[c] for c in range(3))) for a in range(3) for b in range(3))
    lr=max(np.linalg.norm(L[a]@R[b]-R[b]@L[a]) for a in range(3) for b in range(3))
    left=0.;right=0.
    for a in range(3):
        for i in range(2):
            for j in range(2):
                c=L[a]@U[i,j]-U[i,j]@L[a]
                target=-sum(SIG[a][i,k]*U[k,j]/2 for k in range(2))
                left=max(left,float(np.linalg.norm(c-target)))
                c=R[a]@U[i,j]-U[i,j]@R[a]
                target=sum(U[i,k]*SIG[a][k,j]/2 for k in range(2))
                right=max(right,float(np.linalg.norm(c-target)))
    casL=np.linalg.eigvalsh(sum(x@x for x in L));casR=np.linalg.eigvalsh(sum(x@x for x in R))
    passed=max(cliff,so5,suL,suR,lr,left,right)<1e-12
    return {"status":"exact finite two-qubit SU(2) quantum-link algebra","passed":bool(passed),"hilbert_dimension":4,"qubits_per_link":2,"errors":{"Clifford":float(cliff),"so5":float(so5),"su2_left":float(suL),"su2_right":float(suR),"left_right_commute":float(lr),"U_left_covariance":float(left),"U_right_covariance":float(right)},"left_Casimir_spectrum":casL.tolist(),"right_Casimir_spectrum":casR.tolist(),"link_transformation_convention":"[L^a,U]=-(sigma^a/2)U; [R^a,U]=+U(sigma^a/2)","scope_note":"This closes the finite link kinematics only. The gravity Hamiltonian, representation growth and continuum limit remain separate gates."}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);a=ap.parse_args();out=run();txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1
if __name__=="__main__":raise SystemExit(main())
