# Бинарная квантовая гравитация (BQG)
## Emergence Program: от бинарной квантовой информации к геометрии

**Канонический README — 6 октября 2026**

---

# 1. Новый основной вопрос

Главный фронтир BQG теперь формулируется так:

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
\text{oriented volume}
\to
\text{entanglement}
\to
\text{network correlations}
\to
\text{relational distance}
\to
\text{dimension}
\to
\text{effective gravity}
}
$$

Методологический принцип проекта:

$$
\boxed{\text{симметрия сначала, вычисления потом}.}
$$

Мы сначала редуцируем Hilbert space, затем ищем exact algebraic structure и только после этого считаем численно.

---

# 2. Почему мы сменили фронтир

Минимальная static spherical shadow-ветка дала полезный no-go: в заявленном секторе собственная ненулевая BQG hair-поправка не возникла.

Поэтому следующий физический шаг — не придумывать новую функцию метрики, а исследовать происхождение самой геометрии.

Старые SU(2)/Peter-Weyl, graph-changing constraints, HDA, Regge, Plebanski/Urbantke, TT/EFT, cosmology и 2T/Weyl файлы остаются доказательной библиотекой, но больше не задают канонический порядок основной ветки.

---

# 3. Один physical node: exact local theorem

Берём четыре spin-$1/2$.

После SU(2) Gauss / total-spin-zero reduction:

$$
\boxed{
\mathcal H_{\rm phys}^{(4)}
=\mathrm{Inv}_{SU(2)}[(\tfrac12)^{\otimes4}],
\qquad \dim=2.
}
$$

Используем basis

$$
|s\rangle,\qquad |t\rangle.
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

То есть oriented volume возникает из некоммутативности двух pair-geometry observables.

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

Для общего physical state

$$
|\Psi(\alpha,\phi)\rangle
=\cos\alpha|s\rangle+e^{i\phi}\sin\alpha|t\rangle
$$

полная pair-spectrum isotropy возникает только при

$$
\boxed{
\alpha=\frac\pi4,
\qquad
\phi=\frac\pi2\ \text{или}\ \frac{3\pi}{2}.
}
$$

То есть isotropic states — ровно два volume eigenstates.

Если

$$
\mathcal A_p
=\sum_{i<j}\left(p_{ij}-\frac12\right)^2,
$$

то для любого чистого physical state выполняется

$$
\boxed{
\mathcal A_p=4(\Delta Q_{123})^2.
}
$$

Следовательно:

$$
\boxed{
\text{pair-spectrum isotropy}
\Longleftrightarrow
\text{sharp oriented quantum volume}.
}
$$

**Статус: EXACT.**

Файлы:

- `BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md`
- `scripts/bqg_minimal_entanglement_volume_gate.py`

---

# 4. Два physical nodes: exact reduced gluing

Для двух локально редуцированных узлов

$$
\dim\mathcal H_{AB}^{\rm red}=4.
$$

Три local shape projectors:

$$
P_{12}=\frac12(I+Z),
$$

$$
P_{13}=\frac12I+\frac{\sqrt3}{4}X-\frac14Z,
$$

$$
P_{14}=\frac12I-\frac{\sqrt3}{4}X-\frac14Z.
$$

Вводим reduced shape-matching penalty

$$
\boxed{
H_{\rm glue}
=\sum_a(P_a^{(A)}-P_a^{(B)})^2.
}
$$

Он точно упрощается:

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

То есть exact shape matching выбирает maximally entangled intertwiner state.

Локально:

$$
\langle Q_A\rangle=\langle Q_B\rangle=0,
$$

но relationally:

$$
\boxed{
Q_AQ_B|\Phi^+\rangle
=-\frac3{16}|\Phi^+\rangle.
}
$$

Таким образом геометрическая информация переходит из локальной ориентации в relative orientation correlation.

**Статус spectrum/result: EXACT для явно заданного reduced Hamiltonian.**  
**Статус $H_{\rm glue}$ как фундаментального BQG dynamics: CANDIDATE.**

Файлы:

- `BQG_TWO_NODE_REDUCED_GLUING_RESULT.md`
- `scripts/bqg_two_node_reduced_gluing_gate.py`

---

# 5. Три узла: первый network-distance hierarchy

Для open chain $A-B-C$:

$$
\dim\mathcal H_{ABC}^{\rm red}=8.
$$

Берём

$$
H_3=H_{AB}+H_{BC}.
$$

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

Используем symmetry-neutral ground density matrix

$$
\rho_0=\frac{P_0}{2}.
$$

Nearest-neighbor pair spectra:

$$
\boxed{
\operatorname{Spec}\rho_{AB}
=\operatorname{Spec}\rho_{BC}
=\left\{
\frac{3-2\sqrt2}{8},\frac18,\frac18,\frac{3+2\sqrt2}{8}
\right\}.
}
$$

Отсюда

$$
\boxed{
I(A:B)=I(B:C)\approx0.7982479266\ \text{bit}.
}
$$

Для end-to-end pair:

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

Значит

$$
\boxed{
I(A:B)=I(B:C)>I(A:C).
}
$$

Для любой strictly decreasing map $d=f(I)$:

$$
\boxed{
d(A:B)=d(B:C)<d(A:C).}
$$

Volume correlations дают независимый discriminator:

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

То есть topology уже отражается в двух разных quantum-geometric correlation observables.

**Статус: EXACT для reduced nearest-neighbor model.**

Файлы:

- `BQG_THREE_NODE_REDUCED_CHAIN_RESULT.md`
- `scripts/bqg_three_node_reduced_chain_gate.py`

---

# 6. Главный новый результат: вся many-node chain решается аналитически

Текущий reduced $M$-node Hamiltonian:

$$
\boxed{
H_M
=\sum_{i=1}^{M-1}
\left[
\frac32I
-\frac34(X_iX_{i+1}+Z_iZ_{i+1})
\right].
}
$$

Глобальная локальная rotation на $\pi/2$ вокруг logical $X$ переводит

$$
Z\to\pm Y.
$$

Поэтому

$$
\boxed{
H_M\simeq
\frac32(M-1)I
-\frac34\sum_{i=1}^{M-1}(X_iX_{i+1}+Y_iY_{i+1}).
}
$$

То есть текущая reduced BQG chain **точно унитарно эквивалентна open XX model**.

После Jordan-Wigner:

$$
\boxed{
H_M
=\frac32(M-1)I
-\frac32\sum_{i=1}^{M-1}
(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i).
}
$$

Задача становится free-fermionic.

Single-particle momenta:

$$
k_n=\frac{n\pi}{M+1}.
$$

Exact energies:

$$
\boxed{
\varepsilon_n
=-3\cos\left(\frac{n\pi}{M+1}\right).
}
$$

Full many-body spectrum:

$$
\boxed{
E
=\frac32(M-1)
+\sum_{n=1}^{M}\varepsilon_nN_n,
\qquad N_n\in\{0,1\}.
}
$$

Следовательно exponential diagonalization $2^M\times2^M$ не нужна.

---

# 7. Exact parity effect and gap

Для odd $M$ существует exact zero mode:

$$
\boxed{
M\ \text{odd}\Rightarrow g_0=2.
}
$$

Это объясняет двухкратную ground degeneracy при $M=3$.

Для even $M$:

$$
\boxed{
M\ \text{even}\Rightarrow g_0=1.
}
$$

Finite-size gap для even $M$:

$$
\boxed{
\Delta_M^{\rm even}
=3\sin\left(\frac{\pi}{2(M+1)}\right).
}
$$

Для odd $M$, после zero-mode ground degeneracy:

$$
\boxed{
\Delta_M^{\rm odd}
=3\sin\left(\frac{\pi}{M+1}\right).
}
$$

Отсюда:

$$
\boxed{
\Delta_M\to0\quad\text{как}\quad O(M^{-1}).
}
$$

Текущая candidate reduced chain gapless в thermodynamic limit.

Формулы проверены explicit diagonalization для

$$
M=2,3,4,5,6.
$$

**Статус: EXACT для текущего candidate reduced Hamiltonian.**

Файлы:

- `BQG_MANY_NODE_FREE_FERMION_MAPPING.md`
- `scripts/bqg_many_node_xx_mapping_gate.py`

---

# 8. Что это меняет

Наивный путь требовал бы diagonalization пространства размера

$$
2^M.
$$

Новая exact reduction заменяет его one-particle problem размера

$$
M.
$$

И главное: стало ясно, что текущая 1D reduced gluing model — не generic interacting system, а critical free-fermion chain.

Поэтому следующий фронтир надо решать через exact correlation functions и asymptotics.

---

# 9. Каноническая цепочка новой ветки на сегодня

$$
\boxed{
\text{SU(2)-invariant local node}
\to
\text{noncommuting pair geometry}
\to
\text{oriented volume}
\to
\text{local isotropy}
\to
\text{two-node entangled gluing}
\to
\text{three-node distance hierarchy}
\to
\text{exact XX/free-fermion many-node mapping}.
}
$$

Самые сильные exact statements:

1. $Q=i[D_{12},D_{23}]$;
2. $Q_{\rm phys}=(\sqrt3/4)\sigma_y$;
3. local isotropy iff local oriented volume is sharp;
4. $\mathcal A_p=4(\Delta Q)^2$;
5. exact two-node shape matching selects a Bell-type intertwiner state;
6. relative orientation can be sharp while local orientation is uncertain;
7. a three-node chain distinguishes graph distance $1$ and $2$ by both mutual information and volume correlations;
8. the complete current 1D reduced chain maps exactly to free fermions;
9. its gap closes as $O(1/M)$.

---

# 10. Что пока НЕ доказано

Мы не утверждаем, что:

- fundamental BQG обязана иметь exactly этот $H_{\rm glue}$;
- continuum space уже доказано трёхмерно;
- mutual information является уникальным physical distance;
- critical 1D chain сама по себе является пространством нашей Вселенной;
- Einstein dynamics уже получена;
- Lorentzian causal cone уже выведен;
- $G$, $c$, $\hbar$ выведены из binary microphysics.

Ключевой caveat:

$$
\boxed{
\text{exact mathematics of the reduced model}
\neq
\text{proof that the reduced model is fundamental dynamics}.
}
$$

---

# 11. Следующий настоящий расчёт

Теперь не надо увеличивать matrix dimension.

Следующий шаг:

$$
\boxed{
\textbf{derive exact correlation scaling }I(r)\textbf{ and geometric observables from the free-fermion solution.}
}
$$

Приоритет:

1. exact fermionic two-point function $\langle c_i^\dagger c_j\rangle$;
2. logical $X,Y,Z$ correlators versus separation $r$;
3. asymptotic mutual-information decay $I(r)$;
4. проверить наличие/отсутствие finite correlation length;
5. построить correlation-distance law;
6. сравнить chain, ring, square-lattice и branching connectivity;
7. только после этого строить настоящий emergent-dimension estimator;
8. параллельно пытаться вывести $H_{\rm glue}$ из fundamental BQG constraint/history dynamics, а не принимать его как ansatz.

---

# 12. Канонический принцип проекта

> **Сначала уменьшить задачу симметрией. Затем распознать точную математическую структуру. Потом решить её аналитически. И только если это невозможно — считать численно.**

Репозиторий: `Shtenco/binary_quantum_theory`
