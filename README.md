# Бинарная квантовая гравитация (BQG)
## Emergence Program: от бинарной квантовой информации к геометрии

**Канонический README — 6 октября 2026**

---

# 1. Главный вопрос

> **Может ли геометрия, расстояние и затем гравитация возникать из физической структуры бинарной квантовой информации?**

Текущая рабочая цепочка:

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
\text{phase-robust relational geometry}
\to
\text{dimension}
\to
\text{causality}
\to
\text{effective gravity}
}
$$

Канонический метод:

$$
\boxed{\text{симметрия сначала, вычисления потом}.}
$$

Мы редуцируем Hilbert space, ищем exact algebraic structure, выводим asymptotics, затем используем численность только как независимый gate.

---

# 2. Один physical node: exact local theorem

Для четырёх spin-$1/2$ после SU(2) Gauss reduction:

$$
\boxed{
\mathcal H_{\rm phys}^{(4)}
=\mathrm{Inv}_{SU(2)}[(\tfrac12)^{\otimes4}],
\qquad \dim=2.
}
$$

В basis $|s\rangle,|t\rangle$ oriented volume

$$
Q_{123}=\epsilon_{abc}J_1^aJ_2^bJ_3^c
$$

удовлетворяет

$$
\boxed{
Q_{123}=i[\mathbf J_1\!\cdot\!\mathbf J_2,\mathbf J_2\!\cdot\!\mathbf J_3].
}
$$

В physical sector:

$$
\boxed{Q_{123}^{\rm phys}=\frac{\sqrt3}{4}\sigma_y.}
$$

Volume eigenstates:

$$
\boxed{
|\Psi_\pm\rangle=\frac{|s\rangle\pm i|t\rangle}{\sqrt2},
\qquad q_\pm=\pm\frac{\sqrt3}{4}.
}
$$

Именно они являются единственными pure pair-spectrum isotropic states.

Для

$$
\mathcal A_p=\sum_{i<j}\left(p_{ij}-\frac12\right)^2
$$

выполняется exact identity

$$
\boxed{\mathcal A_p=4(\Delta Q_{123})^2.}
$$

Следовательно

$$
\boxed{
\text{pair-spectrum isotropy}
\Longleftrightarrow
\text{sharp oriented quantum volume}.
}
$$

Файлы:

- `BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md`
- `scripts/bqg_minimal_entanglement_volume_gate.py`

---

# 3. Два physical nodes: reduced gluing

Три local shape projectors дают candidate matching Hamiltonian

$$
\boxed{
H_{\rm glue}
=\sum_a(P_a^{(A)}-P_a^{(B)})^2
=\frac32I-\frac34(X_AX_B+Z_AZ_B).
}
$$

Spectrum:

$$
\boxed{\{0,\tfrac32,\tfrac32,3\}.}
$$

Unique zero-mismatch state:

$$
\boxed{|\Phi^+\rangle=\frac{|ss\rangle+|tt\rangle}{\sqrt2}.}
$$

Локально

$$
\langle Q_A\rangle=\langle Q_B\rangle=0,
$$

но

$$
\boxed{Q_AQ_B|\Phi^+\rangle=-\frac3{16}|\Phi^+\rangle.}
$$

То есть local orientation становится неопределённой, а relative orientation остаётся sharp.

**Статус математики: EXACT для заданного reduced Hamiltonian.**  
**Статус $H_{\rm glue}$ как fundamental BQG dynamics: CANDIDATE.**

Файлы:

- `BQG_TWO_NODE_REDUCED_GLUING_RESULT.md`
- `scripts/bqg_two_node_reduced_gluing_gate.py`

---

# 4. Три узла: первый network-distance hierarchy

Для chain $A-B-C$ symmetry-neutral ground sector даёт

$$
\boxed{I(A:B)=I(B:C)\approx0.7982479266\ \text{bit},}
$$

$$
\boxed{I(A:C)=0.5\ \text{bit}.}
$$

То есть

$$
\boxed{I_{\rm nearest}>I_{\rm next-nearest}.}
$$

Volume correlations независимо подтверждают topology:

$$
\boxed{
\langle Q_AQ_B\rangle=\langle Q_BQ_C\rangle=-\frac3{32},
\qquad
\langle Q_AQ_C\rangle=0.
}
$$

Файлы:

- `BQG_THREE_NODE_REDUCED_CHAIN_RESULT.md`
- `scripts/bqg_three_node_reduced_chain_gate.py`

---

# 5. Exact many-node reduction

Для $M$ узлов

$$
\boxed{
H_M
=\sum_{i=1}^{M-1}
\left[
\frac32I-\frac34(X_iX_{i+1}+Z_iZ_{i+1})
\right].
}
$$

После локальной rotation:

$$
\boxed{
H_M\simeq
\frac32(M-1)I
-\frac34\sum_i(X_iX_{i+1}+Y_iY_{i+1}).
}
$$

То есть current reduced chain точно эквивалентна open XX model.

Jordan-Wigner:

$$
\boxed{
H_M
=\frac32(M-1)I
-\frac32\sum_i(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i).
}
$$

Single-particle energies:

$$
\boxed{
\varepsilon_n=-3\cos\frac{n\pi}{M+1}.
}
$$

Gap:

$$
\boxed{
\Delta_M^{\rm even}=3\sin\frac{\pi}{2(M+1)},
\qquad
\Delta_M^{\rm odd}=3\sin\frac{\pi}{M+1}.
}
$$

Следовательно

$$
\boxed{\Delta_M=O(M^{-1})\to0.}
$$

Current chain critical/gapless.

Файлы:

- `BQG_MANY_NODE_FREE_FERMION_MAPPING.md`
- `scripts/bqg_many_node_xx_mapping_gate.py`

---

# 6. Critical correlation asymptotics

В thermodynamic bulk limit

$$
\boxed{
\langle c_0^\dagger c_r\rangle
=\frac{\sin(\pi r/2)}{\pi r}.
}
$$

Longitudinal logical correlator:

$$
\boxed{
C_z(r)
=-\frac{4\sin^2(\pi r/2)}{\pi^2r^2}.
}
$$

Transverse correlator содержит Jordan-Wigner string и имеет Toeplitz form. Fisher-Hartwig asymptotics:

$$
\boxed{
C_x(r)=A_xr^{-1/2}[1+O(r^{-2})],
\qquad A_x\approx0.58835.
}
$$

Two-site reduced state:

$$
\boxed{
\rho_{0r}
=\frac14\left[
I\otimes I+C_x(r)(X\otimes X+Y\otimes Y)+C_z(r)Z\otimes Z
\right].
}
$$

Entropy expansion gives

$$
\boxed{
I_0(r)
=\frac{A_x^2}{\ln2}\frac1r+O(r^{-2}).
}
$$

Numerically

$$
\boxed{
I_0(r)\approx\frac{0.50}{r}\ \text{bit}.
}
$$

Therefore

$$
\boxed{I_0(r)\propto r^{-1}.}
$$

Файлы:

- `BQG_MUTUAL_INFORMATION_ASYMPTOTIC_RESULT.md`
- `scripts/bqg_mutual_information_asymptotic_gate.py`

---

# 7. Первый distance-map falsification

For critical phase:

$$
I_0(r)\sim\frac{\kappa}{r}.
$$

Negative-log map gives

$$
\boxed{
-\ln I_0(r)=\ln r+\text{const}+o(1),
}
$$

не linear distance.

Inverse-information map would give

$$
1/I_0(r)\propto r,
$$

но объявлять $1/I$ фундаментальным distance после знания asymptotics было бы post-hoc.

---

# 8. Controlled gapped deformation

Чтобы проверить distance law на второй фазе той же модели, вводим exactly solvable staggered deformation в XX frame:

$$
\boxed{
H_m=H_0+m\sum_j(-1)^j Z_j.
}
$$

После Jordan-Wigner это alternating onsite mass.

Важно: в исходном intertwiner basis rotated $Z$ соответствует local $Y$, а

$$
Q_j=\frac{\sqrt3}{4}Y_j.
$$

Поэтому deformation имеет quantum-geometric interpretation:

$$
\boxed{
H_m-H_0\propto\sum_j(-1)^jQ_j,
}
$$

то есть это staggered oriented-volume bias.

**Статус этой deformation как fundamental BQG term: CANDIDATE.**

---

# 9. Exact gapped spectrum

Для two-site unit cell single-particle bands:

$$
\boxed{
E_\pm(k)
=\pm\sqrt{(2m)^2+9\cos^2k}.
}
$$

Minimum positive energy:

$$
\boxed{\Delta_{\rm sp}=2|m|.}
$$

Каждый $m\neq0$ открывает gap.

Nearest complex branch point даёт exact correlation length

$$
\boxed{
\xi^{-1}
=\operatorname{arsinh}\left(\frac{2|m|}{3}\right),
}
$$

то есть

$$
\boxed{
\xi(m)
=\frac1{\operatorname{arsinh}(2|m|/3)}.
}
$$

При малом $m$:

$$
\boxed{\xi\sim\frac{3}{2|m|}.}
$$

Для gate-point $m=0.2$:

$$
\boxed{
\Delta_{\rm sp}=0.4,
\qquad
\xi\approx7.5221113.
}
$$

---

# 10. Gapped correlation and mutual-information law

В gapped phase transverse logical correlator имеет large-distance form

$$
\boxed{
C_x^{(m)}(r)
\sim A(m)r^{-1/2}e^{-r/\xi}.
}
$$

Mutual information quadratic in small connected correlators, поэтому

$$
\boxed{
I_m(r)
\sim B(m)r^{-1}e^{-2r/\xi}.
}
$$

Следовательно MI correlation length

$$
\boxed{\xi_I=\frac\xi2.}
$$

Independent finite-chain quadratic gate подтверждает:

- exact gap $2|m|$;
- exact $\xi$;
- $C_x\sim r^{-1/2}e^{-r/\xi}$;
- $I\sim r^{-1}e^{-2r/\xi}$.

Файлы:

- `BQG_GAPPED_DEFORMATION_DISTANCE_NOGO.md`
- `scripts/bqg_gapped_distance_nogo_gate.py`

---

# 11. Новый no-go theorem: pair mutual information недостаточна для universal distance

Теперь у нас две controlled phases одной underlying graph geometry.

Critical:

$$
\boxed{I_0(r)\sim\kappa/r.}
$$

Gapped:

$$
\boxed{I_m(r)\sim Br^{-1}e^{-2r/\xi}.}
$$

Предположим universal phase-independent scalar distance

$$
d(r)=f(I(r))\sim ar+b.
$$

В critical phase:

$$
r\sim\frac{\kappa}{I},
$$

поэтому linearity требует

$$
\boxed{f(I)\sim A/I\qquad(I\to0).}
$$

В gapped phase inversion даёт

$$
r=\frac\xi2\ln\frac1I+O(\ln\ln(1/I)),
$$

поэтому linearity требует

$$
\boxed{f(I)\sim A'\ln(1/I)\qquad(I\to0).}
$$

Эти asymptotics несовместимы.

Следовательно:

$$
\boxed{
\textbf{не существует одной phase-independent scalar function }
 d=f(I_{ij})
\textbf{, которая asymptotically linear в обеих фазах.}
}
$$

Это более сильный результат, чем предыдущий no-go только для $-\ln I$.

Он исключает **весь класс universal pairwise scalar distances, зависящих только от mutual information одной пары**.

---

# 12. Что это означает физически

Mutual information остаётся полезным relational observable, но одного числа $I_{ij}$ недостаточно, чтобы универсально восстановить расстояние.

Physical distance должен использовать более богатую network-level structure, например:

- local neighborhood correlation profile;
- correlation length / gap data;
- full reduced density matrix;
- conditional mutual information;
- multipartite entanglement;
- graph/transfer Laplacian;
- modular response;
- information geometry.

То есть новый вопрос уже не

$$
\text{«какую функцию }f(I)\text{ выбрать?»}
$$

а

$$
\boxed{
\textbf{какой relational operator / variational principle сам определяет metric?}
}
$$

---

# 13. Каноническая цепочка новой ветки на сегодня

$$
\boxed{
\text{SU(2) physical node}
\to
\text{noncommuting pair geometry}
\to
\text{oriented volume}
\to
\text{local isotropy}
\to
\text{entangled gluing}
\to
\text{network hierarchy}
\to
\text{XX/free fermions}
\to
I_0(r)\sim r^{-1}
\to
\text{gapped volume deformation}
\to
I_m(r)\sim r^{-1}e^{-2r/\xi}
\to
\text{scalar-distance no-go}.
}
$$

Самые сильные current results:

1. $Q=i[D_{12},D_{23}]$;
2. $Q_{\rm phys}=(\sqrt3/4)\sigma_y$;
3. local isotropy iff oriented volume is sharp;
4. $\mathcal A_p=4(\Delta Q)^2$;
5. two-node matching selects Bell-type intertwiner entanglement;
6. three nodes distinguish graph separation by MI and volume correlations;
7. complete current 1D reduced chain maps exactly to free fermions;
8. critical gap closes as $O(M^{-1})$;
9. critical $I_0(r)\sim\kappa/r$;
10. staggered oriented-volume deformation opens exact gap $2|m|$;
11. its correlation length is $\xi^{-1}=\operatorname{arsinh}(2|m|/3)$;
12. gapped $I_m(r)\sim Br^{-1}e^{-2r/\xi}$;
13. **no universal phase-independent scalar distance $d=f(I_{ij})$ can be linear in both phases.**

---

# 14. Что пока НЕ доказано

Мы не утверждаем, что:

- $H_{\rm glue}$ уже выведен из fundamental graph-changing BQG constraint;
- staggered-volume term является фундаментальным vacuum deformation;
- continuum space уже доказано трёхмерно;
- mutual information uniquely defines geometry;
- current 1D reduced chain описывает пространство нашей Вселенной;
- Einstein equations уже получены;
- Lorentzian causal cone уже выведен;
- $G$, $c$, $\hbar$ уже выведены из binary microphysics.

Ключевой caveat:

$$
\boxed{
\text{exact mathematics of the reduced model}
\neq
\text{proof that the reduced model is fundamental dynamics}.
}
$$

---

# 15. Следующий настоящий расчёт

После scalar-distance no-go нельзя честно подбирать ещё одну функцию $f(I)$.

Следующий falsification-first frontier:

$$
\boxed{
\textbf{derive a network-level additive metric from local quantum information.}
}
$$

Первый дешёвый кандидат — **local edge cost + shortest path**, где edge weight выводится из local reduced states / conditional information, а не из long-range pair $I_{ij}$.

Нужно проверить одновременно:

1. critical chain;
2. gapped staggered-volume chain;
3. finite ring;
4. затем branching graph.

Успешный distance estimator должен:

- давать additive path length;
- не зависеть от того, critical или gapped bulk state;
- различать topology;
- иметь continuum scaling;
- не требовать post-hoc знания graph distance.

Только после этого имеет смысл вычислять spectral dimension и causal propagation.

---

# 16. Канонический принцип

> **Сначала уменьшить задачу симметрией. Затем распознать точную математическую структуру. Потом решить её аналитически. Отрицательные результаты фиксировать так же строго, как положительные. И только если exact путь закрыт — считать численно.**

Репозиторий: `Shtenco/binary_quantum_theory`
