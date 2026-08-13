# Contribution and research-integrity rules

This repository mixes exact algebra, finite numerical evidence, conditional continuum arguments and open physical hypotheses. Changes must preserve those distinctions.

## Before changing physics claims

1. Rebase or compare against the current `main`.
2. Read `THEORY_STATUS.md` and `theory_gates.json` first.
3. Do not merge an older generated/Codex branch if it overwrites a newer status/ledger.
4. Preserve negative results, blind FAILs and rejected regulator choices.

## Required changes for a claim update

A pull request that changes a scientific claim must update all relevant layers:

- human status: `THEORY_STATUS.md`;
- machine status: `theory_gates.json`;
- reproducible evidence: script/report/source file;
- falsifier or negative control when applicable.

`tested_finite`, `conditional` and `proved` are not synonyms. A finite regression result may not be promoted to `proved` unless a proof actually exists for the stated domain.

## No post-hoc repair

A failed preregistered prediction remains in the repository. If a model, exponent, operator ordering, cutoff or normalization is changed after observing a failure, the new version must receive a new test and must not overwrite the old result.

## Canonical and covariant routes

Do not silently mix the two gravity programmes:

- canonical real-`SU(2)`: Peter--Weyl holonomy/flux variables, Euclidean + Lorentzian Hamiltonian, graph-changing/off-shell HDA;
- covariant BF/spinfoam: simplicity projection and EPRL/FK-like amplitudes.

EPRL simplicity is not automatically preprocessing for the real-`SU(2)` canonical Hamiltonian.

## HDA discipline

Graph or spin change is not, by itself, an HDA anomaly. An HDA claim must compare the Hamiltonian commutator with a declared nontrivial diffeomorphism action on the same domain/habitat. Group-averaged zero alone is not sufficient.

The current target is

$$
[\hat H[N],\hat H[M]]
\stackrel{?}{\longrightarrow}
i\hbar\,\hat D_{\rm path}\!\left[\sharp_{E,q}(N\,dM-M\,dN)\right].
$$

## Local checks before pushing

```bash
python -m pip install -r requirements.txt
python scripts/verify_theory_gates.py
python scripts/validate_github_latex.py
python scripts/verify_sine_bridge.py
python scripts/verify_connection_ward.py
python scripts/verify_geometric_cell.py
python scripts/dual_k5_lapse_cochain_gate.py
python scripts/dual_cell_sharp_rt0_gate.py
python scripts/path_rerouting_diffeo_gate.py
python scripts/path_diffeo_lie_gate.py
python scripts/path_vector_diffeo_gate.py
python scripts/lorentzian_hit_depth_bound.py
```

GitHub Actions runs the corresponding core regression on pushes and pull requests targeting `main`.
