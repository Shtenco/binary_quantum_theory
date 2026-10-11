#!/usr/bin/env python3
"""Bell-volume tradeoff for frozen q2 four-face Gauss singlet.
Kinematic SU(2) theorem only; NOT full BQG physical Bell, HDA, or TT.
Full checks/JSON also available in companion downloadable study packet.
"""
import sympy as s
rt2=s.sqrt(2); rt3=s.sqrt(3); I=s.I
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
pauli=(X,Y,Z); ID=s.eye(2);ket=lambda bits:s.eye(16)[:,int(bits,2)]
u=(ket('0101')-ket('0110')-ket('1001')+ket('1010'))/2
v=(ket('0011')+ket('1100')-(ket('0101')+ket('0110')+ket('1001')+ket('1010'))/2)/rt3
assert (u.H*u)[0]==1 and (v.H*v)[0]==1 and (u.H*v)[0]==0
def face(i,k):
    a=[ID]*4;a[i]=pauli[k]/2;return s.kronecker_product(*a)
Q=s.zeros(16)
for a in range(3):
    for b in range(3):
        for c in range(3):
            if s.LeviCivita(a,b,c):Q+=s.LeviCivita(a,b,c)*face(0,a)*face(1,b)*face(2,c)
V=s.Matrix.hstack(u,v)
assert s.simplify(V.H*Q*V-rt3*Y/4)==s.zeros(2)
singlet=s.Matrix([0,1,-1,0])/rt2
Ps=singlet*singlet.H
def reduced(psi,a,b):
    other=[i for i in range(4) if i not in [a,b]]
    rho=s.zeros(4)
    for i in range(16):
        bit_i=[(i>>(3-t))&1 for t in range(4)]
        for j in range(16):
            bit_j=[(j>>(3-t))&1 for t in range(4)]
            if all(bit_i[t]==bit_j[t] for t in other):
                rho[2*bit_i[a]+bit_i[b],2*bit_j[a]+bit_j[b]]+=psi[i]*s.conjugate(psi[j])
    return s.simplify(rho)
for psi in ((u+I*v)/rt2,(u-I*v)/rt2):
    for a,b in ((0,1),(0,2),(0,3)):
        rho=reduced(psi,a,b)
        p=s.simplify(s.trace(rho*Ps))
        assert p==s.Rational(1,2)
        assert s.simplify(rho-(Ps/s.Integer(2)+(s.eye(4)-Ps)/6))==s.zeros(4)
        pt=s.Matrix(4,4,lambda i,j:rho[2*(i//2)+(j%2),2*(j//2)+(i%2)])
        assert pt.eigenvals()=={s.Rational(1,3):3,s.S.Zero:1}
        assert s.simplify(2*rt2*s.Abs(1-4*p)/3)==2*rt2/3
alpha,phi=s.symbols('alpha phi',real=True)
p=s.cos(alpha)**2
q=rt3*s.sin(2*alpha)*s.sin(phi)/4
assert s.trigsimp(3*p*(1-p)/4-q**2-3*s.sin(2*alpha)**2*s.cos(phi)**2/16)==0
pcrit=(1+3/rt2)/4
ucrit=s.simplify(s.sqrt(4*pcrit*(1-pcrit)))
assert abs(float(ucrit)-0.8280459961740176)<1e-13
Ja=[s.kronecker_product(pauli[a],ID)+s.kronecker_product(ID,pauli[a]) for a in range(3)]
units=[s.eye(4)[:,i]*s.eye(4)[j,:] for i in range(4) for j in range(4)]
C=s.Matrix.vstack(*[s.Matrix.hstack(*[(J*w-w*J).reshape(16,1) for w in units]) for J in Ja])
assert 16-C.rank()==2 # two-face SU2-invariant algebra is abelian
assert s.simplify((2*s.Integer(1)/3)*(1+s.sqrt(7)))>2 # kinematic 4x4 blocks
print('PASS: q2 exact Bell-volume bound, pair PPT, and gauge-invariant 2-face no-go')
print('S_max at max volume =',2*rt2/3)
print('CHSH pair violation requires p >',pcrit,'and |<Q>|/Qmax <',ucrit)
print('Physical Lorentzian HDA and TT pole: OPEN')
