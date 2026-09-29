#!/usr/bin/env python3
import argparse,json,math,pickle,time
from pathlib import Path
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
from scikits.umfpack import UmfpackContext,UMFPACK_A,UMFPACK_At,UMFPACK_RCOND,UMFPACK_UDIAG_NZ,UMFPACK_UMIN,UMFPACK_UMAX,UMFPACK_LU_ENTRIES,UMFPACK_NUMERIC_WALLTIME

ap=argparse.ArgumentParser();ap.add_argument("--plan",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);a=ap.parse_args()
p=json.load(open(a.plan));ins=p["input_ids"];dims=p["dims"];paths=p["paths"];qtu=[tuple(q) for q in p["q_tuples"]];sel=p["row_select"]
Q={q:i for i,q in enumerate(qtu)}
co={};c=0
for i in ins:co[i]=c;c+=dims[i]
ro={};r=0
for q,ids in enumerate(sel):
 if ids:ro[q]=r;r+=len(ids)
assert r==c==130007
nnz=0;im2=0.;re2=0.
for n,i in enumerate(ins,1):
 d=pickle.load(open(paths[i],"rb"))
 for qt,M in d.items():
  q=Q.get(tuple(qt))
  if q is None or not sel[q]:continue
  z=np.asarray(M)[sel[q],:];re=z.real;im=z.imag
  nnz+=int(np.count_nonzero(re));re2+=float(np.dot(re.ravel(),re.ravel()));im2+=float(np.dot(im.ravel(),im.ravel()))
 if n%2000==0:print("COUNT",n,nnz,flush=True)
print("NNZ",nnz,"re_fro",math.sqrt(re2),"im_fro",math.sqrt(im2),flush=True)
rows=np.empty(nnz,np.int32);cols=np.empty(nnz,np.int32);data=np.empty(nnz,np.float64);k=0
for n,i in enumerate(ins,1):
 d=pickle.load(open(paths[i],"rb"));ci=co[i]
 for qt,M in d.items():
  q=Q.get(tuple(qt))
  if q is None or not sel[q]:continue
  re=np.asarray(M).real[sel[q],:];rr,cc=np.nonzero(re);z=len(rr)
  if z:
   rows[k:k+z]=rr+ro[q];cols[k:k+z]=cc+ci;data[k:k+z]=re[rr,cc];k+=z
 if n%2000==0:print("FILL",n,k,flush=True)
assert k==nnz
A=sp.coo_matrix((data,(rows,cols)),shape=(r,c)).tocsc();A.sort_indices()
print("CSC",A.shape,A.nnz,round((A.data.nbytes+A.indices.nbytes+A.indptr.nbytes)/2**20,1),"MB",flush=True)
ctx=UmfpackContext("di");t=time.time();ctx.numeric(A);lusec=time.time()-t
info=ctx.info
udiag=int(info[UMFPACK_UDIAG_NZ]);rcond=float(info[UMFPACK_RCOND]);umin=float(info[UMFPACK_UMIN]);umax=float(info[UMFPACK_UMAX]);luent=float(info[UMFPACK_LU_ENTRIES]);uwall=float(info[UMFPACK_NUMERIC_WALLTIME])
print("UMF",udiag,rcond,umin,umax,luent,lusec,flush=True)
# deterministic solve residual checks
checks=[]
for seed in [0,1,2]:
 rng=np.random.default_rng(seed);x0=rng.standard_normal(c);b=A@x0
 x=ctx.solve(UMFPACK_A,A,b,autoTranspose=True)
 rel=float(np.linalg.norm(x-x0)/np.linalg.norm(x0));res=float(np.linalg.norm(A@x-b)/np.linalg.norm(b))
 checks.append({"seed":seed,"rel_x":rel,"rel_res":res});print("SOLVE",checks[-1],flush=True)
sigma=None;inv_smax=None;sv_err=None;sv_sec=None
if udiag==c:
 try:
  def mv(x):return ctx.solve(UMFPACK_A,A,np.asarray(x),autoTranspose=True)
  def rmv(x):return ctx.solve(UMFPACK_At,A,np.asarray(x),autoTranspose=True)
  Linv=sla.LinearOperator((c,c),matvec=mv,rmatvec=rmv,dtype=np.float64)
  t=time.time();sv=sla.svds(Linv,k=1,which="LM",solver="propack",tol=1e-5,maxiter=100,return_singular_vectors=False)
  sv_sec=time.time()-t;inv_smax=float(np.max(sv));sigma=1.0/inv_smax
  print("INV_SMAX",inv_smax,"SIGMA",sigma,"sec",sv_sec,flush=True)
 except Exception as e:
  sv_err=repr(e);print("SVERR",sv_err,flush=True)
omit=1e-11*math.sqrt(25068);imag=7.362472426071804e-13;budget=omit+imag
res={"shape":[r,c],"nnz":int(A.nnz),"udiag_nz":udiag,"umf_rcond":rcond,"umin":umin,"umax":umax,"lu_entries":luent,"lu_sec":lusec,"umf_numeric_walltime":uwall,"solve_checks":checks,"inverse_smax_estimate":inv_smax,"sigma_min_estimate":sigma,"sv_error":sv_err,"sv_sec":sv_sec,"omitted_fro_bound":omit,"imag_fro_bound_full_giant":imag,"total_perturbation_bound":budget,"robust_if_sigma_gt_budget":bool(sigma is not None and sigma>budget),"selected_imag_fro":math.sqrt(im2),"selected_real_fro":math.sqrt(re2)}
a.out.write_text(json.dumps(res,indent=2)+"\n");print("FINAL",json.dumps(res),flush=True)
