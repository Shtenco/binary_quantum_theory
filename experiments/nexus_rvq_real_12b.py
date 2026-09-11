#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, struct, time, zlib, lzma
from pathlib import Path
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from nexus_dwe_real_12b import SHARDS, header, get_rows, pick, pack_bits, quality

K=256
CONFIGS=[
    {'name':'PQ8x1','block':8,'stages':1},
    {'name':'PQ16x1','block':16,'stages':1},
    {'name':'RVQ16x2','block':16,'stages':2},
    {'name':'RVQ32x2','block':32,'stages':2},
    {'name':'RVQ64x2','block':64,'stages':2},
]

def logq4(norms):
    eps=1e-12
    lg=np.log2(np.maximum(norms,eps)).astype(np.float32)
    lo=float(np.quantile(lg,0.001)); hi=float(np.quantile(lg,0.999));
    if hi<=lo: hi=lo+1e-6
    s=(hi-lo)/15.0
    q=np.rint((lg-lo)/s).clip(0,15).astype(np.uint8)
    deq=np.exp2(lo+q.astype(np.float32)*s).astype(np.float32)
    return q,deq,lo,s

def int8_centroids(c):
    # Per-centroid symmetric scale. 16-bit scale per centroid is included in storage.
    m=np.max(np.abs(c),axis=1).astype(np.float32); m=np.maximum(m,1e-12); scale=m/127.0
    q=np.rint(c/scale[:,None]).clip(-127,127).astype(np.int8)
    deq=q.astype(np.float32)*scale[:,None]
    return q,deq,scale.astype(np.float16)

def blocks_from_rows(w,b):
    rows,d=w.shape; nblk=math.ceil(d/b); pad=nblk*b-d
    if pad: w=np.pad(w,((0,0),(0,pad)))
    return w.reshape(rows,nblk,b),d

def train_stage(target,b,seed,max_train=24000):
    flat=target.reshape(-1,b).astype(np.float32)
    norms=np.linalg.norm(flat,axis=1).astype(np.float32); norms=np.maximum(norms,1e-12)
    dirs=(flat/norms[:,None]).astype(np.float32)
    rng=np.random.default_rng(seed)
    if len(dirs)>max_train:
        sel=np.sort(rng.choice(len(dirs),max_train,replace=False)); train=dirs[sel]
    else: train=dirs
    km=MiniBatchKMeans(n_clusters=K,random_state=seed,batch_size=1024,n_init=2,max_iter=50,reassignment_ratio=0.0)
    km.fit(train)
    labels=km.predict(dirs).astype(np.uint8)
    # Recompute codewords from assigned full data for better compression fidelity.
    cen=np.zeros((K,b),np.float32); counts=np.bincount(labels.astype(np.int32),minlength=K)
    for i in range(K):
        cen[i]=dirs[labels==i].mean(0) if counts[i] else km.cluster_centers_[i]
    cq,cdeq,cscale=int8_centroids(cen)
    nq,ndeq,nlo,ns=logq4(norms)
    recon=(cdeq[labels.astype(np.int32)]*ndeq[:,None]).reshape(target.shape)
    # Entropy of actual byte labels.
    cnt=np.bincount(labels.astype(np.int32),minlength=K); p=cnt[cnt>0].astype(float); p/=p.sum(); H=float(-(p*np.log2(p)).sum())
    payload=cq.tobytes()+cscale.tobytes()+struct.pack('<ff',nlo,ns)+labels.tobytes()+pack_bits(nq,4)
    return recon,{'labels':labels,'norm_codes':nq,'centroids_q':cq,'centroid_scales':cscale,'norm_lo':nlo,'norm_step':ns,'entropy':H,'payload':payload}

def run_config(w,cfg,seed):
    b=cfg['block']; stages=cfg['stages']; blocks,d=blocks_from_rows(w,b); target=blocks.copy(); total=np.zeros_like(blocks); stage_info=[]
    for s in range(stages):
        rec,info=train_stage(target,b,seed+100*s); total+=rec; target=blocks-total; stage_info.append(info)
    recon=total.reshape(w.shape[0],-1)[:,:d]
    cm,c05,nmse,oerr=quality(w,recon,seed+999)
    payload=b''.join(x['payload'] for x in stage_info); cands={'RAW':len(payload),'zlib9':len(zlib.compress(payload,9)),'lzma9':len(lzma.compress(payload,preset=9))}; best=min(cands,key=cands.get)
    return {'cosine_mean':cm,'cosine_p05':c05,'nmse':nmse,'random_activation_rel_l2':oerr,'stage_index_entropy':[x['entropy'] for x in stage_info],'packed_sample_bytes':len(payload),'best_standard_lossless':best,'lossless_bytes':cands[best],'lossless_ratio':len(payload)/cands[best]}

def structural(all_headers,cfg):
    b=cfg['block']; stages=cfg['stages']; total_raw=total=0; mats=0
    for h,_ in all_headers.values():
        for n,e in h.items():
            if n=='__metadata__' or not isinstance(e,dict) or e.get('dtype') not in {'BF16','F16','F32'}: continue
            shape=e.get('shape',[]); bpe={'BF16':2,'F16':2,'F32':4}[e['dtype']]; raw=int(np.prod(shape))*bpe; total_raw+=raw
            if len(shape)==2:
                o,i=map(int,shape); nblk=o*math.ceil(i/b)
                # Per stage: 8-bit code index + 4-bit block norm; codebook K*b int8 + K fp16 scales.
                total += stages*(nblk + math.ceil(nblk*4/8) + K*b + K*2 + 8 + 128); mats+=1
            else: total += raw
    return {'name':cfg['name'],'block':b,'stages':stages,'bytes':total,'mib':total/2**20,'gib':total/2**30,'ratio_vs_bf16':total_raw/total,'effective_bpw':total*8/(total_raw/2),'raw_bytes':total_raw,'matrices':mats}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rows',type=int,default=128); ap.add_argument('--out',default='experiments/results/NEXUS_RVQ_REAL_12B.json'); args=ap.parse_args(); t0=time.time()
    hs={s:header(s) for s in SHARDS}; structs=[structural(hs,c) for c in CONFIGS]
    # Five representative tensors across model; embedding included as a hard case.
    wanted={'model.embed_tokens.weight','model.layers.0.self_attn.q_proj.weight','model.layers.0.mlp.gate_proj.weight','model.layers.20.mlp.up_proj.weight','model.layers.39.mlp.down_proj.weight'}
    selected=[x for x in pick(hs) if x[0] in wanted]
    results=[]; sampled=[]
    for ti,(name,sh,e,ds) in enumerate(selected):
        rows=min(args.rows,int(e['shape'][0])); print('TENSOR',name,e['shape'],'rows',rows,flush=True); w,row0=get_rows(sh,e,ds,rows); sampled.append({'name':name,'shape':e['shape'],'shard':sh,'row0':row0,'rows':rows})
        for ci,cfg in enumerate(CONFIGS):
            print(' CONFIG',cfg,flush=True); r=run_config(w,cfg,7000+ti*1000+ci*100); r.update({'tensor':name,'shape':e['shape'],**cfg}); results.append(r)
    report={'schema':'shtenco.nexus-rvq-real-12b/v1','model':'mistralai/Mistral-Nemo-Base-2407','revision':'2045759120154383da48ee84ce4bf2f90cc6ec1f','elapsed_seconds':time.time()-t0,'whole_model_structural':structs,'sampled_tensors':sampled,'results':results,'notes':['Real BF16 ranges from official five-shard Mistral-Nemo checkpoint.','PQ/RVQ works on short subvectors rather than entire rows.','Each stage stores one 8-bit code index plus one 4-bit log-norm per block; centroids are int8 with one FP16 scale per centroid.','Full-model perplexity is not measured here; random-activation relative L2 is a local falsification metric.']}
    p=Path(args.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(report,indent=2),encoding='utf-8')
    lines=['# NEXUS block PQ / residual VQ on real Mistral-Nemo 12B','',f'Elapsed: {report["elapsed_seconds"]:.1f}s','', '## Whole-model size arithmetic','', '|config|block|stages|MiB|GiB|effective bpw|ratio vs BF16|','|---|---:|---:|---:|---:|---:|---:|']
    for x in structs: lines.append(f'|{x["name"]}|{x["block"]}|{x["stages"]}|{x["mib"]:.1f}|{x["gib"]:.3f}|{x["effective_bpw"]:.3f}|{x["ratio_vs_bf16"]:.1f}x|')
    lines += ['', '## Real-weight local quality','', '|tensor|config|cos mean|cos p05|NMSE|activation rel L2|index entropy/stage|lossless|','|---|---|---:|---:|---:|---:|---|---|']
    for r in results: lines.append(f'|`{r["tensor"]}`|{r["name"]}|{r["cosine_mean"]:.4f}|{r["cosine_p05"]:.4f}|{r["nmse"]:.4f}|{r["random_activation_rel_l2"]:.4f}|{",".join(f"{x:.2f}" for x in r["stage_index_entropy"])}|{r["lossless_ratio"]:.2f}x {r["best_standard_lossless"]}|')
    p.with_suffix('.md').write_text('\n'.join(lines)+'\n',encoding='utf-8'); print(json.dumps({'elapsed':report['elapsed_seconds'],'results':len(results)},indent=2))
if __name__=='__main__': main()
