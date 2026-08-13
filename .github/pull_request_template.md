## Research claim checklist

- [ ] This branch is based on or explicitly compared against the current `main`.
- [ ] I did not overwrite a newer `THEORY_STATUS.md` or `theory_gates.json` with an older generated version.
- [ ] Any changed scientific claim is reflected in `THEORY_STATUS.md`.
- [ ] The matching gate in `theory_gates.json` is updated.
- [ ] Evidence files/scripts referenced by the gate exist and reproduce the stated finite result.
- [ ] Negative results and preregistered FAILs are preserved.
- [ ] `tested_finite` / `conditional` claims were not promoted to `proved` without a proof.
- [ ] Canonical real-SU(2) and covariant BF/spinfoam routes are not silently mixed.
- [ ] Any HDA claim compares against a declared nontrivial diffeomorphism action, not only fixed-sector leakage or group-averaged zero.
- [ ] `python scripts/verify_theory_gates.py` passes.
- [ ] Core regression / CI passes.

## What changed

Describe the mathematical/physical change and its scope.

## Falsifier / negative control

State what result would reject or downgrade this change.

## Evidence

List exact scripts, reports and preregistered targets used by this PR.
