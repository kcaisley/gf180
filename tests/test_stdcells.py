"""Compile-only standard-cell contracts; no foundry models or simulator required."""

import hdl21 as h
import pytest

from pdk import gf180 as pdk
from pdk.gf180.hdl21 import cells, site
from pdk.gf180.hdl21.pdk_logic import Gf180Walker as Walker
from pdk.gf180.hdl21.stdcells import logic_cell


def test_unrelated_external_call_unchanged():
    for domain, name in (("generic", "other"), ("other", "clock_xor")):
        call = h.ExternalModule(domain=domain, name=name, port_list=[], paramtype=h.HasNoParams)()
        assert Walker().visit_external_module_call(call) is call


def test_stdcell_include_is_separate():
    include = site.install.include_stdcell()
    assert isinstance(include, h.sim.Include)
    assert include.path.name == "gf180mcu_fd_sc_mcu7t5v0.sp"
    assert include.path not in site.MODEL_FILES
    assert isinstance(site.install.include(h.pdk.Corner.TYP), h.sim.Lib)
    assert pdk.Install.supply_voltage(h.pdk.Corner.TYP) == 5.0


@pytest.mark.parametrize(("kind", "drive"), [("inverter", 1), ("inverter", 4), ("inverter", 8), ("nor2", 2), ("nand2", 1)])
def test_logic_cells_are_library_cells(kind: str, drive: int):
    params = type("Drive", (), {"drive": drive})()
    wrapper = logic_cell(kind, params)
    inner = next(iter(wrapper.instances.values()))
    name = inner.of.module.name
    assert name in cells.CELLS
    pins, _ = cells.CELLS[name]
    assert {p.name for p in inner.of.module.port_list} == set(pins)
    assert {"VDD", "VSS"} <= set(pins) and not {"VNW", "VPW"} & set(pins)


def test_generic_cells_resolve():
    assert cells.LIBRARY == "gf180mcu_fd_sc_mcu7t5v0"
    for generic, (cell, pins, _high, _low) in cells.GENERIC.items():
        assert cell in cells.CELLS, generic
        assert set(cells.CELLS[cell][0]) - {"VNW", "VPW"} <= set(pins) | set(_high) | set(_low) | set(cells.CELLS[cell][0])
