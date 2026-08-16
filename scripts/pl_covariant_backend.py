#!/usr/bin/env python3
"""Temporary graph-backend adapter for the validated covariant Peter-Weyl stack.

The charged/all-J recoupling algebra is local SU(2) representation theory.  Its
historical implementation imports graph primitives from the K5 module.  This
adapter swaps only those graph-regulator primitives for a
PLPeterWeylEuclidean instance while leaving CG coefficients, charged tensors,
all-J volume blocks and covariant projection code untouched.

It is a context manager: all historical K5 globals are restored on exit.
"""
from __future__ import annotations
from contextlib import contextmanager
import k5_peter_weyl_safe_hda_column as PW

GRAPH_NAMES=(
    'VERT','NEIG','local_spins','oriented_intertwiner','apply_hit_branch',
    'apply_path_branch','initial_factorized_oriented','oriented_specs',
    'T_sequences','adjoint_sequence'
)

@contextmanager
def install_pl_graph(G):
    saved={name:getattr(PW,name) for name in GRAPH_NAMES}
    try:
        PW.VERT=G.VERT
        PW.NEIG=tuple(tuple(G.dual.neighbor[(v,r)] for r in range(4)) for v in G.VERT)
        PW.local_spins=G.local_spins
        PW.oriented_intertwiner=G.oriented_intertwiner
        PW.apply_hit_branch=G.apply_hit_branch
        PW.apply_path_branch=G.apply_path_branch
        PW.initial_factorized_oriented=G.initial_factorized_oriented
        PW.oriented_specs=G.oriented_specs
        PW.T_sequences=G.T_sequences
        PW.adjoint_sequence=G.adjoint_sequence
        yield
    finally:
        for name,value in saved.items():setattr(PW,name,value)

@contextmanager
def install_pl_sine_covariant_K(G):
    """Install the PL graph and physical-sine H_E inside generalized C(K)."""
    import peter_weyl_covariant_K_leg_gate as CK
    import peter_weyl_covariant_K_sine_composition_gate as SCK
    old_he=CK.apply_HE_complete_key
    with install_pl_graph(G):
        try:
            CK.apply_HE_complete_key=SCK.complete_HE_sine
            if hasattr(CK.HE_complete_cached,'cache_clear'):CK.HE_complete_cached.cache_clear()
            yield
        finally:
            CK.apply_HE_complete_key=old_he
            if hasattr(CK.HE_complete_cached,'cache_clear'):CK.HE_complete_cached.cache_clear()
