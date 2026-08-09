# Статус теории — текущий frontier

## 1. Что теперь можно считать устойчивым ядром

### Дискретная/спектральная кинематика

- $L=B^\dagger B\ge0$;
- точный решёточный символ
  \[
  \widehat L(k)=4\sum_i\sin^2(k_i/2);
  \]
- симплектическая свободная динамика;
- условная абсолютная сходимость регуляризованных спектральных сумм.

### Fixed-Regge -> continuum GR cross-check

Без ручной TT-проекции полный metric Hessian приближается к Fierz--Pauli, generic quadratic/cubic Regge action приближается к прямому Einstein--Hilbert functional, а cubic Ward defect стремится к нулю.  На разных observables ведущие finite-size corrections согласуются с примерно quadratic law

\[
\epsilon\sim O(L^{-2}).
\]

Это перестало быть только post-hoc observation.  Закон

\[
e(L)=C/L^2+D/L^4
\]

был заморожен по `L=5..8` **до** вычисления `L=9,10`.  Четыре разных defect-а на обоих held-out размерах дали `8/8` PASS; все относительные ошибки preregistered prediction оказались меньше `0.5%`.

Подробности:

- `GRAVITY_BRIDGE_SCALING.md`;
- `REGGE_EH_CUBIC_BRIDGE.md`;
- `CUBIC_WARD_SCALING.md`;
- `HELDOUT_L9_L10_PREREGISTRATION.md`;
- `HELDOUT_L9_L10_RESULTS.md`.

Это сильный downstream universality cross-check, но он всё ещё стартует с заданного 4D Regge scaffold.

## 2. Старый microscopic carrier пересмотрен

### Euclidean face-qubit route

`face qubit -> B^i -> simplicity -> Urbantke metric -> compatible connection -> Einstein curvature` остаётся полезным **Euclidean reconstruction/control route**.  Он показал, что metric reconstruction, Plebanski simplicity и Einstein curvature являются независимыми falsification gates.

Но один unitary `SU(2)` qubit нельзя считать точным finite carrier полной Lorentzian self-dual `SL(2,C)` connection.  Поэтому основная microscopic линия теперь canonical.

### Canonical Lorentzian-safe line

Текущая структура:

\[
\boxed{
\text{finite }SU(2)\text{ quantum links}
+\text{Gauss intertwiners}
+\text{causal/Fock dynamics}.
}
\]

Lorentzian physics должна возникнуть через real Ashtekar--Barbero constraints, extrinsic curvature, DeWitt signature и $z\to1$, а не объявляться из самого внутреннего `SU(2)` label.

## 3. Binary -> three spatial dimensions: structural theorem candidate

Если local carrier имеет Hilbert dimension `q`, geometric local observables образуют полный traceless Hermitian adjoint algebra, coarse observables аддитивны как fluxes и Gauss closure интерпретирует их как area normals, то

\[
D_{spatial}=q^2-1.
\]

Для binary carrier

\[
q=2\quad\Rightarrow\quad D_{spatial}=3.
\]

При одной независимой causal direction и $z\to1$:

\[
d_{spacetime}=1+D_{spatial}=4.
\]

Это conditional theorem внутри заявленных аксиом, а не замена dynamical tests.  Frozen ensemble всё равно обязан независимо дать

\[
d_s^{slice}\to3,
\qquad
D_{link}\to3,
\qquad
z\to1.
\]

Подробности: `BINARY_ADJOINT_DIMENSION_THEOREM.md`.

## 4. Exact quantum tetrahedron

Четыре spin-$1/2$ face carriers имеют

\[
(1/2)^{\otimes4}=2(0)\oplus3(1)\oplus1(2),
\]

поэтому Gauss-singlet sector двумерен.  Его logical Pauli operators являются настоящими tetrahedral geometry observables:

\[
J_1\cdot J_2=-\frac14I-\frac12Z_L,
\]

\[
J_1\cdot J_3=-\frac14I+\frac14Z_L-\frac{\sqrt3}{4}X_L,
\]

\[
J_1\cdot(J_2\times J_3)=\frac{\sqrt3}{4}Y_L.
\]

Flux closure reconstructs tetrahedron to machine precision.  Equal-area shared faces can nevertheless have different intrinsic shape, поэтому требуется отдельный

\[
\Delta_{shape}\to0.
\]

Подробности: `SPATIAL_QUBIT_GEOMETRY_BRIDGE.md`.

## 5. Collective continuum mechanism

Microscopic geometry-qubit **не должен** оставаться qubit на больших масштабах.

Для `N` aligned spin-$1/2$ carriers на coarse face:

\[
j=N/2,
\qquad
\frac{\Delta J_\perp}{|\langle J\rangle|}=N^{-1/2}.
\]

Если $N_{face}\sim b^2$:

\[
\boxed{\Delta n\sim b^{-1}}.
\]

Для четырёх equal coarse spins

\[
\dim\operatorname{Inv}(V_j^{\otimes4})=2j+1=N+1,
\]

поэтому shape space становится semiclassical.  Exact flux scaling даёт

\[
\boxed{A\sim b^2,\qquad V\sim b^3}.
\]

Spin-coherent second moments одновременно дают systematic operator corrections

\[
\boxed{\delta S/S\sim1/j\sim b^{-2}}.
\]

Это связывает microscopic collective mechanism с independently observed `O(a^2)` Regge/EH/Ward corrections.  Large-$j$ spin-foam calculations также имеют next-to-leading `O(1/j)` quantum corrections, что делает этот exponent отдельной universality hypothesis для проверки, а не только численным совпадением.

## 6. SO(5) quantum links: один carrier отвергнут, другой выжил

### Spinor $\mathbf4$ — volumetric no-go

Четырёхstate spinor link реализует exact `SU(2)_L x SU(2)_R` на двух qubits, но имеет one-rishon counting.  На любом closed 4-valent graph `E=2V`, поэтому средняя endpoint occupancy равна 2, тогда как nondegenerate tetrahedral volume требует `k=4` на каждом node.

Следовательно

\[
\boxed{\mathbf4\text{ не может быть everywhere-volumetric closed carrier}.}
\]

### Vector $\mathbf5$ — текущий минимальный candidate

Под `SU(2)_L\times SU(2)_R`

\[
\boxed{\mathbf5=(\mathbf2,\mathbf2)\oplus(\mathbf1,\mathbf1)}.
\]

Четыре states являются active geometric link с spin-$1/2$ на обоих концах; пятое — gauge singlet `off` state.  Quantum transporter переключает эти sectors точно.

На минимальном four-link plaquette после Gauss reduction:

\[
\dim\mathcal H_{phys}=2,
\qquad
W_p=16X,
\]

то есть Wilson loop literally creates/annihilates a closed active geometric loop.

Подробности:

- `scripts/su2_quantum_link_vector5_gate.py`;
- `scripts/vector5_geometrogenesis_gate.py`.

## 7. Exact closed K5 geometry laboratory

`K5` — dual graph границы одного 4-simplex: 5 tetrahedral nodes, 10 shared faces/links.

Для vector-$\mathbf5$ links:

\[
5^{10}=9\,765\,625
\]

raw states сжимаются exact Gauss law до

\[
\boxed{\dim\mathcal H_G=140}.
\]

Полностью active five-tetrahedron sector:

\[
\boxed{\dim=2^5=32}.
\]

Четыре triangle-loop flips — минимальная graph distance от empty geometry до fully active `K5`.

## 8. No-space -> 4-simplex state

Пусть

\[
W=\sum_{10\ triangles}W_\triangle.
\]

Из vacuum:

\[
|\Psi_4\rangle=P_{full}W^4|0\rangle.
\]

Независимо contracted five-intertwiner 4-simplex/15j boundary state обозначим $|V_5\rangle$.  Получено

\[
\boxed{
|\langle\widehat V_5|\widehat\Psi_4\rangle|^2
=\frac{90}{91}
=98.9011\%.
}
\]

Оставшийся `1/91` нельзя удалить:

- reweighting 10 minimal loop sets;
- all 240 ordered four-loop histories;
- longer pure-Wilson Krylov histories до `W^30`;
- добавлением scalar volume.

Но один exact tensorial shape observable удаляет obstruction полностью:

\[
\|V_5-P_{\mathcal K(W,Z_{shape})}V_5\|^2<5\times10^{-29}.
\]

Shortest exact projected word depth равна 7; в этой глубине требуется как минимум **две** shape insertions.  Это сильный finite discriminator

\[
\text{pure curvature / loop gas}
\neq
\text{tensorial gravity geometry}.
\]

Подробности: `K5_QUANTUM_GEOMETRY_BRIDGE.md`.

## 9. SU(2) constraint kernel: сильный результат, но BF, не ещё GR

Построено семейство local graph-changing kernels

\[
T(v;a,b|c)
=\operatorname{Tr}\left[
(U_{vabv}-U_{vbav})
U_{vc}[U_{cv},P_{k_v=4}]
\right].
\]

На 32D fully active sector:

- 12 constraints одного node: rank 21, kernel 11;
- constraints двух nodes: rank 29, kernel 3;
- constraints трёх nodes: rank 31, kernel 1.

Единственный common-null state совпадает с independently constructed $V_5$ с unit fidelity.  Все remaining local constraints также annihilate $V_5$ до примерно `1e-13`.

Однако на fixed $j=1/2$ fully-active sector volume projector не различает intertwiner shape; соответствующий kernel survives even if the explicit volume commutator is simplified.  Кроме того, 15j recurrence/Hamiltonian constraints известны для topological BF theory.

Поэтому правильная классификация:

\[
\boxed{
\text{finite QLM} \to \text{exact SU(2)/BF-like physical constraint sector}
}
\]

— **не** ещё доказательство Lorentzian quantum GR.

Подробности: `scripts/k5_thiemann_constraint_gate.py`.

## 10. Первый explicit BF -> simplicity control

Чтобы отделить BF от gravity, добавлен малый Euclidean EPRL-type test при

\[
\gamma=1/3,
\qquad
j=3/2,
\qquad
j^+=1,
\qquad
j^-=1/2.
\]

Bare SU(2) `j=3/2` 15j и raw simplicity-projected vertex имеют

\[
\boxed{\mathcal F\simeq0.944224},
\]

то есть simplicity существенно меняет state уже на small spin.

Нормализация локального fusion map также существенно влияет на small-spin vertex: raw и locally isometrized variants имеют fidelity около `0.9624`.  Следовательно нельзя выбирать normalization post-hoc; gravity claim должен опираться на large-spin/regulator universality.

Подробности: `scripts/eprl_simplicity_vertex_gate.py`.

## 11. Главный незакрытый переход теперь

Downstream Regge -> GR больше не главный bottleneck.  Pure SU(2)/BF finite geometry тоже уже вычисляется exact.

Главный frontier:

\[
\boxed{
\text{vector-QLM / collective spin / Fock dynamics}
\dashrightarrow
\text{Lorentzian simplicity + first-class GR constraint phase}.
}
\]

Один frozen microscopic model обязан без retuning дать **одно общее scaling window**:

\[
A\sim b^2,
\qquad
V\sim b^3,
\qquad
\Delta n\sim b^{-1},
\qquad
\Delta_{shape}\to0,
\]

\[
d_s^{slice}\to3,
\qquad
z\to1,
\qquad
d_s^{history}\to4,
\]

\[
\frac{b_{DW}}{a_{DW}}\to-1,
\qquad
\operatorname{spec}G_{kin}\to c(-2,1,1,1,1,1),
\]

и восстановить rank-seven first-class canonical constraint structure

\[
3G+3D+1H.
\]

Тогда Dirac counting автоматически оставляет

\[
18-2\times7=4
\]

physical phase-space dimensions, то есть **две** configuration degrees of freedom.  TT/massless spectrum становится независимым подтверждением spin-2, а не местом, где число 2 вставляется руками.

## 12. Что остаётся OPEN

1. frozen Lorentzian operator ordering / measure;
2. dynamical simplicity on collective large-spin states;
3. HDA / first-class constraint closure;
4. DeWitt Lorentzian kinetic signature;
5. common 3+1 critical continuum window and regulator/Immirzi universality;
6. chiral anomaly-free matter;
7. scale-setting physical observable;
8. preregistered prediction against external data and independent replication.

Пока эти gates не закрыты, проект является **вычислимой candidate architecture with strong finite bridges**, а не доказанной теорией природы.
