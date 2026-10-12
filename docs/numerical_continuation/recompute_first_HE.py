"""Recompute one complete enumerated HE image with the pinned backend."""
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[1]

def run():
    manifest=json.loads((ROOT/'BACKEND_MANIFEST.json').read_text())
    for path,digest in manifest['required_backend_sha256'].items():
        if hashlib.sha256((REPO/path).read_bytes()).hexdigest()!=digest:raise RuntimeError('Backend changed: '+path)
    if hashlib.sha256((ROOT/'volume_candidate.py').read_bytes()).hexdigest()!=manifest['volume_candidate_sha256']:raise RuntimeError('Volume candidate changed')
    sys.path.insert(0,str(REPO/'scripts'))
    import volume_candidate as A
    import peter_weyl_covariant_K_sine_composition_gate as S
    A.install();cfg=json.loads((ROOT/'next_column_config.json').read_text());spins,ks=cfg['bra'];key=(tuple(spins),tuple(('C',0,0,ks[v],ks[v]) if v in (0,1) else ('G',ks[v]) for v in range(5)))
    image,v,b=S.complete_HE_sine(key,0,7,charged_nodes=(0,1))
    return {'scope':'one enumerated projected HE image of the pinned finite candidate','support':len(image),'norm_squared':float(sum(abs(z)**2 for z in image.values())),'max_volume_leakage':float(v),'max_branch_basis_leakage':float(b),'full_error_certified':False,'physicalization_complete':False}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args();result=run();text=json.dumps(result,indent=2);print(text)
    if args.output:args.output.write_text(text+'\n')
