import json
from pathlib import Path
import numpy as np
out=Path(__file__).parent
pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1])]
J=[]
for s in pauli:
    total=np.zeros((16,16),complex)
    for site in range(4):
        term=np.array([[1]],complex)
        for i in range(4): term=np.kron(term,s/2 if i==site else np.eye(2))
        total+=term
    J.append(total)
cas=sum(x@x for x in J)
w,v=np.linalg.eigh(cas)
p0=v[:,abs(w)<1e-10]@v[:,abs(w)<1e-10].conj().T
p2=v[:,abs(w-6)<1e-10]@v[:,abs(w-6)<1e-10].conj().T
ph=np.zeros((16,16));ph[0,0]=ph[-1,-1]=1
up=np.eye(16)[:,0]
g=.1; m=1.
res={'scope':'finite controls and necessary-condition checks; not BQG physical history',
'gauss_spin2':{'singlet_rank':int(round(np.trace(p0).real)),'spin2_rank':int(round(np.trace(p2).real)),'orthogonality_norm':float(np.linalg.norm(p0@p2)),'extremal_state_casimir':float(np.vdot(up,cas@up).real),'helicity_subspace_Jx_leakage':float(np.linalg.norm((np.eye(16)-ph)@J[0]@up))},
'constant_mass_mixing':{'g':g,'M_squared':m,'eigenvalues':np.linalg.eigvalsh([[0,g],[g,m]]).tolist(),'determinant':-g*g,'scope':'positive kinetic metric, flat quadratic two-field model'},
'extra_spatial_dimensions':{'massless_spin2_polarizations':{str(D):D*(D-3)//2 for D in [4,5,6]},'compact_circle':'k_n=n/R; illustrative discrete eigenvalue 4/a_y^2 sin^2(pi*n/N_y), not derived from BQG'},
'finite_hermitian_2T':{'result':'only trivial exact triple','assumptions':'finite dimension, positive inner product, self-adjoint Q11,Q12,Q22, exact Sp(2,R) commutators','proof':'Tr(Q11[Q11,Q12])=0=2i*hbar*Tr(Q11^2), hence Q11=0; remaining relations imply Q12=Q22=0','escape_conditions':'infinite-dimensional/domain limit or different parent construction; finite abstract non-Hermitian sl2 matrices do not evade these assumptions'}}
assert np.linalg.norm(p0@p2)<1e-12
assert res['gauss_spin2']['singlet_rank']==2 and res['gauss_spin2']['spin2_rank']==5
assert res['constant_mass_mixing']['eigenvalues'][0]<0
(out/'hypothesis_checks.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
