#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, time, urllib.request
from pathlib import Path
import numpy as np

QUESTIONS = [
    ("2+3=?", ["4","5","6","7"], 1),
    ("Capital of France?", ["Berlin","Madrid","Paris","Rome"], 2),
    ("9*7=?", ["54","56","63","72"], 2),
    ("Water formula?", ["H2O","CO2","O2","NaCl"], 0),
    ("sqrt(144)=?", ["10","11","13","12"], 3),
    ("Binary 1010 in decimal?", ["8","10","12","14"], 1),
    ("Capital of Kazakhstan?", ["Almaty","Astana","Shymkent","Aktobe"], 1),
    ("d/dx x^2 = ?", ["x","2x","x^2","2"], 1),
    ("15% of 200?", ["20","25","30","35"], 2),
    ("Which is prime?", ["21","27","29","33"], 2),
    ("SI unit of electric current?", ["volt","watt","ampere","ohm"], 2),
    ("Earth is the ___ planet from the Sun.", ["second","third","fourth","fifth"], 1),
]
LETTERS = ["A","B","C","D"]

def post_json(url: str, payload: dict, timeout: int = 900) -> dict:
    req=urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())

def _prob_from_entry(entry: dict) -> float:
    if "prob" in entry:
        return float(entry["prob"])
    if "logprob" in entry:
        return math.exp(float(entry["logprob"]))
    return 0.0

def get_probs(base: str, q: str, opts: list[str]) -> tuple[np.ndarray,float,str]:
    prompt=q+"\n"+"\n".join(f"{LETTERS[i]}) {x}" for i,x in enumerate(opts))+"\nAnswer with one letter only.\nAnswer:"
    payload={
        "prompt":prompt,
        "n_predict":1,
        "temperature":0.0,
        "n_probs":16,
        "post_sampling_probs":True,
        "grammar":'root ::= "A" | "B" | "C" | "D"',
        "cache_prompt":False,
    }
    t=time.perf_counter(); out=post_json(base+"/completion",payload); dt=time.perf_counter()-t
    p=np.full(4,1e-12,dtype=np.float64)
    cps=out.get("completion_probabilities") or []
    if cps:
        first=cps[0]
        candidates=(first.get("top_probs") or first.get("top_logprobs") or first.get("probs") or [])
        for item in candidates:
            tok=str(item.get("token", item.get("tok_str",""))).strip()
            if tok in LETTERS:
                p[LETTERS.index(tok)]=max(_prob_from_entry(item),1e-12)
        # Include sampled token itself if top-list is absent/partial.
        tok=str(first.get("token", first.get("tok_str",""))).strip()
        if tok in LETTERS:
            p[LETTERS.index(tok)]=max(p[LETTERS.index(tok)], _prob_from_entry(first), 1e-12)
    if p.sum() <= 4.0001e-12:
        content=str(out.get("content","")).strip()[:1]
        if content in LETTERS: p[LETTERS.index(content)]=1.0
    p/=p.sum()
    return p,dt,str(out.get("content",""))

def ry(theta: float) -> np.ndarray:
    c=math.cos(theta/2); s=math.sin(theta/2)
    return np.array([[c,-s],[s,c]],dtype=np.complex128)
I=np.eye(2,dtype=np.complex128)
CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],dtype=np.complex128)

def vqc(p: np.ndarray, th: np.ndarray) -> np.ndarray:
    psi=np.sqrt(np.maximum(p,0)).astype(np.complex128)
    psi/=np.linalg.norm(psi)
    U1=np.kron(ry(float(th[0])), ry(float(th[1])))
    U2=np.kron(ry(float(th[2])), I)
    psi=U1@psi
    psi=CNOT@psi
    psi=U2@psi
    psi=CNOT@psi
    q=np.abs(psi)**2
    q=np.maximum(q.real,1e-15); q/=q.sum()
    return q

def nll(rows, th):
    return -sum(math.log(vqc(p,th)[y]+1e-15) for p,y in rows)/len(rows)

def train_vqc(rows, seed=7, trials=5000):
    rng=np.random.default_rng(seed)
    best=np.zeros(3); score=nll(rows,best)
    for scale,count in [(0.8,trials//2),(0.25,trials//3),(0.08,trials-trials//2-trials//3)]:
        center=best.copy()
        for _ in range(count):
            th=center+rng.normal(0,scale,3)
            s=nll(rows,th)
            if s<score: score=s; best=th
    return best,score

def acc(rows, th=None):
    ok=0
    for p,y in rows:
        pred=int(np.argmax(p if th is None else vqc(p,th)))
        ok+=pred==y
    return ok/len(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--server",default="http://127.0.0.1:8080"); ap.add_argument("--out",default="experiments/results/NEXUS_70B_QUANTUM.json"); a=ap.parse_args()
    rows=[]; lat=[]; raw=[]
    for q,opts,y in QUESTIONS:
        p,dt,text=get_probs(a.server,q,opts); rows.append((p,y)); lat.append(dt); raw.append({"q":q,"p":p.tolist(),"gold":y,"raw":text,"latency_s":dt})
    train=rows[:6]; test=rows[6:]
    theta,train_nll=train_vqc(train)
    t0=time.perf_counter()
    for _ in range(20000): vqc(rows[0][0],theta)
    vqc_us=(time.perf_counter()-t0)/20000*1e6
    result={
      "schema":"shtenco.nexus-70b-vqc/v2",
      "questions":len(rows),"train_questions":6,"test_questions":6,
      "baseline_train_accuracy":acc(train),"baseline_test_accuracy":acc(test),
      "vqc_train_accuracy":acc(train,theta),"vqc_test_accuracy":acc(test,theta),
      "theta":theta.tolist(),"train_nll":train_nll,
      "mean_model_query_seconds":float(np.mean(lat)),"median_model_query_seconds":float(np.median(lat)),
      "simulated_2qubit_vqc_overhead_us":vqc_us,
      "note":"Classically simulated 2-qubit post-logit unitary adapter on real A/B/C/D probabilities from a live 70B model; this is not a quantum speedup and not a hidden-state quantum layer.",
      "rows":raw}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
