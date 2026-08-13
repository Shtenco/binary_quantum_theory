# Covariant K-leg projection audit

Status: **frozen after diagnosing the old branch-level FAIL and before the invariant rerun.**

## Historical full-charge run

The first complete-J implementation of

$$
C_e(K_v)=h_e[h_e^{-1},K_v],
\qquad K_v=[V_v,H_v^E],
$$

removed the earlier premature $J=1/2$ truncation.  It produced the following
full-sum results:

$$
\boxed{\Delta^{H_E}_{wrong\ charge}=0},
\qquad
\boxed{\Delta^{K}_{wrong\ charge}=0}
$$

at both charged endpoints.  Explicit full-state weights contained only
$J=1/2$:

$$
w_{H_E}(J=1/2)=0.7505314109861138,
$$

$$
w_K(J=1/2)=0.23051051967078295.
$$

The final matrix-covariant leg was nonzero,

$$
\boxed{\|C_e(K)\|=0.9724789464697686},
$$

with source representation weights

$$
\boxed{w_{J=0}=0.37805430420217057},
$$

$$
\boxed{w_{J=1}=0.5676609971247807},
$$

and exactly zero measured weight for $J>1$.

Nevertheless the run was marked FAIL because

$$
\texttt{complete\_charge\_basis\_leakage}=1.
$$

## Why that diagnostic is not an operator covariance defect

That number was the **maximum over individual fixed-holonomy-index primitive
branches**.  A primitive branch $b_r$ of the traced/orientation-summed
Hamiltonian is not separately gauge invariant.  Gauge covariance is a property
of

$$
H_E=\sum_r b_r,
$$

not of every $b_r$.

The final physical matrix element is obtained with a linear representation
projector $P$:

$$
P H_E|\psi\rangle
=P\sum_r b_r|\psi\rangle
=\sum_r P b_r|\psi\rangle.
$$

Therefore a large individual

$$
\|(1-P)b_r|\psi\rangle\|
$$

is not itself evidence for

$$
(1-P)H_E|\psi\rangle\ne0.
$$

The invariant full-sum charge weights above already show no $J\ne1/2$ component
inside the charged output representation retained by the calculation.

## New invariant regression frozen before rerun

To ensure that term-by-term projection has not changed the physical Gauss
matrix element, the rerun must add an independent **uncharged projection
regression** using the same all-$J$ internal-volume engine:

1. start from the frozen all-$j=1/2$, all-$K=0$ Gauss state;
2. evaluate the complete orientation/index/adjoint Euclidean sum using the new
   all-$J$ internal volume implementation;
3. linearly project completed primitive branches to the Gauss basis;
4. compare the resulting sparse column against the independently existing safe
   Peter--Weyl `H_E` column.

The invariant rerun passes only if

$$
\boxed{
\frac{\|H_E^{allJ/projected}-H_E^{safe}\|}
{\|H_E^{safe}\|}<10^{-9}.
}
$$

In addition the previous hard physical requirements remain frozen:

$$
\Delta^{H_E}_{wrong\ charge}<10^{-18},
\qquad
\Delta^{K}_{wrong\ charge}<10^{-18},
$$

$$
\|C_e(K)\|>0,
\qquad
w_{J=1}>10^{-14},
\qquad
w_{J>1}<10^{-18},
$$

with the existing outer-charge and internal-volume representation errors below
$10^{-10}$.

The old branch-level maximum remains reported under a diagnostic name, but it
is no longer used as a physical pass/fail criterion.  The historical FAIL is
not deleted.
