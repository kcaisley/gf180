"""GF180MCU's LVS source rules, on the netlist's data (``flow.circuit.netlists``' LVS context, run
in a process bound to the kit): each MOS as compiled (the deck's own names, nfet_05v0 and pfet_05v0;
w its total width, nf its fingers), the gf180mcu_fd_sc_mcu7t5v0 subcircuits of the standard cells it
calls (this package's CDL of them, their wells on the rails: openroad/views.py).
"""

from __future__ import annotations


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
    """The library text the source calls: the standard cells' subcircuits (gf180mcu_fd_sc_mcu7t5v0)."""
    from paths import STD_SPICE

    return "\n".join(_subckts(STD_SPICE.read_text(), cells))
