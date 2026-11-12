"""Parameter classes and module constructors for the GF180MCU devices.

The devices are the open PDK's simulation subcircuits (``libs.tech/ngspice/sm141064.ngspice``),
named as the PDK's own netlists and its KLayout LVS name them (``nfet_05v0``, ``ppolyf_u``,
``cap_mim_2f0ff``), but for the 3.3 V core pair: the decks name both a subcircuit and model cards
``nfet_03v3`` (``pfet_03v3``), which Spectre cannot call by name, so the package's are ``nfet_3v3``
and ``pfet_3v3``, a wrapper of each in ``spectre_devices.scs`` / ``ngspice_devices.spice`` (the LVS
source names them as the deck does: ``netlist/lvs.py``). Sizes are in meters.

Derived from the Hdl21 GF180 package (``pdks/Gf180/gf180_hdl21/pdk_data.py``).
"""

from copy import deepcopy

import hdl21 as h
from hdl21.prefix import µ, p
from hdl21.primitives import Diode, Mos, PhysicalCapacitor, ThreeTerminalResistor
from vlsirtools import SpiceType

PDK_NAME = "gf180"


@h.paramclass
class Gf180MosParams:
    """GF180MCU MOS parameters: the subcircuits' ``w`` (the total width: the models divide it among
    the ``nf`` fingers), ``l``, ``nf`` and ``m``.

    Defaults: the 3.3 V core devices' (nfet_3v3) narrowest width and shortest length."""

    w = h.Param(dtype=h.Scalar, desc="Total width (m)", default=0.22 * µ)
    l = h.Param(dtype=h.Scalar, desc="Length (m)", default=0.28 * µ)
    nf = h.Param(dtype=int, desc="Number of fingers", default=1)
    m = h.Param(dtype=int, desc="Multiplier", default=1)
    # the source and drain diffusions (m^2, m): the subcircuits' 0 defaults would leave their
    # junctions out (BSIM4 reads a given 0 as none); the compile pass gives the row cells' own
    # (pdk_logic.junctions). ``As``: SPICE's ``as``, a Python keyword (SPICE and Spectre take it)
    ad = h.Param(dtype=h.Scalar, desc="Drain area (m^2)", default=0)
    As = h.Param(dtype=h.Scalar, desc="Source area (m^2)", default=0)
    pd = h.Param(dtype=h.Scalar, desc="Drain perimeter (m)", default=0)
    ps = h.Param(dtype=h.Scalar, desc="Source perimeter (m)", default=0)


@h.paramclass
class Gf180ResParams:
    """GF180MCU resistor parameters (the subcircuits' ``r_width``, ``r_length``, meters)."""

    r_width = h.Param(dtype=h.Scalar, desc="Width (m)", default=1 * µ)
    r_length = h.Param(dtype=h.Scalar, desc="Length (m)", default=1 * µ)


@h.paramclass
class Gf180CapParams:
    """GF180MCU MIM and MOS capacitor parameters (the subcircuits' ``c_width``, ``c_length``, meters)."""

    c_width = h.Param(dtype=h.Scalar, desc="Width (m)", default=10 * µ)
    c_length = h.Param(dtype=h.Scalar, desc="Length (m)", default=10 * µ)


@h.paramclass
class Gf180DiodeParams:
    """GF180MCU diode parameters: junction area (m^2) and perimeter (m), as the models take them."""

    area = h.Param(dtype=h.Scalar, desc="Junction area (m^2)", default=1 * p)
    pj = h.Param(dtype=h.Scalar, desc="Junction perimeter (m)", default=4 * µ)


@h.paramclass
class Gf180LogicParams:
    """GF180MCU standard cells have no parameters."""


def xtor_module(modname: str) -> h.ExternalModule:
    """A MOS subcircuit (d g s b)."""
    return h.ExternalModule(
        domain=PDK_NAME,
        name=modname,
        desc=f"{PDK_NAME} PDK MOS {modname}",
        port_list=deepcopy(Mos.port_list),
        paramtype=Gf180MosParams,
        spicetype=SpiceType.SUBCKT,
    )


def res_module(modname: str) -> h.ExternalModule:
    """A resistor subcircuit: its two heads and the body's bulk (p, n, b)."""
    return h.ExternalModule(
        domain=PDK_NAME,
        name=modname,
        desc=f"{PDK_NAME} PDK resistor {modname}",
        port_list=deepcopy(ThreeTerminalResistor.port_list),
        paramtype=Gf180ResParams,
        spicetype=SpiceType.SUBCKT,
    )


def cap_module(modname: str) -> h.ExternalModule:
    """A two-terminal capacitor subcircuit (p, n)."""
    return h.ExternalModule(
        domain=PDK_NAME,
        name=modname,
        desc=f"{PDK_NAME} PDK capacitor {modname}",
        port_list=deepcopy(PhysicalCapacitor.port_list),
        paramtype=Gf180CapParams,
        spicetype=SpiceType.SUBCKT,
    )


def diode_module(modname: str) -> h.ExternalModule:
    """A junction diode model (p, n): a D element on the model card."""
    return h.ExternalModule(
        domain=PDK_NAME,
        name=modname,
        desc=f"{PDK_NAME} PDK diode {modname}",
        port_list=deepcopy(Diode.port_list),
        paramtype=Gf180DiodeParams,
        spicetype=SpiceType.DIODE,
    )


def logic_module(modname: str, terminals: list[str]) -> h.ExternalModule:
    """A standard cell, its pins in the library netlist's order."""
    return h.ExternalModule(
        domain=PDK_NAME,
        name=modname,
        desc=f"{PDK_NAME} standard cell {modname}",
        port_list=[h.Inout(name=pin) for pin in terminals],
        paramtype=Gf180LogicParams,
    )
