"""Resume direct HE basis columns of stage two, with JSON checkpoints.

Inverse-holonomy requirements and complete CK actions are not evaluated here.
"""
import argparse,hashlib,json,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[1]

def freeze(x):return tuple(freeze(a) for a in x) if isinstance(x,list) else x

def run(output_dir,max_new_he):
    if max_new_he<0:raise ValueError('max-new-he must be nonnegative')
    backend=json.loads((ROOT/'BACKEND_MANIFEST.json').read_text())
    for path,digest in backend['required_backend_sha256'].items():
        if hashlib.sha256((REPO/path).read_bytes()).hexdigest()!=digest:raise RuntimeError('Backend changed: '+path)
    if hashlib.sha256((ROOT/'volume_candidate.py').read_bytes()).hexdigest()!=backend['volume_candidate_sha256']:raise RuntimeError('Volume candidate changed')
    manifest=json.loads((ROOT/'MANIFEST.json').read_text());archive=ROOT/'saved_vectors.zip'
    if hashlib.sha256(archive.read_bytes()).hexdigest()!=manifest['archive_sha256']:raise RuntimeError('Archive changed')
    sys.path.insert(0,str(REPO/'scripts'))
    import volume_candidate as A
    import peter_weyl_covariant_K_composition_gate as K
    import peter_weyl_covariant_K_composition_cached_gate as B
    import peter_weyl_covariant_K_sine_composition_gate as S
    A.install();source_keys=set();seed_records=[]
    with zipfile.ZipFile(archive) as z:
        for line in z.read('vectors.jsonl').splitlines():
            obj=json.loads(line)
            if obj['id'].startswith('next_middle/'):source_keys.update(freeze(a[0]) for a in obj['coefficients'])
            if obj['id'].startswith('second_stage_HE/'):seed_records.append(obj)
    extra=ROOT/'ADDITIONAL_SECOND_STAGE_HE.json'
    if hashlib.sha256(extra.read_bytes()).hexdigest()!=manifest['additional_second_stage_sha256']:raise RuntimeError('Additional checkpoints changed')
    for checkpoint in json.loads(extra.read_text())['checkpoints']:
        seed_records.append({'metadata':{'arguments':checkpoint['arguments']},'coefficients':checkpoint['coefficients']})
    output_dir.mkdir(parents=True,exist_ok=True)
    config={'archive_sha256':manifest['archive_sha256'],'backend':backend,'wall':7,'additional_sha256':manifest['additional_second_stage_sha256']}
    conf=output_dir/'RUN_CONFIG.json'
    if conf.exists() and json.loads(conf.read_text())!=config:raise RuntimeError('Checkpoint operator/data differs; use a new output-dir')
    conf.write_text(json.dumps(config,indent=2))
    def path_for(arg):return output_dir/(hashlib.sha256(json.dumps(arg,separators=(',',':')).encode()).hexdigest()+'.json')
    for record in seed_records:
        arg=freeze(record['metadata']['arguments']);p=path_for(arg)
        if not p.exists():p.write_text(json.dumps({'arguments':arg,'coefficients':record['coefficients'],'scope':'saved initial direct-HE checkpoint; no total error certificate'},separators=(',',':')))
    requirements=set()
    for key in source_keys:
        key=K.COMP.covariant_key_to_complete(key,0);canonical,_=B.canonicalize_scalar_charge_M(key,(0,));requirements.add((canonical,0,7,(0,)))
        for key in K.CK.apply_volume_complete_state({canonical:1+0j},0):
            canonical,_=B.canonicalize_scalar_charge_M(key,(0,));requirements.add((canonical,0,7,(0,)))
    available=set()
    for arg in requirements:
        p=path_for(arg)
        if p.exists():
            if freeze(json.loads(p.read_text())['arguments'])!=arg:raise RuntimeError('Checkpoint argument mismatch')
            available.add(arg)
    new=0
    for arg in sorted(requirements-available,key=lambda a:(max(a[0][0]),sum(a[0][0]),repr(a)))[:max_new_he]:
        image,v,b=S.complete_HE_sine(arg[0],arg[1],arg[2],charged_nodes=arg[3])
        if any(any(key[1][n][1:3]!=arg[0][1][n][1:3] for n in arg[3]) for key in image):raise RuntimeError('Endpoint charge mismatch')
        data={'arguments':arg,'coefficients':[[key,float(z.real).hex(),float(z.imag).hex()] for key,z in image.items()],'max_volume_leakage':float(v),'max_branch_basis_leakage':float(b),'scope':'one projected direct-HE image; no total error certificate'}
        p=path_for(arg);tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(data,separators=(',',':')));tmp.replace(p);new+=1;available.add(arg)
        print(json.dumps({'new_HE_completed':new,'available_direct_HE':len(available),'required_direct_HE':len(requirements)}),flush=True)
    result={'scope':'direct HE part of second CK stage only','required_direct_HE':len(requirements),'available_direct_HE':len(available),'new_HE':new,'complete_direct_HE':len(available)==len(requirements),'second_CK_actions_completed':0,'direct_reverse_HL_complete':False,'full_error_certified':False,'physicalization_complete':False}
    (output_dir/'progress.json').write_text(json.dumps(result,indent=2));return result
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--max-new-he',type=int,default=2);args=ap.parse_args();print(json.dumps(run(args.output_dir,args.max_new_he),indent=2))
