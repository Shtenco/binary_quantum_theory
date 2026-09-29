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
