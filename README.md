# От бита к пространству, гравитации и реальному эксперименту

## Научная сказка для взрослых учёных детей — в которой формулы важнее чудес, а у природы есть право сказать «нет»

> **Канонический статус: 17 августа 2026. Candidate theory.**
>
> Этот репозиторий не объявляет «теорию всего» доказанной. Он строит длинную, воспроизводимую и всё более жёсткую цепочку от бинарной различимости до 3D пространства, 3+1-like history, SU(2)/Peter–Weyl quantum geometry, spin-2, HDA/GR, реального TT propagator и экспериментально измеримой дисперсии gravitational waves.
>
> Главный принцип репозитория: **красивое совпадение не становится физическим предсказанием, пока не существует выведенного моста между объектами.** Поэтому здесь сохраняются и положительные результаты, и отрицательные controls, и исправления старых интерпретаций.

### Ярлыки доказательности

- **EXACT** — алгебраический/комбинаторный результат в явно заявленных предпосылках.
- **CI** — воспроизводимый finite computation.
- **HELD-OUT** — prediction была frozen до открытия проверочного результата.
- **CONDITIONAL** — вывод зависит от явно записанной дополнительной физической гипотезы.
- **OPEN** — мост сформулирован, но нужный microscopic number ещё не получен.

---

# Пролог. Вселенная, у которой сначала нет координат

Представьте, что мы не имеем права написать `x,y,z`.

Нет решётки.

Нет заранее выбранной размерности.

Нет даже обещания, что continuum вообще появится.

Есть только локальная различимость: событие может различить несколько независимых бинарных альтернатив.

Из этой почти детской постановки проект постепенно приходит к цепочке

```text
binary distinction
 -> q=2
 -> octahedral S2 local link
 -> canonical recursive PL S3 phase
 -> exact causal-volume fixed point d*=3
 -> z ~ 1
 -> 3+1-like history
 -> SU(2) quantum geometry + Hopf U(1) phase
 -> unique collective spin-2 carrier
 -> exact logical-shape -> metric Jacobian
 -> five traceless metric modes E + T2
 -> 8.43% first refined tetrahedral precursor
 -> Peter-Weyl H_E / higher shells
 -> Lorentzian completion + HDA/ADM
 -> onsite six-edge kernel C6^(0)=aI+bA+cO
 -> face-sharing S3 interblock transfer
 -> covariant C6(omega,k)
 -> complete six-dimensional quartic TT Wilson sector
 -> two physical TT pole branches e4_1(n), e4_2(n)
 -> A4_1(n), A4_2(n) in real GW modified-dispersion language
 -> phase / delay / birefringence / optical readout
 -> preregistered blind experiment.
```

У этой истории есть важная особенность: несколько раз она сама запрещает нам слишком лёгкий финал.

Именно поэтому она становится научнее по мере развития.

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

Получаются четыре routes

```text
00  01  10  11
```

с Hamming adjacency `C4`.

Здесь число два не выбрано автором после просмотра результата. Оно является решением локального equation.

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

Первая геометрическая стрелка поэтому выглядит так:

\[
\boxed{
\text{binary local homogeneity}
\to q=2
\to S^2\text{ vertex link}.
}
\]

Но локальная sphere ещё не является пространством. Её надо уметь глобально склеить.

---

# Глава 3. Локальные сферы образуют глобальное трёхмерное пространство

**[EXACT / FINITE PL]**

Canonical minimal+flag globalization — boundary 4D cross-polytope, то есть 16-cell:

```text
(V,E,F,T) = (8,24,32,16)
Betti     = (1,0,0,1)
```

У него

- vertex links = octahedral `S2`;
- edge links = `S1`;
- triangle links = `S0`;
- каждая triangle two-sided;
- complex orientable;
- `boundary^2=0`;
- homology соответствует `S3`.

Следовательно в заявленной canonical completion

\[
\boxed{M^3\cong S^3}.
\]

Barycentric subdivision даёт

```text
16 -> 384 -> 9216 tetrahedra
```

и manifold conditions сохраняются на проверенных уровнях.

**Граница утверждения:** это exact existence/stability result для canonical PL completion. Голый causal graph пока не доказан как единственный возможный global gluing mechanism.

Документ: `GLOBAL_MANIFOLD_Q2_COMPLETION.md`.

---

# Глава 4. Лестница размерности действительно заканчивается на тройке

Раньше мы видели красивую последовательность

```text
2.662965
 -> 2.951745
 -> 2.993853
 -> 2.999229782
 -> 2.999903694
 -> 2.999987961
 -> ...
```

Теперь её предел не extrapolation, а theorem.

**[EXACT]**

При `q=2`

\[
B=2^q=4.
\]

Каждый active causal edge создаёт `2B=8` active children, а causal length scale удваивается.

Exact vertex count:

\[
\boxed{
N_g=\frac{4\,8^g+10}{7}.
}
\]

One-step volume exponent

\[
d_g=\log_2\frac{N_g}{N_{g-1}}
\]

равен

\[
\boxed{
d_g
=3+\log_2\left(
1-\frac{35}{16\,8^{g-1}+40}
\right).
}
\]

Отсюда

\[
d_g<3,
\qquad
d_{g+1}>d_g,
\qquad
\boxed{d_g\nearrow3}.
\]

И поэтому

\[
\boxed{d_*^{causal-volume}=\log_2 8=3}.
\]

Frozen `d_H=2.999229782...` — это не случайное попадание около тройки, а конкретная finite ступень этой exact monotone sequence.

Документ: `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md`.

---

# Глава 5. Почему одного числа «3» всё равно недостаточно

Хороший результат требует независимых свидетелей.

Здесь их несколько:

\[
D_{topo}=3
\]

из `S2` links и canonical PL `M3`,

\[
d_{causal-volume}\to3
\]

из exact rewrite growth,

и frozen dynamical values

\[
\boxed{d_H=2.999229782139151},
\]

\[
\boxed{z=0.998281156}.
\]

В frozen route code исторически называвшийся `ds_slice_holdout` quantity уже равен

\[
\boxed{
d_{eff}^{slice}=\frac{d_H}{z}=3.004393867.
}
\]

Это важно: `3.004393867` нельзя делить на `z` второй раз.

Для one-causal-time history

\[
\boxed{
d_{eff}^{history}
=1+\frac{d_H}{z}
\simeq4.004393867.
}
\]

Получается независимая согласованность

```text
local topology        -> 3
causal-volume growth  -> 3
z                     -> 1
history               -> 3+1-like scaling.
```

Conditional Hodge/two-form selectors дают дополнительное объяснение, почему connection/2-form theory особенно естественно выбирает `3+1`, но не заменяют эти measurements.

Документы: `HODGE_DIMENSION_SELECTOR.md`, `TWO_FORM_DIMENSION_PRINCIPLE.md`.

---

# Глава 6. Дискретное пространство учится выглядеть гладким

**[CI / COARSE-GRAINING]**

Observer smoothing даёт

```text
delta g       ~ b^-2.001707
grad(delta g) ~ b^-3.001458
delta R       ~ b^-4.000524
simplicity    ~ b^-1.994838
Urbantke g    ~ b^-2.019746
```

Это reconstruction/coarse-graining defects.

Одна старая красивая интерпретация была отвергнута: из `delta g ~ b^-2` нельзя было честно объявлять Gaussian TT vacuum spectrum `P(k)~k^+1`.

Прямой reduced TT two-point calculation позже дал

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

Так репозиторий сохраняет не только successes, но и собственные falsified interpretations.

---

# Глава 7. Один qubit открывает двери SU(2) и U(1)

Нормированный двухкомпонентный state живёт на

\[
S^3\subset\mathbb C^2.
\]

Physical ray quotient даёт

\[
\mathbb{CP}^1\cong S^2
\]

и Hopf fibration

\[
\boxed{U(1)\to S^3\to S^2}.
\]

Поэтому один q=2 carrier естественно содержит две линии:

```text
SU(2) / Bloch / flux geometry
U(1) Pancharatnam-Berry phase fiber.
```

Canonical phase link

\[
U_{vw}=\frac{\langle\psi_v|\psi_w\rangle}
{|\langle\psi_v|\psi_w\rangle|}
\]

ведёт себя как compact lattice `U(1)` connection.

**[EXACT KINEMATIC]** U(1) carrier есть.

**[OPEN DYNAMIC]** physical Maxwell phase требует deconfinement и microscopic stiffness `Z_A`.

Документ: `Q2_PANCHARATNAM_U1_LIGHT_BRIDGE.md`.

---

# Глава 8. Четыре spin-1/2 прячут один-единственный collective spin-2

**[EXACT REPRESENTATION THEORY]**

\[
(1/2)^4
=2\times j=0+3\times j=1+1\times j=2.
\]

Следовательно 16D four-qubit Hilbert space содержит ровно один `j=2` irrep.

Massless TT reduction оставляет две physical helicity.

Это не утверждение «четыре qubits и есть гравитон». Это statement о существовании unique collective spin-2 carrier, который после geometric bridge может поддержать tensor mode.

---

# Глава 9. Logical shape превращается в metric

**[EXACT LOCAL BRIDGE]**

В logical singlet sector

```text
X,Z -> intrinsic shape
Y   -> orientation pseudoscalar.
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

Exact Jacobian matrices `M_X,M_Z` удовлетворяют

\[
\operatorname{Tr}(g_0^{-1}M_A)=0,
\]

\[
\boxed{
\operatorname{Tr}(g_0^{-1}M_Ag_0^{-1}M_B)
=\frac32\delta_{AB}.
}
\]

Значит `(X,Z)` образуют orthogonal equal-norm trace-free metric tangent.

Прежняя стрелка

```text
logical shape -> ??? -> metric
```

закрыта конкретным оператором `M`.

Документ: `LOGICAL_SHAPE_METRIC_JACOBIAN.md`.

---

# Глава 10. Пять metric modes и первое число 8.43%

**[CI + EXACT S4 REDUCTION]**

24 barycentric L1 chambers canonical map’ом сжимаются в шесть parent-edge observables.

Six-edge representation:

\[
\boxed{6=A_1\oplus E\oplus T_2}.
\]

Первый q4-projected tangent kernel имеет

```text
a_same     = 1.0220278507464782
b_adjacent = -0.044581968405997735
c_opposite = 0
```

и

\[
\lambda_E=1.1111917875584736,
\]

\[
\lambda_{T_2}=1.0220278507464782.
\]

Поэтому

\[
\Delta_{ET}=0.08916393681199541.
\]

Dimension-weighted traceless mean

\[
\kappa_5
=\frac{2\lambda_E+3\lambda_{T_2}}5
=1.0576934254712764
\]

и

\[
\boxed{
\frac{\Delta_{ET}}{\kappa_5}
=0.08430036026012608.
}
\]

Вот источник **8.43% tetrahedral spin-2 precursor**.

Он настоящий microscopic result.

Но он ещё не physical dispersion coefficient.

Документ: `L1_Q4_S4_METRIC_COMPRESSION_RESULT.md`.

---

# Глава 11. Почему 8.43% нельзя магически превратить в массы частиц

**[EXACT NO-GO]**

На traceless metric space

\[
5=E\oplus T_2.
\]

Unique onsite tetrahedral splitter можно нормировать как

\[
\boxed{
Q_{tet}=\frac35P_E-\frac25P_{T_2}.
}
\]

Если три поколения matter образуют один irreducible `T2` triplet, любой `S4`-invariant mass operator по Schur lemma пропорционален identity:

\[
\boxed{M=mI_3}.
\]

И сам `Q_tet` внутри `T2`

\[
Q_{tet}|_{T_2}=-\frac25I_3.
\]

Поэтому

```text
8.43% -> electron/muon/tau hierarchy
```

**невозможно без дополнительного derived flavor-breaking operator.**

8.43% может позже стать geometric spurion normalization, но только после независимого вывода matter representation, symmetry breaking и Yukawa map.

Документ: `S4_MASS_SPLITTING_NO_GO.md`.

---

# Глава 12. Peter–Weyl идёт на следующий shell

**[CI / EXACT FINITE]**

Spin parity даёт

\[
PH_EP=0.
\]

Определяем

\[
K=PH_E^2P
\]

и normalized second-shell object

\[
\boxed{
\Lambda
=K^{-1/2}(PH_E^4P-K^2)K^{-1/2}.
}
\]

Exact 32-column calculation при second-hit wall `Jmax=5/2` дал

```text
rank(K) = 32
lambda_min(Lambda) = 10.635759878291307
lambda_max(Lambda) = 15.059927665966466
mean = 12.860443113390883
relative distance from scalar identity = 0.09440461833276048
```

Pair trace сохраняет nontrivial shape/orientation structure.

Это доказывает, что next-shell dynamics не превращается в trivial scalar identity.

Но её eigenvalues не называются particle masses.

Документ: `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md`.

---

# Глава 13. Geometry-only blocking не может спрятанно создать нужный RG flow

**[EXACT GALERKIN CONTROL]**

Для recursive PL geometry

\[
\boxed{
P^TL_{g+1}P=\frac14L_g
}
\]

с machine-level residual.

Если geometry и internal kernel factorize, все internal couplings получают один и тот же factor, поэтому их ratio не течёт.

Следовательно nontrivial `E/T2` flow обязан приходить из

```text
Peter-Weyl recoupling
nonseparable quantum blocking
interblock transport
```

а не из скрытого geometric rescaling.

Документ: `PL_GALERKIN_ANISOTROPY_NO_FLOW.md`.

---

# Глава 14. Euclidean Hamiltonian получает Lorentzian вторую половину

Для Ashtekar–Barbero variables

\[
A_a^i=\Gamma_a^i+\beta K_a^i.
\]

Derivative-free kinetic pieces удовлетворяют

\[
H_E^{kin}=-\beta^2Q_{DW},
\]

\[
H_L^{corr}=(1+\beta^2)Q_{DW},
\]

и поэтому

\[
\boxed{H_E^{kin}+H_L^{corr}=Q_{DW}}.
\]

Это exact classical consistency control правильного DeWitt kinetic structure.

Он не объявляет quantum beta-independence доказанной автоматически.

---

# Глава 15. Hamiltonian constraints должны научиться двигать пространство

Главная structural gravity equation:

\[
[\hat H[N],\hat H[M]]
\to
i\hbar\hat D[\sharp(NdM-MdN)].
\]

В frozen habitat route-normal generator строится независимо через cochain/Hodge/flux map.

Для fixed-cutoff scaling

```text
C_cross/D = O(epsilon)
C_GG/D    = O(epsilon^2)
```

и поэтому extra Lorentzian channels исчезают относительно diffeomorphism target.

Conservative simultaneous family

\[
J_{max}=o(\epsilon^{-2/13})
\]

существует, но uniform theorem для абсолютно любого joint path не заявляется.

В локальной ADM-family closure выбирает

\[
\boxed{c=1/2},
\qquad
\boxed{AB=1}.
\]

И не выбирает ложным образом абсолютный `G` или cosmological `Lambda`.

---

# Глава 16. Независимые Plebanski и Regge дороги сходятся к Einstein structure

Две downstream ветви:

```text
B-field -> simplicity -> Urbantke metric -> connection -> curvature -> Einstein criterion
```

и

```text
metric -> Regge Hessian -> Fierz-Pauli -> EH cubic -> Ward restoration.
```

Regge full metric Hessian, до TT projection, приближается к Fierz–Pauli ratios

\[
(1,-2,2,-1)
\]

с leading finite-spacing errors примерно `O(L^-2)`.

Held-out finite-size prediction для TT residue:

```text
Z6_pred = 0.11876923193907167
Z6_obs  = 0.11876075461190198
relative error ~ 0.00714%
```

Это один из самых чистых preregistered numerical tests репозитория.

---

# Глава 17. Первый настоящий TT propagator

**[EXACT REDUCED KERNEL]**

\[
\boxed{
G^{TT}_{AB}(\omega,\mathbf k)
=
\frac{\delta_{AB}}
{Z_T\left[
4\sin^2(\omega/2)
-\frac13\sum_i4\sin^2(k_i/2)
+i0
\right]}.
}
\]

Pole mass

\[
\boxed{m_g=0}
\]

в этом reduced sector.

Small-momentum expansion даёт bare positive-control coefficients

\[
\boxed{\eta_{2,bare}=-1/45},
\]

\[
\boxed{\zeta_{4,bare}=-1/12}.
\]

Equal-time Gaussian covariance даёт

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

Это reduced control, а не уже full interacting microscopic IR answer.

---

# Глава 18. Почему старое `R_aniso -> zeta4` было неправильной стрелкой

Logical operator decomposition

\[
End(E)=A_1(I)+A_2(Y)+E(X,Z).
\]

`Y` — orientation pseudoscalar.

`X,Z` — intrinsic mirror-even shape.

Поэтому logical higher-shell ratio

\[
R_{aniso}\simeq0.08975326618
\]

является internal Peter–Weyl RG diagnostic.

Он **не является** physical spatial cubic-dispersion coefficient.

Правильная дорога начинается с metric carrier:

\[
\boxed{
\Gamma_{shape}
\to M
\to \Gamma_{metric}
\to K_{TT}
\to\text{physical pole coefficients}.
}
\]

Документ: `LOGICAL_SHAPE_TO_TT_RG_BRIDGE.md`.

---

# Глава 19. Onsite kernel действительно сжимается до трёх orbit numbers

**[EXACT S4 FOR k=0 / ONSITE]**

Для одного tetrahedral coarse block

\[
\boxed{
C_6^{(0)}(\omega)
=a_0I+b_0A_{adj}+c_0O_{opp}.
}
\]

Irrep eigenvalues:

\[
\lambda_{A_1}=a_0+4b_0+c_0,
\]

\[
\lambda_E=a_0-2b_0+c_0,
\]

\[
\lambda_{T_2}=a_0-c_0.
\]

На traceless space

\[
\boxed{
C_5^{(0)}
=\kappa_5P_5+\Delta_{ET}Q_{tet}
}
\]

где

\[
\kappa_5=\frac{2\lambda_E+3\lambda_{T_2}}5,
\qquad
\Delta_{ET}=\lambda_E-\lambda_{T_2}=2(c_0-b_0).
\]

Именно этот local depth-two full-`H_E` object сейчас вычисляется production workflow’ом через exact node sharding.

Почему sharding exact:

\[
H_B=\sum_{w=0}^{23}H_w,
\]

поэтому

\[
H_Bu_e
=\sum_{w=0}^{23}H_wu_e.
\]

72 independent shards = `3 edge representatives x 24 H_w` меняют только вычислительную факторизацию, не operator definition.

---

# Глава 20. Главный senior-поворот: momentum сам несёт representation

Здесь теория стала строже.

Слишком ранняя версия physicalization предполагала

\[
C_6(\omega,\mathbf k)=aI+bA+cO
\]

для любого directed `k`.

Это верно для onsite/full-S4-invariant object, но **не является general theorem при generic nonzero vector momentum**.

Правильная covariance law:

\[
\boxed{
C_6(\omega,g\mathbf k)
=U_gC_6(\omega,\mathbf k)U_g^{-1}.
}
\]

Направление `k` само трансформируется.

Representation theory даёт до TT constraints

\[
\mathrm{Sym}^2(E\oplus T_2)
=2A_1\oplus2E\oplus T_1\oplus2T_2,
\]

\[
\mathrm{Sym}^4(T_2)
=2A_1\oplus2E\oplus T_1\oplus2T_2.
\]

Отсюда generic quartic traceless sector содержит

\[
2^2+2^2+1^2+2^2=13
\]

`S4` singlets.

Но physical TT conditions

\[
\operatorname{tr}h=0,
\qquad
h_{ij}k_j=0
\]

резко сокращают пространство.

Exact polynomial quotient даёт

\[
\boxed{
\dim\mathcal W^{(4)}_{TT,S_4}=6.
}
\]

Это теперь полный общий quartic physical target.

Документ: `S4_TT_QUARTIC_COMPLETE_BASIS.md`.

---

# Глава 21. Шесть Wilson coefficients вместо удобной, но преждевременной пары

**[EXACT COMPLETE BASIS]**

Определим Reynolds average

\[
\mathcal R[f]=\frac1{24}\sum_{g\in S_4}f(g\cdot h,g\cdot k).
\]

Один простой complete TT basis:

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

Generic parity-even quartic physical kernel:

\[
\boxed{
\delta K_{TT}^{(4)}
=Z_Tc_T^2a_*^2\sum_{r=1}^{6}c_rW_r.
}
\]

Таким образом настоящая dimensionless gravitational prediction generically — это

\[
\boxed{
\mathbf c^{IR}
=(c_1,c_2,c_3,c_4,c_5,c_6)^{IR}.
}
\]

Три high-symmetry directions `(100),(110),(111)` дают только rank five.

Добавление одного frozen generic direction

\[
\boxed{(120)}
\]

закрывает rank six.

Для выбранных шести polarization-resolved observables exact extraction matrix имеет

\[
\boxed{
\det A=\frac1{699840000}\ne0.
}
\]

И `A^{-1}` уже записан в репозитории **до** открытия production coefficients.

Это убирает generic tensor fitting ambiguity.

Executable: `scripts/s4_tt_quartic_complete_basis_gate.py`.

---

# Глава 22. Где физически появляется momentum

Onsite return не знает, куда распространяется волна.

Momentum появляется из interblock transport.

Два face-sharing tetrahedra имеют shared-face stabilizer `S3`.

Каждый six-edge carrier под ним раскладывается как

\[
\boxed{
6=(A_1\oplus E)_{apex}\oplus(A_1\oplus E)_{face}.
}
\]

Reciprocal even nearest-neighbor transfer поэтому задаётся двумя symmetric `2x2` multiplicity matrices:

```text
one in A1
one in E
```

то есть ровно

\[
\boxed{3+3=6}
\]

real scalar transfer functions для одной canonical shared-face pair.

Все четыре local neighbor directions получаются `S4` transport’ом.

Для regular tetrahedral neighbor vectors

\[
\sum_a n_a^in_a^j=\frac43\delta^{ij}.
\]

Leading `k^2` moment therefore isotropic в equal-hopping control.

Fourth moment

\[
\boxed{
\sum_a(\mathbf k\cdot\mathbf n_a)^4
=\frac45(k^2)^2-\frac89Q_4^{cub}(\mathbf k).
}
\]

То есть сама tetrahedral geometry естественно даёт

```text
leading k^2 -> isotropic
quartic k^4 -> isotropic + tetrahedral memory.
```

Это объясняет, как finite microscopic anisotropy может быть irrelevant correction, не разрушая Einstein light cone.

Документ: `NEAREST_BLOCK_S3_TRANSFER_CLOSURE.md`.

---

# Глава 23. eta2 и zeta4 возвращаются — но теперь как nested hypothesis

Старый compact ansatz

\[
\bar e_4(\hat n)
=\eta_2+\zeta_4Q_4^{cub}(\hat n)
\]

не выбрасывается.

Он становится **проверяемой двумерной subspace внутри полного six-dimensional result**.

Если frozen six-vector действительно лежит в этой subspace, тогда

\[
\zeta_4=2(e_{100}-e_{110}),
\]

\[
\eta_2=\frac15e_{100}+\frac45e_{110},
\]

а третье направление обязано удовлетворять

\[
\boxed{
e_{100}-4e_{110}+3e_{111}=0.
}
\]

Reduced bare propagator проходит этот positive control и возвращает

\[
\eta_{2,bare}=-1/45,
\qquad
\zeta_{4,bare}=-1/12.
\]

Но production microscopic result сначала обязан раскрыть **все шесть** `c_r`.

Документ: `C6_TO_TT_WILSON_COEFFICIENTS.md`.

---

# Глава 24. Tetrahedral memory может расщеплять две gravitational polarizations

Для single-`Q_tet` nested model exact TT projection даёт

\[
(100):\quad\{3/5,-2/5\},
\]

\[
(110):\quad\{7/20,-2/5\},
\]

\[
(111):\quad\{-1/15,-1/15\}.
\]

И identity

\[
\boxed{
\frac12\operatorname{Tr}_{TT}Q_{TT}(\hat n)
=\frac14Q_4^{cub}(\hat n).
}
\]

Если quartic splitter amplitude назвать `gamma4`, то

\[
\boxed{\zeta_4=\gamma_4/4}
\]

для polarization average.

А polarization splitting obeys parameter-free pattern

\[
\boxed{
\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0.
}
\]

Это сильный blind fingerprint.

Но только если полный six-Wilson result действительно проходит single-`Q_tet` nested hypothesis.

Документ: `TETRAHEDRAL_TT_BIREFRINGENCE_THEOREM.md`.

---

# Глава 25. Из Wilson coefficients получается реальная скорость и реальная фаза

Для двух physical TT poles

\[
\boxed{
\omega_\sigma^2
=c^2k^2\left[
1+a_*^2k^2e_{4,\sigma}(\hat n)+O(a_*^4k^4)
\right],
\qquad\sigma=1,2.
}
\]

Тогда

\[
\boxed{
\frac{v_{g,\sigma}-c}{c}
=\frac32a_*^2k^2e_{4,\sigma}(\hat n)+\cdots
}
\]

и accumulated fixed-frequency propagation phase

\[
\boxed{
\delta\phi_\sigma
=-\frac12La_*^2
\left(\frac\omega c\right)^3
e_{4,\sigma}(\hat n)+\cdots.
}
\]

Polarization difference:

\[
\boxed{
\Delta\phi_{pol}
=-\frac12La_*^2
\left(\frac\omega c\right)^3
\Delta e_4(\hat n).
}
\]

Вот здесь microscopic graph окончательно превращается в quantity, которую может увидеть detector.

Документ: `TT_TO_REAL_PHYSICS_OBSERVABLES.md`.

---

# Глава 26. Оказывается, для этого эксперимента уже существует язык

Современные gravitational-wave modified-dispersion analyses используют convention

\[
E^2=(pc)^2+A_\alpha(pc)^\alpha.
\]

Наш quartic TT pole попадает **точно** в `alpha=4` class:

\[
\boxed{
A_{4,\sigma}(\hat n)
=\frac{a_*^2}{(\hbar c)^2}
e_{4,\sigma}(\hat n).
}
\]

После scale map

\[
a_*^2=8\pi\lambda_R^{eff}\ell_P^2
\]

получаем

\[
\boxed{
A_{4,\sigma}(\hat n)
=\frac{8\pi\lambda_R^{eff}}{E_P^2}
e_{4,\sigma}(\hat n).
}
\]

То есть внешний bridge не требует изобретать новый detector observable.

Можно использовать:

1. existing `alpha=4` modified-dispersion GW likelihood, но с correlated sky/polarization law;
2. anisotropic/birefringent dimension-6 SME language;
3. direct theory waveform с frozen six-vector.

Документ: `EXTERNAL_GW_BLIND_MATCHING.md`.

---

# Глава 27. У nested cubic model есть собственный рисунок на небе

Если six-vector проходит scalar-cubic submodel,

\[
Q_4^{cub}(\hat n)
=n_x^4+n_y^4+n_z^4-\frac35
\]

имеет exact spherical-harmonic decomposition

\[
\boxed{
Q_4^{cub}
=\frac{4\sqrt\pi}{15}
\left[
Y_{40}
+\sqrt{\frac5{14}}(Y_{44}+Y_{4,-4})
\right].
}
\]

То есть в intrinsic microscopic frame это pure `l=4` cubic multiplet с фиксированным отношением `m=0` и `m=±4`.

Поворот frame на небо меняет Euler angles, но не внутренние ratios.

Это zero-fit angular fingerprint.

Если global frame orientations декогерируют/усредняются при RG, amplitude может исчезнуть — ещё один genuine falsifier, а не проблема, которую разрешено подправить после данных.

---

# Глава 28. Свет читает metric через phase

Independent optical bridge строит balanced interferometric response

\[
\Delta\Phi=\kappa R x,
\qquad
\kappa=\frac{k_\gamma\ell_*}{2},
\]

где `x` — five traceless metric coordinates.

Five-channel response full-rank на этом sector, поэтому covariance tomography имеет form

\[
\boxed{
S_\Phi=\kappa^2RS_hR^T,
}
\]

\[
\boxed{
S_h=\kappa^{-2}R^{-1}S_\Phi R^{-T}.
}
\]

Retarded TT kernel задаёт response/poles.

Noise amplitude дополнительно требует конкретного quantum/statistical state — vacuum, thermal или non-equilibrium. Эти два объекта не смешиваются.

Compact U(1) carrier уже получен кинематически; настоящий photon sector требует отдельного `Z_A` calculation.

---

# Глава 29. Одна абсолютная шкала — и ни одной тайной второй

Microscopic composition equations оставляют ровно одну common action slope:

\[
\boxed{f(n)=sn}.
\]

Regge scale convention:

\[
\boxed{
\lambda_R^{eff}
=\frac{a_*^2}{8\pi\ell_P^2},
}
\]

\[
\boxed{
\frac{a_*}{\ell_P}
=\sqrt{8\pi\lambda_R^{eff}}.
}
\]

HDA не может честно определить эту overall gravitational normalization: это familiar common scale freedom.

Поэтому допустимы только два честных исхода:

```text
A. microscopic principle дополнительно выводит s / lambda_R_eff;
B. один заранее объявленный physical datum калибрует common scale.
```

После этого все остальные directions, frequencies, polarizations и events — predictions, не новые calibrations.

---

# Глава 30. Где сказка сегодня действительно заканчивается

## Что уже закрыто

| Arrow / observable | Status |
|---|---|
| `q+2=2^q -> q=2` | **EXACT** |
| q=2 octahedral `S2` link | **EXACT** |
| canonical recursive PL `M3~S3` | **EXACT / FINITE STABILITY** |
| causal-volume fixed point `d*=3` | **EXACT** |
| `d_H=2.999229782`, `z~0.99828`, history ~4.00439 | **FROZEN NUMERICAL / DERIVED** |
| local shape `(X,Z) -> metric M` | **EXACT** |
| first L1 `E/T2` split = 8.43% relative | **CI** |
| direct `8.43% -> 3 particle masses` | **EXACT NO-GO** |
| exact 32D higher-shell `Lambda` | **CI PASS** |
| geometry-only anisotropy beta = 0 | **EXACT CONTROL** |
| HDA `c=1/2`, `AB=1` in declared ADM family | **STRUCTURAL / EXACT IN ANSATZ** |
| Regge held-out `Z6` | **HELD-OUT PASS** |
| reduced massless TT propagator | **EXACT REDUCED** |
| reduced `P_TT(k)~k^-1` | **EXACT REDUCED** |
| onsite `C6^(0)=aI+bA+cO` | **EXACT SYMMETRY FORM** |
| shared-face nearest transfer = 6 reciprocal `S3` functions | **EXACT SYMMETRY FORM** |
| generic quartic TT S4 quotient dimension = 6 | **EXACT** |
| six-observable full extractor, `detA=1/699840000` | **EXACT** |
| nested `eta/zeta` extractor | **EXACT CONDITIONAL SUBMODEL** |
| nested `4:3:0` birefringence theorem | **EXACT CONDITIONAL SUBMODEL** |
| TT Wilson -> `A4`, phase, velocity, polarization observables | **EXACT OBSERVABLE BRIDGE** |

## Что ещё требует настоящих microscopic numbers

```text
1. complete full-H_E onsite depth-two artifact
2. six canonical shared-face Peter-Weyl transfer amplitudes
3. one next-separation locality control
4. refinement / regulator extrapolation
5. frozen IR six-vector c1...c6
6. one absolute scale if not internally derived
7. blind comparison with real GW data
8. independent U(1) stiffness / real photon phase
9. realistic gauge + chiral matter + Yukawa sector
```

Это уже не туманная фраза «нужно придумать RG theory».

Это конечный список вычислений.

---

# Три дракона, которых нельзя обмануть

### Dragon I — momentum dynamics

Local 8.43% обязан пройти через interblock transfer и derivative expansion. Если anisotropic mass, kinetic residue или leading `k^2` cone survives — gravity physicalization fails.

### Dragon II — regulator/locality

Если six Wilson coefficients не стабилизируются при declared refinement/cutoff sequence, они не являются physical predictions.

### Dragon III — blind data

После freeze microscopic six-vector запрещено удалять неудобный coefficient, менять tensor basis или вводить event-by-event scale только потому, что posterior оказался неудобным.

У природы должно оставаться право сказать `FAIL`.

---

# Основные новые документы physicalization frontier

```text
Q2_DIMENSION3_FIXED_POINT_CLOSURE.md
LOGICAL_SHAPE_METRIC_JACOBIAN.md
L1_Q4_S4_METRIC_COMPRESSION_RESULT.md
S4_MASS_SPLITTING_NO_GO.md
PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md
PL_GALERKIN_ANISOTROPY_NO_FLOW.md
C6_PHYSICAL_KERNEL_CLOSURE.md
S4_TT_QUARTIC_COMPLETE_BASIS.md
NEAREST_BLOCK_S3_TRANSFER_CLOSURE.md
C6_TO_TT_WILSON_COEFFICIENTS.md
TETRAHEDRAL_TT_BIREFRINGENCE_THEOREM.md
TT_TO_REAL_PHYSICS_OBSERVABLES.md
EXTERNAL_GW_BLIND_MATCHING.md
```

---

# Воспроизводимые gates

Canonical core:

```bash
python bcqg_bit_to_gravity_final.py --strict
python bcqg_unified_verification.py
```

Dimension fixed point:

```bash
python scripts/q2_dimension3_fixed_point_gate.py \
  --max-generation 10 \
  --output verification_results/Q2_DIMENSION3_FIXED_POINT.json
```

Shape -> metric:

```bash
python scripts/logical_shape_metric_jacobian_gate.py
```

Full general quartic TT representation theorem:

```bash
python scripts/s4_tt_quartic_complete_basis_gate.py \
  --output verification_results/S4_TT_QUARTIC_COMPLETE_BASIS.json
```

Nearest-block symmetry/moment theorem:

```bash
python scripts/nearest_block_s3_transfer_gate.py
```

Restricted eta/zeta positive control:

```bash
python scripts/c6_tt_wilson_extractor.py
```

Single-Qtet polarization theorem:

```bash
python scripts/tetrahedral_tt_birefringence_gate.py
```

Reduced propagator:

```bash
python scripts/tt_propagator_first_pass.py
python scripts/tt_vacuum_two_point_gate.py
```

---

# Эпилог. Самая сильная корректная формулировка

> **Binary Causal / Information-Graph Quantum Gravity — кандидатная вычислительная архитектура, в которой independently selected `q=2` создаёт octahedral `S2` local link; canonical recursive PL completion является stable 3-manifold; frozen route growth имеет exact causal-volume fixed point `d=3`; independent dynamics даёт `z≈1` и 3+1-like history scaling. SU(2)/Peter–Weyl sector содержит unique collective spin-2 carrier, а logical shape имеет exact map в traceless metric tangent. Первый refined metric shell показывает nonzero 8.43% `E/T2` tetrahedral precursor, но symmetry запрещает напрямую переименовывать его в particle masses или physical `zeta4`. HDA/ADM, Plebanski и Regge branches воспроизводят GR tensor structures в своём заявленном scope; reduced TT propagator massless and has an exact Gaussian `k^-1` equal-time spectrum. Полный nonzero-momentum audit показывает, что general parity-even tetrahedral quartic TT prediction состоит не из произвольно выбранных двух, а из ровно шести Wilson coefficients; для них уже существует exact full-rank `100/110/111/120` extractor. Nearest-block shared-face symmetry сокращает оставшийся microscopic transport до шести reciprocal `S3` amplitudes. После их full-E calculation, locality/refinement extrapolation и freeze six-vector теория напрямую выдаёт two-polarization `alpha=4` gravitational-wave dispersion, phase, delay and birefringence functions, которые можно сравнить blind с существующей GW experimental infrastructure после не более чем одной common absolute-scale calibration.**

Иными словами, современная граница проекта теперь не

```text
"нужно когда-нибудь придумать RG"
```

и не

```text
R_aniso -> zeta4
```

а конкретная конечная машина:

\[
\boxed{
\text{full-E onsite return}
\to
\text{6 shared-face transfer amplitudes}
\to
\text{low-k moment tensor}
\to
(c_1,\ldots,c_6)^{IR}
\to
\{e_{4,1}(\hat n),e_{4,2}(\hat n)\}
\to
\{A_{4,1},A_{4,2},\delta\phi,\Delta\phi_{pol}\}
\to
\text{blind experiment}.
}
\]

Если эта цепочка проходит — у candidate theory появляется первая честная dimensionless gravitational prediction с прямым мостом к данным.

Если нет — именно эта ветка должна быть отвергнута.

Так и заканчивается научная сказка для взрослых: не обещанием, что герой обязательно победит, а экспериментом, которому позволено решить финал.
