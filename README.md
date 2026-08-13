# Information-Graph / CIMFIG Gravity Programme

**Актуальный статус:** 2026-08-13  
**Класс результата:** вычислимая кандидатная архитектура; фундаментальная физическая теория **не заявлена**.

> Finite identity, regression test, conditional continuum statement and proof are different evidence classes. Green CI is not experimental confirmation of nature.

## Central result: `bit -> spacetime candidate`

The positive branch no longer starts from a preset 4D torus. A coordinate-free
binary-route family $R_q$ is frozen on train generations and tested held-out.
For the selected rule

$$
\boxed{q_*=2},
$$

held-out generation 5 gives

$$
\boxed{d_H=2.999229782},\qquad
\boxed{z=0.998281156},
$$

$$
\boxed{d_s^{slice}=3.004393867},\qquad
\boxed{d_s^{history}\approx4.004393867}.
$$

On the same frozen rule

$$
\boxed{
\delta g\sim b^{-2.001707},\quad
\nabla\delta g\sim b^{-3.001458},\quad
\delta R\sim b^{-4.000524}
}
$$

and

$$
\boxed{
\Delta_{simp}\sim b^{-1.994838},\qquad
\Delta_{g_U}\sim b^{-2.019746}.
}
$$

The independent local topology selector gives

$$
Q_2=C_4,\qquad \Sigma C_4\cong S^2.
$$

Details: [`BIT_TO_SPACETIME_CENTRAL_EQUATION.md`](BIT_TO_SPACETIME_CENTRAL_EQUATION.md), [`OBSERVER_SCALE_SMOOTHING.md`](OBSERVER_SCALE_SMOOTHING.md), [`bcqg_observer_smoothing_unified.py`](bcqg_observer_smoothing_unified.py).

## Global 3-manifold: canonical PL completion

The frozen q=2 shell is the octahedral $S^2$. A natural minimal closed simplicial globalization is the boundary of the four-dimensional cross-polytope (16-cell):

$$
(V,E,F,T)=(8,24,32,16),\qquad
\boxed{\beta_{\mathbb F_2}=(1,0,0,1)}.
$$

It has

$$
\operatorname{Lk}(v)=S^2,\qquad
\operatorname{Lk}(e)=S^1,\qquad
\operatorname{Lk}(f)=S^0.
$$

Two full barycentric refinements were checked simplex-by-simplex:

| g | V | E | F | tetrahedra | bad v-links | bad e-links | bad f-links |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 24 | 32 | 16 | 0 | 0 | 0 |
| 1 | 80 | 464 | 768 | 384 | 0 | 0 | 0 |
| 2 | 1696 | 10912 | 18432 | 9216 | 0 | 0 | 0 |

All levels are orientable, every triangle is two-sided and $\partial^2=0$.

**Status:** canonical PL globalization PASS. This proves existence/stability of a natural global $S^3$ completion compatible with the q=2 shell. It does **not** prove that the bare causal rewrite uniquely selects this gluing unless the completion rule is frozen as part of the microscopic model.

Evidence: [`GLOBAL_MANIFOLD_Q2_COMPLETION.md`](GLOBAL_MANIFOLD_Q2_COMPLETION.md), [`bcqg_global_manifold_gate.py`](bcqg_global_manifold_gate.py).

## HDA: old factorization ruled out, route-normal sector constructed

The RHS is fixed independently:

$$
N,M\to\omega=N\,dM-M\,dN\to\beta=\sharp_{E,q}\omega\to D_{path}[\beta].
$$

If

$$
H[N]=H_{geom}[N]\otimes I_{path},
$$

then its commutator has zero path-derivative component while generic off-shell
$D_{path}[\beta]\ne0$. The normalized witness is exactly

$$
\boxed{\Delta_{factor}=1}.
$$

So increasing $J_{max}$ cannot fix HDA while the Hamiltonian is trivial on path
space.

The missing route action has a parameter-free candidate:

$$
\boxed{
H_{path}[N]=\frac12\{N,\sqrt{-\Delta_{path,q}}\}.
}
$$

Its principal symbol obeys, up to one global vector-constraint orientation convention,

$$
\boxed{
\{N|p|_q,M|p|_q\}
=q^{ab}(M\partial_bN-N\partial_bM)p_a.
}
$$

Thus the HDA metric structure function appears without fitting its magnitude.
The finite spectral WKB test gives approximately

$$
\boxed{\Delta_{HDA}^{path}\sim k^{-2.14}}
$$

and reaches a few $10^{-6}$ at the largest tested carrier.

**Status:** route-sector normal-deformation representation PASS at principal-symbol/semiclassical level; full Peter--Weyl Lorentzian HDA remains OPEN until geometry and route factors are coupled in the same Hamiltonian.

Evidence: [`QUANTUM_HDA_KILLER_RESULT.md`](QUANTUM_HDA_KILLER_RESULT.md), [`bcqg_quantum_hda_killer.py`](bcqg_quantum_hda_killer.py), [`scripts/path_normal_hda_gate.py`](scripts/path_normal_hda_gate.py).

## Current canonical frontier

$$
\boxed{
\text{Peter--Weyl }SU(2)
\to H_E+H_L^{(\beta)}
\to H_{geom+route}
\to \text{nontrivial off-shell HDA}
\to \text{DeWitt/GR continuum}
}
$$

The final finite target is preferably densitized:

$$
\boxed{
\frac32\{V,-i[H[N],H[M]]\}
\longrightarrow
\hbar D_{path}[\sharp_{E,q}(N\,dM-M\,dN)].
}
$$

It must converge simultaneously with

$$
\Delta_\beta\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad
z\to1,
$$

and the independent first-class rank must approach $3G+3D+1H$, not BF flatness rank.

Full status: [`THEORY_STATUS.md`](THEORY_STATUS.md)  
Machine ledger: [`theory_gates.json`](theory_gates.json)

## Important negative controls retained

The repository explicitly keeps results that prevent circular claims:

1. minimal dimension-blind binary reconvergence tends to about two dimensions, not four;
2. `EEF`-looking operators and 15j kernels can be pure BF;
3. group-averaged zero commutator is too weak for off-shell HDA;
4. old $V_5$ BF-like kernel is not preserved by the regulator-safe genuine-volume Hamiltonian;
5. local $S^2$ shell alone was insufficient until a global PL completion was declared and tested;
6. full geometry x route HDA is still open.

## Independent IR cross-checks

The repository also retains:

- exact Peter--Weyl left/right gauge covariance and cutoff-wall theorem;
- DeWitt flux inertia $(5+,1-,3\,0)$;
- classical real-Barbero $\beta$ cancellation;
- independent spectral ADM and finite-simplex HDA controls;
- Regge $\to$ Fierz--Pauli / Einstein--Hilbert / cubic Ward scaling;
- preregistered Regge continuation at $L=9,10$: **8/8 PASS**, all relative defect errors below 0.5%;
- separate covariant EPRL/simplicity branch with its blind extrapolation FAIL preserved.

## Fast regression

```bash
python -m pip install -r requirements.txt
python scripts/verify_theory_gates.py
python bcqg_observer_smoothing_unified.py
python bcqg_global_manifold_gate.py
python bcqg_quantum_hda_killer.py
python scripts/path_normal_hda_gate.py
python bcqg_bit_to_gravity_final.py
```

GitHub Actions runs the full core regression automatically on pushes and pull requests.

## Remaining scientific gates

The main unresolved task is now narrow:

$$
\boxed{
H_{geom+route}[N]
\text{ must couple the full Lorentzian Peter--Weyl geometry operator to the already fixed route-normal sector.}
}
$$

Then the preregistered joint HH-D residual, Immirzi cancellation, DeWitt signature and GR constraint rank must converge in one common window without coefficient tuning.

Beyond that remain: uniqueness/dynamical selection of the global q=2 gluing, matter/chirality/anomalies, physical scale setting and independent empirical replication.

$$
\boxed{\text{Strong computational quantum-geometry programme; not a confirmed theory of nature.}}
$$
