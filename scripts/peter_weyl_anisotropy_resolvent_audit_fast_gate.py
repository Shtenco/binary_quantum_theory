#!/usr/bin/env python3
"""Memoized runner for peter_weyl_anisotropy_resolvent_audit_gate.

The underlying gate is unchanged. This wrapper memoizes the deterministic
state_features(key) calculation so local Peter-Weyl volumes are evaluated once
per intermediate state rather than once per diagnostic weight scan.
"""
from __future__ import annotations

import functools
import peter_weyl_anisotropy_resolvent_audit_gate as AUD

AUD.state_features = functools.lru_cache(maxsize=None)(AUD.state_features)

if __name__ == "__main__":
    raise SystemExit(AUD.main())
