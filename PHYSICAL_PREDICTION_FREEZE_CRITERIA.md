# Physical prediction freeze criteria

`PHYS_PRED` remains open. This file prevents internal controls or selection targets from being relabelled as blind predictions.

A physical observable may be frozen only after all items below are satisfied.

## Forbidden as first blind predictions

The following quantities are **selection-tainted or oracle-tainted** and therefore cannot be used as the first external blind success:

- spatial dimension near 3, because dimension entered the q-selection protocol;
- dynamical exponent near 1 / relativistic scaling, because z entered the q-selection protocol;
- 4D-like history scaling derived from the selected q=2 rule;
- the `Lambda=3` S4 reconstruction, because the S4 geometry is an oracle positive control;
- any constant obtained by fitting the same external value that is later advertised as a prediction.

## Required pre-freeze fields

Before experimental data are opened, commit one machine-readable preregistration containing:

```text
observable_id
physical definition and units
microscopic estimator
single common scale-setting map
all model parameters and their provenance
allowed calibration observables
forbidden fitting operations
numerical implementation/version
predeclared numerical and model-systematic uncertainty
accept/reject rule
identity/hash of the held-out external dataset
```

## Upstream blockers

The first blind dimensional prediction additionally requires:

1. a reproducible physical scale map from dimensionless microscopic quantities to length/time/energy units;
2. no per-observable rescaling;
3. a target observable not used in q/rule selection or continuum normalization;
4. sufficient theoretical and experimental precision to make the predicted deviation falsifiable;
5. an independent implementation or cross-check for the estimator.

Until these conditions are met, `PHYS_PRED` stays `open` even if an internal held-out numerical extrapolation agrees at sub-percent level.

## Purpose

The purpose is to make the eventual comparison genuinely dangerous to the model: after the prediction file is frozen, a disagreement outside the predeclared uncertainty must count as a failure rather than trigger parameter retuning.
