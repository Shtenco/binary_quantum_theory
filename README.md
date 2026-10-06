# Бинарная квантовая гравитация (BQG)
## Emergence Program: от бинарной квантовой информации к геометрии

**Канонический README — 6 октября 2026**

---

# 1. Главный вопрос

> **Может ли геометрия, расстояние, размерность, причинность и затем эффективная гравитация возникать из физической структуры бинарной квантовой информации?**

Текущая каноническая цепочка:

$$
\boxed{
\text{binary quantum degrees of freedom}
\to
\text{SU(2) physical reduction}
\to
\text{noncommuting relational observables}
\to
\text{oriented volume}
\to
\text{local isotropy}
\to
\text{entangled gluing}
\to
\text{local information response}
\to
\text{weighted graph geometry}
\to
\text{spectral dimension}
\to
\text{physical graph dynamics}
\to
\text{causality}
\to
\text{effective gravity}
}
$$

Канонический принцип:

$$
\boxed{\text{симметрия сначала, вычисления потом}.}
$$

И столь же важно:

$$
\boxed{\text{отрицательный результат фиксируется так же строго, как положительный}.}
$$

---

# 2. Один physical node: exact local theorem

Для четырёх spin-$1/2$ после SU(2) Gauss reduction

$$
\boxed{
\mathcal H_{\rm phys}^{(4)}
=\mathrm{Inv}_{SU(2)}[(\tfrac12)^{\otimes4}],
\qquad \dim=2.
}
$$

В basis $|s\rangle,|t\rangle$

$$
Q_{123}=\epsilon_{abc}J_1^aJ_2^bJ_3^c
$$

и exact identity

$$
\boxed{
Q_{123}=i[\mathbf J_1\!\cdot\!\mathbf J_2,\mathbf J_2\!\cdot\!\mathbf J_3].
}
$$

В physical sector

$$
\boxed{Q_{123}^{\rm phys}=\frac{\sqrt3}{4}\sigma_y.}
$$

Volume eigenstates

$$
\boxed{
|\Psi_\pm\rangle=\frac{|s\rangle\pm i|t\rangle}{\sqrt2},
\qquad q_\pm=\pm\frac{\sqrt3}{4}.
}
$$

Именно они являются единственными pure pair-spectrum isotropic states.

Для

$$
\mathcal A_p=\sum_{i<j}\left(p_{ij}-\frac12\right)^2
$$

выполняется

$$
\boxed{\mathcal A_p=4(\Delta Q_{123})^2.}
$$

Следовательно

$$
\boxed{
\text{pair-spectrum isotropy}
\Longleftrightarrow
\text{sharp oriented quantum volume}.
}
$$

Файлы:

- `BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md`
- `scripts/bqg_minimal_entanglement_volume_gate.py`

---

# 3. Reduced gluing

Candidate two-node shape-matching Hamiltonian

$$
\boxed{
H_{\rm glue}
=\sum_a(P_a^{(A)}-P_a^{(B)})^2
=\frac32I-\frac34(X_AX_B+Z_AZ_B).
}
$$

Spectrum

$$
\boxed{\{0,\tfrac32,\tfrac32,3\}.}
$$

Unique zero-mismatch state

$$
\boxed{|\Phi^+\rangle=\frac{|ss\rangle+|tt\rangle}{\sqrt2}.}
$$

И

$$
\boxed{Q_AQ_B|\Phi^+\rangle=-\frac3{16}|\Phi^+\rangle.}
$$

То есть exact shape matching в этой reduced model выбирает maximally entangled intertwiner state с sharp relative orientation.

**Статус математики: EXACT для заданного reduced Hamiltonian.**

**Статус $H_{\rm glue}$ как fundamental BQG dynamics: CANDIDATE.**

Файлы:

- `BQG_TWO_NODE_REDUCED_GLUING_RESULT.md`
- `scripts/bqg_two_node_reduced_gluing_gate.py`

---

# 4. Network hierarchy and exact many-node reduction

Для chain $A-B-C$:

$$
\boxed{I(A:B)=I(B:C)\approx0.7982479266\ \text{bit},}
$$

$$
\boxed{I(A:C)=0.5\ \text{bit}.}
$$

Current many-node Hamiltonian

$$
\boxed{
H_M
=\sum_{i=1}^{M-1}
\left[\frac32I-\frac34(X_iX_{i+1}+Z_iZ_{i+1})\right]
}
$$

после локальной rotation становится open XX model:

$$
\boxed{
H_M\simeq
\frac32(M-1)I
-\frac34\sum_i(X_iX_{i+1}+Y_iY_{i+1}).
}
$$

После Jordan-Wigner:

$$
\boxed{
H_M
=\frac32(M-1)I
-\frac32\sum_i(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i).
}
$$

Single-particle energies

$$
\boxed{\varepsilon_n=-3\cos\frac{n\pi}{M+1}.}
$$

Gap closes as

$$
\boxed{\Delta_M=O(M^{-1})\to0.}
$$

Файлы:

- `BQG_THREE_NODE_REDUCED_CHAIN_RESULT.md`
- `scripts/bqg_three_node_reduced_chain_gate.py`
- `BQG_MANY_NODE_FREE_FERMION_MAPPING.md`
- `scripts/bqg_many_node_xx_mapping_gate.py`

---

# 5. Critical/gapped correlation laws

Critical phase:

$$
\boxed{
\langle c_0^\dagger c_r\rangle=\frac{\sin(\pi r/2)}{\pi r}
}
$$

and

$$
\boxed{
C_x(r)=A_xr^{-1/2}[1+O(r^{-2})],
\qquad A_x\approx0.58835.
}
$$

Hence

$$
\boxed{
I_0(r)=\frac{A_x^2}{\ln2}\frac1r+O(r^{-2})
\approx\frac{0.50}{r}\ \text{bit}.
}
$$

Controlled staggered-volume deformation:

$$
\boxed{H_m=H_0+m\sum_j(-1)^jZ_j.}
$$

Two-band spectrum:

$$
\boxed{E_\pm(k)=\pm\sqrt{(2m)^2+9\cos^2k}.}
$$

Gap:

$$
\boxed{\Delta_{\rm sp}=2|m|.}
$$

Correlation length:

$$
\boxed{\xi^{-1}=\operatorname{arsinh}\left(\frac{2|m|}{3}\right).}
$$

Gapped asymptotics:

$$
\boxed{
I_m(r)\sim B(m)r^{-1}e^{-2r/\xi}.
}
$$

---

# 6. Scalar-distance no-go

Critical phase требует

$$
f(I)\sim A/I,
$$

а gapped phase требует

$$
f(I)\sim A'\ln(1/I).
$$

Поэтому

$$
\boxed{
\textbf{не существует одной phase-independent scalar function }
d=f(I_{ij})
\textbf{, asymptotically linear в обеих фазах.}
}
$$

Long-range pair mutual information остаётся observable, но не универсальной spatial coordinate.

Файлы:

- `BQG_MUTUAL_INFORMATION_ASYMPTOTIC_RESULT.md`
- `scripts/bqg_mutual_information_asymptotic_gate.py`
- `BQG_GAPPED_DEFORMATION_DISTANCE_NOGO.md`
- `scripts/bqg_gapped_distance_nogo_gate.py`

---

# 7. Local information conductance and additive metric

Для edge $e=(ij)$ вводим relative twist generator

$$
\boxed{K_e=\frac{Z_i-Z_j}{2}.}
$$

Relative-twist QFI conductance:

$$
\boxed{g_e^{\rm QFI}=\frac14F_Q(\rho_e,K_e).}
$$

Critical reference scale:

$$
\boxed{
F_{Q,*}=\frac{32}{\pi^2+4},
\qquad
g_*=\frac{8}{\pi^2+4}.
}
$$

Edge resistance length:

$$
\boxed{\ell_e=\ell_*\frac{g_*}{g_e}.}
$$

Network distance:

$$
\boxed{d(i,j)=\min_{\gamma:i\to j}\sum_{e\in\gamma}\ell_e.}
$$

На chain/tree additivity along geodesics exact. Один и тот же rule применяется к critical и gapped phases.

Файлы:

- `BQG_LOCAL_INFORMATION_RESISTANCE_METRIC.md`
- `scripts/bqg_local_information_resistance_gate.py`

---

# 8. Exact QFI-weighted spectral dimension calibration

Weighted Laplacian:

$$
\boxed{(L_g)_{ij}=\delta_{ij}\sum_k g_{ik}-g_{ij}.}
$$

Return probability:

$$
\boxed{P(\tau)=\frac1N\operatorname{Tr}e^{-\tau L_g}.}
$$

Spectral dimension:

$$
\boxed{d_s(\tau)=-2\frac{d\ln P}{d\ln\tau}.}
$$

Для infinite homogeneous $D$-dimensional hypercubic graph:

$$
\boxed{
P_D(\tau)=\left[e^{-2g\tau}I_0(2g\tau)\right]^D
}
$$

и

$$
\boxed{
d_s^{(D)}(\tau)=4Dg\tau\left[1-\frac{I_1(2g\tau)}{I_0(2g\tau)}\right].
}
$$

Therefore

$$
\boxed{\lim_{\tau\to\infty}d_s^{(D)}=D.}
$$

При dimensionless time $u=g\tau$ conductance исчезает, поэтому quantum phase меняет diffusion scale, но не dimension фиксированной topology.

Файлы:

- `BQG_QFI_SPECTRAL_DIMENSION_RESULT.md`
- `scripts/bqg_qfi_spectral_dimension_gate.py`

---

# 9. Branching topology control

Для infinite 3-regular Bethe lattice

$$
\boxed{\lambda_0=3-2\sqrt2>0}
$$

и

$$
P_{\rm Bethe}(\tau)\sim A\tau^{-3/2}e^{-g\lambda_0\tau}.
$$

Hence

$$
\boxed{d_s^{\rm Bethe}(\tau)=2g\lambda_0\tau+3+o(1)\to\infty.}
$$

То есть exponential branching не маскируется под finite-dimensional Euclidean geometry.

---

# 10. Первый topology-free emergence gate

Теперь cubic/square/chain topology удалена из generator полностью.

Minimal BQG-inspired surrogate использует только:

1. maximum valence $4$;
2. preference for free valence;
3. local loop closure within graph distance $\le2$;
4. probability $p_2$ второго локального edge;
5. no coordinate labels;
6. no target dimension;
7. no spectral feedback.

Это **SURROGATE / CANDIDATE graph dynamics**, не fundamental BQG constraint.

Для topology gate используется homogeneous critical QFI conductance $g_*$, чтобы изолировать topology. Uniform $g$ лишь rescale diffusion time и не меняет plateau value.

Automatic plateau detector заранее калиброван на known 1D/2D lattices и затем frozen.

Файлы:

- `BQG_TOPOLOGY_FREE_EMERGENCE_RESULT.md`
- `scripts/bqg_topology_free_emergence_gate.py`

---

# 11. Topology-free result: НЕ 3D

Для шести fixed seeds:

### $N=150$

$$
\boxed{d_s^{\rm plateau}\approx1.316\pm0.106}
$$

valid in $5/6$ realizations.

### $N=300$

$$
\boxed{d_s^{\rm plateau}\approx1.226\pm0.031}
$$

valid in $5/6$ realizations.

### $N=500$

$$
\boxed{d_s^{\rm plateau}\approx1.232\pm0.030}
$$

valid in $6/6$ realizations.

The $N=300$ and $N=500$ values are stable within ensemble spread.

Thus the first topology-free surrogate does **not** drift toward $3$ over the tested size range.

Its average transitivity is around

$$
T\approx0.20-0.21,
$$

and mean degree approaches

$$
\langle k\rangle\approx3,
$$

so it is not simply a tree.

---

# 12. Matched random null

Matched null preserves:

- max valence $4$;
- same growth schedule;
- same free-valence preference;
- same second-edge probability;

but removes local closure preference.

For $N=300$:

$$
\boxed{0/12}
$$

null realizations produced an accepted finite plateau under the same frozen detector.

The null has almost the same mean degree

$$
\langle k\rangle\approx2.97
$$

but transitivity only

$$
T\approx0.011.
$$

So local closure changes diffusion geometry qualitatively, but still does not produce $d_s\approx3$.

---

# 13. Robustness scan

We do **not** tune $p_2$ to dimension.

Scan:

$$
p_2\in\{0.25,0.40,0.50,0.60,0.75\}.
$$

Whenever a stable plateau is detected, its ensemble mean remains approximately below

$$
\boxed{d_s\lesssim1.4}
$$

for the tested sizes and seeds.

No robust $d_s\approx3$ window appears.

Therefore the current result is a genuine falsification of the minimal surrogate rule, not a failed parameter search.

---

# 14. First topology-free no-go

The tested local rule is

$$
\boxed{
\text{four-valent capacity}
+
\text{local free-valence attachment}
+
\text{local loop closure}.
}
$$

It generates a nontrivial low-dimensional diffusion geometry, but not 3D.

Hence:

$$
\boxed{
\textbf{four-valence plus local loop closure is insufficient to derive }d_s\approx3.
}
$$

This is the first topology-free no-go of the emergence program.

It does **not** prove that BQG cannot produce three dimensions. It proves that the present minimal surrogate cannot.

---

# 15. What is missing

The surrogate generator does not yet include:

- full physical projector;
- graph-changing Hamiltonian/master constraints;
- amplitudes from physical history dynamics;
- self-consistent edge-dependent QFI weights;
- interference between gluing histories;
- Pachner-like move amplitudes derived from BQG;
- a dynamical penalty selecting polynomial-growth/manifold-like graphs.

Therefore the central missing object is no longer another graph-growth heuristic.

It is a **physical graph-transition kernel**.

---

# 16. New true frontier: derive graph dynamics from BQG itself

The next target is

$$
\boxed{
\mathcal A(G\to G')
\propto
\langle G'|\Pi_{\rm phys}|G\rangle
}
$$

or an equivalent effective graph-changing kernel derived from constraints/history dynamics.

Then the pipeline becomes

$$
\boxed{
\text{fundamental BQG graph amplitudes}
\to
\text{graph-history ensemble}
\to
\text{self-consistent local }\rho_{ij}
\to
\text{QFI conductances}
\to
L_g
\to
P(\tau)
\to
d_s(\tau).
}
$$

Only if this physical ensemble yields a robust plateau near

$$
\boxed{d_s^{IR}\approx3}
$$

without coordinate labels, cubic connectivity or spectral fitting will we have a serious emergent-3D result.

---

# 17. Current strongest statements

1. $Q=i[D_{12},D_{23}]$.
2. $Q_{\rm phys}=(\sqrt3/4)\sigma_y$.
3. Local isotropy iff oriented volume is sharp.
4. $\mathcal A_p=4(\Delta Q)^2$.
5. Reduced two-node matching selects Bell-type intertwiner entanglement.
6. Current many-node chain maps exactly to free fermions.
7. Critical $I_0(r)\sim\kappa/r$.
8. Staggered oriented-volume deformation opens exact gap $2|m|$.
9. Gapped $I_m(r)\sim Br^{-1}e^{-2r/\xi}$.
10. No universal global scalar distance $d=f(I_{ij})$ works in both phases.
11. Relative-twist QFI defines a phase-robust local conductance rule.
12. Resistance composition gives an additive network metric.
13. Homogeneous QFI-weighted hypercubic graphs satisfy $d_s\to D$ exactly.
14. Quantum phase rescales diffusion time but not spectral dimension of fixed topology.
15. Bethe branching has no finite IR spectral-dimension plateau.
16. **Topology-free valence-4 + local-loop surrogate yields $d_s\approx1.23$, not $3$.**
17. Therefore minimal local gluing heuristics are insufficient; actual graph-changing BQG dynamics is now the decisive missing layer.

---

# 18. What is NOT proved

We do not claim that:

- $H_{\rm glue}$ is already derived from fundamental BQG constraints;
- relative-twist QFI is the unique fundamental metric source;
- $K_{ij}$ is already derived from the physical projector;
- $\ell_*$ is derived from first principles;
- continuum space has been derived as 3D;
- the topology-free surrogate is the true BQG graph dynamics;
- causal Lorentzian propagation has been derived;
- Einstein equations have been obtained;
- $G,c,\hbar$ have been derived from binary microphysics.

Key caveat:

$$
\boxed{
\text{exact mathematics of a reduced/surrogate model}
\neq
\text{proof that it is fundamental dynamics}.
}
$$

---

# 19. Canonical principle

> **Сначала уменьшить задачу симметрией. Затем распознать точную математическую структуру. Потом решить её аналитически. Отрицательные результаты фиксировать так же строго, как положительные. И только если exact путь закрыт — считать численно.**

Репозиторий: `Shtenco/binary_quantum_theory`
