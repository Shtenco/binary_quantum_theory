# Бинарная квантовая гравитация (BQG)
## Единый канонический README: от бинарной микроструктуры к квантовой геометрии, физическому projector, emergent metric и наблюдаемой физике

**Каноническая версия: 10 октября 2026 года**

---

# 0. Зачем этот README переписан заново

5 октября 2026 года README был фактически обнулён и заменён новой emergence-веткой. Эта ветка дала важные новые результаты — oriented-volume theorem, entanglement gluing, XX/free-fermion mapping, mutual-information no-go, QFI metric, spectral dimension и topology-free falsification — но при этом из главного README исчезла большая уже построенная фундаментальная часть проекта:

- q=2 binary microstructure;
- exact dimension-three fixed point;
- Walsh tetrahedral carrier;
- global PL gluing;
- Peter–Weyl graph-changing representation;
- Plebanski/Urbantke/Einstein bridges;
- Regge/EH controls;
- HDA / DeWitt / graph-changing constraints;
- finite master-constraint programme;
- relational-history projector;
- generating functional $Z[J]\to W[J]$;
- TT/graviton reference sector;
- six-dimensional quartic TT observable space;
- cosmology/scalar obstructions;
- 2T and black-hole frontiers;
- depth-4/depth-6 kernel programme.

Этот README восстанавливает **единый канон**.

Новая emergence/info-geometry ветка теперь является **дополнительным слоем внутри старой BQG**, а не заменой всей теории.

Главное правило проекта остаётся:

$$
\boxed{\text{красивая история никогда не сильнее доказательства}.}
$$

И второе правило:

$$
\boxed{\text{симметрия сначала, вычисления потом}.}
$$

---

# 1. Словарь статусов

Во всём README используются только пять основных статусов.

| Статус | Значение |
|---|---|
| **PROVED** | точный theorem / identity в явно заявленной области |
| **FINITE** | воспроизводимый finite numerical/algebraic control, но не continuum theorem |
| **CANDIDATE** | физически мотивированная, но ещё не выведенная фундаментально конструкция |
| **NO-GO** | строго найденный запрет / отрицательный результат в заявленном классе |
| **OPEN** | необходимый физический мост пока не закрыт |

Дополнительные слова вроде `conditional`, `surrogate`, `positive control` всегда относятся к одному из этих пяти классов и не повышают статус.

Критические различия:

$$
\boxed{\text{finite theorem}\neq\text{continuum theorem}}
$$

$$
\boxed{\text{constraint object}\neq\text{physical propagator}}
$$

$$
\boxed{\text{algebraic observable map}\neq\text{prediction}}
$$

$$
\boxed{\text{internal consistency}\neq\text{experimental confirmation}}.
$$

---

# 2. Главная объединённая карта BQG

Текущая теория состоит из двух уже развитых слоёв, которые теперь объединены.

## 2.1. Фундаментальная structural ветка

$$
\boxed{
\text{binary microstructure}
\to q=2
\to \text{Walsh tetrahedron}
\to d_*=3
\to SU(2)/\text{Peter--Weyl quantum geometry}
\to \text{global PL gluing}
\to \text{metric / Urbantke / Regge}
\to \text{graph-changing constraints}
\to \text{HDA / DeWitt}
\to M
\to P_{\rm phys}
\to \text{relational history}
}
$$

## 2.2. Новая emergence / information-geometry ветка

$$
\boxed{
\text{physical intertwiner node}
\to \text{noncommuting pair geometry}
\to \text{oriented volume}
\to \text{entangled gluing}
\to \text{network correlations}
\to \text{local QFI conductance}
\to L_g
\to d_s
}
$$

## 2.3. Физикализация

Обе ветки должны встретиться в одной цепочке:

$$
\boxed{
P_{\rm phys}
\to \text{physical relational histories}
\to Z[J_g]
\to W[J_g]
\to \Gamma[g]
\to K_{TT}(\omega,\mathbf k)
\to (c_1,\ldots,c_6)_{\rm IR}
\to \text{observables}
\to \text{experiment}.
}
$$

Это и есть единая современная BQG.

---

# 3. Binary microstructure: почему начинается с q=2

Два бинарных признака дают четыре состояния

$$
\mathbb Z_2^2.
$$

Три нетривиальных Walsh-character задают четыре нормированных вектора $n_a$, для которых точно:

$$
\boxed{\sum_{a=1}^4 n_a=0,}
$$

$$
\boxed{n_a\cdot n_a=1,}
$$

$$
\boxed{n_a\cdot n_b=-\frac13\quad(a\neq b).}
$$

Это exact normals правильного тетраэдра.

**Статус: PROVED.**

Ключевые файлы:

- `MICRO_WALSH_QGEOM_BRIDGE.md`
- `scripts/micro_walsh_qgeom_gate.py`
- `BINARY_TO_GEOMETRY_GATE.md`
- `BIT_TO_SPACETIME_CENTRAL_EQUATION.md`

---

# 4. Exact dimension-three fixed point

Для frozen q=2 refinement count:

$$
\boxed{N_g=\frac{4\cdot 8^g+10}{7}.}
$$

Finite-step dimension:

$$
\boxed{
d_g=\log_2\frac{N_g}{N_{g-1}}
=3+\log_2\left(1-\frac{35}{16\cdot8^{g-1}+40}\right).
}
$$

Для каждого finite $g$:

$$
d_g<3,
$$

последовательность растёт монотонно, и

$$
\boxed{\lim_{g\to\infty}d_g=3.}
$$

Это analytical fixed-point statement внутри заявленной refinement rule.

**Статус: PROVED для frozen q=2 refinement.**

Файлы:

- `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md`
- `scripts/q2_dimension3_fixed_point_gate.py`

Дополнительные finite diagnostics старой ветки:

```text
d_H          ≈ 2.999229782
d_s(slice)   ≈ 3.004393867
z            ≈ 0.998281156
d_s(history) ≈ 4.004393867
```

**Статус этих diagnostics: FINITE, не blind prediction.**

---

# 5. Local SU(2) quantum geometry

Четыре spin-$1/2$ face carriers имеют Gauss-invariant singlet sector

$$
\mathcal H_{\rm phys}^{(4)}
=\mathrm{Inv}_{SU(2)}[(1/2)^{\otimes4}],
\qquad \dim=2.
$$

В logical basis $|s\rangle,|t\rangle$ intrinsic shape живёт в $X/Z$, orientation — в $Y$.

Logical metric Jacobian имеет

$$
\boxed{\operatorname{rank}J_{\rm metric}=2,}
$$

а $X/Z$ tangents:

- trace-free;
- orthogonal;
- equal DeWitt norm.

**Статус: PROVED для local carrier.**

Файлы:

- `LOGICAL_SHAPE_METRIC_JACOBIAN.md`
- `scripts/logical_shape_metric_jacobian_gate.py`

---

# 6. Exact oriented-volume theorem новой ветки

Определим

$$
Q_{123}=\epsilon_{abc}J_1^aJ_2^bJ_3^c.
$$

Exact operator identity:

$$
\boxed{
Q_{123}
=i[\mathbf J_1\cdot\mathbf J_2,\mathbf J_2\cdot\mathbf J_3].
}
$$

В physical doublet:

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

Для pair-spectrum anisotropy

$$
\mathcal A_p=\sum_{i<j}\left(p_{ij}-\frac12\right)^2
$$

получено exact identity

$$
\boxed{\mathcal A_p=4(\Delta Q_{123})^2.}
$$

Поэтому

$$
\boxed{
\text{pair-spectrum isotropy}
\Longleftrightarrow
\text{sharp oriented volume}.
}
$$

**Статус: PROVED.**

Файлы:

- `BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md`
- `scripts/bqg_minimal_entanglement_volume_gate.py`

---

# 7. Graph-link representation и no-link state

Четырёх активных q=2 states недостаточно для полного graph-changing endpoint carrier.

Добавление no-link / $j=0$ state даёт exact five-component structure

$$
\boxed{(2,2)+(1,1)}
$$

в зарегистрированной $SU(2)_L\times SU(2)_R$ конструкции.

Transporter identity:

$$
\boxed{P_gU_aP_0U_bP_g=|a\rangle\langle b|.}
$$

То есть active-state transition факторизуется через graph-changing excursion в no-link sector.

**Статус: PROVED в finite representation carrier.**

Файлы:

- `Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md`
- `scripts/q2_graphlink_peter_weyl_gate.py`
- `scripts/su2_quantum_link_vector5_gate.py`

---

# 8. Peter–Weyl growth

При явно заданном fully symmetric endpoint blocking occupancy $n$ даёт

$$
j=\frac n2,
$$

$$
\dim(j,j)=(2j+1)^2=(n+1)^2.
$$

Поэтому $n=0,1,\ldots,N$ воспроизводит diagonal Peter–Weyl tower

$$
j=0,\frac12,1,\ldots,\frac N2.
$$

**Статус: CANDIDATE/conditional exact statement**, потому что blocking rule пока не выведена уникально из full microscopic dynamics.

---

# 9. Global PL geometry

Selected finite completion использует boundary 4D cross-polytope:

- 16 tetrahedral cells;
- 32 shared triangular faces;
- dual graph $Q_4$.

На shared faces:

- один и тот же q=2 carrier согласуется на двух incidences;
- orientation parity чередуется;
- outward Walsh flux сокращается pairwise.

**Статус: FINITE exact/tested completion для выбранной PL geometry.**

Файлы:

- `GLOBAL_MANIFOLD_Q2_COMPLETION.md`
- `bcqg_global_manifold_gate.py`
- `scripts/q2_global_face_qubit_gluing_gate.py`

Это не theorem для arbitrary manifold.

---

# 10. Qubit → B → Urbantke → Einstein

Отдельная structural chain:

$$
\boxed{
\text{face qubits}
\to B
\to \text{simplicity}
\to g_{\mu\nu}^{\rm Urbantke}
\to \text{compatible connection}
\to \text{curvature}.
}
$$

Positive control восстанавливает declared Einstein geometry. Independent non-Einstein control отвергается после metric stage.

**Статус: FINITE.**

Файлы:

- `QUBIT_TO_EINSTEIN_END_TO_END.md`
- `PLEBANSKI_URBANTKE_BRIDGE.md`
- `PLEBANSKI_CONNECTION_EINSTEIN_GATE.md`
- `scripts/qubit_to_einstein_end_to_end.py`

---

# 11. Regge / Einstein-Hilbert controls

Finite simplicial bridge проверяет continuum tensor scaling.

Held-out continuation:

$$
Z_L=\frac18+\frac C{L^2}+\frac D{L^4}
$$

fitted only on $L=3,4,5$.

Prediction:

$$
Z_6^{\rm pred}=0.11876923193907167.
$$

Independent value:

$$
Z_6^{\rm obs}=0.11876075461190198.
$$

Relative error:

$$
\boxed{\approx0.00714\%.}
$$

**Статус: FINITE held-out internal control.**

Файлы:

- `REGGE_EH_CUBIC_BRIDGE.md`
- `TT_REGGE_ZT_L6_RESULT.md`
- `scripts/regge_eh_cubic_bridge.py`
- `scripts/tt_regge_zt_l6_gate.py`

---

# 12. DeWitt / ADM / HDA structure

В canonical GR target algebra:

$$
\{H[N],H[M]\}
\to
D[q^{ab}(N\partial_bM-M\partial_bN)].
$$

BQG содержит finite HDA controls с scaling hierarchy:

$$
\text{route}\sim\epsilon,
\qquad
\text{cross}\sim\epsilon,
\qquad
\text{pure geometry}\sim\epsilon^2.
$$

Frozen measured exponents:

```text
route exponent         = 0.9999571195
cross exponent         = 1.0024037289
pure-geometry exponent = 2.0061524985
joint exponent         = 1.0064429344
```

Joint defect при $\epsilon=1/64$:

$$
0.02522380790.
$$

Minimum registered graph-change fraction:

$$
\boxed{0.4440331635.}
$$

**Статус: FINITE HDA evidence, не arbitrary-graph continuum theorem.**

Файлы:

- `THREE_NODE_GRAPH_HDA_RESULT.md`
- `PETER_WEYL_TWO_NODE_EUCLIDEAN_RESULT.md`
- `JOINT_REGULATOR_LIMIT.md`
- `scripts/peter_weyl_three_node_graph_hda_gate.py`

DeWitt radial/conformal direction имеет

$$
\boxed{Q_{\rm DW}=-6.}
$$

**Статус: PROVED в заявленном local canonical ansatz.**

---

# 13. Finite master constraint

Главный positive operator:

$$
\boxed{
M_G=C_A^\dagger G^{AB}C_B\ge0.
}
$$

Для positive-definite $G$:

$$
\boxed{
\ker M_G=\bigcap_A\ker C_A.
}
$$

При isolated zero sector:

$$
\boxed{P_{\rm phys}^{(\epsilon)}=\mathbf1_{\{0\}}(M_G).}
$$

И

$$
\boxed{
P_{\rm phys}^{(\epsilon)}
=\lim_{T\to\infty}e^{-TM_G}
}
$$

в finite regulated setting.

**Статус: PROVED finite theorem.**

Файлы:

- `MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md`
- `scripts/master_constraint_physical_projector_gate.py`

Критическая граница:

$$
\boxed{
P_{\rm phys}^{\rm finite}\neq P_{\rm phys}^{\rm continuum}\ \text{автоматически}.
}
$$

---

# 14. Depth-4 finite rehearsal

Depth-4 Hilbert dimension:

$$
\boxed{217953.}
$$

Все non-vacuum symmetry sectors в заявленном analysis были injective; trivial $[5]$ sector оставляет только vacuum line.

**Статус: FINITE closed in tested scope.**

---

# 15. Depth-6 programme: актуальный статус после 1 октября

Corrected finite K5 shell:

$$
\boxed{264962}
$$

Gauss-admissible spin assignments.

Full Hilbert dimension:

$$
\boxed{3111637.}
$$

S5 spin orbits:

$$
\boxed{2757.}
$$

Irrep multiplicities:

| irrep | multiplicity |
|---|---:|
| $[5]$ | 27,227 |
| $[4,1]$ | 104,146 |
| $[3,2]$ | 130,903 |
| $[3,1,1]$ | 153,455 |
| $[2,2,1]$ | 130,503 |
| $[2,1,1,1]$ | 103,318 |
| $[1^5]$ | 26,794 |

Machine ledger now records:

$$
\boxed{\text{structural depth-6 support closed for all 7 S5 irreps}.}
$$

Numerically closed sectors include:

- $[1^5]$;
- $[5]$ — vacuum only;
- $[4,1]$;
- $[2,1,1,1]$ — **CLOSED_FINITE_NUMERICAL**.

For $[2,1,1,1]$:

$$
\boxed{\operatorname{rank}=103318/103318.}
$$

16 exact $H_0$-null directions are lifted by $H_1$:

$$
\boxed{\operatorname{rank}H_1|_{16}=16/16,}
$$

$$
\boxed{\sigma_{\min}=1.1304521906426825.}
$$

Старый planned $130007\times130007$ H0-only giant minor больше **не является blocker**; ledger помечает его `SUPERSEDED_DO_NOT_USE_AS_BLOCKER`.

Но остаются independent numerical master witnesses для:

$$
\boxed{[3,2],\quad[3,1,1],\quad[2,2,1].}
$$

Поэтому:

$$
\boxed{
\text{finite depth-6 full master theorem}
=\text{NOT YET PROVED}.
}
$$

**Статус: FINITE programme, partial numerical closure + full structural closure.**

Machine truth:

- `depth6_frontier.json`
- `BQG_DEPTH6_2111_MASTER_CLOSED_2026-10-01.json`
- `scripts/verify_depth6_frontier.py`

---

# 16. Relational history already exists as a positive control

Constraint system не имеет external physical time автоматически.

Finite relational-history model показывает, что

$$
\text{global combined-constraint invariance}
$$

может сосуществовать с

$$
\text{nontrivial clock-conditioned evolution}.
$$

Chain:

$$
\boxed{
P_{\rm rel}
\to O_{\rm rel}
\to Z[J]
\to W[J]
\to \Gamma^{(2)}_{\rm tangent}.
}
$$

**Статус: FINITE positive control.**

Но externally declared C8 clock и toy system не являются физическим gravitational history generator BQG.

Файлы:

- `Q2_RELATIONAL_HISTORY_PROJECTOR.md`
- `Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md`
- `scripts/q2_relational_history_projector_gate.py`
- `scripts/q2_relational_metric_source_gate.py`

Theory-specific physical history:

$$
\boxed{\text{OPEN}.}
$$

---

# 17. Почему constraint resolvent не является graviton propagator

Exact Feshbach object:

$$
G_c(z)=Q_0^\dagger(z-H_{\rm constraint})^{-1}Q_0
$$

математически корректен.

Но

$$
\boxed{z\neq\omega_{\rm physical}}
$$

без independently derived history/time structure.

**Статус Feshbach identities: PROVED.**

**Promotion to physical propagator: NO-GO без physical history.**

Файлы:

- `FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md`
- `HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md`
- `scripts/feshbach_block_krylov_identity_gate.py`

---

# 18. Правильный physicalization route

Легальная последовательность:

$$
\boxed{
\{C_A^{(\epsilon)}\}
\to M_\epsilon
\to P_{\rm phys}^{(\epsilon)}
\to \text{refinement / rigging / boundary-history limit}
\to Z[J_g]
\to W[J_g]
\to \Gamma[g]
\to \Gamma^{(2)}_{\rm metric}
\to K_{TT}(\omega,\mathbf k).
}
$$

Нельзя перескакивать:

$$
H_{\rm constraint}\to G(\omega)
$$

напрямую.

**Статус theory-specific continuum route: OPEN.**

---

# 19. TT / graviton reference sector

Reduced TT positive control имеет:

- massless leading pole;
- positive residue;
- expected inverse-momentum equal-time covariance.

Bare control coefficients:

```text
eta2_bare  = -1/45
zeta4_bare = -1/12
```

Это **не** финальные interacting BQG coefficients.

**Статус: FINITE positive control.**

Файлы:

- `TT_PROPAGATOR_FIRST_PASS.md`
- `TT_VACUUM_TWO_POINT_RESULT.md`

---

# 20. Six-dimensional quartic TT observable space

Для parity-even quartic TT response с tetrahedral $S_4$ symmetry:

$$
\boxed{\dim\mathcal V_{\rm quartic}^{TT}=6.}
$$

Общий low-energy datum:

$$
\boxed{\mathbf c_{\rm IR}=(c_1,c_2,c_3,c_4,c_5,c_6).}
$$

Frozen extractor:

$$
\boxed{\operatorname{rank}=6,}
$$

$$
\boxed{\det A=\frac1{699840000}.}
$$

**Статус algebraic quotient/extractor: PROVED.**

Physical values $(c_1,\ldots,c_6)$:

$$
\boxed{\text{OPEN}.}
$$

Файлы:

- `S4_TT_QUARTIC_COMPLETE_BASIS.md`
- `C6_TO_TT_WILSON_COEFFICIENTS.md`
- `scripts/s4_tt_quartic_complete_basis_gate.py`
- `scripts/c6_tt_wilson_extractor.py`

---

# 21. Observable translator уже готов

Если physical six-vector однажды derived/frozen, можно получить

$$
\omega_\sigma^2
=c^2k^2\left[1+a_*^2k^2e_{4,\sigma}(\hat n)+O(a_*^4k^4)\right],
$$

$$
\frac{v_{g,\sigma}-c}{c}
=\frac32a_*^2k^2e_{4,\sigma}+\cdots,
$$

$$
\delta\phi_\sigma
=-\frac12La_*^2\left(\frac\omega c\right)^3e_{4,\sigma}+\cdots.
$$

**Статус map: PROVED algebraically.**

**Статус physical prediction: OPEN.**

Файлы:

- `TT_TO_REAL_PHYSICS_OBSERVABLES.md`
- `scripts/s4_tt_six_wilson_predictor.py`
- `scripts/physical_scale_prediction_bridge.py`

---

# 22. Новый entangled-gluing reduced model

Candidate local matching Hamiltonian:

$$
\boxed{
H_{\rm glue}
=\frac32I-\frac34(X_AX_B+Z_AZ_B).
}
$$

Exact spectrum:

$$
\boxed{\{0,3/2,3/2,3\}.}
$$

Unique ground state:

$$
\boxed{|\Phi^+\rangle=\frac{|ss\rangle+|tt\rangle}{\sqrt2}.}
$$

И

$$
\boxed{Q_AQ_B|\Phi^+\rangle=-\frac3{16}|\Phi^+\rangle.}
$$

**Статус spectrum/result: PROVED для заданного reduced Hamiltonian.**

**Статус $H_{\rm glue}$ как fundamental dynamics: CANDIDATE.**

Файлы:

- `BQG_TWO_NODE_REDUCED_GLUING_RESULT.md`
- `scripts/bqg_two_node_reduced_gluing_gate.py`

---

# 23. Three-node information hierarchy

Для open chain $A-B-C$:

$$
\boxed{I(A:B)=I(B:C)\approx0.7982479266\ \text{bit},}
$$

$$
\boxed{I(A:C)=0.5\ \text{bit}.}
$$

Volume correlations:

$$
\boxed{\langle Q_AQ_B\rangle=\langle Q_BQ_C\rangle=-3/32,}
$$

$$
\boxed{\langle Q_AQ_C\rangle=0.}
$$

**Статус: PROVED для reduced chain.**

---

# 24. Exact many-node XX/free-fermion mapping

Reduced chain Hamiltonian:

$$
H_M
=\sum_{i=1}^{M-1}
\left[\frac32I-\frac34(X_iX_{i+1}+Z_iZ_{i+1})\right].
$$

После local rotation:

$$
\boxed{
H_M\simeq\frac32(M-1)I-\frac34\sum_i(X_iX_{i+1}+Y_iY_{i+1}).
}
$$

После Jordan–Wigner:

$$
\boxed{
H_M=\frac32(M-1)I-\frac32\sum_i(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i).
}
$$

Single-particle energies:

$$
\boxed{\varepsilon_n=-3\cos\frac{n\pi}{M+1}.}
$$

Gap:

$$
\boxed{\Delta_M=O(M^{-1})\to0.}
$$

**Статус: PROVED для current reduced many-node model.**

---

# 25. Critical mutual information asymptotics

Half-filled XX thermodynamic limit:

$$
\langle c_0^\dagger c_r\rangle
=\frac{\sin(\pi r/2)}{\pi r}.
$$

Transverse spin correlation:

$$
C_x(r)=A_xr^{-1/2}[1+O(r^{-2})],
\qquad A_x\approx0.58835.
$$

Следовательно

$$
\boxed{
I_0(r)=\frac{A_x^2}{\ln2}\frac1r+O(r^{-2})
\approx\frac{0.50}{r}\ \text{bit}.
}
$$

**Статус: PROVED asymptotics + numerical gate.**

---

# 26. Gapped staggered-volume deformation

Controlled deformation:

$$
\boxed{H_m=H_0+m\sum_j(-1)^jZ_j.}
$$

В original intertwiner frame это staggered oriented-volume bias.

Band spectrum:

$$
\boxed{E_\pm(k)=\pm\sqrt{(2m)^2+9\cos^2k}.}
$$

Minimum positive single-particle energy:

$$
\boxed{\Delta_{\rm sp}=2|m|.}
$$

Correlation length:

$$
\boxed{\xi^{-1}=\operatorname{arsinh}(2|m|/3).}
$$

Asymptotic mutual information:

$$
\boxed{I_m(r)\sim B(m)r^{-1}e^{-2r/\xi}.}
$$

**Статус mathematics: PROVED for reduced deformation.**

**Fundamental BQG status of deformation: CANDIDATE.**

---

# 27. Universal scalar-MI distance no-go

Предположим universal phase-independent scalar map

$$
d=f(I).
$$

Critical phase требует при $I\to0$:

$$
f(I)\sim A/I.
$$

Gapped phase требует:

$$
f(I)\sim A'\ln(1/I).
$$

Они несовместимы.

Поэтому:

$$
\boxed{
\textbf{не существует одной phase-independent scalar }d=f(I_{ij})
\textbf{, asymptotically linear в обеих фазах.}
}
$$

**Статус: NO-GO.**

Файлы:

- `BQG_GAPPED_DEFORMATION_DISTANCE_NOGO.md`
- `scripts/bqg_gapped_distance_nogo_gate.py`

---

# 28. Local QFI conductance and additive resistance metric

Для edge $e=(ij)$ вводится relative twist

$$
K_e=\frac{Z_i-Z_j}{2}.
$$

Local quantum-information conductance:

$$
\boxed{g_e^{\rm QFI}=\frac14F_Q(\rho_e,K_e).}
$$

Critical reference:

$$
\boxed{F_{Q,*}=\frac{32}{\pi^2+4},}
$$

$$
\boxed{g_*=\frac{8}{\pi^2+4}.}
$$

Resistance length:

$$
\boxed{\ell_e=\ell_*\frac{g_*}{g_e}.}
$$

Network metric:

$$
\boxed{d(i,j)=\min_{\gamma:i\to j}\sum_{e\in\gamma}\ell_e.}
$$

В chain/tree additivity along geodesics exact.

**Статус additive metric class: PROVED mathematically.**

**QFI choice as unique fundamental BQG metric source: CANDIDATE.**

Дополнительный result:

$$
\boxed{
\rho_{ij}\text{ alone does not uniquely select a spatial metric functional.}
}
$$

**Статус: NO-GO на uniqueness from static local state alone.**

---

# 29. QFI-weighted spectral dimension

Weighted graph Laplacian:

$$
(L_g)_{ij}=\delta_{ij}\sum_k g_{ik}-g_{ij}.
$$

Return probability:

$$
P(\tau)=\frac1N\operatorname{Tr}e^{-\tau L_g}.
$$

Spectral dimension:

$$
\boxed{d_s(\tau)=-2\frac{d\ln P}{d\ln\tau}.}
$$

Для infinite homogeneous $D$-dimensional hypercubic graph:

$$
\boxed{
P_D(\tau)=\left[e^{-2g\tau}I_0(2g\tau)\right]^D.
}
$$

И

$$
\boxed{
d_s^{(D)}(\tau)=4Dg\tau\left[1-\frac{I_1(2g\tau)}{I_0(2g\tau)}\right].
}
$$

Следовательно

$$
\boxed{\lim_{\tau\to\infty}d_s^{(D)}=D.}
$$

При $u=g\tau$ conductance меняет diffusion scale, но не dimension fixed topology.

**Статус: PROVED calibration theorem.**

Файлы:

- `BQG_QFI_SPECTRAL_DIMENSION_RESULT.md`
- `scripts/bqg_qfi_spectral_dimension_gate.py`

---

# 30. Branching topology discriminator

Для infinite 3-regular Bethe lattice:

$$
\lambda_0=3-2\sqrt2>0,
$$

$$
P(\tau)\sim A\tau^{-3/2}e^{-g\lambda_0\tau}.
$$

Поэтому

$$
\boxed{d_s(\tau)=2g\lambda_0\tau+3+o(1)\to\infty.}
$$

То есть exponential branching не маскируется под finite-dimensional Euclidean geometry.

**Статус: PROVED asymptotic topology control.**

---

# 31. Topology-free surrogate gate: честный отрицательный результат

Первый unlabeled BQG-inspired generator использовал только:

- max valence 4;
- free-valence preference;
- local loop closure;
- no coordinates;
- no target dimension;
- no spectral feedback.

Получено:

$$
N=150:\quad d_s\approx1.316\pm0.106,
$$

$$
N=300:\quad d_s\approx1.226\pm0.031,
$$

$$
N=500:\quad d_s\approx1.232\pm0.030.
$$

Robustness scan по

$$
p_2\in\{0.25,0.40,0.50,0.60,0.75\}
$$

не дал robust $d_s\approx3$.

Следовательно:

$$
\boxed{
\textbf{four-valence + local loop closure insufficient to derive }d_s\approx3.
}
$$

**Статус: NO-GO для minimal surrogate rule.**

Файлы:

- `BQG_TOPOLOGY_FREE_EMERGENCE_RESULT.md`
- `scripts/bqg_topology_free_emergence_gate.py`

---

# 32. Physical graph-transition kernel: как новая ветка соединяется со старой

Новая emergence ветка не должна использовать arbitrary graph-growth probabilities.

Finite master theorem уже задаёт правильный object:

$$
\boxed{
K_T(\Gamma',\Gamma)
=\Pi_{\Gamma'}e^{-TM}\Pi_\Gamma.
}
$$

Physical graph-sector block:

$$
\boxed{
K_{\rm phys}(\Gamma',\Gamma)
=\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma.
}
$$

Microstate amplitude:

$$
\boxed{
\mathcal A^{\rm phys}_{\beta\alpha}
=\langle\Gamma',\beta|P_{\rm phys}|\Gamma,\alpha\rangle.
}
$$

Short-$T$ coupling:

$$
\boxed{
\langle\beta|M|\alpha\rangle
=\sum_{AB}G^{AB}\langle C_A\beta|C_B\alpha\rangle.
}
$$

Existing K5/Peter–Weyl regulator already has graph-changing support; about $44.4\%$ of one frozen commutator-column norm lies in sectors with $j=0$ links after cylindrical reduction.

Но:

$$
\boxed{44.4\%\neq|\mathcal A^{\rm phys}|^2.}
$$

**Статус finite projector formula: PROVED.**

**Numerical physical K5 graph-transition matrix: OPEN.**

Файлы:

- `BQG_PHYSICAL_GRAPH_TRANSITION_KERNEL.md`
- `scripts/bqg_projector_graph_transition_gate.py`
- `scripts/bqg_k5_graph_sector_master_shell.py`

---

# 33. Cosmology: exact local result и conformal obstruction

Finite relational source дал exact local 1PI shape action:

$$
\boxed{
\Gamma_{\rm shape}(s)
=s\operatorname{artanh}s+\frac12\log(1-s^2).
}
$$

Expansion:

$$
\Gamma_{\rm shape}
=\frac{s^2}{2}+\frac{s^4}{12}+\frac{s^6}{30}+\cdots.
$$

Но $X/Z$ local metric tangents trace-free:

$$
\operatorname{Tr}(g_0^{-1}M_X)=0,
$$

$$
\operatorname{Tr}(g_0^{-1}M_Z)=0.
$$

Следовательно local q=2 shape carrier не содержит нужного conformal/volume scalar.

**Статус action: PROVED finite.**

**Статус absence of local conformal scalar in X/Z carrier: NO-GO.**

Candidate next scalar carrier:

- collective $j=1$ volume sector.

Файлы:

- `Q2_FIRST_SCALAR_EFFECTIVE_ACTION.md`
- `Q2_COLLECTIVE_SCALAR_CARRIER.md`
- `COLLECTIVE_J1_VOLUME_DYNAMICS.md`

Physical cosmology:

$$
\boxed{\text{OPEN}.}
$$

---

# 34. Matter, photon and lensing

Даже physical metric kernel недостаточен без theory-specific matter coupling.

Open requirements:

- conserved matter source coupling;
- dynamical Maxwell kernel $\Gamma^{(2)}_{AA}$;
- massless deconfined photon pole;
- common causal IR cone;
- one scalar metric response for dynamics + weak/strong/CMB lensing + Fermat phase + GW wave optics.

**Статус: OPEN.**

Файлы:

- `BQG_SCALAR_RESPONSE_TO_MATTER.md`
- `UNIFIED_PHYSICAL_COSMOLOGY_INTERFERENCE.md`
- `physicalization_gates.json`

---

# 35. 2T extension

Potential two-time embedding требует реальной structure

$$
Q_{11}\sim X^2,
\qquad
Q_{12}\sim X\cdot P,
\qquad
Q_{22}\sim P^2,
$$

с $Sp(2,\mathbb R)$ closure.

Пока не доказаны:

- exact $Sp(2,\mathbb R)$ closure;
- $(d,2)$ kinetic signature;
- ghost-free 2T $\to$ 1T reduction.

**Статус: OPEN.**

Файлы:

- `README_2T_FRONTIER.md`
- `BQG_2T_ALGEBRA_GATE.md`
- `BQG_2T_CLOSURE_SCAN.md`
- `BQG_2T_CONSTRAINT_INVENTORY.md`

---

# 36. Shadow action / black-hole frontier

Цель:

$$
(A,\Theta,g_{\mu\nu})
\to S_{\rm shadow}.
$$

Затем spherical solution должна дать

$$
\boxed{h_{\rm BQG}(r)}
$$

из equations, а не из ansatz.

Только затем допустимо вычислять

$$
\Delta T_H,
\qquad
\Delta r_{\rm ph},
\qquad
\Delta\Omega_{\rm QNM}.
$$

Старый static-spherical reduced branch дал no-go:

$$
\boxed{h_{\rm BQG}=0}
$$

в том конкретном ansatz/sector.

**Статус этого reduced branch: NO-GO.**

**General shadow-action derivation: OPEN.**

---

# 37. Machine-readable truth

README не является последним судьёй.

Основные ledgers:

- `theory_gates.json`
- `physicalization_gates.json`
- `depth6_frontier.json`

Verifiers:

- `scripts/verify_theory_gates.py`
- `scripts/verify_physicalization_gates.py`
- `scripts/verify_depth6_frontier.py`

Если prose расходится с machine truth, приоритет имеет воспроизводимый certificate/ledger.

---

# 38. Единая актуальная карта статусов

## 38.1. PROVED

- q=2 exact Walsh tetrahedral carrier;
- exact q=2 dimension-three fixed point;
- logical metric Jacobian rank two;
- active + no-link exact graph-link representation;
- finite master-kernel theorem $\ker M=\cap\ker C_A$;
- oriented-volume commutator identity;
- $Q_{\rm phys}=(\sqrt3/4)\sigma_y$;
- anisotropy-volume identity $\mathcal A_p=4(\Delta Q)^2$;
- exact two-node reduced spectrum;
- exact three-node reduced information hierarchy;
- XX/free-fermion mapping;
- critical/gapped asymptotics in reduced chain;
- scalar-MI incompatibility theorem;
- additive resistance-metric theorem for positive edge conductances;
- hypercubic QFI spectral-dimension calibration;
- Bethe-lattice asymptotic discriminator;
- six-dimensional quartic TT quotient;
- six-Wilson extractor full rank;
- Feshbach/block-Krylov identities;
- algebraic GW observable translator.

## 38.2. FINITE

- selected global PL 16-cell gluing;
- Plebanski/Urbantke/Einstein reconstruction controls;
- Regge/EH finite continuum-direction controls;
- L=6 held-out Regge prediction;
- Peter–Weyl graph-changing constraint stack;
- HDA scaling controls;
- DeWitt/ADM finite controls;
- depth-4 closure;
- depth-6 structural closure and several numerical irrep closures;
- finite relational-history positive control;
- finite metric-source generating functional positive control;
- reduced TT propagator/vacuum controls;
- topology-free surrogate ensembles;
- finite graph-transition projector bridge selftest.

## 38.3. CANDIDATE

- fully symmetric Peter–Weyl blocking as unique microscopic RG rule;
- reduced $H_{\rm glue}$ as fundamental BQG dynamics;
- staggered oriented-volume mass as fundamental deformation;
- QFI relative-twist conductance as unique fundamental spatial metric source;
- resistance length normalization $\ell_*$ from first principles;
- collective $j=1$ scalar carrier;
- graph-history interpretation of finite-$T$ master heat kernel.

## 38.4. NO-GO

- local pairwise scalar distance $d=f(I_{ij})$ universal across critical/gapped phases;
- unique spatial metric from static $\rho_{ij}$ alone;
- valence-4 + local-loop-closure surrogate as sufficient mechanism for $d_s\approx3$;
- promotion of constraint resolvent spectral parameter $z$ to physical $\omega$ without physical history;
- local X/Z q=2 shape carrier as sufficient conformal scalar;
- previous static-spherical ansatz yielding nonzero BQG black-hole hair;
- treating $H_0$-nullity as master-kernel nullity.

## 38.5. OPEN

- remaining numerical depth-6 master witnesses $[3,2]$, $[3,1,1]$, $[2,2,1]$;
- all-depth/refinement theorem;
- continuum physical projector / rigging map;
- theory-specific physical clock/history;
- connected interblock metric cumulants;
- physical $\Gamma[g]$;
- physical interacting $K_{TT}(\omega,\mathbf k)$;
- microscopic physical six-Wilson vector;
- one common physical scale;
- self-consistent irregular-graph QFI weights from physical histories;
- actual numerical K5 graph-sector $\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma$ blocks;
- physical Maxwell sector;
- background and scalar cosmology;
- universal matter/lensing response;
- 2T closure;
- derived shadow action and non-ansatz $h_{\rm BQG}(r)$;
- blind experimental comparison.

---

# 39. Девять обязательных physicalization gates

Machine ledger `physicalization_gates.json` требует закрыть:

1. `PHYSICAL_PROJECTOR_HISTORY`;
2. `CONNECTED_INTERBLOCK_HISTORY`;
3. `PHYSICAL_TT_KERNEL`;
4. `IR_SIX_VECTOR`;
5. `COMMON_SCALE_CALIBRATION`;
6. `DYNAMICAL_MAXWELL_KERNEL`;
7. `PHYSICAL_BACKGROUND_COSMOLOGY`;
8. `PHYSICAL_SCALAR_COSMOLOGY`;
9. `LENSING_DYNAMICS_CLOSURE`.

Пока эти gates не закрыты, нельзя заявлять завершённую predictive quantum gravity.

---

# 40. Что является настоящим следующим рубежом

После объединения старой и новой веток frontier больше не должен определяться одним красивым новым proxy.

Следующие задачи идут параллельно, но имеют разный приоритет.

## 40.1. Computational structural priority

Закрыть remaining numerical depth-6 witnesses:

$$
[3,2],\quad[3,1,1],\quad[2,2,1].
$$

После этого честно проверить:

$$
\boxed{\ker M^{(d=6)}=\operatorname{span}\{|0\rangle\}?}
$$

## 40.2. Main mathematical priority

Вместо бесконечного brute-force по depth:

$$
\boxed{\text{derive refinement / induction theorem}.}
$$

Цель:

$$
P_{\rm phys}^{(d)}\to P_{\rm phys}^{\rm continuum}.
$$

## 40.3. Main physical priority

Построить theory-specific physical history:

$$
\boxed{
P_{\rm phys}
\to \text{relational history}
\to Z[J_g]
\to W[J_g]
\to \Gamma[g].
}
$$

## 40.4. Emergence priority

Не использовать новый hand-built graph generator.

Нужно получить реальные physical graph-sector amplitudes:

$$
\boxed{
A_{\Gamma'\Gamma}
=\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma.
}
$$

Затем:

$$
\boxed{
\text{physical graph histories}
\to \rho_{ij}
\to g_{ij}^{\rm QFI}
\to L_g
\to P(\tau)
\to d_s(\tau).
}
$$

Только если $d_s\approx3$ возникнет **из projector-weighted histories без topology-by-hand**, это будет сильный emergent-3D result.

---

# 41. Короткая формулировка BQG сегодня

> **Binary Quantum Gravity — это воспроизводимая discrete quantum-gravity candidate architecture, в которой binary q=2 microstructure даёт exact tetrahedral geometric carrier и analytical dimension-three refinement fixed point; SU(2)/Peter–Weyl sectors реализуют local quantum geometry и graph-changing dynamics; finite Plebanski, Regge, DeWitt and HDA gates проверяют gravitational structure; master constraint задаёт finite physical projector; relational positive controls показывают легальную дорогу к $Z[J]\to W[J]\to\Gamma[g]$; новая emergence-ветка связывает oriented volume, entanglement, local QFI conductance и spectral dimension. При этом continuum physical projector, theory-specific physical history, interacting graviton kernel, physical six-Wilson vector, common scale, cosmology, Maxwell sector и experimental confirmation остаются OPEN.**

Ещё короче:

$$
\boxed{
\text{binary information}
\to \text{quantum geometry}
\to \text{finite gravity constraints}
\to \text{emergent network geometry}
\to \text{unfinished physical continuum}.
}
$$

---

# 42. Где мы реально находимся

Мы уже далеко прошли путь

$$
\text{idea}
\to \text{microstructure}
\to \text{local geometry}
\to \text{global finite geometry}
\to \text{graph-changing constraints}
\to \text{large finite habitats}
\to \text{master-projector machinery}
\to \text{information-geometry diagnostics}.
$$

Но вертикальная граница остаётся здесь:

$$
\boxed{
\underbrace{
\text{binary microstructure}
\to
\text{finite quantum geometry}
\to
\text{finite gravity dynamics}
}_{\text{сильная построенная часть}}
\quad\Big|\quad
\underbrace{
\text{refinement}
\to
P_{\rm phys}^{\rm continuum}
\to
\text{physical history}
\to
\Gamma[g]
\to
K_{TT}
\to
\text{prediction}
}_{\text{главная открытая физика}}
}
$$

Новая QFI/spectral-dimension ветка не отменяет эту границу; она даёт дополнительный инструмент для проверки того, какая spatial geometry возникает **после** physical graph dynamics.

---

# 43. Что может убить теорию

BQG должна быть отвергнута или серьёзно пересмотрена, если:

- refinement не стабилизирует physical sector;
- full depth sequence порождает uncontrolled new master kernels;
- HDA anomaly не исчезает в controlled limit;
- physical inner product нельзя сделать положительным;
- theory-specific physical history не существует;
- physical TT kernel не имеет Einstein/Fierz–Pauli massless pole;
- возникают unavoidable ghost/tachyon modes;
- physical six-vector не имеет regulator-independent limit;
- разные observables требуют разных fitted scales;
- scalar/matter/photon sectors нельзя согласовать с одним geometry/history;
- projector-derived graph histories не имеют controlled continuum geometry;
- blind external data исключают frozen predictions.

Это часть научной ценности проекта, а не слабость.

---

# 44. Канонические источники

## Structural status

- `THEORY_STATUS.md`
- `CANONICAL_THEORY_PACKAGE.md`
- `theory_gates.json`

## Physicalization

- `MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md`
- `Q2_RELATIONAL_HISTORY_PROJECTOR.md`
- `Q2_RELATIONAL_METRIC_SOURCE_GENERATING_FUNCTIONAL.md`
- `physicalization_gates.json`

## Depth-6

- `depth6_frontier.json`
- `BQG_DEPTH6_2111_MASTER_CLOSED_2026-10-01.json`

## Emergence / information geometry

- `BQG_MINIMAL_ENTANGLEMENT_VOLUME_RESULT.md`
- `BQG_TWO_NODE_REDUCED_GLUING_RESULT.md`
- `BQG_THREE_NODE_REDUCED_CHAIN_RESULT.md`
- `BQG_MANY_NODE_FREE_FERMION_MAPPING.md`
- `BQG_MUTUAL_INFORMATION_ASYMPTOTIC_RESULT.md`
- `BQG_GAPPED_DEFORMATION_DISTANCE_NOGO.md`
- `BQG_LOCAL_INFORMATION_RESISTANCE_METRIC.md`
- `BQG_QFI_SPECTRAL_DIMENSION_RESULT.md`
- `BQG_TOPOLOGY_FREE_EMERGENCE_RESULT.md`
- `BQG_PHYSICAL_GRAPH_TRANSITION_KERNEL.md`

## Future observables

- `S4_TT_QUARTIC_COMPLETE_BASIS.md`
- `C6_TO_TT_WILSON_COEFFICIENTS.md`
- `TT_TO_REAL_PHYSICS_OBSERVABLES.md`
- `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md`

---

# 45. Последнее правило

Любое новое утверждение должно отвечать на пять вопросов:

1. theorem или numerical evidence?
2. finite или continuum?
3. constraint object или physical observable?
4. algebraic map или physical prediction?
5. internal consistency или experimental confirmation?

Если ответ неясен, статус понижается.

Источник истины:

$$
\boxed{
\text{код}
+\text{certificate}
+\text{machine ledger}
+\text{reproducible gate}
>\text{красивая формулировка README}.
}
$$

---

# Финальная объединённая формула проекта

$$
\boxed{
\begin{array}{c}
\mathbb Z_2^2\\
\downarrow\\
\text{Walsh tetrahedron}\\
\downarrow\\
d_*=3\\
\downarrow\\
SU(2)\text{ physical nodes}\\
\downarrow\\
\text{oriented volume + shape geometry}\\
\downarrow\\
\text{Peter--Weyl graph-changing dynamics}\\
\downarrow\\
\text{Plebanski / Regge / HDA controls}\\
\downarrow\\
M\to P_{\rm phys}\\
\downarrow\\
\text{relational histories}\\
\downarrow\\
\text{entanglement / QFI network geometry}\\
\downarrow\\
L_g\to d_s\\
\downarrow\\
Z[J_g]\to W[J_g]\to\Gamma[g]\\
\downarrow\\
K_{TT}(\omega,\mathbf k)\\
\downarrow\\
(c_1,\ldots,c_6)_{\rm IR}\\
\downarrow\\
\text{one-scale frozen observables}\\
\downarrow\\
\text{experiment}
\end{array}
}
$$

Верхняя и средняя части этой лестницы уже содержат множество exact и finite results.

Нижняя часть — **главная открытая физика BQG**.


---

# 46. Dynamical distance: первый строгий мост к причинности

После QFI-weighted spatial geometry можно задать локальный propagation Hamiltonian

$$
oxed{
h=V-A_g,
}
$$

где $V$ — произвольный diagonal onsite operator, а на каждом physical edge

$$
(A_g)_{ij}=g_{ij}>0.
$$

Для propagator

$$
U(t)=e^{-iht}
$$

и graph distance $d_G(i,j)$ выполняется exact theorem:

$$
oxed{
(h^n)_{ij}=0
qquad
n<d_G(i,j).
}
$$

На первом разрешённом порядке $d=d_G(i,j)$

$$
oxed{
(h^d)_{ij}
=
(-1)^d
sum_{gammain {m SP}(i,j)}
prod_{eingamma} g_e

eq0,
}
$$

поскольку все edge weights положительны и shortest-path contributions не могут сократиться.

Поэтому

$$
oxed{
d_G(i,j)
=
minleft{
n:
partial_t^nU_{ij}(0)
eq0
ight}.
}
$$

То есть combinatorial shortest-path distance восстанавливается из **первого ненулевого short-time propagation order**, без координат, fit и long-range correlation ansatz.

Для QFI weights

$$
g_{ij}^{\rm QFI}=\frac14F_Q(\rho_{ij},K_{ij})>0
$$

получаем

$$
oxed{
d_G(i,j)
=
minleft{
n:
partial_t^n[e^{-ih_{\rm QFI}t}]_{ij}|_{t=0}
eq0
ight}.
}
$$

Arbitrary diagonal gap / staggered onsite terms не меняют этот порядок, поэтому result устойчив к critical/gapped onsite deformations.

Frozen numerical regression:

- $N=6,8,10$;
- 10 random connected weighted graphs на размер;
- arbitrary positive edge weights;
- random diagonal onsite potentials;
- 30/30 graphs PASS.

**Статус: PROVED для sign-definite graph-local Hamiltonians + FINITE regression.**

Это ещё не Lorentzian spacetime causality. Не выведены physical clock, light cone и universal propagation speed.

Файлы:

- `BQG_DYNAMICAL_DISTANCE_THEOREM.md`
- `scripts/bqg_dynamical_distance_gate.py`

Следующий causal frontier:

$$
oxed{
\text{projector-derived graph histories}
\to
\text{many-body local generator}
\to
\text{nested-commutator front}
\to
v_{\rm LR}
\to
\text{continuum causal cone}.
}
$$


---

# 47. Many-body operator front и exact velocity-gap-correlation relation

Одночастичный short-time theorem поднимается до many-body locality.

Для graph-local Hamiltonian

\[
H=\sum_X h_X,
\]

где каждый \(h_X\) поддержан на одной вершине или одном edge, и local operator \(O_i\),

\[
O_i(t)=
\sum_{n=0}^{\infty}
\frac{(it)^n}{n!}\operatorname{ad}_H^n(O_i).
\]

После \(n\) nested commutators support не может выйти за radius-\(n\) graph ball:

\[
\boxed{
\operatorname{supp}\operatorname{ad}_H^n(O_i)
\subseteq B_n(i).
}
\]

Поэтому для local probe \(O_j\)

\[
\boxed{
[\operatorname{ad}_H^n(O_i),O_j]=0,
\qquad
n<d_G(i,j).
}
\]

То есть operator influence cannot appear before graph-distance order.

Для positive-coupling XX path/tree sector и endpoint probes \(Z_i,Z_j\) первый ненулевой nested-commutator order равен точно

\[
\boxed{
\min\{n:[\operatorname{ad}_H^n(Z_i),Z_j]\neq0\}
=
d_G(i,j).
}
\]

**Статус: PROVED в заявленном graph-local / path-tree scope.**

Для homogeneous reduced chain

\[
\varepsilon(k)=-3\cos k
\]

и поэтому

\[
\boxed{v_{\max}(0)=3.}
\]

Для staggered-volume deformation

\[
E_\pm(k)=\pm\sqrt{4m^2+9\cos^2k}
\]

точный maximum group velocity:

\[
\boxed{
v_{\max}(m)=\sqrt{4m^2+9}-2|m|.
}
\]

С ранее выведенными

\[
\Delta_{\rm sp}=2|m|,
\]

\[
\xi^{-1}=\operatorname{arsinh}(2|m|/3)
\]

получаем

\[
\boxed{
v_{\max}
=
\sqrt{\Delta_{\rm sp}^2+9}-\Delta_{\rm sp}
}
\]

и особенно

\[
\boxed{
\frac{v_{\max}}{3}
=
e^{-1/\xi}.
}
\]

Таким образом в reduced model одна и та же deformation одновременно:

- открывает gap;
- сокращает static correlation length;
- замедляет ballistic information front.

И эти три quantities связаны **exact analytically**, а не empirical fit.

**Статус: PROVED для homogeneous staggered-volume reduced model.**

Это ещё не physical speed of light. Для Lorentzian cone остаются OPEN:

- physical clock/history;
- projector-derived graph dynamics;
- continuum/refinement limit;
- isotropic causal cone;
- common gravity/matter/photon cone.

Файлы:

- \`BQG_MANY_BODY_OPERATOR_FRONT_RESULT.md\`
- \`scripts/bqg_many_body_operator_front_gate.py\`


---

# 48. Sharp analytic propagation cone

Для homogeneous reduced chain generic Lieb–Robinson norm bound не является tight. Благодаря exact free-fermion dispersion можно получить более сильный complex-momentum cone.

Для critical phase

\[
\varepsilon(k)=-3\cos k,
\]

propagator равен

\[
\boxed{
U_r(t)=i^rJ_r(3t).
}
\]

Contour shift \(k\to k+i\mu\) даёт

\[
\boxed{
|U_r(t)|
\le
\exp[-\mu r+3|t|\sinh\mu].
}
\]

Поэтому

\[
\boxed{
v_\mu^{(0)}
=
3\frac{\sinh\mu}{\mu},
}
\]

и

\[
\boxed{
\lim_{\mu\to0^+}v_\mu^{(0)}=3=v_{\max}(0).
}
\]

Для staggered-volume phase

\[
E_\pm(k)=\pm\sqrt{4m^2+9\cos^2k}
\]

nearest complex branch point находится на

\[
\boxed{
\mu_c
=
\operatorname{arsinh}\left(\frac{2|m|}{3}\right)
=
\xi^{-1}.
}
\]

То есть **static correlation length и dynamical analyticity strip задаются одной и той же singularity**.

Для любого

\[
0<\mu<\mu_c
\]

получено exact:

\[
\boxed{
\sup_k|\Im E(k+i\mu)|
=
\frac{v_{\max}(m)}2\sinh(2\mu).
}
\]

Следовательно существует finite \(C_m(\mu)\), для которого

\[
\boxed{
\|U_r(t)\|
\le
C_m(\mu)
\exp\left[
-\mu r
+
\frac{v_{\max}(m)}2|t|\sinh(2\mu)
\right].
}
\]

Или

\[
\boxed{
\|U_r(t)\|
\le
C_m(\mu)
e^{-\mu[r-v_\mu(m)|t|]},
}
\]

где

\[
\boxed{
v_\mu(m)
=
v_{\max}(m)
\frac{\sinh(2\mu)}{2\mu}.
}
\]

При \(\mu\to0\)

\[
\boxed{
v_\mu(m)\to v_{\max}(m).
}
\]

Поэтому для каждого \(v>v_{\max}\) существует exponential exterior cone, и asymptotic ballistic front равен

\[
\boxed{
v_{\rm front}(m)
=
v_{\max}(m).
}
\]

С учётом предыдущих результатов:

\[
\boxed{
\Delta_{\rm sp}=2|m|,
}
\]

\[
\boxed{
\mu_c=\xi^{-1}
=
\operatorname{arsinh}(\Delta_{\rm sp}/3),
}
\]

\[
\boxed{
v_{\rm front}
=
\sqrt{\Delta_{\rm sp}^2+9}-\Delta_{\rm sp},
}
\]

\[
\boxed{
\frac{v_{\rm front}}3=e^{-1/\xi}.
}
\]

То есть одна complex-momentum singularity одновременно управляет:

- static exponential correlations;
- analyticity radius;
- exponential propagation cone;
- exact asymptotic information-front velocity.

**Статус: PROVED для homogeneous reduced free-fermion / staggered-volume model.**

Это всё ещё не physical Lorentz cone полной BQG.

Файлы:

- \`BQG_SHARP_ANALYTIC_CAUSAL_CONE.md\`
- \`scripts/bqg_sharp_analytic_causal_cone_gate.py\`


---

# 49. Graph-changing master-flow causal order

Для graph-sector decomposition

\[
\mathcal H=\bigoplus_\Gamma\mathcal H_\Gamma
\]

и finite master constraint

\[
M=C_A^\dagger G^{AB}C_B
\]

graph-sector heat kernel

\[
K_T(\Gamma',\Gamma)
=
\Pi_{\Gamma'}e^{-TM}\Pi_\Gamma
\]

имеет expansion

\[
K_T
=
\sum_{n\ge0}
\frac{(-T)^n}{n!}
\Pi_{\Gamma'}M^n\Pi_\Gamma.
\]

Определим

\[
\boxed{
d_M(\Gamma,\Gamma')
=
\min\{n:
\Pi_{\Gamma'}M^n\Pi_\Gamma\neq0\}.
}
\]

Тогда

\[
\boxed{
d_M
=
\min\{n:
\partial_T^n K_T(\Gamma',\Gamma)|_{T=0}\neq0\}.
}
\]

Это exact graph-changing analogue fixed-graph dynamical distance.

Если каждый microscopic constraint \(C_A\) меняет graph sector максимум на один elementary move, то

\[
\Pi_{\Gamma'}M\Pi_\Gamma=0
\quad
\text{при }
d_C(\Gamma,\Gamma')>2,
\]

и, более общо,

\[
\boxed{
\Pi_{\Gamma'}M^n\Pi_\Gamma=0
\quad
\text{если }
d_C(\Gamma,\Gamma')>2n.
}
\]

Следовательно

\[
\boxed{
d_M(\Gamma,\Gamma')
\ge
\left\lceil
\frac{d_C(\Gamma,\Gamma')}{2}
\right\rceil.
}
\]

И

\[
\boxed{
K_T(\Gamma',\Gamma)
=
O\!\left(
T^{\lceil d_C/2\rceil}
\right).
}
\]

Это строгий finite-regulator graph-changing locality bound.

**Статус: PROVED.**

Но \(T\) здесь всё ещё projector/master flow parameter, а не physical time.

Файлы:

- \`BQG_GRAPH_CHANGING_CAUSAL_ORDER_THEOREM.md\`
- \`scripts/bqg_graph_changing_causal_order_gate.py\`

---

# 50. NO-GO: physical projector alone does not determine causality

Physical projector

\[
P_{\rm phys}
=
\mathbf 1_{\{0\}}(M)
\]

не сохраняет уникально locality/support structure nonzero master spectrum.

Exact counterexample:

\[
M_{\rm path}
=
\begin{pmatrix}
1&-1&0\\
-1&2&-1\\
0&-1&1
\end{pmatrix}
\]

имеет support graph

\[
1-2-3
\]

и

\[
d_M(1,3)=2.
\]

Но

\[
M_{\rm complete}
=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix}
\]

имеет complete support graph и

\[
d_M(1,3)=1.
\]

При этом оба master operators имеют один и тот же zero mode

\[
\frac1{\sqrt3}(1,1,1)^T
\]

и один и тот же полный projector

\[
\boxed{
P_{\rm phys}
=
\frac13
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix}.
}
\]

Следовательно

\[
\boxed{
P_{\rm phys}
\text{ alone cannot reconstruct causal order.}
}
\]

Даже полный \(P_{\rm phys}\), не только отдельный block, недостаточен.

Поэтому universal rule

\[
d(\Gamma,\Gamma')
=
F(\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma)
\]

не существует.

**Статус: NO-GO / PROVED by exact counterexample.**

Правильная архитектура теперь:

\[
\boxed{
\{C_A\}
\to
M
\to
\text{local transition order}
\to
P_{\rm phys}
+
\text{relational history}
\to
\text{physical causal histories}.
}
\]

То есть

\[
\boxed{
\text{constraint selection}
\neq
\text{causal ordering}.
}
\]

Файлы:

- \`BQG_PROJECTOR_ONLY_CAUSALITY_NOGO.md\`
- \`scripts/bqg_projector_only_causality_nogo_gate.py\`


---

# 51. Refinement-projector stability theorem

Для finite positive master operators

\[
M_d,\qquad M_{d+1}
\]

и isometric embedding

\[
\iota_d:\mathcal H_d\to\mathcal H_{d+1}
\]

определим

\[
R_d=M_{d+1}\iota_d-\iota_dM_d.
\]

Пусть

\[
P_d=\mathbf1_{\{0\}}(M_d),
\qquad
P_{d+1}=\mathbf1_{\{0\}}(M_{d+1}),
\]

а \(\Delta_d,\Delta_{d+1}\) — первые positive master gaps.

Тогда exact:

\[
\boxed{
\|(I-P_{d+1})\iota_dP_d\|
\le
\frac{\|R_d\|}{\Delta_{d+1}},
}
\]

\[
\boxed{
\|P_{d+1}\iota_d(I-P_d)\|
\le
\frac{\|R_d\|}{\Delta_d},
}
\]

и поэтому

\[
\boxed{
\|P_{d+1}\iota_d-\iota_dP_d\|
\le
\frac{\|R_d\|}
{\min(\Delta_d,\Delta_{d+1})}.
}
\]

Следовательно sufficient refinement condition:

\[
\boxed{
\epsilon_d
=
\frac{\|R_d\|}
{\min(\Delta_d,\Delta_{d+1})}
\to0.
}
\]

Если

\[
\sum_d\epsilon_d<\infty,
\]

то embedded physical projections образуют Cauchy sequence на inductive-limit carrier, что даёт controlled route к

\[
\boxed{P_\infty.}
\]

**Статус: PROVED exact finite operator theorem.**

Файлы:

- \`BQG_REFINEMENT_PROJECTOR_STABILITY_THEOREM.md\`
- \`scripts/bqg_refinement_projector_stability_gate.py\`

---

# 52. Canonical BQG refinement residual decomposition

Первый BQG embedding уже существует:

\[
W:[2,2]_{j=1/2}\to[2,2]_{j=1},
\]

\[
\boxed{
W=
\begin{pmatrix}
0&2/3\\
1&0\\
0&-\sqrt5/3
\end{pmatrix},
\qquad
W^\dagger W=I.
}
\]

Он exact intertwiner для всех \(24\) permutations \(S_4\).

Для coarse/fine operators:

\[
R=M_cW-WM_f
\]

exact разложение:

\[
\boxed{
R
=
(I-WW^\dagger)M_cW
+
W(W^\dagger M_cW-M_f).
}
\]

Определим

\[
L=(I-WW^\dagger)M_cW,
\]

\[
D=W^\dagger M_cW-M_f.
\]

Тогда

\[
\boxed{
R=L+WD,
}
\]

\[
\boxed{
R^\dagger R=L^\dagger L+D^\dagger D.
}
\]

Таким образом full RG defect распадается на:

- **carrier leakage** \(L\);
- **internal dynamical mismatch** \(D\).

Это превращает continuum test из giant-matrix comparison в thin-block calculation.

**Статус: PROVED exact identity.**

Файлы:

- \`BQG_CANONICAL_REFINEMENT_RESIDUAL_DECOMPOSITION.md\`
- \`scripts/bqg_canonical_refinement_residual_gate.py\`

---

# 53. Первый theory-specific dynamical RG datum

Реализован прямой расчёт

\[
j=\frac12\to j=1
\]

на одинаковом 32D logical carrier.

Fine:

\[
K_{1/2}=P(H_{E,0}^{\rm sine}+H_{E,1}^{\rm sine})^2P.
\]

Coarse logical states строятся через

\[
W^{\otimes5}
\]

в all-\(j=1\) K5 singlet sector, после чего тем же production Peter–Weyl operator вычисляется

\[
K_1.
\]

Первый dynamical RG mismatch:

\[
\boxed{
D_{1/2\to1}^{\rm return}
=
K_1-K_{1/2}.
}
\]

Это ещё не full master \(M=C^\dagger GC\), но уже первый прямой same-dynamics / same-logical-coordinates RG test.

Файлы:

- \`BQG_JHALF_TO_J1_RETURN_RG.md\`
- \`scripts/bqg_jhalf_to_j1_return_rg_gate.py\`
- \`.github/workflows/bqg-refinement-jhalf-j1.yml\`

**Статус: IMPLEMENTED / NUMERICAL EXECUTION ACTIVE.**


---

# 54. S4 logical-carrier multiplicity theorem

Для equal-spin four-valent singlet space

\[
\mathcal H_j^{\rm sing}
=
\mathrm{Inv}_{SU(2)}(V_j^{\otimes4})
\]

точная multiplicity irrep \([2,2]\) равна

\[
\boxed{
m_{[2,2]}(j)
=
\left\lceil\frac{2j}{3}\right\rceil.
}
\]

Следовательно multiplicity-one сохраняется только для

\[
\boxed{
j=\frac12,\ 1,\ \frac32.
}
\]

Уже при

\[
\boxed{
j=2
}
\]

имеем

\[
\boxed{
m_{[2,2]}=2.
}
\]

Поэтому \(S_4\) symmetry **не может** сама по себе задавать один уникальный logical qubit на всех Peter-Weyl scales.

**Статус: PROVED + NO-GO.**

Corrected CI scan на real recoupling engine прошёл GREEN до \(j=4\) и подтвердил

\[
\operatorname{rank}P_{22}^{(j)}
=
2m_{[2,2]}(j).
\]

Правильная coarse structure теперь:

\[
\boxed{
\mathbb C^{m_{22}(j)}
\otimes
V_{[2,2]}.
}
\]

То есть с \(j\ge2\) появляется новый multiplicity channel, который должен выбираться dynamics, а не symmetry alone.

Файлы:

- \`BQG_S4_LOGICAL_MULTIPLICITY_THEOREM.md\`
- \`scripts/bqg_s4_refinement_carrier_scan.py\`
- \`.github/workflows/bqg-s4-refinement-carrier.yml\`

---

# 55. Первый multiplicity-space selection target: j=2

На \(j=2\) впервые возникает

\[
m_{[2,2]}=2,
\]

то есть \([2,2]\)-isotypic sector имеет вид

\[
\mathbb C^2_{\rm mult}\otimes V_{[2,2]}.
\]

Для любого \(S_4\)-invariant operator \(O\):

\[
\boxed{
O|_{[2,2]\text{-iso}}
=
A_2\otimes I_2.
}
\]

Поэтому первый minimal selection problem — вычислить \(A_2\).

В качестве первого geometric diagnostic уже реализован existing absolute-volume operator:

\[
V=|Q|^{1/4}.
\]

Если restricted spectrum содержит две distinct doubly-degenerate eigenvalues, geometry сама задаёт canonical multiplicity eigenbasis.

Если нет — selection должен исходить из full dynamics/master operator.

Файлы:

- \`BQG_J2_MULTIPLICITY_VOLUME_RESULT.md\`
- \`scripts/bqg_j2_multiplicity_volume_gate.py\`
- \`.github/workflows/bqg-j2-multiplicity-volume.yml\`

**Статус: IMPLEMENTED / NUMERICAL EXECUTION ACTIVE.**


---

# 56. Multiplicity-channel spectral selection theorem

Пусть \(S_4\)-equivariant master/operator на \([2,2]\)-isotypic sector имеет вид

\[
P_{22}M_jP_{22}=A_j\otimes I_2.
\]

Если \(A_j\) имеет isolated simple eigenvalue \(\lambda_j\) с multiplicity gap

\[
\gamma_j
=
\min_{\mu\neq\lambda_j}
|\mu-\lambda_j|,
\]

то eigenvector \(u_j\) задаёт unique \(S_4\)-covariant logical copy

\[
\boxed{
\mathcal L_j
=
\operatorname{span}\{u_j\}
\otimes
V_{[2,2]}.
}
\]

Для Hermitian perturbation \(A_j\to A_j+E_j\) при \(\|E_j\|<\gamma_j/2\):

\[
\boxed{
\|\widetilde\Pi_{\mathcal L_j}-\Pi_{\mathcal L_j}\|
\le
\frac{2\|E_j\|}{\gamma_j}.
}
\]

Вводим второй refinement-control parameter:

\[
\boxed{
\eta_j=\frac{\|\delta A_j\|}{\gamma_j}.
}
\]

Теперь fast-closure hierarchy:

\[
\boxed{
A_j
\to
\gamma_j
\to
\Pi_{\mathcal L_j}
\to
\iota_j
\to
R_j
\to
\epsilon_j
\to
P_\infty.
}
\]

Где

\[
\epsilon_j
=
\frac{\|R_j\|}{\Delta_{\min,j}}.
\]

**Статус: PROVED finite operator theorem.**

Файлы:

- \`BQG_MULTIPLICITY_CHANNEL_SELECTION_THEOREM.md\`
- \`scripts/bqg_multiplicity_channel_selection_gate.py\`

---

# 57. Actual j=2 constraint-master multiplicity calculation

Запущен первый actual constraint-dynamics multiplicity test.

На symmetric K5 background с all links \(j=2\) и локальным node-0 singlet carrier \(K_2=0,2,4,6,8\) используется production operator

\[
C_0=H_{E,0}^{\rm sine}.
\]

Строится positive local master block

\[
\boxed{
M_0=C_0^\dagger C_0
}
\]

и его restriction

\[
\boxed{
P_{22}^{(2)}M_0P_{22}^{(2)}
=
A_2^{(M)}\otimes I_2
}
\]

если \(S_4\)-equivariance проходит.

Измеряются:

- eigenvalues \(A_2^{(M)}\);
- multiplicity gap \(\gamma_2^{(M)}\);
- doubled-degeneracy defect;
- \([M_{22},V_{22}]\);
- overlap master-selected и volume-selected low channels.

Это actual local Euclidean constraint master, не surrogate.

**Статус: IMPLEMENTED / NUMERICAL EXECUTION ACTIVE.**

Файлы:

- \`BQG_J2_CONSTRAINT_MASTER_MULTIPLICITY.md\`
- \`scripts/bqg_j2_constraint_master_multiplicity_gate.py\`
- \`.github/workflows/bqg-j2-constraint-master.yml\`


---

# 58. Scale-free refinement control

Physical projector не меняется при

\[
M_j\to c_jM_j,\qquad c_j>0.
\]

Поэтому raw cross-scale residual зависит от arbitrary engineering normalization и не является canonical continuum diagnostic.

Для \(\rho>0\):

\[
R_\rho
=
M_{j'}\iota-\rho\,\iota M_j.
\]

Refinement-projector theorem даёт

\[
\boxed{
\|P_{j'}\iota-\iota P_j\|
\le
\frac{\|R_\rho\|}
{\min(\Delta_{j'},\rho\Delta_j)}.
}
\]

Минимизируя по \(\rho\):

\[
\boxed{
\epsilon_j^{\rm sf}
=
\inf_{\rho>0}
\frac{\|M_{j'}\iota-\rho\,\iota M_j\|}
{\min(\Delta_{j'},\rho\Delta_j)}.
}
\]

Это invariant при независимом positive rescaling обоих master operators.

**Статус: PROVED finite operator theorem.**

Файлы:

- \`BQG_SCALE_FREE_REFINEMENT_RESIDUAL_THEOREM.md\`
- \`scripts/bqg_scale_free_refinement_residual_gate.py\`

---

# 59. Canonical selected-channel intertwiner

После того как multiplicity matrix \(A_j\) nondegenerately выбирает один \([2,2]\)-channel, межмасштабный embedding не нужно fit-ить.

Для выбранных irreducible copies group-average

\[
\mathcal P_{\rm Hom}(X)
=
\frac1{24}
\sum_{g\in S_4}
U_{j'}(g)XU_j(g)^\dagger
\]

проецирует любой seed \(X\) в one-dimensional intertwiner space.

После normalization:

\[
\boxed{
\iota_{j\to j'}
=
\frac{Y}{\sqrt{\alpha}},
\qquad
Y^\dagger Y=\alpha I.
}
\]

Получаем

\[
\boxed{
\iota^\dagger\iota=I,
\qquad
U_{j'}(g)\iota=\iota U_j(g).
}
\]

Intertwiner unique up to overall phase, которая не влияет на projector-distance norms.

**Статус: PROVED finite representation theorem.**

Файлы:

- \`BQG_CANONICAL_SELECTED_CHANNEL_INTERTWINER_THEOREM.md\`
- \`scripts/bqg_canonical_selected_channel_intertwiner_gate.py\`

---

# 60. Serial multiplicity-master RG scan

Запущен первый серийный calculation на

\[
j=2,\frac52,3,\frac72,4.
\]

На каждом scale используется один и тот же production operator

\[
C_0=H_{E,0}^{\rm sine},
\qquad
M_j^{\rm tw}
=
\mathcal T_{S_4}(C_0^\dagger C_0).
\]

Из

\[
P_{22}^{(j)}M_j^{\rm tw}P_{22}^{(j)}
=
A_j\otimes I_2
\]

извлекаются:

- \(m_{22}(j)\);
- spectrum \(A_j\);
- lowest-channel isolation gap \(\gamma_j\);
- pair-degeneracy defect;
- raw/twirled covariance diagnostics.

Это первая последовательность данных, необходимая для построения

\[
\eta_j,\qquad
\iota_j,\qquad
\epsilon_j^{\rm sf}.
\]

Файлы:

- \`BQG_SERIAL_MULTIPLICITY_MASTER_SCAN.md\`
- \`scripts/bqg_serial_multiplicity_master_scan.py\`
- \`.github/workflows/bqg-serial-multiplicity-master.yml\`

**Статус: IMPLEMENTED / NUMERICAL EXECUTION ACTIVE.**


---

# 61. Five-scale multiplicity-master RG result

На пяти consecutive representation scales

\[
j=2,\frac52,3,\frac72,4
\]

один и тот же production Peter-Weyl Euclidean constraint

\[
C_0=H_{E,0}^{\rm sine}
\]

был использован для построения exact \(S_4\)-twirled local master

\[
M_j^{\rm tw}
=
\mathcal T_{S_4}(C_0^\dagger C_0).
\]

На \([2,2]\)-isotypic sector:

\[
P_{22}^{(j)}M_j^{\rm tw}P_{22}^{(j)}
=
A_j\otimes I_2.
\]

Получено:

| \(j\) | \(m_{22}\) | \(\operatorname{spec}A_j\) | \(\gamma_j\) |
|---:|---:|---|---:|
| \(2\) | 2 | \(5.067680982954,\ 5.807713077901\) | \(0.740032094948\) |
| \(5/2\) | 2 | \(5.769201915254,\ 22.499018693032\) | \(16.729816777778\) |
| \(3\) | 2 | \(9.001223358412,\ 10.264684071156\) | \(1.263460712743\) |
| \(7/2\) | 3 | \(7.140843485222,\ 9.459669912782,\ 36.381268968404\) | \(2.318826427560\) |
| \(4\) | 3 | \(7.819342874141,\ 14.040428696350,\ 16.140265919741\) | \(6.221085822210\) |

На всех tested scales:

\[
\boxed{\gamma_j>0.}
\]

То есть lowest master-selected multiplicity channel остаётся isolated.

Gap nonmonotonic, поэтому monotone convergence law пока не выводится.

**Статус: FINITE PASS.**

Файлы:

- \`BQG_SERIAL_MULTIPLICITY_MASTER_RESULT.md\`
- \`scripts/bqg_serial_multiplicity_master_scan.py\`
- \`.github/workflows/bqg-multiplicity-master-shards.yml\`

---

# 62. NO-GO для direct spin refinement и binary-ancilla theorem

Для inequivalent SU(2) irreps:

\[
\boxed{
\mathrm{Hom}_{SU(2)}(V_j,V_{j+1/2})=0.
}
\]

Следовательно прямой equivariant refinement

\[
V_j\to V_{j+1/2}
\]

невозможен.

Но после добавления нового q=2 strand:

\[
V_j\otimes V_{1/2}
=
V_{j+1/2}\oplus V_{j-1/2}.
\]

Высокоспиновый symmetric channel multiplicity-one, поэтому edge blocking

\[
\boxed{
V_j\otimes V_{1/2}^{\rm new}
\to
V_{j+1/2}
}
\]

unique up to phase.

**Статус: PROVED.**

Файлы:

- \`BQG_ANCILLA_PETER_WEYL_REFINEMENT_THEOREM.md\`
- \`scripts/bqg_ancilla_peter_weyl_refinement_gate.py\`

---

# 63. Pure-ancilla refinement NO-GO и exact bilinear refinement tensor

Четыре fresh edge ancillas после Gauss reduction сами образуют

\[
[2,2]_{\rm anc}.
\]

В этом representation нет invariant vector:

\[
\boxed{
\dim [2,2]^{S_4}=0.
}
\]

Поэтому fixed pure ancilla singlet не может породить canonical \(S_4\)-equivariant linear refinement map.

Finite gate дал reconstruction error \(=1\).

**Статус: NO-GO.**

Правильный microscopic object:

\[
\boxed{
[2,2]_{\rm old}
\otimes
[2,2]_{\rm anc}
\to
[2,2]_{\rm coarse}.
}
\]

Product decomposition:

\[
\boxed{
[2,2]\otimes[2,2]
=
[4]\oplus[2,2]\oplus[1^4].
}
\]

Microscopic blocking gate даёт:

\[
\text{covariance error}
\approx
9.996\times10^{-16},
\]

\[
\operatorname{rank}F=2,
\]

\[
\sigma_1=\sigma_2=\frac1{\sqrt2},
\]

и exact projector identities:

\[
\boxed{
2F^\dagger F
=
P_{22}^{\rm old\otimes anc}
}
\]

с error

\[
1.78\times10^{-15},
\]

\[
\boxed{
2FF^\dagger
=
P_{22}^{\rm coarse}
}
\]

с error

\[
2.44\times10^{-15}.
\]

Следовательно

\[
\boxed{
\sqrt2\,F
}
\]

является unitary identification единственного \([2,2]\) fusion channel между
old+binary-ancilla и coarse geometry.

**Статус: PROVED / FINITE exact-regression PASS.**

Файлы:

- \`BQG_MICROSCOPIC_NODE_REFINEMENT.md\`
- \`BQG_MICROSCOPIC_BILINEAR_REFINEMENT_THEOREM.md\`
- \`scripts/bqg_microscopic_bilinear_refinement_gate.py\`

---

# 64. Correct graph-changing refinement architecture

Для настоящего constraint refinement одного base map недостаточно.

Нужны:

\[
\iota_0:
\mathcal H_f^{(0)}
\to
\mathcal H_c^{(0)}
\]

и

\[
\iota_1:
\mathcal H_f^{(1)}
\to
\mathcal H_c^{(1)}
\]

на one-hit graph/spin-changed habitat.

Forward residual:

\[
E_a
=
C_{c,a}\iota_0-\iota_1C_{f,a}.
\]

Return residual:

\[
F_a
=
C_{c,a}^\dagger\iota_1-\iota_0C_{f,a}^\dagger.
\]

Exact:

\[
\boxed{
M_c\iota_0-\iota_0M_f
=
\sum_a
\left(
C_{c,a}^\dagger E_a+F_aC_{f,a}
\right).
}
\]

Поэтому:

\[
\boxed{
\|R\|
\le
\sum_a
\left(
\|C_{c,a}\|\|E_a\|
+
\|F_a\|\|C_{f,a}\|
\right).
}
\]

Это позволяет получать master-refinement bound из one-hit constraint calculations.

**Статус: PROVED.**

Файлы:

- \`BQG_CONSTRAINT_LEVEL_REFINEMENT_BOUND.md\`
- \`BQG_TWO_SIDED_HABITAT_REFINEMENT_THEOREM.md\`
- \`scripts/bqg_constraint_level_refinement_bound_gate.py\`
- \`scripts/bqg_two_sided_habitat_refinement_gate.py\`

---

# 65. Cross-scale multiplicity trajectory

Target isotypic sector:

\[
\mathcal H_{22}^{(j')}
\simeq
\mathbb C^{m_{22}(j')}
\otimes
V_{[2,2]}.
\]

Любой equivariant microscopic refinement из одного \([2,2]\) fusion channel имеет вид

\[
\boxed{
F_j=v_j\otimes I_2.
}
\]

Master-selected copy задаётся multiplicity vector \(u_{j'}\).

Поэтому canonical cross-scale overlap:

\[
\boxed{
\mathcal F_j
=
|\langle u_{j'},v_j\rangle|^2
=
\frac12
\operatorname{Tr}
(P_{j'}^{\rm block}P_{j'}^{\rm master}).
}
\]

И channel mismatch:

\[
\boxed{
\chi_j
=
\sqrt{1-\mathcal F_j}
=
\|P_{j'}^{\rm block}-P_{j'}^{\rm master}\|_2.
}
\]

Это превращает representation RG в trajectory of lines в малых multiplicity spaces.

**Статус theorem: PROVED.**

Numerical \(\mathcal F_j\) для пар

\[
2\to2.5,\quad2.5\to3,\quad3\to3.5,\quad3.5\to4
\]

вычисляются отдельным cross-scale gate.

Файлы:

- \`BQG_MULTIPLICITY_VECTOR_TRAJECTORY_THEOREM.md\`
- \`BQG_CROSS_SCALE_CHANNEL_OVERLAP.md\`
- \`scripts/bqg_cross_scale_channel_overlap_gate.py\`
