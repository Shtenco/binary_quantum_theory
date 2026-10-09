# BQG multiplicity-vector RG trajectory theorem

Status: **PROVED finite representation theorem.**

Let the target \(S_4[2,2]\)-isotypic sector be

\[
\mathcal H_{22}^{(j')}
\simeq
\mathbb C^{m_{j'}}\otimes V_{[2,2]}.
\]

Let the source microscopic fusion channel be one irreducible copy

\[
V_{[2,2]}^{\rm src}.
\]

Any \(S_4\)-equivariant linear map

\[
F:
V_{[2,2]}^{\rm src}
\to
\mathbb C^{m_{j'}}\otimes V_{[2,2]}
\]

has the form

\[
\boxed{
F=v\otimes I_{[2,2]}
}
\]

up to the fixed identification of the equivalent irreducible representations,
for a unique multiplicity vector

\[
v\in\mathbb C^{m_{j'}}.
\]

This follows because

\[
\mathrm{Hom}_{S_4}
\left(
V_{[2,2]},
\mathbb C^{m}\otimes V_{[2,2]}
\right)
\simeq
\mathbb C^m.
\]

Therefore the image of a nonzero refinement map is exactly one
\([2,2]\)-copy, specified by the line \(\operatorname{span}\{v\}\) in
multiplicity space.

If the master dynamics at the target scale selects normalized multiplicity
vector \(u\), then

\[
P_{\rm block}=|v_n\rangle\langle v_n|\otimes I_2,
\qquad
P_{\rm master}=|u\rangle\langle u|\otimes I_2,
\]

where \(v_n=v/\|v\|\).

Hence the normalized projector overlap is exactly

\[
\boxed{
\mathcal F
=
\frac12\operatorname{Tr}(P_{\rm block}P_{\rm master})
=
|\langle u,v_n\rangle|^2.
}
\]

The operator-norm projector distance is

\[
\boxed{
\chi
=
\|P_{\rm block}-P_{\rm master}\|_2
=
\sqrt{1-\mathcal F}.
}
\]

Thus the cross-scale representation RG is a trajectory of lines in the small
multiplicity spaces:

\[
\boxed{
v_j^{\rm block}
\quad\text{versus}\quad
u_{j+1/2}^{\rm master}.
}
\]

This is the canonical meaning of the channel-overlap column.

## Consequence

The continuum programme now has three logically distinct controls:

1. **selection gap**
   \[
   \gamma_j
   \]
   — does the master uniquely select a multiplicity line?

2. **microscopic/master channel mismatch**
   \[
   \chi_j=\sqrt{1-\mathcal F_j}
   \]
   — does binary microscopic refinement flow into the next master-selected
   line?

3. **full physical-projector residual**
   \[
   \epsilon_j^{\rm sf}
   \]
   — does the full graph-changing master/projector refine consistently?

A plausible continuum trajectory requires at minimum

\[
\gamma_j>0,
\qquad
\chi_j\to0,
\qquad
\epsilon_j^{\rm sf}\to0,
\]

with summability conditions providing the stronger inductive-limit route.

The previously introduced perturbative stability ratio

\[
\eta_j^{\rm stab}=\|\delta A_j\|/\gamma_j
\]

has a different role: it controls robustness of the selected line under
operator perturbations and must not be confused with the measured cross-scale
trajectory mismatch \(\chi_j\).
