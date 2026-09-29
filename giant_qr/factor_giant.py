#!/usr/bin/env python3
import argparse,json,math,pickle,time
from pathlib import Path
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
import sparseqr

ap=argparse.ArgumentParser();ap.add_argument("--meta",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);a=ap.parse_args()
m=json.load(open(a.meta));ins=m["inputs"];dims=m["dims"];paths=m["paths"];qtu=[tuple(q) for q in m["q_tuples"]];qrows=m["q_rows"]
Q={q:i for i,q in enumerate(qtu)}
co={};c=0
for i in ins:co[i]=c;c+=dims[i]
ro={};r=0
for qi,nr in enumerate(qrows):ro[qi]=r;r+=nr
assert (r,c)==(153202,130007)
real_nnz=0;im2=re2=0.;mxre=mxim=0.
for n,i in enumerate(ins,1):
 d=pickle.load(open(paths[i],"rb"))
 for q,M in d.items():
  qi=Q.get(tuple(q))
  if qi is None:continue
  z=np.asarray(M);re=z.real;im=z.imag
  real_nnz+=int(np.count_nonzero(re));re2+=float(np.dot(re.ravel(),re.ravel()));im2+=float(np.dot(im.ravel(),im.ravel()))
  mxre=max(mxre,float(np.max(np.abs(re),initial=0)));mxim=max(mxim,float(np.max(np.abs(im),initial=0)))
 if n%2000==0:print("COUNT",n,real_nnz,flush=True)
rows=np.empty(real_nnz,np.int32);cols=np.empty(real_nnz,np.int32);data=np.empty(real_nnz,np.float64);k=0
for n,i in enumerate(ins,1):
 d=pickle.load(open(paths[i],"rb"));ci=co[i]
 for q,M in d.items():
  qi=Q.get(tuple(q))
  if qi is None:continue
  re=np.asarray(M).real;rr,cc=np.nonzero(re);z=len(rr)
  if z:rows[k:k+z]=rr+ro[qi];cols[k:k+z]=cc+ci;data[k:k+z]=re[rr,cc];k+=z
 if n%2000==0:print("FILL",n,k,flush=True)
assert k==real_nnz
A=sp.coo_matrix((data,(rows,cols)),shape=(r,c))
print("MATRIX",A.shape,A.nnz,round((A.data.nbytes+A.row.nbytes+A.col.nbytes)/2**20,1),"MB",flush=True)
b=np.zeros((r,1),float);tol=1e-10;t=time.time()
Z,R,E,rank=sparseqr.rz(A,b,tolerance=tol);qrsec=time.time()-t
print("RANK",rank,"R",R.shape,R.nnz,"sec",qrsec,flush=True)
diag=np.abs(R.diagonal());dmin=float(diag.min()) if len(diag) else 0.
sigma=None;err=None;svsec=None
if rank==c:
 try:
  t=time.time();sv=sla.svds(R.tocsc(),k=1,which="SM",solver="propack",tol=1e-8,maxiter=500,return_singular_vectors=False)
  svsec=time.time()-t;sigma=float(np.min(sv));print("SIGMA",sigma,"sec",svsec,flush=True)
 except Exception as e:err=repr(e);print("SVDSERR",err,flush=True)
imfro=math.sqrt(im2);omit=1e-11*math.sqrt(25068);budget=imfro+omit
res={"rank":int(rank),"target_rank":c,"shape":[r,c],"nnz":int(A.nnz),"R_nnz":int(R.nnz),"tol":tol,"diag_min_abs":dmin,"sigma_min_estimate":sigma,"svds_error":err,"imag_fro":imfro,"real_fro":math.sqrt(re2),"max_imag":mxim,"max_real":mxre,"omitted_fro_bound":omit,"total_perturbation_bound":budget,"robust_if_sigma_gt_budget":bool(sigma is not None and sigma>budget),"qr_sec":qrsec,"svds_sec":svsec}
a.out.write_text(json.dumps(res,indent=2)+"\n");print("FINAL",json.dumps(res),flush=True)
