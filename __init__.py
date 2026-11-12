"""
GlobalFoundries GF180MCU (open PDK, gf180mcuD) for Hdl21

This package provides Hdl21 integration for the open GF180MCU PDK, variant gf180mcuD (five
metals, 11 kA top metal, MIM option B), with its 5 V core devices and the
gf180mcu_fd_sc_mcu7t5v0 standard cells.

Usage:
    import hdl21 as h
    from pdk import gf180

    @h.module
    class MyInverter:
        vdd, vss, inp, out = h.Ports(4)
        p = h.Mos(tp=h.MosType.PMOS)(g=inp, d=out, s=vdd, b=vdd)
        n = h.Mos(tp=h.MosType.NMOS)(g=inp, d=out, s=vss, b=vss)

    gf180.compile(MyInverter)
"""

from hdl21.pdk import register

# Grab our primary PDK-definition module
from .hdl21 import pdk_logic
from .hdl21.pdk_logic import *

# The optional external-data installation.
# Set by an instantiator of `Install`, if available.
install: Install | None = None

# And register as a PDK module
register(pdk_logic)
