#!/usr/bin/env python3
import argparse,gc,json,math,pickle,time
from pathlib import Path
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

ap=argparse.ArgumentParser();ap.add_argument("--plan",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);a=ap.parse_args()
p=json.load(open(a.plan));ins=p["input_ids"];dims=p["dims"];paths=p["paths"];qtu=[tuple(q) for q in p["q_tuples"]];sel=p["row_select"];Q={q:i for i,q in enumerate(qtu)}
co={};c=0
for i in ins:co[i]=c;c+=dims[i]
ro={};r=0
for q,ids in enumerate(sel):
 if ids:ro[q]=r;r+=len(ids)
assert r==c==130007
nnz=0
for n,i in enumerate(ins,1):
 d=pickle.load(open(paths[i],"rb"))
 for qt,M in d.items():
  q=Q.get(tuple(qt))
  if q is not None and sel[q]:nnz+=int(np.count_nonzero(np.asarray(M).real[sel[q],:]))
 if n%2500==0:print("COUNT",n,nnz,flush=True)
rows=np.empty(nnz,np.int32);cols=np.empty(nnz,np.int32);data=np.empty(nnz,np.float64);k=0
for n,i in enumerate(ins,1):
 d=pickle.load(open(paths[i],"rb"));ci=co[i]
 for qt,M in d.items():
  q=Q.get(tuple(qt))
  if q is None or not sel[q]:continue
  x=np.asarray(M).real[sel[q],:];rr,cc=np.nonzero(x);z=len(rr)
  if z:rows[k:k+z]=rr+ro[q];cols[k:k+z]=cc+ci;data[k:k+z]=x[rr,cc];k+=z
 if n%2500==0:print("FILL",n,k,flush=True)
A=sp.coo_matrix((data,(rows,cols)),shape=(r,c)).tocsr();del rows,cols,data;gc.collect()
print("CSR",A.shape,A.nnz,round((A.data.nbytes+A.indices.nbytes+A.indptr.nbytes)/2**20,1),"MB",flush=True)
# deterministic start
v0=np.sin(np.arange(c,dtype=float)*0.6180339887498949+0.123);v0/=np.linalg.norm(v0)
runs=[]
for idx,tol in enumerate([1e-6,1e-8]):
 try:
  t=time.time();u,s,vt=sla.svds(A,k=6,which="SM",solver="propack",tol=tol,maxiter=3000,v0=v0,return_singular_vectors=True)
  sec=time.time()-t;o=np.argsort(s);s=s[o];u=u[:,o];vt=vt[o,:]
  residuals=[]
  for j,sv in enumerate(s):
   v=vt[j];uu=u[:,j]
   r1=np.linalg.norm(A@v-sv*uu);r2=np.linalg.norm(A.T@uu-sv*v)
   residuals.append(float(max(r1,r2)))
  rec={"tol":tol,"sec":sec,"s":[float(x) for x in s],"residuals":residuals}
  runs.append(rec);print("RUN",idx,json.dumps(rec),flush=True)
 except Exception as e:
  rec={"tol":tol,"error":repr(e)};runs.append(rec);print("ERR",idx,repr(e),flush=True)
omit=1e-11*math.sqrt(25068);imag=7.362472426071804e-13;budget=omit+imag
best=None
for x in runs:
 if "s" in x:
  z=x["s"][0]
  if best is None or x["tol"]<best["tol"]:best=x
res={"shape":[r,c],"nnz":int(A.nnz),"runs":runs,"perturbation_budget":budget,"best_sigma_min_estimate":None if best is None else best["s"][0],"best_residual":None if best is None else best["residuals"][0],"robust_margin_estimate":None if best is None else best["s"][0]-budget}
a.out.write_text(json.dumps(res,indent=2)+"\n");print("FINAL",json.dumps(res),flush=True)
