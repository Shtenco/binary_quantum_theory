#!/usr/bin/env python3
import ast, json, os, time, urllib.request
from pathlib import Path

MODEL=os.environ['MODEL']
OUT=Path(os.environ.get('OUT','teacher_result_structured.json'))
# Reuse the exact frozen Q literal from the already-published benchmark source,
# without importing/executing that script.
src=Path('nexus_r74_multiteacher_lab/teacher_benchmark.py').read_text(encoding='utf-8')
tree=ast.parse(src)
Q=None
for node in tree.body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='Q' for t in node.targets):
        Q=ast.literal_eval(node.value); break
if Q is None: raise RuntimeError('Frozen Q list not found')

schema={"type":"object","properties":{"answer":{"type":"string","enum":["A","B","C","D"]}},"required":["answer"]}

def ask(prompt):
    body=json.dumps({
        'model':MODEL,
        'messages':[{'role':'user','content':prompt}],
        'stream':False,
        'think':False,
        'format':schema,
        'options':{'temperature':0,'seed':42,'num_predict':32}
    }).encode()
    req=urllib.request.Request('http://127.0.0.1:11434/api/chat',data=body,headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=300) as r: return json.loads(r.read().decode())

rows=[];t0=time.time()
for iid,cat,q,opts,ans in Q:
    prompt='Выбери ровно один правильный вариант A, B, C или D. Верни только запрошенный структурированный ответ.\n\n'+q+'\n'+'\n'.join(opts)
    ts=time.time();err=None;raw='';pred='?'
    try:
        z=ask(prompt);raw=z.get('message',{}).get('content','')
        obj=json.loads(raw); pred=str(obj.get('answer','?')).upper().strip()
        if pred not in ('A','B','C','D'):pred='?'
    except Exception as e: err=repr(e)
    rows.append({'id':iid,'cat':cat,'q':q,'options':opts,'answer':ans,'pred':pred,'correct':pred==ans,'raw':raw,'error':err,'sec':time.time()-ts})
    print(MODEL,iid,pred,ans,pred==ans,flush=True)
cats={}
for c in sorted({r['cat'] for r in rows}):
    z=[r for r in rows if r['cat']==c];cats[c]={'n':len(z),'correct':sum(r['correct'] for r in z),'accuracy':sum(r['correct'] for r in z)/len(z)}
res={'protocol':'R74_STRUCTURED_V2','model':MODEL,'n':len(rows),'correct':sum(r['correct'] for r in rows),'accuracy':sum(r['correct'] for r in rows)/len(rows),'categories':cats,'elapsed_sec':time.time()-t0,'rows':rows}
OUT.write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in res.items() if k!='rows'},ensure_ascii=False,indent=2))
