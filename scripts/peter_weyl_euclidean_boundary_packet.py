#!/usr/bin/env python3
"""Serialize the complete 5x32 Euclidean q=2 boundary constraint packet.

This is the reusable microscopic E-sector input for the BQG master assembler.
All five node constraints H_E,v are applied to all 32 frozen all-j=1/2 Gauss
boundary states with the same regulator-safe Peter-Weyl implementation used by
the canonical five-node boundary master.  Every sparse outgoing column is
written once, hashed, and the resulting M_EE Gram is audited without re-running
the microscopic action.

The 32D boundary is deliberately marked domain_complete=false.  Its full-rank
compressed master is a boundary diagnostic, not the full physical projector.
"""
from __future__ import annotations

import argparse, hashlib, json, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_constraint_column as COL
import bqg_constraint_master_assembler_gate as MASTER

EXPECTED_NODE0_INPUT0_SHA="a5b5461cdaeedd1baf49dcfac881eda96e3d04cea182b8b6b639f5a6a585edbf"


def canonical_packet_hash(rows):
    h=hashlib.sha256()
    for r in rows:
        h.update(f"{r['family']}:{r['node']}:{r['input_index']}:{r['sha256']}\n".encode())
    return h.hexdigest()


def run(outdir:Path,jmax2=5,prune=1e-8):
    basis=PW.basis_full_jhalf()
    if len(basis)!=32: raise RuntimeError(f"expected 32 boundary states, got {len(basis)}")
    coldir=outdir/'columns'; coldir.mkdir(parents=True,exist_ok=True)
    packet_rows=[]; images={v:[] for v in range(5)}; support=[]; norms=[]
    for v in range(5):
        for i in range(32):
            payload=COL.run(v,i,jmax2,prune)
            p=coldir/f'E_node{v}_input{i:02d}.json'
            p.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
            rows=payload['complete_gauss_outgoing_column']['state']
            st=MASTER.decode_state_rows(rows)
            images[v].append(st)
            support.append(payload['complete_gauss_outgoing_column']['support'])
            norms.append(payload['complete_gauss_outgoing_column']['norm'])
            packet_rows.append({
                'family':'E','node':v,'input_index':i,
                'path':str(p.relative_to(outdir)),
                'sha256':payload['column_sha256'],
                'support':payload['complete_gauss_outgoing_column']['support'],
                'norm':payload['complete_gauss_outgoing_column']['norm'],
            })

    MEE=np.zeros((32,32),complex); node_rows=[]
    for v in range(5):
        G=MASTER.gram(images[v]); MEE+=G
        node_rows.append({'node':v,'trace':float(np.trace(G).real),'frobenius_norm':float(np.linalg.norm(G))})
    MEE=.5*(MEE+MEE.conj().T); audit=MASTER.spectral_audit(MEE)
    manifest={
        'schema':'BQG_MICROSCOPIC_CONSTRAINT_PACKET_V1',
        'status':'complete Euclidean q=2 boundary outgoing-column packet',
        'family':'E','domain_label':'q2_all_jhalf_K5_boundary','domain_dimension':32,
        'domain_complete':False,'nodes':[0,1,2,3,4],'Jmax':jmax2/2,'prune_threshold':prune,
        'columns':packet_rows,'packet_sha256':canonical_packet_hash(packet_rows),
        'M_EE':{
            'rank':audit['rank'],'nullity':audit['nullity'],'rank_tolerance':audit['rank_tolerance'],
            'eigenvalue_min':float(np.min(audit['eigenvalues'])),'eigenvalue_max':float(np.max(audit['eigenvalues'])),
            'smallest_positive':audit['smallest_positive'],'condition_number_on_support':audit['condition_number_on_support'],
            'trace':float(np.trace(MEE).real),'frobenius_norm':float(np.linalg.norm(MEE)),
            'hash':MASTER.hash_arrays(MEE),'per_node':node_rows,
        },
        'support_summary':{'min':int(min(support)),'max':int(max(support)),'mean':float(np.mean(support))},
        'norm_summary':{'min':float(min(norms)),'max':float(max(norms)),'mean':float(np.mean(norms))},
        'regression':{
            'node0_input0_sha_expected':EXPECTED_NODE0_INPUT0_SHA,
            'node0_input0_sha_observed':packet_rows[0]['sha256'],
            'matches_existing_export':packet_rows[0]['sha256']==EXPECTED_NODE0_INPUT0_SHA,
        },
        'passed':bool(packet_rows[0]['sha256']==EXPECTED_NODE0_INPUT0_SHA and len(packet_rows)==160),
        'claim_boundary':'Complete reusable E-sector boundary packet only. domain_complete=false: no physical-projector claim follows from the compressed 32D spectrum.'
    }
    (outdir/'euclidean_packet_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    return manifest


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-dir',type=Path,default=Path('euclidean_boundary_packet'))
    ap.add_argument('--jmax2',type=int,default=5);ap.add_argument('--prune',type=float,default=1e-8)
    a=ap.parse_args();out=run(a.output_dir,a.jmax2,a.prune)
    print(json.dumps({k:v for k,v in out.items() if k!='columns'},indent=2))
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
