#!/usr/bin/env python3
"""Compatibility entry point for the audited Peter-Weyl resolvent decomposition.

The former implementation scanned weights depending only on `spin_cost`. The
audited 648-state one-hit support shows that every intermediate state has the
same spin_cost=3 and exactly three changed edges, so those scans merely rescaled
the whole kernel and were not an independent robustness test.

The canonical replacement is `peter_weyl_anisotropy_resolvent_audit_gate.py`,
which hard-checks matrix reconstruction and then reports sign, volume and
representation-channel fingerprints. This file remains only so old reproduction
commands and workflows fail closed into the corrected audit rather than
resurrecting stale thresholds.
"""
from __future__ import annotations

import functools
import peter_weyl_anisotropy_resolvent_audit_gate as AUD

# Avoid recomputing local volume data for every diagnostic weighting family.
AUD.state_features = functools.lru_cache(maxsize=None)(AUD.state_features)

if __name__ == "__main__":
    raise SystemExit(AUD.main())
