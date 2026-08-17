# Joint epsilon / Peter-Weyl cutoff limit

## Statement

For a finite word of fundamental holonomies, each hit changes a link spin by at most \(1/2\). Therefore an input link spin \(j_{in}\) acted on at most \(r\) times has no support above

\[
j_{in}+\frac r2.
\]

Consequently Peter-Weyl truncation is **exactly inactive** whenever

\[
J_{max}\ge j_{in}+\frac r2.
\]

This is a finite support theorem, not a fitted cutoff extrapolation.

## Euclidean three-node HH family

For the frozen all-\(j=1/2\) K5 input used by the three-node graph-changing gate, enumeration of the Euclidean HH words gives

```text
j_in                  = 1/2
maximum hits per link = 4
sufficient Jmax       = 5/2
```

Above this wall the Peter-Weyl truncation error is exactly zero for the declared finite-word family.

The measured common-habitat HDA defect from `THREE_NODE_GRAPH_HDA_RESULT.md` has

\[
\Delta_{joint}/D\sim \epsilon^{1.0064429343525387}
\]

and decreases monotonically from `0.4115150041` at \(\epsilon=1/4\) to `0.02522380790` at \(\epsilon=1/64\).

Hence, for every simultaneous path satisfying

\[
\epsilon\to0,
\qquad
J_{max}(\epsilon)\ge5/2,
\]

within this frozen finite-input Euclidean HH family, the cutoff contribution is identically zero and the measured regulator defect tends toward zero with the same fitted power.

## Lorentzian support wall

The existing conservative hit-depth analysis for the full declared Lorentzian HH word gives

```text
maximum hits per link = 12
sufficient Jmax       = 13/2
```

This is a support bound only; it does not substitute for a full three-node Lorentzian commutator evaluation.

## Status

`JOINT_FIXED_INPUT = tested_finite` is justified by the combination of an exact support theorem and the frozen numerical epsilon family.

The broader `JOINT_LIMIT` remains **open** because a refinement sequence can change the input/coarse spin and graph complexity. A uniform theorem still needs a declared growth law such as

\[
J_{max}(b)\ge j_{in}(b)+r(b)/2
\]

plus uniform control of the HDA residual, norms and habitat as \(b\) and graph size grow.
