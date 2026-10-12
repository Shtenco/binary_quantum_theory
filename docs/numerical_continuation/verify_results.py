"""Replay saved vectors only; do not regenerate microscopic amplitudes."""
import hashlib,json,math,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def freeze(x):return tuple(freeze(v) for v in x) if isinstance(x,list) else x

def run():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text());archive=ROOT/'saved_vectors.zip'
    if hashlib.sha256(archive.read_bytes()).hexdigest()!=manifest['archive_sha256']:raise ValueError('Archive hash mismatch')
    if manifest['physicalization_complete'] is not False:raise ValueError('Unjustified physical completion flag')
    vectors={}; stage_checks=0
    with zipfile.ZipFile(archive) as z:
        meta=json.loads(z.read('metadata.json'))
        for line in z.read('vectors.jsonl').splitlines():
            obj=json.loads(line);vec={}
            for key,re,im in obj['coefficients']:
                a,b=float.fromhex(re),float.fromhex(im)
                if not math.isfinite(a) or not math.isfinite(b):raise ValueError('Non-finite amplitude')
                vec[freeze(key)]=complex(a,b)
            if obj['id'] in vectors:raise ValueError('Duplicate record')
            vectors[obj['id']]=vec
            if obj['id'].startswith('second_stage_HE/'):
                arg=obj['metadata']['arguments'];labels=arg[0][1]
                if any(any(k[1][n][1:3]!=tuple(labels[n][1:3]) for n in arg[3]) for k in vec):raise ValueError('Endpoint charge mismatch')
                stage_checks+=1
    if len(vectors)!=manifest['records']:raise ValueError('Record count mismatch')
    extra=ROOT/'ADDITIONAL_SECOND_STAGE_HE.json'
    if hashlib.sha256(extra.read_bytes()).hexdigest()!=manifest['additional_second_stage_sha256']:raise ValueError('Additional checkpoint hash mismatch')
    for record in json.loads(extra.read_text())['checkpoints']:
        arg=record['arguments'];labels=arg[0][1]
        for key,re,im in record['coefficients']:
            z=complex(float.fromhex(re),float.fromhex(im))
            if not math.isfinite(z.real) or not math.isfinite(z.imag):raise ValueError('Non-finite additional amplitude')
            if any(key[1][n][1:3]!=labels[n][1:3] for n in arg[3]):raise ValueError('Additional charge mismatch')
        stage_checks+=1
    def dot(a,b):return sum(z.conjugate()*b.get(k,0j) for k,z in a.items())
    r=0j
    for b in (1,2,3,4):
        for c in (1,2,3,4):
            if b==c:continue
            for i in (0,1):
                for j in (0,1):
                    for k in (0,1):r+=dot(vectors[f'old_adj/{b}_{c}_{k}_{j}_{i}'],vectors[f'new_CV/{c}_{k}{i}'])
    rd=0j
    for t,(sign,a,b,c) in enumerate(meta['terms']):
        for i in (0,1):
            for j in (0,1):
                for k in (0,1):rd-=sign*dot(vectors[f'old_middle/0_{t:02d}_{i}{k}{j}_1'],vectors[f'new_CK/{a}_{k}{i}'])
    hl=(r-rd)/(2j);key=freeze(meta['source_config']['covariant_key']);expected=vectors['original_HL'][key].conjugate()
    diff=abs(hl-expected);norm=sum(abs(z)**2 for z in vectors['original_HL'].values())
    if diff>2e-12 or abs(norm-.12626247639165408)>2e-12:raise ValueError('Saved-vector replay mismatch')
    return {'passed_saved_vector_replay':True,'scope':'conditional primitive-adjoint weak form; no amplitude regeneration','records':len(vectors),'second_stage_charge_checks':stage_checks,'weak_reverse_HL':[hl.real,hl.imag],'conjugacy_difference':diff,'original_column_norm_squared':norm,'direct_reverse_column_complete':False,'full_error_certified':False,'physicalization_complete':False}
if __name__=='__main__':print(json.dumps(run(),indent=2))
