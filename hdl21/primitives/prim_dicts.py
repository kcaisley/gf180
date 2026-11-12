"""Device dictionaries for the GF180MCU PDK: Hdl21 primitive parameters to the PDK's devices.

MOS: the 3.3 V devices are the core (MosFamily.CORE), the ones the gf180mcu_osu_sc_gp9t3v3 standard
cells are made of and the row cells draw (layout/tech.py MODELS), by the package's names (nfet_3v3,
pfet_3v3: pdk_data); the 5 V devices (Dualgate, V5_XTOR) are the I/O family, which the rows do not
draw. The 6 V devices are left out (Spectre cannot call them by name either, and the kit gives them
no role). The kit has one threshold: LOW and HIGH requests take it.
"""

from dataclasses import dataclass, field

import hdl21 as h
from hdl21.prefix import µ
from hdl21.primitives import (
    BipolarParams,
    DiodeParams,
    MosFamily,
    MosParams,
    MosType,
    MosVth,
    PhysicalCapacitorParams,
    PhysicalResistorParams,
)

from ..pdk_data import cap_module, diode_module, res_module, xtor_module

# MOS key: (name, MosType, MosVth, MosFamily)
MosKey = tuple[str, MosType, MosVth, MosFamily]

xtors: dict[MosKey, h.ExternalModule] = {
    # 3.3 V core: the standard cells' devices, L >= 0.28 um (PL.2_LV), the decks' nfet_03v3, pfet_03v3
    ("NFET_3p3V", MosType.NMOS, MosVth.STD, MosFamily.CORE): xtor_module("nfet_3v3"),
    ("PFET_3p3V", MosType.PMOS, MosVth.STD, MosFamily.CORE): xtor_module("pfet_3v3"),
    # 5 V I/O (Dualgate, V5_XTOR), L >= 0.6 um (N), 0.5 um (P)
    ("NFET_5p0V", MosType.NMOS, MosVth.STD, MosFamily.IO): xtor_module("nfet_05v0"),
    ("PFET_5p0V", MosType.PMOS, MosVth.STD, MosFamily.IO): xtor_module("pfet_05v0"),
}

# Resistors: three terminals (p, n, and the bulk under the body). ppolyf_u is the row cells'
# (layout/tech.py RES: unsalicided P+ poly, 350 ohm/sq)
ress: dict[str, h.ExternalModule] = {
    name: res_module(name)
    for name in (
        "ppolyf_u",
        "npolyf_u",
        "ppolyf_s",
        "npolyf_s",
        "ppolyf_u_1k",
        "ppolyf_u_2k",
        "ppolyf_u_3k",
        "ppolyf_u_1k_6p0",
        "ppolyf_u_2k_6p0",
        "nplus_u",
        "pplus_u",
        "nplus_s",
        "pplus_s",
        "nwell",
    )
}

# Capacitors: MIM (option B, gf180mcuD: 1.0, 1.5 and 2.0 fF/um^2), MOS (accumulation, in their
# wells; "_b": the inverted-well variants)
caps: dict[str, h.ExternalModule] = {
    name: cap_module(name)
    for name in (
        "cap_mim_1f0ff",
        "cap_mim_1f5ff",
        "cap_mim_2f0ff",
        "cap_nmos_03v3",
        "cap_pmos_03v3",
        "cap_nmos_03v3_b",
        "cap_pmos_03v3_b",
        "cap_nmos_06v0",
        "cap_pmos_06v0",
        "cap_nmos_06v0_b",
        "cap_pmos_06v0_b",
    )
}

# Junction diodes: model cards (D elements, area and perimeter)
diodes: dict[str, h.ExternalModule] = {
    name: diode_module(name)
    for name in (
        "diode_nd2ps_03v3",
        "diode_pd2nw_03v3",
        "diode_nw2ps_03v3",
        "diode_nd2ps_06v0",
        "diode_pd2nw_06v0",
        "diode_nw2ps_06v0",
        "diode_pw2dw",
        "diode_dw2ps",
    )
}

# not wrapped by this package: the PDK's BJTs (npn_*, pnp_*); the standard cells are hdl21/cells.py
bjts: dict[str, h.ExternalModule] = {}
stdcells: dict[str, h.ExternalModule] = {}

# MOS: (width, length) per model; generic sizes are multiples of these. Each device's narrowest
# COMP (DF.1a_LV 0.22, DF.1a_MV 0.3 um) and its shortest gate (PL.2_LV 0.28; PL.2_MV 0.6 / 0.5 um):
# frida's unit is the shortest of these (flow.circuit.devices.core_unit), the core pair's
default_xtor_size: dict[str, tuple[h.Prefixed, h.Prefixed]] = {
    "nfet_3v3": (0.22 * µ, 0.28 * µ),
    "pfet_3v3": (0.22 * µ, 0.28 * µ),
    "nfet_05v0": (0.3 * µ, 0.6 * µ),
    "pfet_05v0": (0.3 * µ, 0.5 * µ),
}

# Resistors: (width, length); the poly resistors' narrowest body (PRES.1, LRES.1), the others' 1 um
default_res_size: dict[str, tuple[h.Prefixed, h.Prefixed]] = {
    name: ((0.8 * µ, 2 * µ) if "poly" in name else (1 * µ, 1 * µ)) for name in ress
}

# Capacitors: (width, length)
default_cap_size: dict[str, tuple[h.Prefixed, h.Prefixed]] = {name: (5 * µ, 5 * µ) for name in caps}


@dataclass
class Cache:
    """Module-scope caches of the compiled calls."""

    mos_modcalls: dict[MosParams, h.ExternalModuleCall] = field(default_factory=dict)
    res_modcalls: dict[PhysicalResistorParams, h.ExternalModuleCall] = field(default_factory=dict)
    cap_modcalls: dict[PhysicalCapacitorParams, h.ExternalModuleCall] = field(default_factory=dict)
    diode_modcalls: dict[DiodeParams, h.ExternalModuleCall] = field(default_factory=dict)
    bjt_modcalls: dict[BipolarParams, h.ExternalModuleCall] = field(default_factory=dict)


CACHE = Cache()
