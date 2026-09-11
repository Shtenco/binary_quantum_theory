#!/usr/bin/env python3
from __future__ import annotations
import argparse, heapq, json, math, struct, time, urllib.request, zlib, lzma
from collections import Counter
from pathlib import Path
import numpy as np
from sklearn.cluster import MiniBatchKMeans

MODEL='mistralai/Mistral-Nemo-Base-2407'
REV='2045759120154383da48ee84ce4bf2f90cc6ec1f'
BASE=f'https://huggingface.co/{MODEL}/resolve/{REV}'
SHARDS=[f'model-{i:05d}-of-00005.safetensors' for i in range(1,6)]
BPE={'BF16':2,'F16':2,'F32':4}

def url(shard): return f'{BASE}/{shard}?download=true'

def prefix(u,n):
    req=urllib.request.Request(u,headers={'User-Agent':'nexus-real-weight-probe/1.0'})
    with urllib.request.urlopen(req,timeout=120) as r:
        out=bytearray()
        while len(out)<n:
            b=r.read(min(1<<20,n-len(out)))
            if not b: break
            out+=b
        return bytes(out)

def read_range(u,start,n):
    end=start+n-1
    req=urllib.request.Request(u,headers={'Range':f'bytes={start}-{end}','User-Agent':'nexus-real-weight-probe/1.0'})
    with urllib.request.urlopen(req,timeout=180) as r:
        status=getattr(r,'status',200); cr=r.headers.get('Content-Range','')
        if start>0 and status!=206 and not cr.startswith(f'bytes {start}-'):
            raise RuntimeError(f'range not honored status={status} cr={cr!r}')
        data=r.read(n+1)
    if len(data)!=n: raise RuntimeError(f'short range {len(data)} != {n}')
    return data

def header(shard):
    first=prefix(url(shard),8)
    hlen=struct.unpack('<Q',first)[0]
    blob=prefix(url(shard),8+hlen)
    return json.loads(blob[8:8+hlen]),8+hlen

def decode(raw,dtype):
    if dtype=='BF16':
        u=np.frombuffer(raw,dtype='<u2').astype(np.uint32)<<16
        return u.view(np.float32)
    if dtype=='F16': return np.frombuffer(raw,dtype='<f2').astype(np.float32)
    if dtype=='F32': return np.frombuffer(raw,dtype='<f4').astype(np.float32)
    raise ValueError(dtype)

def get_rows(shard,e,data_start,rows):
    out_dim,in_dim=map(int,e['shape']); rows=min(rows,out_dim); bpe=BPE[e['dtype']]
    row0=max(0,(out_dim-rows)//2); rel0=int(e['data_offsets'][0]); rb=in_dim*bpe
    raw=read_range(url(shard),data_start+rel0+row0*rb,rows*rb)
    return decode(raw,e['dtype']).reshape(rows,in_dim),row0

def qnorm(norms,bits):
    lo=float(norms.min()); hi=float(norms.max()); m=(1<<bits)-1
    if hi<=lo: return np.zeros(len(norms),np.uint8),np.full_like(norms,lo),lo,0.0
    s=(hi-lo)/m; q=np.rint((norms-lo)/s).clip(0,m).astype(np.uint8)
    return q,(lo+q.astype(np.float32)*s).astype(np.float32),lo,float(s)

def q2_literal(c):
    s=float(np.max(np.abs(c))) or 1.0
    q=np.rint(c/s*3.0).clip(0,3).astype(np.uint8)
    return q,q.astype(np.float32)/3.0*s,s

def q2_sym(c):
    s=float(np.max(np.abs(c))) or 1.0; lv=np.array([-1.,-1/3,1/3,1.],np.float32)
    f=(c/s).ravel(); q=np.empty(f.size,np.uint8)
    for i in range(0,f.size,500000):
        x=f[i:i+500000]; q[i:i+len(x)]=np.argmin(np.abs(x[:,None]-lv[None,:]),axis=1).astype(np.uint8)
    q=q.reshape(c.shape); return q,lv[q]*s,s

def entropy(labels):
    c=np.bincount(labels); c=c[c>0].astype(float); p=c/c.sum(); return float(-(p*np.log2(p)).sum())

def huff_lengths(labels,k):
    freq=Counter(map(int,labels)); heap=[]
    for s in range(k):
        if freq.get(s,0): heap.append((freq[s],[s]))
    if len(heap)==1:
        out=[0]*k; out[heap[0][1][0]]=1; return out
    heapq.heapify(heap); out=[0]*k
    while len(heap)>1:
        w1,a=heapq.heappop(heap); w2,b=heapq.heappop(heap)
        for x in a: out[x]+=1
        for x in b: out[x]+=1
        heapq.heappush(heap,(w1+w2,a+b))
    return out

def pack_bits(vals,bits):
    vals=np.asarray(vals,dtype=np.uint8).ravel(); out=bytearray((len(vals)*bits+7)//8); pos=0; mask=(1<<bits)-1
    for vv in vals:
        v=int(vv)&mask; bi=pos>>3; sh=pos&7; out[bi]|=(v<<sh)&255
        if sh+bits>8: out[bi+1]|=v>>(8-sh)
        pos+=bits
    return bytes(out)

def cluster(v,k,seed):
    rng=np.random.default_rng(seed); d=v.shape[1]; cols=np.sort(rng.choice(d,size=min(512,d),replace=False))
    km=MiniBatchKMeans(n_clusters=k,random_state=seed,batch_size=min(256,len(v)),n_init=2,max_iter=40,reassignment_ratio=0.0)
    lab=km.fit_predict(v[:,cols]).astype(np.int32); cen=np.zeros((k,d),np.float32); cnt=np.bincount(lab,minlength=k)
    for i in range(k): cen[i]=v[lab==i].mean(0) if cnt[i] else v[rng.integers(0,len(v))]
    return lab,cen

def quality(w,r,seed):
    eps=1e-12; wn=np.linalg.norm(w,axis=1); rn=np.linalg.norm(r,axis=1)
    cos=np.sum(w*r,axis=1)/np.maximum(wn*rn,eps)
    nmse=float(np.sum((w-r)**2)/max(float(np.sum(w*w)),eps)); rng=np.random.default_rng(seed); errs=[]
    for _ in range(6):
        x=rng.standard_normal(w.shape[1],dtype=np.float32); y=w@x; yr=r@x
        errs.append(float(np.linalg.norm(y-yr)/max(float(np.linalg.norm(y)),eps)))
    return float(cos.mean()),float(np.quantile(cos,.05)),nmse,float(np.mean(errs))

def packed_sample(qc,labels,lens,qn,norm_bits,scale,lo,ns):
    # storage proxy; code lengths retained as one byte per symbol + fixed-width labels proxy
    return struct.pack('<fff',scale,lo,ns)+pack_bits(qc,2)+bytes(lens)+pack_bits(labels,max(1,math.ceil(math.log2(max(2,len(lens))))))+pack_bits(qn,norm_bits)

def structural(all_headers,k,cbits,nbits):
    total_raw=total=0; mats=0
    for h,_ in all_headers.values():
        for n,e in h.items():
            if n=='__metadata__' or not isinstance(e,dict) or e.get('dtype') not in BPE: continue
            shape=e.get('shape',[]); raw=int(np.prod(shape))*BPE[e['dtype']]; total_raw+=raw
            if len(shape)==2:
                o,i=map(int,shape); total+=math.ceil(k*i*cbits/8)+math.ceil(o*math.ceil(math.log2(k))/8)+math.ceil(o*nbits/8)+128; mats+=1
            else: total+=raw
    return {'k':k,'centroid_bits':cbits,'norm_bits':nbits,'bytes':total,'mib':total/2**20,'ratio_vs_bf16':total_raw/total,'effective_bpw':total*8/(total_raw/2),'matrices':mats,'raw_bytes':total_raw}

def pick(all_headers):
    all_e={}
    for s,(h,ds) in all_headers.items():
        for n,e in h.items():
            if n!='__metadata__' and isinstance(e,dict): all_e[n]=(s,e,ds)
    wanted=['model.embed_tokens.weight','model.layers.0.self_attn.q_proj.weight','model.layers.0.mlp.gate_proj.weight','model.layers.10.mlp.down_proj.weight','model.layers.20.self_attn.o_proj.weight','model.layers.20.mlp.up_proj.weight','model.layers.39.self_attn.q_proj.weight','model.layers.39.mlp.down_proj.weight','lm_head.weight']
    return [(n,*all_e[n]) for n in wanted if n in all_e]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rows',type=int,default=256); ap.add_argument('--out',default='experiments/results/NEXUS_DWE_REAL_12B.json'); args=ap.parse_args(); t0=time.time()
    hs={}
    for s in SHARDS:
        print('HEADER',s,flush=True); hs[s]=header(s)
    structs=[structural(hs,k,cb,nb) for k in [16,32,64,128] for cb,nb in [(2,4),(2,8),(16,4)]]
    results=[]; sampled=[]
    for ti,(name,sh,e,ds) in enumerate(pick(hs)):
        rows=min(args.rows,int(e['shape'][0])); print('TENSOR',name,e['shape'],'rows',rows,flush=True); w,row0=get_rows(sh,e,ds,rows); sampled.append({'name':name,'shape':e['shape'],'dtype':e['dtype'],'shard':sh,'row0':row0,'rows':rows})
        norms=np.linalg.norm(w,axis=1).astype(np.float32); norms=np.maximum(norms,1e-12); v=(w/norms[:,None]).astype(np.float32); raw_full=int(e['shape'][0])*int(e['shape'][1])*2
        for k in [16,32,64,128]:
            if k>=rows: continue
            lab,cen=cluster(v,k,1000+ti*100+k); H=entropy(lab); lens=huff_lengths(lab,k); hb=float(np.mean([lens[int(x)] for x in lab]))
            for mode in ['fp16','literal-pasted-2bit','symmetric-2bit']:
                if mode=='fp16': cq=cen.astype(np.float16).astype(np.float32); qc=None; scale=0.; cbits=16
                elif mode=='literal-pasted-2bit': qc,cq,scale=q2_literal(cen); cbits=2
                else: qc,cq,scale=q2_sym(cen); cbits=2
                for nb in [4,8]:
                    qn,dn,lo,ns=qnorm(norms,nb); r=cq[lab]*dn[:,None]; cm,c05,nmse,oe=quality(w,r,2000+ti*100+k+nb)
                    fixed=math.ceil(k*int(e['shape'][1])*cbits/8)+math.ceil(int(e['shape'][0])*math.ceil(math.log2(k))/8)+math.ceil(int(e['shape'][0])*nb/8)+128
                    hest=math.ceil(k*int(e['shape'][1])*cbits/8)+math.ceil(int(e['shape'][0])*hb/8)+math.ceil(int(e['shape'][0])*nb/8)+k+128
                    if qc is not None:
                        blob=packed_sample(qc,lab,lens,qn,nb,scale,lo,ns); cands={'RAW':len(blob),'zlib9':len(zlib.compress(blob,9)),'lzma9':len(lzma.compress(blob,preset=9))}; br=min(cands,key=cands.get); lb=cands[br]; ps=len(blob)
                    else: br='n/a'; lb=ps=0
                    results.append({'tensor':name,'shape':e['shape'],'sample_rows':rows,'k':k,'centroid_mode':mode,'norm_bits':nb,'cosine_mean':cm,'cosine_p05':c05,'nmse':nmse,'random_activation_rel_l2':oe,'index_entropy_bits':H,'huffman_bits_per_index':hb,'structural_bytes_fixed_index':fixed,'ratio_vs_bf16':raw_full/fixed,'estimated_bytes_huffman':hest,'ratio_huffman_vs_bf16':raw_full/hest,'packed_sample_bytes':ps,'best_standard_lossless':br,'lossless_bytes':lb,'lossless_ratio':(ps/lb if lb else 1.0)})
    report={'schema':'shtenco.nexus-dwe-real-12b/v1','model':MODEL,'revision':REV,'elapsed_seconds':time.time()-t0,'sampled_tensors':sampled,'whole_model_structural':structs,'results':results,'notes':['Weights in distortion rows are real BF16 byte ranges from official Mistral-Nemo 12B Safetensors.','Whole-model structural sizes come from all five official Safetensors headers and are representation arithmetic, not quality claims.','literal-pasted-2bit intentionally preserves the negative-value clipping bug in the supplied sketch.','random_activation_rel_l2 uses deterministic Gaussian probes, not text-calibration activations.']}
    p=Path(args.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(report,indent=2),encoding='utf-8')
    md=p.with_suffix('.md'); sym=[r for r in results if r['centroid_mode']=='symmetric-2bit' and r['norm_bits']==4]; lit=[r for r in results if r['centroid_mode']=='literal-pasted-2bit' and r['norm_bits']==4]
    lines=['# NEXUS DWE real Mistral-Nemo 12B','',f'Model: `{MODEL}` @ `{REV}`','',f'Elapsed: {report["elapsed_seconds"]:.1f}s','', '## Whole-model structural arithmetic','', '|K|centroid bits|norm bits|size MiB|ratio vs BF16|effective bpw|','|---:|---:|---:|---:|---:|---:|']
    for x in structs: lines.append(f'|{x["k"]}|{x["centroid_bits"]}|{x["norm_bits"]}|{x["mib"]:.3f}|{x["ratio_vs_bf16"]:.1f}x|{x["effective_bpw"]:.5f}|')
    lines += ['', '## Real-weight distortion — symmetric 2-bit centroids, 4-bit norms','', '|tensor|K|cos mean|cos p05|NMSE|activation rel L2|index H|std lossless|','|---|---:|---:|---:|---:|---:|---:|---:|']
    for r in sym: lines.append(f'|`{r["tensor"]}`|{r["k"]}|{r["cosine_mean"]:.4f}|{r["cosine_p05"]:.4f}|{r["nmse"]:.4f}|{r["random_activation_rel_l2"]:.4f}|{r["index_entropy_bits"]:.3f}|{r["lossless_ratio"]:.2f}x {r["best_standard_lossless"]}|')
    lines += ['', '## Literal pasted 2-bit quantizer control','', '|tensor|K|cos mean|NMSE|activation rel L2|','|---|---:|---:|---:|---:|']
    for r in lit: lines.append(f'|`{r["tensor"]}`|{r["k"]}|{r["cosine_mean"]:.4f}|{r["nmse"]:.4f}|{r["random_activation_rel_l2"]:.4f}|')
    md.write_text('\n'.join(lines)+'\n',encoding='utf-8'); print(json.dumps({'json':str(p),'md':str(md),'rows':len(results),'elapsed':report['elapsed_seconds']},indent=2))
if __name__=='__main__': main()
