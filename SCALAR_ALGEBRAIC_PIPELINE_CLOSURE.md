# Scalar algebraic pipeline closure

Status: **CLOSED algebraic consumer pipeline; theory-specific connected physical history remains OPEN_PHYSICAL.**

This note freezes the strongest scalar statement currently supported by the repository after the exact ADM/Dirac reduction, scalar Ward quotient, universal conserved test-probe convention, connected-history Legendre extractor and response/pole classifier were composed and independently CI-certified.

## 1. Closed deterministic chain

On the flat/local scalar Ward quotient define the two gauge-invariant source coordinates

\[
\mathcal Q=\delta N+\partial_t B-\partial_t^2E,
\qquad
\zeta.
\]

The exact Ward-compatible scalar Hessian is completely parameterized by three functions,

\[
\Gamma^{(2)}_{\rm scalar}
\equiv
H(\omega,k)
=
\begin{pmatrix}
A&B\\
B&C
\end{pmatrix},
\]

rather than ten arbitrary symmetric ADM entries.

For a nonsingular physical connected source Hessian

\[
G_{\rm conn}
=
\begin{pmatrix}
G_{QQ}&G_{Q\zeta}\\
G_{Q\zeta}&G_{\zeta\zeta}
\end{pmatrix},
\]

the Legendre-Hessian relation gives exactly

\[
\boxed{\Gamma^{(2)}_{\rm scalar}=G_{\rm conn}^{-1}}.
\]

Thus, with

\[
D_G=G_{QQ}G_{\zeta\zeta}-G_{Q\zeta}^2,
\]

\[
\boxed{
A=\frac{G_{\zeta\zeta}}{D_G},\qquad
B=-\frac{G_{Q\zeta}}{D_G},\qquad
C=\frac{G_{QQ}}{D_G}.
}
\]

The common scalar response denominator is

\[
\boxed{\Delta=AC-B^2}.
\]

With the one frozen conserved external probe convention, the same kernel determines the Newtonian-gauge response variables and therefore dynamics and lensing from one source normalization. The response classifier then determines whether the reduced kernel has no physical scalar pole or has an extra pole and, if present, evaluates residue, ghost/tachyon diagnostics, mass squared and effective sound speed.

The executable closed chain is therefore

```text
G_QQ, G_Qzeta, G_zetazeta
 -> exact Legendre inverse
 -> A, B, C
 -> Delta = A*C-B^2
 -> Psi, Phi from one conserved source
 -> omega^2 poles
 -> residue / ghost / tachyon / m^2 / c_s^2
```

## 2. Fail-closed singular case

If

\[
D_G=0,
\]

the source Hessian still contains a null/constraint direction or otherwise needs further reduction. The production extractor returns `REDUCE_FURTHER` and does **not** apply a Moore--Penrose pseudoinverse to manufacture a scalar pole.

Likewise no physical interpretation is emitted unless the packet certifies all of:

- one theory-specific connected physical history;
- disconnected vacuum pieces removed through the connected generating functional;
- physical frequency derived from physical history/boundary time rather than a constraint spectral coordinate;
- Ward source basis certified;
- Legendre-Hessian convention certified;
- the frozen conserved source convention and background/scale convention.

## 3. Exact remaining microscopic input

The unresolved scalar microscopic object is no longer an unspecified ADM matrix and is no longer an unspecified set of functions `A,B,C`.

It is exactly

\[
\boxed{
G_{QQ}(\omega,k),\qquad
G_{Q\zeta}(\omega,k),\qquad
G_{\zeta\zeta}(\omega,k)
}
\]

computed from the **theory-specific physical connected history**.

These three functions must arise from derivatives of the physical connected functional `W_phys[J]`, not from raw constraint moments, a Feshbach resolvent, a local normalized trace, or a fitted phenomenological response.

## 4. CI evidence

Dedicated workflow:

```text
.github/workflows/scalar-connected-history-closure.yml
```

Independent successful closure run:

```text
GitHub Actions run 33986178474
head 3ab90f63b497ae9eb80e4c26708b9648d7b26898
```

The run passed:

- connected-history Legendre extractor;
- singular-source fail-closed control;
- end-to-end `G_conn -> A,B,C -> response` composition;
- independent scalar response/pole classifier;
- final closure assertion.

The healthy synthetic control reconstructs a single pole with

\[
m^2=2,\qquad c_s^2=\frac14,
\]

positive nonzero residue and no tachyon. This is an implementation control only, **not a BQG prediction**.

The canonical scalar truth workflow also passed after the consumer pipeline was marked frozen:

```text
GitHub Actions run 33986268369
head 6e7afb9ed35409d8fef860478ea31dbce414cc81
```

It simultaneously verifies that `Phi`, `Psi`, `mu_BQG`, `Sigma_BQG`, `rho_hist` and the theory-specific scalar kernel remain `OPEN_PHYSICAL` until the actual connected history is supplied.

## 5. Frozen status

The precise status is

\[
\boxed{\textbf{SCALAR ALGEBRAIC CONSUMER PIPELINE = CLOSED}}
\]

and simultaneously

\[
\boxed{\textbf{THEORY-SPECIFIC CONNECTED SCALAR HISTORY = OPEN\_PHYSICAL}}.
\]

Therefore

```text
SCALAR_CONNECTED_HISTORY_TO_RESPONSE_PIPELINE = frozen
CONNECTED_SCALAR_INTERBLOCK_HISTORY          = open_physical
PHYSICAL_BQG_SCALAR_KERNEL                    = open_physical
PHYSICAL_SCALAR_COSMOLOGY                     = open_physical
```

## 6. Forbidden regressions

Do not:

- return to an unreduced four-variable ADM Hessian as if the Ward quotient had not been derived;
- treat `A,B,C` as new fit functions;
- pseudoinvert a singular connected source Hessian;
- rename constraint `z` as physical `omega`;
- use different source normalizations for dynamics and lensing;
- call a synthetic pole dark matter;
- infer dark energy from a normalized local trace or `W(0)=0`;
- mark the BQG scalar kernel frozen before the three connected physical cumulants are actually computed.

The next physical computation is uniquely defined: obtain the three connected Ward-source cumulants from one source-dressed BQG physical history and feed them into the already-closed consumer chain.
