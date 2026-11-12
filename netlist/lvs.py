"""GF180MCU's LVS source rules, on the netlist's data (``flow.circuit.netlists``' LVS context, run
in a process bound to the kit): each MOS by the deck's own names (the package's nfet_3v3 / pfet_3v3
are the deck's nfet_03v3 / pfet_03v3), its total width and length, the gf180mcu_osu_sc_gp9t3v3
subcircuits of the standard cells it calls (this package's CDL of them: openroad/views.py).
"""

from __future__ import annotations

# the package's device names -> the deck's
DECK_NAMES = {"nfet_3v3": "nfet_03v3", "pfet_3v3": "pfet_03v3"}


def mos(model: str, w_m: float, l_m: float) -> tuple[str, dict[str, float]] | None:
    """The deck's device for a MOS of ``model`` of total width ``w_m`` and length ``l_m`` (metres):
    its name (``DECK_NAMES``), ``W`` and ``L`` (the deck compares those; its junction values are not
    compared)."""
    return DECK_NAMES.get(model, model), {"W": w_m, "L": l_m}


def _subckts(text: str, names: set[str]) -> list[str]:
    out, keep = [], False
    for line in text.splitlines():
        f = line.split()
        if f and f[0].lower() == ".subckt":
            keep = f[1] in names
        if keep:
            out.append(line)
        if f and f[0].lower() == ".ends":
            keep = False
    return out


def library(cells: set[str], devices: set[str]) -> str:
    """The library text the source calls: the standard cells' subcircuits (gf180mcu_osu_sc_gp9t3v3)."""
    from paths import STD_SPICE

    return "\n".join(_subckts(STD_SPICE.read_text(), cells))
