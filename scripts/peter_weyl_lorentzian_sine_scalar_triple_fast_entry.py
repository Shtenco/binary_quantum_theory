#!/usr/bin/env python3
"""Entrypoint for the research scalar-triple accelerator."""
import numpy as np
import peter_weyl_lorentzian_sine_scalar_triple_fast_gate as FAST
FAST.np = np
raise SystemExit(FAST.main())
