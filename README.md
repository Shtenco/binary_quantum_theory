# Бинарная квантовая гравитация (BQG)
## Emergence Program: от бинарной квантовой информации к геометрии

**Канонический README — 6 октября 2026**

---

# 1. Новый основной вопрос

Главный фронтир BQG теперь формулируется не как поиск произвольной поправки к готовой метрике, а глубже:

> **может ли пространство, геометрия и затем гравитация возникать из физической структуры бинарной квантовой информации?**

Новая цепочка проекта:

$$
\boxed{
\text{binary quantum degrees of freedom}
\to
\text{constraints}
\to
\text{noncommuting relational observables}
\to
\text{quantum volume}
\to
\text{entanglement / pair spectra}
\to
\text{relational geometry}
\to
\text{large-scale dimension}
\to
\text{causality}
\to
\text{effective gravity}
}
$$

Старая работа репозитория не удалена: SU(2)/Peter–Weyl carriers, graph-changing constraints, master constraints, HDA/GR controls, Regge/Plebanski/Urbantke bridges, TT/EFT machinery, cosmology, 2T/Weyl и depth-6 proof frontier остаются доказательной библиотекой. Но они больше не задают канонический порядок рассказа.

Главное правило:

$$
\boxed{\text{симметрия сначала, вычисления потом}}
$$

и

$$
\boxed{\text{красивая идея никогда не сильнее доказательства}.}
$$

---

# 2. Почему мы сменили фронтир

Минимальный static spherical shadow-sector не дал собственной ненулевой BQG hair-поправки: в заявленных предпосылках система возвращает тривиальный hair / Schwarzschild-like результат.

Это полезный no-go.

Он говорит, что новый физический эффект не нужно выжимать из слишком узкого ansatz. Вместо этого мы возвращаемся к более фундаментальному уровню и спрашиваем, откуда вообще появляется геометрия.

---

# 3. Минимальный физический объект новой ветки

Берём четыре spin-$1/2$:

$$
\mathcal H=(\mathbb C^2)^{\otimes4},
\qquad \dim\mathcal H=16.
$$

Но сразу применяем SU(2) Gauss / total-spin-zero reduction:

$$
\boxed{
\mathcal H_{\rm phys}^{(4)}
=\mathrm{Inv}_{SU(2)}[(\tfrac12)^{\otimes4}],
\qquad
\dim\mathcal H_{\rm phys}^{(4)}=2.
}
$$

То есть первая фундаментальная задача живёт в матрицах $2\times2$, а не в большом brute-force пространстве.

Используем ортонормированный recoupling basis

$$
|s\rangle=|s_{12}\rangle|s_{34}\rangle,
$$

$$
|t\rangle=((t_{12}t_{34})_{J=0}).
$$

Любое чистое физическое состояние:

$$
\boxed{
|\Psi(\alpha,\phi)\rangle
=\cos\alpha|s\rangle+e^{i\phi}\sin\alpha|t\rangle.
}
$$

---

# 4. Первый новый точный theorem: объём — это некоммутативность парной геометрии

Определим oriented triple product

$$
Q_{123}=\epsilon_{abc}J_1^aJ_2^bJ_3^c.
$$

Точный операторный расчёт даёт:

$$
\boxed{
Q_{123}
=i\left[
\mathbf J_1\!\cdot\!\mathbf J_2,
\mathbf J_2\!\cdot\!\mathbf J_3
\right].
}
$$

То есть oriented quantum volume появляется из **некоммутативности двух конкурирующих pair-geometry observables**.

Это важнее, чем просто формула для объёма: объём здесь является мерой невозможности одновременно сделать две соседние парные геометрии классически совместимыми.

В physical basis:

$$
\boxed{
Q_{123}^{\rm phys}
=\frac{\sqrt3}{4}\sigma_y
=\frac{\sqrt3}{4}
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix}.
}
$$

Следовательно,

$$
\boxed{
|\Psi_+\rangle
=\frac{|s\rangle+i|t\rangle}{\sqrt2},
\qquad
Q_{123}|\Psi_+\rangle
=+\frac{\sqrt3}{4}|\Psi_+\rangle,
}
$$

$$
\boxed{
|\Psi_-\rangle
=\frac{|s\rangle-i|t\rangle}{\sqrt2},
\qquad
Q_{123}|\Psi_-\rangle
=-\frac{\sqrt3}{4}|\Psi_-\rangle.
}
$$

**Статус: EXACT.**

---

# 5. Вторая точная часть: pair-spectrum isotropy

Любая двухчастичная редукция global SU(2) singlet является SU(2)-инвариантной и определяется singlet weight $p_{ij}$:

$$
\operatorname{Spec}\rho_{ij}
=\left\{
 p_{ij},
 \frac{1-p_{ij}}3,
 \frac{1-p_{ij}}3,
 \frac{1-p_{ij}}3
\right\}.
$$

Для общего $|\Psi(\alpha,\phi)\rangle$:

$$
\boxed{p_{12}=p_{34}=\cos^2\alpha,}
$$

$$
\boxed{
p_{13}=p_{24}
=\frac12-\frac14\cos2\alpha
+\frac{\sqrt3}{4}\sin2\alpha\cos\phi,
}
$$

$$
\boxed{
p_{14}=p_{23}
=\frac12-\frac14\cos2\alpha
-\frac{\sqrt3}{4}\sin2\alpha\cos\phi.
}
$$

Условие одинакового спектра всех шести пар имеет в каноническом диапазоне точные решения

$$
\boxed{
\alpha=\frac\pi4,
\qquad
\phi=\frac\pi2\ \text{или}\ \frac{3\pi}{2}.
}
$$

То есть **единственные pair-spectrum isotropic pure states** — ровно два orientation eigenstates $Q_{123}$.

Следовательно:

$$
\boxed{
\text{pair-spectrum isotropy}
\Longleftrightarrow
\text{sharp oriented-volume state}
}
$$

с точностью до global phase и orientation sign.

**Статус: EXACT.**

---

# 6. Общий спектр и mutual information

В isotropic states:

$$
p_{ij}=\frac12\qquad\forall i<j,
$$

поэтому

$$
\boxed{
\operatorname{Spec}\rho_{ij}
=\left\{\frac12,\frac16,\frac16,\frac16\right\}.
}
$$

Каждый одиночный spin maximally mixed:

$$
S_i=1.
$$

Pair entropy:

$$
S_{ij}=\frac12+\frac12\log_2 6.
$$

И все шесть mutual informations равны:

$$
\boxed{
I_{ij}
=\frac32-\frac12\log_2 6
\approx0.20751875\ \mathrm{bit}.
}
$$

Если использовать одинаковую монотонную map $d_{ij}=f(I_{ij})$, эти четыре leg-labels образуют равноудалённую relational configuration — regular tetrahedral distance pattern.

Важно: **это ещё не доказательство трёхмерности continuum space**. Четырёхточечный simplex сам по себе кинематически допускает минимальное 3D Euclidean embedding. Настоящий dimension test начнётся только на растущей сети.

---

# 7. Главный новый точный результат: anisotropy = volume uncertainty

Определим pair-spectrum anisotropy

$$
\mathcal A_p
=\sum_{i<j}\left(p_{ij}-\frac12\right)^2.
$$

Для произвольного чистого физического состояния получаем точно

$$
\boxed{
\mathcal A_p
=\frac34\left[
\cos^2(2\alpha)
+\sin^2(2\alpha)\cos^2\phi
\right].
}
$$

При этом

$$
\langle Q_{123}\rangle
=\frac{\sqrt3}{4}\sin(2\alpha)\sin\phi,
$$

а

$$
(Q_{123}^{\rm phys})^2=\frac{3}{16}\mathbf1.
$$

Поэтому

$$
(\Delta Q_{123})^2
=\frac{3}{16}-\langle Q_{123}\rangle^2.
$$

И возникает точное тождество

$$
\boxed{
\mathcal A_p=4(\Delta Q_{123})^2.
}
$$

Это центральный результат первого шага новой ветки.

Он означает:

$$
\boxed{
\mathcal A_p=0
\Longleftrightarrow
\Delta Q_{123}=0.
}
$$

То есть **pairwise quantum-geometric isotropy в минимальном physical sector эквивалентна нулевой квантовой неопределённости oriented volume**.

Не приблизительно.

Не после fit.

Не только около vacuum point.

А точно для всего двумерного pure-state physical sector.

**Статус: EXACT.**

---

# 8. Устойчивость

Возмутим один isotropic state:

$$
\alpha=\frac\pi4+\varepsilon,
\qquad
\phi=\frac\pi2+\delta.
$$

Тогда

$$
p_{12}-\frac12=-\varepsilon+O(2),
$$

$$
p_{13}-\frac12
=\frac\varepsilon2-\frac{\sqrt3}{4}\delta+O(2),
$$

$$
p_{14}-\frac12
=\frac\varepsilon2+\frac{\sqrt3}{4}\delta+O(2).
$$

И

$$
\boxed{
\mathcal A_p
=3\varepsilon^2+\frac34\delta^2+O(3).
}
$$

Значит isotropic orientation states — изолированные quadratic minima в обеих независимых физических координатах.

Для mutual-information anisotropy:

$$
\boxed{
\mathcal A_I
=(\log_2 3)^2
\left(3\varepsilon^2+\frac34\delta^2\right)+O(3).
}
$$

---

# 9. Что этот первый блок доказывает

В минимальном четырёх-spin SU(2)-singlet sector доказано:

1. oriented volume является commutator двух pair-geometry operators;
2. physical volume matrix пропорциональна $\sigma_y$;
3. complex phases $\pm i$ выбираются exact volume eigenstates;
4. те же и только те же states имеют isotropic spectra всех пар;
5. все pair mutual informations в них одинаковы;
6. pair-spectrum anisotropy точно равна четырём volume variances;
7. isotropy locally stable как isolated quadratic minimum.

Коротко:

$$
\boxed{
\text{noncommuting pair geometry}
\to
\text{oriented volume}
\to
\pm i\text{ phase}
\Longleftrightarrow
\text{sharp volume}
\Longleftrightarrow
\text{pair-spectrum isotropy}.
}
$$

---

# 10. Что НЕ доказано

Мы пока не утверждаем, что:

- continuum space обязательно трёхмерно;
- mutual information является уникальным физическим расстоянием;
- universe vacuum обязан быть локальным $|\Psi_+\rangle$ или $|\Psi_-\rangle$;
- large-scale Lorentzian causality уже выведена;
- Einstein equations уже следуют из этого theorem;
- $G$, $c$ и $\hbar$ уже получены из бинарной микрофизики.

Первый блок локальный. Следующий тест обязан быть сетевым.

---

# 11. Новый настоящий фронтир: рост без экспоненты

Мы **не** переходим к full $(\mathbb C^2)^{\otimes N}$.

Вместо этого следующий объект строится из уже редуцированных двухмерных intertwiner sectors.

Для $M$ четырёхвалентных узлов наивное локально-физическое пространство имеет размер

$$
2^M,
$$

но и его нужно дополнительно уменьшать:

- gluing constraints;
- graph automorphisms;
- orientation sectors;
- conserved total channels;
- orbit representatives;
- sparse transfer operators.

Следующая цель:

$$
\boxed{
\text{coupled physical intertwiners}
\to
\text{correlation graph}
\to
\text{spectral dimension }d_s
}
$$

без заранее заданного $d=3$.

Это будет первый настоящий test emergent dimension.

---

# 12. Ближайшие gates

## E2 — Two-node exact gluing

Два physical tetrahedral nodes, связанный face/channel, exact symmetry reduction.

Проверить:

- какие orientation combinations допустимы;
- сохраняется ли sharp-volume/isotropy relation;
- появляется ли nontrivial inter-node mutual information;
- можно ли определить relational edge без ad hoc distance map.

## E3 — Minimal network dimension

Построить smallest nontrivial connected network после symmetry reduction и вычислить:

$$
d_s(\tau)=-2\frac{d\ln P(\tau)}{d\ln\tau}.
$$

Именно здесь можно впервые честно спрашивать, возникает ли $d_s\approx3$.

## E4 — Causal propagation

Запустить локальное physical perturbation и измерять commutator growth / information front.

Цель:

$$
\text{finite propagation cone}
\to
\text{emergent causal speed}.
$$

## E5 — Geometry response

Проверить

$$
\delta\text{source}
\to
\delta I
\to
\delta\text{relational geometry}.
$$

Это будет первый шаг к emergent gravity.

---

# 13. Доказательные файлы новой ветки

Главные новые файлы:

- [`BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md`](BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md)
- [`scripts/bqg_minimal_entanglement_volume_gate.py`](scripts/bqg_minimal_entanglement_volume_gate.py)

Запуск:

```bash
python scripts/bqg_minimal_entanglement_volume_gate.py
```

Ожидаемый финал:

```text
PASS
```

Полезные прежние строительные блоки:

- `MICRO_WALSH_QGEOM_BRIDGE.md`
- `SPATIAL_QUBIT_GEOMETRY_BRIDGE.md`
- `LOGICAL_SHAPE_METRIC_JACOBIAN.md`
- `MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md`
- `Q2_RELATIONAL_HISTORY_PROJECTOR.md`
- `Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md`
- `THEORY_STATUS.md`
- `OPEN_PROBLEMS.md`

---

# 14. Канонический принцип проекта

> **Сначала уменьшить задачу симметрией. Затем решить её точно. И только потом тратить вычисления.**

Текущая точка продолжения:

$$
\boxed{
\textbf{Two-node exact physical gluing and first genuine network-level emergence test.}
}
$$
