"""Logic cells from gf180mcu_osu_sc_gp9t3v3 (Oklahoma State's 3.3 V, 9-track cells)."""

import hdl21 as h


def _cell(name: str, inputs: tuple[str, ...]) -> h.ExternalModule:
    return h.ExternalModule(
        domain="gf180",
        name=name,
        port_list=[
            *(h.Input(name=pin) for pin in inputs),
            h.Output(name="Y"),
            h.Inout(name="VDD"),
            h.Inout(name="VSS"),
        ],
        paramtype=h.HasNoParams,
    )


# generic logic cell (flow/circuit/devices.py) and drive band -> gf180mcu_osu_sc_gp9t3v3 cell; the
# library's NOR2 has one drive, which the band of two takes
_LOGIC = {
    ("inverter", 1): _cell("gf180mcu_osu_sc_gp9t3v3__inv_1", ("A",)),
    ("inverter", 4): _cell("gf180mcu_osu_sc_gp9t3v3__inv_4", ("A",)),
    ("inverter", 8): _cell("gf180mcu_osu_sc_gp9t3v3__inv_8", ("A",)),
    ("nor2", 2): _cell("gf180mcu_osu_sc_gp9t3v3__nor2_1", ("A", "B")),
    ("nand2", 1): _cell("gf180mcu_osu_sc_gp9t3v3__nand2_1", ("A", "B")),
}
_WRAPPERS: dict[tuple[str, int], h.Module] = {}


def logic_cell(kind: str, params) -> h.Module:
    """A generic inverter, NOR2 or NAND2 (inputs A, B; output Y) as its gf180mcu_osu_sc_gp9t3v3 cell."""

    key = (kind, params.drive)
    if key in _WRAPPERS:
        return _WRAPPERS[key]
    cell = _LOGIC.get(key)
    if cell is None:
        raise ValueError(f"no gf180mcu_osu_sc_gp9t3v3 cell for a {kind} of drive {params.drive}")
    wrapper = h.Module(name=f"gf180_{kind}_d{params.drive}")
    wrapper.A, wrapper.Y = h.Input(), h.Output()
    wrapper.VDD, wrapper.VSS = h.Inout(), h.Inout()
    pins = {"A": wrapper.A, "Y": wrapper.Y, "VDD": wrapper.VDD, "VSS": wrapper.VSS}
    if kind != "inverter":
        wrapper.B = h.Input()
        pins["B"] = wrapper.B
    wrapper.add(cell()(**pins), name="cell")
    _WRAPPERS[key] = wrapper
    return wrapper
