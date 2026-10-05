# Бинарная квантовая гравитация (BQG)
## Emergence Program: от бинарной квантовой информации к геометрии

**Канонический README новой исследовательской ветки — 6 октября 2026**

> Главный вопрос этой версии проекта:
>
> **может ли пространство возникать из физической структуры квантовых отношений, а не быть заранее заданным фоном?**

---

# 0. Новый старт

Проект BQG прошёл длинную ветку finite SU(2)-геометрии, graph-changing constraints, master constraints, HDA/GR-контролей, TT/EFT-переводчиков и отдельной 2T/Weyl-гипотезы. Эта работа не удаляется из репозитория и остаётся доказательной базой и историей проекта.

Но канонический фронтир меняется.

Минимальный статический сферически-симметричный shadow-sector не дал собственной ненулевой hair-поправки: в заявленных предпосылках он возвращает Schwarzschild/constant-map и `h_BQG = 0`. Это означает, что следующий разумный шаг — не подгонять новую функцию метрики, а исследовать более глубокий вопрос: **откуда сама геометрия может появиться в бинарной квантовой системе**.

Поэтому новая основная программа:

$$
\boxed{
\text{binary quantum degrees of freedom}
\to
\text{physical constraints}
\to
\text{entanglement / correlations}
\to
\text{relational distance}
\to
\text{emergent geometry}
\to
\text{causality}
\to
\text{effective gravity}
}
$$

Главное правило остаётся прежним:

$$
\boxed{\text{красивая идея никогда не сильнее доказательства}}
$$

Статусы:

- **EXACT** — точный конечномерный результат;
- **FINITE PASS** — воспроизводимая конечная вычислительная проверка;
- **CANDIDATE** — математически определённая, но ещё не физически выведенная конструкция;
- **OPEN** — следующий рубеж;
- **NO-GO** — проверенный отрицательный результат в явно указанной области.

---

# 1. Первый объект новой ветки

Мы начинаем максимально дёшево вычислительно.

Не с гигантского графа.

Не с полного пространства $2^N$.

Не с continuum.

А с минимального четырёхвалентного SU(2)-инвариантного узла из четырёх spin-$1/2$.

Полное пространство:

$$
(\mathbb C^2)^{\otimes 4},
\qquad \dim=16.
$$

После Gauss / total-spin-zero projection:

$$
\boxed{
\mathcal H_{\rm phys}^{(4)}
=\mathrm{Inv}_{SU(2)}\left[(\tfrac12)^{\otimes4}\right],
\qquad
\dim \mathcal H_{\rm phys}^{(4)}=2.
}
$$

То есть вся первая задача живёт не в 16 измерениях, а в **двумерном физическом секторе**.

Это и есть принцип новой программы:

$$
\boxed{\text{symmetry first, numerics last}}
$$

---

# 2. Канонический физический базис

Используем coupling channel $(12)(34)$.

Первое состояние — произведение двух singlet-пар:

$$
|s\rangle
=|s_{12}\rangle|s_{34}\rangle,
$$

где

$$
|s_{ij}\rangle
=\frac{|01\rangle-|10\rangle}{\sqrt2}.
$$

Второе состояние — две triplet-пары, связанные обратно в полный $J=0$:

$$
|t\rangle
=\frac1{\sqrt3}
\left(
|t_+\rangle|t_-\rangle
-|t_0\rangle|t_0\rangle
+|t_-\rangle|t_+\rangle
\right).
$$

Они ортонормированы:

$$
\langle s|s\rangle=1,
\qquad
\langle t|t\rangle=1,
\qquad
\langle s|t\rangle=0.
$$

Любое нормированное физическое состояние можно записать как

$$
\boxed{
|\Psi(\alpha,\phi)\rangle
=\cos\alpha\,|s\rangle
+e^{i\phi}\sin\alpha\,|t\rangle.
}
$$

После gauge reduction первая новая ветка BQG имеет всего два реальных параметра: $\alpha$ и $\phi$.

---

# 3. Первый точный результат: isotropic entanglement state

Рассматриваем состояние

$$
\boxed{
|\Psi_{\rm tet}^{+}\rangle
=\frac{|s\rangle+i|t\rangle}{\sqrt2}
}
$$

и его complex-conjugate orientation partner

$$
\boxed{
|\Psi_{\rm tet}^{-}\rangle
=\frac{|s\rangle-i|t\rangle}{\sqrt2}.
}
$$

Для любой пары $i<j$ определяем

$$
\rho_{ij}
=\mathrm{Tr}_{\overline{ij}}
|\Psi\rangle\langle\Psi|.
$$

Для обоих состояний $|\Psi_{\rm tet}^{\pm}\rangle$ все шесть двухчастичных reduced density matrices имеют один и тот же спектр:

$$
\boxed{
\operatorname{Spec}\rho_{ij}
=\left\{\frac12,\frac16,\frac16,\frac16\right\}
\qquad \forall i<j.
}
$$

Отсюда pair entropy:

$$
S_{ij}
=-\frac12\log_2\frac12
-3\frac16\log_2\frac16
=\frac12+\frac12\log_2 6.
$$

Каждый одиночный spin maximally mixed:

$$
S_i=1.
$$

Поэтому mutual information любой пары одинакова:

$$
\boxed{
I_{ij}
=S_i+S_j-S_{ij}
=\frac32-\frac12\log_2 6
\approx0.20751875\ \text{bit}.
}
$$

**Статус: EXACT для минимального четырёх-spin singlet sector.**

---

# 4. Информационная геометрия

Рабочая гипотеза новой ветки:

> пространственная близость может быть эффективным описанием силы физических квантовых отношений.

Пока это **CANDIDATE**, а не фундаментально выведенная формула.

Можно ввести монотонное отображение

$$
 d_{ij}=f(I_{ij}),
\qquad f'<0.
$$

Например, только как удобную координатизацию:

$$
 d_{ij}
=-\ell_*\ln\left(\frac{I_{ij}}{I_{\max}}\right).
$$

Для isotropic state:

$$
I_{12}=I_{13}=I_{14}=I_{23}=I_{24}=I_{34},
$$

следовательно

$$
\boxed{
 d_{12}=d_{13}=d_{14}=d_{23}=d_{24}=d_{34}.
}
$$

Четыре равноудалённые точки реализуются как regular tetrahedron.

Это даёт минимальную тетраэдрическую relational geometry.

## Важное ограничение

Этот факт **ещё не является доказательством**

$$
q=2\Rightarrow d=3.
$$

Причина: для четырёх равноудалённых точек трёхмерный simplex является стандартной минимальной евклидовой реализацией. Поэтому сам rank-3 embedding здесь частично кинематичен.

Сильный будущий тест должен показать, что трёхмерность сохраняется или возникает **на растущих физических графах**, а не только у одного четырёхточечного simplex.

Это ограничение является частью результата, а не примечанием мелким шрифтом.

---

# 5. Что именно уже интересно

Хотя один tetrahedron ещё не выводит размерность Вселенной, первый результат даёт важную новую структуру:

$$
\boxed{
\text{SU(2) constraint}
+\text{complex physical phase}
\to
\text{pairwise isotropic quantum relations}.
}
$$

Ключевой неожиданный элемент — относительная фаза

$$
\boxed{e^{\pm i\pi/2}=\pm i.}
$$

Она не является косметической: real superpositions и generic phases дают другую pair-correlation structure.

Поэтому следующий вопрос становится точным:

> существует ли SU(2)-инвариантный геометрический оператор, который динамически выделяет именно эти две фазовые ориентации?

---

# 6. Следующий gate: oriented-volume / chirality operator

Определяем минимальный oriented triple product

$$
\boxed{
Q_{123}
=\epsilon_{abc}J_1^aJ_2^bJ_3^c
=\mathbf J_1\cdot(\mathbf J_2\times\mathbf J_3).
}
$$

Следующая проверка должна быть проведена **точно в двумерном физическом базисе** $\{|s\rangle,|t\rangle\}$.

Цель:

$$
Q_{\rm phys}
=P_{J=0}Q_{123}P_{J=0}
\stackrel{?}{\propto}\sigma_y.
$$

Если это выполняется, то

$$
|\Psi_{\rm tet}^{\pm}\rangle
$$

оказываются eigenstates oriented-volume/chirality operator.

Тогда новая цепочка станет:

$$
\boxed{
\text{orientation}
\to
\text{complex phase}
\to
\text{isotropic correlations}
\to
\text{tetrahedral relational geometry}.
}
$$

**Статус на момент этого README: OPEN — следующий точный расчёт.**

---

# 7. После volume gate: только дешёвые аналитические проверки

Мы не увеличиваем систему, пока не закрыты следующие локальные вопросы.

## Gate E1 — exact isotropy locus

Для

$$
|\Psi(\alpha,\phi)\rangle
$$

вывести аналитически spectra / singlet weights всех шести $\rho_{ij}$ и решить условия их равенства.

Цель: понять, являются ли $|\Psi_{\rm tet}^{\pm}\rangle$ уникальной isotropic pair-spectrum парой с точностью до global phase и orientation.

## Gate E2 — stability

Возмутить

$$
\alpha=\frac\pi4+\varepsilon,
\qquad
\phi=\pm\frac\pi2+\delta
$$

и вывести leading anisotropy analytically.

## Gate E3 — energy/geometry response

Выбрать физический локальный source operator $O_E$ и проверить

$$
|\Psi\rangle
\to
O_E|\Psi\rangle
\to
\delta I_{ij}
\to
\delta d_{ij}.
$$

Цель — получить первый finite relational analogue идеи

$$
\boxed{\text{energy changes geometry}.}
$$

## Gate E4 — growth

Только после E1–E3 переходить к нескольким связанным intertwiners и измерять:

- spectral dimension;
- area/volume-law scaling;
- correlation length;
- causal propagation front.

---

# 8. Большая программа

Если минимальные gates проходят, новая BQG-программа раскладывается на четыре линии.

## BQG-I — Emergent Reality

$$
\text{binary states}
\to
\text{physical correlations}
\to
\text{distance}
\to
\text{dimension}
\to
\text{causal cone}.
$$

## BQG-II — Emergent Gravity

Искать количественный мост

$$
\delta\rho
\to
\delta I
\to
\delta g
$$

и затем проверять, появляется ли в coarse-grained limit Einstein-like response.

## BQG-III — Quantum Cosmology

Строить homogeneous/isotropic coarse-grained states и выводить effective dynamics $a(t)$, а не задавать её вручную.

## BQG-IV — Horizons & Information

Проверять area law, horizon entanglement и Page-like information flow в конечном физическом Hilbert space.

---

# 9. Что НЕ заявляется

Этот README намеренно запрещает следующие преждевременные утверждения.

Мы пока **не доказали**, что:

- физическое пространство обязано быть трёхмерным;
- mutual information является фундаментальным расстоянием;
- continuum GR уже выведена из новой entanglement branch;
- $c$, $G$ или $\hbar$ уже получены из бинарной микрофизики;
- проблема измерения решена;
- тёмная материя или тёмная энергия объяснены;
- 2T / extra-dimensional гипотезы выведены из BQG;
- существуют физические wormholes из entanglement graph;
- минимальный tetrahedral state описывает реальный вакуум Вселенной.

Это не недостаток формулировки. Это список будущих falsification gates.

---

# 10. Что остаётся от старой ветки

Репозиторий содержит большое число прежних finite-конструкций и проверок: SU(2)/Peter–Weyl carriers, global gluing, graph-changing HDA attempts, master constraints, Regge/Plebanski/Urbantke bridges, TT/EFT machinery, cosmology candidates, 2T/Weyl analysis и depth-6 proof frontier.

Они **не объявляются автоматически доказательствами новой emergence chain**.

Они являются библиотекой уже построенных операторов, representations, constraints и negative controls, которую новая программа будет использовать только там, где связь будет явно доказана.

Полезные существующие точки входа:

- `MICRO_WALSH_QGEOM_BRIDGE.md`
- `SPATIAL_QUBIT_GEOMETRY_BRIDGE.md`
- `LOGICAL_SHAPE_METRIC_JACOBIAN.md`
- `MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md`
- `Q2_RELATIONAL_HISTORY_PROJECTOR.md`
- `Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md`
- `THEORY_STATUS.md`
- `OPEN_PROBLEMS.md`

---

# 11. Вычислительная философия новой ветки

Никакого brute force без необходимости.

Каждый новый уровень проходит лестницу:

$$
\boxed{
\text{constraints}
\to
\text{symmetry reduction}
\to
\text{irreducible sectors}
\to
\text{analytic invariants}
\to
\text{sparse numerics only if unavoidable}.
}
$$

Мы предпочитаем точную матрицу $2\times2$ огромному численному скану, если они отвечают на один и тот же физический вопрос.

Мы предпочитаем no-go красивой, но не проверяемой гипотезе.

Мы предпочитаем один вычислимый observable десяти философским заявлениям.

---

# 12. Текущий фронтир

На 6 октября 2026 года каноническая точка продолжения:

$$
\boxed{
Q_{123}
=\epsilon_{abc}J_1^aJ_2^bJ_3^c
\quad\text{в}\quad
\mathcal H_{\rm phys}^{(4)}.
}
$$

Нужно ответить на четыре вопроса:

1. Какова точная матрица $Q_{123}$ в базисе $\{|s\rangle,|t\rangle\}$?
2. Являются ли $|\Psi_{\rm tet}^{\pm}\rangle$ её eigenstates?
3. Совпадает ли pair-spectrum isotropy locus с oriented-volume eigenstates?
4. Насколько быстро возникает анизотропия при отклонении от этих состояний?

Если ответы окажутся положительными, первый локальный блок новой ветки будет закрыт точной цепочкой:

$$
\boxed{
\text{Gauss-invariant binary quantum node}
\to
\text{oriented volume}
\to
\pm i\text{ phase}
\to
\text{isotropic pair spectra}
\to
\text{tetrahedral relational geometry}.
}
$$

После этого можно переходить от одного tetrahedron к **росту сети и настоящему тесту emergent dimension**.

---

## Репозиторий

`Shtenco/binary_quantum_theory`

## Канонический принцип

> **Сначала уменьшить задачу симметрией. Затем решить её точно. И только потом тратить вычисления.**
