# Статус теории — актуальный frontier

## Что уже действительно получено

1. Точное дискретное спектральное ядро: $B$, $L=B^\dagger B\ge0$, синусовый символ и massless lattice pole.
2. Симплектическая свободная динамика и два TT-компонента в линейном reduced/Regge sector.
3. Off-shell local-frame invariance конечного SU(2) plaquette; после PR17 проверка расширена до двух склеенных plaquettes с общей connection/frames.
4. Для finite geometric cell проверены closure, diagonal simplicity, cross-simplicity и nondegeneracy; общий SO(4) frame rotation сохраняет условия, nonsimple Pluecker control отвергается.
5. Dimension-blind control убивает минимальный binary reconvergent diamond как механизм 4D: он стремится к approximately two-dimensional geometry.
6. Conditional qubit-isotropy chain выделяет spatial $D=3$: только для qubit полная adjoint frame freedom $PSU(2)$ совпадает с полным rotation group $SO(3)$; для $q>2$ adjoint $PSU(q)$ не покрывает $SO(q^2-1)$.
7. Four spin-$1/2$ face carriers имеют двухмерный SU(2) singlet/intertwiner sector; logical Pauli operators являются exact tetrahedral shape/oriented-volume observables.
8. Absolute volume theorem: любой two-dimensional four-valent intertwiner sector имеет $V\propto I$; $j=1$ — первый equal-spin sector, где volume различает zero/nonzero geometry; несколько ненулевых volume scales требуют intertwiner dimension $\ge4$.
9. Finite Peter--Weyl link
   $$\mathcal H_{link}^{J_{max}}=\bigoplus_{j\le J_{max}}V_j^L\otimes V_j^R$$
   сохраняет exact left/right SU(2) covariance. Holonomy word с $r$ hits на одном link cutoff-exact при $j_{in}+r/2\le J_{max}$; vacuum Wilson staircase проверяет это через $J_{max}=5/2$.
10. На $K_5$ vector-link truncation $5^{10}$ сжимается Gauss law до 140 states; fully-active five-tetrahedron sector имеет dimension 32. Четыре loop moves — минимальная distance от empty geometry до fully-active $K_5$.
11. Exact five-tetrahedron $j=1/2$ vertex tensor и link-level geometrogenesis почти совпадают: $P_{full}W^4|0\rangle$ имеет fidelity squared $90/91$ к independently contracted vertex. Pure Wilson/scalar volume не закрывают missing $1/91$, tensorial shape — закрывает.
12. Orientation-covariant finite normal constraints имеют robust physical-state kernel: на 32D sector constraints трёх nodes уже дают rank 31 и unique null state, равный independently constructed $V_5$.
13. Но тот же $J_{max}=1/2$ model **не проходит quantum HDA**. После правильных geometric orientation signs все 10 HH pairs permutation-covariant, но graph-changing norm fraction squared равен
   $$\boxed{37/69}.$$
   Graph-preserving $Q_{ij}=-iP[H_i,H_j]P$ span содержит projected $SO(5)$-like skeleton, однако higher-body Lie anomaly при $j=1/2$ остаётся огромной.
14. Tangential/normal finite Dirac hierarchy: common kernel всех десяти $Q_{ij}$ двумерен,
   $$\operatorname{span}\{V_5,Y^{\otimes5}V_5\},$$
   а normal constraints выбирают только $V_5$.
15. Для regulator-safe HH из all-$j=1/2$ $K_5$ exact per-link wall требует $J_{max}=5/2$. Reachable Gauss basis имеет не $91^{10}$, а только 4193 admissible spin assignments / 24364 spin-network states. Среди всех local spin quartets встречается лишь 163 distinct blocks, intertwiner multiplicity $\le3$.
16. Plebański/Urbantke route проверен отдельно: simple nondegenerate $B^i$ reconstructs metric; compatible connection from $D_AB=0$ и anti-self-dual curvature block отличают Einstein $S^4$ от smooth non-Einstein control.
17. Simplicity projector
   $$P_{simp}=F(F^\dagger F)^{-1}F^\dagger$$
   normalization-independent. EPRL coherent geometric rays сохраняются, а preregistered single-power extrapolation raw-vs-isometrized ambiguity на $j=15/2$ честно **FAIL** — rejected was the premature power law, not coherent geometry preservation.
18. Fixed 4D Regge scaffold independently approaches Fierz--Pauli / Einstein--Hilbert / cubic Ward. A law frozen on $L=5..8$ predicted four defects at held-out $L=9,10$: **8/8 preregistered checks passed**, all relative defect errors below 0.5%.
19. Flux-to-metric pullback of the DeWitt supermetric has inertia
   $$\boxed{(5+,1-,3\,0)}$$
   on 100/100 random nondegenerate tetrahedra; the three zeros are Gauss/frame rotations and the unique negative mode is common radial flux scaling.
20. Independent classical HDA controls pass in two formulations: spectral ADM grid and finite 4-simplex deformation algebra, both to approximately $10^{-10}$ in safe windows.
21. Within the local two-derivative ADM ansatz, generic HH closure fixes
   $$\boxed{c_{DW}=1/2,\qquad AB=1}$$
   while leaving Newton scale and $\Lambda$ free. Therefore the same closure also gives the leading tensor cone $c_T^2=AB=1$ and, with first-class Dirac counting in $D=3$, two physical configuration modes.
22. Real Ashtekar--Barbero classical kinetic sector obeys exact cancellation
   $$H_E^{kin}+H_L^{corr}=H_{DW}$$
   for any real $\beta$; the finite quantum theory must reproduce this only after appropriate Gauss/diffeomorphism projection.

## Что означают новые PR16/17

Последние PR добавили полезные **tier-1 finite precursors**: glued frame/connection covariance и четыре geometric-cell invariants. Они усиливают local kinematics, но не закрывают continuum/HDA gates. Важно: PR17 временно перезаписал этот status и machine ledger старой укороченной версией; ledger теперь восстановлен без отката новых W1/SIMP1 tests.

## Главный незакрытый переход

Сейчас центральный killer-gate один:

$$
\boxed{
J_{max}=5/2\ \text{regulator-safe Peter--Weyl }K_5
\longrightarrow
[H_k,H_l]\simeq i\,D_{kl}/(3V)
}
$$

в exact Gauss/recoupling basis, без coefficient tuning.

Для этого уже известен конечный размер задачи:

- 4193 admissible global spin assignments after two local Hamiltonians;
- 24364 exact spin-network states;
- only 163 distinct local four-spin blocks;
- local intertwiner dimension never exceeds 3 in the reachable HH space.

Следовательно dense link Hilbert не нужен: следующий verifier должен cache local CG/6j/volume blocks and apply $H_kH_l-H_lH_k$ directly in the reachable spin-network basis.

## Joint pass condition

Теория продвигается к GR только если **в одном scaling window** одновременно:

$$
\Delta_{HH}^{Q}\to0,
\qquad
\Delta_\beta\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad
z\to1,
$$

а затем microscopic first-class system даёт seven constraints $(3G+3D+1H)$ and therefore exactly two physical configuration degrees of freedom without manual TT projection.

Открыты также frozen microscopic measure/rules, dynamical emergence of the common continuum window, matter/chirality/anomalies, physical scale setting and independent empirical replication.
