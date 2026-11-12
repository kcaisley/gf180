"""Named device exports for direct use: the modules ``prim_dicts`` maps the Hdl21 primitives onto
(``xtors["NFET_5p0V", ...]``: nfet_05v0; ``ress["ppolyf_u"]``, ``caps["cap_mim_2f0ff"]``, ...)."""

from .prim_dicts import bjts, caps, diodes, ress, stdcells, xtors

__all__ = ["xtors", "ress", "caps", "diodes", "bjts", "stdcells"]
