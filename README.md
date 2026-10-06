# Бинарная квантовая гравитация (BQG)
## Emergence Program: от бинарной квантовой информации к геометрии

**Канонический README — 6 октября 2026**

---

# 1. Главный вопрос

> **Может ли геометрия, расстояние, размерность и затем гравитация возникать из физической структуры бинарной квантовой информации?**

Текущая цепочка проекта:

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
\text{local information response}
\to
\text{weighted graph geometry}
\to
\text{spectral dimension}
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

Мы сначала уменьшаем Hilbert space, затем ищем exact algebraic structure, затем asymptotics и только потом используем численность как независимый gate.

---

# 2. Один physical node: exact local theorem

Для четырёх spin-$1/2$ после SU(2) Gauss reduction

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

удовлетворяет exact identity

$$
\boxed{
Q_{123}=i[\mathbf J_1\!\cdot\!\mathbf J_2,\mathbf J_2\!\cdot\!\mathbf J_3].
}
$$

В physical sector

$$
\boxed{Q_{123}^{\rm phys}=\frac{\sqrt3}{4}\sigma_y.}
$$

Volume eigenstates

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

выполняется

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

Spectrum

$$
\boxed{\{0,\tfrac32,\tfrac32,3\}.}
$$

Unique zero-mismatch state

$$
\boxed{|\Phi^+\rangle=\frac{|ss\rangle+|tt\rangle}{\sqrt2}.}
$$

Локально

$$
\langle Q_A\rangle=\langle Q_B\rangle=0,
$$

но relative orientation sharp:

$$
\boxed{Q_AQ_B|\Phi^+\rangle=-\frac3{16}|\Phi^+\rangle.}
$$

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

После локальной rotation

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

Single-particle energies

$$
\boxed{\varepsilon_n=-3\cos\frac{n\pi}{M+1}.}
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

Longitudinal logical correlator

$$
\boxed{
C_z(r)
=-\frac{4\sin^2(\pi r/2)}{\pi^2r^2}.
}
$$

Transverse correlator содержит Jordan-Wigner string и имеет Toeplitz/Fisher-Hartwig asymptotics

$$
\boxed{
C_x(r)=A_xr^{-1/2}[1+O(r^{-2})],
\qquad A_x\approx0.58835.
}
$$

Entropy expansion даёт

$$
\boxed{
I_0(r)=\frac{A_x^2}{\ln2}\frac1r+O(r^{-2})
\approx\frac{0.50}{r}\ \text{bit}.
}
$$

Файлы:

- `BQG_MUTUAL_INFORMATION_ASYMPTOTIC_RESULT.md`
- `scripts/bqg_mutual_information_asymptotic_gate.py`

---

# 7. Controlled gapped deformation

В XX frame вводим exactly solvable staggered deformation

$$
\boxed{
H_m=H_0+m\sum_j(-1)^j Z_j.
}
$$

В исходном intertwiner basis это staggered oriented-volume bias, поскольку

$$
Q_j=\frac{\sqrt3}{4}Y_j.
$$

Two-band spectrum

$$
\boxed{
E_\pm(k)=\pm\sqrt{(2m)^2+9\cos^2k}.
}
$$

Gap

$$
\boxed{\Delta_{\rm sp}=2|m|.}
$$

Correlation length

$$
\boxed{
\xi^{-1}=\operatorname{arsinh}\left(\frac{2|m|}{3}\right).
}
$$

Large-distance laws

$$
\boxed{
C_x^{(m)}(r)\sim A(m)r^{-1/2}e^{-r/\xi},
}
$$

$$
\boxed{
I_m(r)\sim B(m)r^{-1}e^{-2r/\xi}.
}
$$

Файлы:

- `BQG_GAPPED_DEFORMATION_DISTANCE_NOGO.md`
- `scripts/bqg_gapped_distance_nogo_gate.py`

---

# 8. Scalar-distance no-go

Critical phase:

$$
I_0(r)\sim\kappa/r.
$$

Gapped phase:

$$
I_m(r)\sim Br^{-1}e^{-2r/\xi}.
$$

Если universal scalar distance имеет вид

$$
d(r)=f(I(r))\sim ar+b,
$$

то critical phase требует

$$
\boxed{f(I)\sim A/I\qquad(I\to0),}
$$

а gapped phase требует

$$
\boxed{f(I)\sim A'\ln(1/I)\qquad(I\to0).}
$$

Эти asymptotics несовместимы.

Следовательно

$$
\boxed{
\textbf{не существует одной phase-independent scalar function }
d=f(I_{ij})
\textbf{, asymptotically linear в обеих фазах.}
}
$$

То есть long-range pair mutual information может быть observable, но не универсальной spatial coordinate.

---

# 9. Новый поворот: correlation как conductance, а не distance

После scalar-distance no-go мы перестаём инвертировать long-range correlation law.

Вместо этого для каждого локального edge

$$
e=(ij)
$$

используем полную reduced state

$$
\rho_e=\rho_{ij}
$$

и извлекаем **локальную information conductance**.

Тогда geometry строится network-wise:

$$
\boxed{
\text{local state}
\to
\text{edge conductance}
\to
\text{edge resistance length}
\to
\text{shortest-path metric}.
}
$$

Это принципиально отличается от

$$
d_{ij}=f(I_{ij}),
$$

потому что дальняя distance больше не извлекается из дальней корреляции напрямую.

---

# 10. Relative-twist quantum Fisher conductance

Для edge $e=(ij)$ вводим локальный относительный twist generator

$$
\boxed{
K_e=\frac{Z_i-Z_j}{2}.
}
$$

Рассматриваем unitary family

$$
\rho_e(\theta)=e^{-i\theta K_e}\rho_e e^{+i\theta K_e}.
$$

Quantum Fisher information

$$
F_Q(\rho_e,K_e)
=2\sum_{a,b}
\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}
|\langle a|K_e|b\rangle|^2.
$$

Определяем local QFI conductance

$$
\boxed{
g_e^{\rm QFI}=\frac14F_Q(\rho_e,K_e).}
$$

Фактор $1/4$ совпадает со стандартной Bures/Fisher normalization

$$
ds_B^2=\frac14F_Q\,d\theta^2.
$$

Таким образом $g_e$ измеряет **локальную чувствительность physical edge state к relative relational deformation**.

Это уже не просто «сколько два узла коррелированы», а operational response coefficient.

---

# 11. Exact critical QFI scale

Для thermodynamic critical reference chain nearest-neighbor correlators дают exact

$$
\boxed{
F_{Q,*}=\frac{32}{\pi^2+4}.
}
$$

Следовательно

$$
\boxed{
g_*=\frac{8}{\pi^2+4}.}
$$

Численно

$$
F_{Q,*}\approx2.307203513,
\qquad
g_*\approx0.576800878.
$$

Это первый exact local information-response scale текущей emergence-ветки.

---

# 12. Information resistance metric

Для positive local conductance определяем edge resistance length

$$
\boxed{
\ell_e=\ell_*\frac{g_*}{g_e}.
}
$$

А network distance

$$
\boxed{
d(i,j)=\min_{\gamma:i\to j}\sum_{e\in\gamma}\ell_e.}
$$

На chain path unique, поэтому

$$
\boxed{
d(i,j)=\sum_{e=i}^{j-1}\ell_e.}
$$

В homogeneous phase

$$
\boxed{
d_m(i,j)=|i-j|\ell(m).}
$$

То есть additivity точная и не зависит от того, algebraic или exponential long-distance correlations имеет bulk state.

В controlled family $m=0,0.2,0.5,1,2$ relative-twist QFI остаётся positive, а normalized resistance length растёт примерно как

| $m$ | $F_Q$ | $\ell_Q/\ell_*$ |
|---:|---:|---:|
| 0 | $\approx2.31$ | $\approx1.00$ |
| 0.2 | $\approx2.097$ | $\approx1.10$ |
| 0.5 | $\approx1.623$ | $\approx1.42$ |
| 1.0 | $\approx0.999$ | $\approx2.31$ |
| 2.0 | $\approx0.421$ | $\approx5.48$ |

Orientation-mass deformation therefore weakens local information conductance and stretches local emergent resistance length, while the metric composition law remains unchanged.

Файлы:

- `BQG_LOCAL_INFORMATION_RESISTANCE_METRIC.md`
- `scripts/bqg_local_information_resistance_gate.py`

---

# 13. Positive theorem: phase-robust additive metric class exists

Для любого graph с positive edge conductances

$$
g_e>0
$$

локальные resistance lengths

$$
\ell_e\propto g_e^{-1}
$$

и shortest-path construction автоматически дают metric с triangle inequality:

$$
\boxed{d(i,k)\le d(i,j)+d(j,k).}
$$

На tree/chain вдоль geodesic path additivity exact.

Следовательно текущая reduced BQG branch впервые имеет конструкцию

$$
\boxed{
\rho_{ij}
\to
\text{local information response}
\to
\text{edge conductance}
\to
\text{additive network metric}
}
$$

которая применяет **один и тот же rule** к critical и gapped фазам.

Это первый positive phase-robust metric result новой ветки.

---

# 14. Новый uniqueness no-go

Однако full local state $\rho_{ij}$ сама по себе всё ещё не выбирает единственную metric functional.

Для одного и того же edge естественны, например,

$$
I(\rho_{ij}),
$$

$$
D_B^2(\rho_{ij},\rho_i\otimes\rho_j),
$$

и

$$
\frac14F_Q(\rho_{ij},K_{ij}).
$$

Все они positive local information measures, но дают разные phase-dependent local scales.

Поэтому

$$
\boxed{
\rho_{ij}\ \text{alone}
\not\Rightarrow
\text{unique spatial metric functional}.
}
$$

Нужен ещё один principle: **какая именно физическая deformation определяет длину?**

Сейчас relative-twist QFI предпочтителен, потому что он связан с response к конкретной relational deformation, но generator $K_{ij}$ пока должен быть выведен из fundamental BQG dynamics.

---

# 15. Каноническая цепочка новой ветки на сегодня

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
\text{XX/free fermions}
\to
\text{critical/gapped correlation laws}
\to
\text{scalar-distance no-go}
\to
\text{local QFI conductance}
\to
\text{additive resistance metric}.
}
$$

Самые сильные current statements:

1. $Q=i[D_{12},D_{23}]$;
2. $Q_{\rm phys}=(\sqrt3/4)\sigma_y$;
3. local isotropy iff oriented volume is sharp;
4. $\mathcal A_p=4(\Delta Q)^2$;
5. two-node matching selects Bell-type intertwiner entanglement;
6. current many-node chain maps exactly to free fermions;
7. critical $I_0(r)\sim\kappa/r$;
8. staggered oriented-volume deformation opens gap $2|m|$;
9. gapped $I_m(r)\sim Br^{-1}e^{-2r/\xi}$;
10. no universal global scalar distance $d=f(I_{ij})$ works in both phases;
11. local relative-twist QFI has exact critical scale $32/(\pi^2+4)$;
12. resistance composition produces an exact additive path metric in both phases;
13. static local $\rho_{ij}$ alone does not uniquely select the metric functional.

---

# 16. Что пока НЕ доказано

Мы не утверждаем, что:

- $H_{\rm glue}$ уже выведен из fundamental graph-changing BQG constraint;
- staggered-volume deformation является fundamental vacuum term;
- relative-twist QFI является unique fundamental metric source;
- $K_{ij}$ уже выведен из physical BQG projector/history dynamics;
- reference length $\ell_*$ выведена из binary microphysics;
- continuum space уже доказано трёхмерно;
- Einstein equations уже получены;
- Lorentzian causal cone уже выведен;
- $G$, $c$, $\hbar$ уже выведены из first principles.

Ключевой caveat:

$$
\boxed{
\text{exact mathematics of the reduced model}
\neq
\text{proof that the reduced model is fundamental dynamics}.
}
$$

---

# 17. Новый настоящий фронтир: weighted Laplacian and spectral dimension

Теперь перестаём искать ещё одну distance formula.

Следующий exact/calibration gate:

$$
\boxed{
(L_g)_{ij}
=\delta_{ij}\sum_k g_{ik}-g_{ij},
}
$$

где

$$
g_{ij}=\frac14F_Q(\rho_{ij},K_{ij})
$$

для physical edges.

Из weighted graph Laplacian строим heat kernel

$$
K(\tau)=e^{-\tau L_g},
$$

return probability

$$
\boxed{
P(\tau)=\frac1N\operatorname{Tr}e^{-\tau L_g},
}
$$

и spectral dimension

$$
\boxed{
d_s(\tau)=-2\frac{d\ln P(\tau)}{d\ln\tau}.}
$$

Первый calibration test обязан дать

$$
\boxed{d_s\to1}
$$

на large homogeneous chain/ring в diffusion window.

После этого тот же local QFI rule, **без retuning**, должен быть применён к:

1. ring;
2. square lattice;
3. branching/tree graph;
4. irregular glued graph;
5. затем к graph states, которые реально выдаёт BQG constraint/history dynamics.

Если weighted diffusion geometry сохраняет правильную topological/spectral dimension при смене quantum phase, это будет первый настоящий network-level emergent-dimension result.

---

# 18. Канонический принцип

> **Сначала уменьшить задачу симметрией. Затем распознать точную математическую структуру. Потом решить её аналитически. Отрицательные результаты фиксировать так же строго, как положительные. И только если exact путь закрыт — считать численно.**

Репозиторий: `Shtenco/binary_quantum_theory`
