"""Write this directory's views of gf180mcu_fd_sc_mcu7t5v0 from the open PDK (``GF180_OPEN_PDK``,
the ciel root, README.md), and the package's ngspice copy of its cells; rerun after a PDK update
and commit the result:

    uv run python pdk/gf180/openroad/views.py

* ``gf180mcu_tech.lef``: the library's nominal technology LEF (``__nom.tlef``);
* ``lef/gf180mcu_fd_sc_mcu7t5v0.lef``: the cells' LEF, as the library has it;
* ``lib/``: the typical (tt 25 C 5.00 V) and slow (ss 125 C 4.50 V) Liberty, gzipped;
* ``gds/gf180mcu_fd_sc_mcu7t5v0.gds.gz``: the cells' GDS, gzipped;
* ``sp/gf180mcu_fd_sc_mcu7t5v0.sp``: the cells' CDL (M lines: LVS, the layout flow's library
  reader, Spectre) with each cell's well pins VNW and VPW on its rails (VDD, VSS): the row cells'
  wells are their rails', tied by the library's filltie at every row end;
* ``../hdl21/gf180mcu_fd_sc_mcu7t5v0.spice``: the same cells as the PDK's SPICE has them (X lines
  on the device subcircuits, which ngspice needs), their well pins likewise on the rails;
* ``v/gf180mcu_fd_sc_mcu7t5v0.v``: one instance of every Liberty cell (pdk/test_openroad.py).
"""

from __future__ import annotations

import gzip
import os
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("GF180_OPEN_PDK", "/users/kcaisley/Documents/libs/gf180mcu-open-pdk"))
NAME = "gf180mcu_fd_sc_mcu7t5v0"
LIB = ROOT / "gf180mcuD/libs.ref" / NAME
CORNERS = ("tt_025C_5v00", "ss_125C_4v50")
WELLS = {"VNW": "VDD", "VPW": "VSS"}  # each well pin's rail


def on_rails(text: str, kind: str) -> str:
    """A library netlist with its cells' well pins on their rails: left out of each .subckt line
    and replaced by the rail in each device line."""
    out = [
        f"* {NAME} ({kind}) for FRIDA (pdk/gf180/openroad/views.py): the open PDK's cells, each well",
        "* pin (VNW, VPW) on its rail (VDD, VSS)",
    ]
    for line in re.sub(r"\n\+", " ", text).splitlines():
        fields = line.split()
        if not fields or line.startswith("*"):
            continue
        if fields[0].lower() == ".subckt":
            out.append(" ".join(f for f in fields if f not in WELLS))
        elif fields[0].lower() == ".ends":
            out += [".ENDS", ""]
        elif fields[0][0] in "Dd":  # a diode: the CDL's positional area and perimeter by name
            nets = [WELLS.get(f, f) for f in fields[1:3]]
            sizes = [f for f in fields[4:] if not f.startswith("$")]
            if sizes and "=" not in sizes[0]:
                sizes = [f"AREA={sizes[0]}", *(f"PJ={v}" for v in sizes[1:2])]
            out.append(" ".join([fields[0].upper(), *nets, fields[3], *sizes]))
        else:
            out.append(" ".join(WELLS.get(f, f) for f in fields))
    return "\n".join(out) + "\n"


def verilog(cells: list[str]) -> str:
    """One instance of each cell, unconnected (pdk/test_openroad.py links it)."""
    lines = [f"// One unconnected instance of every {NAME} cell: the design pdk/test_openroad.py links.", f"module {NAME} ();"]
    lines += [f"  {cell} u{i} ();" for i, cell in enumerate(cells)]
    return "\n".join([*lines, "endmodule", ""])


def _gzip(src: Path, dst: Path) -> None:
    with src.open("rb") as file, gzip.GzipFile(dst, "wb", compresslevel=9, mtime=0) as out:
        shutil.copyfileobj(file, out)


def main() -> None:
    shutil.copyfile(LIB / f"techlef/{NAME}__nom.tlef", HERE / "gf180mcu_tech.lef")
    shutil.copyfile(LIB / f"lef/{NAME}.lef", HERE / f"lef/{NAME}.lef")
    for corner in CORNERS:
        _gzip(LIB / f"lib/{NAME}__{corner}.lib", HERE / f"lib/{NAME}__{corner}.lib.gz")
    _gzip(LIB / f"gds/{NAME}.gds", HERE / f"gds/{NAME}.gds.gz")
    (HERE / f"sp/{NAME}.sp").write_text(on_rails((LIB / f"cdl/{NAME}.cdl").read_text(), "CDL"))
    (HERE.parent / f"hdl21/{NAME}.spice").write_text(on_rails((LIB / f"spice/{NAME}.spice").read_text(), "SPICE"))
    liberty = (LIB / f"lib/{NAME}__{CORNERS[0]}.lib").read_text()
    cells = sorted(set(re.findall(r"^\s*cell\s*\(\s*\"?([\w$]+)\"?\s*\)", liberty, re.MULTILINE)))
    (HERE / f"v/{NAME}.v").write_text(verilog(cells))


if __name__ == "__main__":
    main()
