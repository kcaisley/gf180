"""
Hdl21 + GlobalFoundries GF180MCU (open PDK, variant gf180mcuD) Modules and Transformations

Defines the `hdl21.ExternalModule`s of the GF180MCU devices (``pdk_data``, ``primitives``) and
the compile pass that converts process-portable `hdl21.Primitive` elements into them.

The process: 180 nm, 3.3 V, 5 V and 6 V CMOS, five metals (gf180mcuD: Metal1 to Metal4 and an
11 kA top metal, Metal5), MIM option B. The kit's core is the 5 V device pair the
gf180mcu_fd_sc_mcu7t5v0 standard cells are made of (nfet_05v0, pfet_05v0), at a 5.0 V supply.

Target devices for conversion from `hdl21.Primitive`:
- MOS: nfet_05v0, pfet_05v0 (CORE), nfet_06v0, pfet_06v0 (IO)
- Resistors: the poly, diffusion and well resistors (ppolyf_u, npolyf_u, ppolyf_u_1k, ...)
- Capacitors: MIM (cap_mim_2f0ff, ...) and MOS capacitors
- Diodes: the junction diodes (diode_nd2ps_06v0, ...)

Derived from the Hdl21 GF180 package (``pdks/Gf180/gf180_hdl21/pdk_logic.py``).
"""

from pathlib import Path
from typing import Any, ClassVar, Optional

import hdl21 as h
from hdl21.pdk import PdkInstallation
from hdl21.primitives import (
    Bipolar,
    Diode,
    DiodeParams,
    Mos,
    MosParams,
    PhysicalCapacitor,
    PhysicalCapacitorParams,
    PhysicalResistor,
    PhysicalResistorParams,
    ThreeTerminalCapacitor,
    ThreeTerminalResistor,
)
from pydantic.dataclasses import dataclass

from .pdk_data import Gf180CapParams, Gf180DiodeParams, Gf180MosParams, Gf180ResParams
from .primitives.prim_dicts import *

# The widest MOS finger each row-cell type fits (pdk/gf180/layout/tech.py: W_MAX for the analog
# cells, LOGIC_OD for the logic ones), in unit widths (default_xtor_size: 300 nm). Generators that
# place their devices in these cells read this through hdl21.pdk.default() and size every finger in
# whole units.
MOS_FINGER_UNITS = {"analog": 6, "logic_n": 2, "logic_p": 3}
# The narrowest analog finger the row cells contact: a 220 nm contact with 70 nm of COMP past its
# end and beside it (layout/tech.py CO, CO_OD_END, CO_OD_SIDE) needs 360 nm, two units.
MOS_FINGER_MIN_UNITS = 2
# A fingered MOS's w is its total width, with nf: the models divide it among the fingers (a
# w=6u nf=2 device carries the current of two w=3u ones).

# the model library's sections per corner: the MOS's, and each passive's and the diodes' as
# <kind>_<section> (res_typical, mimcap_ff, diode_ss)
CORNERS = {h.pdk.Corner.TYP: "typical", h.pdk.Corner.FAST: "ff", h.pdk.Corner.SLOW: "ss"}


@dataclass
class Install(PdkInstallation):
    """
    PDK installation data for GF180MCU: an open_pdks install of the gf180mcu family (``ciel``'s
    PDK root, ``pdk_path``) and the variant used (``gf180mcuD``).

    Spectre and ngspice both read the open PDK's ngspice decks (``libs.tech/ngspice``): Spectre
    takes their SPICE syntax as it is, so one set of includes serves both simulators.

    Attributes:
        pdk_path: The PDK root (``GF180_OPEN_PDK``), holding ``<variant>/libs.{ref,tech}``.
        variant: The open_pdks variant (gf180mcuD: five metals, 11 kA top metal, MIM option B).
    """

    pdk_path: Path
    variant: str = "gf180mcuD"

    LOCAL_SPICE_FILES: ClassVar[list[Path]] = [
        Path("gf180mcuD/libs.tech/ngspice/design.ngspice"),
        Path("gf180mcuD/libs.tech/ngspice/sm141064.ngspice"),
        Path("gf180mcuD/libs.tech/ngspice/sm141064_mim.ngspice"),
        Path("gf180mcuD/libs.ref/gf180mcu_fd_sc_mcu7t5v0/spice/gf180mcu_fd_sc_mcu7t5v0.spice"),
    ]

    @property
    def models(self) -> Path:
        """The model library: its MOS corners and each passive's and diode's sections."""
        return self.pdk_path / self.variant / "libs.tech/ngspice/sm141064.ngspice"

    # what the site's model decks do not model, per simulator: a device, or "cells", and why
    # (pdk/test_spice.py)
    UNMODELED: ClassVar[dict[str, dict[str, str]]] = {
        "spectre": {
            name: f"the open decks name both a subcircuit and the model cards {name}: Spectre cannot bind an "
            "instance of that name (SFE-405); the core 5 V devices wrap the same cards"
            for name in ("nfet_06v0", "pfet_06v0")
        },
    }

    def simulation_includes(self, corner: h.pdk.Corner, simulator: str = "spectre", mismatch: bool = False) -> list:
        """What a simulation of this package's devices and standard cells includes, in order, for
        ``simulator`` ("spectre", or "ngspice" in HSPICE compatibility): the models' global
        switches (``design.ngspice``), the MOS models at ``corner``, the resistors, capacitors and
        diodes at ``corner``, the standard cells' netlist, the package's device wrappers. Both
        simulators read the same open decks. ``mismatch``: the decks vary mismatch through their
        own switches (``sw_stat_mismatch``, agauss), not a simulator's statistics blocks."""

        if mismatch:
            raise NotImplementedError("the open decks' mismatch is their agauss switches, not Spectre's statistics")
        if simulator not in ("spectre", "ngspice"):
            raise ValueError(f"no {simulator} models for GF180MCU")
        cells = self.include_stdcell() if simulator == "spectre" else self.include_stdcell_ngspice()
        return [
            self.include_pre_simulation(),
            self.include(corner),
            self.include_res(corner),
            *self.include_mimcap(corner),
            self.include_moscap(corner),
            self.include_diodes(corner),
            cells,
            self.include_devices(),
        ]

    SUPPLY_RAILS: ClassVar[dict[str, dict[str, float]]] = {
        "VDD": {"nominal": 5.0, "min": 4.5, "max": 5.5},
        "VSS": {"nominal": 0.0, "min": 0.0, "max": 0.0},
    }

    @classmethod
    def supply_voltage(cls, corner: h.pdk.Corner, rail: str = "VDD") -> float:
        """Return rail voltage for the given process-voltage corner."""
        r = cls.SUPPLY_RAILS.get(rail.upper())
        if r is None:
            raise KeyError(f"Unknown rail '{rail}' for GF180MCU.")
        return {
            h.pdk.Corner.SLOW: r["min"],
            h.pdk.Corner.TYP: r["nominal"],
            h.pdk.Corner.FAST: r["max"],
        }[corner]

    def include(self, corner: h.pdk.Corner) -> h.sim.Lib:
        """The MOS models at ``corner`` (typical, ff, ss: the 3.3 V devices' corners; the 6 V
        family, the core 5 V devices among it, stays at typical in every section)."""
        if corner not in CORNERS:
            raise ValueError(f"Invalid corner {corner}")
        return h.sim.Lib(path=self.models, section=CORNERS[corner])

    def include_pre_simulation(self) -> h.sim.Include:
        """The models' global switches and corner parameters (``design.ngspice``: statistics off
        unless a run sets them), which every model card reads."""
        return h.sim.Include(path=self.pdk_path / self.variant / "libs.tech/ngspice/design.ngspice")

    def _passive(self, kind: str, corner: h.pdk.Corner) -> h.sim.Lib:
        if corner not in CORNERS:
            raise ValueError(f"Invalid corner {corner}")
        return h.sim.Lib(path=self.models, section=f"{kind}_{CORNERS[corner]}")

    def include_res(self, corner: h.pdk.Corner) -> h.sim.Lib:
        """The resistors (poly, diffusion, well, metal) at ``corner``."""
        return self._passive("res", corner)

    def include_mimcap(self, corner: h.pdk.Corner) -> list[h.sim.Lib]:
        """The MIM capacitors: their corner factors at ``corner`` and the capacitors by the LVS
        deck's names (cap_mim_2f0ff, its ``cap_mim`` section)."""
        return [self._passive("mimcap", corner), h.sim.Lib(path=self.models, section="cap_mim")]

    def include_moscap(self, corner: h.pdk.Corner) -> h.sim.Lib:
        """The MOS capacitors at ``corner``."""
        return self._passive("moscap", corner)

    def include_diodes(self, corner: h.pdk.Corner) -> h.sim.Lib:
        """The junction diodes (the standard cells' antenna diodes among them) at ``corner``."""
        return self._passive("diode", corner)

    def include_stdcell(self) -> h.sim.Include:
        """The gf180mcu_fd_sc_mcu7t5v0 cells' CDL (this package's copy, which the row cells and LVS
        draw from: M lines on the device subcircuits, which Spectre takes, the wells on the
        rails); the device models must be included separately."""
        return h.sim.Include(path=Path(__file__).resolve().parents[1] / "openroad/sp/gf180mcu_fd_sc_mcu7t5v0.sp")

    def include_stdcell_ngspice(self) -> h.sim.Include:
        """The same cells for ngspice, whose subcircuit calls must be X lines (this package's copy
        of the PDK's SPICE, the wells on the rails: openroad/views.py)."""
        return h.sim.Include(path=Path(__file__).resolve().parent / "gf180mcu_fd_sc_mcu7t5v0.spice")

    def include_devices(self) -> h.sim.Include:
        """The package's device names the PDK's decks lack (``devices.sp``, SPICE, which both
        simulators read): the poly resistor by its body's ``l`` and ``w`` (the frida poly-resistor
        request's parameters), on the deck's ``ppolyf_u``; include after the resistors."""
        return h.sim.Include(path=Path(__file__).resolve().parent / "devices.sp")

    singleton: Optional["Install"] = None

    @classmethod
    def instance(cls) -> "Install":
        """Get the singleton Install instance."""
        if cls.singleton is None:
            raise ValueError("The Install instance has not been initialized yet.")
        return cls.singleton

    def __post_init__(self):
        if Install.singleton is not None:
            raise ValueError("The Install instance has already been initialized.")
        Install.singleton = self


# the row cells' source and drain strips along the channel (layout/tech.py): an outer one, from
# the gate to the diffusion's end (OD_EXT + CO / 2 + CO_GATE), and one shared by two gates (CO + 2
# CO_GATE), in meters
_SD_OUTER, _SD_INNER = 440e-9, 520e-9


def junctions(w: float, nf: int) -> dict[str, float]:
    """The source and drain diffusions of a device of total width ``w`` (m) in ``nf`` fingers as the
    row cells draw it (strips S D S D ..., the ends outer): their areas and perimeters (m^2, m),
    gate edges included, as the open LVS deck extracts them (KLayout's AS, AD, PS, PD)."""
    wf = w / nf
    strips = [_SD_OUTER if i in (0, nf) else _SD_INNER for i in range(nf + 1)]
    source, drain = strips[0::2], strips[1::2]
    return {
        "As": sum(source) * wf,
        "ad": sum(drain) * wf,
        "ps": sum(2 * (s + wf) for s in source),
        "pd": sum(2 * (d + wf) for d in drain),
    }


class Gf180Walker(h.HierarchyWalker):
    """Hierarchical walker converting `h.Primitive` instances to GF180MCU `ExternalModule`s."""

    def visit_external_module_call(self, call: h.ExternalModuleCall) -> h.Instantiable:
        """Generic logic cells (inverter, nor2, nand2) and the generic cell library become
        gf180mcu_fd_sc_mcu7t5v0 standard cells."""
        from flow.circuit.cells import substitute

        from . import cells

        wrapper = substitute(call, cells)  # a generic cell (flow.circuit.cells): its library cell
        if wrapper is not None:
            return wrapper
        if call.module.domain == "generic" and call.module.name in ("inverter", "nor2", "nand2"):
            from .stdcells import logic_cell

            return logic_cell(call.module.name, call.params)
        return call

    def visit_primitive_call(self, call: h.PrimitiveCall) -> h.Instantiable:
        """Replace instances of `h.Primitive` with GF180MCU `ExternalModule`s."""
        if call.prim is Mos:
            return self.mos_module_call(call.params)
        if call.prim is PhysicalResistor or call.prim is ThreeTerminalResistor:
            return self.res_module_call(call.params)
        if call.prim is PhysicalCapacitor or call.prim is ThreeTerminalCapacitor:
            return self.cap_module_call(call.params)
        if call.prim is Diode:
            return self.diode_module_call(call.params)
        if call.prim is Bipolar:
            raise RuntimeError("GF180MCU bipolar devices are not wrapped by this package")
        return call

    def mos_module(self, params: MosParams) -> h.ExternalModule:
        """The `ExternalModule` for MOS parameters `params`: by model name where given, else by
        type and family (NONE: the core). The kit has one threshold, which LOW and HIGH take."""
        if params.model is not None:
            try:
                return next(v for k, v in xtors.items() if params.model in (k[0], v.name))
            except StopIteration:
                raise RuntimeError(f"No Mos module for model name {params.model}") from None
        mostype = h.MosType.NMOS if params.tp is None else params.tp
        mosfam = h.MosFamily.CORE if params.family in (None, h.MosFamily.NONE) else params.family
        for (_name, tp, _vth, fam), module in xtors.items():
            if tp == mostype and fam == mosfam:
                return module
        raise RuntimeError(f"No GF180MCU MOS for type={mostype}, family={mosfam}")

    def mos_module_call(self, params: MosParams) -> h.ExternalModuleCall:
        """Retrieve or create a `Call` for MOS parameters `params`."""
        if params in CACHE.mos_modcalls:
            return CACHE.mos_modcalls[params]
        mod = self.mos_module(params)
        w, l = self.use_defaults(params, mod.name, default_xtor_size)
        nf = int(params.nf or 1)
        # the diffusions' junctions where the width is a number (not an expression)
        sd = {k: v for k, v in junctions(float(w), nf).items()} if isinstance(w, h.Prefixed) else {}
        modparams = Gf180MosParams(
            w=w,  # the total width: the models divide it among the nf fingers
            l=l,
            nf=nf,
            m=int(params.mult or 1),
            **{k: h.Prefixed.new(round(v * 1e18) / 1e18 if k in ("As", "ad") else round(v * 1e12) / 1e12) for k, v in sd.items()},
        )
        modcall = mod(modparams)
        CACHE.mos_modcalls[params] = modcall
        return modcall

    def res_module_call(self, params: PhysicalResistorParams) -> h.ExternalModuleCall:
        """A resistor by model name (``ress``; default ppolyf_u, the row cells')."""
        if params in CACHE.res_modcalls:
            return CACHE.res_modcalls[params]
        model = getattr(params, "model", None) or "ppolyf_u"
        mod = ress.get(model)
        if mod is None:
            raise RuntimeError(f"No Res module for model {model}. Available: {list(ress)}")
        w, l = self.use_defaults(params, mod.name, default_res_size)
        modcall = mod(Gf180ResParams(r_width=w, r_length=l))
        CACHE.res_modcalls[params] = modcall
        return modcall

    def cap_module_call(self, params: Any) -> h.ExternalModuleCall:
        """A capacitor by model name (``caps``; default cap_mim_2f0ff, gf180mcuD's MIM)."""
        if params in CACHE.cap_modcalls:
            return CACHE.cap_modcalls[params]
        model = getattr(params, "model", None) or "cap_mim_2f0ff"
        mod = caps.get(model)
        if mod is None:
            raise RuntimeError(f"No Cap module for model {model}. Available: {list(caps)}")
        w, l = self.use_defaults(params, mod.name, default_cap_size)
        modcall = mod(Gf180CapParams(c_width=w, c_length=l))
        CACHE.cap_modcalls[params] = modcall
        return modcall

    def diode_module_call(self, params: DiodeParams) -> h.ExternalModuleCall:
        """A junction diode by model name (``diodes``), its area and perimeter from w and l."""
        if params in CACHE.diode_modcalls:
            return CACHE.diode_modcalls[params]
        mod = diodes.get(params.model)
        if mod is None:
            raise RuntimeError(f"No Diode module for model {params.model}. Available: {list(diodes)}")
        if params.w is not None and params.l is not None:
            modparams = Gf180DiodeParams(area=params.w * params.l, pj=2 * (params.w + params.l))
        else:
            modparams = Gf180DiodeParams()
        modcall = mod(modparams)
        CACHE.diode_modcalls[params] = modcall
        return modcall

    def scale_param(self, orig: h.Scalar | None, default: h.Prefixed) -> h.Scalar:
        """Scale device parameter value: unitless generic values are multiples of the model's
        default dimensions (``default_*_size``)."""
        if orig is None:
            return default
        if isinstance(orig, h.Prefixed):
            if orig.prefix == h.Prefix.UNIT:
                return orig.number * default
            return orig
        if isinstance(orig, (int, float)):
            return h.Prefixed.new(orig, h.Prefix.UNIT) * default
        if isinstance(orig, h.Literal):
            return h.Literal(f"({orig.text} * {default.number}e{default.prefix.value})")
        raise TypeError(f"Param Value {orig}")

    def use_defaults(
        self, params: h.paramclass, modname: str, defaults: dict[str, tuple[h.Prefixed, h.Prefixed]]
    ) -> tuple[h.Scalar, h.Scalar]:
        """Width and length, unitless values scaled by the model's defaults."""
        w0, l0 = defaults.get(modname) or next(iter(defaults.values()))
        w = self.scale_param(getattr(params, "w", None), w0)
        l = self.scale_param(getattr(params, "l", None), l0)
        return w, l


def compile(src: h.Elaboratables) -> None:
    """Compile `src` into the GF180MCU technology: every `h.Primitive` instance becomes the PDK's
    `ExternalModule` (Gf180Walker)."""
    Gf180Walker().walk(src)
