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
\text{causality}
\to
\text{effective gravity}
}
$$

Канонический метод проекта:

$$
\boxed{\text{симметрия сначала, вычисления потом}.}
$$

Мы сначала уменьшаем Hilbert space, затем ищем exact algebraic structure, затем asymptotics и только потом используем численность как независимый gate.

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

В basis $|s\rangle,|t\rangle$ oriented volume

$$
Q_{123}=\epsilon_{abc}J_1^aJ_2^bJ_3^c
$$

удовлетворяет exact identity

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

# 3. Два physical nodes: reduced gluing

Три local shape projectors дают candidate matching Hamiltonian

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

Локально

$$
\langle Q_A\rangle=\langle Q_B\rangle=0,
$$

но relative orientation sharp:

$$
\boxed{Q_AQ_B|\Phi^+\rangle=-\frac3{16}|\Phi^+\rangle.}
$$

**Статус математики: EXACT для заданного reduced Hamiltonian.**

**Статус $H_{\rm glue}$ как fundamental BQG dynamics: CANDIDATE.**

Файлы:

- `BQG_TWO_NODE_REDUCED_GLUING_RESULT.md`
- `scripts/bqg_two_node_reduced_gluing_gate.py`

---

# 4. Три узла и первый network hierarchy

Для chain $A-B-C$ symmetry-neutral ground sector:

$$
\boxed{I(A:B)=I(B:C)\approx0.7982479266\ \text{bit},}
$$

$$
\boxed{I(A:C)=0.5\ \text{bit}.}
$$

Volume correlations независимо подтверждают topology:

$$
\boxed{
\langle Q_AQ_B\rangle=\langle Q_BQ_C\rangle=-\frac3{32},
\qquad
\langle Q_AQ_C\rangle=0.
}
$$

Файлы:

- `BQG_THREE_NODE_REDUCED_CHAIN_RESULT.md`
- `scripts/bqg_three_node_reduced_chain_gate.py`

---

# 5. Exact many-node reduction

Для $M$ узлов

$$
\boxed{
H_M
=\sum_{i=1}^{M-1}
\left[
\frac32I-\frac34(X_iX_{i+1}+Z_iZ_{i+1})
\right].
}
$$

После локальной rotation

$$
\boxed{
H_M\simeq
\frac32(M-1)I
-\frac34\sum_i(X_iX_{i+1}+Y_iY_{i+1}).
}
$$

То есть current reduced chain точно эквивалентна open XX model.

Jordan-Wigner:

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

Gap:

$$
\boxed{
\Delta_M^{\rm even}=3\sin\frac{\pi}{2(M+1)},
\qquad
\Delta_M^{\rm odd}=3\sin\frac{\pi}{M+1}.
}
$$

Следовательно

$$
\boxed{\Delta_M=O(M^{-1})\to0.}
$$

Current chain critical/gapless.

Файлы:

- `BQG_MANY_NODE_FREE_FERMION_MAPPING.md`
- `scripts/bqg_many_node_xx_mapping_gate.py`

---

# 6. Critical and gapped correlation laws

Critical phase:

$$
\boxed{
\langle c_0^\dagger c_r\rangle
=\frac{\sin(\pi r/2)}{\pi r},
}
$$

$$
\boxed{
C_x(r)=A_xr^{-1/2}[1+O(r^{-2})],
\qquad A_x\approx0.58835,
}
$$

$$
\boxed{
I_0(r)=\frac{A_x^2}{\ln2}\frac1r+O(r^{-2})
\approx\frac{0.50}{r}\ \text{bit}.
}
$$

Controlled staggered-volume deformation:

$$
\boxed{
H_m=H_0+m\sum_j(-1)^jZ_j.
}
$$

В исходном intertwiner basis это staggered oriented-volume bias.

Two-band spectrum:

$$
\boxed{
E_\pm(k)=\pm\sqrt{(2m)^2+9\cos^2k}.
}
$$

Gap:

$$
\boxed{\Delta_{\rm sp}=2|m|.}
$$

Correlation length:

$$
\boxed{
\xi^{-1}=\operatorname{arsinh}\left(\frac{2|m|}{3}\right).
}
$$

Gapped asymptotics:

$$
\boxed{
C_x^{(m)}(r)\sim A(m)r^{-1/2}e^{-r/\xi},
}
$$

$$
\boxed{
I_m(r)\sim B(m)r^{-1}e^{-2r/\xi}.
}
$$

Файлы:

- `BQG_MUTUAL_INFORMATION_ASYMPTOTIC_RESULT.md`
- `scripts/bqg_mutual_information_asymptotic_gate.py`
- `BQG_GAPPED_DEFORMATION_DISTANCE_NOGO.md`
- `scripts/bqg_gapped_distance_nogo_gate.py`

---

# 7. Scalar-distance no-go

Critical phase требует для linear distance

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

Long-range pair mutual information остаётся physical observable, но не является универсальной spatial coordinate.

---

# 8. Local information conductance and additive metric

После scalar-distance no-go geometry строится локально.

Для edge $e=(ij)$ вводим relative twist generator

$$
\boxed{K_e=\frac{Z_i-Z_j}{2}.}
$$

Relative-twist quantum Fisher conductance:

$$
\boxed{
g_e^{\rm QFI}=\frac14F_Q(\rho_e,K_e).}
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
\boxed{
\ell_e=\ell_*\frac{g_*}{g_e}.
}
$$

Network distance:

$$
\boxed{
d(i,j)=\min_{\gamma:i\to j}\sum_{e\in\gamma}\ell_e.}
$$

На chain/tree additivity along geodesics exact.

Один и тот же local QFI rule применим и к critical, и к gapped phase. Quantum phase меняет local length scale, но не composition law.

Файлы:

- `BQG_LOCAL_INFORMATION_RESISTANCE_METRIC.md`
- `scripts/bqg_local_information_resistance_gate.py`

---

# 9. Новый exact result: QFI-weighted spectral dimension

Строим weighted graph Laplacian

$$
\boxed{
(L_g)_{ij}
=\delta_{ij}\sum_k g_{ik}-g_{ij}.
}
$$

Heat kernel:

$$
\boxed{K(\tau)=e^{-\tau L_g}.}
$$

Return probability:

$$
\boxed{
P(\tau)=\frac1N\operatorname{Tr}e^{-\tau L_g}.
}
$$

Spectral dimension:

$$
\boxed{
d_s(\tau)
=-2\frac{d\ln P(\tau)}{d\ln\tau}.
}
$$

Для бесконечной homogeneous $D$-dimensional hypercubic graph с одинаковым QFI conductance $g$ на всех nearest-neighbor edges

$$
\lambda(\mathbf k)
=2g\sum_{a=1}^D(1-\cos k_a).
$$

Return probability факторизуется exact:

$$
\boxed{
P_D(\tau)
=\left[e^{-2g\tau}I_0(2g\tau)\right]^D.
}
$$

Отсюда exact running dimension:

$$
\boxed{
d_s^{(D)}(\tau)
=4Dg\tau
\left[
1-\frac{I_1(2g\tau)}{I_0(2g\tau)}
\right].
}
$$

При $\tau\to\infty$:

$$
\boxed{
d_s^{(D)}(\tau)
=D+O((g\tau)^{-1}).
}
$$

Следовательно

$$
\boxed{
\lim_{\tau\to\infty}d_s^{(D)}(\tau)=D.
}
$$

Это первый exact dimension-calibration theorem текущей emergence branch.

---

# 10. Phase robustness of dimension

Вводим dimensionless diffusion time

$$
\boxed{u=g\tau.}
$$

Тогда

$$
\boxed{
d_s^{(D)}(u)
=4Du\left[1-\frac{I_1(2u)}{I_0(2u)}\right],
}
$$

и conductance $g$ полностью исчезает.

Поэтому critical и gapped homogeneous phases на одной topology имеют **одну и ту же running spectral-dimension curve**, различаясь только физическим diffusion timescale.

Контрольные значения:

при $u=10$

$$
d_s^{(1)}\approx1.01318,
\qquad
d_s^{(2)}\approx2.02636,
\qquad
d_s^{(3)}\approx3.03954,
$$

а при $u=100$

$$
\boxed{
d_s^{(1)}\approx1.001256,
\quad
d_s^{(2)}\approx2.002513,
\quad
d_s^{(3)}\approx3.003769.
}
$$

То есть один и тот же local QFI rule без retuning корректно калибрует 1D, 2D и 3D regular lattices.

Файлы:

- `BQG_QFI_SPECTRAL_DIMENSION_RESULT.md`
- `scripts/bqg_qfi_spectral_dimension_gate.py`

---

# 11. Branching topology discriminator

Для infinite 3-regular Bethe lattice

$$
\boxed{\lambda_0=3-2\sqrt2>0.}
$$

Long-time return probability имеет вид

$$
P_{\rm Bethe}(\tau)
\sim A\tau^{-3/2}e^{-g\lambda_0\tau}.
$$

Следовательно

$$
\boxed{
d_s^{\rm Bethe}(\tau)
=2g\lambda_0\tau+3+o(1).
}
$$

И поэтому

$$
\boxed{
d_s^{\rm Bethe}(\tau)\to\infty.}
$$

Регулярное exponential branching не маскируется под конечномерную Euclidean geometry.

Это важный контроль: QFI-weighted diffusion различает manifold-like lattices и non-amenable branching topology.

---

# 12. Что теперь доказано в reduced emergence branch

Самые сильные current statements:

1. $Q=i[D_{12},D_{23}]$;
2. $Q_{\rm phys}=(\sqrt3/4)\sigma_y$;
3. local isotropy iff oriented volume is sharp;
4. $\mathcal A_p=4(\Delta Q)^2$;
5. two-node matching selects Bell-type intertwiner entanglement;
6. current many-node chain maps exactly to free fermions;
7. critical $I_0(r)\sim\kappa/r$;
8. staggered oriented-volume deformation opens exact gap $2|m|$;
9. gapped $I_m(r)\sim Br^{-1}e^{-2r/\xi}$;
10. no universal global scalar distance $d=f(I_{ij})$ works in both phases;
11. local relative-twist QFI defines a phase-robust conductance rule;
12. resistance composition gives an additive network metric;
13. homogeneous QFI-weighted hypercubic graphs satisfy $d_s\to D$ exactly;
14. critical/gapped change of $g$ rescales diffusion time but not dimension;
15. Bethe branching has no finite IR spectral-dimension plateau.

Короткая current chain:

$$
\boxed{
\text{binary SU(2) data}
\to
\text{oriented quantum volume}
\to
\text{entangled gluing}
\to
\text{local QFI conductance}
\to
\text{resistance metric}
\to
\text{weighted Laplacian}
\to
\text{spectral dimension}.
}
$$

---

# 13. Что пока НЕ доказано

Мы не утверждаем, что:

- $H_{\rm glue}$ уже выведен из fundamental graph-changing BQG constraint;
- relative-twist QFI является unique fundamental metric source;
- $K_{ij}$ уже выведен из full physical projector/history dynamics;
- reference length $\ell_*$ выведена из binary microphysics;
- **пространство автоматически становится 3D**;
- cubic/hypercubic connectivity уже выведена из BQG;
- irregular/dynamical BQG graph уже показал flow к $d_s=3$;
- Lorentzian causal cone уже выведен;
- Einstein equations уже получены;
- $G$, $c$, $\hbar$ уже выведены из first principles.

Главный caveat текущего dimension result:

$$
\boxed{
\text{we calibrated dimension on supplied topology}
\neq
\text{we derived 3D topology from binary dynamics}.
}
$$

---

# 14. Новый настоящий фронтир: убрать topology-by-hand loophole

Следующий шаг больше не должен брать заранее готовую chain/square/cubic lattice.

Нужно построить family irregular/dynamical graphs непосредственно из BQG gluing/state data и проверить, возникает ли стабильный IR plateau

$$
\boxed{d_s(\tau)\approx\text{const}.}
$$

Главный falsification target:

$$
\boxed{
\textbf{dynamical / irregular QFI-weighted BQG graph}
\to
P(\tau)
\to
d_s(\tau)
\to
\textbf{test for an emergent dimension plateau}.
}
$$

Особенно сильный результат был бы

$$
\boxed{d_s^{IR}\to3}
$$

без hard-coded cubic connectivity и без fit dimension by hand.

Практический следующий gate:

1. генерировать irregular graphs из local gluing compatibility;
2. задавать edge weights только через local QFI rule;
3. не использовать coordinate labels;
4. вычислять heat-kernel spectrum;
5. искать plateau $d_s(\tau)$;
6. проверить robustness к critical/gapped local state;
7. сравнить с randomized/null graph ensembles;
8. только после этого переходить к causal propagation.

---

# 15. Канонический принцип

> **Сначала уменьшить задачу симметрией. Затем распознать точную математическую структуру. Потом решить её аналитически. Отрицательные результаты фиксировать так же строго, как положительные. И только если exact путь закрыт — считать численно.**

Репозиторий: `Shtenco/binary_quantum_theory`
