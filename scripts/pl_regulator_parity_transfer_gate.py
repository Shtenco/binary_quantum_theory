#!/usr/bin/env python3
"""Show that the K5 doubled-spin Z2 parity rule is regulator-valence dependent.

Each Peter-Weyl fundamental holonomy hit changes the total doubled-spin sum by
an odd integer. A Euclidean T term contains two source-link hits plus the full
dual plaquette of length q, so its global doubled-spin parity changes by
(-1)^(q+2)=(-1)^q. Thus odd-valence primal edges flip parity; even-valence
edges preserve it.

The historical K5 / boundary-4-simplex has q=3. The canonical 16-cell and its
barycentric refinements have only even primal-edge valences over the levels
checked here. We also compute one exact physical-sine 16-cell column as an
amplitude witness.
"""
from __future__ import annotations
import argparse,json,sys
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,boundary_4simplex,seed_16cell_boundary,barycentric_subdivision
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean


def valence_row(name,tets):
    D=DualComplex(tets);c=Counter(len(v) for v in D.edge_incidence.values())
    return {'name':name,'tetrahedra':len(tets),'primal_edges':len(D.edge_incidence),
            'edge_valence_histogram':{str(k):v for k,v in sorted(c.items())},
            'all_even':all(k%2==0 for k in c),'all_odd':all(k%2==1 for k in c)}

def run():
    rows=[valence_row('boundary_4simplex_K5',boundary_4simplex())]
    t=seed_16cell_boundary();rows.append(valence_row('16cell_L0',t))
    for l in (1,2):
        t=barycentric_subdivision(t);rows.append(valence_row(f'16cell_L{l}',t))
    D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D)
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets);col=G.H_sine_basis(seed,0,5,1e-10)
    seed_parity=sum(seed[0])%2
    par=Counter(sum(k[0])%2 for k in col)
    deltas=Counter(sum(k[0])-sum(seed[0]) for k in col)
    amp={'node':0,'support':len(col),'seed_sum_parity':seed_parity,
         'output_sum_parity_counts':{str(k):v for k,v in sorted(par.items())},
         'sum_doubled_spin_delta_counts':{str(k):v for k,v in sorted(deltas.items())},
         'all_outputs_preserve_seed_parity':all((sum(k[0])%2)==seed_parity for k in col)}
    checks={'K5_all_q3':rows[0]['edge_valence_histogram']=={'3':10},
            '16cell_L0_all_even':rows[1]['all_even'],
            '16cell_L1_all_even':rows[2]['all_even'],
            '16cell_L2_all_even':rows[3]['all_even'],
            'exact_16cell_E_column_preserves_parity':amp['all_outputs_preserve_seed_parity'],
            'exact_16cell_E_column_nonzero':amp['support']>0}
    return {'status':'exact regulator-valence transfer theorem for doubled-spin Z2 parity',
            'passed':bool(all(checks.values())),'checks':checks,
            'formula':'DeltaPi_E=(-1)^(q+2)=(-1)^q where q is primal-edge valence / dual-plaquette length',
            'valence_rows':rows,'exact_16cell_amplitude_witness':amp,
            'consequence':'The K5 statement that H_E flips global doubled-spin parity is not a graph-independent theorem. It holds on odd-valence K5 plaquettes (q=3), while the canonical 16-cell barycentric family checked here has even q and H_E preserves the same global parity. Therefore K5 parity-sector orthogonality may not be used to delete ES/SE or mixed collective anomaly channels.',
            'microscopic_scope_note':'This does not invalidate the frozen K5 parity theorem on its declared habitat; it restricts its transfer to general PL refinement.',
            'collective_rule':'Collective Krylov construction and HDA residuals must retain all E/S mixed sectors unless a new refinement-specific grading is independently proved.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
