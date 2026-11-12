"""Logic cells from gf180mcu_fd_sc_mcu7t5v0 (5 V), as this package's netlists of them have them:
the library's well pins (VNW, VPW) on the rails (openroad/views.py)."""

import hdl21 as h


def _cell(name: str, inputs: tuple[str, ...]) -> h.ExternalModule:
    return h.ExternalModule(
        domain="gf180",
        name=name,
        port_list=[
            *(h.Input(name=pin) for pin in inputs),
            h.Output(name="ZN"),
            h.Inout(name="VDD"),
            h.Inout(name="VSS"),
        ],
        paramtype=h.HasNoParams,
    )


# generic logic cell (flow/circuit/devices.py) and drive band -> gf180mcu_fd_sc_mcu7t5v0 cell
_LOGIC = {
    ("inverter", 1): _cell("gf180mcu_fd_sc_mcu7t5v0__inv_1", ("I",)),
    ("inverter", 4): _cell("gf180mcu_fd_sc_mcu7t5v0__inv_4", ("I",)),
    ("inverter", 8): _cell("gf180mcu_fd_sc_mcu7t5v0__inv_8", ("I",)),
    ("nor2", 2): _cell("gf180mcu_fd_sc_mcu7t5v0__nor2_2", ("A1", "A2")),
    ("nand2", 1): _cell("gf180mcu_fd_sc_mcu7t5v0__nand2_1", ("A1", "A2")),
}
_WRAPPERS: dict[tuple[str, int], h.Module] = {}


def logic_cell(kind: str, params) -> h.Module:
    """A generic inverter, NOR2 or NAND2 (inputs A, B; output Y) as its gf180mcu_fd_sc_mcu7t5v0 cell."""

    key = (kind, params.drive)
    if key in _WRAPPERS:
        return _WRAPPERS[key]
    cell = _LOGIC.get(key)
    if cell is None:
        raise ValueError(f"no gf180mcu_fd_sc_mcu7t5v0 cell for a {kind} of drive {params.drive}")
    wrapper = h.Module(name=f"gf180_{kind}_d{params.drive}")
    wrapper.A, wrapper.Y = h.Input(), h.Output()
    wrapper.VDD, wrapper.VSS = h.Inout(), h.Inout()
    pins = {"ZN": wrapper.Y, "VDD": wrapper.VDD, "VSS": wrapper.VSS}
    if kind == "inverter":
        pins["I"] = wrapper.A
    else:
        wrapper.B = h.Input()
        pins |= {"A1": wrapper.A, "A2": wrapper.B}
    wrapper.add(cell()(**pins), name="cell")
    _WRAPPERS[key] = wrapper
    return wrapper
