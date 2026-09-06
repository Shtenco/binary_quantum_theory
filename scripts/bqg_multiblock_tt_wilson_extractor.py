#!/usr/bin/env python3
"""Fail-closed BQG multi-block Schur -> metric -> TT -> six-Wilson extractor.

This script introduces no new physical operator.  It consumes an already-produced
collective multi-block BQG constraint matrix in the frozen six-coordinate metric
carrier, performs the zero-energy Schur/Feshbach reduction on gapped Q modes,
applies the measured q->metric map, forms the nearest-neighbour Fourier symbol,
projects to TT, and extracts the six canonical parity-even S4 quartic Wilson
coefficients.

If the input contains a Q zero mode coupled to P, an incomplete/non-production
operator, a non-tetrahedral neighbour shell, or a non-GR leading TT sector, the
script stops and does not report c1..c6 as a BQG science result.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
try:
    import s4_tt_six_wilson_predictor as WILSON
except Exception:
    WILSON = None

RTOL = 1e-10
GEOM_TOL = 2e-9
LEADING_TOL = 2e-6
FIT_TOL = 2e-8

# Frozen L1 metric map reconstructed from
# scripts/collective_l1_coarse_flux_response_gate.py:
# M_hq = (J_F^bg)^(-1) B_F, with C_face=9/2 and opposite response=-sqrt(3).
# Coordinate order h=(xx,yy,zz,sqrt(2)xy,sqrt(2)xz,sqrt(2)yz).
def frozen_metric_map() -> np.ndarray:
    a = 1.0 / math.sqrt(12.0)
    b = 1.0 / math.sqrt(6.0)
    return np.asarray([
        [a,0,0,0,0,a],
        [0,a,0,0,a,0],
        [0,0,a,a,0,0],
        [0,0,b,-b,0,0],
        [0,b,0,0,-b,0],
        [b,0,0,0,0,-b],
    ], float)


def hermitian_defect(A: np.ndarray) -> float:
    return float(np.linalg.norm(A - A.conj().T) / max(np.linalg.norm(A), 1e-300))


def blockdiag(A: np.ndarray, n: int) -> np.ndarray:
    return np.kron(np.eye(n), A)


def load_metadata(z) -> dict:
    if 'metadata_json' not in z.files:
        return {}
    raw = z['metadata_json']
    if np.ndim(raw) == 0:
        raw = raw.item()
    if isinstance(raw, bytes):
        raw = raw.decode('utf-8')
    return json.loads(str(raw))


def validate_provenance(meta: dict) -> tuple[bool, list[str]]:
    errors = []
    if meta.get('actual_bqg_operator') is not True:
        errors.append('metadata.actual_bqg_operator must be true')
    if meta.get('synthetic') is not False:
        errors.append('metadata.synthetic must be false')
    comps = set(meta.get('operator_components', []))
    if not {'E','S','R_op'} <= comps:
        errors.append('operator_components must contain E,S,R_op')
    if not str(meta.get('source_commit', '')).strip():
        errors.append('source_commit is required')
    if not meta.get('regulator'):
        errors.append('regulator declaration is required')
    if meta.get('target_fitting_used') is not False:
        errors.append('target_fitting_used must be false')
    return not errors, errors


def schur_zero_energy(C: np.ndarray, pidx: np.ndarray, rtol: float = RTOL) -> dict:
    C = np.asarray(C, complex)
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError('C_full must be square')
    if hermitian_defect(C) > 5e-9:
        raise RuntimeError(f'C_full is not Hermitian: defect={hermitian_defect(C):.3e}')
    n = C.shape[0]
    pidx = np.asarray(pidx, int).ravel()
    if len(set(map(int, pidx))) != len(pidx) or np.any(pidx < 0) or np.any(pidx >= n):
        raise ValueError('invalid p_indices')
    mask = np.ones(n, dtype=bool); mask[pidx] = False
    qidx = np.flatnonzero(mask)
    CPP = C[np.ix_(pidx,pidx)]
    if qidx.size == 0:
        return {
            'Ceff': CPP.copy(), 'q_indices': qidx, 'q_eigenvalues': np.asarray([]),
            'q_gap': None, 'q_spectral_radius': None, 'q_condition': None,
            'zero_mode_count': 0, 'coupled_zero_mode_norm': 0.0,
            'zero_modes_uncoupled': True,
        }
    CPQ = C[np.ix_(pidx,qidx)]
    A = C[np.ix_(qidx,qidx)]
    vals,U = np.linalg.eigh((A + A.conj().T)/2)
    scale = max(float(np.max(np.abs(vals))), 1.0)
    nz = np.abs(vals) > rtol * scale
    zmask = ~nz
    coupled_zero = 0.0
    if np.any(zmask):
        coupled_zero = float(np.linalg.norm(CPQ @ U[:,zmask]) / max(np.linalg.norm(C),1e-300))
        if coupled_zero > 20*rtol:
            raise RuntimeError(
                'GAPLESS_COUPLED_Q_MODE_REQUIRES_PROMOTION: '
                f'{int(np.sum(zmask))} Q zero modes, relative coupling={coupled_zero:.3e}'
            )
    invvals = np.zeros_like(vals)
    invvals[nz] = 1.0 / vals[nz]
    Ainv = (U * invvals) @ U.conj().T
    Ceff = CPP - CPQ @ Ainv @ CPQ.conj().T
    Ceff = (Ceff + Ceff.conj().T)/2
    av = np.abs(vals[nz])
    gap = float(np.min(av)) if av.size else None
    radius = float(np.max(av)) if av.size else None
    cond = float(radius/gap) if gap not in (None,0.0) else None
    return {
        'Ceff': Ceff, 'q_indices': qidx, 'q_eigenvalues': vals,
        'q_gap': gap, 'q_spectral_radius': radius, 'q_condition': cond,
        'zero_mode_count': int(np.sum(zmask)), 'coupled_zero_mode_norm': coupled_zero,
        'zero_modes_uncoupled': coupled_zero <= 20*rtol,
    }


def canonicalize_p(Ceff: np.ndarray, p_block: np.ndarray, p_coord: np.ndarray,
                   positions: np.ndarray, central_block: int) -> tuple[np.ndarray,list[int]]:
    p_block=np.asarray(p_block,int).ravel(); p_coord=np.asarray(p_coord,int).ravel()
    if p_block.size != Ceff.shape[0] or p_coord.size != Ceff.shape[0]:
        raise ValueError('p_block/p_coord length must equal len(p_indices)')
    blocks=sorted(set(map(int,p_block)))
    if central_block not in blocks:
        raise ValueError('central_block absent from p_block')
    if len(blocks) != 5:
        raise RuntimeError(f'nearest-neighbour production requires exactly 5 P blocks (center+4), got {len(blocks)}')
    if positions.shape != (len(blocks),3):
        raise ValueError('block_positions must have shape (number_of_P_blocks,3) ordered by sorted block id')
    order_blocks=[central_block]+[b for b in blocks if b!=central_block]
    order=[]
    for b in order_blocks:
        for c in range(6):
            hit=np.flatnonzero((p_block==b)&(p_coord==c))
            if hit.size != 1:
                raise RuntimeError(f'block {b} coordinate {c}: expected exactly one P basis vector, got {hit.size}')
            order.append(int(hit[0]))
    return Ceff[np.ix_(order,order)], order_blocks


def geometry(order_blocks: list[int], all_blocks_sorted: list[int], positions: np.ndarray) -> dict:
    pos_by_block={b:np.asarray(positions[i],float) for i,b in enumerate(all_blocks_sorted)}
    c=order_blocks[0]; rc=pos_by_block[c]
    offs=np.asarray([pos_by_block[b]-rc for b in order_blocks[1:]],float)
    lens=np.linalg.norm(offs,axis=1)
    if np.min(lens)<=0: raise RuntimeError('zero neighbour displacement')
    a=float(np.mean(lens)); unit=offs/lens[:,None]
    sum_def=float(np.linalg.norm(np.sum(unit,axis=0)))
    second=unit.T@unit
    second_def=float(np.linalg.norm(second-(4/3)*np.eye(3)))
    length_def=float(np.max(np.abs(lens/a-1)))
    passed=max(sum_def,second_def,length_def)<GEOM_TOL
    return {'offsets':offs,'a_star':a,'unit_normals':unit,'sum_defect':sum_def,
            'second_moment_defect':second_def,'equal_length_defect':length_def,'passed':passed}


def hvec(H: np.ndarray) -> np.ndarray:
    s2=math.sqrt(2.0)
    return np.asarray([H[0,0],H[1,1],H[2,2],s2*H[0,1],s2*H[0,2],s2*H[1,2]],float)


def tt_frame(n) -> np.ndarray:
    if WILSON is None:
        raise RuntimeError('s4_tt_six_wilson_predictor.py is required')
    hp,hx=WILSON.tt_basis(n)
    return np.column_stack((hvec(hp),hvec(hx)))


def central_offsets(Kh: np.ndarray, offs: np.ndarray) -> tuple[np.ndarray,list[np.ndarray]]:
    if Kh.shape != (30,30): raise ValueError('Kh must be 30x30 for center+4 six-coordinate blocks')
    K0=Kh[:6,:6]
    Knb=[Kh[:6,6+6*i:12+6*i] for i in range(4)]
    return K0,Knb


def taylor_matrices(K0: np.ndarray, Knb: list[np.ndarray], offs: np.ndarray, n) -> tuple[np.ndarray,np.ndarray,np.ndarray,float]:
    n=np.asarray(n,float);n=n/np.linalg.norm(n)
    mass=K0.copy()
    K2=np.zeros((6,6),float);K4=np.zeros((6,6),float)
    odd=0.0
    for A,r in zip(Knb,offs):
        Ar=np.asarray(A,float)
        S=Ar+Ar.T; D=Ar-Ar.T
        x=float(n@r)
        mass+=S
        K2+=-0.5*S*x*x
        K4+=(1/24)*S*x**4
        odd=max(odd,float(np.linalg.norm(D)/max(np.linalg.norm(S),1e-300)))
    return mass,K2,K4,odd


DIRS={
    '100':np.asarray([1,0,0],float),
    '110':np.asarray([1,1,0],float),
    '111':np.asarray([1,1,1],float),
    '120':np.asarray([1,2,0],float),
    'generic':np.asarray([2,3,5],float),
}

# Exact six-observable extraction matrix certified by s4_tt_quartic_complete_basis_gate.py.
EXTRACT_A=np.asarray([
    [1/6,0,0,0,0,0],
    [0,0,1/6,0,0,0],
    [5/96,1/48,0,1/96,1/24,1/96],
    [0,0,1/24,1/48,0,0],
    [1/81,1/81,1/81,1/81,1/81,1/81],
    [341/3750,16/1875,0,17/1875,2/75,17/1875],
],float)


def extract_six(rows: dict[str,np.ndarray]) -> np.ndarray:
    obs=np.asarray([
        rows['100'][0,0], rows['100'][1,1],
        rows['110'][0,0], rows['110'][1,1],
        rows['111'][0,0], rows['120'][0,0],
    ],float)
    return np.linalg.solve(EXTRACT_A,obs)


def analyze_spatial_kernel(Kh: np.ndarray, offs: np.ndarray, a_star: float) -> dict:
    K0,Knb=central_offsets(Kh,offs)
    k2tt={};k4tt={};masstt={};odd=0.0
    for name,n in DIRS.items():
        mass,K2,K4,o=taylor_matrices(K0,Knb,offs,n)
        E=tt_frame(n)
        masstt[name]=E.T@mass@E
        k2tt[name]=E.T@K2@E
        k4tt[name]=E.T@K4@E
        odd=max(odd,o)
    residues=np.asarray([np.trace(k2tt[k])/2 for k in DIRS],float)
    Z2=float(np.mean(residues))
    if abs(Z2)<1e-14: raise RuntimeError('leading TT k^2 residue is zero')
    leading_def=max(float(np.linalg.norm(k2tt[k]/Z2-np.eye(2))) for k in DIRS)
    mass_scale=abs(Z2)/max(a_star*a_star,1e-300)
    mass_def=max(float(np.linalg.norm(masstt[k])/max(mass_scale,1e-300)) for k in DIRS)
    dimless={k:k4tt[k]/(Z2*a_star*a_star) for k in DIRS}
    c=extract_six(dimless)
    fit_def=0.0;pred={}
    for k,n in DIRS.items():
        p=np.asarray(WILSON.evaluate(c,n)['quartic_TT_matrix'],float)
        pred[k]=p
        fit_def=max(fit_def,float(np.linalg.norm(dimless[k]-p)/max(np.linalg.norm(dimless[k]),1.0)))
    checks={
        'leading_k2_positive':Z2>0,
        'leading_TT_isotropic':leading_def<LEADING_TOL,
        'TT_massless_at_k0':mass_def<LEADING_TOL,
        'parity_even_reciprocal_transfer':odd<LEADING_TOL,
        'six_Wilson_fit_closes':fit_def<FIT_TOL,
    }
    return {
        'Z2_spatial':Z2,'leading_isotropy_defect':leading_def,'mass_defect':mass_def,
        'reciprocity_odd_defect':odd,'wilson_fit_relative_defect':fit_def,
        'coefficients':c,'checks':checks,'passed':bool(all(checks.values())),
        'k2_TT':k2tt,'k4_TT_dimensionless':dimless,'wilson_reconstruction':pred,
    }


def science_run(path: Path, output: Path|None=None) -> dict:
    with np.load(path,allow_pickle=False) as z:
        required={'C_full','p_indices','p_block','p_coord','block_positions','central_block','C00','metadata_json'}
        missing=sorted(required-set(z.files))
        if missing: raise RuntimeError(f'missing production arrays: {missing}')
        meta=load_metadata(z);okprov,perr=validate_provenance(meta)
        if not okprov:
            raise RuntimeError('PRODUCTION_PROVENANCE_REJECTED: '+'; '.join(perr))
        C=np.asarray(z['C_full'],complex);pidx=np.asarray(z['p_indices'],int)
        pb=np.asarray(z['p_block'],int);pc=np.asarray(z['p_coord'],int)
        positions=np.asarray(z['block_positions'],float);central=int(np.asarray(z['central_block']).item())
        C00=complex(np.asarray(z['C00']).item())
        M=np.asarray(z['metric_map'],float) if 'metric_map' in z.files else frozen_metric_map()
    if M.shape!=(6,6) or np.linalg.matrix_rank(M,RTOL)!=6:
        raise RuntimeError('metric_map must be invertible 6x6')
    sch=schur_zero_energy(C,pidx)
    all_blocks=sorted(set(map(int,pb)))
    Ce,order_blocks=canonicalize_p(sch['Ceff'],pb,pc,positions,central)
    # Exact normalized-state Hessian from the frozen protocol.
    if abs(C00.imag)>1e-9: raise RuntimeError('C00 must be real for Hermitian physical scalar')
    Kq=2*Ce.real-2*C00.real*np.eye(Ce.shape[0])
    T=blockdiag(np.linalg.inv(M),5)
    Kh=T.T@Kq@T
    geo=geometry(order_blocks,all_blocks,positions)
    if not geo['passed']:
        raise RuntimeError('NEIGHBOUR_GEOMETRY_NOT_FROZEN_TETRAHEDRAL: '+json.dumps({k:v for k,v in geo.items() if k not in ('offsets','unit_normals')}))
    spatial=analyze_spatial_kernel(Kh,geo['offsets'],geo['a_star'])
    out={
        'status':'BQG actual multi-block Schur-to-TT six-Wilson extraction',
        'science_status':'PHYSICAL_TT_SIX_WILSON_EXTRACTED' if spatial['passed'] else 'MULTIBLOCK_KERNEL_FAILS_PHYSICAL_IR_GUARDS',
        'passed':bool(spatial['passed']),
        'source_metadata':meta,
        'metric_map':M.tolist(),'metric_map_condition_number':float(np.linalg.cond(M)),
        'schur':{
            'q_dimension':int(len(sch['q_indices'])),'q_gap':sch['q_gap'],
            'q_spectral_radius':sch['q_spectral_radius'],'q_condition':sch['q_condition'],
            'zero_mode_count':sch['zero_mode_count'],'coupled_zero_mode_norm':sch['coupled_zero_mode_norm'],
        },
        'geometry':{k:(v.tolist() if isinstance(v,np.ndarray) else v) for k,v in geo.items()},
        'spatial':{
            'Z2_spatial':spatial['Z2_spatial'],
            'leading_isotropy_defect':spatial['leading_isotropy_defect'],
            'mass_defect':spatial['mass_defect'],
            'reciprocity_odd_defect':spatial['reciprocity_odd_defect'],
            'wilson_fit_relative_defect':spatial['wilson_fit_relative_defect'],
            'checks':spatial['checks'],
        },
        'c_BQG_IR':spatial['coefficients'].tolist() if spatial['passed'] else None,
        'hard_scope_guard':'c_BQG_IR is emitted only for an actual frozen E+S+R_op multi-block BQG operator passing Q-gap, tetrahedral-geometry, massless/isotropic k2, reciprocity and six-basis closure guards.',
    }
    if output is not None:
        output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    return out


def selftest() -> dict:
    if WILSON is None: raise RuntimeError('missing six-Wilson predictor')
    M=frozen_metric_map(); metric_ok=bool(abs(float(np.linalg.cond(M))-math.sqrt(2))<2e-12)
    normals=np.asarray([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)],float)/math.sqrt(3)
    # Target h-coordinate 5-block nearest-neighbour kernel: K_a=-I, K_0=8I.
    Kh=np.zeros((30,30),float)
    for b in range(5): Kh[6*b:6*b+6,6*b:6*b+6]=8*np.eye(6)
    for i in range(4):
        sl=slice(6+6*i,12+6*i)
        Kh[:6,sl]=-np.eye(6);Kh[sl,:6]=-np.eye(6)
    Bm=blockdiag(M,5)
    Kq=Bm.T@Kh@Bm
    Ceff=0.5*Kq
    rng=np.random.default_rng(20260906)
    qdim=4;D=np.diag([2.0,-3.0,4.0,5.0]);X=rng.normal(size=(30,qdim))*0.02
    CPP=Ceff+X@np.linalg.inv(D)@X.T
    C=np.block([[CPP,X],[X.T,D]])
    sch=schur_zero_energy(C,np.arange(30))
    schur_err=float(np.linalg.norm(sch['Ceff']-Ceff)/np.linalg.norm(Ceff))
    Kq2=2*sch['Ceff'].real
    T=blockdiag(np.linalg.inv(M),5);Kh2=T.T@Kq2@T
    spatial=analyze_spatial_kernel(Kh2,normals,1.0)
    expected=(-1/20)*WILSON.ISO+(1/18)*WILSON.Q4V
    c_err=float(np.linalg.norm(spatial['coefficients']-expected)/np.linalg.norm(expected))
    gapless_rejected=False
    try:
        schur_zero_energy(np.asarray([[0.0,0.01],[0.01,0.0]]),np.asarray([0]))
    except RuntimeError as e:
        gapless_rejected='GAPLESS_COUPLED_Q_MODE_REQUIRES_PROMOTION' in str(e)
    checks={
        'frozen_metric_map_cond_sqrt2':metric_ok,
        'gapless_coupled_Q_mode_rejected':gapless_rejected,
        'synthetic_Schur_recovers_target':schur_err<2e-12,
        'tetra_scalar_kernel_passes_IR_guards':spatial['passed'],
        'known_analytic_Wilson_vector_recovered':c_err<2e-10,
    }
    return {
        'status':'synthetic known-answer test only','science_status':'INFRASTRUCTURE_SELFTEST_NOT_BQG_EVIDENCE',
        'passed':bool(all(checks.values())),'checks':checks,'schur_relative_error':schur_err,
        'expected_c':expected.tolist(),'recovered_c':spatial['coefficients'].tolist(),
        'c_relative_error':c_err,'spatial_diagnostics':{
            'Z2_spatial':spatial['Z2_spatial'],'leading_isotropy_defect':spatial['leading_isotropy_defect'],
            'mass_defect':spatial['mass_defect'],'wilson_fit_relative_defect':spatial['wilson_fit_relative_defect'],
        }
    }


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,help='production NPZ containing actual multi-block BQG operator')
    p.add_argument('--output',type=Path)
    p.add_argument('--selftest',action='store_true')
    a=p.parse_args()
    if a.selftest or a.input is None:
        out=selftest()
    else:
        try:
            out=science_run(a.input,a.output)
        except Exception as e:
            out={'status':'STOP','science_status':'MISSING_OR_INVALID_ACTUAL_MULTIBLOCK_INPUT','passed':False,
                 'c_BQG_IR':None,'error':str(e),
                 'hard_scope_guard':'No Wilson coefficients are emitted when the frozen physical input chain is incomplete.'}
            if a.output is not None:
                a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,default=lambda x:x.tolist() if isinstance(x,np.ndarray) else x))
    return 0 if out.get('passed') else 2

if __name__=='__main__':
    raise SystemExit(main())
