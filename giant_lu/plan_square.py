#!/usr/bin/env python3
import argparse,json,pickle
from collections import deque
from pathlib import Path
import numpy as np

ap=argparse.ArgumentParser();ap.add_argument("--meta",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);a=ap.parse_args()
m=json.load(open(a.meta));ins=m["inputs"];dims=m["dims"];paths=m["paths"];qtu=[tuple(q) for q in m["q_tuples"]];qrows=m["q_rows"]
Q={q:i for i,q in enumerate(qtu)};nq=len(qtu);ni=len(ins)
sup=[];ener=[np.zeros(r,float) for r in qrows]
for n,i in enumerate(ins,1):
 d=pickle.load(open(paths[i],"rb"));ls=[]
 for q,M in d.items():
  k=Q.get(tuple(q))
  if k is None:continue
  ls.append(k);x=np.asarray(M).real;ener[k]+=np.einsum("ij,ij->i",x,x)
 sup.append(ls)
 if n%2000==0:print("SCAN",n,flush=True)
S=0;I0=1;Q0=I0+ni;T=Q0+nq;N=T+1
adj=[[] for _ in range(N)]
def add(u,v,c):
 x=[v,len(adj[v]),c,c];y=[u,len(adj[u]),0,0];adj[u].append(x);adj[v].append(y)
for ii,i in enumerate(ins):add(S,I0+ii,dims[i])
for ii,i in enumerate(ins):
 for q in sup[ii]:add(I0+ii,Q0+q,dims[i])
for q,r in enumerate(qrows):add(Q0+q,T,r)
flow=0
while 1:
 lev=[-1]*N;lev[S]=0;dq=deque([S])
 while dq:
  u=dq.popleft()
  for e in adj[u]:
   if e[2]>0 and lev[e[0]]<0:lev[e[0]]=lev[u]+1;dq.append(e[0])
 if lev[T]<0:break
 ptr=[0]*N
 def dfs(u,f):
  if u==T:return f
  while ptr[u]<len(adj[u]):
   e=adj[u][ptr[u]]
   if e[2]>0 and lev[e[0]]==lev[u]+1:
    z=dfs(e[0],min(f,e[2]))
    if z:e[2]-=z;adj[e[0]][e[1]][2]+=z;return z
   ptr[u]+=1
  return 0
 while 1:
  z=dfs(S,10**18)
  if not z:break
  flow+=z
 print("FLOW",flow,flush=True)
assert flow==130007
used=[]
for q in range(nq):
 e=next(e for e in adj[Q0+q] if e[0]==T)
 used.append(e[3]-e[2])
assert sum(used)==130007
sel=[]
for e,u in zip(ener,used):
 if u==len(e):ids=list(range(len(e)))
 elif u:
  ids=np.argpartition(-e,u-1)[:u];ids=ids[np.argsort(-e[ids])].tolist()
 else:ids=[]
 sel.append(ids)
out={"input_ids":ins,"dims":dims,"paths":paths,"q_tuples":[list(q) for q in qtu],"q_rows":qrows,"q_used":used,"row_select":sel,"flow":flow,"selection":"top row energy within each q"}
a.out.write_text(json.dumps(out))
print("PLAN",len(ins),len(qtu),sum(map(len,sel)),min(float(ener[k][ids].min()) for k,ids in enumerate(sel) if ids),flush=True)
