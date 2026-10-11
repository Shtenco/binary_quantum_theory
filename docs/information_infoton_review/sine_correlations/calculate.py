"""Free lattice vacuum benchmark. Not a derivation from full BQG constraints."""
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

def variance_ratio(L,n):
    # a=c=hbar=1; spherical coordinates restricted exactly to cubic BZ.
    mu,wm=leggauss(n); phi=np.arange(2*n)*np.pi/n
    dirs=np.stack(np.broadcast_arrays(np.sqrt(1-mu[:,None]**2)*np.cos(phi),np.sqrt(1-mu[:,None]**2)*np.sin(phi),mu[:,None]+np.zeros_like(phi)),axis=-1).reshape(-1,3)
    angular=np.repeat(wm,2*n)*np.pi/n
    xmax=np.minimum(9.,np.pi*L/np.max(abs(dirs),axis=1))
    z,w=leggauss(n)
    t=(z[:,None]+1)*xmax[None,:]/2
    k=t[:,:,None]*dirs[None,:,:]/L
    om=2*np.sqrt(np.sum(np.sin(k/2)**2,axis=-1))
    integral=np.sum(w[:,None]*xmax[None,:]/2 * angular[None,:]*t*t*np.exp(-t*t)/(L*om))
    # V= integral/(2(2pi)^3 L^2); continuum V=1/(8pi² L²)
    return float(integral/(2*np.pi))
rows=[]
for L in [2,4,8,16]:
    lo=variance_ratio(L,24);hi=variance_ratio(L,40)
    rows.append({'L_over_a':L,'V_lattice_over_continuum':hi,'quadrature_difference':abs(hi-lo),'scaled_leading_coefficient':(hi-1)*L*L,'V_hbar_c_units':hi/(8*np.pi**2*L*L)})
# actual finite periodic dynamical matrix, ground-state covariance, zero removed
N=7
D=np.zeros((N,N))
for j in range(N):D[j,j]=2;D[j,(j+1)%N]=-1;D[j,(j-1)%N]=-1
w,U=np.linalg.eigh(D); mask=w>1e-12
C=(U[:,mask]*(1/(2*np.sqrt(w[mask]))))@U[:,mask].T
res={'scope':'quadratic nearest-neighbor free vacuum, not physical BQG history','dispersion':'omega^2=4 c^2/a^2 sum sin^2(k_i a/2)','vacuum_spectrum':'S(k)=hbar/(2 omega(k))','continuum_variance':'hbar/(8 pi^2 c L^2)','leading_correction':'V_lattice/V_continuum=1+a^2/(40 L^2)+O(a^4/L^4)','rows':rows,'finite_covariance_min_eigenvalue':float(np.linalg.eigvalsh(C)[0]),'ground_state_equation_error':float(np.linalg.norm(D@C@C-(np.eye(N)-np.ones((N,N))/N)/4)),'zero_mode':'removed; massless periodic constant mode has no normalizable oscillator vacuum','discrete_time_stability':'c dt/a <= 1/sqrt(3); sine time rule alone does not imply positive Hamiltonian','HDA_warning':'sin^2(delta K) replacement implies beta=cos(2 delta K) in reviewed reduced ansatz; beta may become negative'}
assert res['ground_state_equation_error']<1e-12
assert all(r['quadrature_difference']<1e-7 for r in rows)
assert abs(rows[-1]['scaled_leading_coefficient']-.025)<1e-4
Path(__file__).with_name('results.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
