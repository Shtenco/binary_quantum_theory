# От бита к пространству, гравитации и свету

## Научная сказка для взрослых учёных детей — с формулами, отрицательными контролями и правом природы сказать «нет»

> **Статус: candidate theory, 17 августа 2026.**
>
> Этот репозиторий не объявляет новую теорию природы доказанной. Он делает более трудную вещь: строит одну длинную вычислимую цепочку от бинарного различия до геометрии, spin-2, HDA/GR, фазы `U(1)`, света и экспериментальных observables — и в каждой главе оставляет природе возможность разрушить сюжет.
>
> Здесь слово **EXACT** означает алгебраический/комбинаторный результат в заявленных предпосылках; **CI** — воспроизводимый finite computation; **HELD-OUT** — число было заморожено до открытия проверочного результата; **CONDITIONAL** — физический вывод при явно указанной дополнительной гипотезе; **OPEN** — мост ещё не закрыт.

---

# Пролог. Представьте Вселенную, у которой сначала нет пространства

Нет координат.

Нет метров.

Нет заранее написанного `x,y,z`.

Нет даже обещания, что измерений будет три.

Есть только различимость: локальное событие может различать несколько независимых бинарных альтернатив.

Мы задаём почти детский вопрос:

> **Сколько бинарных различий может иметь локальная однородная causal cell, если число маршрутов должно совпадать с числом её естественных соседей?**

И внезапно этот вопрос начинает строить геометрию.

Вся история проекта в одной строке:

```text
binary distinction
 -> q=2
 -> S2 local link
 -> recursive S3 spatial phase
 -> exact causal-volume d*=3
 -> d_eff(slice)=d_H/z ~ 3, z ~ 1
 -> 3+1-like history
 -> SU(2) quantum geometry + Hopf U(1) phase
 -> traceless metric spin-2 sector E + T2
 -> Peter-Weyl dynamics
 -> C6(omega,k)=aI+bA+cO
 -> K_TT
 -> eta2_IR, zeta4_IR
 -> light-phase/interferometer observable
 -> blind experiment.
```

Но это только оглавление. Теперь — история по шагам.

---

# Глава 1. Бит обнаруживает, что его должно быть два

**[EXACT]**

Пусть локальное событие содержит `q` независимых бинарных различий. Тогда число route states равно

\[
2^q.
\]

У каждой route-вершины есть `q` Hamming-neighbours плюс два causal poles, поэтому естественная степень равна

\[
q+2.
\]

Локальная однородность требует

\[
q+2=2^q.
\]

Для целых `q>=1` решение единственно:

\[
\boxed{q=2}.
\]

Не `q=3`, потому что `5 != 8`. Не `q=4`, потому что `6 != 16`.

Получаются четыре маршрута

```text
00, 01, 10, 11
```

— квадрат `C4` в Hamming graph.

Это первый момент сказки, где число появляется не как параметр автора, а как решение уравнения.

---

# Глава 2. Четыре маршрута строят сферу вокруг точки

**[EXACT]**

Добавим два causal poles к `C4`. Получится октаэдральный shell:

```text
V = 6
E = 12
F = 8
chi = 2.
```

Это simplicial `S2`.

Почему это важно? Потому что у обычной внутренней вершины трёхмерного PL-manifold link должен быть двумерной сферой:

\[
\operatorname{link}(v)\cong S^2.
\]

То есть локальный бинарный объект неожиданно ведёт себя так, будто вокруг него должно существовать **три** пространственных направления.

Но локальная сфера ещё не означает глобальное пространство. Следующая дверь — gluing.

---

# Глава 3. Локальные сферы учатся жить вместе

**[EXACT / FINITE PL]**

Наиболее экономная minimal+flag globalization q=2 shell — boundary четырёхмерного cross-polytope, 16-cell:

```text
(V,E,F,T) = (8,24,32,16)
Betti     = (1,0,0,1).
```

У неё:

- every vertex link = octahedral `S2`;
- every edge link = `S1`;
- every face link = `S0`;
- каждая triangle принадлежит ровно двум tetrahedra;
- complex orientable;
- `boundary^2=0`;
- homology соответствует `S3`.

Иными словами,

\[
\boxed{M^3\cong S^3}
\]

в canonical completion.

При barycentric refinement:

```text
16 -> 384 -> 9216 tetrahedra
```

manifold links сохраняются.

**Важная граница:** это existence/stability theorem для canonical PL completion, а не доказательство того, что голый causal graph единственным образом принуждает именно такое глобальное склеивание.

Документ: `GLOBAL_MANIFOLD_Q2_COMPLETION.md`.

---

# Глава 4. Лестница размерности и место, где она действительно останавливается

Это та линия, которая раньше выглядела как красивый numerical gradient:

```text
2.662965
 -> 2.951745
 -> 2.993853
 -> 2.999229782
 -> 2.999903694
 -> 2.999987961
 -> ...
```

Теперь её можно закрыть аналитически.

## 4.1 Frozen q=2 rewrite

**[EXACT]**

После независимого выбора `q=2` число route midpoints

\[
B=2^q=4.
\]

Каждый active causal edge в следующем поколении создаёт

\[
2B=8
\]

active child edges.

А causal linear scale удваивается:

\[
L_{g+1}=2L_g.
\]

Число вершин после `g` generations:

\[
N_g
=2+B\frac{(2B)^g-1}{2B-1}.
\]

Для `q=2`:

\[
\boxed{N_g=\frac{4\,8^g+10}{7}}.
\]

Определим finite-step causal-volume dimension

\[
d_g=\log_2\frac{N_g}{N_{g-1}}.
\]

Тогда точно

\[
\boxed{
d_g
=3+\log_2\left(1-\frac{35}{16\,8^{g-1}+40}\right).
}
\]

Отсюда следует сразу три вещи:

\[
d_g<3,
\]

\[
d_{g+1}>d_g,
\]

и

\[
\boxed{\lim_{g\to\infty}d_g=\log_2 8=3}.
\]

То есть `2.999229782` — не случайное попадание около тройки. Это `g=5` точной последовательности, сходящейся к `3` снизу.

Документ: `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md`.

Executable gate: `scripts/q2_dimension3_fixed_point_gate.py`.

## 4.2 Почему мы всё равно не называем один exponent окончательной размерностью

Потому что хороший научный сюжет любит независимых свидетелей.

У нас есть три разных свидетеля:

1. **topology:** `S2` vertex link и canonical PL `M3`;
2. **causal-volume scaling:** exact `d_* = 3`;
3. **diffusion/dynamics:** frozen `d_H` и `z` дают
   \[
   \boxed{d_{eff}^{slice}\equiv d_H/z=3.004393867}.
   \]

Здесь важно не перепутать обозначения. В frozen code число `3.004393867` **уже содержит деление на `z`** и исторически называлось `ds_slice_holdout`.

Отдельно

\[
\boxed{d_H=2.999229782139151},
\qquad
\boxed{z\simeq0.998281156}.
\]

Так что сильная формулировка теперь:

\[
\boxed{
D_{topo}=3,
\qquad
d_{causal-volume}\to3,
\qquad
d_H/z\simeq3.00439,
\qquad z\simeq1.
}
\]

Это гораздо труднее случайно получить одним и тем же fitting bias.

---

# Глава 5. От трёх пространственных направлений к истории 3+1

**[NUMERICAL / STRUCTURAL]**

Для scaling kernel

\[
K(\omega,k)\sim\omega^2+|k|^{2z}
\]

обычная continuum запись history exponent имеет вид

\[
d_{eff}^{history}=1+\frac{D}{z},
\]

где `D` — spatial volume/Hausdorff exponent.

В frozen route code роль `D` играет `d_H`, поэтому

\[
\boxed{
d_{eff}^{history}
=1+\frac{d_H}{z}
=1+d_{eff}^{slice}
\simeq4.004393867.
}
\]

Иными словами, число `3.004393867` нельзя делить на `z` второй раз: это был бы двойной учёт dynamical exponent.

Смысл не в том, что «мы добавили единицу потому что хотели 4».

Смысл в независимом требовании:

```text
spatial topology -> 3
causal-volume fixed point -> 3
z -> 1
causal history -> 3+1-like scaling.
```

В `HODGE_DIMENSION_SELECTOR.md` и `TWO_FORM_DIMENSION_PRINCIPLE.md` есть ещё два conditional structural explanations, почему `3+1` особенно естественно:

- на spatial slice Hodge closure `C1 <-> C2` выбирает `D=3`;
- в spacetime `B` и curvature `F` являются 2-forms, а metric-free `B wedge F` и `B wedge B` — top forms именно при `d=4`.

Эти аргументы — **selectors**, а не замена independent dimension measurements.

---

# Глава 6. Геометрия учится становиться гладкой

**[CI / COARSE-GRAINING]**

Observer blocking даёт

```text
delta g       ~ b^-2.001707
grad(delta g) ~ b^-3.001458
delta R       ~ b^-4.000524
simplicity    ~ b^-1.994838
Urbantke g    ~ b^-2.019746.
```

Это означает: coarse observer видит уменьшающиеся metric/curvature defects.

Но здесь проект однажды почти попался в красивую ловушку. Из smoothing exponent было соблазнительно вывести foam spectrum

```text
P(k) ~ k^+1.003414.
```

Позже прямой TT calculation показал, что это **не Gaussian TT vacuum spectrum**.

И это важная часть истории: хорошая теория должна уметь исправлять собственные красивые интерпретации.

---

# Глава 7. Qubit открывает сразу две двери: SU(2) и U(1)

Здесь бинарность перестаёт быть только graph label.

Нормированный двухкомпонентный quantum state живёт на

\[
S^3\subset\mathbb C^2.
\]

Но physical ray не замечает overall phase:

\[
|\psi\rangle\sim e^{i\lambda}|\psi\rangle.
\]

Поэтому

\[
\boxed{\mathbb{CP}^1\cong S^2}
\]

и возникает Hopf fibration

\[
\boxed{U(1)\longrightarrow S^3\longrightarrow S^2}.
\]

Один и тот же `q=2` carrier имеет две естественные стороны:

```text
SU(2) / Bloch geometry -> shape, flux, intertwiners
U(1) phase fiber       -> Pancharatnam/Berry connection.
```

Для соседних rays канонический link phase

\[
\boxed{
U_{vw}
=\frac{\langle\psi_v|\psi_w\rangle}
{|\langle\psi_v|\psi_w\rangle|}
}
\]

преобразуется как lattice `U(1)` connection, а plaquette product даёт gauge-invariant Berry holonomy.

**[EXACT KINEMATIC]** compact `U(1)` carrier получен.

**[OPEN DYNAMIC]** propagating photon требует показать deconfined Maxwell phase и вычислить gauge stiffness.

Документ: `Q2_PANCHARATNAM_U1_LIGHT_BRIDGE.md`.

---

# Глава 8. Четыре spin-1/2 qubits прячут единственный spin-2

**[EXACT REPRESENTATION THEORY]**

\[
(1/2)^4
=2\times j=0+3\times j=1+1\times j=2.
\]

То есть в 16-dimensional Hilbert space находится **ровно один** `j=2` irrep.

В continuum massless TT reduction остаются две helicity:

```text
+2
-2.
```

Это не означает, что четыре qubits «являются гравитоном». Это означает более аккуратную вещь: microscopic carrier содержит единственный collective spin-2 representation sector, который может быть сопоставлен TT degrees of freedom после geometric bridge.

---

# Глава 9. Shape превращается в настоящий metric tangent

**[EXACT LOCAL BRIDGE]**

В logical singlet sector Pauli directions имеют разный geometric смысл:

```text
X, Z -> intrinsic shape
Y    -> orientation pseudoscalar.
```

Для regular tetrahedron background

\[
g_0=
\begin{pmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{pmatrix}.
\]

Из face-flux Gram geometry получены exact Jacobian matrices

\[
M_X=\frac{\partial g}{\partial X},
\qquad
M_Z=\frac{\partial g}{\partial Z}.
\]

И они удовлетворяют

\[
\boxed{\operatorname{Tr}(g_0^{-1}M_A)=0},
\]

\[
\boxed{
\operatorname{Tr}(g_0^{-1}M_Ag_0^{-1}M_B)
=\frac32\delta_{AB}.
}
\]

Значит `(X,Z)` — ортогональный equal-norm **trace-free metric tangent**.

Это закрывает прежнюю абстрактную стрелку

```text
logical shape -> ??? -> metric
```

и заменяет её оператором `M`.

Документ: `LOGICAL_SHAPE_METRIC_JACOBIAN.md`.

---

# Глава 10. Пять metric modes встречают тетраэдральную анизотропию 8.43%

**[CI, EXACT S4 REDUCTION]**

На первом refined L1 shell 24 barycentric chambers сжимаются canonical map в шесть parent-edge observables:

\[
24\longrightarrow6.
\]

Под `S4`

\[
\boxed{6=A_1\oplus E\oplus T_2}.
\]

`A1` — trace. Пять traceless metric degrees:

\[
\boxed{5=E\oplus T_2}.
\]

Exact CI-compressed kernel имеет всего три orbit coefficients:

\[
K_6=aI+bA_{adj}+cO_{opp},
\]

где

```text
a = 1.0220278507464782
b = -0.044581968405997735
c = 0.
```

Отсюда

\[
\lambda_E=a-2b+c=1.1111917875584736,
\]

\[
\lambda_{T_2}=a-c=1.0220278507464782,
\]

и

\[
\boxed{\Delta_{ET}=0.08916393681199541}.
\]

Dimension-weighted isotropic stiffness

\[
\kappa_{iso}
=\frac{2\lambda_E+3\lambda_{T_2}}5
=1.0576934254712764.
\]

Поэтому

\[
\boxed{
\mathcal A_{tet}^{UV}
=\frac{\Delta_{ET}}{\kappa_{iso}}
=0.08430036026012608.
}
\]

Именно отсюда появляется знаменитое **8.43%**.

Но теперь мы знаем, что это значит математически.

Уникальный tetrahedral symmetry-breaking operator на traceless spin-2 space:

\[
\boxed{
Q_{tet}
=\frac35P_E-\frac25P_{T_2}
=\frac{4O_{opp}-A_{adj}}{10}.
}
\]

Следовательно

\[
\boxed{
K_5
=\kappa_{iso}P_5
+\Delta_{ET}Q_{tet}.
}
\]

Это **реальная microscopic metric anisotropy**, но пока ещё не physical `zeta4`.

Документ: `L1_Q4_S4_METRIC_COMPRESSION_RESULT.md`.

---

# Глава 11. Почему 8.43% не разрешено сразу превращать в массы частиц

**[EXACT NO-GO]**

Здесь сказка специально отказывается от лёгкого чуда.

У `Q_tet` только два eigenvalues:

\[
+\frac35\quad\text{на }E,
\qquad
-\frac25\quad\text{на }T_2.
\]

Если три поколения matter field образуют один irreducible `S4` triplet `T2`, то любой `S4`-invariant mass operator должен коммутировать со всеми matrices representation.

По лемме Шура

\[
\boxed{M=mI_3}.
\]

А внутри `T2`

\[
Q_{tet}|_{T_2}=-\frac25I_3.
\]

Следовательно один scalar coefficient `0.08430036...` **не может расщепить три поколения**.

Это закрывает неправильный shortcut:

```text
8.43% -> electron/muon/tau masses        NO.
```

Правильная будущая цепочка:

```text
microscopic algebra
 -> gauge group
 -> chiral matter irreps
 -> generation representation
 -> derived S4-breaking / Higgs / Yukawa spurions
 -> frozen Yukawa matrix
 -> eigenvalue ratios
 -> blind particle-mass comparison.
```

8.43% может позже войти как **geometric spurion normalization**, но только если соответствующий nontrivial flavor operator будет независимо выведен до просмотра масс.

Отдельный no-go: higher-shell `Lambda` spectrum имеет dynamic range лишь

\[
\lambda_{max}/\lambda_{min}\simeq1.416,
\]

поэтому прямые `m_i proportional lambda_i` или `sqrt(lambda_i)` также не объясняют charged-lepton hierarchy.

Документ: `S4_MASS_SPLITTING_NO_GO.md`.

Это не проигрыш. Это момент, где теория отказалась от нумерологии и сузила настоящий matter bottleneck.

---

# Глава 12. Peter–Weyl Hamiltonian идёт на второй shell

**[CI PASS]**

Из spin parity

\[
P H_EP=0.
\]

Первый return:

\[
K=PH_E^2P.
\]

Следующий denominator-free shell observable:

\[
\boxed{
\Lambda
=K^{-1/2}
\left(PH_E^4P-K^2\right)
K^{-1/2}.
}
\]

Полный 32-column calculation завершён.

```text
rank(K) = 32
lambda_min(K) = 4.306075987001578
lambda_max(K) = 13.352781352746604
cond(K) = 3.100916331493829
```

Для `Lambda`:

```text
lambda_min = 10.635759878291307
lambda_max = 15.059927665966466
mean       = 12.860443113390883
std        = 1.21953176104
max/min    = 1.4159710108447772
relative distance to scalar I = 0.09440461833276048.
```

Pair trace содержит

```text
J_shape  = -0.3629900150598623
J_orient = +0.7912767588958898
Delta    = +1.1542667739557522.
```

То есть higher shell не схлопывается в identity.

Block-Lanczos reconstruction даёт

\[
B_1^\dagger B_1=K,
\qquad
B_2^\dagger B_2=\Lambda
\]

с errors порядка `1e-13`.

Это открывает естественный resolvent continued fraction и превращает «следующий shell» в путь к propagator, а не в коллекцию отдельных matrices.

Документ: `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md`.

---

# Глава 13. Geometry-only RG оказывается слишком честным: он ничего не исправляет

**[EXACT FINITE PL]**

Для actual recursive 16-cell barycentric geometry

\[
\boxed{P^TL_{g+1}P=\frac14L_g}
\]

с residual порядка `2.2e-16`.

Если internal kernel separable от geometry, все couplings получают один и тот же factor `1/4`.

Поэтому ratio anisotropy не течёт:

\[
R_{aniso}'=R_{aniso}.
\]

Это важный no-go:

> **простое усреднение пространства не может magically восстановить rotational invariance.**

Нетривиальный flow обязан идти из Peter–Weyl recoupling / nonseparable block dynamics.

Документ: `PL_GALERKIN_ANISOTROPY_NO_FLOW.md`.

---

# Глава 14. Настоящий bottleneck теперь помещается в одну строку

Старый shorthand

```text
R_aniso -> zeta4
```

больше не используется.

Правильная цепочка:

\[
\boxed{
\text{Peter--Weyl}
\to\Gamma_{metric}^{E,T_2}(\omega,k)
\to\Delta_{ET}(\omega,k)
\to K_{TT}(\omega,k)
\to\{\eta_2^{IR},\zeta_4^{IR}\}.
}
\]

Local shape→metric Jacobian `M` уже выведен.

`S4` projectors уже выведены.

Первый refined `E/T2` split уже измерен.

Поэтому сложный six-by-six effective kernel имеет всего три independent orbit functions:

\[
\boxed{
C_6(\omega,k)
=a(\omega,k)I
+b(\omega,k)A
+c(\omega,k)O.
}
\]

И сразу

\[
\boxed{\lambda_E=a-2b+c},
\]

\[
\boxed{\lambda_{T_2}=a-c},
\]

\[
\boxed{\Delta_{ET}=2(c-b)}.
\]

Это ключевое сжатие задачи: вместо generic matrix fitting — три symmetry orbit amplitudes.

Полный depth-two `H_E` workflow считает непосредственно

\[
|u_e\rangle
=\frac12\sum_{c\to e}H_c|\Omega\rangle,
\]

\[
|v_e\rangle
=H_B|u_e\rangle,
\qquad H_B=\sum_{w=1}^{24}H_w,
\]

а затем

\[
K=\langle u|u\rangle,
\quad
A=\langle u|H_Bu\rangle,
\quad
B=\langle H_Bu|H_Bu\rangle.
\]

Три representatives `same/adjacent/opposite` достаточны для восстановления всего `S4` kernel.

**На момент этого README final depth-two numbers не объявляются**, пока workflow artifact не прошёл gate. Это сознательно: queued/in-progress вычисление не превращается в PASS силой литературного стиля.

---

# Глава 15. TT propagator: где гравитация впервые начинает распространяться

**[EXACT REDUCED MODEL]**

Reduced causal transfer имеет pole

\[
\boxed{
4\sin^2\frac\omega2
=r^2\sum_i4\sin^2\frac{k_i}{2},
\qquad r=\frac1{\sqrt3}.
}
\]

Для двух TT polarizations

\[
\boxed{
G^{TT}_{AB}(\omega,\mathbf k)
=\frac{\delta_{AB}}
{Z_T\left[
4\sin^2(\omega/2)
-r^2\sum_i4\sin^2(k_i/2)+i0
\right]}.
}
\]

В этом reduced sector

\[
\boxed{m_g=0}.
\]

Это ещё не final interacting Peter–Weyl/history propagator, но это explicit connected propagator с massless pole.

---

# Глава 16. Старый красивый spectrum проигрывает прямому calculation

Equal-time covariance reduced TT vacuum:

\[
C(\mathbf k)
=\frac1{Z_T\Omega_{\mathbf k}\sqrt{\Omega_{\mathbf k}^2+4}},
\]

\[
\Omega_{\mathbf k}^2
=r^2\sum_i4\sin^2\frac{k_i}{2}.
\]

При `k -> 0`

\[
\boxed{C(k)\sim\frac1{2Z_Tr|k|}},
\]

поэтому

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

Numerical slope:

```text
-1.000000148
```

а direct frequency integration совпадает с closed form до relative error ниже `2.1e-16`.

Значит старое

```text
smoothing exponent -> k^+1.003414 quantum vacuum
```

было неверной физической интерпретацией.

Оно сохраняется только как observer self-averaging law, не как TT vacuum prediction.

---

# Глава 17. Первые dispersion coefficients появляются — но пока bare

Small-momentum expansion:

\[
\omega^2
=r^2k^2
+\frac{r^2}{12}
\left[r^2(k^2)^2-\sum_i k_i^4\right]
+O(k^6).
\]

Для directions:

| direction | bare coefficient |
|---|---:|
| `(100)` | `-1/18` |
| `(110)` | `-1/72` |
| `(111)` | `0` |

Разложение на isotropic и cubic invariants даёт

\[
\boxed{\eta_{2,bare}^{iso}=-1/45},
\]

\[
\boxed{\zeta_{4,bare}^{cub}=-1/12}.
\]

Но физическое предсказание требует renormalized numbers:

\[
\boxed{\eta_2^{IR},\qquad\zeta_4^{IR}}.
\]

Если leading `E/T2` anisotropy не исчезнет к IR, theory fails known Lorentz/isotropy phenomenology. Поэтому допустимый healthy scenario:

\[
\Delta_{ET}(k)=O(a_*^2k^4)
\]

или быстрее, а не finite correction к leading `k^2` cone.

---

# Глава 18. HDA спрашивает у Hamiltonian: «Ты действительно гравитация?»

**[STRUCTURAL / FINITE CERTIFICATES]**

Целевая algebra:

\[
[\hat H[N],\hat H[M]]
\to
i\hbar\hat D[\sharp(NdM-MdN)].
\]

Route-normal sector независимо строит `sharp(NdM-MdN)` через cochain/Hodge/flux map.

В frozen habitat:

```text
C_cross / D = O(epsilon)
C_GG    / D = O(epsilon^2).
```

То есть

\[
\boxed{
\Delta_{full}
\le
\Delta_{route}
+C_1\epsilon
+C_2\epsilon^2
\to0
}
\]

в заявленном fixed-cutoff scope.

Для simultaneous cutoff growth существует conservative admissible family

\[
\boxed{J_{max}=o(\epsilon^{-2/13})}.
\]

Uniform theorem для произвольного joint path остаётся open.

---

# Глава 19. HDA выбирает форму GR, но не печатает Newton constant на бумаге

Для ADM-family

\[
H_{A,B,c,\Lambda}[N]
=\int N\left[
A\frac{\pi_{ab}\pi^{ab}-c\pi^2}{\sqrt q}
-B\sqrt q(R-2\Lambda)
\right]
\]

closure выбирает

\[
\boxed{c=\frac12},
\qquad
\boxed{AB=1}.
\]

То есть DeWitt trace structure и kinetic/curvature relative normalization фиксируются.

Но общий gravitational normalization и vacuum term остаются:

\[
\boxed{G,\qquad\Lambda}.
\]

Это не баг HDA. Algebra constraints не обязана определять overall action unit.

---

# Глава 20. Один свободный slope вместо кладбища fitting parameters

Microscopic phase-composition system при `M=8`:

```text
shape   = 184 x 16
rank    = 15
nullity = 1.
```

Единственное null direction:

\[
\boxed{f(n)=sn}.
\]

Slopes `0.1`, `0.5`, `1`, `sqrt(2)`, `pi` проходят composition residual ниже `1e-14`.

Значит структура phase law фиксирована, но остаётся одна overall action normalization.

Regge scale map:

\[
\boxed{
\lambda_R^{eff}=\frac{a_*^2}{8\pi\ell_P^2}
}
\]

и

\[
\boxed{
\frac{a_*}{\ell_P}=\sqrt{8\pi\lambda_R^{eff}}.
}
\]

Это одна scale-setting проблема, а не десятки скрытых knobs.

---

# Глава 21. Regge делает предсказание до того, как увидит ответ

**[HELD-OUT PASS]**

Для TT residue

\[
Z_L=c_1(L)/L^4
\]

из `L=3,4,5` был frozen ansatz

\[
Z_L=\frac18+\frac{C}{L^2}+\frac{D}{L^4}.
\]

До открытия `L=6`:

```text
Z6_pred = 0.11876923193907167.
```

После independent computation:

```text
Z6_obs  = 0.11876075461190198.
```

Relative error:

\[
\boxed{0.00714\%}.
\]

Позже held-out `L=9,10` Regge families также дали `8/8` preregistered observables внутри PASS band, все prediction errors of defects ниже `0.5%`.

Эта глава важна не только числом: она показывает protocol, который должен использоваться для будущей внешней physics prediction.

---

# Глава 22. Два независимых пути снова находят Einstein structure

Первая ветвь:

```text
B-field
 -> simplicity
 -> Urbantke metric
 -> compatible connection
 -> curvature
 -> Einstein criterion.
```

Вторая:

```text
metric
 -> Regge Hessian
 -> Fierz-Pauli
 -> Einstein-Hilbert cubic
 -> nonlinear Ward restoration.
```

На full unprojected metric Hessian continuum ratios идут к Fierz–Pauli target

\[
(1,-2,2,-1)
\]

с leading errors примерно `O(L^-2)`.

Directional differences между lattice orientations тоже падают примерно квадратично — независимый precursor того, что rotational lattice anisotropy является irrelevant deformation.

Это особенно важно рядом с нашим `8.43%`: finite microscopic anisotropy не обязана быть IR anisotropy.

---

# Глава 23. Свет появляется не как лампочка, а как фаза

Simplicial `U(1)` kinematics даёт

\[
F=d_1A,
\qquad
A\to A+d_0\lambda,
\]

и

\[
d_1d_0=0.
\]

Quadratic gauge action имеет Maxwell form

\[
S_A=\frac{Z_A}{4}\int F_{\mu\nu}F^{\mu\nu}.
\]

Kinematic Hopf/Pancharatnam bridge объясняет, почему compact phase connection естественна уже в q=2 state space.

Но пока не вычислен `Z_A` из microscopic phase dynamics, нельзя объявлять численное значение fine-structure constant.

Если minimal Wilson charge нормирован как `1`, то после canonical normalization

\[
\boxed{e=\frac1{\sqrt{Z_A}}},
\]

и

\[
\boxed{\alpha=\frac1{4\pi Z_A}}.
\]

Так что задача «получить 137» сведена не к поиску красивой комбинации integers, а к одному честному microscopic stiffness calculation.

Документы: `Q2_PANCHARATNAM_U1_LIGHT_BRIDGE.md`, `CONSTANTS_ZERO_FIT_LEDGER.md`.

---

# Глава 24. Интерферометр превращает metric fluctuation в число на экране

Пусть шесть tetrahedral optical arms измеряют fractional squared-length perturbations `y_e`.

Linear map

\[
y=Jh
\]

имеет full rank на symmetric metric sector, а balanced combinations удаляют только common trace.

Таким образом пять traceless metric modes `E+T2` имеют оптические readout channels.

Для света

\[
k_\gamma=\frac{2\pi}{\lambda},
\]

а phase shift вдоль arm

\[
\boxed{
\delta\phi_e
=k_\gamma\delta\ell_e.
}
\]

Для двух paths

\[
P_\pm
=\frac{1\pm\cos\Delta\phi}{2}.
\]

Если phase сама квантово флуктуирует,

\[
V=
\left|\left\langle e^{i\Delta\hat\phi}\right\rangle\right|,
\]

а для Gaussian fluctuations

\[
\boxed{V=e^{-\frac12\operatorname{Var}(\Delta\phi)}}.
\]

То есть microscopic geometry получает прямую дорогу к visibility interferometer fringes.

---

# Глава 25. Самый чистый оптический observable почти ничего не знает об абсолютных единицах

Exact optical gains для irreps:

\[
g_E^2=\frac12,
\qquad
g_{T_2}^2=1.
\]

Определим power per mode `S_E` и `S_T2`. Тогда

\[
\boxed{
\mathcal R_\gamma(\omega)
=\frac{S_E/g_E^2}{S_{T_2}/g_{T_2}^2}
=2\frac{S_E}{S_{T_2}}.
}
\]

В этом ratio сокращаются common arm scale, common optical gain, laser power и общая amplitude normalization metric noise.

Если rotational symmetry восстанавливается:

\[
\boxed{\mathcal R_\gamma\to1}.
\]

Если остаётся tetrahedral IR fixed point:

\[
\mathcal R_\gamma\to R_*\ne1.
\]

Вот здесь научная сказка впервые превращается в очень обычный лабораторный вопрос: **совпадут ли spectra двух symmetry channels?**

---

# Глава 26. Что значит «сначала свет, потом информация»

Есть два разных смысла слова «информация».

Если информация — это фундаментальная различимость, то цепочка идёт

\[
\boxed{
\text{distinction}
\to q=2
\to \text{quantum ray}
\to U(1)\ \text{phase}
\to \text{light-like gauge propagation}.
}
\]

То есть различимость логически раньше света.

Но если информация — **классическая запись наблюдателя**, то действительно:

\[
\boxed{
\text{coherent phase}
\to \text{propagation}
\to \text{interference}
\to \text{measurement}
\to \text{classical information}.
}
\]

Поэтическая, но физически аккуратная версия:

> **Различимость родила фазу. Фаза получила возможность распространяться. Интерференция сделала различимость наблюдаемой информацией.**

---

# Глава 27. Что теория сегодня уже предсказывает, а что ещё только обещает вычислить

| Quantity | Status |
|---|---|
| `q=2` | **EXACT** binary selector |
| local octahedral `S2` | **EXACT** |
| canonical minimal flag `S3` PL completion | **EXACT/FINITE** in declared semantics |
| causal-volume fixed point `d*=3` | **EXACT** for frozen q=2 rewrite |
| held-out `d_H=2.999229782...` | **EXACT finite step of closed sequence** |
| `d_eff(slice)=d_H/z=3.004393867` | **CI / derived from frozen scaling** |
| `z=0.998281156` | **CI / frozen** |
| `d_eff(history)=1+d_H/z=4.004393867` | **derived / numerical** |
| smoothing exponents | **CI** |
| unique collective `j=2` | **EXACT** representation theory |
| local shape→metric `M` | **EXACT** |
| `6=A1+E+T2` metric reduction | **EXACT symmetry + CI amplitudes** |
| UV metric anisotropy `0.08430036026` | **CI** |
| exact 32D higher-shell `Lambda` | **CI PASS** |
| Regge `Z_TT -> 1/8` / held-out L6 | **HELD-OUT PASS** |
| reduced `m_g=0` | **EXACT in reduced kernel** |
| reduced `P_TT(k)~k^-1` | **EXACT in reduced Gaussian kernel** |
| `eta2_bare=-1/45` | **EXACT reduced bare** |
| `zeta4_bare=-1/12` | **EXACT reduced bare** |
| full `C6(omega,k)` depth-two values | **COMPUTING / not frozen yet** |
| `eta2_IR`, `zeta4_IR` | **OPEN physical prediction** |
| `R_gamma(omega)` microscopic curve | **OPEN after full RG** |
| `G` | one overall gravitational scale normalization |
| cosmological `Lambda` | **OPEN relevant coupling** |
| compact q=2 `U(1)` carrier | **EXACT kinematic** |
| deconfined photon/Maxwell phase | **CONDITIONAL / dynamic gate** |
| `Z_A -> alpha` | **OPEN microscopic stiffness** |
| realistic gauge group | **OPEN** |
| three generations | **OPEN** |
| Yukawa matrices | **OPEN** |
| particle mass ratios | **OPEN**; direct 8.43% shortcut ruled out |

---

# Глава 28. Три дракона, которых теория обязана победить — или погибнуть

## Dragon A: rotational restoration

Если

\[
\lim_{k\to0}\Delta_{ET}(k)\ne0
\]

в leading `k^2` cone, physical branch fails.

Healthy outcome requires leading anisotropy to disappear and, at most, a suppressed irrelevant quartic tensor remain:

\[
\omega^2
=c_T^2k^2
+c_T^2a_*^2k^4
\left[
\eta_2^{IR}
+\zeta_4^{IR}
\left(\sum_i\hat k_i^4-\frac35\right)
\right]
+\cdots.
\]

## Dragon B: gauge stiffness

Hopf `U(1)` is kinematic. A real photon candidate needs a stable deconfined Maxwell phase and a microscopic calculation of `Z_A`.

## Dragon C: matter hierarchy

Neither `Lambda` eigenvalues nor scalar 8.43% anisotropy can be renamed particle masses. A real result requires derived matter irreps, symmetry breaking and frozen Yukawa matrix before experimental comparison.

---

# Глава 29. Mirror/orientation branch — другая сказка в той же библиотеке

Logical orientation operator obeys schematically

\[
Q\propto Y_L.
\]

Complex conjugation preserves intrinsic metric directions but flips orientation:

```text
X -> X
Z -> Z
Y -> -Y
Q -> -Q.
```

Поэтому

```text
mirror orientation != negative gravitational mass.
```

На dual 16-cell graph `Q4` существует staggered mirror-order channel. Finite 16-qubit gates показывают ordered и disordered regimes, а healthy continuum extension допускает positive-kinetic orientation-dependent mediator.

Это отдельная conditional phenomenology branch. Она не используется для подгонки TT prediction и не заменяет matter derivation.

---

# Глава 30. Правило, которое защищает эту сказку от превращения в миф

Перед внешним comparison должны быть заморожены:

```text
microscopic commit SHA
operator ordering
regulator sequence
blocking prescription
momentum directions
fit window
c_TT(b)
eta2_iso(b)
zeta4_cub(b)
continuum extrapolation
finite-size/RG uncertainty
scale calibration rule
external observable
PASS / TENSION / FAIL criterion.
```

После открытия external posterior запрещено менять microscopic coefficient потому, что эксперимент оказался неудобным.

Это уже было проверено на held-out Regge continuation. Тот же protocol обязателен для настоящего dimensionless physical prediction.

---

# Каноническая цепочка 2026-08-17

```text
BIT / DISTINCTION
  |
  v
q+2 = 2^q
  |
  +--> q=2 ------------------------------------+
  |                                            |
  v                                            v
C4 routes                                  normalized C^2 state
  |                                            |
  v                                            +--> SU(2) geometry
Octahedral S2 link                            |
  |                                            +--> Hopf U(1) phase
  v
canonical PL S3
  |
  +--> exact causal-volume d* = log2(8) = 3
  +--> d_H/z ~ 3.00439 with z ~ 1
  +--> history 1+d_H/z ~ 4.00439
  |
  v
3+1-like smooth history
  |
  v
face qubits / B-field / Peter-Weyl SU(2)
  |
  v
logical shape (X,Z)
  |
  v
exact shape-to-metric Jacobian M
  |
  v
six edge metric carrier = A1 + E + T2
  |
  +--> UV Delta_ET/kappa_iso = 0.08430036026
  |
  v
Peter-Weyl shell recursion
  |
  v
Gamma_metric^(E,T2)(omega,k)
  |
  v
C6(omega,k)=aI+bA+cO
  |
  +--> lambda_E=a-2b+c
  +--> lambda_T2=a-c
  +--> Delta_ET=2(c-b)
  |
  v
TT projection
  |
  v
eta2_IR , zeta4_IR
  |
  +--> gravitational propagation
  +--> optical E/T2 phase readout
  |
  v
R_gamma(omega)=2 S_E/S_T2
  |
  v
PREREGISTERED BLIND EXPERIMENT.
```

---

# Основные документы — карта библиотеки

## От бита к размерности

- `BINARY_TO_GEOMETRY_GATE.md` — dimension-blind negative control для minimal diamond;
- `GLOBAL_MANIFOLD_Q2_COMPLETION.md` — canonical global PL completion;
- `MANIFOLD_DIMENSION_GATE.md` — coordinate-free local link dimension test;
- `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md` — exact q=2 causal-volume fixed point `d*=3`;
- `HODGE_DIMENSION_SELECTOR.md` — conditional edge/face Hodge selector;
- `TWO_FORM_DIMENSION_PRINCIPLE.md` — conditional 2-form `d=4` spacetime selector;
- `OBSERVER_SCALE_SMOOTHING.md` — coarse observer smoothing.

## Quantum geometry / gravity

- `SPATIAL_QUBIT_GEOMETRY_BRIDGE.md`;
- `FACE_QUBIT_BFIELD.md`;
- `PLEBANSKI_URBANTKE_BRIDGE.md`;
- `PLEBANSKI_CONNECTION_EINSTEIN_GATE.md`;
- `REGGE_EH_CUBIC_BRIDGE.md`;
- `GRAVITY_BRIDGE_SCALING.md`;
- `ADM_HDA_PARAMETER_SELECTION.md`;
- `LORENTZIAN_BETA_CANCELLATION.md`;
- `ALL_ARROWS_GRAVITY_CERTIFICATE.md`;
- `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md`.

## Physicalization / TT / RG

- `PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md`;
- `PHYSICALIZATION_PASS_01_RESULTS.md`;
- `TT_PROPAGATOR_FIRST_PASS.md`;
- `TT_VACUUM_TWO_POINT_RESULT.md`;
- `TT_REGGE_ZT_L6_PREREGISTRATION.md`;
- `TT_REGGE_ZT_L6_RESULT.md`;
- `HELDOUT_L9_L10_PREREGISTRATION.md`;
- `HELDOUT_L9_L10_RESULTS.md`;
- `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md`;
- `PETER_WEYL_HIGHER_SHELL_S4_RG_SEED.md`;
- `LOGICAL_SHAPE_METRIC_JACOBIAN.md`;
- `LOGICAL_SHAPE_TO_TT_RG_BRIDGE.md`;
- `L1_Q4_S4_METRIC_COMPRESSION_RESULT.md`;
- `PL_GALERKIN_ANISOTROPY_NO_FLOW.md`;
- `PETER_WEYL_J1_INTERNAL_RG_PREREGISTRATION.md`;
- `TT_RG_PHYSICAL_PREDICTION_PREREGISTRATION.md`.

## Light / constants / matter frontier

- `Q2_PANCHARATNAM_U1_LIGHT_BRIDGE.md`;
- `PHYSICAL_CLOSURE_GRAVITY_LIGHT_CONSTANTS.md`;
- `CONSTANTS_ZERO_FIT_LEDGER.md`;
- `S4_MASS_SPLITTING_NO_GO.md`;
- `MIRROR_WILSON_MATTER.md`;
- `MIRROR_CHIRALITY_GRAVITY.md`.

## Canonical status

- `THEORY_STATUS.md` — human-readable ledger;
- `theory_gates.json` — machine-readable gate ledger;
- `OPEN_PROBLEMS.md` — unresolved obligations.

---

# Воспроизводимость: несколько дверей в лабораторию

Exact q=2 dimension-three fixed point:

```bash
python scripts/q2_dimension3_fixed_point_gate.py \
  --max-generation 10 \
  --output verification_results/Q2_DIMENSION3_FIXED_POINT.json
```

Canonical architecture:

```bash
python bcqg_bit_to_gravity_final.py --strict
```

Unified verification:

```bash
python bcqg_unified_verification.py
```

Global PL manifold:

```bash
python bcqg_global_manifold_gate.py
```

Reduced TT propagator:

```bash
python scripts/tt_propagator_first_pass.py
```

Reduced TT vacuum:

```bash
python scripts/tt_vacuum_two_point_gate.py
```

Regge held-out L6:

```bash
python scripts/tt_regge_zt_l6_gate.py
```

Higher-shell Peter–Weyl column:

```bash
python scripts/peter_weyl_higher_shell_lambda_gate.py \
  --column 0 \
  --output verification_results/columns/column_0.json
```

Higher-shell assembly after all 32 columns:

```bash
python scripts/peter_weyl_higher_shell_lambda_gate.py \
  --assemble-dir verification_results/columns \
  --output verification_results/PETER_WEYL_HIGHER_SHELL_LAMBDA.json
```

Shape-to-metric Jacobian:

```bash
python scripts/logical_shape_metric_jacobian_gate.py
```

First refined S4 metric compression:

```bash
python scripts/collective_l1_q4_s4_metric_compression.py --help
```

Hopf/Pancharatnam U(1):

```bash
python scripts/q2_pancharatnam_u1_gate.py
```

Optical metric anisotropy map:

```bash
python scripts/physicalization_optical_metric_anisotropy_gate.py
```

Physical scale map:

```bash
python scripts/physical_scale_prediction_bridge.py --help
```

---

# Эпилог. Где заканчивается сказка и начинается физика

На сегодня самая сильная корректная формулировка такая:

> **Binary Causal / Information-Graph Quantum Gravity — вычислительно проверяемая кандидатная архитектура, в которой локальная бинарная однородность выбирает q=2; q=2 создаёт octahedral S2 link и canonical recursive PL three-manifold; frozen route growth имеет точный causal-volume fixed point d=3, а frozen dynamics даёт d_H/z≈3.00439 при z≈1 и историю 1+d_H/z≈4.00439; q=2 quantum carrier естественно несёт SU(2) geometry и Hopf U(1) phase; Peter–Weyl dynamics содержит nontrivial higher shells и measurable five-component traceless metric sector E⊕T2; первый refined shell имеет 8.43% tetrahedral metric anisotropy; HDA/Regge/Plebanski routes воспроизводят GR tensor structure в своём проверенном scope; explicit reduced TT propagator massless and has P_TT(k)~k^-1. Главный physical frontier теперь сведен к three-orbit kernel C6(omega,k)=aI+bA+cO, из которого без generic fitting извлекаются eta2_IR and zeta4_IR, после чего optical E/T2 phase ratio R_gamma даёт dimensionless blind experimental channel. Compact U(1) carrier выведен кинематически, но alpha требует microscopic gauge stiffness Z_A. Particle masses не выводятся из 8.43% напрямую; S4 symmetry запрещает такой shortcut и требует отдельного derived matter/Yukawa bridge.**

Если последующие full-H_E / Lorentzian RG calculations покажут

\[
\Delta_{ET}^{leading}\to0,
\qquad
\eta_2\to\eta_2^*,
\qquad
\zeta_4\to\zeta_4^*
\]

regulator-independently, мы получим первую настоящую frozen dimensionless gravitational prediction этой microscopic theory.

Если нет — эта ветка должна получить `FAIL`.

Именно поэтому это научная сказка для взрослых: в ней у дракона есть право победить.
