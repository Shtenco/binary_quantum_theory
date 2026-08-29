# Bell/CHSH q=2 reference control

Status: **standard-QM reference control, not a BCQG dynamics theorem and not an experimental Bell test**.

## Purpose

The repository already contains a finite two-qubit realization of its SU(2) quantum-link algebra in `scripts/su2_quantum_link_two_qubit_gate.py`. The Bell/CHSH control reuses that file's exact Pauli convention and asks a deliberately narrower question:

> Does the two-qubit tensor-product carrier, with the same Pauli basis/sign convention used by the repository, reproduce the exact kinematic identities of ordinary spin-1/2 quantum mechanics?

This is a useful cross-check because sign, tensor-ordering, basis and Hermiticity errors can survive simpler dimension/Casimir tests.

## Reference state and observables

The control uses the normalized singlet

$$
|\psi^-\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}
$$

and unit-vector spin observables

$$
A(\mathbf n)=\mathbf n\cdot\boldsymbol\sigma.
$$

The Pauli matrices are imported from the repository SU(2) gate rather than redefined independently.

The inherited algebra must satisfy

$$
[\sigma_i,\sigma_j]=2i\epsilon_{ijk}\sigma_k,
\qquad
\{\sigma_i,\sigma_j\}=2\delta_{ij}I.
$$

## Singlet invariants

The control verifies

$$
(\sigma_i\otimes I+I\otimes\sigma_i)|\psi^-\rangle=0,
$$

and therefore checks finite common rotations numerically through

$$
(U\otimes U)|\psi^-\rangle=|\psi^-\rangle,
\qquad U\in SU(2).
$$

Its full correlation tensor is required to be

$$
T_{ij}=\langle\psi^-|\sigma_i\otimes\sigma_j|\psi^-\rangle=-\delta_{ij},
$$

which implies for arbitrary unit directions

$$
E(\mathbf a,\mathbf b)=-\mathbf a\cdot\mathbf b.
$$

The implementation checks this both on the Cartesian basis and on a frozen deterministic sample of random directions.

## CHSH and Tsirelson control

For

$$
\mathcal B=
A\otimes B+A\otimes B'
+A'\otimes B-A'\otimes B',
$$

the local-hidden-variable reference bound is

$$
|S|\le2,
$$

while quantum spin-1/2 observables obey the Tsirelson bound

$$
\|\mathcal B\|\le2\sqrt2.
$$

The frozen optimal singlet settings must attain

$$
|\langle\mathcal B\rangle|=2\sqrt2.
$$

The gate also checks the operator identity

$$
\mathcal B^2=4I-[A,A']\otimes[B,B']
$$

for the declared sign convention, the optimal spectrum

$$
\{-2\sqrt2,0,0,2\sqrt2\},
$$

and the two-qubit Horodecki criterion

$$
S_{\max}=2\sqrt{m_1+m_2},
$$

where $m_1,m_2$ are the two largest eigenvalues of $T^TT$.

## Claim boundary

Passing this control establishes only consistency with standard two-qubit Hilbert-space kinematics under the repository's Pauli convention.

It does **not** establish any of the following:

- that the two Bell tensor factors are physically separated BCQG subsystems;
- that the BCQG microscopic dynamics prepares the singlet;
- that the Born rule or measurement locality has been derived from the binary model;
- that Bell nonlocality has been derived from the gravity construction;
- that the theory has passed an experimental Bell test;
- that the GR/HDA continuum sector is correct.

This distinction matters because the four active q=2 labels and the endpoint $SU(2)_L\times SU(2)_R$ representation have their own representation-theoretic bridge. A standard Bell singlet on a two-qubit tensor product must not be silently identified with that endpoint structure without an additional physical subsystem/state-preparation derivation.

## CI isolation

The reference is intentionally run in `.github/workflows/q2-bell-reference.yml`, separate from `core-regression.yml`.

Therefore:

```text
Bell reference GREEN  != proof of BCQG gravity
Bell reference RED    = inconsistency in the declared two-qubit/SU(2) reference layer
core-regression GREEN = unchanged canonical gravity-candidate regression status
```

The separation prevents a standard-QM identity from artificially strengthening the scientific status of the gravity core while still making convention drift immediately visible.
