"""GF180MCU devices by name, for explicit instantiation: the modules ``prim_dicts`` maps the
Hdl21 primitives onto.

    from pdk.gf180.hdl21.primitives import NFET_5P0V
    n = NFET_5P0V(Gf180MosParams(w=1 * µ, l=0.6 * µ))(d=out, g=inp, s=vss, b=vss)
"""

from .prim_dicts import caps, diodes, ress, xtors

_MOS = {key[0]: module for key, module in xtors.items()}

# 5 V core (the standard cells' devices) and 6 V I/O transistors
NFET_5P0V = _MOS["NFET_5p0V"]
PFET_5P0V = _MOS["PFET_5p0V"]
NFET_6P0V = _MOS["NFET_6p0V"]
PFET_6P0V = _MOS["PFET_6p0V"]

# the unsalicided P+ poly resistor of the row cells (layout/tech.py RES)
PPOLYF_U = ress["ppolyf_u"]

# the MIM capacitor of gf180mcuD (option B, 2 fF/um^2)
CAP_MIM_2F0 = caps["cap_mim_2f0ff"]

__all__ = ["NFET_5P0V", "PFET_5P0V", "NFET_6P0V", "PFET_6P0V", "PPOLYF_U", "CAP_MIM_2F0", "xtors", "ress", "caps", "diodes"]
