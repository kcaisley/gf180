"""Local HDL21 and VLSIR contract tests for GF180MCU."""

import ast
import json
from io import StringIO
from pathlib import Path

import hdl21 as h
import pytest

from pdk import gf180
from pdk.gf180.hdl21 import site
from pdk.gf180.hdl21.pdk_logic import MOS_FINGER_MIN_UNITS, MOS_FINGER_UNITS, Install
from pdk.gf180.hdl21.primitives.prim_dicts import caps, default_xtor_size, diodes, ress, xtors

KIT = Path(__file__).resolve().parents[1]
_MOS_VARIANTS = tuple(
    (mos_type, mos_vth, mos_family, module.name) for (_, mos_type, mos_vth, mos_family), module in xtors.items()
)


def _tech(name: str):
    """A value of layout/tech.py, read without importing the row engine's path."""
    for node in ast.parse((KIT / "layout/tech.py").read_text()).body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if getattr(target, "id", None) == name:
                return ast.literal_eval(node.value)
            if isinstance(target, ast.Tuple) and name in [getattr(e, "id", None) for e in target.elts]:
                return ast.literal_eval(node.value)[[e.id for e in target.elts].index(name)]
    raise KeyError(name)


def test_supply_metadata() -> None:
    rails = gf180.Install.SUPPLY_RAILS
    assert rails["VDD"]["nominal"] == 3.3
    assert gf180.Install.supply_voltage(h.pdk.Corner.SLOW) == rails["VDD"]["min"]
    assert gf180.Install.supply_voltage(h.pdk.Corner.TYP) == rails["VDD"]["nominal"]
    assert gf180.Install.supply_voltage(h.pdk.Corner.FAST) == rails["VDD"]["max"]
    # the corners stay within 90 / 110 % of nominal
    assert rails["VDD"]["min"] >= 0.9 * rails["VDD"]["nominal"] - 1e-9
    assert rails["VDD"]["max"] <= 1.1 * rails["VDD"]["nominal"] + 1e-9


@pytest.mark.parametrize(("mos_type", "mos_vth", "mos_family", "model_name"), _MOS_VARIANTS)
def test_compile_and_netlist_mos_variant(
    mos_type: h.MosType,
    mos_vth: h.MosVth,
    mos_family: h.MosFamily,
    model_name: str,
) -> None:
    @h.module
    class Dut:
        d, g, s, b = h.Signals(4)
        m = h.Mos(tp=mos_type, vth=mos_vth, family=mos_family, w=2, l=1)(d=d, g=g, s=s, b=b)

    gf180.compile(Dut)
    call = Dut.m.of
    assert isinstance(call, h.ExternalModuleCall)
    assert call.module.name == model_name
    default_w, default_l = default_xtor_size[model_name]
    assert float(call.params.w) == pytest.approx(2 * float(default_w))
    assert float(call.params.l) == pytest.approx(float(default_l))

    for fmt in ("spice", "spectre"):
        output = StringIO()
        h.netlist(Dut, output, fmt=fmt)
        assert model_name in output.getvalue()


@pytest.mark.parametrize("vth", [h.MosVth.LOW, h.MosVth.STD, h.MosVth.HIGH])
@pytest.mark.parametrize(("tp", "name"), [(h.MosType.NMOS, "nfet_3v3"), (h.MosType.PMOS, "pfet_3v3")])
def test_every_threshold_is_the_core_device(vth, tp, name) -> None:
    """The kit has one threshold: every request of the core family is the 3.3 V device the
    standard cells and the row cells are made of (layout/tech.py MODELS)."""

    @h.module
    class Dut:
        d, g, s, b = h.Signals(4)
        m = h.Mos(tp=tp, vth=vth)(d=d, g=g, s=s, b=b)

    gf180.compile(Dut)
    assert Dut.m.of.module.name == name
    assert name in _tech("MODELS").values()


def test_passives_compile() -> None:
    @h.module
    class Dut:
        a, b, s = h.Signals(3)
        r = h.ThreeTerminalResistor(w=2, l=4)(p=a, n=b, b=s)
        c = h.PhysicalCapacitor(w=2, l=2)(p=a, n=s)
        d = h.Diode(model="diode_nd2ps_06v0", w=1 * h.prefix.µ, l=1 * h.prefix.µ)(p=s, n=a)

    gf180.compile(Dut)
    assert Dut.r.of.module.name == "ppolyf_u"
    assert float(Dut.r.of.params.r_width) == pytest.approx(1.6e-6)
    assert Dut.c.of.module.name == "cap_mim_2f0ff"
    assert Dut.d.of.module.name == "diode_nd2ps_06v0"
    out = StringIO()
    h.netlist(Dut, out, fmt="spice")
    assert "ppolyf_u" in out.getvalue()


def test_row_profile_matches_the_device_tables() -> None:
    """The row cells' widest and narrowest finger in unit widths, and the poly resistor, as the
    hdl21 package states them."""
    unit = round(float(default_xtor_size["nfet_3v3"][0]) * 1e9)
    assert MOS_FINGER_UNITS["analog"] == _tech("W_MAX") // unit
    co, end, side = _tech("CO"), _tech("CO_OD_END"), _tech("CO_OD_SIDE")
    assert (MOS_FINGER_MIN_UNITS - 1) * unit < co + max(end, side) * 2 <= MOS_FINGER_MIN_UNITS * unit
    assert _tech("RES")["model"] in ress
    # a three-layer MOM unit's channels run on the metal below its plates: the horizontal Metal2
    assert len(_tech("MOM_LAYERS")) == 3 and _tech("MOM_LAYERS")[0] - 1 == 2
    for name in caps | diodes:
        assert name.islower()


def test_includes_serve_both_simulators() -> None:
    for simulator in ("spectre", "ngspice"):
        attrs = site.install.simulation_includes(h.pdk.Corner.TYP, simulator)
        assert all(isinstance(a, (h.sim.Include, h.sim.Lib)) for a in attrs)
        assert attrs[0].path.name == "design.ngspice"
    assert site.install.include(h.pdk.Corner.FAST).section == "ff"
    assert site.install.include_res(h.pdk.Corner.SLOW).section == "res_ss"
    with pytest.raises(NotImplementedError):
        site.install.simulation_includes(h.pdk.Corner.TYP, "spectre", mismatch=True)
    assert set(Install.UNMODELED) <= {"spectre", "ngspice"}


def test_cell_netlists_name_the_kits_devices() -> None:
    """The library's netlist as the kit keeps it (openroad/views.py): the CDL's M lines on the
    deck's 3.3 V names (LVS), the SPICE's X lines on the package's (simulation)."""
    cdl = (KIT / "openroad/sp/gf180mcu_osu_sc_gp9t3v3.sp").read_text().splitlines()
    spice = (KIT / "hdl21/gf180mcu_osu_sc_gp9t3v3.spice").read_text().splitlines()
    assert {line.split()[-7] for line in cdl if line.startswith("M")} <= {"nfet_03v3", "pfet_03v3"}
    assert {line.split()[5] for line in spice if line.startswith("X")} == {"nfet_3v3", "pfet_3v3"}
    from pdk.gf180.netlist.lvs import DECK_NAMES

    assert set(DECK_NAMES) == set(_tech("MODELS").values())


def test_device_tables_are_the_kits() -> None:
    for kind in ("mosfet", "moscap", "polyres", "momcap"):
        path = KIT / "devices" / f"{kind}.json"
        if not path.exists():
            pytest.skip(f"no {kind} table yet")
        table = json.loads(path.read_text())
        assert table["provenance"]["pdk"] == "gf180"
        assert table["provenance"]["kind"] == kind


@pytest.mark.site_pdk
def test_site_files_exist() -> None:
    missing = [path for path in site.MODEL_FILES if not path.exists()]
    assert not missing, f"Missing GF180MCU site files: {missing}"
