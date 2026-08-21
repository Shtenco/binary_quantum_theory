# От бита к пространству, гравитации, свету и реальному эксперименту

## Научная сказка для взрослых учёных детей — в которой формулы важнее чудес, а у природы всегда есть право сказать «нет»

> **Канонический статус: 21 августа 2026. Candidate theory.**
>
> Этот репозиторий не объявляет «теорию всего» доказанной. Он строит длинную вычислимую цепочку от бинарной различимости до трёхмерной PL-геометрии, 3+1-like history, SU(2)/Peter–Weyl quantum geometry, compact U(1) phase, spin-2, HDA/GR, physical projector, 1PI effective action и реальных observables.
>
> Главный принцип: **красивое совпадение не становится физическим предсказанием, пока между объектами не построен явный мост.** Поэтому здесь сохраняются positive results, negative controls, no-go theorems, исправления прежних интерпретаций и открытые bottlenecks.

### Как читать репозиторий

- **README.md** — путешествие от бита к физике.
- **CANONICAL_THEORY_PACKAGE.md** — сухой evidence index.
- **THEORY_STATUS.md** — human-readable status ledger.
- **theory_gates.json** и physicalization ledgers — machine-readable truth surface.
- **PREDICTIONS_AND_EXPERIMENTAL_TESTS.md** — внешний слой проверок.
- [Исходная сказка 17 августа 2026](docs/archive/README_STORY_2026-08-17.md) сохранена как отдельный исторический snapshot.

### Ярлыки доказательности

- **EXACT** — алгебраический/комбинаторный результат в заявленных предпосылках.
- **CI / FINITE PASS** — воспроизводимый конечномерный computation.
- **HELD-OUT** — prediction была frozen до открытия проверочного результата.
- **CONDITIONAL** — вывод зависит от явно записанной дополнительной физической гипотезы.
- **OPEN PHYSICAL** — математический объект определён, но physical bridge или microscopic number ещё не получен.
- **NO-GO** — доказано, что привлекательный shortcut не работает.

---

# Пролог. Вселенная, у которой сначала нет координат

Представьте, что нам запрещено начинать с `x,y,z`.

Нет метров.

Нет решётки.

Нет заранее выбранной размерности.

Нет света.

Нет частиц.

Нет даже обещания, что continuum появится.

Есть только различимость: локальное событие может различать несколько независимых бинарных альтернатив.

Из этого вопроса проект пытается пройти всю дорогу:

```text
binary distinction
 -> q=2
 -> octahedral S2 local link
 -> canonical recursive PL S3 phase
 -> exact causal-volume fixed point d*=3
 -> z ~ 1
 -> 3+1-like history
 -> quantum geometric tensor
      Re Q -> distinguishability / geometry
      Im Q -> Berry / Hopf phase
 -> SU(2) quantum geometry + compact U(1) phase
 -> collective spin-2 carrier
 -> logical shape -> metric
 -> five traceless metric modes E + T2
 -> Peter-Weyl constraint dynamics
 -> Lorentzian completion + HDA/ADM
 -> finite master-constraint projector
 -> relational / geometric boundary time
 -> physical history generating functional
 -> 1PI effective action Gamma[g,A,...]
 -> TT and Maxwell physical kernels
 -> S4 -> SO(3) -> Lorentz universality ladder
 -> G, Lambda, Z_A
 -> pole observables + connected fluctuations
 -> blind experiment.
```

У истории есть важная особенность: несколько раз она сама запрещает нам слишком лёгкий финал. Именно это делает её научной.

---

# Глава 1. Бит обнаруживает, что его должно быть два

**[EXACT]**

Пусть локальная cell содержит `q` независимых бинарных различий. Число route states равно

\[
2^q.
\]

Route vertex имеет `q` Hamming-neighbours и два causal poles, значит естественная степень равна

\[
q+2.
\]

Локальная однородность требует

\[
q+2=2^q.
\]

Для целых `q>=1` единственное решение

\[
\boxed{q=2}.
\]

Получаются четыре labels

```text
00  01  10  11
```

с Hamming adjacency `C4`. Первое число возникает не как fitted parameter, а как решение equation.

---

# Глава 2. Четыре маршрута строят сферу вокруг точки

**[EXACT]**

Добавление двух causal poles к `C4` даёт octahedral shell

```text
V=6, E=12, F=8, chi=2
```

и потому simplicial

\[
\boxed{S^2}.
\]

У внутренней вершины обычного combinatorial 3-manifold link должен быть `S2`:

\[
\boxed{\text{binary homogeneity}\to q=2\to S^2\text{ vertex link}}.
\]

Но локальная sphere ещё не является глобальным пространством.

---

# Глава 3. Локальные сферы образуют глобальное пространство

**[EXACT / FINITE PL]**

Canonical minimal+flag globalization — boundary 4D cross-polytope, 16-cell:

```text
(V,E,F,T)=(8,24,32,16)
Betti=(1,0,0,1)
```

Vertex links — `S2`, edge links — `S1`, triangle links — `S0`; complex orientable, every triangle two-sided, `boundary^2=0`.

Следовательно в canonical completion

\[
\boxed{M^3\cong S^3}.
\]

Barycentric refinement:

```text
16 -> 384 -> 9216 tetrahedra
```

с сохранением manifold conditions на проверенных уровнях.

**Граница:** это exact existence/stability result для canonical PL completion, не theorem уникальности любого возможного nonflag gluing.

---

# Глава 4. Лестница размерности заканчивается на тройке

При `q=2`, `B=2^q=4`, каждый active causal edge создаёт `2B=8` children, а causal scale удваивается.

Exact count:

\[
\boxed{N_g=\frac{4\,8^g+10}{7}}.
\]

One-step exponent:

\[
d_g=\log_2\frac{N_g}{N_{g-1}}
=3+\log_2\left(1-\frac{35}{16\,8^{g-1}+40}\right).
\]

Поэтому

\[
d_g<3,\qquad d_{g+1}>d_g,\qquad \boxed{d_g\nearrow3}.
\]

И

\[
\boxed{d_*^{causal-volume}=3}.
\]

Frozen `d_H=2.999229782139151` — finite point этой exact sequence, а не случайное попадание около тройки.

---

# Глава 5. Одного числа «3» недостаточно

Независимые свидетели:

\[
D_{topo}=3,\qquad d_{causal-volume}\to3,
\]

и frozen dynamics

\[
\boxed{d_H=2.999229782139151},\qquad \boxed{z\simeq0.998281156}.
\]

Исторический `ds_slice_holdout` уже содержит division by `z`:

\[
\boxed{d_{eff}^{slice}=\frac{d_H}{z}=3.004393867}.
\]

Его нельзя делить на `z` второй раз.

Для one-causal-time history:

\[
\boxed{d_{eff}^{history}=1+\frac{d_H}{z}\simeq4.004393867}.
\]

```text
local topology       -> 3
causal-volume growth -> 3
z                    -> 1
history              -> 3+1-like scaling
```

---

# Глава 6. Дискретное пространство учится выглядеть гладким

**[CI / COARSE-GRAINING]**

```text
delta g       ~ b^-2.001707
grad(delta g) ~ b^-3.001458
delta R       ~ b^-4.000524
```

Это reconstruction defects, не vacuum spectrum.

Прежняя интерпретация `delta g ~ b^-2 -> P(k)~k^+1` была отвергнута. Прямой reduced TT calculation дал

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

Falsified interpretation сохраняется как negative control.

---

# Глава 7. Qubit одновременно открывает геометрию и фазу

Нормированный state живёт на `S3` в `C2`; ray quotient даёт `CP1~S2`, а Hopf fibration

\[
\boxed{U(1)\to S^3\to S^2}.
\]

Обе ветви сидят в quantum geometric tensor

\[
Q_{ab}=\langle\partial_a\psi|(1-|\psi\rangle\langle\psi|)|\partial_b\psi\rangle.
\]

Для Bloch spinor:

\[
\boxed{ds^2_{FS}=\frac14(d\theta^2+\sin^2\theta\,d\phi^2)},
\]

\[
\boxed{F=\frac12\sin\theta\,d\theta\wedge d\phi}.
\]

То есть

\[
\boxed{
q=2\text{ ray}\Rightarrow
\begin{cases}
\Re Q:&\text{ distinguishability / geometry},\\
\Im Q:&\text{ Berry/Hopf phase / }U(1).
\end{cases}}
\]

---

# Глава 8. Четыре spin-1/2 содержат один collective spin-2

**[EXACT REPRESENTATION THEORY]**

\[
(1/2)^4=2\times j=0+3\times j=1+1\times j=2.
\]

Unique `j=2` carrier существует; TT reduction оставляет две helicity. Это не «четыре qubits и есть гравитон», а existence theorem для spin-2 carrier, который ещё должен пройти geometric и dynamical bridges.

---

# Глава 9. Logical shape превращается в metric

**[EXACT]**

В logical singlet sector `X,Z` — intrinsic shape, `Y` — orientation pseudoscalar.

Для regular tetrahedron

\[
g_0=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}.
\]

Exact tangents `M_X,M_Z`:

\[
\operatorname{Tr}(g_0^{-1}M_A)=0,
\]

\[
\boxed{\operatorname{Tr}(g_0^{-1}M_Ag_0^{-1}M_B)=\frac32\delta_{AB}}.
\]

Значит shape doublet map’ится в orthogonal equal-norm trace-free metric tangents.

---

# Глава 10. Пять metric modes и 8.43%

**[FINITE PASS + EXACT S4 REDUCTION]**

\[
\boxed{6=A_1\oplus E\oplus T_2}.
\]

First refined q4 kernel:

\[
\lambda_E=1.1111917875584736,\qquad
\lambda_{T_2}=1.0220278507464782,
\]

\[
\Delta_{ET}=0.08916393681199541,
\]

\[
\kappa_5=\frac{2\lambda_E+3\lambda_{T_2}}5=1.0576934254712764.
\]

Отсюда

\[
\boxed{\Delta_{ET}/\kappa_5=0.08430036026012608}.
\]

Это **local Euclidean tetrahedral spin-2 anisotropy precursor**, не physical `zeta4`, не speed anisotropy и не mass ratio.

---

# Глава 11. Почему 8.43% нельзя превратить в particle masses

**[EXACT NO-GO]**

На traceless metric space `5=E+T2`. Для

\[
Q_{tet}=\frac35P_E-\frac25P_{T_2}
\]

имеем

\[
Q_{tet}|_{T_2}=-\frac25I_3.
\]

Если generations образуют irreducible `T2`, любой `S4`-invariant mass operator по Schur lemma

\[
\boxed{M=mI_3}.
\]

Значит `8.43% -> e/mu/tau hierarchy` невозможно без independently derived flavor symmetry breaking и Yukawa map.

---

# Глава 12. Peter–Weyl идёт на следующий shell

**[FINITE PASS]**

Spin parity: `P H_E P=0`.

\[
K=PH_E^2P,
\]

\[
\boxed{\Lambda=K^{-1/2}(PH_E^4P-K^2)K^{-1/2}}.
\]

32D result:

```text
rank(K)=32
lambda_min=10.635759878291307
lambda_max=15.059927665966466
mean=12.860443113390883
distance from scalar identity=0.09440461833276048
```

Это finite **constraint spectral data**, не physical frequencies и не masses.

---

# Глава 13. Geometry-only blocking не создаёт hidden RG flow

**[EXACT CONTROL]**

\[
\boxed{P^TL_{g+1}P=\frac14L_g}.
\]

Для separable geometry/internal kernel все internal couplings получают один factor, normalized anisotropy не течёт. Genuine flow обязан идти из Peter–Weyl recoupling, nonseparable blocking, interblock transport и history dynamics.

---

# Глава 14. Euclidean Hamiltonian получает Lorentzian половину

\[
A_a^i=\Gamma_a^i+\beta K_a^i,
\]

\[
H_E^{kin}=-\beta^2Q_{DW},\qquad
H_L^{corr}=(1+\beta^2)Q_{DW},
\]

поэтому

\[
\boxed{H_E^{kin}+H_L^{corr}=Q_{DW}}.
\]

Exact classical consistency control; quantum beta-independence этим не доказана.

---

# Глава 15. Hamiltonian constraints учатся двигать пространство

Target:

\[
[\hat H[N],\hat H[M]]\to i\hbar\hat D[\sharp(NdM-MdN)].
\]

Frozen route-normal generator строится независимо. Fixed-cutoff asymptotics:

```text
C_cross / D = O(epsilon)
C_GG    / D = O(epsilon^2)
```

с conservative family

\[
J_{max}=o(\epsilon^{-2/13}).
\]

В ADM ansatz closure выбирает

\[
\boxed{c=1/2},\qquad \boxed{AB=1}.
\]

HDA не выводит numerical `G`; cosmological term cancels из bracket.

---

# Глава 16. Plebanski и Regge независимо идут к Einstein structure

```text
B-field -> simplicity -> Urbantke metric -> connection -> curvature
```

и

```text
metric -> Regge Hessian -> Fierz-Pauli -> EH/Ward controls
```

дают независимые downstream checks.

Regge held-out rule

\[
Z_L=\frac18+\frac{C}{L^2}+\frac{D}{L^4}
\]

предсказал

```text
Z6_pred=0.11876923193907167
Z6_obs =0.11876075461190198
relative error ~0.00714%
```

Это internal held-out control, не external experimental confirmation.

---

# Глава 17. Первый reduced TT propagator

**[EXACT REDUCED CONTROL]**

\[
\boxed{
G^{TT}_{AB}(\omega,\mathbf k)=
\frac{\delta_{AB}}
{Z_T[4\sin^2(\omega/2)-\frac13\sum_i4\sin^2(k_i/2)+i0]}}
\]

имеет massless pole в reduced model.

Bare controls:

\[
\boxed{\eta_{2,bare}=-1/45},\qquad
\boxed{\zeta_{4,bare}=-1/12}.
\]

И

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

Это regulator positive control, не final interacting physical prediction.

---

# Глава 18. Почему `R_aniso -> zeta4` было неправильной стрелкой

\[
R_{aniso}\simeq0.08975326618
\]

— internal Peter–Weyl diagnostic. Он не physical spatial dispersion coefficient.

Легальная chain:

\[
\boxed{\Gamma_{shape}\to M\to\Gamma_{metric}\to K_{TT}\to\text{physical poles}}.
\]

---

# Глава 19. Onsite kernel сжимается до трёх numbers — только onsite

**[EXACT S4, k=0]**

\[
\boxed{C_6^{(0)}=a_0I+b_0A_{adj}+c_0O_{opp}}.
\]

\[
\lambda_{A_1}=a_0+4b_0+c_0,
\]

\[
\lambda_E=a_0-2b_0+c_0,\qquad
\lambda_{T_2}=a_0-c_0.
\]

Это правильная onsite symmetry compression. Generic directed momentum требует большего space.

---

# Глава 20. Momentum сам несёт representation

\[
\boxed{C_6(\omega,g\mathbf k)=U_gC_6(\omega,\mathbf k)U_g^{-1}}.
\]

До TT quotient representation count даёт 13 quartic `S4` singlets. После

\[
\operatorname{tr}h=0,\qquad h_{ij}k_j=0
\]

exact polynomial quotient:

\[
\boxed{\dim\mathcal W^{(4)}_{TT,S_4}=6}.
\]

---

# Глава 21. Шесть Wilson coefficients и frozen extractor

Один complete basis:

\[
W_1=\mathcal R[h_{xx}^2k_z^4],\quad
W_2=\mathcal R[h_{xx}^2k_x^4],
\]

\[
W_3=\mathcal R[h_{xy}^2k_z^4],\quad
W_4=\mathcal R[h_{xy}^2k_y^4],
\]

\[
W_5=\mathcal R[h_{xx}^2k_y^2k_z^2],\quad
W_6=\mathcal R[h_{xx}^2k_x^2k_z^2].
\]

\[
\boxed{\delta K_{TT}^{(4)}=Z_Tc_T^2a_*^2\sum_{r=1}^6c_rW_r}.
\]

`100/110/111` дают rank 5; preregistered `120` закрывает rank 6.

\[
\boxed{\det A=1/699840000\neq0}.
\]

`A^{-1}` frozen до microscopic data.

---

# Глава 22. Momentum рождается из interblock transport

Face-sharing stabilizer — `S3`.

\[
6=(A_1\oplus E)_{apex}\oplus(A_1\oplus E)_{face}.
\]

Reciprocal transfer для canonical shared face задаётся шестью real functions.

Regular tetrahedral moments:

\[
\sum_an_a^in_a^j=\frac43\delta^{ij},
\]

\[
\boxed{\sum_a(\mathbf k\cdot\mathbf n_a)^4=\frac45(k^2)^2-\frac89Q_4^{cub}(\mathbf k)}.
\]

Поэтому leading `k^2` может быть isotropic, а tetrahedral memory появляться на quartic order.

---

# Глава 23. eta2 и zeta4 — nested hypothesis

\[
\bar e_4(\hat n)=\eta_2+\zeta_4Q_4^{cub}(\hat n)
\]

— двумерная subspace полного six-dimensional result.

Если six-vector туда попадает:

\[
\zeta_4=2(e_{100}-e_{110}),
\]

\[
\eta_2=\frac{e_{100}+4e_{110}}5,
\]

и held-out condition

\[
\boxed{e_{100}-4e_{110}+3e_{111}=0}.
\]

---

# Глава 24. Tetrahedral polarization fingerprint

Single-`Q_tet` nested model:

\[
(100):\{3/5,-2/5\},
\]

\[
(110):\{7/20,-2/5\},
\]

\[
(111):\{-1/15,-1/15\}.
\]

Следовательно

\[
\boxed{\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0}.
\]

Это zero-fit fingerprint только после того, как full six-vector сам выберет эту submodel.

---

# Глава 25. On-shell Wilson space переживает field redefinitions

Leading kernel:

\[
K_0=Z_T(-\omega^2+c_T^2k^2)I_{TT}.
\]

Local redefinition `h -> (I+a_*^2R_2)h` добавляет quartic terms, пропорциональные `K_0`. На massless leading pole `K_0=0`, поэтому они исчезают.

Значит six-dimensional quotient — space genuine on-shell quartic pole observables, хотя off-shell action может иметь больше coefficients.

---

# Глава 26. Constraint spectrum — ещё не physical time propagator

Это главный conceptual correction.

Peter–Weyl `H[N]` — Hamiltonian **constraint**. Поэтому

\[
(z-\hat H)^{-1}
\]

нельзя автоматически назвать

\[
G(\omega,\mathbf k).
\]

Constraint spectral `z` не physical `omega`.

Легальная chain:

\[
\boxed{
\hat H[N]
\to\mathcal P_{phys}
\to Z[J_g]
\to W[J_g]
\to\Gamma[g]
\to\Gamma^{(2)}_{metric}
\to K_{TT}(\omega,\mathbf k)}.
\]

Finite Peter–Weyl `K/A/B/Lambda` остаются важными constraint-dynamics data, но не переименовываются в physical graviton self-energy.

---

# Глава 27. Physical projector перестал быть словом

**[EXACT FINITE + CI PASS]**

Для constraints `C_A` и positive-definite `G^{AB}`:

\[
\boxed{\mathbb M_G=C_A^\dagger G^{AB}C_B}.
\]

Тогда

\[
\boxed{\ker\mathbb M_G=\bigcap_A\ker C_A}.
\]

Physical projector:

\[
\boxed{P_0=\chi_{\{0\}}(\mathbb M_G)}.
\]

Finite CI control:

\[
\max_A\|C_AP_0\|\simeq1.35\times10^{-15},
\]

\[
\max_{G_i,G_j}\|P_0(G_i)-P_0(G_j)\|\simeq2.82\times10^{-15}.
\]

И

\[
\|e^{-T\mathbb M}-P_0\|=e^{-T\Delta_M}
\]

совпадает с spectral prediction на machine precision.

Открыт refinement/rigging limit:

\[
\boxed{\delta_P(g)=\frac{\|P_{g+1}I_g-I_gP_g\|}{\|I_gP_g\|}\to0}.
\]

---

# Глава 28. Время появляется после physical conditioning

Minimal constrained control:

\[
C=P_T+H_s.
\]

После projection и relational conditioning:

\[
\boxed{2\langle T_{out}|P_{phys}|T_{in}\rangle=e^{-iH_s(T_{out}-T_{in})}}.
\]

Physical time появляется через boundary/relational conditioning, а не переименование constraint eigenvalue.

Для gravity естественный candidate — boundary proper separation `tau`, определяемый semiclassical geometry/extrinsic curvature; `omega` then conjugate to physical `tau`.

---

# Глава 29. Настоящая физика живёт в 1PI action

После physical projector/history measure нужны

\[
Z[J_g,J_A,\ldots]
\]

и

\[
\Gamma[g,A,\ldots].
\]

Physical quadratic kernels:

\[
K_g=\frac{\delta^2\Gamma}{\delta h_{TT}\delta h_{TT}},\qquad
K_A=\frac{\delta^2\Gamma}{\delta A_T\delta A_T}.
\]

Только здесь разрешено говорить о physical poles, residues, propagation и phase.

---

# Глава 30. Шесть coefficients могут законно исчезнуть

Для isotropic coefficient vector

\[
v_{iso}=(6,24,6,36,-9,18)^T
\]

frozen extractor даёт

\[
\boxed{Av_{iso}=(1,1,1,1,1,1)^T}.
\]

Поэтому observable ladder:

\[
\boxed{S_4:\ y\in\mathbb R^6},
\]

\[
\boxed{SO(3):\ y_1=\cdots=y_6},
\]

\[
\boxed{\text{Lorentz metric-only massless vacuum}:\ y_1=\cdots=y_6=0}.
\]

То есть

\[
\boxed{6\to1\to0}.
\]

Пять contrasts тестируют spatial isotropy; шестая common amplitude — surviving preferred-foliation quartic shift.

---

# Глава 31. Lorentz-invariant metric-only vacuum защищает massless cone

Если vacuum Lorentz invariant, diffeomorphism unbroken и low-energy helicity-2 field — metric graviton:

\[
\boxed{K_{TT}(s)=P_{TT}\,sF(a_*^2s)},\qquad s=-\omega^2+c^2k^2.
\]

Massless root

\[
\boxed{s=0}
\]

не сдвигается local analytic higher derivatives. Они могут менять off-shell form factor или добавлять heavy roots `F=0`, но не обязаны давать `k^4,k^6,...` shift исходному massless graviton.

Значит Planck-suppressed vacuum dispersion **не является обязательной сигнатурой quantum gravity**.

---

# Глава 32. Physical tetrahedral order имеет свой tensor

\[
S_{ijkl}=\sum_{a=1}^4n_{ai}n_{aj}n_{ak}n_{al},
\]

\[
\boxed{T^{(4)}_{ijkl}=S_{ijkl}-\frac45\delta_{(ij}\delta_{kl)}}.
\]

Он trace-free:

\[
T^{(4)}_{iikl}=0,
\]

с

\[
\|T^{(4)}\|^2=\frac{128}{135},
\]

и

\[
\boxed{T^{(4)}_{ijkl}k_ik_jk_kk_l=-\frac89Q_4^{cub}(\mathbf k)}.
\]

Если anisotropic pole выживает, тот же physical order parameter должен существовать в state/history/EFT. Иначе это regulator contamination.

---

# Глава 33. Свет: compact U(1) получает canonical dynamics

На seed `S3` complex:

```text
V=8, E=24, F=32, T=16
rank d0=7
rank d1=17
d1 d0=0
b1=0
```

Если blocked phase sector даёт positive local quadratic action

\[
L_A=\frac{Z_A}{2}(\dot\theta-d_0A_0)^TM_1(\dot\theta-d_0A_0)
-\frac{Z_A}{2}(d_1\theta)^TM_2(d_1\theta),
\]

то

\[
p=Z_AM_1(\dot\theta-d_0A_0)
\]

и variation по `A_0` даёт

\[
\boxed{d_0^Tp=0}.
\]

Transverse dynamics:

\[
\boxed{\ddot\theta=-M_1^{-1}d_1^TM_2d_1\theta}.
\]

`Z_A` сокращается из linear dispersion: coupling normalization и light speed — разные quantities.

---

# Глава 34. Hopf topology не может одна выдать 137

Compactness фиксирует phase period и integer charge lattice. Но family

\[
\Gamma_A[Z_A]= -\frac{Z_A}{4}\int F^2,\qquad Z_A>0
\]

имеет ту же gauge symmetry, compactness, Chern class и massless cone для любого `Z_A`.

Поэтому

\[
\boxed{\text{Hopf topology + gauge symmetry + Maxwell form}\not\Rightarrow\alpha}.
\]

В unit-charge convention

\[
\boxed{\alpha=\frac1{4\pi Z_A}}.
\]

Число требует microscopic phase-history/RG calculation `Z_A`. Случайный Peter–Weyl eigenvalue нельзя переименовать в `137`.

---

# Глава 35. Почему 3+1 важно для compact U(1)

Независимо получены

\[
q=2\to d_{space}=3
\]

и

\[
q=2\to U(1)_{compact}.
\]

Вместе:

\[
\boxed{3+1\text{ dimensional compact }U(1)}.
\]

Эта dimensionality допускает deconfined/Coulomb phase. Это compatibility statement, а не proof того, что microscopic `Z_A` уже в deconfined basin.

---

# Глава 36. Гравитация и свет могут иметь один principal cone

Если physical IR action приходит к одной emergent metric:

\[
\Gamma_{IR}[g,A]=\int\sqrt{-g}\left[\frac{R-2\Lambda}{16\pi G}-\frac{Z_A}{4}F^2\right]+\cdots,
\]

то leading scalar

\[
s=g^{\mu\nu}k_\mu k_\nu
\]

общий. В Lorentz-invariant vacuum

\[
K_g=sF_g(s),\qquad K_\gamma=sF_\gamma(s),
\]

поэтому исходные photon и graviton имеют

\[
\boxed{s=0}.
\]

`G`, `Z_A` и `alpha` не используются как ручки для подгонки скорости.

Conditional massless spin-2 consistency ведёт к universal gravitational coupling, тогда как U(1) требует conservation/quantization charge, но не одинакового charge у всех species.

---

# Глава 37. G, Lambda и alpha — три разных microscopic questions

Они не извлекаются из одного красивого spectrum.

## Newton constant

После geometric normalization:

\[
\Gamma[g]\supset C_R\int\sqrt{-g}\,R,
\]

\[
\boxed{G=\frac1{16\pi C_R}}.
\]

## Cosmological constant

`Lambda` не выводится HDA bracket. Нужен physical saddle

\[
\boxed{\left.\frac{\delta\Gamma}{\delta g}\right|_{\bar g}=0}
\]

и curvature соответствующего vacuum solution.

## Fine-structure constant

\[
\boxed{\alpha=\frac1{4\pi Z_A}}.
\]

`G`, `Lambda`, `Z_A` — разные microscopic estimators.

---

# Глава 38. Zero dispersion не означает zero quantum geometry

Даже если

\[
\boxed{c_1=\cdots=c_6=0},
\]

connected metric covariance

\[
C_h(x,y)=\langle h(x)h(y)\rangle_c
\]

может быть nonzero.

Optical phase map

\[
\delta\phi=\frac{k\ell}{2}Jh
\]

даёт

\[
\boxed{C_\phi=\left(\frac{k\ell}{2}\right)^2JC_hJ^T}.
\]

Эксперимент разделяется на

```text
pole / dispersion test
connected fluctuation / interference test
```

и symmetry ratio

\[
\boxed{R_\gamma=2\frac{S_E}{S_{T_2}}\to1}
\]

в isotropic IR.

---

# Глава 39. S3 не запрещает fermions

`S3` parallelizable, поэтому

\[
w_2(S^3)=0.
\]

А

\[
H^1(S^3,\mathbb Z_2)=0,
\]

поэтому

\[
\boxed{\text{на }S^3\text{ существует ровно одна spin structure}}.
\]

Seed 16-cell over `Z2` даёт

\[
(b_0,b_1,b_2,b_3)=(1,0,0,1).
\]

Это topological prerequisite для spin-1/2 fields, но не derivation Standard Model, chirality, generations или Yukawa sector. Geometric `Spin(3)~SU(2)` нельзя автоматически называть electroweak `SU(2)`.

---

# Глава 40. Global S3 имеет cosmological falsifiers

Если physical continuum сохраняет closed `S3` spatial slices, FRW sign

\[
\boxed{k=+1}.
\]

Это не требует заметной curvature сегодня.

Scalar harmonics:

\[
\boxed{-\nabla^2Y_n=\frac{n(n+2)}{a^2}Y_n},\qquad n=0,1,2,\ldots
\]

с degeneracy `(n+1)^2`.

Это conditional global-topology test: history dynamics ещё должна показать, что microscopic canonical `S3` survives в cosmological continuum.

---

# Глава 41. Где тяжёлая микрофизика упирается сейчас

## j=1 representation RG

Canonical `j=1 S4[2,2]` carrier и master-projector preflight прошли finite gates. Exact ordered Peter–Weyl paths реально вычисляются, но часть paths превышает hosted-runner wall, поэтому full

\[
\Lambda(j=1)
\]

и

\[
R_{aniso}(j=1)
\]

ещё не frozen.

Следующая exact factorization:

\[
\boxed{H_sH_r=\sum_{\alpha,\beta}H_{s,\beta}H_{r,\alpha}}.
\]

Это computational sharding, не physics approximation.

## full-H_E L1 block

Active-cone backend — representation optimization. Reference-vs-local certificate упёрся в CI time wall до guard, поэтому 72 L1 production shards нельзя объявлять завершёнными. Нужно shard’ить сам equivalence certificate, сохраняя прежние tolerances.

---

# Глава 42. Truth table на сегодня

| Arrow / observable | Status |
|---|---|
| `q+2=2^q -> q=2` | **EXACT** |
| octahedral `S2` link | **EXACT** |
| canonical PL `S3` | **EXACT / FINITE STABILITY** |
| causal-volume `d*=3` | **EXACT** |
| `d_H/z≈3.00439`, history `≈4.00439` | **FROZEN / DERIVED** |
| quantum geometric tensor `ReQ/ImQ` | **EXACT KINEMATIC** |
| logical shape -> metric | **EXACT** |
| L1 `E/T2` split 8.43% | **FINITE PASS** |
| `8.43% -> particle masses` | **NO-GO** |
| 32D higher-shell constraint `Lambda` | **FINITE PASS** |
| geometry-only anisotropy flow | **NO-FLOW CONTROL** |
| HDA/ADM declared closure | **STRUCTURAL PASS** |
| Regge held-out `Z6` | **HELD-OUT PASS** |
| reduced massless TT propagator | **EXACT REDUCED CONTROL** |
| generic quartic TT `S4` dimension = 6 | **EXACT** |
| six-observable extractor | **EXACT** |
| on-shell field-redefinition invariance | **EXACT** |
| finite master projector | **EXACT + CI PASS** |
| constraint `z` = physical `omega` | **REJECTED SHORTCUT** |
| `6 -> 1 -> 0` ladder | **EXACT / CONDITIONAL IR** |
| compact Hopf U(1) carrier | **EXACT KINEMATIC** |
| Maxwell form from positive phase action | **CONDITIONAL THEOREM** |
| `Hopf topology -> alpha` | **NO-GO** |
| unique spin structure on `S3` | **EXACT TOPOLOGICAL** |
| physical projector continuum/rigging limit | **OPEN PHYSICAL** |
| microscopic physical `Gamma[g,A]` | **OPEN PHYSICAL** |
| frozen physical six-vector | **OPEN PHYSICAL** |
| microscopic `G`, `Lambda`, `Z_A` | **OPEN PHYSICAL** |
| realistic gauge/chiral/Yukawa matter | **OPEN** |
| experimental confirmation | **OPEN / DATA** |

---

# Четыре дракона, которых нельзя обмануть

### Dragon I — constraint is not time

Нельзя переименовать spectral variable constraint в physical frequency. Сначала projector/history, затем `Gamma`, затем pole.

### Dragon II — regulator is not nature

Если tetrahedral anisotropy не сопровождается physical order parameter или не stabilizes under refinement, она regulator memory.

### Dragon III — common scale is common

Нельзя отдельно калибровать directions, polarizations, events и sectors. Один derived scale или один заранее объявленный calibration datum.

### Dragon IV — blind data

После freeze нельзя менять basis, удалять неудобный coefficient или выбирать submodel потому, что posterior красивее.

У природы всегда должно оставаться право сказать `FAIL`.

---

# Воспроизводимые gates

```bash
python scripts/verify_theory_gates.py
python bcqg_bit_to_gravity_final.py --strict
python scripts/q2_dimension3_fixed_point_gate.py --max-generation 10
python scripts/logical_shape_metric_jacobian_gate.py
python scripts/peter_weyl_j1_s4_block_gate.py
python scripts/tt_propagator_first_pass.py
python scripts/tt_vacuum_two_point_gate.py
python scripts/s4_tt_quartic_complete_basis_gate.py
python scripts/s4_tt_six_wilson_predictor.py --selftest
python scripts/nearest_block_s3_transfer_gate.py
python scripts/c6_tt_wilson_extractor.py
python scripts/tetrahedral_tt_birefringence_gate.py
```

---

# Канонические входы

| Layer | Entry point |
|---|---|
| Full evidence index | `CANONICAL_THEORY_PACKAGE.md` |
| Human status | `THEORY_STATUS.md` |
| Machine ledger | `theory_gates.json` |
| Binary -> spacetime | `BIT_TO_SPACETIME_CENTRAL_EQUATION.md` |
| q=2 fixed point | `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md` |
| q=2 geometry | `MICRO_WALSH_QGEOM_BRIDGE.md` |
| Shape -> metric | `LOGICAL_SHAPE_METRIC_JACOBIAN.md` |
| Mass no-go | `S4_MASS_SPLITTING_NO_GO.md` |
| Higher shell | `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md` |
| HDA | `THREE_NODE_GRAPH_HDA_RESULT.md`, `JOINT_REGULATOR_LIMIT.md` |
| Regge control | `TT_REGGE_ZT_L6_RESULT.md` |
| Quartic TT space | `S4_TT_QUARTIC_COMPLETE_BASIS.md` |
| Observable dictionary | `TT_TO_REAL_PHYSICS_OBSERVABLES.md` |
| External tests | `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md` |
| Original story snapshot | `docs/archive/README_STORY_2026-08-17.md` |

Если отдельный physicalization theorem пока живёт только в research history, его канонический результат описан здесь inline, но отсутствующий main-file не объявляется частью frozen main evidence package.

---

# Эпилог. Что получилось из одного бинарного вопроса

Мы начали с

\[
q+2=2^q.
\]

Он выбрал `q=2`.

`q=2` построил octahedral `S2` link.

Canonical gluing дал `S3`.

Recursive causal growth дал exact fixed point `3`.

Dynamics дала `z~1` и 3+1-like history.

Quantum geometric tensor одновременно открыл geometry и phase.

Logical shape получил exact map в metric.

Peter–Weyl dynamics оказался nontrivial.

HDA приблизился к ADM structure.

Regge и Plebanski дали independent Einstein controls.

Generic quartic TT sector оказался шестимерным.

Потом теория сама остановила нас:

> **constraint spectrum ещё не physical time.**

Мы построили finite master projector.

Потом она сказала:

> **six-vector может не выжить IR вообще.**

И появился

\[
\boxed{6\to1\to0}.
\]

Потом compact U(1) сказал:

> **topology может дать charge lattice, но не может одна дать alpha.**

И появился independent `Z_A`.

Потом gravity сказала:

> **G, Lambda и alpha нельзя вытащить из одного красивого spectral number.**

И появились три разных microscopic estimators.

И наконец:

> **zero vacuum dispersion не означает zero quantum geometry.**

Connected metric fluctuations могут оставлять phase correlations даже при exact massless Lorentz cone.

Современная конечная машина поэтому не

```text
8.43% -> magical number -> experiment
```

и не

```text
constraint eigenvalue -> omega -> gravitational wave
```

а

\[
\boxed{
\text{binary microstructure}
\to\text{quantum geometry}
\to\text{constraints}
\to P_{phys}
\to\text{history / boundary amplitude}
\to\Gamma[g,A,\ldots]
\to
\begin{cases}
K_{TT},\\
K_A,\\
C_h^{conn}
\end{cases}
\to
\begin{cases}
6\to1\to0\text{ pole test},\\
\text{phase/correlation test},\\
G,\Lambda,Z_A
\end{cases}
\to\text{blind data}.}
\]

Если microscopic history calculation проходит эти gates, candidate theory получает настоящую physical prediction.

Если нет — соответствующая ветка должна быть отвергнута.

Так и должна заканчиваться научная сказка для взрослых: **не обещанием, что герой обязательно победит, а экспериментом, которому позволено решить финал.**