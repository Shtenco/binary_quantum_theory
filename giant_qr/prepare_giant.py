#!/usr/bin/env python3
import argparse,glob,json,os,pickle,tarfile
from collections import deque
from pathlib import Path
NIN=11956
ap=argparse.ArgumentParser();ap.add_argument("--artifacts",type=Path,required=True);ap.add_argument("--work",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);a=ap.parse_args()
a.work.mkdir(parents=True,exist_ok=True)
tars=sorted(a.artifacts.rglob("bqg-s4sign-v2-shard-*.tar.gz"))
assert len(tars)==128,len(tars)
dirs=[]
for n,t in enumerate(tars):
 d=a.work/f"s{n:03d}";d.mkdir(exist_ok=True)
 with tarfile.open(t,"r:gz") as tf:tf.extractall(d)
 dirs.append(d)
dims=[0]*NIN;paths=[None]*NIN
for d in dirs:
 ss=list(d.rglob("summary.json"));assert len(ss)==1
 j=json.load(open(ss[0]));assert (j["shell_states"],j["s4sign_blocks"],j["s4sign_dim"])==(264962,11956,130112)
 assert j["failed_blocks"]==0 and j["ok_blocks"]==j["assigned_blocks"]
 for r in j["records"]:dims[int(r["i"])]=int(r["d"])
 for p in d.rglob("b*.pkl"):paths[int(p.stem[1:])]=str(p)
assert all(paths) and sum(dims)==130112
qidx={};qlist=[];qrows=[];sup=[None]*NIN
for i,p in enumerate(paths):
 x=pickle.load(open(p,"rb"));ls=[]
 for q,M in x.items():
  q=tuple(q);k=qidx.get(q)
  if k is None:k=len(qlist);qidx[q]=k;qlist.append(q);qrows.append(int(M.shape[0]))
  else:assert qrows[k]==int(M.shape[0])
  ls.append(k)
 sup[i]=ls
 if (i+1)%2000==0:print("INDEX",i+1,len(qlist),flush=True)
NQ=len(qlist);S=0;I0=1;Q0=I0+NIN;T=Q0+NQ;N=T+1
adj=[[] for _ in range(N)]
def add(u,v,c):
 x=[v,len(adj[v]),c];y=[u,len(adj[u]),0];adj[u].append(x);adj[v].append(y)
for i,d in enumerate(dims):add(S,I0+i,d)
for i,ls in enumerate(sup):
 for q in ls:add(I0+i,Q0+q,dims[i])
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
M=NIN+NQ;g=[[] for _ in range(M)];gr=[[] for _ in range(M)]
def loc(v):
 if I0<=v<Q0:return v-I0
 if Q0<=v<T:return NIN+v-Q0
for u in range(I0,T):
 lu=loc(u)
 for e in adj[u]:
  lv=loc(e[0])
  if lv is not None and e[2]>0:g[lu].append(lv);gr[lv].append(lu)
seen=[0]*M;order=[]
for s in range(M):
 if seen[s]:continue
 st=[(s,0)];seen[s]=1
 while st:
  u,k=st[-1]
  if k<len(g[u]):
   v=g[u][k];st[-1]=(u,k+1)
   if not seen[v]:seen[v]=1;st.append((v,0))
  else:order.append(u);st.pop()
comp=[-1]*M;cs=[]
for s in reversed(order):
 if comp[s]>=0:continue
 cid=len(cs);ns=[];st=[s];comp[s]=cid
 while st:
  u=st.pop();ns.append(u)
  for v in gr[u]:
   if comp[v]<0:comp[v]=cid;st.append(v)
 cs.append(ns)
G=max(cs,key=len);ins=sorted(u for u in G if u<NIN);qs=sorted(u-NIN for u in G if u>=NIN)
reach=[0]*N;reach[S]=1;dq=deque([S])
while dq:
 u=dq.popleft()
 for e in adj[u]:
  if e[2]>0 and not reach[e[0]]:reach[e[0]]=1;dq.append(e[0])
defic=[i for i in range(NIN) if reach[I0+i]]
out={"flow":flow,"inputs":ins,"q_tuples":[list(qlist[q]) for q in qs],"q_rows":[qrows[q] for q in qs],"dims":dims,"paths":paths,"deficient":defic}
assert (flow,len(ins),sum(dims[i] for i in ins),len(qs),sum(qrows[q] for q in qs),defic)==(130096,11923,130007,14586,153202,list(range(16)))
a.out.write_text(json.dumps(out))
print("OK",flow,len(ins),len(qs),flush=True)
