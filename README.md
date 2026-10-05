# Бинарная квантовая гравитация (BQG)
## Emergence Program: от бинарной квантовой информации к геометрии

**Канонический README — 6 октября 2026**

---

# 1. Главный вопрос новой ветки

BQG теперь ставит более фундаментальный вопрос, чем поиск поправки к заранее заданной метрике:

> **может ли геометрия, расстояние и затем гравитация возникать из физической структуры бинарной квантовой информации?**

Рабочая цепочка:

$$
\boxed{
\text{binary quantum degrees of freedom}
\to
\text{SU(2) constraints}
\to
\text{noncommuting relational observables}
\to
\text{oriented quantum volume}
\to
\text{entanglement / pair spectra}
\to
\text{inter-node correlations}
\to
\text{relational distance ordering}
\to
\text{large-scale dimension}
\to
\text{effective gravity}
}
$$

Главный методологический принцип:

$$
\boxed{\text{симметрия сначала, вычисления потом}.}
$$

Мы предпочитаем точную матрицу $2\times2$, $4\times4$ или $8\times8$ огромному brute-force пространству, если они отвечают на тот же физический вопрос.

---

# 2. Почему был сменён фронтир

Предыдущая static spherical shadow-ветка дала полезный no-go: в минимальном секторе собственная ненулевая BQG hair-поправка не возникла.

Это не провал, а указание, что новый эффект не надо выжимать из слишком узкого ansatz.

Поэтому канонический фронтир смещён глубже: к вопросу о происхождении самой геометрии.

Старые SU(2), Peter-Weyl, HDA, Regge, Plebanski/Urbantke, TT/EFT, cosmology и 2T/Weyl файлы остаются библиотекой доказательных инструментов, но больше не задают порядок основной истории.

---

# 3. Один физический узел: точный локальный theorem

Берём четыре spin-$1/2$:

$$
\mathcal H=(\mathbb C^2)^{\otimes4}.
$$

После SU(2) Gauss / total-spin-zero reduction:

$$
\boxed{
\mathcal H_{\rm phys}^{(4)}
=\mathrm{Inv}_{SU(2)}[(\tfrac12)^{\otimes4}],
\qquad \dim=2.
}
$$

Используем recoupling basis

$$
|s\rangle,\qquad |t\rangle.
$$

Любое чистое physical state:

$$
|\Psi(\alpha,\phi)\rangle
=\cos\alpha|s\rangle+e^{i\phi}\sin\alpha|t\rangle.
$$

Определим oriented volume / scalar chirality

$$
Q_{123}=\epsilon_{abc}J_1^aJ_2^bJ_3^c.
$$

Точно:

$$
\boxed{
Q_{123}
=i[\mathbf J_1\!\cdot\!\mathbf J_2,\mathbf J_2\!\cdot\!\mathbf J_3].
}
$$

То есть oriented volume рождается из некоммутативности двух конкурирующих pair-geometry observables.

В physical basis:

$$
\boxed{
Q_{123}^{\rm phys}=\frac{\sqrt3}{4}\sigma_y.
}
$$

Eigenstates:

$$
\boxed{
|\Psi_\pm\rangle
=\frac{|s\rangle\pm i|t\rangle}{\sqrt2},
\qquad
q_\pm=\pm\frac{\sqrt3}{4}.
}
$$

Для общего physical state pair-singlet weights равны

$$
p_{12}=p_{34}=\cos^2\alpha,
$$

$$
p_{13}=p_{24}
=\frac12-\frac14\cos2\alpha
+\frac{\sqrt3}{4}\sin2\alpha\cos\phi,
$$

$$
p_{14}=p_{23}
=\frac12-\frac14\cos2\alpha
-\frac{\sqrt3}{4}\sin2\alpha\cos\phi.
$$

Полная pair-spectrum isotropy возникает только при

$$
\boxed{
\alpha=\frac\pi4,
\qquad
\phi=\frac\pi2\ \text{или}\ \frac{3\pi}{2}.
}
$$

То есть ровно в двух volume eigenstates.

Определим

$$
\mathcal A_p
=\sum_{i<j}\left(p_{ij}-\frac12\right)^2.
$$

Тогда для любого чистого physical state выполняется точное тождество

$$
\boxed{
\mathcal A_p=4(\Delta Q_{123})^2.
}
$$

Следовательно

$$
\boxed{
\text{pair-spectrum isotropy}
\Longleftrightarrow
\text{sharp oriented quantum volume}.
}
$$

**Статус: EXACT.**

Подробности:

- `BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md`
- `scripts/bqg_minimal_entanglement_volume_gate.py`

---

# 4. Два физических узла: первая настоящая склейка

Каждый локальный physical node имеет dimension $2$, поэтому для двух узлов

$$
\boxed{\dim\mathcal H_{AB}^{\rm red}=4.}
$$

Три локальных pair-shape projectors:

$$
P_{12}=\frac12(I+Z),
$$

$$
P_{13}=\frac12I+\frac{\sqrt3}{4}X-\frac14Z,
$$

$$
P_{14}=\frac12I-\frac{\sqrt3}{4}X-\frac14Z.
$$

Они образуют trine в logical $X$-$Z$ plane.

Вводим минимальный reduced shape-matching Hamiltonian

$$
\boxed{
H_{\rm glue}
=\sum_{a\in\{12,13,14\}}
(P_a^{(A)}-P_a^{(B)})^2.
}
$$

Он точно упрощается до

$$
\boxed{
H_{\rm glue}
=\frac32I-\frac34(X_AX_B+Z_AZ_B).
}
$$

Спектр:

$$
\boxed{
\{0,\tfrac32,\tfrac32,3\}.
}
$$

Unique zero-mismatch state:

$$
\boxed{
|\Phi^+\rangle
=\frac{|ss\rangle+|tt\rangle}{\sqrt2}.
}
$$

То есть exact matching трёх shape channels выбирает не product state, а maximally entangled intertwiner state.

Каждый узел отдельно имеет

$$
\boxed{S(A)=S(B)=1\ \text{bit}.}
$$

При этом локальная ориентация теряет sharpness:

$$
\langle Q_A\rangle=\langle Q_B\rangle=0,
$$

$$
(\Delta Q_A)^2=(\Delta Q_B)^2=\frac3{16}.
$$

Но relative orientation становится sharp:

$$
\boxed{
Q_AQ_B|\Phi^+\rangle
=-\frac3{16}|\Phi^+\rangle.
}
$$

То есть геометрическая информация перемещается из локальных expectation values в inter-node correlations.

Ключевая network-level цепочка:

$$
\boxed{
\text{shape matching}
\to
\text{maximal node entanglement}
\to
\text{sharp relative orientation}.
}
$$

**Статус спектрального результата: EXACT для явно заданного reduced Hamiltonian.**  
**Статус самого $H_{\rm glue}$ как фундаментального BQG dynamics: CANDIDATE.**

Подробности:

- `BQG_TWO_NODE_REDUCED_GLUING_RESULT.md`
- `scripts/bqg_two_node_reduced_gluing_gate.py`

---

# 5. Три узла: первый correlation-distance hierarchy

Для open chain $A-B-C$:

$$
\boxed{\dim\mathcal H_{ABC}^{\rm red}=8.}
$$

Берём

$$
H_3=H_{AB}+H_{BC},
$$

где каждый link имеет ту же reduced gluing form.

Точный spectrum:

$$
\boxed{
3-\frac{3\sqrt2}{2}\quad(\deg=2),
}
$$

$$
\boxed{
3\quad(\deg=4),
}
$$

$$
\boxed{
3+\frac{3\sqrt2}{2}\quad(\deg=2).
}
$$

Чтобы не вводить произвольный выбор внутри двухмерного ground space, используем symmetry-neutral density matrix

$$
\boxed{
\rho_0=\frac{P_0}{2}.
}
$$

Каждый single node maximally mixed:

$$
\rho_A=\rho_B=\rho_C=\frac12I.
$$

Для nearest neighbors:

$$
\boxed{
\operatorname{Spec}\rho_{AB}
=\operatorname{Spec}\rho_{BC}
=
\left\{
\frac{3-2\sqrt2}{8},\frac18,\frac18,\frac{3+2\sqrt2}{8}
\right\}.
}
$$

И

$$
\boxed{
I(A:B)=I(B:C)\approx0.7982479266\ \text{bit}.
}
$$

Для next-nearest pair:

$$
\boxed{
\operatorname{Spec}\rho_{AC}
=\left\{0,\frac14,\frac14,\frac12\right\},
}
$$

поэтому

$$
\boxed{I(A:C)=0.5\ \text{bit}.}
$$

Получаем первый настоящий hierarchy:

$$
\boxed{
I(A:B)=I(B:C)>I(A:C).
}
$$

Следовательно для любой strictly decreasing distance map $d=f(I)$:

$$
\boxed{
d(A:B)=d(B:C)<d(A:C).
}
$$

То есть correlation geometry уже отличает graph distance $1$ от graph distance $2$.

Oriented-volume correlations дают независимый контроль:

$$
\boxed{
\langle Q_AQ_B\rangle
=\langle Q_BQ_C\rangle
=-\frac3{32},
}
$$

$$
\boxed{
\langle Q_AQ_C\rangle=0.
}
$$

Это первый minimal network result, где топологическое соседство отражается сразу в двух разных физических корреляционных observables.

**Статус: EXACT для явно заданной nearest-neighbor reduced model.**

Подробности:

- `BQG_THREE_NODE_REDUCED_CHAIN_RESULT.md`
- `scripts/bqg_three_node_reduced_chain_gate.py`

---

# 6. Что уже получилось в новой ветке

На данный момент замкнута последовательность:

$$
\boxed{
\text{SU(2)-invariant local qubit}
\to
\text{noncommuting pair geometry}
\to
\text{oriented volume}
\to
\text{local isotropy}
\to
\text{two-node entangled shape matching}
\to
\text{three-node correlation-distance hierarchy}.
}
$$

Самые сильные exact statements:

1. $Q=i[D_{12},D_{23}]$;
2. $Q_{\rm phys}=(\sqrt3/4)\sigma_y$;
3. local isotropy iff local volume is sharp;
4. $\mathcal A_p=4(\Delta Q)^2$;
5. exact two-node shape matching selects a Bell-type intertwiner state;
6. local orientation uncertainty can coexist with sharp relative orientation;
7. a three-node ground sector distinguishes nearest from next-nearest nodes through mutual information and volume correlations.

---

# 7. Что пока НЕ доказано

Мы пока не утверждаем, что:

- continuum physical space обязательно трёхмерно;
- $H_{\rm glue}$ уже выведен из fundamental graph-changing BQG Hamiltonian;
- mutual information является уникальным физическим расстоянием;
- large-scale metric obeys Einstein equations;
- correlation distance additive;
- Lorentzian causal cone уже возник;
- $G$, $c$ или $\hbar$ выведены из бинарной микрофизики.

Это следующие falsification gates.

---

# 8. Следующий расчёт: не brute force, а идентификация many-node модели

Для графа из reduced physical nodes текущий candidate Hamiltonian имеет вид

$$
\boxed{
H_G
=\sum_{\langle ij\rangle}
\left[
\frac32I-\frac34(X_iX_j+Z_iZ_j)
\right].
}
$$

Перед увеличением $M$ нужно выяснить, к какому exactly/analytically solvable spin-chain class он относится.

Следующий приоритет:

1. убрать константу и распознать $XX+ZZ$ chain через локальные rotations;
2. проверить эквивалентность стандартной $XX$ / free-fermion модели;
3. вывести gap и correlation length аналитически;
4. получить $I(r)$ без diagonalization $2^M$;
5. затем сравнить 1D chain, ring и branching graphs;
6. только после этого строить настоящий emergent-dimension estimator.

То есть новый центральный рубеж:

$$
\boxed{
\textbf{derive many-node correlation scaling analytically before scaling numerics.}
}
$$

---

# 9. Канонический принцип проекта

> **Сначала уменьшить задачу симметрией. Затем распознать точную математическую структуру. Потом решить её аналитически. И только если это невозможно — считать численно.**

Репозиторий: `Shtenco/binary_quantum_theory`
