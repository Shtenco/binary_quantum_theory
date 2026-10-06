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
\text{relational distance}
\to
\text{dimension}
\to
\text{effective gravity}
}
$$

Канонический метод проекта:

$$
\boxed{\text{симметрия сначала, вычисления потом}.}
$$

Мы сначала редуцируем Hilbert space, затем ищем exact algebraic structure, затем asymptotics, и только если это невозможно — используем тяжёлую численность.

---

# 2. Почему новая ветка

Минимальная static spherical shadow-ветка дала полезный no-go: в заявленном секторе собственная ненулевая BQG hair-поправка не возникла.

Поэтому новый фронтир — не подгонять функцию метрики, а спросить, откуда сама геометрия может появиться.

Старые SU(2)/Peter-Weyl, graph-changing constraints, HDA, Regge, Plebanski/Urbantke, TT/EFT, cosmology и 2T/Weyl файлы остаются библиотекой результатов, но не задают канонический порядок новой emergence-ветки.

---

# 3. Один physical node: exact local theorem

Для четырёх spin-$1/2$ после SU(2) Gauss / total-spin-zero reduction:

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

удовлетворяет точному operator identity

$$
\boxed{
Q_{123}
=i[\mathbf J_1\!\cdot\!\mathbf J_2,\mathbf J_2\!\cdot\!\mathbf J_3].
}
$$

В physical sector:

$$
\boxed{Q_{123}^{\rm phys}=\frac{\sqrt3}{4}\sigma_y.}
$$

Eigenstates:

$$
\boxed{
|\Psi_\pm\rangle
=\frac{|s\rangle\pm i|t\rangle}{\sqrt2},
\qquad q_\pm=\pm\frac{\sqrt3}{4}.
}
$$

Именно эти два states являются единственными pure pair-spectrum isotropic states.

Если

$$
\mathcal A_p
=\sum_{i<j}\left(p_{ij}-\frac12\right)^2,
$$

то для любого pure physical state

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

**Статус: EXACT.**

Файлы:

- `BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md`
- `scripts/bqg_minimal_entanglement_volume_gate.py`

---

# 4. Два physical nodes: reduced gluing

Для двух локально редуцированных узлов

$$
\dim\mathcal H_{AB}^{\rm red}=4.
$$

Используем три local shape projectors

$$
P_{12}=\frac12(I+Z),
$$

$$
P_{13}=\frac12I+\frac{\sqrt3}{4}X-\frac14Z,
$$

$$
P_{14}=\frac12I-\frac{\sqrt3}{4}X-\frac14Z.
$$

Candidate reduced shape-matching Hamiltonian:

$$
\boxed{
H_{\rm glue}
=\sum_a(P_a^{(A)}-P_a^{(B)})^2
=\frac32I-\frac34(X_AX_B+Z_AZ_B).
}
$$

Его spectrum:

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

но relative orientation фиксирована:

$$
\boxed{Q_AQ_B|\Phi^+\rangle=-\frac3{16}|\Phi^+\rangle.}
$$

**Статус spectrum/result: EXACT для заданного reduced Hamiltonian.**  
**Статус самого $H_{\rm glue}$ как фундаментальной BQG dynamics: CANDIDATE.**

Файлы:

- `BQG_TWO_NODE_REDUCED_GLUING_RESULT.md`
- `scripts/bqg_two_node_reduced_gluing_gate.py`

---

# 5. Три узла: первый network-distance hierarchy

Для open chain $A-B-C$:

$$
\dim\mathcal H_{ABC}^{\rm red}=8.
$$

При

$$
H_3=H_{AB}+H_{BC}
$$

symmetry-neutral ground state даёт

$$
\boxed{I(A:B)=I(B:C)\approx0.7982479266\ \text{bit},}
$$

а

$$
\boxed{I(A:C)=0.5\ \text{bit}.}
$$

Следовательно

$$
\boxed{I_{\rm nearest}>I_{\rm next-nearest}.}
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
\boxed{\langle Q_AQ_C\rangle=0.}
$$

То есть topology уже отражается в двух независимых quantum-geometric observables.

**Статус: EXACT для reduced nearest-neighbor model.**

Файлы:

- `BQG_THREE_NODE_REDUCED_CHAIN_RESULT.md`
- `scripts/bqg_three_node_reduced_chain_gate.py`

---

# 6. Вся many-node chain решается аналитически

Для $M$ узлов

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

После локальной rotation:

$$
\boxed{
H_M\simeq
\frac32(M-1)I
-\frac34\sum_{i=1}^{M-1}(X_iX_{i+1}+Y_iY_{i+1}).
}
$$

То есть reduced BQG chain точно унитарно эквивалентна open XX model.

Jordan-Wigner даёт free fermions:

$$
\boxed{
H_M
=\frac32(M-1)I
-\frac32\sum_{i=1}^{M-1}
(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i).
}
$$

Single-particle spectrum:

$$
\boxed{
\varepsilon_n
=-3\cos\left(\frac{n\pi}{M+1}\right).
}
$$

Поэтому exponential diagonalization $2^M\times2^M$ не нужна.

Gap:

$$
\boxed{
\Delta_M^{\rm even}
=3\sin\left(\frac{\pi}{2(M+1)}\right),
}
$$

$$
\boxed{
\Delta_M^{\rm odd}
=3\sin\left(\frac{\pi}{M+1}\right).
}
$$

Следовательно

$$
\boxed{\Delta_M=O(M^{-1})\to0.}
$$

Текущая reduced chain critical/gapless в thermodynamic limit.

Файлы:

- `BQG_MANY_NODE_FREE_FERMION_MAPPING.md`
- `scripts/bqg_many_node_xx_mapping_gate.py`

---

# 7. Новый exact asymptotic geometry calculation

Теперь большой Hilbert space вообще не нужен.

В thermodynamic bulk limit half-filled XX chain имеет exact fermionic correlator

$$
\boxed{
C_f(r)
=\langle c_0^\dagger c_r\rangle
=\frac{\sin(\pi r/2)}{\pi r}.
}
$$

Важно: physical logical-spin transverse correlator не равен $C_f(r)$, потому что Jordan-Wigner transformation содержит string.

Для longitudinal logical correlator:

$$
\boxed{
C_z(r)
=\langle Z_0Z_r\rangle
=-4|C_f(r)|^2
=-\frac{4\sin^2(\pi r/2)}{\pi^2r^2}.
}
$$

Следовательно

$$
C_z(r)=0\quad(r\;\text{even}),
$$

и

$$
C_z(r)=-\frac{4}{\pi^2r^2}\quad(r\;\text{odd}).
$$

Transverse correlator имеет exact Toeplitz form

$$
\boxed{
C_x(r)=\langle X_0X_r\rangle
=\det_{1\le j,k\le r}G_{j-k-1},
}
$$

где

$$
G_n=\frac{2\sin(\pi n/2)}{\pi n},\qquad G_0=0.
$$

Fisher-Hartwig asymptotics даёт

$$
\boxed{
C_x(r)=A_xr^{-1/2}[1+O(r^{-2})].
}
$$

Для нашей Pauli normalization

$$
A_x\approx0.58835.
$$

---

# 8. Exact two-site density matrix and mutual information

U(1) symmetry, zero magnetization и translation invariance фиксируют pair state:

$$
\boxed{
\rho_{0r}
=\frac14\left[
I\otimes I
+C_x(r)(X\otimes X+Y\otimes Y)
+C_z(r)Z\otimes Z
\right].
}
$$

Eigenvalues:

$$
\boxed{
\lambda_{1,2}=\frac{1+C_z}{4},
}
$$

$$
\boxed{
\lambda_{\pm}=\frac{1-C_z\pm2C_x}{4}.
}
$$

Каждый single node maximally mixed:

$$
\rho_i=I/2,\qquad S_i=1\ \text{bit}.
$$

Поэтому exact mutual information:

$$
\boxed{
I(r)=2+\sum_{a=1}^{4}\lambda_a(r)\log_2\lambda_a(r).
}
$$

Это уже closed thermodynamic-limit formula после подстановки Toeplitz determinant $C_x(r)$.

---

# 9. Главный новый asymptotic result

При больших $r$:

$$
C_x(r)=O(r^{-1/2}),
\qquad
C_z(r)=O(r^{-2}).
$$

Entropy expansion около $I_4/4$ даёт

$$
\boxed{
I(r)
=\frac{C_x(r)^2}{\ln2}
+\frac{C_z(r)^2}{2\ln2}
+O(C_x^4,C_x^2C_z,C_z^3).
}
$$

Следовательно

$$
\boxed{
I(r)
=\frac{A_x^2}{\ln2}\frac1r
+O(r^{-2}).
}
$$

Обозначая

$$
\kappa=\frac{A_x^2}{\ln2},
$$

получаем

$$
\boxed{\kappa\approx0.4994.}
$$

То есть practically

$$
\boxed{
I(r)\approx\frac{0.50}{r}\ \text{bit}.
}
$$

Главный закон:

$$
\boxed{I(r)\propto r^{-1}.}
$$

Gate на exact Toeplitz determinants подтверждает

$$
rI(r)\to0.5
$$

для больших separations.

**Статус: analytic asymptotic result для текущей exact XX reduction + independent determinant check.**

Файлы:

- `BQG_MUTUAL_INFORMATION_ASYMPTOTIC_RESULT.md`
- `scripts/bqg_mutual_information_asymptotic_gate.py`

---

# 10. Falsification result для distance maps

Теперь можно проверить конкретные distance laws.

## Negative-log map

Если

$$
d_{\log}(r)
=-\ell_*\ln\frac{I(r)}{I_*},
$$

то из $I(r)\sim\kappa/r$ следует

$$
\boxed{
d_{\log}(r)=\ell_*\ln r+\text{const}+o(1).}
$$

Следовательно standard negative-log information distance **не воспроизводит linear graph distance** текущей critical chain.

Это настоящий отрицательный результат, а не проблема вычислений.

## Inverse-information map

Если вместо этого

$$
d_{\rm inv}(r)=\ell_*\frac{I_*}{I(r)},
$$

то

$$
\boxed{d_{\rm inv}(r)\propto r.}
$$

То есть $1/I$ способен восстановить linear asymptotic distance именно в этой critical model.

Но мы **не объявляем** это фундаментальной формулой BQG, потому что выбор $1/I$ после знания результата был бы post-hoc.

---

# 11. Что мы поняли о расстоянии

Критическое отличие:

- в gapped phase обычно ожидается
  $$I(r)\sim e^{-r/\xi},$$
  и тогда
  $$-\ln I(r)\sim r/\xi;$$

- в нашей current critical phase
  $$I(r)\sim r^{-1},$$
  и тогда
  $$-\ln I(r)\sim\ln r.$$

Следовательно универсальное правило

$$
\boxed{d\propto-\ln I}
$$

не может быть принято без дополнительного принципа.

Настоящий BQG distance должен быть **выведен**, а не выбран.

Кандидаты для следующего derivation gate:

1. Bures/Fisher information geometry;
2. additive local edge cost из conditional mutual information;
3. modular-Hamiltonian response;
4. shortest-path reconstruction from local correlation weights;
5. comparison critical vs deliberately gapped deformation.

---

# 12. Каноническая цепочка новой ветки на сегодня

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
\text{network distance hierarchy}
\to
\text{XX/free fermions}
\to
\text{exact correlation asymptotics}
\to
I(r)\sim r^{-1}.
}
$$

Самые сильные statements:

1. $Q=i[D_{12},D_{23}]$;
2. $Q_{\rm phys}=(\sqrt3/4)\sigma_y$;
3. local isotropy iff local oriented volume is sharp;
4. $\mathcal A_p=4(\Delta Q)^2$;
5. reduced two-node gluing selects a Bell-type intertwiner state;
6. three nodes already distinguish nearest and next-nearest separation;
7. complete current 1D reduced chain maps exactly to free fermions;
8. its gap closes as $O(1/M)$;
9. $C_x(r)\sim r^{-1/2}$;
10. **mutual information decays as $I(r)\sim\kappa/r$**;
11. negative-log information distance gives $\ln r$, not $r$;
12. therefore the physical distance functional remains an OPEN derivation problem.

---

# 13. Что пока НЕ доказано

Мы не утверждаем, что:

- fundamental BQG обязана иметь exactly этот $H_{\rm glue}$;
- continuum space уже доказано трёхмерно;
- mutual information itself uniquely defines distance;
- $1/I$ является фундаментальной метрикой;
- critical 1D chain описывает пространство нашей Вселенной;
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

# 14. Следующий настоящий расчёт

Теперь лучший falsification-first шаг:

$$
\boxed{
\textbf{controlled gapped deformation of the same reduced chain.}
}
$$

Нужно ввести минимальную deformation, которая сохраняет понятный microscopic meaning, но открывает gap, затем аналитически проверить

$$
I(r):\quad r^{-1}\longrightarrow e^{-r/\xi}\times\text{power correction}.
$$

После этого сравнить candidate distance functionals **на двух фазах одной и той же модели**.

Если одна и та же formula $d[I]$ не восстанавливает один и тот же graph distance одновременно в critical и gapped regimes, она исключается как universal BQG distance.

Это намного сильнее, чем просто подобрать функцию под один asymptotic law.

---

# 15. Канонический принцип

> **Сначала уменьшить задачу симметрией. Затем распознать точную математическую структуру. Потом решить её аналитически. И только если это невозможно — считать численно.**

Репозиторий: `Shtenco/binary_quantum_theory`
