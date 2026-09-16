# BQG 2T Frontier — новый физический frontier

**Обновление: 16 сентября 2026**  
**Статус: OPEN / falsification program.**

Это расширение канонического README посвящено вопросу, который появился после сопоставления BQG с Two-Time Physics (2T): может ли существующая relational-history структура BQG быть не просто внутренним clock, а тенью более глубокой двухвременной constrained theory?

> **Ключевой принцип:** мы не объявляем BQG двухвременной теорией. Мы строим тест, который может как подтвердить, так и опровергнуть такую интерпретацию.

## 1. Что уже есть в BQG

Текущая теория уже содержит:

```text
binary microstructure
        ↓
q=2 geometry
        ↓
3D spatial fixed point
        ↓
quantum geometry
        ↓
constraint dynamics
        ↓
relational history
        ↓
ADM/HDA target
        ↓
TT spin-2 sector
```

В relational-history control используется

```text
G = S_clock ⊗ R_geom
P_rel = (1/8) Σ_{τ=0}^{7} G^τ
```

и условная эволюция

```text
|ψ(t)⟩ = R^t |ψ0⟩.
```

Это пока **не** доказательство второго времени. Это только достаточная структура, чтобы сформулировать строгий следующий тест.

## 2. Что означает «два времени» в строгом смысле

Необходимо различать:

```text
A. второй индекс истории
B. второй канонический clock
C. второе evolution-подобное направление
D. Sp(2,R)-тип gauge symmetry
E. настоящий metric signature (d,2)
```

Для настоящей 2T-интерпретации нужны как минимум D + E, а затем ghost-free gauge reduction к одной физической временной координате.

## 3. Почему здесь появляется Sp(2,R)

В Bars 2T Physics parent system живёт в `d+2` измерениях и обладает `Sp(2,R)` gauge symmetry в фазовом пространстве. Канонический constraint fingerprint имеет вид

```text
Q11 ~ X·X
Q12 ~ X·P
Q22 ~ P·P
```

с замыканием в `sp(2,R)`.

Разные gauge choices могут давать разные one-time «shadows». Поэтому для BQG важен не сам факт наличия второго параметра, а существование constrained parent theory, из которой 3+1 BQG получается как gauge-reduced sector.

## 4. Новый главный вопрос BQG

```text
Can Binary Quantum Gravity be a 2T-reduction
of its own microscopic binary theory?
```

То есть:

```text
binary microstructure
        ↓
relational history
        ↓
parent constrained phase space
        ↓
possible Sp(2,R)
        ↓
possible (3+2) parent signature
        ↓
gauge reduction
        ↓
3+1 BQG
        ↓
HDA / GR
```

Это теперь отдельный falsifiable branch теории.

## 5. Главный gate

Нужно взять **реальные** BQG constraints и искать три независимые комбинации

```text
C1, C2, C3
```

с закрытой алгеброй типа

```text
{C1,C2} ~ C3
{C2,C3} ~ C1
{C3,C1} ~ C2
```

с точными коэффициентами, которые после выбора нормировки совпадают с `sp(2,R)`.

Запрещено просто ввести `Q11,Q12,Q22` вручную.

Подробный протокол находится в [`BQG_2T_ALGEBRA_GATE.md`](BQG_2T_ALGEBRA_GATE.md).

## 6. Что будет считаться настоящим результатом

### PASS

```text
exact/controlled 3-generator first-class algebra
          +
independent canonical clock pair(s)
          +
(d,2) kinetic signature
          +
ghost-free gauge reduction
          +
3+1 BQG/HDA recovery
```

Тогда появляется серьёзное основание говорить о genuine BQG 2T embedding.

### PARTIAL PASS

Если найден `sp(2,R)`-подобный algebraic sector, но нет второй timelike metric direction, корректная формулировка будет:

> **hidden phase-space duality / 2T-like algebra**

а не «доказано два времени».

### NO-GO

Если три независимых first-class генератора не существуют, либо closure появляется только после подгонки параметров, BQG не проходит Bars-type 2T gate в исследованной реализации.

Это будет нормальным научным результатом.

## 7. Что нельзя использовать как доказательство

Не являются достаточными сами по себе:

- `d_s^history ≈ 4`;
- наличие clock register;
- конечный циклический projector;
- дополнительный индекс `τ`;
- высокая размерность Hilbert space;
- визуальная аналогия с `(3+2)`;
- совпадение нескольких чисел с 2T-моделью.

Особенно важно: `d_history ≈ 4` может означать пространственные 3 измерения плюс один параметр истории и не доказывает вторую timelike coordinate.

## 8. Следующий computational experiment

Минимальный тест:

```text
1. enumerate actual BQG constraints
2. construct finite matrices
3. find independent 3D candidate constraint sectors
4. compute exact commutator closure
5. test Jacobi
6. test first-class preservation
7. reconstruct canonical X,P if possible
8. test kinetic signature
9. gauge-fix one time
10. compare reduced evolution with P_rel
```

Главный output:

```text
closure residual
Jacobi residual
rank(C)
canonical-pair reconstruction error
signature
ghost count
reduced-Hamiltonian mismatch
HDA mismatch
```

## 9. Relation to existing BQG bottleneck

Это не отдельная красивая надстройка. 2T-gate должен атаковать именно текущий физический bottleneck:

```text
PHYSICAL PROJECTOR / RELATIONAL HISTORY
                    ↓
             physical constraint
                    ↓
              Z[J] / Γ[g]
                    ↓
             Γ^(2)_TT
                    ↓
             six Wilson coefficients
```

Если 2T parent существует, relational history может получить более глубокий constrained interpretation. Если нет — BQG остаётся one-time relational quantum-gravity construction.

## 10. Canonical status

На 16 сентября 2026:

```text
BQG spatial/geometric chain                 : existing declared results
relational history control                  : existing control construction
physical graph-changing history generator   : OPEN
physical projector / rigging map             : OPEN
Sp(2,R) BQG embedding                       : UNTESTED
(d,2) parent metric                         : UNTESTED
ghost-free 2T → 1T reduction                : UNTESTED
Schwarzschild parent/shadow test             : FUTURE
experimental two-time signature              : NO CLAIM
```

### Scientific rule

**Сначала algebra. Потом signature. Потом gauge reduction. Потом gravity. Только после этого — физическая интерпретация.**

