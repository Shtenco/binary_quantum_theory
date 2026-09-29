# Бинарная квантовая гравитация  
## Научная сказка о том, как два бита пытаются стать пространством, геометрией, временем и гравитацией

**Каноническое повествование репозитория на 29 сентября 2026 года**

Эта книга-README написана сразу для двух читателей.

Первый читатель — любознательный ребёнок, который умеет спрашивать простые и опасные вопросы:

- из чего сделано пространство;
- почему оно трёхмерное;
- откуда берётся геометрия;
- почему гравитация похожа на кривизну;
- можно ли построить всё это из очень маленького количества информации.

Второй читатель — физик, математик или исследователь, который после каждого красивого образа спрашивает:

- где оператор;
- где Hilbert space;
- где constraint;
- где theorem;
- где numerical certificate;
- где отрицательный контроль;
- где граница применимости;
- где физический observable;
- и что именно ещё НЕ доказано.

Поэтому каждая глава этой научной сказки имеет два слоя:

1. **образный слой** — чтобы видеть общую идею;
2. **строгий слой** — формулы, статусы, ссылки на файлы и ограничения.

Главное правило книги:

\[
\boxed{
\text{красивая история никогда не сильнее доказательства}
}
\]

Если что-то пока только идея — мы пишем OPEN.

Если есть конечная вычислительная проверка — мы пишем FINITE PASS.

Если доказан точный результат в заявленной области — мы пишем PROVED.

Если найден запрет или obstruction — мы не прячем его, а делаем частью сюжета.

Если физическая теория ещё не замкнута — мы так и говорим.

---

# Пролог. Самый маленький вопрос

Представим, что у Вселенной ещё нет привычных координат.

Нет метров.

Нет секунд.

Нет готовой гладкой метрики.

Нет заранее данного трёхмерного пространства.

Нет даже уверенности, что слово «расстояние» уже имеет смысл.

Есть только маленькие различимые состояния и правила, по которым они могут соседствовать, связываться и преобразовываться.

Тогда можно задать почти детский вопрос:

> Может ли пространство появиться не как фон, а как коллективное свойство очень простой квантовой информации?

Бинарная квантовая гравитация, или BQG, — это попытка сделать этот вопрос вычислимым.

Не философским.

Не метафорическим.

А таким, чтобы на каждом шаге можно было написать:

\[
\text{input}
\longrightarrow
\text{operator}
\longrightarrow
\text{certificate}
\longrightarrow
\text{PASS или FAIL}.
\]

В этом репозитории построена большая цепочка:

\[
\boxed{
\text{binary microstructure}
\to
q=2
\to
3D geometry
\to
SU(2)\text{ quantum geometry}
\to
\text{graph-changing constraints}
\to
\text{GR/HDA controls}
\to
\text{TT observable algebra}
}
\]

Но последняя строчка нашей сказки пока не написана.

После этой цепочки остаётся самая трудная часть:

\[
\boxed{
\text{finite quantum geometry}
\not\Rightarrow
\text{physical continuum quantum gravity автоматически}.
}
\]

Именно эту границу важно помнить во всех последующих главах.

---

# Глава 1. Четыре маленьких знака

## 1.1. Почему именно q=2

Начальная микроструктура использует бинарный алфавит.

Два независимых бинарных признака дают четыре состояния:

\[
\mathbb Z_2^2.
\]

Их можно представить как четыре вершины маленького логического квадрата.

Но удивительный момент возникает, когда мы рассматриваем не сами состояния, а три нетривиальных Walsh-character.

Они задают три числовые координаты для каждого из четырёх состояний.

После нормировки эти четыре вектора оказываются направлены как вершины правильного тетраэдра.

То есть из простейшей бинарной структуры внезапно появляется не линия и не квадрат, а тетраэдрический flux-frame.

Строгий результат хранится в:

- [MICRO_WALSH_QGEOM_BRIDGE.md](MICRO_WALSH_QGEOM_BRIDGE.md)
- [scripts/micro_walsh_qgeom_gate.py](scripts/micro_walsh_qgeom_gate.py)

Точные тождества:

\[
\sum_{a=1}^{4} n_a = 0,
\]

\[
n_a\cdot n_a=1,
\]

\[
n_a\cdot n_b=-\frac13,
\qquad a\neq b.
\]

Это ровно геометрия нормалей правильного тетраэдра.

**Статус: PROVED в заявленной конечной конструкции.**

---

## 1.2. Первая мораль сказки

Важно не перепутать два утверждения.

Мы НЕ говорим:

> четыре бита автоматически доказывают существование нашего пространства.

Мы говорим более осторожно:

> выбранная q=2 бинарная конструкция содержит точный тетраэдрический геометрический carrier.

Это уже сильнее простой визуальной аналогии.

Но ещё слабее физической теории природы.

---

# Глава 2. Почему пространство хочет быть трёхмерным

Ребёнок может спросить:

> А почему тетраэдр вообще связан с тремя измерениями?

BQG отвечает не одной картинкой, а отдельной refinement-конструкцией.

Для frozen q=2 refinement count получено:

\[
N_g=\frac{4\cdot 8^g+10}{7}.
\]

Из отношения соседних поколений определяется effective finite-step dimension:

\[
d_g
=
\log_2\frac{N_g}{N_{g-1}}.
\]

Она принимает вид

\[
d_g
=
3+
\log_2
\left(
1-
\frac{35}{16\cdot 8^{g-1}+40}
\right).
\]

Для каждого конечного шага:

\[
d_g<3,
\]

но последовательность монотонно растёт и

\[
\boxed{
\lim_{g\to\infty}d_g=3.
}
\]

Это не численный фит.

Это аналитический fixed-point statement внутри выбранной refinement rule.

Основные файлы:

- [Q2_DIMENSION3_FIXED_POINT_CLOSURE.md](Q2_DIMENSION3_FIXED_POINT_CLOSURE.md)
- [scripts/q2_dimension3_fixed_point_gate.py](scripts/q2_dimension3_fixed_point_gate.py)

**Статус: PROVED для frozen q=2 refinement count.**

---

# Глава 3. Как грань становится квантовой

Тетраэдрическая геометрия сама по себе ещё классическая картинка.

Чтобы войти в квантовую геометрию, нужно заменить обычные векторы состояниями и операторами.

В BQG используются SU(2)-структуры, знакомые по spin-network / loop-inspired constructions.

На четырёхвалентном узле возникают intertwiner degrees of freedom.

Gauss constraint требует локальной gauge-invariance.

В простейшем q=2 carrier получено:

\[
\text{Gauss-singlet weight}=\frac29.
\]

Появляется двумерный logical sector.

В нём удобно говорить о Pauli-like logical directions:

\[
X,\quad Y,\quad Z.
\]

Два направления, \(X\) и \(Z\), меняют intrinsic shape.

Направление \(Y\) связано с orientation / oriented-volume branch.

Точный logical metric Jacobian имеет rank два:

\[
\boxed{
\operatorname{rank}J_{\rm metric}=2.
}
\]

Причём \(X\)- и \(Z\)-tangents:

- trace-free;
- взаимно ортогональны;
- имеют одинаковую DeWitt norm.

Основные доказательные файлы:

- [LOGICAL_SHAPE_METRIC_JACOBIAN.md](LOGICAL_SHAPE_METRIC_JACOBIAN.md)
- [scripts/logical_shape_metric_jacobian_gate.py](scripts/logical_shape_metric_jacobian_gate.py)

**Статус: PROVED для локального carrier.**

---

# Глава 4. Пятое состояние, которого сначала не было

Если оставить только четыре активных q=2 состояния, endpoint representation оказывается слишком бедной для нужного graph-changing transport.

В конструкции появляется no-link / \(j=0\) state.

Тогда набор

\[
4\ \text{active states}
+
1\ \text{no-link state}
\]

образует точную пятикомпонентную структуру, связанную с SO(5)-вектором:

\[
(2,2)+(1,1)
\]

в соответствующем SU(2)\(_L\times\)SU(2)\(_R\) разложении.

Ключевой transporter identity:

\[
P_g U_a P_0 U_b P_g
=
|a\rangle\langle b|.
\]

То есть переход между активными состояниями можно факторизовать через graph-changing excursion в no-link sector.

Файлы:

- [Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md](Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md)
- [scripts/q2_graphlink_peter_weyl_gate.py](scripts/q2_graphlink_peter_weyl_gate.py)

**Статус: PROVED для заявленного finite representation carrier.**

---

# Глава 5. Как один тетраэдр учится жить среди других

Один тетраэдр — ещё не пространство.

Нужно научить много клеток склеиваться.

В canonical finite completion используется boundary 4D cross-polytope:

- 16 tetrahedral cells;
- 32 shared triangular faces;
- dual graph \(Q_4\).

На общей грани соседние клетки используют согласованный q=2 carrier.

Orientation parity чередуется.

Outward Walsh flux на shared face сокращается попарно.

Основные файлы:

- [GLOBAL_MANIFOLD_Q2_COMPLETION.md](GLOBAL_MANIFOLD_Q2_COMPLETION.md)
- [bcqg_global_manifold_gate.py](bcqg_global_manifold_gate.py)
- [scripts/q2_global_face_qubit_gluing_gate.py](scripts/q2_global_face_qubit_gluing_gate.py)

**Статус: finite exact/tested completion для выбранной PL-геометрии.**

Это ещё не theorem для произвольного manifold.

Но это уже настоящий global gluing certificate для конкретной модели.

---

# Глава 6. Волшебная лестница Peter–Weyl

Когда quantum link становится более возбуждённым, representation content должен расти.

При явно заданном symmetric blocking occupancy \(n\) даёт

\[
j=\frac n2.
\]

Размер representation:

\[
\dim(j,j)
=
(2j+1)^2
=
(n+1)^2.
\]

Таким образом occupancy

\[
n=0,1,\ldots,N
\]

воспроизводит диагональную Peter–Weyl tower

\[
j=0,\frac12,1,\frac32,\ldots,\frac N2.
\]

Ключевой файл:

- [Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md](Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md)

Важно:

**Статус: CONDITIONAL**, потому что statement зависит от явно выбранного fully symmetric endpoint blocking.

Это хороший пример того, как README должен быть честнее красивой истории.

---

# Глава 7. Как из flux появляется metric

Чтобы назвать конструкцию гравитационной, мало иметь SU(2)-labels.

Нужно получить объекты, которые ведут себя как геометрия.

В проекте есть несколько независимых мостов:

\[
\text{flux}
\to
B\text{-field}
\to
\text{simplicity}
\to
\text{Urbantke metric}
\to
\text{connection}
\to
\text{curvature}.
\]

Файлы:

- [PLEBANSKI_URBANTKE_BRIDGE.md](PLEBANSKI_URBANTKE_BRIDGE.md)
- [PLEBANSKI_CONNECTION_EINSTEIN_GATE.md](PLEBANSKI_CONNECTION_EINSTEIN_GATE.md)
- [QUBIT_TO_EINSTEIN_END_TO_END.md](QUBIT_TO_EINSTEIN_END_TO_END.md)
- [scripts/qubit_to_einstein_end_to_end.py](scripts/qubit_to_einstein_end_to_end.py)

Positive control восстанавливает заявленную Einstein geometry.

Independent non-Einstein control отвергается после metric stage.

Это важно: gate не только ищет совпадение, но и умеет сказать NO.

**Статус: FINITE TESTED CONTROL.**

---

# Глава 8. Regge-мост: когда дискретная геометрия вспоминает Эйнштейна

Ещё один путь идёт через Regge calculus.

Вместо гладкой curvature рассматриваются piecewise-linear simplicial geometries.

Проверяется, что finite Hessian / cubic structures стремятся к правильным continuum tensor relations.

Есть directional controls:

- axial;
- diagonal-2;
- diagonal-3.

Held-out test на \(L=6\) использует rule, обученную только на \(L=3,4,5\):

\[
Z_L
=
\frac18
+
\frac C{L^2}
+
\frac D{L^4}.
\]

Получено:

\[
Z_6^{\rm pred}
=
0.11876923193907167,
\]

\[
Z_6^{\rm obs}
=
0.11876075461190198.
\]

Relative error около

\[
0.00714\%.
\]

Файлы:

- [REGGE_EH_CUBIC_BRIDGE.md](REGGE_EH_CUBIC_BRIDGE.md)
- [TT_REGGE_ZT_L6_RESULT.md](TT_REGGE_ZT_L6_RESULT.md)
- [scripts/regge_eh_cubic_bridge.py](scripts/regge_eh_cubic_bridge.py)
- [scripts/tt_regge_zt_l6_gate.py](scripts/tt_regge_zt_l6_gate.py)

**Статус: FINITE TESTED CONTROL, не continuum theorem.**

---

# Глава 9. Замок constraints

В общей теории относительности динамика устроена не как обычная система «координата плюс внешний time».

Есть constraints.

В canonical gravity появляются:

- Gauss-like gauge structure;
- spatial diffeomorphism constraint;
- Hamiltonian constraint.

Их closure кодирует саму геометрию spacetime.

Целевой continuum HDA:

\[
\{H[N],H[M]\}
\to
D
\left[
q^{ab}
(N\partial_bM-M\partial_bN)
\right].
\]

BQG строит finite analogues и проверяет scaling hierarchy на выбранных habitats.

Например three-node graph-changing control показывает:

\[
\text{route}\sim\epsilon,
\]

\[
\text{cross}\sim\epsilon,
\]

\[
\text{pure geometry}\sim\epsilon^2.
\]

Для joint defect measured exponent:

\[
\boxed{
1.0064429344.
}
\]

Файлы:

- [THREE_NODE_GRAPH_HDA_RESULT.md](THREE_NODE_GRAPH_HDA_RESULT.md)
- [JOINT_REGULATOR_LIMIT.md](JOINT_REGULATOR_LIMIT.md)
- [scripts/peter_weyl_three_node_graph_hda_gate.py](scripts/peter_weyl_three_node_graph_hda_gate.py)
- [scripts/joint_regulator_limit_gate.py](scripts/joint_regulator_limit_gate.py)

**Статус: FINITE CONTROL в заявленных habitats.**

Не arbitrary-graph theorem.

Не unbounded refinement theorem.

---

# Глава 10. DeWitt: правильный знак в сердце геометрии

Canonical GR имеет особенную kinetic signature в superspace.

В репозитории есть отдельные gates:

- [DEWITT_HDA_UNIQUENESS.md](DEWITT_HDA_UNIQUENESS.md)
- [FLUX_DEWITT_SIGNATURE_THEOREM.md](FLUX_DEWITT_SIGNATURE_THEOREM.md)
- [scripts/dewitt_hda_uniqueness_gate.py](scripts/dewitt_hda_uniqueness_gate.py)

Один важный вывод:

common radial flux scaling

\[
E_f\to(1+\epsilon)E_f
\]

задаёт conformal DeWitt direction с

\[
\boxed{Q_{\rm DW}=-6}.
\]

Этот результат позже становится важным для scalar/cosmology story, потому что локальный \(X/Z\)-carrier сам по себе conformal mode не содержит.

---

# Глава 11. Hamiltonian, который меняет граф

Теперь наш герой должен научиться не только измерять геометрию, но и менять её.

Graph-changing Hamiltonian acts locally.

В finite Peter–Weyl habitats он переводит spin assignments в соседние assignments, изменяя три рёбра около выбранной пары.

Именно здесь возникает сложность:

одна локальная формула рождает огромные sparse operators.

Поэтому проект использует:

- symmetry reduction;
- orbit decomposition;
- stabilizers;
- S4/S5 representation theory;
- sparse support graphs;
- structural Hall-flow;
- local rank certificates;
- distributed sharding.

Это не декоративная оптимизация.

Без неё depth-6 Hilbert space уже имеет миллионы состояний.

---

# Глава 12. Master constraint: судья, который слушает все вершины

Вместо требования анализировать каждый constraint отдельно вводится positive master operator:

\[
\boxed{
M
=
\sum_{v=0}^{4}
H_v^\dagger H_v.
}
\]

Поскольку каждый term положителен,

\[
\langle\psi|M|\psi\rangle
=
\sum_v
\|H_v\psi\|^2.
\]

Поэтому

\[
\boxed{
\ker M
=
\bigcap_{v=0}^{4}
\ker H_v.
}
\]

Это важнейшая логика всей depth-6 программы.

Отсюда следует ключевой урок:

\[
\boxed{
H_0\psi=0
\quad\not\Rightarrow\quad
\psi\in\ker M.
}
\]

Чтобы быть master-null, состояние должно умереть под всеми relevant \(H_v\).

Файл общего finite theorem:

- [MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md](MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md)

**Статус finite theorem: PROVED.**

Но continuum physical projector ещё OPEN.

---

# Глава 13. Маленькая репетиция: depth-4

До гигантского depth-6 была depth-4 репетиция.

Полный finite depth-4 Hilbert space:

\[
\dim\mathcal H_{d=4}=217953.
\]

S5 multiplicities:

\[
[5]:2085,
\]

\[
[4,1]:7357,
\]

\[
[3,2]:9332,
\]

\[
[3,1,1]:10471,
\]

\[
[2,2,1]:9249,
\]

\[
[2,1,1,1]:7180,
\]

\[
[1^5]:1989.
\]

Все non-vacuum sectors были found injective в соответствующем finite analysis.

В trivial \([5]\)-sector остаётся только vacuum line.

Это стало важным positive control перед depth-6.

---

# Глава 14. Огромный город depth-6

Теперь начинается текущая главная computational saga.

Corrected finite \(K_5\) depth-6 shell содержит:

\[
\boxed{
264\,962
}
\]

Gauss-admissible spin assignments.

Полная Hilbert dimension:

\[
\boxed{
3\,111\,637.
}
\]

S5 spin-orbits:

\[
\boxed{
2757.
}
\]

Максимальный doubled spin:

\[
2j_{\max}=7,
\qquad
j_{\max}=\frac72.
\]

Точный S5 multiplicity ledger:

| \(S_5\)-irrep | multiplicity |
|---|---:|
| \([5]\) | 27,227 |
| \([4,1]\) | 104,146 |
| \([3,2]\) | 130,903 |
| \([3,1,1]\) | 153,455 |
| \([2,2,1]\) | 130,503 |
| \([2,1,1,1]\) | 103,318 |
| \([1^5]\) | 26,794 |

С учётом dimensions irreps это точно даёт

\[
\boxed{
3\,111\,637.
}
\]

Машинный источник правды:

- [depth6_frontier.json](depth6_frontier.json)
- [scripts/verify_depth6_frontier.py](scripts/verify_depth6_frontier.py)

---

# Глава 15. Три уже закрытые крепости

## 15.1. Sign irrep \([1^5]\)

Получено:

\[
\boxed{
\operatorname{rank}H_0
=
26794/26794.
}
\]

Следовательно:

\[
\boxed{
\ker=0.
}
\]

**Статус: CLOSED.**

---

## 15.2. Trivial irrep \([5]\)

Нулевой spin orbit — vacuum.

На non-vacuum части:

\[
\boxed{
\operatorname{rank}H_0
=
27226/27226.
}
\]

Поэтому:

\[
\boxed{
\ker H_0^{[5]}
=
\operatorname{span}\{|0\rangle\}.
}
\]

**Статус: CLOSED, vacuum only.**

---

## 15.3. Standard irrep \([4,1]\)

Используется branching:

\[
[4,1]\downarrow S_4
=
[4]\oplus[3,1].
\]

Финальный finite rank:

\[
\boxed{
104146/104146.
}
\]

**Статус: CLOSED.**

---

# Глава 16. Почему остальные четыре сектора оказались хитрее

Mixed irreps:

\[
[3,2],
\quad
[3,1,1],
\quad
[2,2,1],
\quad
[2,1,1,1].
\]

Для них naive идея:

> если \(H_0\) full rank, сектор закрыт

оказалась слишком сильной.

У mixed representation могут существовать \(H_0\)-null directions, которые не являются master-null.

И это не баг.

Это representation-theoretic структура.

Поэтому весь проект был переведён на master-aware branch strategy.

---

# Глава 17. Branch-sum theorem

Для S5-irrep \(\lambda\) master operator можно разложить по S4 branches:

\[
\boxed{
B_\lambda
=
\frac{5}{d_\lambda}
\sum_{\mu\to\lambda}
d_\mu
A_{\lambda,\mu}
}
\]

где

\[
A_{\lambda,\mu}
=
H_0^\dagger H_0
\]

на соответствующей branch.

Поскольку

\[
A_{\lambda,\mu}\ge0,
\]

имеем:

\[
\boxed{
\ker B_\lambda
=
\bigcap_{\mu\to\lambda}
\ker A_{\lambda,\mu}.
}
\]

Для оставшихся sectors:

\[
\boxed{
B_{[3,2]}
=
3A_{31}+2A_{22}
}
\]

\[
\boxed{
B_{[3,1,1]}
=
\frac52
(A_{31}+A_{211})
}
\]

\[
\boxed{
B_{[2,2,1]}
=
2A_{22}+3A_{211}
}
\]

\[
\boxed{
B_{[2,1,1,1]}
=
\frac54
(3A_{211}+A_{1111})
}
\]

Это один из главных conceptual boosts проекта.

Четыре разные brute-force задачи превращаются в одну общую positive branch-sum architecture.

---

# Глава 18. Structural support: карта дорог, а не доказательство путешествия

Для всех mixed irreps geometric/capacity support уже structurally closes.

\[
[3,2]:
\quad
2755/2755\ \text{blocks},
\quad
130903/130903\ \text{columns}
\]

\[
[3,1,1]:
\quad
2719/2719,
\quad
153455/153455
\]

\[
[2,2,1]:
\quad
2749/2749,
\quad
130503/130503
\]

\[
[2,1,1,1]:
\quad
2712/2712,
\quad
103318/103318.
\]

Это означает:

\[
\boxed{
\text{structural obstruction}=0
}
\]

в соответствующем support model.

Но очень важно:

\[
\boxed{
\text{Hall capacity}
\neq
\text{numeric injectivity автоматически}.
}
\]

Structural support говорит:

> места для independent outputs достаточно.

Но только actual matrix rank говорит:

> операторы действительно независимы.

---

# Глава 19. Секрет S4-sign и шестнадцать молчащих стражей

Для \([2,1,1,1]\) появился дополнительный shortcut:

\[
\mathcal H^{S_4\text{-sign}}
=
[1^5]
\oplus
[2,1,1,1].
\]

Размер:

\[
\boxed{
130112
=
26794+103318.
}
\]

Structural peeling:

\[
11956/11956
\]

blocks,

\[
130112/130112
\]

columns.

Сначала казалось, что можно доказать injectivity одним \(H_0\).

Но actual-support max-flow дал:

\[
\boxed{
130096/130112.
}
\]

Не хватало ровно шестнадцати scalar directions.

Min-cut показал:

\[
\boxed{
S_{\rm deficient}
=
\{0,1,\ldots,15\}.
}
\]

Каждый block одномерен:

\[
d_i=1.
\]

---

# Глава 20. Почему шестнадцать стражей молчали

Пересчёт с нулевым cutoff показал:

\[
\boxed{
H_0\psi_i=0
}
\]

для всех 16.

Это не numerical cancellation.

Причина геометрическая.

У всех этих states:

\[
(j_{01},j_{02},j_{03},j_{04})
=
(0,0,0,0).
\]

То есть все четыре edges, входящие в vertex \(0\), имеют zero spin.

Локальный vertex-0 Hamiltonian просто не видит там активной геометрии.

Это очень хороший пример научного no-go.

Старая гипотеза:

\[
H_0
\text{ injective on total S4-sign}
\]

оказалась неверной.

И проект обязан это запомнить.

Именно поэтому machine-ledger теперь запрещает объявлять такой statement theorem.

---

# Глава 21. Но master constraint услышал другой голос

Хотя

\[
H_0\psi_i=0,
\]

мы проверили \(H_1\).

Для всей 16D obstruction subspace:

\[
\boxed{
\operatorname{rank}
H_1|_{16}
=
16/16.
}
\]

Минимальная singular value:

\[
\boxed{
\sigma_{\min}
=
1.1304521906426823.
}
\]

Максимальная:

\[
\boxed{
\sigma_{\max}
=
3.304257962941286.
}
\]

Condition number:

\[
\kappa\approx2.923.
\]

Поэтому:

\[
\boxed{
\ker H_0
\text{ на этих 16 directions}
\not\subset
\ker M.
}
\]

Все шестнадцать directions подняты \(H_1\).

**Это закрытый локальный obstruction, но ещё не весь sector theorem.**

---

# Глава 22. Гигант за воротами

После удаления локализованной 16D obstruction основной S4-sign giant component имеет:

\[
\boxed{
11923
}
\]

input blocks,

\[
\boxed{
130007
}
\]

columns,

\[
\boxed{
14586
}
\]

output \(q\)-blocks.

Номинальная row capacity:

\[
153202.
\]

После actual numerical row-rank audit:

\[
\boxed{
\sum_q r_q^{\rm numerical}
=
153056.
}
\]

Несмотря на локальные rank deficits, rank-aware max-flow остаётся:

\[
\boxed{
130007/130007.
}
\]

Deficient inputs после этого flow:

\[
\boxed{
0.
}
\]

Уже выбран square minor:

\[
\boxed{
A_{\rm giant}
\in
\mathbb C^{130007\times130007}.
}
\]

Expected scalar nonzero entries:

\[
\boxed{
47\,543\,521.
}
\]

Zero selected rows:

\[
\boxed{
0.
}
\]

Но главный вопрос ещё открыт:

\[
\boxed{
\operatorname{rank}
A_{\rm giant}
\stackrel{?}{=}
130007.
}
\]

**Статус: ACTIVE / NOT YET CLOSED.**

---

# Глава 23. Почему мы не называем depth-6 доказанным

Соблазн велик.

Три irreps уже CLOSED.

Structural support остальных закрыт.

16D obstruction поднят.

Giant Hall flow полон.

Но science начинается именно там, где хочется сказать «ну почти же».

Пока sparse minor не factorized rank-revealing методом, мы не имеем права писать:

\[
[2,1,1,1]\ \text{CLOSED}.
\]

И пока остальные mixed irreps не получили финальные numeric certificates, мы не имеем права писать:

\[
\boxed{
\ker M^{(d=6)}
=
\operatorname{span}\{|0\rangle\}.
}
\]

Поэтому machine truth сейчас:

\[
\boxed{
\text{finite depth-6 theorem status}
=
\text{NOT YET PROVED}.
}
\]

---

# Глава 24. Что останется после S4-sign giant

Если giant rank gate проходит, \([2,1,1,1]\) становится CLOSED.

После этого остаются:

\[
\boxed{
[3,2],
\quad
[3,1,1],
\quad
[2,2,1].
}
\]

Для них уже есть:

- Jucys/branch selectors;
- structural supports;
- generic master-map architecture;
- distributed shard workflows;
- fail-closed aggregators.

То есть следующая работа — не новая теория representation reduction с нуля.

Это numerical completion уже построенного engine.

---

# Глава 25. Самая важная черта между конечным и бесконечным

Представим, что завтра мы получаем:

\[
\boxed{
\ker M^{(d=6)}
=
\operatorname{span}\{|0\rangle\}.
}
\]

Будет ли BQG доказанной quantum gravity?

Нет.

Это будет очень сильный finite-habitat theorem.

Но continuum требует больше.

Нужна последовательность:

\[
d=4,
\quad
d=6,
\quad
d=8,
\quad
\ldots
\]

и понятие refinement map между ними.

Идеальная цель:

\[
\boxed{
\ker M^{(d)}
=
\operatorname{span}\{|0\rangle\}
\quad
\forall d\ge d_0
}
\]

или более физически правильный stabilized-kernel theorem.

Самый выгодный будущий breakthrough — не бесконечно считать depth \(8,10,12,\ldots\), а доказать induction/refinement mechanism.

---

# Глава 26. Physical projector: дверь в настоящую quantum gravity

Finite master theorem говорит:

\[
M_G
=
C_A^\dagger
G^{AB}
C_B
\ge0,
\]

и для positive \(G\)

\[
\boxed{
\ker M_G
=
\bigcap_A
\ker C_A.
}
\]

Если zero sector isolated, можно построить finite spectral projector.

Но настоящая physical theory требует limit:

\[
P_{\rm phys}^{(d)}
\longrightarrow
P_{\rm phys}^{\rm continuum}.
\]

Нужно показать:

- refinement consistency;
- regulator independence;
- anomaly control;
- physical inner product;
- rigging-map or boundary-history meaning.

Главный файл:

- [MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md](MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md)

Machine ledger:

- [physicalization_gates.json](physicalization_gates.json)

**Статус theory-specific continuum projector: OPEN.**

---

# Глава 27. Время, которое нельзя просто подарить теории

Constraint system не даёт обычный external time автоматически.

Поэтому в проекте есть finite relational-history positive controls.

Они показывают математическую возможность цепочки:

\[
\text{combined constraint projector}
\to
\text{relational observables}
\to
Z[J]
\to
W[J].
\]

Но текущий finite control использует deliberately declared clock construction.

Он не доказывает, что именно такой clock является физическим временем BQG.

Файлы:

- [Q2_RELATIONAL_HISTORY_PROJECTOR.md](Q2_RELATIONAL_HISTORY_PROJECTOR.md)
- [Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md](Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md)

**Статус: FINITE POSITIVE CONTROL.**

Theory-specific physical history:

\[
\boxed{
\text{OPEN}.
}
\]

---

# Глава 28. Почему resolvent ещё не propagator

Есть очень опасная интеллектуальная ловушка.

Можно взять constraint operator \(H\) и написать:

\[
(z-H)^{-1}.
\]

Объект похож на Green function.

Но parameter \(z\) не обязан быть physical frequency \(\omega\).

Поэтому:

\[
\boxed{
(z-H_{\rm constraint})^{-1}
\neq
G_{\rm physical}(\omega)
}
\]

без independently derived time/history structure.

Репозиторий специально фиксирует этот запрет в:

- [HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md](HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md)
- [FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md](FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md)

Это важная защита от красивого, но ложного shortcut.

---

# Глава 29. Правильная дорога к эффективному действию

Легальная цепочка выглядит так:

\[
\boxed{
\{C_A\}
\to
M
\to
P_{\rm phys}
\to
Z[J_g]
\to
W[J_g]
\to
\Gamma[g]
}
\]

затем

\[
\Gamma[g]
\to
\Gamma^{(2)}_{\rm metric}
\to
K_{TT}(\omega,\mathbf k).
\]

И только после этого можно говорить о physical graviton pole.

Это один из главных незакрытых мостов всего проекта.

**Статус: interface fixed, theory-specific construction OPEN.**

---

# Глава 30. TT-сектор: когда геометрия учится волноваться

Для spin-2 sector проект строит transverse-traceless response.

Positive control показывает leading massless pole.

Есть finite Gaussian vacuum two-point function.

Файлы:

- [TT_PROPAGATOR_FIRST_PASS.md](TT_PROPAGATOR_FIRST_PASS.md)
- [TT_VACUUM_TWO_POINT_RESULT.md](TT_VACUUM_TWO_POINT_RESULT.md)

Но это именно reduced/reference controls.

Они не заменяют interacting theory-specific physical \(K_{TT}\).

---

# Глава 31. Шесть чисел будущего

Для parity-even quartic TT response с tetrahedral \(S_4\) symmetry доказано:

\[
\boxed{
\dim\mathcal V_{\rm quartic}^{TT}
=
6.
}
\]

То есть общий on-shell quartic response определяется шестью Wilson coefficients:

\[
\boxed{
\mathbf c_{\rm IR}
=
(c_1,c_2,c_3,c_4,c_5,c_6).
}
\]

Файлы:

- [S4_TT_QUARTIC_COMPLETE_BASIS.md](S4_TT_QUARTIC_COMPLETE_BASIS.md)
- [C6_TO_TT_WILSON_COEFFICIENTS.md](C6_TO_TT_WILSON_COEFFICIENTS.md)
- [scripts/s4_tt_quartic_complete_basis_gate.py](scripts/s4_tt_quartic_complete_basis_gate.py)

Extraction system имеет full rank six.

Exact determinant:

\[
\boxed{
\det A
=
\frac1{699840000}.
}
\]

**Статус algebraic basis/extractor: PROVED.**

Но physical values \(c_i\) ещё не выведены.

---

# Глава 32. Что произойдёт, если шесть чисел однажды появятся

Physical TT poles можно написать:

\[
\omega_\sigma^2
=
c^2k^2
\left[
1+a_*^2k^2e_{4,\sigma}(\hat n)
+
O(a_*^4k^4)
\right].
\]

Тогда:

\[
\frac{v_{g,\sigma}-c}{c}
=
\frac32
a_*^2k^2
e_{4,\sigma}(\hat n)
+\cdots
\]

и phase shift:

\[
\delta\phi_\sigma
=
-\frac12
La_*^2
\left(
\frac\omega c
\right)^3
e_{4,\sigma}(\hat n)
+\cdots
\]

Polarization splitting:

\[
\Delta e_4(\hat n)
=
e_{4,1}(\hat n)
-
e_{4,2}(\hat n).
\]

Observable translator уже готов:

- [TT_TO_REAL_PHYSICS_OBSERVABLES.md](TT_TO_REAL_PHYSICS_OBSERVABLES.md)
- [scripts/s4_tt_six_wilson_predictor.py](scripts/s4_tt_six_wilson_predictor.py)
- [scripts/physical_scale_prediction_bridge.py](scripts/physical_scale_prediction_bridge.py)

Но сегодня:

\[
\boxed{
(c_1,\ldots,c_6)_{\rm physical}
\text{ ещё OPEN}.
}
\]

Поэтому observable algebra готова.

Physical prediction ещё нет.

---

# Глава 33. Один масштаб, а не шесть подгонок

После получения dimensionless six-vector нужен абсолютный scale.

В проекте используется convention:

\[
\lambda_R^{\rm eff}
=
\frac{a_*^2}{8\pi\ell_P^2}.
\]

Правило anti-overfitting:

- либо scale выводится microscopically;
- либо ровно один preregistered datum фиксирует common scale;
- после этого он не меняется между observables.

Запрещено:

> подогнать отдельный scale для каждой красивой кривой.

**Статус physical common scale: OPEN.**

---

# Глава 34. Космология: место, где сказка сама сказала «пока нет»

Очень важный отрицательный результат содержится в:

- [Q2_FIRST_SCALAR_EFFECTIVE_ACTION.md](Q2_FIRST_SCALAR_EFFECTIVE_ACTION.md)

Для finite relational source получен exact local 1PI shape action:

\[
\boxed{
\Gamma_{\rm shape}(s)
=
s\,\operatorname{artanh}s
+
\frac12
\log(1-s^2)
}
\]

и expansion:

\[
\Gamma_{\rm shape}
=
\frac{s^2}{2}
+
\frac{s^4}{12}
+
\frac{s^6}{30}
+
\cdots.
\]

Это настоящий exact nonlinear result.

Но затем обнаруживается conformal obstruction.

Локальные \(X/Z\) tangents trace-free:

\[
\operatorname{Tr}
(g_0^{-1}M_X)
=
0,
\]

\[
\operatorname{Tr}
(g_0^{-1}M_Z)
=
0.
\]

Поэтому local q=2 shape carrier не содержит нужный conformal/volume scalar.

Кроме того отсутствуют:

- independent lapse-response source;
- connected interblock history;
- physical momentum kernel.

Следовательно сегодня нельзя честно вывести:

\[
\rho_{\rm hist}(a),
\]

\[
\Phi(a,k),
\quad
\Psi(a,k),
\]

\[
\mu_{\rm BQG}(a,k),
\quad
\Sigma_{\rm BQG}(a,k).
\]

**Статус cosmological scalar physics: OPEN.**

Это не поражение.

Это полезный no-go, который говорит, какой carrier надо добавить.

---

# Глава 35. Где искать missing scalar

DeWitt analysis подсказывает natural direction.

Common radial flux scaling создаёт conformal mode.

При фиксированном \(j=\frac12\) absolute volume frozen в маленьком intertwiner carrier.

Но \(j=1\) — первый equal-spin four-valent sector, где absolute volume становится non-scalar.

Conditional symmetric blocking даёт:

\[
2\ \text{active q=2 strands}
\longrightarrow
j=1.
\]

Отсюда возникает следующий candidate scalar carrier.

Файлы:

- [Q2_COLLECTIVE_SCALAR_CARRIER.md](Q2_COLLECTIVE_SCALAR_CARRIER.md)
- [COLLECTIVE_J1_VOLUME_DYNAMICS.md](COLLECTIVE_J1_VOLUME_DYNAMICS.md)

Это хороший пример того, как отрицательный gate направляет следующую архитектуру.

---

# Глава 36. Материя: кто скажет геометрии, что рядом масса

Даже physical metric Hessian недостаточен, чтобы определить response to matter.

Нужно вывести или явно зафиксировать coupling к conserved source.

Файл:

- [BQG_SCALAR_RESPONSE_TO_MATTER.md](BQG_SCALAR_RESPONSE_TO_MATTER.md)

Пока coupling не derived:

\[
\mu_{\rm BQG},
\quad
\Sigma_{\rm BQG}
\]

не являются predictions.

**Статус matter-response coupling: OPEN.**

---

# Глава 37. Фотон тоже не должен появляться магически

Physicalization ledger отдельно требует dynamical Maxwell kernel.

Нужно получить theory-specific transverse photon 1PI kernel:

\[
\Gamma^{(2)}_{AA}
\]

и показать:

- massless photon pole;
- positive stiffness;
- causal IR cone;
- compatibility с той же physical history.

В текущем canonical tree нет завершённого photon bridge, который мог бы считаться proof.

Поэтому photon/lensing comparisons остаются future physicalization gates.

---

# Глава 38. 2T: вторая дверь, которая пока только нарисована на стене

В проекте есть интересная extension-гипотеза:

может ли relational-history sector быть shadow более глубокой two-time theory?

Но настоящая 2T physics требует не просто второго индекса.

Нужна структура типа:

\[
Q_{11}\sim X^2,
\]

\[
Q_{12}\sim X\cdot P,
\]

\[
Q_{22}\sim P^2,
\]

с

\[
Sp(2,\mathbb R)
\]

gauge closure.

Файлы:

- [README_2T_FRONTIER.md](README_2T_FRONTIER.md)
- [BQG_2T_ALGEBRA_GATE.md](BQG_2T_ALGEBRA_GATE.md)
- [BQG_2T_CLOSURE_SCAN.md](BQG_2T_CLOSURE_SCAN.md)

Сегодня НЕ доказаны:

\[
Sp(2,\mathbb R)\ \text{closure},
\]

\[
(d,2)\ \text{kinetic signature},
\]

ghost-free 2T \(\to\) 1T reduction.

Поэтому корректная фраза:

> BQG имеет relational-history architecture, пригодную для строгого теста 2T embedding.

Некорректная фраза:

> BQG уже является two-time theory.

**Статус: OPEN / falsification programme.**

---

# Глава 39. Shadow action и чёрная дыра, которую ещё надо заслужить

Вторая большая исследовательская линия хочет получить:

\[
(A,\Theta,g_{\mu\nu})
\to
S_{\rm shadow}
\]

и затем решить spherical sector без ручного выбора metric correction:

\[
\boxed{
h_{\rm BQG}(r)
}
\]

должна выйти из equations, а не быть вставлена ansatz'ом.

Только после этого можно честно вычислять:

\[
\Delta T_H,
\]

\[
\Delta r_{\rm ph},
\]

\[
\Delta\Omega_{\rm QNM}.
\]

Пока такой derived \(h_{\rm BQG}(r)\) не существует.

Поэтому black-hole deviations — future observable target, не готовое prediction.

---

# Глава 40. Что значит «реальная физическая теория»

На этом месте важно дать строгий критерий.

Чтобы BQG стала полноценной predictive quantum-gravity candidate, нужны как минимум следующие мосты.

## 40.1. Refinement theorem

Нужно показать, что finite construction не является случайностью одного cutoff.

## 40.2. Physical Hilbert space

Нужен continuum/refinement-compatible physical projector or rigging map.

## 40.3. Physical history

Нужно определить, откуда появляется physical time/history.

## 40.4. Connected generating functional

Нужно построить:

\[
Z[J_g]
\to
W[J_g].
\]

## 40.5. Effective action

Нужно получить:

\[
\Gamma[g].
\]

## 40.6. Physical graviton kernel

Нужно вывести:

\[
K_{TT}(\omega,\mathbf k).
\]

## 40.7. Einstein pole

Leading low-energy part должен восстановить massless Einstein/Fierz–Pauli spin-2 sector.

## 40.8. Microscopic corrections

Только потом читаются:

\[
(c_1,\ldots,c_6)_{\rm IR}.
\]

## 40.9. Один absolute scale

Он выводится или калибруется один раз.

## 40.10. Blind external comparison

И только после freeze theory можно открыть external likelihood/data.

---

# Глава 41. Девять открытых физических ворот

Machine ledger [physicalization_gates.json](physicalization_gates.json) содержит девять настоящих OPEN physical gates:

1. PHYSICAL_PROJECTOR_HISTORY;
2. CONNECTED_INTERBLOCK_HISTORY;
3. PHYSICAL_TT_KERNEL;
4. IR_SIX_VECTOR;
5. COMMON_SCALE_CALIBRATION;
6. DYNAMICAL_MAXWELL_KERNEL;
7. PHYSICAL_BACKGROUND_COSMOLOGY;
8. PHYSICAL_SCALAR_COSMOLOGY;
9. LENSING_DYNAMICS_CLOSURE.

Именно эти ворота определяют, насколько мы далеко от законченной physical theory.

Не количество Markdown-файлов.

Не количество формул.

Не количество зелёных finite tests.

---

# Глава 42. Что уже закрыто в structural candidate package

Machine ledger [theory_gates.json](theory_gates.json) разделяет statuses.

На текущем уровне structural package включает:

- exact/proved gates;
- finite-tested gates;
- explicitly conditional gates.

Это означает:

\[
\boxed{
\text{structural candidate architecture exists}
}
\]

но не:

\[
\boxed{
\text{theory of Nature experimentally established}.
}
\]

Главная дисциплина:

\[
\text{finite structural theorem}
\neq
\text{continuum theorem}
\]

\[
\neq
\text{physical propagator}
\]

\[
\neq
\text{prediction}
\]

\[
\neq
\text{experiment}.
\]

---

# Глава 43. Машинная правда

В этом репозитории документация не должна быть единственным судьёй.

Есть machine-readable ledgers:

- [theory_gates.json](theory_gates.json)
- [physicalization_gates.json](physicalization_gates.json)
- [depth6_frontier.json](depth6_frontier.json)

И verifiers:

- [scripts/verify_theory_gates.py](scripts/verify_theory_gates.py)
- [scripts/verify_physicalization_gates.py](scripts/verify_physicalization_gates.py)
- [scripts/verify_depth6_frontier.py](scripts/verify_depth6_frontier.py)

Если README однажды случайно напишет больше, чем позволяет machine truth, CI должен упасть.

Так и должно быть.

---

# Глава 44. Почему мы переписали depth-6 CI

Исторически S4-sign orchestration пытался интерпретировать sector как full \(H_0\)-injective.

Свежий расчёт доказал:

\[
\boxed{
16\ \text{exact }H_0\text{-null directions}.
}
\]

Поэтому такое утверждение стало неверным.

Workflow был исправлен.

Теперь S4-sign aggregate — это diagnostic H0 layer.

Финальный depth-6 gate не имеет права строить full theorem certificate, пока нет master-aware closure.

Также large shard aggregators переведены на API pagination, потому что стандартный artifact download в реальном run забрал только первые 100 из 128 artifacts.

Для этого добавлен:

- [scripts/download_workflow_artifacts_paginated.py](scripts/download_workflow_artifacts_paginated.py)

Это пример того, как infrastructure bug может выглядеть как scientific failure, если не отделять одно от другого.

---

# Глава 45. Репозиторий как лаборатория, а не музей

Основные активные поверхности:

## Каноническая карта

- [THEORY_STATUS.md](THEORY_STATUS.md)
- [CANONICAL_THEORY_PACKAGE.md](CANONICAL_THEORY_PACKAGE.md)
- [OPEN_PROBLEMS.md](OPEN_PROBLEMS.md)

## Машинные ledgers

- [theory_gates.json](theory_gates.json)
- [physicalization_gates.json](physicalization_gates.json)
- [depth6_frontier.json](depth6_frontier.json)

## Core CI

- [.github/workflows/core-regression.yml](.github/workflows/core-regression.yml)
- [.github/workflows/physicalization-truth.yml](.github/workflows/physicalization-truth.yml)

## Depth-6 CI

- [.github/workflows/bqg-depth6-s4sign-aggregate.yml](.github/workflows/bqg-depth6-s4sign-aggregate.yml)
- [.github/workflows/bqg-depth6-mixed-stage-a.yml](.github/workflows/bqg-depth6-mixed-stage-a.yml)
- [.github/workflows/bqg-depth6-mixed-stage-b-final.yml](.github/workflows/bqg-depth6-mixed-stage-b-final.yml)

## Proof utilities

- [proof_tools/bqg_s4sign_aggregate_streaming.py](proof_tools/bqg_s4sign_aggregate_streaming.py)
- [proof_tools/bqg_mixed_master_aggregate_streaming.py](proof_tools/bqg_mixed_master_aggregate_streaming.py)

---

# Глава 46. Исторический архив

Репозиторий хранит старые версии README и retired research branches в:

- [docs/archive](docs/archive)

Они важны как история исследования.

Но они не являются текущей canonical truth.

Посторонний NEXUS R7.4 benchmark-lab также перенесён в:

- [docs/archive/noncanonical_nexus_r74](docs/archive/noncanonical_nexus_r74)

чтобы active BQG surface не смешивалась с unrelated AI benchmark experiments.

---

# Глава 47. Как воспроизвести быстрый structural core

Основной workflow:

- [.github/workflows/core-regression.yml](.github/workflows/core-regression.yml)

Локально минимально:

    python scripts/audit_core_scope.py
    python scripts/verify_theory_gates.py
    python scripts/verify_depth6_frontier.py
    python scripts/verify_physicalization_gates.py

После этого запускаются конкретные gates.

Например:

    python scripts/q2_dimension3_fixed_point_gate.py

    python scripts/micro_walsh_qgeom_gate.py

    python scripts/logical_shape_metric_jacobian_gate.py

    python scripts/regge_eh_cubic_bridge.py

    python scripts/peter_weyl_three_node_graph_hda_gate.py

    python scripts/s4_tt_quartic_complete_basis_gate.py

Green core regression означает:

> зарегистрированный structural candidate package воспроизведён в заявленном finite/exact/conditional scope.

Он НЕ означает:

> quantum gravity solved.

---

# Глава 48. Карта доказательности

| Уровень | Смысл | Текущий статус |
|---|---|---|
| Binary q=2 fixed-point structure | combinatorial microstructure | сильная exact/finite база |
| Exact tetrahedral Walsh carrier | local geometry seed | PROVED |
| Local SU(2)/Gauss geometry | quantum geometry carrier | PROVED/FINITE |
| Selected global PL gluing | finite manifold carrier | FINITE |
| Metric / Plebanski / Urbantke bridges | geometry reconstruction | FINITE TESTED |
| Regge / EH controls | continuum-direction controls | FINITE TESTED |
| ADM / HDA controls | constraint architecture | FINITE TESTED |
| Depth-4 master-kernel control | finite habitat | CLOSED in tested scope |
| Depth-6 kernel | giant finite habitat | ACTIVE |
| All-depth/refinement theorem | regulator family | OPEN |
| Continuum physical projector | physical Hilbert space | OPEN |
| Theory-specific physical history | time/history | OPEN |
| Connected \(W[J]\) | physical correlations | OPEN |
| Physical \(\Gamma[g]\) | effective action | OPEN |
| Physical \(K_{TT}\) | graviton kernel | OPEN |
| Six Wilson values | microscopic IR prediction | OPEN |
| One physical scale | absolute normalization | OPEN |
| Scalar cosmology | background/perturbations | OPEN |
| Maxwell sector | photon dynamics | OPEN |
| Lensing closure | one metric response | OPEN |
| 2T embedding | optional falsifiable extension | OPEN |
| Shadow black-hole correction | derived observable | FUTURE |
| Blind experiment | confrontation with Nature | NOT STARTED |

---

# Глава 49. Что было бы настоящим следующим прорывом

Не ещё один красивый finite gate.

Не ещё одна coincidence.

Не новый phenomenological ansatz.

Самый сильный математический следующий шаг:

\[
\boxed{
\text{finish finite depth-6}
}
\]

затем

\[
\boxed{
\text{derive refinement / induction theorem}.
}
\]

Самый сильный физический следующий шаг:

\[
\boxed{
P_{\rm phys}^{\rm continuum}
}
\]

и затем

\[
\boxed{
Z[J_g]
\to
W[J_g]
\to
\Gamma[g].
}
\]

Если из этой цепочки emerge:

\[
K_{TT}(\omega,\mathbf k)
\]

с правильным Einstein pole и без ghost/tachyon pathology, проект перейдёт в другой научный класс.

---

# Глава 50. Что могло бы убить теорию

Хорошая теория должна уметь умереть.

BQG должна быть отвергнута или радикально пересмотрена, если, например:

- refinement не стабилизирует physical sector;
- master-kernel начинает расти неконтролируемо;
- HDA anomaly не исчезает;
- physical inner product не положителен;
- continuum TT kernel не имеет massless Einstein pole;
- возникает ghost;
- возникает tachyon;
- leading low-energy cone остаётся anisotropic на недопустимом order;
- microscopic six-vector зависит от regulator без controlled limit;
- требуется отдельная подгонка масштаба для каждого observable;
- scalar sector невозможно согласовать с universal matter response;
- photon и graviton требуют несовместимых histories;
- blind external data исключают frozen predictions.

Это не слабость.

Это научная проверяемость.

---

# Глава 51. Самая короткая формулировка проекта

Если нужно описать BQG в одном абзаце:

> **Binary Quantum Gravity — это воспроизводимая дискретная quantum-gravity candidate architecture, в которой бинарная q=2 микроструктура порождает точный тетраэдрический геометрический carrier, трёхмерный refinement fixed point, SU(2)/Peter–Weyl quantum geometry, graph-changing constraint dynamics и finite GR/HDA/TT controls. Проект уже содержит exact и finite theorems, machine-checked gates и algebraic observable dictionary, но continuum physical Hilbert space, theory-specific physical history, interacting graviton kernel, physical six-Wilson vector и экспериментально замороженное prediction ещё не выведены.**

Ещё короче:

\[
\boxed{
\text{binary information}
\to
\text{quantum geometry}
\to
\text{finite gravity constraints}
\to
\text{unfinished physical continuum}.
}
\]

---

# Глава 52. Самый честный ответ на вопрос «насколько мы близко?»

Нельзя честно сказать:

> сделано 70%.

Нельзя честно сказать:

> осталось 20%.

Потому что разные этапы имеют разную математическую сложность.

Один theorem про continuum refinement может быть труднее сотни finite calculations.

Поэтому вместо процента лучше использовать лестницу.

Мы уже далеко прошли:

\[
\text{idea}
\to
\text{microstructure}
\to
\text{local geometry}
\to
\text{global finite geometry}
\to
\text{constraint operators}
\to
\text{large finite habitats}.
\]

Сейчас мы стоим примерно здесь:

\[
\boxed{
\text{large finite master-kernel programme}
}
\]

и смотрим на следующую гору:

\[
\boxed{
\text{continuum physicalization}.
}
\]

---

# Глава 53. Почему эта история всё-таки необычная

Есть много моделей, которые начинают с continuum fields и потом quantize их.

BQG пытается идти наоборот.

Сначала:

- маленькая discrete information;
- representation structure;
- local geometry;
- gluing;
- constraints.

И только потом пытается заслужить право говорить:

- metric;
- spacetime;
- graviton;
- cosmology;
- black hole.

Это очень строгий путь.

Он может закончиться no-go.

Но если он сработает, результат будет интересен именно потому, что continuum geometry не была вставлена в самое начало.

---

# Глава 54. Маленький словарь для большого путешествия

## q=2

Бинарная локальная структура с четырьмя состояниями \(\mathbb Z_2^2\).

## Walsh carrier

Три нетривиальных characters, образующие тетраэдрический flux-frame.

## Gauss constraint

Локальная gauge-invariance condition.

## Intertwiner

Gauge-invariant способ соединить SU(2) representations на node.

## Peter–Weyl tower

Representation expansion по SU(2) spins.

## PL geometry

Piecewise-linear geometry.

## Regge calculus

Discrete curvature framework для simplicial geometry.

## HDA

Hypersurface-deformation algebra.

## Master constraint

Positive sum

\[
M=\sum_v H_v^\dagger H_v.
\]

## Habitat

Конечное или контролируемое пространство states/operators, на котором выполняется calculation.

## Irrep

Irreducible representation symmetry group.

## TT

Transverse-traceless spin-2 sector.

## Wilson coefficients

Low-energy effective coefficients, кодирующие higher-derivative response.

## Rigging map

Способ построения physical states/inner product для constrained system.

## 1PI effective action

\[
\Gamma[g]
\]

— объект, Hessian которого определяет physical linear response.

## 2T

Two-Time Physics hypothesis с \(Sp(2,\mathbb R)\)-type gauge structure.

---

# Глава 55. Главная карта всей теории

\[
\boxed{
\begin{array}{c}
\text{binary labels}\\
\downarrow\\
q=2\\
\downarrow\\
\text{Walsh tetrahedron}\\
\downarrow\\
\text{SU(2) face qubits}\\
\downarrow\\
\text{Gauss-invariant local geometry}\\
\downarrow\\
\text{PL gluing}\\
\downarrow\\
\text{Peter--Weyl growth}\\
\downarrow\\
\text{graph-changing Hamiltonian}\\
\downarrow\\
\text{finite HDA / GR controls}\\
\downarrow\\
\text{master constraint}\\
\downarrow\\
\text{depth-4 / depth-6 kernels}\\
\downarrow\\
\text{refinement theorem ?}\\
\downarrow\\
P_{\rm phys}^{\rm continuum}\ ?\\
\downarrow\\
Z[J_g]\ ?\\
\downarrow\\
\Gamma[g]\ ?\\
\downarrow\\
K_{TT}(\omega,\mathbf k)\ ?\\
\downarrow\\
(c_1,\ldots,c_6)_{\rm IR}\ ?\\
\downarrow\\
\text{frozen observables}\\
\downarrow\\
\text{experiment}
\end{array}
}
\]

Верхняя половина этой лестницы уже густо населена exact и finite results.

Нижняя половина — текущая frontier.

---

# Глава 56. Правило для будущих авторов

Если вы добавляете новый результат, задайте пять вопросов.

### 1. Это theorem или numerical evidence?

Не смешивать.

### 2. Это finite result или continuum result?

Не смешивать.

### 3. Это constraint object или physical propagator?

Не смешивать.

### 4. Это algebraic observable map или physical prediction?

Не смешивать.

### 5. Это internal consistency или experimental confirmation?

Не смешивать.

Если ответ неясен — status должен быть слабее, а не сильнее.

---

# Глава 57. Правило для будущего ИИ, который будет продолжать проект

Не повышать статус из-за красивого числа.

Не объявлять PASS без сохранённого certificate.

Не заменять master constraint одним \(H_0\), если mixed sector этого не позволяет.

Не считать structural flow numeric rank.

Не считать finite projector continuum rigging map.

Не считать constraint resolvent graviton propagator.

Не считать observable translator prediction.

Не считать 2T analogy \(Sp(2,\mathbb R)\) theorem.

Не считать README доказательством.

Источник истины — код, сертификат, ledger и воспроизводимый gate.

---

# Эпилог. Два бита смотрят на звёзды

В начале истории было почти ничего.

Два бинарных признака.

Четыре состояния.

Три Walsh-character.

Из них появился тетраэдр.

Из тетраэдра — quantum geometry carrier.

Из carrier — связи, representations и constraints.

Из constraints — finite gravitational dynamics.

Из finite dynamics — огромная depth-6 задача размерности

\[
3\,111\,637.
\]

Мы уже научились разрезать её symmetry на irreps.

Три крепости закрыты.

В четвёртой найдено шестнадцать silent directions.

Они оказались не master-kernel.

За ними стоит giant sparse matrix.

А за giant matrix — ещё более высокая гора: continuum.

И именно там решится судьба всей сказки.

Либо binary microstructure действительно сможет пройти путь:

\[
\boxed{
\text{bits}
\to
\text{geometry}
\to
\text{gravity}
\to
\text{physics},
}
\]

либо на одном из gates теория честно остановится.

Оба исхода научны.

Потому что настоящая научная сказка отличается от обычной сказки одним правилом:

\[
\boxed{
\text{конец нельзя придумать заранее}.
}
\]

---

# Канонические источники статуса

Если вы хотите читать не сказку, а сухую карту:

- [THEORY_STATUS.md](THEORY_STATUS.md)
- [CANONICAL_THEORY_PACKAGE.md](CANONICAL_THEORY_PACKAGE.md)
- [OPEN_PROBLEMS.md](OPEN_PROBLEMS.md)
- [theory_gates.json](theory_gates.json)
- [physicalization_gates.json](physicalization_gates.json)
- [depth6_frontier.json](depth6_frontier.json)

Если вы хотите проверить код:

- [scripts](scripts)
- [proof_tools](proof_tools)
- [.github/workflows](.github/workflows)

Если вы хотите увидеть историю развития:

- [docs/archive](docs/archive)

---

# Текущий canonical status в одной таблице

| Вопрос | Ответ |
|---|---|
| Есть ли оформленная candidate architecture? | **Да** |
| Есть ли exact/finite квантово-геометрические результаты? | **Да** |
| Есть ли finite GR/HDA controls? | **Да** |
| Есть ли algebraic TT observable basis? | **Да** |
| Закрыт ли весь depth-6 master kernel? | **Нет** |
| Закрыт ли \([2,1,1,1]\)? | **Нет, ACTIVE** |
| Поднят ли 16D exact \(H_0\)-null obstruction? | **Да, \(H_1\) rank \(16/16\)** |
| Выполнен ли giant sparse rank \(130007\times130007\)? | **Нет** |
| Есть ли all-depth refinement theorem? | **Нет** |
| Есть ли continuum physical projector? | **Нет** |
| Есть ли theory-specific physical history? | **Нет** |
| Есть ли interacting physical graviton kernel? | **Нет** |
| Выведен ли physical six-Wilson vector? | **Нет** |
| Зафиксирован ли absolute scale? | **Нет** |
| Есть ли полноценная scalar cosmology? | **Нет** |
| Доказана ли 2T embedding? | **Нет** |
| Выведен ли \(h_{\rm BQG}(r)\)? | **Нет** |
| Есть ли экспериментальное подтверждение? | **Нет** |
| Есть ли серьёзная воспроизводимая исследовательская программа? | **Да** |

---

# Последняя формула этой версии README

Сегодня наиболее точная граница проекта выглядит так:

\[
\boxed{
\underbrace{
\text{binary microstructure}
\to
\text{finite quantum geometry}
\to
\text{finite gravity constraints}
}_{\text{сильная построенная часть}}
\quad
\Bigg|\quad
\underbrace{
\text{refinement}
\to
P_{\rm phys}
\to
\Gamma[g]
\to
K_{TT}
\to
\text{prediction}
}_{\text{главная открытая физика}}
}
\]

Именно эту вертикальную черту мы сейчас пытаемся перейти.


---

# ТОМ II. Атлас мира BQG  
## Подробный путеводитель для читателя, который дошёл до конца сказки и сказал: «А теперь покажите всё»

Первая половина README рассказала основную историю.

Теперь мы откроем двери лаборатории.

Здесь меньше метафор и больше карт.

Но мы всё ещё будем двигаться от простого к сложному.

---

# Глава 58. Три уровня правды

У BQG есть три разных языка.

Они не должны смешиваться.

## 58.1. Structural truth

Это утверждения вида:

- выбранная microstructure имеет точное свойство;
- конкретный operator обладает определённой rank;
- finite habitat имеет такой-то spectrum;
- symmetry quotient имеет такую-то dimension;
- numerical regression проходит в declared scope.

Structural truth записывается в:

- [theory_gates.json](theory_gates.json)

Текущий core ledger содержит три допустимых класса:

\[
\text{PROVED},
\]

\[
\text{TESTED\_FINITE},
\]

\[
\text{CONDITIONAL}.
\]

Это означает:

> архитектура внутри своей заявленной finite/exact/conditional области построена.

Это не означает:

> физическая Вселенная обязана быть устроена так же.

---

## 58.2. Physical truth

Physical truth начинается там, где нужно определить:

- physical states;
- physical inner product;
- physical time/history;
- physical propagator;
- physical response;
- physical scale.

Machine source:

- [physicalization_gates.json](physicalization_gates.json)

Там существуют статусы:

\[
\text{proved},
\quad
\text{tested\_finite},
\quad
\text{open\_physical},
\quad
\text{experimental\_test}.
\]

Сегодня большая часть genuinely physical gates остаётся OPEN.

---

## 58.3. Experimental truth

Даже если мы получим ideal continuum theory, остаётся вопрос:

> описывает ли она наш мир?

Для этого нужны blind tests.

В частности:

- frozen GW dispersion/birefringence likelihood;
- cosmology/lensing comparison;
- independent implementation;
- held-out predictions after one common scale calibration.

Сегодня:

\[
\boxed{
\text{experimentally confirmed}=false.
}
\]

---

# Глава 59. Почему красивое внутреннее совпадение не является экспериментом

В репозитории есть числа, близкие к физически знакомым значениям.

Например:

\[
d_H\approx2.999229782,
\]

\[
d_s(\text{slice})\approx3.004393867,
\]

\[
z\approx0.998281156.
\]

Очень легко посмотреть на них и сказать:

> вот же, пространство трёхмерное и \(z=1\)!

Но scientific protocol требует осторожности.

Эти числа получены внутри сконструированной microscopic model.

Они являются internal evidence.

Чтобы превратить их в external confirmation, нужно заранее определить blind protocol, открыть независимые данные и проверить prediction, которая не использовалась при построении модели.

Именно поэтому internal near-hit:

\[
\neq
\]

experimental confirmation.

---

# Глава 60. Как q=2 получает размерность три — подробнее

Давайте посмотрим на fixed-point equation внимательнее.

Имеем:

\[
N_g=
\frac{4\cdot8^g+10}{7}.
\]

Для больших \(g\):

\[
N_g
\sim
\frac47 8^g.
\]

Поскольку

\[
8=2^3,
\]

один refinement step asymptotically умножает count на \(2^3\).

Отсюда и возникает three-dimensional exponent.

Но BQG не ограничивается asymptotic argument.

Она использует exact finite-step dimension:

\[
d_g
=
\log_2
\frac{N_g}{N_{g-1}}.
\]

Можно переписать:

\[
d_g
=
3+
\log_2
\left[
1-
\frac{35}
{16\cdot8^{g-1}+40}
\right].
\]

В квадратных скобках число меньше единицы.

Поэтому:

\[
d_g<3.
\]

С ростом \(g\) correction стремится к нулю.

Следовательно:

\[
d_g\nearrow3.
\]

Здесь важен не факт, что numerical fit дал 3.

Важен exact limit.

---

# Глава 61. Почему тетраэдр — не просто красивая картинка

Возьмём четыре binary labels.

Три nontrivial Walsh characters дают четыре points в трёхмерном character space.

Их pairwise scalar products:

\[
n_a\cdot n_b=-\frac13.
\]

Для unit vectors это именно cosine tetrahedral angle.

Кроме того:

\[
\sum_a n_a=0.
\]

То есть центр mass находится в origin.

Эти два свойства фиксируют regular tetrahedron up to orthogonal transformation.

Поэтому tetrahedral geometry не дорисована вручную.

Она следует из character structure.

Но ещё раз:

это local carrier.

Чтобы получить пространство, нужен gluing.

---

# Глава 62. Локальный квантовый тетраэдр и intertwiner space

На four-valent SU(2) node physical local states должны удовлетворять Gauss constraint.

Если внешние spins фиксированы, gauge-invariant space — intertwiner space.

В q=2 carrier возникает маленькая logical Hilbert space.

В ней Pauli-like operators \(X,Y,Z\) удобно интерпретируются как directions в space of shapes/orientation.

Exact metric Jacobian показывает:

\[
X,Z
\]

дают два independent trace-free metric tangents.

Это значит:

\[
\dim T_{\rm local\ shape}=2
\]

в данном minimal carrier.

Именно поэтому позже возникает scalar cosmology obstruction: full symmetric spatial metric имеет больше directions.

---

# Глава 63. Почему Y отличается от X и Z

В intrinsic metric shape важна orientation-insensitive geometry.

Orientation reversal может оставить intrinsic lengths неизменными, но поменять sign oriented volume.

Именно это разделение отражается в logical basis.

Схематично:

\[
X,Z
\to
\text{intrinsic shape}
\]

а

\[
Y
\to
\text{orientation-sensitive direction}.
\]

Это не значит, что \(Y\) «не геометрический».

Это значит, что он относится к другому типу geometric information.

---

# Глава 64. От face qubit к global gluing

Чтобы две tetrahedra делили face, недостаточно совпадения названий.

Нужно согласование:

- carrier state;
- orientation;
- flux;
- incidence map.

В selected 16-cell completion:

\[
16\ \text{tetrahedra},
\]

\[
32\ \text{shared faces}.
\]

Dual adjacency:

\[
Q_4.
\]

Shared-face flux cancellation гарантирует local consistency.

Это напоминает детскую мозаику:

если два кусочка встретились по границе, рисунок на границе должен совпасть.

Только здесь «рисунок» — quantum geometric data.

---

# Глава 65. Почему выбран именно PL-manifold, а не сразу continuum

Потому что continuum нельзя получить честно, если не определено, что именно refine.

PL geometry даёт:

- finite cells;
- finite adjacency;
- finite curvature controls;
- clear refinement operations.

Она является мостом между combinatorics и differential geometry.

BQG сознательно не начинает с smooth \(g_{\mu\nu}(x)\).

Она пытается получить его как collective description.

---

# Глава 66. Первый мост к Einstein geometry

Plebanski-like language удобен тем, что gravity можно выразить через two-form \(B\) и simplicity constraints.

Схема:

\[
\text{qubit/flux data}
\to
B
\to
\text{simplicity}
\to
g_{\mu\nu}.
\]

Urbantke reconstruction позволяет получить metric из подходящего triplet two-forms.

Затем compatible connection и curvature проверяют, соответствует ли geometry Einstein-like sector.

В positive control reconstruction проходит.

В non-Einstein control — нет.

Это важно, потому что gate умеет различать.

---

# Глава 67. Почему unit-S4 Lambda не является cosmological prediction

В некоторых reconstruction controls появляется число, похожее на:

\[
\Lambda\approx3
\]

в определённых unit conventions.

Но это oracle / normalization reconstruction check.

Без:

- physical scale;
- physical vacuum;
- physical continuum history;

нельзя называть это cosmological constant prediction.

Это пример claim discipline.

---

# Глава 68. L1 q4 S4 metric compression

В более коллективном q4 sector получено symmetry-resolved splitting:

\[
\lambda_E
=
1.1111917875584736,
\]

\[
\lambda_{T_2}
=
1.0220278507464782.
\]

Разность:

\[
\Delta_{ET}
=
0.08916393681199541.
\]

Mean-normalized split:

\[
\boxed{
0.08359564595312347
}
\]

то есть около \(8.36\%\).

S4 commutator relative max:

\[
6.89\times10^{-16}.
\]

S4 orbit residual:

\[
1.79\times10^{-16}.
\]

Это сильный finite symmetry certificate.

Но он всё ещё не physical mass splitting.

---

# Глава 69. Regge calculus как контроль памяти пространства

В continuum GR curvature распределена гладко.

В Regge calculus она сидит на hinges.

Если refinement корректен, discrete Hessians должны приближать continuum structure.

В BQG Regge chain используется не как доказательство всего continuum limit, а как проверка правильного направления.

Особенно важен held-out \(L=6\) test.

Он демонстрирует, что fitted finite-size trend обладает predictive continuation хотя бы на следующую lattice size.

Это именно хороший computational-science habit:

train на одном диапазоне,

проверить на unseen point.

---

# Глава 70. Почему HDA — один из самых опасных gate

Можно построить красивую metric geometry и всё равно не получить GR dynamics.

Canonical GR определяется first-class constraint structure.

Поэтому нужно воспроизвести не только Einstein-like tensor, но и algebra of deformations.

Цель:

\[
\{H[N],H[M]\}
\sim
D[\ldots].
\]

Если algebra не closes, theory может содержать anomaly.

Finite HDA tests поэтому являются не украшением, а центральной проверкой.

---

# Глава 71. Finite word cutoff theorem

Graph-changing operators способны поднимать spin.

Для finite operator word длины \(r\) есть support bound:

\[
\boxed{
J_{\max}
\ge
j_{\rm in}
+
\frac r2.
}
\]

Для frozen Euclidean HH word:

\[
j_{\rm in}=\frac12,
\]

\[
r=4,
\]

значит:

\[
J_{\max}
=
\frac52
\]

уже находится за exact support wall.

То есть truncation error above support wall:

\[
0.
\]

Это существенно сильнее statement:

> мы взяли достаточно большой cutoff и кажется converged.

---

# Глава 72. Lorentzian sector и осторожность

Euclidean constraints проще.

Lorentzian part требует extra structure, coefficient controls и larger support.

В текущем package declared conservative Lorentzian support wall:

\[
\boxed{
J_{\max}
=
\frac{13}{2}.
}
\]

Это finite declared wall.

Не unbounded theorem.

Именно поэтому arbitrary-habitat Lorentzian closure остаётся stronger extension.

---

# Глава 73. 32D master normalization

Ранний Peter–Weyl control работает на complete 32D logical sector.

Важно, что nonlinear master normalization выполняется до environment tracing.

Почему?

Потому что trace до nonlinear normalization может изменить spectrum и kernel structure.

Этот gate защищает порядок операций.

Файл:

- [scripts/peter_weyl_master_32_gate.py](scripts/peter_weyl_master_32_gate.py)

---

# Глава 74. Higher-shell Lambda

Historical certified result:

\[
\lambda_{\min}
=
10.635759878291307,
\]

\[
\lambda_{\max}
=
15.059927665966466.
\]

Relative distance from scalar identity:

\[
\boxed{
0.09440461833276048.
}
\]

Block-Lanczos reconstruction closes примерно на scale:

\[
10^{-13}.
\]

Это говорит, что higher-shell operator positive и заметно non-scalar в tested finite sector.

Но снова:

это constraint-spectrum object.

Не physical graviton dispersion.

---

# Глава 75. Что такое branch, orbit и stabilizer человеческим языком

Когда symmetry group действует на states, многие states физически одинаковы up to relabeling.

Orbit — семейство states, получаемых symmetry transformations.

Stabilizer — transformations, которые оставляют state неизменным.

Irrep — irreducible symmetry sector.

Использование orbit decomposition позволяет заменить миллионы raw states тысячами symmetry blocks.

Depth-6:

\[
3\,111\,637
\]

Hilbert states превращаются в

\[
2757
\]

S5 spin orbits для symmetry bookkeeping.

Это колоссальное computational compression.

---

# Глава 76. Почему S5

\(K_5\) имеет пять vertices.

Permutation group пяти vertices:

\[
S_5.
\]

Hamiltonian covariance under relabeling позволяет decomposing Hilbert space по irreps \(S_5\).

Проверенная covariance:

\[
H_{p(v)}U(p)
=
c_v(p)
U(p)H_v,
\]

\[
c_v(p)
=
\operatorname{sgn}(p)
(-1)^{p(v)-v}.
\]

Это фундамент всей representation reduction.

---

# Глава 77. Почему \([5]\) хранит vacuum

Trivial irrep содержит fully symmetric states.

Zero-spin configuration invariant under all permutations.

Hamiltonian не может извлечь geometric excitation из абсолютного zero-spin vacuum в данной finite construction.

Поэтому vacuum line остаётся kernel.

Это не ошибка rank algorithm.

Это expected physical/combinatorial state.

---

# Глава 78. Почему sign irrep оказался проще

\([1^5]\) — one-dimensional sign representation of S5.

Symmetry restrictions делают branch structure очень жёсткой.

В depth-6 sector удалось полностью certify:

\[
26794
\]

multiplicity columns.

Никакого kernel.

Это один из самых чистых full-rank certificates.

---

# Глава 79. Почему mixed sectors труднее

У mixed irrep есть несколько S4 branches.

Один vertex Hamiltonian probes определённое branching.

Null direction одной branch может быть visible другой branch.

Поэтому master sum естественно важнее single \(H_0\).

Именно здесь branch-sum theorem становится центральным.

---

# Глава 80. Jucys–Murphy как навигационные метки

Jucys–Murphy operators позволяют различать branches внутри symmetric-group representation.

Вместо построения огромных projectors можно выбирать branch через eigenvalue labels.

Для mixed sectors это даёт компактные one-row representation carriers.

Таким образом computational problem становится:

\[
\text{orbit multiplicity}
\to
\text{selected branch row}
\to
\text{local Hamiltonian map}.
\]

Это один из ключевых engineering tricks depth-6.

---

# Глава 81. Structural peeling

Представим bipartite graph.

Слева input blocks.

Справа output channels.

Edge означает:

> этот input block геометрически может попасть в этот output.

Если output channel связан только с одним input, он unique.

Если unique rows обладают достаточной capacity и numeric rank, input block можно удалить из active core.

После удаления появляются новые unique rows.

Так возникает peeling cascade.

Это похоже на разбор головоломки:

сначала снимаются очевидные детали,

потом открываются новые очевидные детали,

и постепенно остаётся hard core.

---

# Глава 82. Почему geometric support консервативен

Geometric graph может содержать edge, для которого actual representation-projected matrix оказывается нулевой.

Поэтому geometric support — superset.

Использовать его для uniqueness безопасно в одну сторону:

если row уникальна даже в superset,

она точно уникальна в actual operator.

Но superset может искусственно скрывать uniqueness.

Именно поэтому conservative peeling может оставить большой residual core даже если true operator full rank.

---

# Глава 83. Thresholded actual support и его опасность

В distributed S4-sign maps использовался numerical threshold порядка:

\[
10^{-11}.
\]

Actual support меньше geometric.

Но отсутствие matrix block после threshold не означает exact zero.

Поэтому нельзя автоматически объявить отсутствующий q mathematical zero.

Это стало важным при попытке rescue H0 rank.

Мы отказались от unsafe inference.

---

# Глава 84. Perturbation bound

Если discarded local block имеет Frobenius norm не больше:

\[
10^{-11},
\]

и discarded edges \(N_{\rm omit}\), то global discarded operator obeys:

\[
\|E\|_2
\le
\|E\|_F
\le
10^{-11}\sqrt{N_{\rm omit}}.
\]

Для observed omitted count:

\[
N_{\rm omit}
=
25068.
\]

Получалось:

\[
\boxed{
\|E\|_2
\lesssim
1.5833\times10^{-9}.
}
\]

Это useful robust bound.

Но в итоге выяснилось, что 16 H0-null directions exact, поэтому perturbation не может их спасти.

---

# Глава 85. Hall theorem глазами ребёнка

Есть \(n\) детей и \(n\) стульев.

Каждый ребёнок может сесть только на некоторые стулья.

Hall condition проверяет:

> любой набор детей имеет достаточно доступных стульев?

Если да, существует matching.

В BQG:

- дети — input columns;
- стулья — output row capacity;
- allowed seating — operator support.

Max-flow \(130007/130007\) говорит:

> structural row capacity giant core достаточна.

Но ещё не говорит:

> выбранные matrix rows линейно независимы.

Для этого нужен numerical rank.

---

# Глава 86. Почему giant sparse minor — правильный следующий gate

Full thresholded operator слишком большой.

Но flow выбирает ровно столько rows, сколько columns:

\[
130007.
\]

Получается square matrix.

Если:

\[
\det A_{\rm giant}\neq0
\]

или equivalently

\[
\operatorname{rank}
A_{\rm giant}
=
130007,
\]

giant component injective.

Поскольку 16D exact H0 obstruction уже lifted by H1, master-aware sector closure становится достижимой.

Это dramatically дешевле full dense SVD исходного operator.

---

# Глава 87. Что будет считаться доказательством giant rank

Не достаточно:

- flow;
- row-count;
- absence zero rows;
- random sketch alone;
- one LU without conditioning diagnostics.

Желательно сохранить:

- matrix construction hash;
- row-selection ledger;
- column ordering;
- sparse format checksum;
- rank-revealing factorization output;
- pivot diagnostics;
- numerical tolerance rule;
- independent cross-check;
- residual norm.

Если matrix near-singular, нужен higher precision или exact/modular auxiliary proof.

---

# Глава 88. Как finite theorem должен войти в CI

После настоящего giant certificate machine ledger должен измениться.

Например:

\[
\text{numerical\_rank}
=
130007.
\]

Только тогда verifier разрешит сменить:

\[
[2,1,1,1]:
\quad
\text{ACTIVE}
\to
\text{CLOSED}.
\]

Затем mixed sector certificates должны быть сохранены.

И лишь после all seven irreps:

\[
\boxed{
\text{finite depth-6 common kernel}
=
\operatorname{span}\{|0\rangle\}
}
\]

может стать theorem statement.

---

# Глава 89. Почему мы не будем считать depth 8 тупо первым делом

Если после depth-6 просто перейти к depth-8 brute force, dimension может резко вырасти.

Это даст ещё одну finite точку.

Но не решит all-depth question.

Более ценный поиск:

- monotonic support property;
- inductive block decomposition;
- refinement intertwining;
- stable branch-sum structure;
- uniform lower bound on relevant singular values;
- small-separator theorem;
- regulator-compatible kernel embedding.

То есть задача:

\[
d=4,6
\]

должна стать base case, а не началом бесконечного списка.

---

# Глава 90. Physical projector в деталях

Finite theorem:

\[
M_G
=
C^\dagger G C.
\]

Если \(G>0\), тогда:

\[
\langle\psi|M_G|\psi\rangle
=
\|G^{1/2}C\psi\|^2.
\]

Следовательно:

\[
M_G\psi=0
\]

iff

\[
C_A\psi=0
\]

для всех constraints.

Но continuum theory требует больше.

Нужно определить family:

\[
M^{(d)}.
\]

И maps между physical sectors:

\[
\iota_{d\to d'}.
\]

Хотелось бы compatibility:

\[
P_{\rm phys}^{(d')}
\iota_{d\to d'}
\approx
\iota_{d\to d'}
P_{\rm phys}^{(d)}.
\]

Без такого control physical spaces разных cutoff могут быть несогласованы.

---

# Глава 91. Rigging map человеческим языком

В constrained quantum system physical states часто не лежат как обычные vectors в kinematical Hilbert space.

Rigging map — способ перейти от kinematical states к solutions constraints с правильным inner product.

Схематично:

\[
\eta:
\mathcal H_{\rm kin}
\to
\mathcal H_{\rm phys}^\ast.
\]

Для BQG нужно, чтобы этот construction emerged from actual constraint family и behaved under refinement.

Finite projector theorem показывает algebraic possibility.

Но theory-specific continuum rigging map пока отсутствует.

---

# Глава 92. Почему history должна быть connected

Если blocks независимы:

\[
Z_N
=
\prod_b Z_b.
\]

Тогда:

\[
W_N
=
\sum_b W_b.
\]

Cross-block connected correlators:

\[
\frac{\partial^2 W_N}
{\partial j_b\partial j_c}
=
0
\quad
b\neq c.
\]

Без connected interblock response невозможно получить настоящий momentum-dependent propagation.

Поэтому nearest-neighbor transfer сам по себе ещё не physical history.

Нужна nonfactorizing amplitude.

---

# Глава 93. От W к Gamma

Connected generator:

\[
W[J]
=
-i\hbar\log Z[J].
\]

Mean field:

\[
\bar g
=
\frac{\delta W}{\delta J}.
\]

Legendre transform:

\[
\Gamma[\bar g]
=
W[J]
-
J\cdot\bar g
\]

с соответствующими convention signs.

Hessian:

\[
\Gamma^{(2)}
\]

является inverse connected response на physical subspace.

Только после gauge/constraint reduction этот Hessian можно интерпретировать как physical kernel.

---

# Глава 94. Что такое TT projection

Metric perturbation:

\[
h_{ij}.
\]

TT conditions:

\[
\partial_i h_{ij}=0,
\]

\[
h_{ii}=0.
\]

Остаются две graviton polarizations.

Проектор:

\[
\Pi_{TT}.
\]

Physical TT kernel:

\[
K_{TT}
=
\Pi_{TT}
\Gamma^{(2)}
\Pi_{TT}.
\]

Leading small-\(k\) behavior должен давать massless spin-2 pole.

Если появляется mass term, wrong sign residue или extra ghost pole — theory fails или требует пересмотра.

---

# Глава 95. Почему шесть quartic Wilson structures

Tetrahedral symmetry меньше full rotational symmetry.

Поэтому at quartic order могут жить anisotropic structures.

После:

- parity-even restriction;
- on-shell quotient;
- TT projection;
- field-redefinition redundancy;

остаются шесть independent physical structures.

Это не arbitrary choice числа параметров.

Это dimension quotient space.

---

# Глава 96. Почему три направления недостаточны

Directions:

\[
100,\quad110,\quad111
\]

кажутся естественными high-symmetry probes.

Но extraction matrix на них имеет rank пять.

Чтобы получить полный rank шесть, нужен дополнительный direction, например:

\[
120.
\]

Exact determinant full extraction:

\[
\frac1{699840000}.
\]

Это отличный пример, как symmetry intuition может недосчитать observable space.

---

# Глава 97. Nested models

После получения full six-vector можно проверить более простые hypotheses.

Например scalar cubic:

\[
\bar e_4(\hat n)
=
\eta_2
+
\zeta_4
Q_4^{cub}(\hat n).
\]

Или single-\(Q_{\rm tet}\) splitting.

Но порядок должен быть:

1. сначала freeze full six-vector;
2. потом test nested model.

Нельзя сначала увидеть result, а потом выбрать удобный lower-dimensional ansatz.

---

# Глава 98. Bare control coefficients — не prediction

В reduced TT control встречаются:

\[
\eta_2^{\rm bare}
=
-\frac1{45},
\]

\[
\zeta_4^{\rm bare}
=
-\frac1{12}.
\]

Они относятся к конкретной bare/reduced control model.

Их нельзя молча переносить в interacting physical microscopic coefficients.

Это отдельный пункт claim discipline.

---

# Глава 99. Как появится gravitational-wave test

Если physical six-vector и scale frozen, theory предсказывает:

- sky dependence;
- polarization dependence;
- frequency scaling;
- phase accumulation.

Modified dispersion class:

\[
E^2
=
(pc)^2
+
A_{4,\sigma}(\hat n)
(pc)^4
+
\ldots
\]

где:

\[
A_{4,\sigma}
=
\frac{a_*^2}{(\hbar c)^2}
e_{4,\sigma}.
\]

Тогда можно preregister likelihood.

До freeze шестёрки этого делать нельзя без риска data leakage.

---

# Глава 100. Почему cosmology сложнее gravitational waves

TT sector использует trace-free spin-2 modes.

Scalar cosmology требует:

- conformal mode;
- lapse;
- shift;
- matter coupling;
- constraint reduction;
- background history;
- connected interblock response.

Minimal q=2 \(X/Z\) carrier covers only rank-two trace-free slice.

Поэтому scalar sector обнаружил no-go раньше, чем TT sector.

Это естественно.

---

# Глава 101. Три missing ingredients scalar cosmology

Exact analysis выделил три отсутствующих компонента.

## 101.1. Conformal/volume carrier

В \(X/Z\) его нет.

## 101.2. Lapse/clock response

Independent susceptibility не построена.

## 101.3. Connected interblock physical history

Local product source не создаёт \(k\)-dependence.

Эта декомпозиция очень полезна: она превращает vague «космология не готова» в три конкретных engineering tasks.

---

# Глава 102. Что значит lensing closure

Одна и та же derived metric response должна объяснять:

- massive-body dynamics;
- weak lensing;
- strong lensing;
- CMB lensing;
- Fermat potential;
- time delay;
- wave optics phase.

Нельзя иметь отдельную «линзирующую потенцию», подогнанную независимо от dynamics.

Поэтому physicalization ledger содержит gate:

\[
\text{LENSING\_DYNAMICS\_CLOSURE}.
\]

---

# Глава 103. Maxwell gate

Если theory претендует на full physical world, photon sector не может быть external decoration.

Нужен:

\[
\Gamma_{AA}^{(2)}.
\]

Требования:

- transverse massless pole;
- positive residue/stiffness;
- shared causal low-energy structure;
- same physical history.

Сегодня этот gate:

\[
\boxed{
\text{OPEN}.
}
\]

---

# Глава 104. Почему 2T ветка отделена от core

2T embedding может:

- дать deeper explanation relational history;
- дать parent constrained phase space;
- возможно объяснить shadow structure.

Но core BQG не должен зависеть от 2T, пока 2T не прошла собственные gates.

Иначе возникает circular reasoning:

мы хотим 2T,

поэтому вводим 2T constraints,

потом объявляем, что нашли 2T.

Репозиторий запрещает такой путь.

---

# Глава 105. Минимальный честный 2T эксперимент

Нужно:

1. enumerate actual BQG constraints;
2. build finite matrices;
3. search three-generator independent subspaces;
4. compute commutator closure;
5. check Jacobi;
6. reconstruct canonical \(X,P\);
7. derive signature;
8. gauge-fix;
9. compare reduced dynamics with existing BQG history.

До шага 6 говорить о second time рано.

---

# Глава 106. Shadow-action программа

Если 2T-like or Weyl-compatible parent structure eventually exists, следующая ambition:

\[
S_{\rm parent}
\to
S_{\rm shadow}[A,\Theta,g].
\]

Затем spherical ansatz должен быть решён from equations.

Нельзя написать:

\[
h(r)
\]

руками только потому, что хочется получить красивое black-hole correction.

Correct target:

\[
\boxed{
h_{\rm BQG}(r)
=
\text{solution of derived field equations}.
}
\]

---

# Глава 107. Какие black-hole observables действительно интересны

Если \(h_{\rm BQG}(r)\) существует, можно вычислить:

## Hawking temperature

\[
\Delta T_H.
\]

## Photon sphere

\[
\Delta r_{\rm ph}.
\]

## Quasinormal modes

\[
\Delta\Omega_{\rm QNM}.
\]

Эти quantities гораздо ближе к real phenomenology, чем abstract parent action.

Но без derived \(h(r)\) они premature.

---

# Глава 108. Что означает отрицательный результат

В BQG отрицательный результат должен сохраняться.

Примеры:

- local q=2 source не даёт full scalar cosmology;
- \(H_0\) не injective на total S4-sign;
- 2T closure не заявлена;
- photon bridge отсутствует в canonical tree.

Каждый такой result уменьшает пространство допустимых сказок.

Именно поэтому проект становится научнее.

---

# Глава 109. Почему CI — часть науки

Для large computational theory проблема проста:

через месяц никто не помнит, какая цифра была:

- финальной;
- временной;
- старой;
- полученной с другим cutoff;
- полученной после bugfix.

Поэтому CI должен проверять truth ledger.

Core regression now checks:

- scope hygiene;
- theory gates;
- depth-6 frontier;
- LaTeX/status surfaces;
- binary-to-geometry gates;
- geometry bridges;
- Regge controls;
- Peter–Weyl controls;
- HDA;
- TT;
- Wilson basis;
- selected expensive historical certificates.

---

# Глава 110. Почему artifact pagination оказалась научной проблемой

В distributed proof мы использовали больше 100 shards.

Standard artifact action в одном реальном run скачал только 100.

Если не заметить это, можно ошибочно решить:

> theorem failed.

На деле:

> aggregation input incomplete.

Поэтому добавлен explicit paginated downloader.

Scientific computing требует audit infrastructure так же строго, как formulas.

---

# Глава 111. Почему post-hoc README опасен

Если сначала написать красивую conclusion, а потом подобрать файлы, получается narrative bias.

Правильный порядок:

\[
\text{certificate}
\to
\text{ledger}
\to
\text{README}.
\]

Именно поэтому текущий README ссылается на machine truth.

---

# Глава 112. Основные типы файлов в репозитории

## Theorem / status Markdown

Документируют scope и result.

## Gate scripts

Воспроизводят finite/exact calculation.

## JSON ledgers

Хранят machine-readable status.

## GitHub workflows

Запускают gates.

## Proof tools

Агрегируют distributed evidence.

## Archive

Хранит историю и noncanonical branches.

---

# Глава 113. Как читать файл со словом THEOREM

Название файла само по себе ничего не доказывает.

Нужно проверить:

- statement;
- assumptions;
- proof or computation;
- status;
- reproducer;
- machine ledger registration.

Theorem without scope — опасное слово.

---

# Глава 114. Как читать файл со словом RESULT

Result может быть:

- exact;
- finite numerical;
- positive control;
- held-out regression;
- no-go;
- historical.

Нужно читать status header.

---

# Глава 115. Как читать слово CLOSED

В этом проекте CLOSED всегда должен иметь scope.

Например:

\[
[4,1]\ \text{depth-6 finite sector CLOSED}.
\]

Это не значит:

\[
\text{BQG continuum CLOSED}.
\]

Scope — часть theorem.

---

# Глава 116. Как читать слово CORE

Core означает:

> часть declared structural candidate package.

Core не означает:

> experimentally established fundamental law.

Это distinction encoded в theory_gates.

---

# Глава 117. Как читать слово PHYSICAL

Physical claim должен пройти более строгую цепочку:

\[
P_{\rm phys}
\to
W
\to
\Gamma
\to
\text{gauge reduction}
\to
\text{observable}.
\]

Если какого-то звена нет, слово physical должно использоваться осторожно.

---

# Глава 118. Почему independent replication обязательна

Когда codebase и theory развиваются вместе, есть риск shared implementation bias.

Поэтому сильный future test:

другая команда,

другой код,

те же mathematical definitions,

те же certificates.

Особенно для:

- depth-6 ranks;
- higher-shell operators;
- Regge Hessians;
- TT quotient;
- physicalization chain.

---

# Глава 119. Возможный путь к exact rank proof

Giant sparse rank может быть numerically difficult.

Возможные методы:

- sparse QR;
- rank-revealing LU;
- iterative singular-value estimate;
- modular arithmetic on rationalized entries;
- exact algebraic number representation for local recoupling pieces;
- randomized sketch as auxiliary witness;
- block elimination preserving determinant.

Но final certificate должен понимать conditioning.

---

# Глава 120. Почему singular value важнее одного determinant

Для floating-point matrix determinant может underflow/overflow и плохо отражать conditioning.

Minimal singular value:

\[
\sigma_{\min}
\]

прямо показывает расстояние до rank deficiency.

Если:

\[
\sigma_{\min}
\gg
\text{numerical error},
\]

rank certificate устойчив.

Если:

\[
\sigma_{\min}
\sim
\text{roundoff},
\]

нужна higher precision/exact method.

---

# Глава 121. Что считать настоящим all-depth theorem

Сильный theorem должен включать не только dimensions.

Он должен контролировать:

- support growth;
- branch multiplicities;
- local amplitudes;
- kernel embedding;
- new null directions;
- singular-value behavior;
- regulator maps.

Иначе depth \(d+2\) может неожиданно родить новые physical zero modes.

---

# Глава 122. Возможный физический смысл nontrivial kernel

Если future depths обнаружат non-vacuum common kernel, это не обязательно катастрофа.

Возможно, это и есть physical state sector.

Тогда target:

\[
\ker M
=
\operatorname{span}\{|0\rangle\}
\]

будет неверным physical conjecture.

Нужно будет понять structure kernel.

Проект должен быть готов принять такой result.

---

# Глава 123. Vacuum line и physical universe

Даже если finite kernel only vacuum, это не значит, что physical theory имеет только пустое состояние.

В constrained systems physical observables/history могут кодироваться relationally.

Кроме того continuum limit может изменить structure.

Поэтому finite vacuum-only result — statement о конкретном master kernel, не полный ontology Вселенной.

---

# Глава 124. Почему finite kernel theorem всё равно очень важен

Он показывает:

- отсутствие accidental zero modes;
- rigidity constraint family;
- consistency symmetry reduction;
- nontrivial local constraints;
- feasibility physical projector programme.

Это сильный foundation result.

Просто не последний.

---

# Глава 125. Карта current bottlenecks

## Bottleneck A

\[
130007\times130007
\]

sparse rank.

## Bottleneck B

Mixed sectors:

\[
[3,2],
[3,1,1],
[2,2,1].
\]

## Bottleneck C

All-depth refinement.

## Bottleneck D

Theory-specific physical history.

## Bottleneck E

Physical effective action.

## Bottleneck F

Frozen observables.

---

# Глава 126. Приоритеты по scientific leverage

Если цель — максимальный прогресс минимальными силами, порядок примерно такой.

### Приоритет 1

Закрыть giant sparse rank.

### Приоритет 2

Закрыть три mixed depth-6 sectors generic engine.

### Приоритет 3

Искать induction/refinement theorem.

### Приоритет 4

Строить theory-specific physical projector/history.

### Приоритет 5

Получить physical TT kernel.

### Приоритет 6

Заморозить six-vector и scale.

### Приоритет 7

Blind external tests.

---

# Глава 127. Чего сейчас НЕ надо делать

Не надо:

- бесконечно добавлять новые analogies;
- подгонять black-hole correction;
- искать красивую cosmological fit без scalar kernel;
- объявлять 2T до algebra closure;
- строить phenomenology из bare TT coefficients;
- считать internal coincidences experimental evidence.

Каждый такой shortcut создаёт illusion progress, но не сокращает путь к theory.

---

# Глава 128. Чего сейчас НАДО делать

Надо:

- finish proof certificates;
- freeze assumptions;
- preserve negative results;
- centralize ledgers;
- reduce duplicate documents;
- derive refinement maps;
- construct physical history;
- separate constraints from propagators.

---

# Глава 129. Научная история проекта в одной минуте

1. Начали с binary microstructure.
2. Нашли q=2 geometric carrier.
3. Получили exact 3D refinement fixed point.
4. Построили local quantum geometry.
5. Склеили finite PL manifold.
6. Связали geometry с Plebanski/Urbantke/Regge.
7. Построили finite Peter–Weyl dynamics.
8. Проверили HDA controls.
9. Построили TT observable algebra.
10. Перешли к master-kernel.
11. Закрыли первые depth-6 irreps.
12. Нашли exact H0 obstruction.
13. Подняли его H1.
14. Сжали остаток до giant sparse rank gate.
15. Ещё не перешли continuum physicalization.

---

# Глава 130. Вопросы, которые обычно задаёт ребёнок

## Почему именно два бита?

Потому что q=2 — минимальная выбранная binary route, в которой internal character structure даёт нужный tetrahedral carrier и exact dimension-three refinement rule.

Это construction choice с сильными properties, а не доказательство, что природа обязана начинаться ровно с двух битов.

## Где время?

Пока есть relational-history controls.

Physical time ещё должен быть derived.

## Где материя?

Matter coupling не закрыт.

## Где чёрные дыры?

Пока future shadow-action programme.

## Где эксперимент?

После physical kernel и frozen predictions.

---

# Глава 131. Вопросы, которые обычно задаёт физик

## Где continuum limit?

OPEN.

## Где anomaly-free full constraint algebra?

Finite controls есть; arbitrary/unbounded continuum theorem OPEN.

## Где physical Hilbert space?

OPEN.

## Где interacting propagator?

OPEN.

## Где ghost analysis?

Полный physical kernel ещё не получен, поэтому final ghost analysis впереди.

## Где renormalization/refinement universality?

OPEN extension.

## Где independent code?

OPEN experimental/replication task.

---

# Глава 132. Вопросы, которые обычно задаёт математик

## Какой precise category refinement maps?

Ещё не финализирована для continuum theorem.

## Exact или floating-point amplitudes?

Зависит от gate; многие local structures exact/symbolic, большие rank problems numerical.

## Есть ли uniform bounds?

Не для полного unbounded refinement.

## Есть ли theorem arbitrary graph?

Нет.

## Есть ли proof compactness/convergence projector family?

Нет.

Это frontier.

---

# Глава 133. Вопросы, которые обычно задаёт numerical scientist

## Где tolerances?

В gate scripts и certificates.

## Где held-out tests?

Есть для некоторых Regge / finite extrapolation tasks.

## Где reproducibility?

GitHub workflows + machine ledgers.

## Где sharding?

Depth-6 distributed workflows.

## Где failure logs?

GitHub Actions runs.

## Где independent implementation?

Пока нет.

---

# Глава 134. Система anti-overclaim

В проекте теперь действуют четыре уровня защиты.

### Документальная

README и status files указывают scope.

### Машинная

JSON ledgers.

### CI

Verifiers.

### Методологическая

OPEN/FINITE/PROVED distinctions.

Если один слой ошибся, другой должен поймать.

---

# Глава 135. Почему archive нужен

Научное исследование редко движется по прямой.

Старые hypotheses могут быть:

- полезными;
- ошибочными;
- частично верными;
- superseded.

Удалить их полностью — потерять историю.

Оставить в active root — запутать current truth.

Поэтому архив:

\[
\text{история сохраняется},
\]

но

\[
\text{canonical surface остаётся чистой}.
\]

---

# Глава 136. Почему unrelated AI benchmark был вынесен

В active tree раньше находился NEXUS R7.4 multi-teacher lab.

Он не относится к BQG physics.

Даже если код полезен, его присутствие:

- увеличивало cognitive noise;
- добавляло unrelated workflows;
- размывало scope repository.

Теперь он сохранён в noncanonical archive.

Это hygiene, а не удаление истории.

---

# Глава 137. Что делает core scope audit

Script:

- [scripts/audit_core_scope.py](scripts/audit_core_scope.py)

проверяет, что retired vocabulary/modules не вернулись в active core.

Archive исключён из active scan.

Это не physics theorem.

Это governance theorem репозитория.

Но для долгого проекта это важно.

---

# Глава 138. Как добавить новый gate правильно

Новый gate должен иметь:

1. понятный ID;
2. status;
3. closure role;
4. precise claim;
5. evidence paths;
6. reproducer;
7. hard scope;
8. negative controls если возможно.

После этого update machine ledger.

И только потом README.

---

# Глава 139. Как добавить новое prediction правильно

1. Freeze theory commit.
2. Freeze regulator.
3. Freeze observable extraction.
4. Freeze six-vector.
5. Freeze common scale rule.
6. Freeze likelihood.
7. Only then open external data.

Если порядок нарушен, результат нельзя считать blind prediction.

---

# Глава 140. Что будет означать успешный конец finite saga

Если все depth-6 sectors закрыты:

\[
[1^5],
[5],
[4,1],
[3,2],
[3,1,1],
[2,2,1],
[2,1,1,1]
\]

и только vacuum line survives, тогда:

\[
\boxed{
\ker M^{(d=6)}
=
\operatorname{span}\{|0\rangle\}.
}
\]

Это будет новый canonical theorem.

README тогда должен измениться только после machine certificate.

---

# Глава 141. Что будет означать неуспешный giant rank

Если:

\[
\operatorname{rank}A_{\rm giant}<130007,
\]

мы не будем «лечить» result threshold tuning.

Нужно:

- find nullspace;
- verify precision;
- lift through other \(H_v\);
- understand symmetry;
- determine master nullity.

Возможно giant H0 minor deficient, но master full rank.

16D example уже показал такую возможность.

---

# Глава 142. Почему master-aware logic должна стать стандартом

Mixed sectors доказали:

single vertex не всегда достаточно.

Поэтому future proof architecture должна строить master combinations сразу.

Лучше лишний раз учитывать covariance, чем потом ошибочно принимать \(H_0\)-null за physical null.

---

# Глава 143. Почему branch-sum — больше, чем оптимизация

Positive sum:

\[
B_\lambda
=
\sum_\mu w_\mu A_\mu
\]

с \(w_\mu>0\) даёт:

\[
\ker B_\lambda
=
\bigcap_\mu\ker A_\mu.
\]

Это conceptual simplification kernel problem.

Он превращает master constraint в intersection branch kernels.

Это mathematical structure, не просто faster code.

---

# Глава 144. Возможная связь с renormalization

Representation growth и block transfer намекают на RG-like story.

Но чтобы это стало настоящим renormalization framework, нужны:

- blocking maps;
- coupling flow;
- fixed points;
- universality analysis;
- observable stability.

Пока часть элементов есть, но full RG theorem нет.

Поэтому слова RG используются только в declared local contexts.

---

# Глава 145. Почему dimension-three fixed point ещё не universality

Exact q=2 fixed point доказывает property конкретного refinement count.

Universality потребовала бы:

- семейство microscopic rules;
- basin of attraction;
- robustness perturbations;
- same macroscopic dimension.

Это отдельный extension gate.

---

# Глава 146. Почему q=2 может оказаться слишком специальным

Сильная symmetry часто упрощает model.

Возможно:

- она essential;
- она accidental;
- она one point in universality class.

Только perturbing microstructure покажет.

Поэтому external extension:

\[
\text{MICRO\_DYNAMICAL\_UNIQUENESS}
\]

остаётся open.

---

# Глава 147. Почему arbitrary graph theorem важен

K5 и selected PL families — controlled laboratories.

Но continuum gravity должна работать не только на одном graph family.

Arbitrary graph theorem проверил бы:

- local constraint consistency;
- support growth;
- anomaly behavior;
- topology dependence.

Сегодня это stronger extension.

---

# Глава 148. Почему topology matters

Global manifold properties могут влиять на:

- zero modes;
- holonomies;
- physical sectors;
- boundary states.

Selected cross-polytope completion контролирует один topology class.

General topological universality не доказана.

---

# Глава 149. Boundary states

Physical amplitude требует:

\[
|\Psi_{\rm in}\rangle,
\quad
|\Psi_{\rm out}\rangle.
\]

Выбор boundary states не должен быть скрытой подгонкой.

Нужно freeze:

- semiclassicality criteria;
- geometry labels;
- gauge treatment;
- normalization.

Это часть future physicalization protocol.

---

# Глава 150. Source insertion

Physical generating functional требует source coupling:

\[
J_g\cdot O_g.
\]

Observable \(O_g\) должен быть derived metric operator.

Insertion prescription должен быть symmetric/gauge-compatible.

Без этого derivatives \(W[J]\) могут не быть physical correlators.

---

# Глава 151. Vacuum subtraction

Connected correlators приходят из:

\[
W=\log Z.
\]

Не из raw \(Z\).

Почему?

Потому что \(\log Z\) автоматически отделяет connected diagrams/cumulants.

В finite product model это сразу показывает отсутствие interblock connected response.

---

# Глава 152. Полюс и residue

Physical graviton propagator должен иметь pole:

\[
\omega^2-c^2k^2=0
\]

на leading order.

Residue должен иметь правильный знак.

Если residue negative:

\[
\text{ghost}.
\]

Если pole смещён mass-like term без основания:

\[
\text{wrong IR gravity}.
\]

Эти checks будут частью physical TT gate.

---

# Глава 153. Higher derivatives и EFT

Quartic corrections:

\[
a_*^2k^4
\]

естественно интерпретируются как higher-derivative EFT terms.

Но EFT coefficients physical только после integrating/projecting correct physical degrees of freedom.

Поэтому raw constraint-spectrum anisotropy не равна Wilson coefficient.

---

# Глава 154. Что значит one-scale rule

Если six coefficients dimensionless, нужен один length scale:

\[
a_*.
\]

Можно:

- derive \(a_*/\ell_P\);
- или calibrate one datum.

После этого все другие observables predicted.

Если каждый direction/polarization получает свой fitted \(a_*\), predictive power исчезает.

---

# Глава 155. Blind GW test

Future test должен заранее зафиксировать:

- sky pattern;
- polarization pattern;
- frequency law;
- common scale procedure;
- event selection;
- likelihood;
- priors.

И только потом смотреть data.

Это важно особенно для anisotropic model с шестью coefficients.

---

# Глава 156. Independent cosmology test

Если scalar sector когда-нибудь closed, нужно jointly compare:

- expansion \(H(z)\);
- growth;
- lensing;
- slip;
- CMB;
- possibly GW propagation.

Один common physical action должен объяснять всё.

Не отдельная функция для каждого dataset.

---

# Глава 157. Что делает theory falsifiable

Сейчас falsifiability существует на нескольких уровнях.

## Internal

Gate can fail.

## Mathematical

Refinement theorem can fail.

## Physical

Einstein pole can fail.

## Phenomenological

Prediction can conflict with data.

Это гораздо лучше, чем theory, которую нельзя опровергнуть.

---

# Глава 158. Что BQG пока НЕ утверждает

BQG пока не утверждает:

- окончательное происхождение всех Standard Model fields;
- unique microscopic rule of Nature;
- proven continuum quantum gravity;
- solved black-hole singularity;
- derived dark energy;
- derived dark matter;
- literal second time;
- experimentally detected Lorentz violation;
- measured quantum spacetime.

Любое такое утверждение было бы преждевременным.

---

# Глава 159. Что BQG уже вправе утверждать внутри declared scope

Можно утверждать:

- exact q=2 tetrahedral character geometry;
- exact dimension-three fixed point для frozen count;
- finite global gluing control;
- exact local metric tangent results;
- finite Plebanski/Regge/HDA controls;
- exact finite master-kernel identity;
- closed depth-4 reference result;
- closed depth-6 sectors \([1^5],[5],[4,1]\);
- structural closure mixed sectors;
- exact 16D H0 obstruction и H1 lift;
- six-dimensional quartic TT quotient;
- algebraic observable translator.

Это уже немало.

---

# Глава 160. Чего мы хотим добиться в ближайшем цикле

## Milestone M1

Giant sparse rank certificate.

## M2

Master-aware \([2,1,1,1]\) closure.

## M3

\([3,2]\) closure.

## M4

\([3,1,1]\) closure.

## M5

\([2,2,1]\) closure.

## M6

Full finite depth-6 theorem.

## M7

Refinement induction architecture.

## M8

Physical projector/history.

## M9

Physical TT kernel.

## M10

Frozen six-vector + scale.

---

# Глава 161. Что будет после M10

Тогда впервые появится право написать:

\[
\boxed{
\text{BQG predicts ...}
}
\]

с конкретными numbers/functions.

До этого правильнее:

\[
\boxed{
\text{BQG constructs/tests ...}
}
\]

или

\[
\boxed{
\text{BQG would predict ... if physical coefficients are derived}.
}
\]

---

# Глава 162. Научная сказка как метод документации

Почему README написан именно так?

Потому что large theory легко становится unreadable.

Если документы читают только авторы, errors могут жить долго.

Narrative structure заставляет отвечать:

- откуда появился объект;
- зачем он нужен;
- что он доказывает;
- чего не доказывает;
- куда ведёт дальше.

Это полезно даже expert reader.

---

# Глава 163. Два режима чтения

## Режим A: история

Читайте главы по порядку.

## Режим B: аудит

Сразу откройте:

- machine ledgers;
- gate scripts;
- workflows;
- proof tools;
- status files.

Обе траектории должны привести к одной и той же картине.

---

# Глава 164. Карта файлов по физическим слоям

## Microstructure

- BIT_TO_SPACETIME_CENTRAL_EQUATION.md
- OBSERVER_SCALE_SMOOTHING.md
- Q2_DIMENSION3_FIXED_POINT_CLOSURE.md

## Local geometry

- MICRO_WALSH_QGEOM_BRIDGE.md
- LOGICAL_SHAPE_METRIC_JACOBIAN.md
- FACE_QUBIT_BFIELD.md

## Global geometry

- GLOBAL_MANIFOLD_Q2_COMPLETION.md
- SPATIAL_QUBIT_GEOMETRY_BRIDGE.md

## Metric/GR bridges

- PLEBANSKI_URBANTKE_BRIDGE.md
- PLEBANSKI_CONNECTION_EINSTEIN_GATE.md
- REGGE_EH_CUBIC_BRIDGE.md
- DEWITT_HDA_UNIQUENESS.md

## Quantum dynamics

- K5_PETER_WEYL_SAFE_HDA_FIRST_COLUMN.md
- PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md
- THREE_NODE_GRAPH_HDA_RESULT.md
- JOINT_REGULATOR_LIMIT.md

## Physical projector

- MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md
- Q2_RELATIONAL_HISTORY_PROJECTOR.md
- HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md

## TT/observables

- TT_PROPAGATOR_FIRST_PASS.md
- S4_TT_QUARTIC_COMPLETE_BASIS.md
- TT_TO_REAL_PHYSICS_OBSERVABLES.md

## Cosmology

- Q2_FIRST_SCALAR_EFFECTIVE_ACTION.md
- Q2_COLLECTIVE_SCALAR_CARRIER.md
- BQG_SCALAR_RESPONSE_TO_MATTER.md

## 2T

- README_2T_FRONTIER.md
- BQG_2T_ALGEBRA_GATE.md
- BQG_2T_CLOSURE_SCAN.md

---

# Глава 165. Машинные команды здоровья репозитория

Минимальный health check:

    python scripts/audit_core_scope.py
    python scripts/verify_theory_gates.py
    python scripts/verify_depth6_frontier.py
    python scripts/verify_physicalization_gates.py
    python scripts/validate_github_latex.py README.md THEORY_STATUS.md OPEN_PROBLEMS.md CANONICAL_THEORY_PACKAGE.md

Если это не проходит, narrative surface нельзя считать canonical.

---

# Глава 166. Почему LaTeX validator нужен

README содержит много equations.

GitHub rendering может ломаться из-за:

- unmatched delimiters;
- unsupported macros;
- malformed escapes.

Validator не доказывает physics.

Но он делает scientific surface читаемым.

---

# Глава 167. Как понимать GREEN core regression

GREEN означает:

\[
\boxed{
\text{registered internal structural package reproduced}.
}
\]

Не означает:

\[
\boxed{
\text{Nature confirmed BQG}.
}
\]

Эта фраза должна быть мысленно приклеена к каждому зелёному badge.

---

# Глава 168. Как понимать FAIL

FAIL может быть:

- mathematical;
- numerical;
- infrastructure;
- missing artifact;
- stale reference;
- timeout.

Поэтому сначала нужно классифицировать failure.

Пример 128-shard incident показал это очень наглядно.

---

# Глава 169. Как сохранять evidence

Для expensive run нужно сохранять:

- source commit;
- input manifest;
- parameters;
- shards;
- aggregation script;
- final certificate;
- hashes.

Только так result survives context loss.

---

# Глава 170. Почему chat не является архивом теории

Разговор полезен для исследования.

Но canonical result должен жить:

- в repository;
- в machine ledger;
- в artifact/certificate.

Иначе после timeout можно потерять точку доказательства.

Именно поэтому новые frontier ledgers критически важны.

---

# Глава 171. Чему научил depth-6 процесс

Самые важные уроки:

1. symmetry reduction важнее brute force;
2. single-vertex injectivity может быть ложной целью;
3. structural flow полезен, но не равен rank;
4. distributed computation требует artifact audit;
5. negative results экономят время;
6. machine truth должен обновляться раньше prose.

---

# Глава 172. Возможный общий theorem из branch-sum

Если future work сможет показать uniform lower bounds для branch operators, positive branch-sum structure может стать основой all-depth induction.

Идея схематична:

\[
B_\lambda^{(d)}
=
\sum_\mu
w_{\lambda\mu}
A_{\lambda\mu}^{(d)}.
\]

Если kernels branches контролируются under refinement, можно попытаться prove stability master kernel.

Это пока research direction.

Не theorem.

---

# Глава 173. Возможный separator theorem

Другой путь — графовая структура support.

Если при росте depth residual cores имеют uniformly small separators, giant rank proofs можно reduce к reusable local relations.

Это computational hypothesis.

Её стоит исследовать после depth-6.

---

# Глава 174. Возможный exact arithmetic route

Local SU(2) recoupling amplitudes часто выражаются через radicals/rational combinations.

Если удастся map giant matrix к exact algebraic field или modular representation, numerical rank можно подкрепить exact determinant/rank proof.

Это потенциально очень сильный upgrade.

---

# Глава 175. Почему higher precision не всегда решение

130k square matrix при arbitrary precision может быть слишком дорогой.

Нужно использовать structure:

- blocks;
- sparsity;
- symmetry;
- elimination order;
- modular projections.

Просто «посчитать с 200 digits» может быть computationally бессмысленно.

---

# Глава 176. Что делать, если giant rank near-singular

1. Estimate \(\sigma_{\min}\).
2. Find candidate null vectors.
3. Verify residual in high precision.
4. Classify by symmetry.
5. Test other vertex maps.
6. Determine master lift.
7. Only then change sector status.

---

# Глава 177. Почему H1 lift 16D так ценен

Он показывает concrete example:

\[
\ker H_0
\neq
\ker M.
\]

Это не abstract warning.

Это actual depth-6 phenomenon.

Поэтому future algorithms должны быть master-aware by construction.

---

# Глава 178. Почему [3,2] особенно полезен как следующий mixed sector

Он уже использовался как laboratory для:

- S3/Jucys selectors;
- H0 deficiencies;
- H2 lifts;
- branch-sum ideas.

Поэтому после S4-sign closure generic mixed engine лучше всего валидировать именно там.

---

# Глава 179. Почему старый H2-null-lift путь не бесполезен

Он superseded как основной workflow.

Но он остаётся diagnostic evidence:

- показывает genuine H0 deficiencies;
- демонстрирует vertex complementarity;
- подтверждает master logic.

То есть superseded не значит worthless.

---

# Глава 180. Что значит «канонический»

Canonical в этом repository значит:

- current source of truth;
- not historical;
- not experimental branch;
- consistent with machine ledgers.

Canonical result может позже быть superseded новым более сильным result.

---

# Глава 181. Почему README не должен быть единственным entry point

Large theory требует несколько levels.

README — narrative.

THEORY_STATUS — concise truth.

CANONICAL_THEORY_PACKAGE — evidence index.

OPEN_PROBLEMS — frontier.

JSON — machine truth.

Scripts — reproduction.

Это здоровая architecture documentation.

---

# Глава 182. Как будущий reviewer может атаковать BQG

Самые полезные критические вопросы:

- Why q=2?
- How universal is 3D fixed point?
- Are refinement maps unique?
- Does HDA close beyond selected habitats?
- Is physical Hilbert space nontrivial?
- Does continuum kernel recover GR exactly?
- Are higher-order corrections stable?
- Is matter coupling universal?
- Are predictions parameter-free after one scale?
- Can another implementation reproduce ranks?

Проект должен приветствовать такие атаки.

---

# Глава 183. Какой paper был бы логичен первым

Не «Theory of Everything».

Гораздо сильнее научно:

> Finite master-kernel structure of a binary-derived K5 quantum geometry at depth 6.

С точными:

- Hilbert counts;
- S5 decomposition;
- branch-sum theorem;
- closed irreps;
- master-aware obstruction lifts;
- distributed sparse rank certificates.

Это конкретный publishable mathematical-computational result, если довести proof до конца.

---

# Глава 184. Какой paper мог бы быть вторым

> From binary q=2 characters to tetrahedral SU(2) quantum geometry and a three-dimensional refinement fixed point.

Фокус:

- exact Walsh geometry;
- d*=3 theorem;
- gluing;
- local metric Jacobian.

---

# Глава 185. Какой paper был бы физически главным

После physicalization:

> A physical TT kernel and frozen quartic gravitational-wave signatures from binary quantum gravity.

Но этот paper пока рано писать.

---

# Глава 186. Какой result изменит оценку проекта сильнее всего

Не ещё один finite number.

А успешная chain:

\[
\boxed{
P_{\rm phys}^{\rm continuum}
\to
\Gamma[g]
\to
K_{TT}
}
\]

с Einstein pole.

Это watershed.

До него BQG — sophisticated candidate framework.

После него — predictive quantum-gravity candidate.

---

# Глава 187. Почему экспериментальный успех без этого был бы подозрительным

Если заранее подобрать phenomenological \(h(r)\), dispersion или cosmology и найти fit, это не проверит microscopic theory.

Нужно prediction from internal dynamics.

Иначе data fitting подменяет derivation.

---

# Глава 188. Что значит «из битов в гравитацию» строго

Не:

\[
\text{bit}
=
\text{graviton}.
\]

А:

\[
\text{binary combinatorics}
\to
\text{representation carrier}
\to
\text{quantum geometry}
\to
\text{constraint dynamics}
\to
\text{coarse geometric response}.
\]

Это длинная chain.

Каждый arrow требует своего gate.

---

# Глава 189. Почему проект называется Binary Quantum Gravity

Binary — microscopic information rule.

Quantum — Hilbert spaces, SU(2), constraints, operator spectra.

Gravity — target emergent geometric/HDA/TT sector.

Название — research programme, не assertion completion.

---

# Глава 190. Финальная карта для ребёнка

Если совсем просто:

1. Мы взяли четыре знака.
2. Они неожиданно сложились в тетраэдр.
3. Мы научили тетраэдры склеиваться.
4. Мы сделали их квантовыми.
5. Мы дали им правила движения.
6. Мы проверили, что правила напоминают нужную геометрию GR.
7. Мы построили огромный экзамен из миллионов состояний.
8. Часть экзамена уже сдана.
9. Самый трудный вопрос ещё решается.
10. Даже после экзамена нужно доказать, что бесконечная теория существует.
11. И только потом спросить Вселенную, согласна ли она.

---

# Глава 191. Финальная карта для эксперта

\[
\boxed{
\begin{aligned}
&\mathbb Z_2^2
\to
\text{Walsh tetrahedral frame}
\to
\text{SU(2) intertwiner carrier}
\\
&\to
\text{PL gluing}
\to
\text{Peter--Weyl representation growth}
\to
\text{graph-changing constraints}
\\
&\to
\text{finite HDA/Regge/Plebanski controls}
\to
M=\sum_vH_v^\dagger H_v
\\
&\to
S_5\text{-resolved finite kernel programme}
\to
\text{refinement-compatible physical projector}
\\
&\to
W[J_g]
\to
\Gamma[g]
\to
K_{TT}
\to
\mathbf c_{\rm IR}
\to
\text{observables}.
\end{aligned}
}
\]

Current frontier sits between line three and line four.

---

# Глава 192. Последний научный принцип

В этой теории нельзя выигрывать спор красивым словом.

Только следующим более сильным объектом.

Не:

> «похоже на пространство».

А:

\[
\text{metric map}.
\]

Не:

> «похоже на GR».

А:

\[
\text{HDA / Einstein controls}.
\]

Не:

> «похоже на physical state».

А:

\[
P_{\rm phys}.
\]

Не:

> «похоже на graviton».

А:

\[
K_{TT}.
\]

Не:

> «можно подобрать correction».

А:

\[
h_{\rm BQG}(r)
\text{ derived from equations}.
\]

Не:

> «данные вроде согласуются».

А:

\[
\text{blind frozen likelihood}.
\]

Именно так сказка превращается в физику.

---

# Большое приложение A. Текущие числовые ориентиры

## Microstructure

\[
d_H=2.999229782
\]

\[
d_s(\text{slice})=3.004393867
\]

\[
z=0.998281156
\]

\[
d_s(\text{history})\approx4.004393867
\]

Эти значения — internal finite diagnostics.

## L1 q4 S4 metric

\[
\lambda_E=1.1111917875584736
\]

\[
\lambda_{T_2}=1.0220278507464782
\]

\[
\Delta_{ET}=0.08916393681199541
\]

\[
\text{relative split}=0.08359564595312347
\]

## Higher-shell Lambda

\[
\lambda_{\min}=10.635759878291307
\]

\[
\lambda_{\max}=15.059927665966466
\]

\[
\text{relative nonscalarity}=0.09440461833276048
\]

## Three-node HDA

\[
\text{route exponent}=0.9999571195
\]

\[
\text{cross exponent}=1.0024037289
\]

\[
\text{pure geometry exponent}=2.0061524985
\]

\[
\text{joint exponent}=1.0064429344
\]

## Depth-6

\[
N_{\rm Gauss}=264962
\]

\[
\dim\mathcal H=3111637
\]

\[
N_{S_5\text{ orbits}}=2757
\]

## S4-sign obstruction

\[
16\ \text{exact }H_0\text{-null directions}
\]

\[
\operatorname{rank}H_1=16/16
\]

\[
\sigma_{\min}=1.1304521906426823
\]

## Giant component

\[
11923\ \text{blocks}
\]

\[
130007\ \text{columns}
\]

\[
14586\ q\text{-blocks}
\]

\[
153056\ \text{sum numerical q-row ranks}
\]

\[
130007/130007\ \text{rank-aware max-flow}
\]

\[
47\,543\,521\ \text{expected scalar nonzeros in square plan}
\]

---

# Большое приложение B. Статусные слова

## PROVED

Exact theorem в declared scope.

## TESTED_FINITE

Numerically/reproducibly verified finite statement.

## CONDITIONAL

True given explicitly stated assumption.

## ACTIVE

Calculation underway; no final theorem.

## OPEN_PHYSICAL

Required physical result missing.

## EXPERIMENTAL_TEST

Future external validation.

## CLOSED

Only with explicit scope.

---

# Большое приложение C. Красные линии

Нельзя писать:

\[
\text{BQG доказана}
\]

пока continuum physicalization open.

Нельзя писать:

\[
\text{2T доказана}
\]

пока нет \(Sp(2,\mathbb R)\) closure.

Нельзя писать:

\[
\text{black-hole correction predicted}
\]

пока нет derived \(h_{\rm BQG}(r)\).

Нельзя писать:

\[
\text{dark energy explained}
\]

пока physical FLRW action open.

Нельзя писать:

\[
\text{GW dispersion predicted}
\]

пока physical six-vector open.

---

# Большое приложение D. Зелёные линии

Можно писать:

\[
\text{exact q=2 tetrahedral character carrier}
\]

в declared construction.

Можно писать:

\[
d_*=3
\]

для frozen q=2 refinement count.

Можно писать:

\[
\text{finite depth-6 }[1^5],[5],[4,1]\text{ CLOSED}.
\]

Можно писать:

\[
16D\ H_0\text{ obstruction lifted by }H_1.
\]

Можно писать:

\[
\dim\mathcal V_{TT}^{(4)}=6.
\]

Можно писать:

\[
\text{physicalization remains open}.
\]

---

# Большое приложение E. Чек-лист перед новым релизом

- [ ] core-regression GREEN
- [ ] verify_theory_gates PASS
- [ ] verify_depth6_frontier PASS
- [ ] verify_physicalization_gates PASS
- [ ] README status matches machine ledgers
- [ ] THEORY_STATUS synchronized
- [ ] CANONICAL_THEORY_PACKAGE synchronized
- [ ] OPEN_PROBLEMS synchronized
- [ ] no broken evidence links
- [ ] no historical file promoted as canonical
- [ ] no physical claim inferred from structural result
- [ ] no experiment claim inferred from internal control
- [ ] all expensive certificates preserved

---

# Большое приложение F. Если вы хотите помочь проекту

Самые полезные contributions:

1. independent sparse-rank implementation;
2. exact/modular rank methods;
3. refinement-map formalization;
4. independent HDA audit;
5. physical rigging-map construction;
6. connected history amplitude;
7. TT effective-action derivation;
8. scalar carrier completion;
9. independent replication;
10. rigorous external preregistration design.

---

# Большое приложение G. Сказка в десяти формулах

Первая:

\[
\mathbb Z_2^2.
\]

Вторая:

\[
n_a\cdot n_b=-\frac13.
\]

Третья:

\[
\lim_{g\to\infty}d_g=3.
\]

Четвёртая:

\[
M=\sum_vH_v^\dagger H_v.
\]

Пятая:

\[
\ker M=\bigcap_v\ker H_v.
\]

Шестая:

\[
\dim\mathcal H_{d=6}=3111637.
\]

Седьмая:

\[
B_\lambda
=
\frac5{d_\lambda}
\sum_{\mu\to\lambda}
d_\mu A_{\lambda,\mu}.
\]

Восьмая:

\[
P_{\rm phys}^{(d)}
\to
P_{\rm phys}^{\rm continuum}\ ?.
\]

Девятая:

\[
K_{TT}
=
\Pi_{TT}
\Gamma^{(2)}
\Pi_{TT}.
\]

Десятая:

\[
\text{prediction}
\stackrel{?}{=}
\text{Nature}.
\]

Между первой и десятой формулой находится вся наша научная сказка.


---

# ТОМ III. Полный реестр ворот  
## Machine-ledger, переведённый на человеческий язык

Этот том автоматически собран из текущих machine-readable ledgers.

Его назначение простое:

если в сказке выше встречается красивое утверждение, здесь можно найти его официальный gate, статус и evidence-path.

---

# Часть I. Structural candidate gates

Ниже перечислены все зарегистрированные gates из theory_gates.json.


## BITQ2

**Статус:** tested_finite  
**Роль:** core

Frozen q=2 binary-route train/held-out dimensional and observer-smoothing controls pass in the declared protocol.

**Evidence:**

- [BIT_TO_SPACETIME_CENTRAL_EQUATION.md](BIT_TO_SPACETIME_CENTRAL_EQUATION.md)
- [OBSERVER_SCALE_SMOOTHING.md](OBSERVER_SCALE_SMOOTHING.md)
- [bcqg_observer_smoothing_unified.py](bcqg_observer_smoothing_unified.py)


## DIM3_FIXED_POINT

**Статус:** proved  
**Роль:** core

For the frozen q=2 refinement count N_g=(4*8^g+10)/7, the finite-step dimension increases monotonically from below to the exact fixed point d*=3.

**Evidence:**

- [Q2_DIMENSION3_FIXED_POINT_CLOSURE.md](Q2_DIMENSION3_FIXED_POINT_CLOSURE.md)
- [scripts/q2_dimension3_fixed_point_gate.py](scripts/q2_dimension3_fixed_point_gate.py)


## MAN3

**Статус:** tested_finite  
**Роль:** core

The selected q=2 cross-polytope PL completion is a recursive orientable 3-manifold completion with the declared link and homology checks.

**Evidence:**

- [GLOBAL_MANIFOLD_Q2_COMPLETION.md](GLOBAL_MANIFOLD_Q2_COMPLETION.md)
- [bcqg_global_manifold_gate.py](bcqg_global_manifold_gate.py)


## MICRO_WALSH_TETRA

**Статус:** proved  
**Роль:** core

The three nontrivial Walsh characters of the frozen q=2 labels form an exact closed regular-tetrahedron flux frame and the declared qubit lift has exact Gauss-singlet geometry support.

**Evidence:**

- [MICRO_WALSH_QGEOM_BRIDGE.md](MICRO_WALSH_QGEOM_BRIDGE.md)
- [scripts/micro_walsh_qgeom_gate.py](scripts/micro_walsh_qgeom_gate.py)


## MICRO_GLOBAL_GLUE

**Статус:** proved  
**Роль:** core

On the selected 16-cell PL completion, q=2 face carriers glue exactly with Q4 dual graph, alternating orientation and pairwise shared-face flux cancellation.

**Evidence:**

- [MICRO_WALSH_QGEOM_BRIDGE.md](MICRO_WALSH_QGEOM_BRIDGE.md)
- [scripts/q2_global_face_qubit_gluing_gate.py](scripts/q2_global_face_qubit_gluing_gate.py)


## Q2_GRAPHLINK_REP

**Статус:** proved  
**Роль:** core

Four active q=2 states plus the graph-changing no-link singlet give the exact SO(5) (2,2)+(1,1) endpoint representation and factor the frozen q=2 Hamming adjacency through two graph-changing transporter steps.

**Evidence:**

- [Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md](Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md)
- [scripts/q2_graphlink_peter_weyl_gate.py](scripts/q2_graphlink_peter_weyl_gate.py)
- [scripts/su2_quantum_link_vector5_gate.py](scripts/su2_quantum_link_vector5_gate.py)


## PW_SYM_BLOCK_GROWTH

**Статус:** conditional  
**Роль:** core

Under the explicitly declared fully symmetric endpoint blocking, occupancy n=0..N supplies exactly the diagonal Peter-Weyl j=0,1/2,...,N/2 tower with correct dimensions and SU(2) Casimirs.

**Evidence:**

- [Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md](Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md)
- [scripts/q2_symmetric_block_peter_weyl_growth_gate.py](scripts/q2_symmetric_block_peter_weyl_growth_gate.py)


## Q2EIN

**Статус:** tested_finite  
**Роль:** core

A single-data-path Euclidean control reconstructs B, simplicity, Urbantke metric, compatible connection and Einstein curvature from face-qubit data, with an independent non-Einstein negative control.

**Evidence:**

- [QUBIT_TO_EINSTEIN_END_TO_END.md](QUBIT_TO_EINSTEIN_END_TO_END.md)
- [scripts/qubit_to_einstein_end_to_end.py](scripts/qubit_to_einstein_end_to_end.py)


## LOGICAL_METRIC_JACOBIAN

**Статус:** proved  
**Роль:** core

The logical X/Z shape doublet maps with exact rank two to orthogonal equal-norm trace-free tangents of the reconstructed tetrahedral metric, with the same intrinsic Jacobian on both orientation branches.

**Evidence:**

- [LOGICAL_SHAPE_METRIC_JACOBIAN.md](LOGICAL_SHAPE_METRIC_JACOBIAN.md)
- [scripts/logical_shape_metric_jacobian_gate.py](scripts/logical_shape_metric_jacobian_gate.py)


## L1_METRIC_PRECURSOR

**Статус:** tested_finite  
**Роль:** core

The certified L1 q4 six-edge S4 compression resolves E and T2 metric channels with lambda_E=1.1111917875584736, lambda_T2=1.0220278507464782, Delta_ET=0.08916393681199541 and mean-normalized relative_ET_split=0.08359564595312347.

**Evidence:**

- [L1_Q4_S4_METRIC_COMPRESSION_RESULT.md](L1_Q4_S4_METRIC_COMPRESSION_RESULT.md)
- [scripts/collective_l1_q4_s4_metric_compression.py](scripts/collective_l1_q4_s4_metric_compression.py)


## REGGEEH

**Статус:** tested_finite  
**Роль:** core

The implemented Regge/Einstein-Hilbert refinement controls reproduce the declared finite continuum-scaling relations on their test geometries.

**Evidence:**

- [REGGE_EH_CUBIC_BRIDGE.md](REGGE_EH_CUBIC_BRIDGE.md)
- [scripts/regge_eh_cubic_bridge.py](scripts/regge_eh_cubic_bridge.py)


## PLEBANSKI

**Статус:** tested_finite  
**Роль:** core

Finite simplicity/Urbantke/connection controls reconstruct the declared metric-sector quantities and distinguish Einstein from non-Einstein controls.

**Evidence:**

- [PLEBANSKI_URBANTKE_BRIDGE.md](PLEBANSKI_URBANTKE_BRIDGE.md)
- [PLEBANSKI_CONNECTION_EINSTEIN_GATE.md](PLEBANSKI_CONNECTION_EINSTEIN_GATE.md)
- [scripts/plebanski_urbantke_gate.py](scripts/plebanski_urbantke_gate.py)
- [scripts/plebanski_connection_einstein_gate.py](scripts/plebanski_connection_einstein_gate.py)


## PWGEO

**Статус:** tested_finite  
**Роль:** core

Finite Peter-Weyl SU(2) geometry, Euclidean Hamiltonian, volume/extrinsic-curvature and covariant composition gates pass within the declared cutoff domains.

**Evidence:**

- [PETER_WEYL_TRUNCATION_GATE.md](PETER_WEYL_TRUNCATION_GATE.md)
- [K5_PETER_WEYL_SAFE_HDA_FIRST_COLUMN.md](K5_PETER_WEYL_SAFE_HDA_FIRST_COLUMN.md)
- [scripts/peter_weyl_lorentzian_K_block_gate.py](scripts/peter_weyl_lorentzian_K_block_gate.py)
- [scripts/peter_weyl_covariant_composition_gate.py](scripts/peter_weyl_covariant_composition_gate.py)
- [scripts/peter_weyl_covariant_K_composition_gate.py](scripts/peter_weyl_covariant_K_composition_gate.py)


## PW_MASTER32

**Статус:** tested_finite  
**Роль:** core

The nonlinear two-shell Peter-Weyl master normalization is applied on the complete 32D logical sector before environment tracing and its support-projector limit passes the finite control.

**Evidence:**

- [scripts/peter_weyl_master_32_gate.py](scripts/peter_weyl_master_32_gate.py)
- [CANONICAL_THEORY_PACKAGE.md](CANONICAL_THEORY_PACKAGE.md)


## PW_HIGHER_SHELL

**Статус:** tested_finite  
**Роль:** core

The completed 32D higher-shell Lambda is positive and non-scalar with lambda_min=10.635759878291307, lambda_max=15.059927665966466 and block-Lanczos reconstruction at approximately 1e-13 residual scale.

**Evidence:**

- [PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md](PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md)
- [scripts/peter_weyl_higher_shell_lambda_gate.py](scripts/peter_weyl_higher_shell_lambda_gate.py)


## PW_J1_S4

**Статус:** tested_finite  
**Роль:** core

The four-j=1 singlet space contains the multiplicity-one S4 [2,2] coarse doublet used as the representation-RG geometry carrier.

**Evidence:**

- [PETER_WEYL_J1_S4_BLOCK_RESULT.md](PETER_WEYL_J1_S4_BLOCK_RESULT.md)
- [scripts/peter_weyl_j1_s4_block_gate.py](scripts/peter_weyl_j1_s4_block_gate.py)


## ROUTE

**Статус:** tested_finite  
**Роль:** core

Independent dual-cell sharp, path-diffeomorphism and route-normal HDA principal-symbol gates pass on the declared probes.

**Evidence:**

- [DUAL_CELL_SHARP_RT0.md](DUAL_CELL_SHARP_RT0.md)
- [QUANTUM_HDA_KILLER_RESULT.md](QUANTUM_HDA_KILLER_RESULT.md)
- [scripts/path_normal_hda_gate.py](scripts/path_normal_hda_gate.py)
- [scripts/path_rerouting_diffeo_gate.py](scripts/path_rerouting_diffeo_gate.py)
- [scripts/path_vector_diffeo_gate.py](scripts/path_vector_diffeo_gate.py)


## E2NODE

**Статус:** tested_finite  
**Роль:** core

The preregistered two-node Euclidean Peter-Weyl by route HDA regression exhibits the declared route, cross and pure-geometry scaling hierarchy without channel-dependent fitting.

**Evidence:**

- [PETER_WEYL_TWO_NODE_EUCLIDEAN_RESULT.md](PETER_WEYL_TWO_NODE_EUCLIDEAN_RESULT.md)
- [PETER_WEYL_TWO_NODE_EUCLIDEAN_PREREGISTRATION.md](PETER_WEYL_TWO_NODE_EUCLIDEAN_PREREGISTRATION.md)
- [scripts/peter_weyl_two_node_euclidean_joint_gate.py](scripts/peter_weyl_two_node_euclidean_joint_gate.py)


## HDA_3NODE

**Статус:** tested_finite  
**Роль:** core

The frozen three-node graph-changing Peter-Weyl by route regression retains j=0 outputs and reproduces route~epsilon, cross~epsilon, pure-geometry~epsilon^2 and joint~epsilon scaling across all node pairs.

**Evidence:**

- [THREE_NODE_GRAPH_HDA_RESULT.md](THREE_NODE_GRAPH_HDA_RESULT.md)
- [scripts/peter_weyl_three_node_graph_hda_gate.py](scripts/peter_weyl_three_node_graph_hda_gate.py)


## LORENTZ

**Статус:** tested_finite  
**Роль:** core

The fixed real-beta Lorentzian coefficient control, spin-parity control and finite Peter-Weyl support bound pass through the declared regulator-safe window.

**Evidence:**

- [LORENTZIAN_BETA_CANCELLATION.md](LORENTZIAN_BETA_CANCELLATION.md)
- [scripts/lorentzian_beta_cancellation_gate.py](scripts/lorentzian_beta_cancellation_gate.py)
- [scripts/lorentzian_hit_depth_bound.py](scripts/lorentzian_hit_depth_bound.py)
- [scripts/peter_weyl_lorentzian_parity_gate.py](scripts/peter_weyl_lorentzian_parity_gate.py)


## LHDA_COMP

**Статус:** proved  
**Роль:** core

Under the explicitly stated fixed-cutoff habitat assumptions, composition gives cross/D=O(epsilon) and geometry-geometry/D=O(epsilon^2), reducing the full defect to the route defect in the regulator limit.

**Evidence:**

- [FIXED_CUTOFF_COMPOSITION_BOUND.md](FIXED_CUTOFF_COMPOSITION_BOUND.md)


## JOINT_FIXED_INPUT

**Статус:** tested_finite  
**Роль:** core

For the frozen all-j=1/2 finite HH family the exact hit-depth theorem makes truncation inactive above Jmax=5/2 in the Euclidean calculation while the measured joint HDA defect decreases as epsilon^1.00644; the declared Lorentzian support wall is Jmax=13/2.

**Evidence:**

- [JOINT_REGULATOR_LIMIT.md](JOINT_REGULATOR_LIMIT.md)
- [scripts/joint_regulator_limit_gate.py](scripts/joint_regulator_limit_gate.py)
- [scripts/lorentzian_hit_depth_bound.py](scripts/lorentzian_hit_depth_bound.py)


## DEWITT

**Статус:** proved  
**Роль:** core

Within the declared local two-derivative canonical ansatz, the DeWitt/HDA signature and degree-counting results identify the GR kinetic structure required by first-class closure.

**Evidence:**

- [DEWITT_HDA_UNIQUENESS.md](DEWITT_HDA_UNIQUENESS.md)
- [FLUX_DEWITT_SIGNATURE_THEOREM.md](FLUX_DEWITT_SIGNATURE_THEOREM.md)
- [BF_GR_DIRAC_COUNT_DISCRIMINATOR.md](BF_GR_DIRAC_COUNT_DISCRIMINATOR.md)


## REGGE_L6_HELDOUT

**Статус:** tested_finite  
**Роль:** core

The preregistered L=3,4,5 Regge TT residue continuation predicted the independently computed L=6 value with about 0.00714 percent relative error without refitting on L=6.

**Evidence:**

- [TT_REGGE_ZT_L6_PREREGISTRATION.md](TT_REGGE_ZT_L6_PREREGISTRATION.md)
- [TT_REGGE_ZT_L6_RESULT.md](TT_REGGE_ZT_L6_RESULT.md)
- [scripts/tt_regge_zt_l6_gate.py](scripts/tt_regge_zt_l6_gate.py)


## TT_PROPAGATOR

**Статус:** tested_finite  
**Роль:** core

The reduced TT positive-control kernel has a massless leading pole, positive residue and the expected inverse-momentum equal-time covariance, with exact bare lattice correction controls in the declared model.

**Evidence:**

- [TT_PROPAGATOR_FIRST_PASS.md](TT_PROPAGATOR_FIRST_PASS.md)
- [scripts/tt_propagator_first_pass.py](scripts/tt_propagator_first_pass.py)


## TT_VACUUM

**Статус:** tested_finite  
**Роль:** core

The finite Gaussian TT vacuum two-point calculation reproduces the declared polarization covariance and equal-time scaling checks.

**Evidence:**

- [TT_VACUUM_TWO_POINT_RESULT.md](TT_VACUUM_TWO_POINT_RESULT.md)
- [scripts/tt_vacuum_two_point_gate.py](scripts/tt_vacuum_two_point_gate.py)


## S4_TT_QUARTIC

**Статус:** proved  
**Роль:** core

The generic directed-momentum parity-even S4 quartic TT quotient has exactly six independent physical structures.

**Evidence:**

- [S4_TT_QUARTIC_COMPLETE_BASIS.md](S4_TT_QUARTIC_COMPLETE_BASIS.md)
- [scripts/s4_tt_quartic_complete_basis_gate.py](scripts/s4_tt_quartic_complete_basis_gate.py)


## SIX_WILSON_EXTRACTOR

**Статус:** proved  
**Роль:** core

The frozen 100/110/111/120 extraction system has full rank six and exact determinant 1/699840000; the first three high-symmetry directions alone have rank five.

**Evidence:**

- [S4_TT_QUARTIC_COMPLETE_BASIS.md](S4_TT_QUARTIC_COMPLETE_BASIS.md)
- [C6_TO_TT_WILSON_COEFFICIENTS.md](C6_TO_TT_WILSON_COEFFICIENTS.md)
- [scripts/c6_tt_wilson_extractor.py](scripts/c6_tt_wilson_extractor.py)


## NEAREST_BLOCK_S3

**Статус:** proved  
**Роль:** core

A reciprocal face-sharing nearest-block transfer reduces to two symmetric 2x2 multiplicity matrices, giving six real amplitudes, and the regular tetrahedral stencil has the declared isotropic second and symmetry-resolved fourth moments.

**Evidence:**

- [NEAREST_BLOCK_S3_TRANSFER_CLOSURE.md](NEAREST_BLOCK_S3_TRANSFER_CLOSURE.md)
- [scripts/nearest_block_s3_transfer_gate.py](scripts/nearest_block_s3_transfer_gate.py)


## ON_SHELL_WILSON

**Статус:** proved  
**Роль:** core

Four-derivative terms proportional to the leading TT equation of motion are field-redefinition redundant on shell, leaving the physical quartic pole quotient six-dimensional.

**Evidence:**

- [ON_SHELL_TT_WILSON_INVARIANCE.md](ON_SHELL_TT_WILSON_INVARIANCE.md)


## FESHBACH

**Статус:** proved  
**Роль:** core

For a specified Hermitian constraint operator and coarse carrier, the projected resolvent and K/A/B block-Krylov/Feshbach identities are exact.

**Evidence:**

- [FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md](FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md)
- [scripts/feshbach_block_krylov_identity_gate.py](scripts/feshbach_block_krylov_identity_gate.py)


## REAL_GW_MAP

**Статус:** proved  
**Роль:** core

A frozen six-Wilson TT pole response maps algebraically to the two polarization eigenvalues, alpha=4 modified-dispersion coefficient, velocity and phase observables.

**Evidence:**

- [TT_TO_REAL_PHYSICS_OBSERVABLES.md](TT_TO_REAL_PHYSICS_OBSERVABLES.md)
- [scripts/s4_tt_six_wilson_predictor.py](scripts/s4_tt_six_wilson_predictor.py)


## SCALE_MAP

**Статус:** conditional  
**Роль:** core

Given one common positive action/length normalization lambda_R_eff, the repository maps dimensionless TT coefficients to one common microscopic length and physical modified-dispersion units without per-observable fitting.

**Evidence:**

- [PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md](PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md)
- [scripts/physical_scale_prediction_bridge.py](scripts/physical_scale_prediction_bridge.py)
- [CONSTANTS_ZERO_FIT_LEDGER.md](CONSTANTS_ZERO_FIT_LEDGER.md)


## CORECERT

**Статус:** conditional  
**Роль:** core

The registered exact, finite-tested and explicitly conditional arrows compose into one internally closed candidate gravity package; conditional labels preserve their stated assumptions and do not imply experimental truth.

**Evidence:**

- [CANONICAL_THEORY_PACKAGE.md](CANONICAL_THEORY_PACKAGE.md)
- [THEORY_STATUS.md](THEORY_STATUS.md)
- [FIXED_CUTOFF_COMPOSITION_BOUND.md](FIXED_CUTOFF_COMPOSITION_BOUND.md)


## MICRO_DYNAMICAL_UNIQUENESS

**Статус:** external_extension  
**Роль:** extension

A stronger theorem could prove unique dynamical attraction from broad generic microscopic ensembles to the same Peter-Weyl geometric phase and blocking measure; this is not a blocker for the declared constructed candidate.

**Evidence:**

- [Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md](Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md)
- [PREDICTIONS_AND_EXPERIMENTAL_TESTS.md](PREDICTIONS_AND_EXPERIMENTAL_TESTS.md)


## HDA_ARBITRARY_GRAPH

**Статус:** external_extension  
**Роль:** extension

A theorem uniform over arbitrary graph families, arbitrary held-out habitats and the full Lorentzian graph-changing domain would strengthen universality beyond the finite declared HDA package.

**Evidence:**

- [GRAPH_CHANGING_HDA_TARGET.md](GRAPH_CHANGING_HDA_TARGET.md)
- [OFF_SHELL_HDA_HABITAT_TARGET.md](OFF_SHELL_HDA_HABITAT_TARGET.md)
- [PREDICTIONS_AND_EXPERIMENTAL_TESTS.md](PREDICTIONS_AND_EXPERIMENTAL_TESTS.md)


## JOINT_UNBOUNDED_REFINEMENT

**Статус:** external_extension  
**Роль:** extension

A uniform theorem over unbounded graph size, collective spin and regulator refinement would strengthen the finite-word support and fixed-input joint-limit result.

**Evidence:**

- [JOINT_REGULATOR_LIMIT.md](JOINT_REGULATOR_LIMIT.md)
- [FIXED_CUTOFF_COMPOSITION_BOUND.md](FIXED_CUTOFF_COMPOSITION_BOUND.md)
- [PREDICTIONS_AND_EXPERIMENTAL_TESTS.md](PREDICTIONS_AND_EXPERIMENTAL_TESTS.md)


## UNIVERSALITY

**Статус:** external_extension  
**Роль:** extension

Testing broad alternative microscopic ensembles, compatible blocking maps and larger graph families can measure the universality class of the closed candidate without redefining its current core.

**Evidence:**

- [PREDICTIONS_AND_EXPERIMENTAL_TESTS.md](PREDICTIONS_AND_EXPERIMENTAL_TESTS.md)


## BLIND_GW_TEST

**Статус:** experimental_test  
**Роль:** experiment

Freeze the theory commit, six-vector, common scale rule and likelihood before opening a held-out gravitational-wave dispersion/birefringence comparison.

**Evidence:**

- [PREDICTIONS_AND_EXPERIMENTAL_TESTS.md](PREDICTIONS_AND_EXPERIMENTAL_TESTS.md)
- [TT_TO_REAL_PHYSICS_OBSERVABLES.md](TT_TO_REAL_PHYSICS_OBSERVABLES.md)


## INDEPENDENT_REPLICATION

**Статус:** experimental_test  
**Роль:** experiment

Independently written implementations should reproduce the key exact and numerical certificates without importing the implementation under test.

**Evidence:**

- [PREDICTIONS_AND_EXPERIMENTAL_TESTS.md](PREDICTIONS_AND_EXPERIMENTAL_TESTS.md)
- [CANONICAL_THEORY_PACKAGE.md](CANONICAL_THEORY_PACKAGE.md)


---

# Часть II. Physicalization gates

Эта часть особенно важна: она показывает разницу между уже работающими reference/positive controls и теми physical objects, которые всё ещё нужно вывести.


## CONSTRAINT_FESHBACH

**Статус:** proved  
**Роль:** reference

For a specified finite Hermitian constraint operator and coarse carrier, the projected resolvent, Feshbach/Schur complement and block-Krylov identities are exact.

**Жёсткая граница применимости:** The constraint spectral parameter z is not physical omega and this gate does not construct a graviton propagator.

**Evidence:**

- [FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md](FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md)
- [scripts/feshbach_block_krylov_identity_gate.py](scripts/feshbach_block_krylov_identity_gate.py)


## MASTER_PROJECTOR_FINITE

**Статус:** proved  
**Роль:** reference

For a finite regulated constraint family C_A and every positive-definite constraint metric G, M_G=C_A^dagger G^AB C_B is positive and ker(M_G)=intersection_A ker(C_A); an isolated zero sector defines an exact finite spectral projector.

**Жёсткая граница применимости:** Exact finite operator theorem only; the candidate-theory refinement/rigging-map limit and physical boundary amplitude remain open.

**Evidence:**

- [MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md](MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md)
- [scripts/master_constraint_physical_projector_gate.py](scripts/master_constraint_physical_projector_gate.py)


## GRAPH_CHANGING_HDA_PREREQUISITE

**Статус:** tested_finite  
**Роль:** reference

The current three-node graph-changing Peter-Weyl HDA control retains graph/spin-changing outputs and exhibits the frozen route/cross/pure-geometry scaling hierarchy on its finite habitat family.

**Жёсткая граница применимости:** Finite HDA consistency prerequisite only; it does not select the physical inner product, rigging map, boundary state or physical time.

**Evidence:**

- [THREE_NODE_GRAPH_HDA_RESULT.md](THREE_NODE_GRAPH_HDA_RESULT.md)
- [scripts/peter_weyl_three_node_graph_hda_gate.py](scripts/peter_weyl_three_node_graph_hda_gate.py)


## RELATIONAL_HISTORY_POSITIVE_CONTROL

**Статус:** tested_finite  
**Роль:** positive_control

A finite C8 Page-Wootters/rigging-map model shows exactly that a combined clock+system projector can be globally invariant while retaining nontrivial clock-conditioned system evolution.

**Жёсткая граница применимости:** Positive control only: the clock factor is declared externally and R=J is not the graph-changing gravitational evolution operator.

**Evidence:**

- [Q2_RELATIONAL_HISTORY_PROJECTOR.md](Q2_RELATIONAL_HISTORY_PROJECTOR.md)
- [scripts/q2_relational_history_projector_gate.py](scripts/q2_relational_history_projector_gate.py)


## RELATIONAL_METRIC_SOURCE_POSITIVE_CONTROL

**Статус:** tested_finite  
**Роль:** positive_control

On the finite relational positive control, gauge-invariant source insertions implement the legal order P_rel -> Z[J] -> W[J] -> connected metric response -> tangent Gamma^(2) pseudoinverse.

**Жёсткая граница применимости:** Positive control only: this Gamma^(2) is not the spacetime 1PI graviton kernel, the C8 label is not physical omega, and no physical TT Wilson coefficient is frozen.

**Evidence:**

- [Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md](Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md)
- [scripts/q2_relational_metric_source_gate.py](scripts/q2_relational_metric_source_gate.py)


## HISTORY_INTERFERENCE_REFERENCE

**Статус:** tested_finite  
**Роль:** reference

The finite history reference reproduces coherent two-path composition, environment-overlap decoherence and zero Sorkin I3 under a quadratic Born rule.

**Жёсткая граница применимости:** Reference identities only; they do not derive the BQG Born rule, photon state or physical Maxwell dynamics.

**Evidence:**

- [UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md](UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md)
- [scripts/binary_history_interference_lensing_gate.py](scripts/binary_history_interference_lensing_gate.py)


## GRAVITATIONAL_WAVE_OPTICS_REFERENCE

**Статус:** tested_finite  
**Роль:** reference

A finite point-lens control uses one Fermat potential for both stationary lensing paths and their relative wave-optics phase, with a split-potential negative control.

**Жёсткая граница применимости:** Standard wave-optics reference only; the physical BQG Weyl potential remains open.

**Evidence:**

- [UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md](UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md)
- [scripts/binary_history_interference_lensing_gate.py](scripts/binary_history_interference_lensing_gate.py)


## BACKGROUND_SCALAR_COSMOLOGY_REFERENCE

**Статус:** tested_finite  
**Роль:** reference

The finite cosmology reference verifies rho-to-w conservation identities and the mu/Sigma/slip lensing-dynamics consistency dictionary with negative controls.

**Жёсткая граница применимости:** Reference bookkeeping only; it does not supply a BQG dark component or observational fit.

**Evidence:**

- [UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md](UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md)
- [scripts/physical_cosmology_background_scalar_gate.py](scripts/physical_cosmology_background_scalar_gate.py)


## PHYSICAL_PROJECTOR_HISTORY

**Статус:** open_physical  
**Роль:** physical

Construct the theory-specific anomaly/refinement-compatible rigging-map or boundary-history amplitude from the actual graph-changing gravitational constraint family, with a derived clock only if the microscopic construction supplies one.

**Жёсткая граница применимости:** The exact finite master-projector theorem and the C8 relational positive control do not close this theory-specific physical gate.

**Evidence:**

- [MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md](MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md)
- [Q2_RELATIONAL_HISTORY_PROJECTOR.md](Q2_RELATIONAL_HISTORY_PROJECTOR.md)
- [CORE_FALSIFICATION_TESTS.md](CORE_FALSIFICATION_TESTS.md)


## CONNECTED_INTERBLOCK_HISTORY

**Статус:** open_physical  
**Роль:** physical

Compute connected multi-block/refinement metric cumulants with the theory-specific physical projector/history amplitude and remove vacuum-disconnected pieces through the generating functional.

**Жёсткая граница применимости:** A local finite shape-source Hessian is not a connected spacetime interblock correlator.

**Evidence:**

- [Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md](Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md)
- [CORE_FALSIFICATION_TESTS.md](CORE_FALSIFICATION_TESTS.md)


## PHYSICAL_TT_KERNEL

**Статус:** open_physical  
**Роль:** physical

Derive the continuum/IR physical metric 1PI Hessian and its TT projection K_TT(omega,k) from the theory-specific physical generating functional, recovering the leading massless Einstein/Fierz-Pauli pole before reading quartic corrections.

**Жёсткая граница применимости:** Constraint-resolvent z, finite C8 character angle and reduced TT positive-control frequency are not promoted to the physical omega of the interacting gravity theory.

**Evidence:**

- [MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md](MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md)
- [Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md](Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md)
- [TT_PROPAGATOR_FIRST_PASS.md](TT_PROPAGATOR_FIRST_PASS.md)


## IR_SIX_VECTOR

**Статус:** open_physical  
**Роль:** physical

Freeze the six microscopic on-shell quartic TT Wilson coefficients from the derived physical TT pole without post-hoc reduction to a lower-dimensional ansatz.

**Жёсткая граница применимости:** The six-dimensional observable dictionary and extractor are closed algebraically, but the interacting physical six-vector itself is not yet derived.

**Evidence:**

- [S4_TT_QUARTIC_COMPLETE_BASIS.md](S4_TT_QUARTIC_COMPLETE_BASIS.md)
- [C6_TO_TT_WILSON_COEFFICIENTS.md](C6_TO_TT_WILSON_COEFFICIENTS.md)
- [scripts/s4_tt_six_wilson_predictor.py](scripts/s4_tt_six_wilson_predictor.py)


## COMMON_SCALE_CALIBRATION

**Статус:** open_physical  
**Роль:** physical

After the dimensionless physical outputs are frozen, derive one common physical scale internally or calibrate exactly one declared datum and hold that scale fixed for all remaining observables.

**Жёсткая граница применимости:** The algebraic unit translator is available, but no common physical calibration is declared complete here and separate sector-by-sector scales are forbidden.

**Evidence:**

- [PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md](PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md)
- [CONSTANTS_ZERO_FIT_LEDGER.md](CONSTANTS_ZERO_FIT_LEDGER.md)
- [CORE_FALSIFICATION_TESTS.md](CORE_FALSIFICATION_TESTS.md)
- [COSMOLOGY_INTERFERENCE_PREREGISTRATION.md](COSMOLOGY_INTERFERENCE_PREREGISTRATION.md)


## DYNAMICAL_MAXWELL_KERNEL

**Статус:** open_physical  
**Роль:** physical

Derive the theory-specific transverse photon 1PI kernel Gamma_AA^(2), Maxwell stiffness Z_A, massless deconfined photon pole and IR causal cone from the same connected physical history generating functional.

**Жёсткая граница применимости:** Compact U(1) phase topology, Chern number and finite interference identities are not a physical Maxwell derivation.

**Evidence:**

- [UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md](UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md)
- [COSMOLOGY_INTERFERENCE_PREREGISTRATION.md](COSMOLOGY_INTERFERENCE_PREREGISTRATION.md)


## PHYSICAL_BACKGROUND_COSMOLOGY

**Статус:** open_physical  
**Роль:** physical

Derive the physical homogeneous Gamma_FLRW and its rho_hist(a), p_hist(a), H(a) and w_hist(a) from the same connected history measure, with w inferred only after rho is derived.

**Жёсткая граница применимости:** The rho-to-w reference map is solved, but no BQG background dark component is currently derived and no evolving-dark-energy ansatz is selected from data.

**Evidence:**

- [UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md](UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md)
- [COSMOLOGY_INTERFERENCE_PREREGISTRATION.md](COSMOLOGY_INTERFERENCE_PREREGISTRATION.md)


## PHYSICAL_SCALAR_COSMOLOGY

**Статус:** open_physical  
**Роль:** physical

Derive the physical scalar metric kernel and stable Phi/Psi, growth, effective sound-speed and anisotropic-stress response from the same theory-specific effective action.

**Жёсткая граница применимости:** No TT coefficient, E/T2 split, constraint eigenvalue or fitted mu/Sigma function is promoted to physical dark matter.

**Evidence:**

- [UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md](UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md)
- [COSMOLOGY_INTERFERENCE_PREREGISTRATION.md](COSMOLOGY_INTERFERENCE_PREREGISTRATION.md)


## LENSING_DYNAMICS_CLOSURE

**Статус:** open_physical  
**Роль:** physical

Show that one derived scalar metric response simultaneously predicts massive-body dynamics, weak/strong/CMB lensing, Fermat/time-delay phase and coherent gravitational wave-optics, with no independent lensing or interference potential.

**Жёсткая граница применимости:** Finite lensing/interference and mu/Sigma controls are prerequisites only; joint observed BQG lensing-dynamics closure remains uncomputed.

**Evidence:**

- [UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md](UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md)
- [COSMOLOGY_INTERFERENCE_PREREGISTRATION.md](COSMOLOGY_INTERFERENCE_PREREGISTRATION.md)
- [scripts/binary_history_interference_lensing_gate.py](scripts/binary_history_interference_lensing_gate.py)
- [scripts/physical_cosmology_background_scalar_gate.py](scripts/physical_cosmology_background_scalar_gate.py)


## BLIND_GW_COMPARISON

**Статус:** experimental_test  
**Роль:** experiment

Only after the physical TT kernel, six-vector and one-scale rule are frozen, preregister and open a held-out gravitational-wave dispersion/birefringence likelihood comparison.

**Жёсткая граница применимости:** No current internal regression constitutes experimental confirmation of the theory.

**Evidence:**

- [PREDICTIONS_AND_EXPERIMENTAL_TESTS.md](PREDICTIONS_AND_EXPERIMENTAL_TESTS.md)
- [TT_TO_REAL_PHYSICS_OBSERVABLES.md](TT_TO_REAL_PHYSICS_OBSERVABLES.md)


## BLIND_COSMOLOGY_LENSING_COMPARISON

**Статус:** experimental_test  
**Роль:** experiment

After background, scalar, photon, lensing-dynamics and one-scale outputs are frozen, compare jointly against preregistered expansion, growth and lensing datasets without retuning.

**Жёсткая граница применимости:** DESI, CMB, lensing and dark-matter observations are external tests, not selectors for the microscopic BQG output.

**Evidence:**

- [COSMOLOGY_INTERFERENCE_PREREGISTRATION.md](COSMOLOGY_INTERFERENCE_PREREGISTRATION.md)
- [UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md](UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md)


---

# Часть III. Как читать этот реестр

Если gate имеет статус **proved**, это не означает больше, чем написано в его claim и hard scope.

Если gate имеет статус **tested_finite**, это finite evidence, а не автоматически continuum theorem.

Если gate имеет статус **conditional**, assumption является частью результата.

Если gate имеет статус **open_physical**, его нельзя заменять ссылкой на structural control.

Если gate имеет статус **experimental_test**, он не считается выполненным до внешнего blind protocol.

Самая важная формула этого тома:

\[
\boxed{
\text{status}
+
\text{scope}
+
\text{evidence}
=
\text{полный смысл результата}.
}
\]

