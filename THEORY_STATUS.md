# Статус теории — актуальный frontier

## Центральная цепь

Текущая strongest candidate architecture больше не начинается с заранее
заданного 4D torus:

$$
\boxed{
\text{binary route bits}
\to q_*=2
\to \text{local }S^2\text{ shell}
\to \text{canonical global PL }M^3
\to D_{slice}\simeq3
\to z\simeq1
\to \text{smooth observer IR}
}
$$

после чего canonical gravity branch требует

$$
\boxed{
\text{Peter--Weyl }SU(2)
\to H_E+H_L^{(\beta)}
\to H_{\rm geom+route}
\to \text{nontrivial off-shell HDA}
\to \text{DeWitt/GR continuum}.
}
$$

Ни один finite PASS ниже не считается экспериментальным подтверждением природы.

## 1. Bit -> 3-space candidate

Frozen family $R_q$ содержит только binary route labels и Hamming adjacency.
Train generations $g=2,3,4$ выбирают $q$ по заранее объявленному score
$D_{slice}\approx3$, $z\approx1$; до held-out $g=5$ фиксируется

$$
\boxed{q_*=2}.
$$

Аналитически для family

$$
\lambda_\ell=2,\qquad \lambda_V=2^{q+1},
$$

поэтому

$$
\boxed{d_H=q+1}.
$$

Held-out transition $4\to5$ даёт

$$
\boxed{d_H=2.999229782},\qquad
\boxed{z=0.998281156},
$$

$$
\boxed{d_s^{slice}=3.004393867},\qquad
\boxed{d_s^{history}\approx4.004393867}.
$$

Независимый topology control, не входивший в selection score, использует
$Q_2=C_4$. Два endpoint states дают

$$
\Sigma C_4\cong S^2,
$$

с Betti $(1,0,1)$.

Observer smoothing на том же frozen rule даёт

$$
\boxed{
\delta g\sim b^{-2.001707},\quad
\nabla\delta g\sim b^{-3.001458},\quad
\delta R\sim b^{-4.000524}
}
$$

и

$$
\boxed{
\Delta_{simp}\sim b^{-1.994838},\qquad
\Delta_{g_U}\sim b^{-2.019746}.
}
$$

Evidence: `bcqg_observer_smoothing_unified.py`,
`OBSERVER_SCALE_SMOOTHING.md`, `BIT_TO_SPACETIME_CENTRAL_EQUATION.md`.

## 2. Global 3-manifold gate

Frozen $q=2$ shell — octahedral $S^2$ with f-vector $(6,12,8)$. A canonical
closed simplicial globalization is the boundary of the 4D cross-polytope
(16-cell):

$$
(V,E,F,T)=(8,24,32,16),
$$

$$
\boxed{\beta_{\mathbb F_2}=(1,0,0,1)}.
$$

It has exactly the required local incidences:

$$
\operatorname{Lk}(v)\cong S^2,\qquad
\operatorname{Lk}(e)\cong S^1,\qquad
\operatorname{Lk}(f)\cong S^0.
$$

The executable gate then performs two global barycentric refinements:

| g | V | E | F | T | bad vertex links | bad edge links | bad face links |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 24 | 32 | 16 | 0 | 0 | 0 |
| 1 | 80 | 464 | 768 | 384 | 0 | 0 | 0 |
| 2 | 1696 | 10912 | 18432 | 9216 | 0 | 0 | 0 |

At all levels $\partial^2=0$, every triangle is two-sided, the complex is
orientable and $\chi=0$.

**Status:** canonical PL completion PASS. It proves existence and recursive PL
stability of a natural $S^3$ globalization compatible with the q=2 shell.
It does **not** prove that the bare causal edge-rewrite graph uniquely selects
this face pairing unless the PL completion is promoted to a frozen microscopic
axiom.

Evidence: `bcqg_global_manifold_gate.py`, `GLOBAL_MANIFOLD_Q2_COMPLETION.md`.

## 3. Canonical geometry already established

The canonical branch still uses finite Peter--Weyl links

$$
\mathcal H_{link}^{J_{max}}
=\bigoplus_{j\le J_{max}}V_j^L\otimes V_j^R,
$$

with exact left/right $SU(2)$ covariance and the per-link cutoff theorem

$$
j_{in}+\frac r2\le J_{max}.
$$

Other retained finite results:

- four spin-$1/2$ faces have a 2D Gauss-singlet geometry sector;
- any 2D four-valent intertwiner sector has scalar absolute volume;
- $j=1$ first distinguishes zero/nonzero volume and several nonzero volume
  scales require intertwiner dimension at least four;
- old $K_5$ vector-link Hilbert $5^{10}$ reduces to 140 Gauss states and a 32D
  fully-active sector;
- $P_{full}W^4|0\rangle$ has fidelity squared $90/91$ with the independent
  five-tetrahedron tensor;
- the old unique $V_5$ kernel is robust but is classified as BF/15j-like, not
  GR;
- the regulator-safe genuine-volume $J_{max}=5/2$ Hamiltonian does **not** keep
  $V_5$ in its kernel: $\|H_0V_5\|=1.4002194669856702$.

## 4. BF negative control remains mandatory

On the same dual $K_5$ graph the known BF/Ooguri projected-flatness structure
has an $EEF$-looking small-curvature form and 15j recursions. Therefore

$$
\boxed{EEF\text{-looking}+15j\text{ kernel}\not\Rightarrow GR.}
$$

Dirac counting separates the universality classes:

$$
SU(2)\ BF:\quad18-2(3G+6F)=0,
$$

whereas

$$
GR:\quad18-2(3G+3D+1H)=4
$$

phase dimensions, i.e. two local metric configuration modes.

## 5. HDA RHS is fixed independently

For node lapses

$$
\omega=N\,dM-M\,dN,
$$

and the generic dual-cell Hodge/RT0 map gives

$$
\beta=\sharp_{E,q}\omega.
$$

The path register supplies a nontrivial diffeomorphism representation

$$
D_{\rm path}[\beta]
$$

with the 2D transverse vector-field Lie defect decreasing approximately as
$L^{-1.98}$.

Preferred inverse-volume-free target:

$$
\boxed{
\frac32\{V,-i[H[N],H[M]]\}
\longrightarrow
\hbar D_{\rm path}[\sharp_{E,q}(N\,dM-M\,dN)].
}
$$

## 6. Exact HDA no-go for the old tensor factorisation

If the Hamiltonian acts as

$$
H[N]=H_{geom}[N]\otimes I_{path},
$$

then its commutator has zero path-derivative component. For nonconstant lapses
the independently constructed RHS has $D_{path}[\beta]\ne0$. The normalized
path-channel witness is exactly

$$
\boxed{\Delta_{factor}=1}.
$$

Thus increasing $J_{max}$ or the spin-network basis cannot repair HDA while
$H$ remains trivial on the path factor.

## 7. Constructive route-normal HDA representation

The missing path action has a parameter-free candidate:

$$
\boxed{
H_{path}[N]=\frac12\{N,\Omega_q\},\qquad
\Omega_q=\sqrt{-\Delta_{path,q}}.
}
$$

Its symbol is

$$
h_N=N\sqrt{q^{ab}p_ap_b}.
$$

Direct symbol calculus gives, up to one global vector-constraint orientation
convention,

$$
\boxed{
\{h_N,h_M\}
=q^{ab}(M\partial_bN-N\partial_bM)p_a.
}
$$

Metric-derivative terms cancel. The finite spectral path test on WKB carriers
$k=2,3,4,6,8,12,16,24$ gives approximately

$$
\boxed{\Delta_{HDA}^{path}\sim k^{-2.14}},
$$

with the largest-carrier defect at a few $10^{-6}$.

**Status:** route-sector normal-deformation representation PASS at principal
symbol / semiclassical level. The full Peter--Weyl Lorentzian HDA is **not yet
closed** because the geometry Hamiltonian has not yet been coupled to this same
route-normal domain.

Evidence: `scripts/path_normal_hda_gate.py`, `bcqg_quantum_hda_killer.py`,
`QUANTUM_HDA_KILLER_RESULT.md`.

## 8. Lorentzian / DeWitt controls retained

Flux pullback of the DeWitt supermetric gives

$$
\boxed{(5+,1-,3\,0)}.
$$

Within the local two-derivative ADM ansatz HDA closure fixes

$$
\boxed{c_{DW}=1/2,\qquad AB=1},
$$

leaving Newton scale and $\Lambda$ free. Hence $c_T=1$ and conditional Dirac
counting in $D=3$ gives two physical metric modes.

For real Ashtekar--Barbero variables the isolated kinetic sector obeys

$$
\boxed{H_E^{kin}+H_L^{corr}=H_{DW}}
$$

for real $\beta$ at machine precision. This is a classical regression target,
not quantum Immirzi-independence proof.

The conservative full Lorentzian nested-commutator hit wall remains

$$
r_e(H_E)=2,\qquad r_e(H_L)=6,\qquad r_e(HH)=12,
$$

so all-$j=1/2$ HH is guaranteed transient-cutoff-safe at $J_{max}=13/2$.
Support-only reachability is finite: 615884 admissible spin assignments / about
11.3M spin-network states after one HH pair, assembled from only 2850 local
blocks of size at most $7\times7$.

## 9. Independent covariant branch

The Plebański/Urbantke and EPRL/simplicity line remains separate from the
canonical real-$SU(2)$ Hamiltonian. In particular

$$
P_{simp}=F(F^\dagger F)^{-1}F^\dagger
$$

is normalization-independent, coherent simplicity rays pass, and the old
preregistered single-power extrapolation at $j=15/2$ remains an honest FAIL.

## 10. Regge -> GR cross-check

The fixed-4D Regge scaffold independently approaches Fierz--Pauli,
Einstein--Hilbert and cubic Ward identities. The law frozen on $L=5..8$
predicted held-out $L=9,10$: **8/8 checks passed**, all relative defect errors
below 0.5 percent. This is an IR cross-check, not microscopic derivation.

## Current single bottleneck

The remaining canonical killer is now much narrower:

$$
\boxed{
H_{geom+route}[N]
\quad\text{must couple Peter--Weyl Lorentzian geometry to}\quad
\frac12\{N,\sqrt{-\Delta_{path,q}}\}
}
$$

on one common graph-changing domain, after which the preregistered densitized
HH-D residual must satisfy

$$
\boxed{\Delta_{HH}^{off}\to0}
$$

without coefficient tuning, simultaneously with

$$
\Delta_\beta\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad
z\to1,
$$

and first-class rank must approach $3G+3D+1H$, not BF flatness rank.

Open beyond that: uniqueness/dynamical selection of the global q=2 gluing,
matter/chirality/anomalies, physical scale setting and independent empirical
replication.
