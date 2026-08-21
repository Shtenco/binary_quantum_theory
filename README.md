# От бита к пространству, гравитации, свету и реальному эксперименту

## Научная сказка для взрослых учёных детей — в которой формулы важнее чудес, а у природы всегда есть право сказать «нет»

> **Канонический статус: 21 августа 2026. Candidate theory.**
>
> Этот репозиторий не объявляет «теорию всего» доказанной. Он строит длинную, вычислимую и всё более жёсткую цепочку от бинарной различимости до трёхмерной PL-геометрии, 3+1-like history, SU(2)/Peter–Weyl quantum geometry, compact U(1) phase, spin-2, HDA/GR, physical projector, 1PI effective action и реальных экспериментальных observables.
>
> Главный принцип проекта: **красивое совпадение не становится физическим предсказанием, пока между объектами не построен явный мост.** Поэтому здесь сохраняются не только положительные результаты, но и no-go theorems, отрицательные controls, исправления прежних интерпретаций и открытые bottlenecks.

### Как читать репозиторий

- **README.md** — научное путешествие от бита к физике.
- **CANONICAL_THEORY_PACKAGE.md** — сухой доказательный индекс.
- **THEORY_STATUS.md** — человеческий status ledger.
- **theory_gates.json / physicalization ledgers** — machine-readable truth surface.
- **PREDICTIONS_AND_EXPERIMENTAL_TESTS.md** — внешний слой проверок.
- [Архив исходной сказки 17 августа 2026](docs/archive/README_STORY_2026-08-17.md) сохранён отдельным неизменяемым историческим снимком.

### Ярлыки доказательности

- **EXACT** — алгебраический или комбинаторный результат в явно заявленных предпосылках.
- **CI / FINITE PASS** — воспроизводимый конечномерный computation.
- **HELD-OUT** — prediction была заморожена до открытия проверочного результата.
- **CONDITIONAL** — физический вывод при явно записанной дополнительной гипотезе.
- **OPEN PHYSICAL** — математический объект определён, но нужный physical bridge или microscopic number ещё не получен.
- **NO-GO** — доказано, что привлекательный shortcut не работает.

---

# Пролог. Вселенная, у которой сначала нет координат

Представьте, что нам запрещено начинать с `x,y,z`.

Нет метров.

Нет решётки.

Нет заранее выбранной размерности.

Нет света.

Нет частиц.

Нет даже обещания, что continuum когда-нибудь появится.

Есть только различимость: локальное событие может различать несколько независимых бинарных альтернатив.

И из этой почти детской постановки проект пытается пройти всю дорогу:

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
 -> physical generating functional Z[g]
 -> 1PI effective action Gamma[g,A,...]
 -> TT and Maxwell physical kernels
 -> S4 -> SO(3) -> Lorentz universality ladder
 -> G, Lambda, Z_A
 -> pole observables + connected fluctuations
 -> blind experiment.
```

Важнейшая особенность истории в том, что она несколько раз сама запрещает нам слишком лёгкий финал.

Именно это делает её научной.

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

Получаются четыре route labels

```text
00  01  10  11
```

с Hamming adjacency `C4`.

Первое число возникает не как fitted parameter, а как решение уравнения.

---

# Глава 2. Четыре маршрута строят сферу вокруг точки

**[EXACT]**

Добавим к route-square два causal poles. Возникает octahedral shell

```text
V = 6
E = 12
F = 8
chi = 2
```

и потому simplicial surface

\[
\boxed{S^2}.
\]

У внутренней вершины обычного combinatorial 3-manifold link должен быть `S2`.

Первая геометрическая стрелка:

\[
\boxed{
\text{binary local homogeneity}
\to q=2
\to S^2\text{ vertex link}.
}
\]

Локальная sphere ещё не является глобальным пространством. Её надо склеить.

---

# Глава 3. Локальные сферы образуют глобальное трёхмерное пространство

**[EXACT / FINITE PL]**

Canonical minimal+flag globalization — boundary 4D cross-polytope, 16-cell:

```text
(V,E,F,T) = (8,24,32,16)
Betti     = (1,0,0,1)
```

У него:

- vertex links = octahedral `S2`;
- edge links = `S1`;
- triangle links = `S0`;
- каждая triangle two-sided;
- complex orientable;
- `boundary^2=0`;
- homology соответствует `S3`.

Поэтому в заявленной canonical completion

\[
\boxed{M^3\cong S^3}.
\]

Barycentric subdivision:

```text
16 -> 384 -> 9216 tetrahedra
```

и manifold conditions сохраняются на проверенных refinement levels.

**Граница утверждения:** это existence/stability theorem для canonical PL completion, а не доказательство уникальности абсолютно любого возможного nonflag global gluing.

---

# Глава 4. Лестница размерности действительно заканчивается на тройке

Раньше мы видели последовательность

```text
2.662965
 -> 2.951745
 -> 2.993853
 -> 2.999229782
 -> 2.999903694
 -> 2.999987961
 -> ...
```

Теперь её предел закрыт аналитически.

При `q=2`

\[
B=2^q=4,
\]

каждый active causal edge создаёт `2B=8` active children, а causal linear scale удваивается.

Exact vertex count:

\[
\boxed{N_g=\frac{4\,8^g+10}{7}}.
\]

One-step volume exponent:

\[
d_g=\log_2\frac{N_g}{N_{g-1}}
=3+\log_2\left(1-\frac{35}{16\,8^{g-1}+40}\right).
\]

Следовательно

\[
d_g<3,
\qquad
d_{g+1}>d_g,
\qquad
\boxed{d_g\nearrow3}.
\]

И потому

\[
\boxed{d_*^{causal-volume}=3}.
\]

Frozen `d_H=2.999229782139151` — конкретная finite ступень этой exact sequence.

---

# Глава 5. Почему одного числа «3» недостаточно

Независимые свидетели:

\[
D_{topo}=3,
\qquad
d_{causal-volume}\to3,
\]

и frozen dynamical values

\[
\boxed{d_H=2.999229782139151},
\qquad
\boxed{z\simeq0.998281156}.
\]

Исторически названный `ds_slice_holdout` quantity уже содержит деление на `z`:

\[
\boxed{d_{eff}^{slice}=\frac{d_H}{z}=3.004393867}.
\]

Его нельзя делить на `z` второй раз.

Для one-causal-time history:

\[
\boxed{d_{eff}^{history}=1+\frac{d_H}{z}\simeq4.004393867}.
\]

Так возникает согласованность

```text
local topology        -> 3
causal-volume growth  -> 3
z                     -> 1
history               -> 3+1-like scaling.
```

---

# Глава 6. Дискретное пространство учится выглядеть гладким

**[CI / COARSE-GRAINING]**

Observer smoothing:

```text
delta g       ~ b^-2.001707
grad(delta g) ~ b^-3.001458
delta R       ~ b^-4.000524
```

Это reconstruction/coarse-graining defects.

Одна прежняя красивая интерпретация была отвергнута: `delta g ~ b^-2` нельзя честно переименовать в Gaussian TT vacuum spectrum `P(k)~k^+1`.

Прямой reduced TT calculation позже дал

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

В проекте falsified interpretation не стирается — она становится отрицательным control.

---

# Глава 7. Один qubit одновременно открывает геометрию и фазу

Нормированный двухкомпонентный state живёт на

\[
S^3\subset\mathbb C^2.
\]

Physical ray quotient:

\[
\mathbb{CP}^1\cong S^2,
\]

а Hopf fibration:

\[
\boxed{U(1)\to S^3\to S^2}.
\]

Но ещё глубже обе ветви содержатся в quantum geometric tensor

\[
Q_{ab}
=\langle\partial_a\psi|
(1-|\psi\rangle\langle\psi|)
|\partial_b\psi\rangle.
\]

Для Bloch spinor

\[
|\psi\rangle=
\begin{pmatrix}
\cos(\theta/2)\\
e^{i\phi}\sin(\theta/2)
\end{pmatrix}
\]

получаем одновременно

\[
\boxed{ds^2_{FS}=\frac14(d\theta^2+\sin^2\theta\,d\phi^2)}
\]

и

\[
\boxed{F=\frac12\sin\theta\,d\theta\wedge d\phi}.
\]

То есть

\[
\boxed{
q=2\text{ ray}
\Rightarrow
\begin{cases}
\Re Q:&\text{ distinguishability / information geometry},\\
\Im Q:&\text{ Berry/Hopf phase / }U(1).
\end{cases}}
\]

Это один из самых красивых мостов проекта: geometry и phase не приклеены друг к другу позднее — они являются двумя частями одного quantum-geometric object.

---

# Глава 8. Четыре spin-1/2 прячут один collective spin-2

**[EXACT REPRESENTATION THEORY]**

\[
(1/2)^4=2\times j=0+3\times j=1+1\times j=2.
\]

В 16D four-qubit Hilbert space существует ровно один `j=2` irrep.

Massless TT reduction оставляет две physical helicity.

Это не утверждение «четыре qubits и есть гравитон». Это existence theorem для unique collective spin-2 carrier, который ещё должен пройти geometric и dynamical bridges.

---

# Глава 9. Logical shape превращается в metric

**[EXACT LOCAL BRIDGE]**

В logical singlet sector:

```text
X,Z -> intrinsic shape
Y   -> orientation pseudoscalar
```

Для regular tetrahedron

\[
g_0=
\begin{pmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{pmatrix}.
\]

Exact Jacobian tangents `M_X,M_Z` удовлетворяют

\[
\operatorname{Tr}(g_0^{-1}M_A)=0,
\]

\[
\boxed{
\operatorname{Tr}(g_0^{-1}M_Ag_0^{-1}M_B)
=\frac32\delta_{AB}}.
\]

Следовательно `(X,Z)` — orthogonal equal-norm trace-free metric tangents.

Стрелка

```text
logical shape -> ??? -> metric
```

заменена явным оператором.

---

# Глава 10. Пять metric modes и первое число 8.43%

**[CI + EXACT S4 REDUCTION]**

Six-edge representation:

\[
\boxed{6=A_1\oplus E\oplus T_2}.
\]

Для first refined q4 tangent kernel:

\[
\lambda_E=1.1111917875584736,
\qquad
\lambda_{T_2}=1.0220278507464782,
\]

\[
\Delta_{ET}=0.08916393681199541.
\]

Dimension-weighted traceless mean:

\[
\kappa_5=\frac{2\lambda_E+3\lambda_{T_2}}5
=1.0576934254712764.
\]

Поэтому

\[
\boxed{\frac{\Delta_{ET}}{\kappa_5}=0.08430036026012608}.
\]

Это **8.43% local Euclidean tetrahedral spin-2 anisotropy precursor**.

Он настоящий finite microscopic result.

Но он не равен автоматически ни physical `zeta4`, ни speed anisotropy, ни particle mass ratio.

---

# Глава 11. Почему 8.43% нельзя превратить в массы частиц

**[EXACT NO-GO]**

На traceless metric space

\[
5=E\oplus T_2.
\]

Normalize

\[
Q_{tet}=\frac35P_E-\frac25P_{T_2}.
\]

Если три поколения matter образуют один irreducible `T2` triplet, любой `S4`-invariant mass operator по Schur lemma

\[
\boxed{M=mI_3}.
\]

Причём

\[
Q_{tet}|_{T_2}=-\frac25I_3.
\]

Следовательно shortcut

```text
8.43% -> electron / muon / tau hierarchy
```

запрещён без independently derived flavor representation, symmetry-breaking spurion и Yukawa operator.

В этом репозитории нельзя искать известные массы через степени и комбинации `0.0843` и потом объявлять найденную нумерологию выводом.

---

# Глава 12. Peter–Weyl идёт на следующий shell

**[FINITE PASS]**

Spin parity:

\[
PH_EP=0.
\]

Определяем

\[
K=PH_E^2P
\]

и second-shell object

\[
\boxed{\Lambda=K^{-1/2}(PH_E^4P-K^2)K^{-1/2}}.
\]

Exact 32D calculation:

```text
rank(K) = 32
lambda_min(Lambda) = 10.635759878291307
lambda_max(Lambda) = 15.059927665966466
mean = 12.860443113390883
relative distance from scalar identity = 0.09440461833276048
```

Это finite **constraint spectral data**.

Именно здесь действует важная граница: eigenvalues `Lambda` не являются автоматически particle masses или physical frequencies.

---

# Глава 13. Geometry-only blocking не может тайно создать нужный RG flow

**[EXACT GALERKIN CONTROL]**

Для recursive PL geometry

\[
\boxed{P^TL_{g+1}P=\frac14L_g}
\]

с machine-level residual.

Если geometry и internal kernel factorize, все internal couplings масштабируются одинаково и normalized anisotropy ratio не течёт.

Значит genuine flow должен идти из

```text
Peter-Weyl recoupling
nonseparable quantum blocking
interblock transport
history dynamics
```

а не из скрытого geometric rescaling.

---

# Глава 14. Euclidean Hamiltonian получает Lorentzian вторую половину

Для Ashtekar–Barbero variables

\[
A_a^i=\Gamma_a^i+\beta K_a^i.
\]

Derivative-free kinetic pieces:

\[
H_E^{kin}=-\beta^2Q_{DW},
\qquad
H_L^{corr}=(1+\beta^2)Q_{DW},
\]

следовательно

\[
\boxed{H_E^{kin}+H_L^{corr}=Q_{DW}}.
\]

Это exact classical consistency control правильного DeWitt kinetic structure.

Он не является доказательством полной quantum beta-independence.

---

# Глава 15. Hamiltonian constraints учатся двигать пространство

Structural gravity target:

\[
[\hat H[N],\hat H[M]]
\to
i\hbar\hat D[\sharp(NdM-MdN)].
\]

Frozen route-normal generator строится независимо через cochain/Hodge/flux map.

Для fixed-cutoff scaling:

```text
C_cross / D = O(epsilon)
C_GG    / D = O(epsilon^2)
```

и существует conservative family

\[
J_{max}=o(\epsilon^{-2/13}).
\]

В локальной ADM family closure выбирает

\[
\boxed{c=1/2},
\qquad
\boxed{AB=1}.
\]

Cosmological term cancels из bracket, поэтому HDA **не** выводит численно `G` или `Lambda`.

---

# Глава 16. Plebanski и Regge независимо идут к Einstein structure

Две дороги:

```text
B-field -> simplicity -> Urbantke metric -> connection -> curvature -> Einstein criterion
```

и

```text
metric -> Regge Hessian -> Fierz-Pauli -> EH / Ward controls.
```

Regge TT residue sequence:

```text
L3 = 0.1021131745
L4 = 0.1114624530
L5 = 0.1161306996
```

Held-out rule

\[
Z_L=\frac18+\frac{C}{L^2}+\frac{D}{L^4}
\]

предсказал

```text
Z6_pred = 0.11876923193907167
Z6_obs  = 0.11876075461190198
relative error ~ 0.00714%
```

Это genuine internal held-out numerical control, но не внешнее experimental confirmation quantum gravity.

Directional calculations поддерживают общий continuum residue, стремящийся к `1/8`; finite directional convergence ещё не превращается в theorem о любой lattice anisotropy.

---

# Глава 17. Первый reduced TT propagator

**[EXACT REDUCED POSITIVE CONTROL]**

\[
\boxed{
G^{TT}_{AB}(\omega,\mathbf k)
=
\frac{\delta_{AB}}
{Z_T\left[4\sin^2(\omega/2)-\frac13\sum_i4\sin^2(k_i/2)+i0\right]}}
\]

имеет massless pole в этом reduced sector.

Small-momentum positive-control coefficients:

\[
\boxed{\eta_{2,bare}=-1/45},
\qquad
\boxed{\zeta_{4,bare}=-1/12}.
\]

Equal-time Gaussian covariance:

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

Эти числа — bare regulator controls, не final interacting IR prediction.

---

# Глава 18. Почему `R_aniso -> zeta4` было неправильной стрелкой

Logical higher-shell ratio

\[
R_{aniso}\simeq0.08975326618
\]

является internal Peter–Weyl RG diagnostic.

Он не является physical spatial dispersion coefficient.

Правильная дорога:

\[
\boxed{
\Gamma_{shape}
\to M
\to\Gamma_{metric}
\to K_{TT}
\to\text{physical pole observables}.}
\]

---

# Глава 19. Onsite kernel сжимается до трёх orbit numbers — но только onsite

**[EXACT S4 FOR k=0]**

Для одного tetrahedral coarse block:

\[
\boxed{C_6^{(0)}=a_0I+b_0A_{adj}+c_0O_{opp}}.
\]

Irrep eigenvalues:

\[
\lambda_{A_1}=a_0+4b_0+c_0,
\]

\[
\lambda_E=a_0-2b_0+c_0,
\qquad
\lambda_{T_2}=a_0-c_0.
\]

На traceless space:

\[
C_5^{(0)}=\kappa_5P_5+\Delta_{ET}Q_{tet}.
\]

Это правильная symmetry compression для onsite/full-S4 object.

Но generic directed momentum несёт собственную representation и требует более богатой структуры.

---

# Глава 20. Momentum сам несёт representation

Правильная covariance law:

\[
\boxed{C_6(\omega,g\mathbf k)=U_gC_6(\omega,\mathbf k)U_g^{-1}}.
\]

Representation count до TT quotient:

\[
\mathrm{Sym}^2(E\oplus T_2)
=2A_1\oplus2E\oplus T_1\oplus2T_2,
\]

и аналогично для quartic momentum harmonics.

После physical TT constraints

\[
\operatorname{tr}h=0,
\qquad
h_{ij}k_j=0
\]

exact polynomial quotient даёт

\[
\boxed{\dim\mathcal W^{(4)}_{TT,S_4}=6}.
\]

Это полный parity-even quartic TT pole space при surviving tetrahedral symmetry.

---

# Глава 21. Шесть Wilson coefficients и extractor без подгонки

Один complete basis:

\[
W_1=\mathcal R[h_{xx}^2k_z^4],
\quad
W_2=\mathcal R[h_{xx}^2k_x^4],
\]

\[
W_3=\mathcal R[h_{xy}^2k_z^4],
\quad
W_4=\mathcal R[h_{xy}^2k_y^4],
\]

\[
W_5=\mathcal R[h_{xx}^2k_y^2k_z^2],
\quad
W_6=\mathcal R[h_{xx}^2k_x^2k_z^2].
\]

Generic quartic correction:

\[
\boxed{\delta K_{TT}^{(4)}=Z_Tc_T^2a_*^2\sum_{r=1}^6c_rW_r}.
\]

High-symmetry `(100),(110),(111)` дают rank five. Добавление preregistered `(120)` закрывает rank six.

Для frozen six-observable extractor:

\[
\boxed{\det A=\frac1{699840000}\neq0}.
\]

`A^{-1}` фиксирован до открытия microscopic coefficients.

---

# Глава 22. Momentum рождается из interblock transport

Два face-sharing tetrahedra имеют stabilizer `S3`.

Каждый six-edge carrier:

\[
6=(A_1\oplus E)_{apex}\oplus(A_1\oplus E)_{face}.
\]

Reciprocal even nearest-neighbor transfer задаётся двумя symmetric `2x2` multiplicity matrices — всего шестью real transfer functions для canonical face-sharing pair.

Для regular tetrahedral neighbour vectors:

\[
\sum_an_a^in_a^j=\frac43\delta^{ij},
\]

но

\[
\boxed{
\sum_a(\mathbf k\cdot\mathbf n_a)^4
=\frac45(k^2)^2-\frac89Q_4^{cub}(\mathbf k)}.
\]

Поэтому geometry естественно допускает

```text
leading k^2 -> isotropic
quartic k^4 -> isotropic + tetrahedral memory.
```

---

# Глава 23. eta2 и zeta4 возвращаются только как nested hypothesis

Ansatz

\[
\bar e_4(\hat n)=\eta_2+\zeta_4Q_4^{cub}(\hat n)
\]

является двумерной subspace полного six-dimensional result.

Если production six-vector туда попадает, тогда

\[
\zeta_4=2(e_{100}-e_{110}),
\]

\[
\eta_2=\frac{e_{100}+4e_{110}}5,
\]

а held-out relation обязана быть

\[
\boxed{e_{100}-4e_{110}+3e_{111}=0}.
\]

Reduced bare positive control проходит этот relation exactly.

---

# Глава 24. Tetrahedral memory имеет parameter-free polarization fingerprint

Для single-`Q_tet` nested model TT eigenvalues:

\[
(100):\{3/5,-2/5\},
\]

\[
(110):\{7/20,-2/5\},
\]

\[
(111):\{-1/15,-1/15\}.
\]

И

\[
\frac12\operatorname{Tr}_{TT}Q_{tet}=\frac14Q_4^{cub}.
\]

Поэтому polarization splitting obeys

\[
\boxed{\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0}.
\]

Но это zero-fit fingerprint **только если** full six-vector действительно лежит в этой nested submodel.

---

# Глава 25. On-shell coefficients переживают field redefinitions

Пусть leading Einstein TT kernel

\[
K_0=Z_T(-\omega^2+c_T^2k^2)I_{TT}.
\]

Local field redefinition

\[
h\to(I+a_*^2R_2)h
\]

сдвигает quartic kernel terms пропорционально `K_0`.

На leading massless pole

\[
K_0=0,
\]

поэтому эти shifts исчезают.

Следовательно six-dimensional quotient описывает genuine **on-shell quartic pole observables**, хотя off-shell action может иметь больше basis-dependent coefficients.

---

# Глава 26. Главная физическая поправка: constraint spectrum — ещё не physical time propagator

Вот место, где теория стала взрослее всего.

Peter–Weyl operator

\[
\hat H[N]
\]

является Hamiltonian **constraint**.

Поэтому spectral resolvent

\[
(z-\hat H)^{-1}
\]

нельзя автоматически переименовать в physical propagator

\[
G(\omega,\mathbf k).
\]

Constraint spectral variable `z` не является автоматически physical frequency `omega`.

Легальная цепочка:

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

Именно поэтому finite `K/A/B/Lambda` Peter–Weyl data остаются важными constraint-dynamics observables, но не должны напрямую называться physical graviton self-energy.

---

# Глава 27. Physical projector перестал быть словом

**[EXACT FINITE THEOREM + CI PASS]**

Для конечного набора constraints `C_A` и любого positive-definite metric `G^{AB}` вводим master constraint

\[
\boxed{\mathbb M_G=C_A^\dagger G^{AB}C_B}.
\]

Тогда

\[
\boxed{\ker\mathbb M_G=\bigcap_A\ker C_A}.
\]

Physical projector — zero spectral projector

\[
\boxed{P_0=\chi_{\{0\}}(\mathbb M_G)}.
\]

CI positive control дал

\[
\max_A\|C_AP_0\|\simeq1.35\times10^{-15},
\]

\[
\max_{G_i,G_j}\|P_0(G_i)-P_0(G_j)\|
\simeq2.82\times10^{-15}.
\]

И heat-kernel convergence

\[
\|e^{-T\mathbb M}-P_0\|=e^{-T\Delta_M}
\]

совпала с finite spectral prediction на machine precision.

Открыт уже не сам projector, а его **theory-specific refinement / rigging limit**.

Правильный refinement test:

\[
\boxed{
\delta_P(g)=
\frac{\|P_{g+1}I_g-I_gP_g\|}{\|I_gP_g\|}
\to0}.
\]

---

# Глава 28. Время появляется после physical conditioning

Minimal constrained positive control:

\[
C=P_T+H_s.
\]

После projection на physical kernel и conditioning на relational clock states получается exact identity

\[
\boxed{
2\langle T_{out}|P_{phys}|T_{in}\rangle
=e^{-iH_s(T_{out}-T_{in})}}.
\]

То есть physical time не появляется переименованием eigenvalue constraint.

Он появляется через relational/boundary conditioning physical state amplitude.

Для gravity наиболее естественная branch — semiclassical boundary geometry, где proper separation `tau` задаётся самой metric/extrinsic geometry; тогда `omega` становится Fourier-conjugate к physical `tau`.

---

# Глава 29. Настоящая физика живёт в 1PI effective action

После physical projector/history measure нужный объект:

\[
Z[J_g,J_A,\ldots]
\]

и

\[
\Gamma[g,A,\ldots].
\]

Физические quadratic kernels:

\[
K_g=\frac{\delta^2\Gamma}{\delta h_{TT}\delta h_{TT}},
\qquad
K_A=\frac{\delta^2\Gamma}{\delta A_T\delta A_T}.
\]

И только теперь разрешено спрашивать о poles, residues, propagation, phase и observables.

Это новый главный physical bottleneck репозитория.

---

# Глава 30. Шесть коэффициентов могут законно исчезнуть

Это второй большой senior-поворот.

Полный `S4` quartic pole space имеет dimension six.

Но если RG восстанавливает continuous spatial rotations, physical observable vector обязан лечь на isotropic line.

Frozen extractor имеет замечательное exact свойство. Для isotropic coefficient vector

\[
v_{iso}=(6,24,6,36,-9,18)^T
\]

получаем

\[
\boxed{Av_{iso}=(1,1,1,1,1,1)^T}.
\]

Поэтому observable symmetry ladder:

\[
\boxed{S_4:\quad y\in\mathbb R^6},
\]

\[
\boxed{SO(3):\quad y_1=y_2=\cdots=y_6},
\]

а при unbroken Lorentz/diffeomorphism metric-only massless vacuum

\[
\boxed{y_1=\cdots=y_6=0}.
\]

Иными словами:

\[
\boxed{6\longrightarrow1\longrightarrow0}.
\]

Пять independent contrasts проверяют восстановление spatial isotropy. Шестая common amplitude проверяет, остаётся ли physical preferred-foliation quartic shift.

---

# Глава 31. Почему Lorentz-invariant metric-only vacuum защищает massless cone

Если IR vacuum Lorentz invariant, diffeomorphism unbroken и единственный low-energy helicity-2 field — metric graviton, inverse propagator имеет form

\[
\boxed{K_{TT}(s)=P_{TT}\,sF(a_*^2s)},
\qquad
s=-\omega^2+c^2k^2.
\]

Massless root

\[
\boxed{s=0}
\]

не сдвигается local analytic higher derivatives.

Они могут менять off-shell form factor и создавать additional heavy poles `F=0`, но не обязаны давать vacuum law

\[
\omega^2=k^2+\beta_4k^4+\beta_6k^6+\cdots
\]

для того же massless graviton.

Поэтому **ненулевая Planck-suppressed dispersion не является обязательной сигнатурой quantum gravity**.

Если six-vector остаётся ненулевым, теория обязана одновременно вывести physical preferred order parameter, а не просто сохранить orientation regulator.

---

# Глава 32. Если tetrahedral order физический, у него есть собственный tensor

Regular tetrahedron normals `n_a` define

\[
S_{ijkl}=\sum_{a=1}^4n_{ai}n_{aj}n_{ak}n_{al}.
\]

Trace-free quartic order tensor:

\[
\boxed{
T^{(4)}_{ijkl}
=S_{ijkl}-\frac45\delta_{(ij}\delta_{kl)}}.
\]

Он удовлетворяет

\[
T^{(4)}_{iikl}=0,
\qquad
\|T^{(4)}\|^2=\frac{128}{135},
\]

и

\[
\boxed{
T^{(4)}_{ijkl}k_ik_jk_kk_l
=-\frac89Q_4^{cub}(\mathbf k)}.
\]

Следовательно surviving nonzero anisotropic pole должен сопровождаться тем же physical order parameter в state/history/EFT.

Если order parameter исчезает, а anisotropic pole остаётся, это regulator contamination.

---

# Глава 33. Свет: compact U(1) получает canonical dynamics

На seed `S3` complex:

```text
V=8, E=24, F=32, T=16
rank d0 = 7
rank d1 = 17
d1 d0 = 0
b1 = 0
```

Если blocked Pancharatnam phase sector даёт positive local quadratic action,

\[
L_A=
\frac{Z_A}{2}(\dot\theta-d_0A_0)^TM_1(\dot\theta-d_0A_0)
-
\frac{Z_A}{2}(d_1\theta)^TM_2(d_1\theta),
\]

то canonical momentum

\[
p=Z_AM_1(\dot\theta-d_0A_0)
\]

и variation по `A_0` автоматически даёт Gauss law

\[
\boxed{d_0^Tp=0}.
\]

Transverse equation:

\[
\boxed{\ddot\theta=-M_1^{-1}d_1^TM_2d_1\theta}.
\]

Важно:

\[
\boxed{Z_A\text{ cancels from linear dispersion}.}
\]

`Z_A` задаёт normalization/coupling, а не скорость света.

---

# Глава 34. Почему Hopf topology не может сама выдать 137

Compactness фиксирует phase period и integer charge lattice.

Но family

\[
\Gamma_A[Z_A]=-rac{Z_A}{4}\int F^2,
\qquad Z_A>0
\]

имеет ту же gauge symmetry, compactness, Chern class и massless cone для любого `Z_A`.

Поэтому exact underdetermination statement:

\[
\boxed{
\text{Hopf topology + gauge symmetry + Maxwell form}
\not\Rightarrow\alpha}.
\]

В standard unit-charge convention

\[
\boxed{\alpha=\frac1{4\pi Z_A}}.
\]

Чтобы получить число, нужно вычислить `Z_A` из microscopic phase-history/RG dynamics.

Именно поэтому случайный Peter–Weyl eigenvalue нельзя переименовывать в `137`.

---

# Глава 35. Почему размерность 3+1 важна для compact U(1)

Две независимые ветви проекта дают

\[
q=2\to d_{space}=3
\]

и

\[
q=2\to U(1)_{compact}.
\]

Совместно:

\[
\boxed{3+1\text{ dimensional compact }U(1)}.
\]

Именно в этой dimensionality compact U(1) допускает deconfined/Coulomb phase; в lower-dimensional pure compact cases monopole effects создают намного более жёсткий confinement obstruction.

Это **compatibility theorem**, не proof того, что наш microscopic `Z_A` уже находится в deconfined basin.

Deconfinement остаётся dynamic question.

---

# Глава 36. Гравитация и свет могут иметь один и тот же principal cone

Если physical IR action приходит к одной emergent metric,

\[
\Gamma_{IR}[g,A]
=\int\sqrt{-g}\left[
\frac{R-2\Lambda}{16\pi G}
-\frac{Z_A}{4}F^2
\right]+\cdots,
\]

то leading kernels имеют общий principal scalar

\[
s=g^{\mu\nu}k_\mu k_\nu.
\]

В Lorentz-invariant vacuum:

\[
K_g=sF_g(s),
\qquad
K_\gamma=sF_\gamma(s).
\]

Следовательно исходные massless photon и graviton лежат на одном cone

\[
\boxed{s=0}.
\]

Ни `G`, ни `Z_A`, ни `alpha` не используются как ручка для подгонки скорости.

Conditional soft-graviton consistency дополнительно требует universal gravitational coupling к conserved energy-momentum, тогда как U(1) gauge consistency требует charge conservation, но не равенства charges разных species.

Так возникает естественная архитектура:

```text
gravity -> universal coupling
U(1)    -> quantized/conserved but species-dependent charge
```

---

# Глава 37. G, Lambda и alpha — три разных microscopic questions

Они не должны извлекаться из одного красивого spectrum.

## Newton constant

После geometric normalization metric:

\[
\Gamma[g]\supset C_R\int\sqrt{-g}\,R,
\]

и только тогда

\[
\boxed{G=\frac1{16\pi C_R}}.
\]

В internal units первым вычисляется dimensionless

\[
g_N=G/a_*^2.
\]

## Cosmological constant

`Lambda` не выводится HDA bracket.

Нужно найти physical background saddle

\[
\boxed{\frac{\delta\Gamma}{\delta g}\bigg|_{\bar g}=0}
\]

и извлечь curvature vacuum solution.

Finite unit-radius `S4` result около `3` — reconstruction positive control, а не measured dark energy.

## Fine-structure constant

\[
\boxed{\alpha=\frac1{4\pi Z_A}}
\]

после microscopic Maxwell stiffness calculation.

Три константы — три разных estimators.

---

# Глава 38. Нулевая vacuum dispersion не означает нулевую quantum geometry

Даже если final physical pole result даёт

\[
\boxed{c_1=\cdots=c_6=0},
\]

connected metric fluctuations могут быть ненулевыми:

\[
C_h(x,y)=\langle h(x)h(y)\rangle_c.
\]

Optical phase map:

\[
\delta\phi=\frac{k\ell}{2}Jh
\]

даёт

\[
\boxed{
C_\phi=
\left(\frac{k\ell}{2}\right)^2JC_hJ^T}.
\]

То есть experiment разделяется на две линии:

```text
pole / dispersion test
connected fluctuation / interference test
```

Zero Lorentz violation не делает quantum-gravity candidate автоматически невидимой.

Symmetry ratio

\[
\boxed{R_\gamma=2\frac{S_E}{S_{T_2}}}
\]

должен идти к `1` в isotropic IR, даже если absolute correlated phase PSD остаётся ненулевым.

---

# Глава 39. Пространство S3 не запрещает fermions

`S3` parallelizable, поэтому

\[
w_2(S^3)=0.
\]

Spin structures образуют torsor над

\[
H^1(S^3,\mathbb Z_2)=0.
\]

Значит

\[
\boxed{\text{на }S^3\text{ существует ровно одна spin structure}}.
\]

Seed 16-cell homology over `Z2`:

\[
(b_0,b_1,b_2,b_3)=(1,0,0,1).
\]

Это закрывает топологический prerequisite для global spin-1/2 fields.

Но Standard Model gauge group, chirality, generations и Yukawa sector **не выведены**. Geometric `Spin(3)~SU(2)` нельзя автоматически переименовывать в electroweak `SU(2)`.

---

# Глава 40. Если глобальная S3 survives в cosmology, у неё есть falsifiers

Если physical continuum действительно сохраняет closed `S3` spatial slices, FRW curvature sign фиксирован:

\[
\boxed{k=+1}.
\]

Это не означает заметную curvature today: `|Omega_k|` может быть очень малой при большом curvature radius.

Scalar harmonics на `S3` радиуса `a` имеют discrete spectrum

\[
\boxed{-\nabla^2Y_n=\frac{n(n+2)}{a^2}Y_n},
\qquad n=0,1,2,\ldots
\]

с degeneracy `(n+1)^2`.

Поэтому global topology потенциально проверяется low-k cosmological mode structure, независимо от local GR limit.

Это **conditional global-topology prediction**: physical history dynamics ещё должна показать, что canonical microscopic `S3` действительно survives как cosmological topology.

---

# Глава 41. Где тяжёлая микрофизика упирается сегодня

Здесь важно отделить теорию от вычислительной инженерии.

## j=1 representation RG

Canonical `j=1` `S4[2,2]` coarse carrier прошёл finite gate.

Master-projector preflight тоже PASS.

Ordered Peter–Weyl second-hit sharding показал, что exact paths реально вычисляются: успешные shards имеют finite sparse supports, zero first-order leakage и regulator-safe max spin.

Но часть route paths превышает hosted-runner wall, поэтому полный

\[
\Lambda(j=1)
\]

и

\[
R_{aniso}(j=1)
\]

ещё не frozen.

Следующий computational factorization должен идти глубже:

\[
H_sH_r
=\sum_{\alpha,\beta}H_{s,\beta}H_{r,\alpha}.
\]

Это exact decomposition operator sum, не physics approximation.

## full-H_E L1 block

Active-cone backend создан как exact representation optimization, но reference-vs-local certificate оказался тяжелее CI time budget до завершения guard.

Поэтому 72 production L1 shards нельзя считать запущенным/завершённым physical result до fail-closed equivalence PASS.

Правильное решение — shard сам certificate, не ослабляя tolerances.

Именно здесь сейчас находится вычислительный bottleneck.

---

# Глава 42. Что в теории уже действительно закрыто, а что ещё нет

| Arrow / observable | Status |
|---|---|
| `q+2=2^q -> q=2` | **EXACT** |
| q=2 octahedral `S2` link | **EXACT** |
| canonical PL `S3` completion | **EXACT / FINITE STABILITY** |
| causal-volume fixed point `d*=3` | **EXACT** |
| `d_H/z≈3.00439`, history `≈4.00439` | **FROZEN / DERIVED** |
| quantum geometric tensor split `ReQ/ImQ` | **EXACT KINEMATIC** |
| logical shape -> metric | **EXACT** |
| first L1 `E/T2` split = 8.43% | **FINITE PASS** |
| `8.43% -> particle masses` | **NO-GO** |
| 32D higher-shell constraint `Lambda` | **FINITE PASS** |
| geometry-only normalized anisotropy flow | **NO-FLOW CONTROL** |
| HDA/ADM structural closure in declared ansatz | **STRUCTURAL PASS** |
| Regge held-out `Z6` | **HELD-OUT PASS** |
| reduced massless TT propagator | **EXACT REDUCED CONTROL** |
| generic quartic TT `S4` quotient dim = 6 | **EXACT** |
| six-observable extractor | **EXACT** |
| on-shell field-redefinition invariance | **EXACT** |
| master-constraint finite projector | **EXACT + CI PASS** |
| constraint `z` = physical `omega` | **REJECTED SHORTCUT** |
| `6 -> 1 -> 0` observable ladder | **EXACT / CONDITIONAL IR** |
| compact Hopf U(1) carrier | **EXACT KINEMATIC** |
| Maxwell canonical form from positive phase action | **CONDITIONAL THEOREM** |
| `Hopf topology -> alpha` | **NO-GO** |
| unique spin structure on `S3` | **EXACT TOPOLOGICAL** |
| physical history / rigging continuum limit | **OPEN PHYSICAL** |
| physical 1PI `Gamma[g,A]` from microscopic history | **OPEN PHYSICAL** |
| frozen physical six-vector | **OPEN PHYSICAL** |
| microscopic `G`, `Lambda`, `Z_A` | **OPEN PHYSICAL** |
| Standard Model matter/Yukawa sector | **OPEN** |
| experimental confirmation | **OPEN / DATA** |

---

# Четыре дракона, которых нельзя обмануть

## Dragon I — constraint is not time

Нельзя переименовать spectral variable constraint в physical frequency. Сначала projector/history, потом `Gamma`, потом pole.

## Dragon II — regulator is not nature

Если tetrahedral anisotropy не сопровождается physical order parameter или не стабилизируется под refinement, она должна быть отвергнута как regulator memory.

## Dragon III — common scale is common

Нельзя отдельно подгонять scale для разных directions, polarizations, events или sectors. Либо microscopic principle выводит scale, либо один заранее объявленный datum калибрует его один раз.

## Dragon IV — blind data

После freeze theory output запрещено менять basis, удалять неудобный coefficient или выбирать submodel потому, что posterior оказался красивее.

У природы всегда должно оставаться право сказать `FAIL`.

---

# Воспроизводимые gates

Canonical regression:

```bash
python scripts/verify_theory_gates.py
python bcqg_bit_to_gravity_final.py --strict
```

Dimension fixed point:

```bash
python scripts/q2_dimension3_fixed_point_gate.py --max-generation 10
```

Shape -> metric:

```bash
python scripts/logical_shape_metric_jacobian_gate.py
```

Higher-shell Peter–Weyl:

```bash
python scripts/peter_weyl_higher_shell_lambda_gate.py --help
python scripts/peter_weyl_j1_s4_block_gate.py
```

TT reduced controls:

```bash
python scripts/tt_propagator_first_pass.py
python scripts/tt_vacuum_two_point_gate.py
```

Complete generic quartic TT theorem:

```bash
python scripts/s4_tt_quartic_complete_basis_gate.py
python scripts/s4_tt_six_wilson_predictor.py --selftest
```

Nearest-block symmetry:

```bash
python scripts/nearest_block_s3_transfer_gate.py
```

Nested tetrahedral checks:

```bash
python scripts/c6_tt_wilson_extractor.py
python scripts/tetrahedral_tt_birefringence_gate.py
```

---

# Канонические документы

| Layer | Entry point |
|---|---|
| Full evidence index | `CANONICAL_THEORY_PACKAGE.md` |
| Human status | `THEORY_STATUS.md` |
| Machine truth ledger | `theory_gates.json` |
| Central binary -> spacetime equation | `BIT_TO_SPACETIME_CENTRAL_EQUATION.md` |
| q=2 fixed point | `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md` |
| q=2 geometry | `MICRO_WALSH_QGEOM_BRIDGE.md` |
| q=2 U(1) phase | `Q2_PANCHARATNAM_U1_LIGHT_BRIDGE.md` where present in physicalization history |
| Shape -> metric | `LOGICAL_SHAPE_METRIC_JACOBIAN.md` |
| Mass shortcut no-go | `S4_MASS_SPLITTING_NO_GO.md` |
| Peter–Weyl higher shell | `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md` |
| HDA | `THREE_NODE_GRAPH_HDA_RESULT.md`, `JOINT_REGULATOR_LIMIT.md` |
| Regge held-out control | `TT_REGGE_ZT_L6_RESULT.md` |
| Complete quartic TT space | `S4_TT_QUARTIC_COMPLETE_BASIS.md` |
| Observable bridge | `TT_TO_REAL_PHYSICS_OBSERVABLES.md` |
| External tests | `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md` |
| Historical story snapshot | `docs/archive/README_STORY_2026-08-17.md` |

Если конкретный physicalization document ещё живёт только в research branch, README содержит его канонический результат inline, но не объявляет отсутствующий в `main` файл частью frozen main evidence package.

---

# Эпилог. Что получилось из одного бинарного вопроса

Мы начали с почти наивного уравнения

\[
q+2=2^q.
\]

Оно выбрало

\[
q=2.
\]

`q=2` построил octahedral `S2` link.

Canonical gluing дал `S3`.

Recursive causal growth дал exact fixed point `3`.

Dynamical scaling оказался близок к relativistic `z=1`.

Qubit geometry одновременно принесла `SU(2)` geometry и compact `U(1)` phase.

Logical shape получил точный map в metric.

Peter–Weyl dynamics оказался nontrivial.

Constraint algebra приблизился к ADM/HDA structure.

Regge и Plebanski дали независимые Einstein controls.

Generic quartic TT sector оказался не удобной парой параметров, а ровно шестимерным observable space.

Потом теория сама остановила нас и сказала:

> constraint spectrum ещё не physical time.

Мы построили master projector.

Потом теория сказала:

> tetrahedral six-vector может не выжить IR вообще.

И появился ladder

\[
\boxed{6\to1\to0}.
\]

Потом `U(1)` сказал:

> topology может дать charge lattice, но не может одна дать `alpha`.

И появился отдельный `Z_A`.

Потом gravity сказала:

> `G`, `Lambda` и `alpha` нельзя вытащить из одного красивого spectral number.

И появились три разных microscopic estimators.

И наконец выяснилось ещё одно важное:

> даже если vacuum dispersion в итоге равна нулю, connected quantum geometry всё равно может оставлять measurable phase correlations.

Поэтому современная конечная машина проекта выглядит не так:

```text
8.43% -> magical number -> experiment
```

и не так:

```text
constraint eigenvalue -> omega -> gravitational wave
```

а так:

\[
\boxed{
\text{binary microstructure}
\to
\text{quantum geometry}
\to
\text{constraints}
\to
P_{phys}
\to
\text{history / boundary amplitude}
\to
\Gamma[g,A,\ldots]
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
\to
\text{blind data}.
}
\]

Если microscopic history calculation проходит все эти gates, candidate theory получает настоящую физическую prediction.

Если нет — соответствующая ветка должна быть отвергнута.

Так и должна заканчиваться научная сказка для взрослых: не обещанием, что герой обязательно победит, а экспериментом, которому позволено решить финал.