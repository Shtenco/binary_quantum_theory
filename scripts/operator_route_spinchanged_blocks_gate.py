#!/usr/bin/env python3
"""Compatibility entry point for the canonical spin-changed operator-route gate.

The implementation lives in ``peter_weyl_operator_route_block_gate.py``.
This wrapper exists so historical/machine-ledger evidence paths remain stable
without duplicating any physics or acceptance logic.
"""
from peter_weyl_operator_route_block_gate import main

if __name__ == '__main__':
    raise SystemExit(main())
