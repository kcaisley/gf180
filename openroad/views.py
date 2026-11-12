"""Write this directory's views of gf180mcu_osu_sc_gp9t3v3 (Oklahoma State's 3.3 V, 9-track cells) from
their repository (``GF180_OSU_SC``, README.md), and the package's ngspice/Spectre copy of the cells;
rerun after a library update and commit the result:

    uv run python pdk/gf180/openroad/views.py

* ``gf180mcu_tech.lef``: the library's technology LEF (``tlef/``);
* ``lef/gf180mcu_osu_sc_gp9t3v3.lef``: the cells' LEF, each cell's rails (OBS in the library's,
  but for its fillers') as VDD and VSS pins, as the row cells and placers read supplies; each
  signal pin as its Metal2 pad alone (its Metal1 and Via1 in OBS): the layout flow reaches a pin
  through its pad (``stdcell_access``), as a router does;
* ``lib/``: the library's one Liberty (typical, 25 C, 3.30 V), gzipped;
* ``gds/gf180mcu_osu_sc_gp9t3v3.gds.gz``: the cells' GDS (one file a cell in the library) in one
  library, each with its outline on PR_bndry (0/0), which the library's cells lack, and its implants
  completed to the library's own band edges across its width (``_implants``: the library's stop
  short of the cell edges and its fillers have none);

  in both, the row cells' (``layout/tech.py`` STD_CELLS) pin pads trimmed to the M2 space from
  the rows' tracks beside their own (``PITCH``): the library's pads (0.4 um tall, on its 0.6 um pin
  grid) hold a track each, but reach to 0.26 um of a wire on the next, which a router does not know
  of (it sees the access bar on the pad's track);
* ``sp/gf180mcu_osu_sc_gp9t3v3.sp``: the cells' netlist with M lines on the PDK's device names
  (``nfet_03v3``, ``pfet_03v3``): LVS and the layout flow's library reader (``flow/layout/stdcells.py``);
* ``../hdl21/gf180mcu_osu_sc_gp9t3v3.spice``: the same cells with the library's X lines on the
  package's device names (``nfet_3v3``, ``pfet_3v3``: ``hdl21/*_devices.*``), which Spectre and ngspice
  read (Spectre cannot call the PDK's ``nfet_03v3`` by name, SFE-405);
* ``v/gf180mcu_osu_sc_gp9t3v3.v``: one instance of every Liberty cell (pdk/test_openroad.py).
"""

from __future__ import annotations

import gzip
import os
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "layout"))
import tech

ROOT = Path(os.environ.get("GF180_OSU_SC", "/users/kcaisley/Documents/libs/gf180mcu_osu_sc"))
NAME = "gf180mcu_osu_sc_gp9t3v3"
LIB = ROOT / NAME
LIBERTY = f"{NAME}_TT_25C.ccs.lib"
HEIGHT_UM = 6.3
RAIL_UM = 0.6  # each rail's M1 inside the cell: 0 to 0.6 (VSS) and H - 0.6 to H (VDD)
DEVICES = {"nfet_03v3": "nfet_3v3", "pfet_03v3": "pfet_3v3"}  # the PDK's names -> the package's


def _cells(text: str):
    """Each subcircuit of the library's SPICE: (name, pins, body lines)."""
    text = re.sub(r"\n\+", " ", text)
    for match in re.finditer(
        r"^\.subckt\s+(\S+)([^\n]*)\n(.*?)^\.ends", text, re.MULTILINE | re.DOTALL | re.IGNORECASE
    ):
        body = [line.split() for line in match.group(3).splitlines() if line.strip() and not line.startswith("*")]
        yield match.group(1), match.group(2).split(), body


def netlist(spice: str, cdl: bool) -> str:
    """The cells' netlist: M lines on the PDK's names (``cdl``) or X lines on the package's."""
    kind = "CDL, M lines on the PDK's device names" if cdl else "SPICE, X lines on the package's device names"
    out = [f"* {NAME} ({kind}) for FRIDA (pdk/gf180/openroad/views.py)"]
    for name, pins, body in _cells(spice):
        out.append(" ".join([".SUBCKT", name, *pins]))
        for fields in body:
            if fields[0][0] in "Xx":
                params = [f for f in fields if "=" in f]
                nets_model = [f for f in fields[1:] if "=" not in f]
                *nets, model = nets_model
                if cdl:
                    out.append(" ".join(["M" + fields[0][1:], *nets, model, *params]))
                else:
                    out.append(" ".join([fields[0], *nets, DEVICES.get(model, model), *params]))
            else:
                out.append(" ".join(fields))
        out += [".ENDS", ""]
    return "\n".join(out) + "\n"


def lef(text: str) -> str:
    """The cells' LEF, each cell's rails as its VDD and VSS pins (and no longer OBS)."""

    def macro(match: re.Match) -> str:
        body = match.group(0)
        width = float(re.search(r"SIZE\s+([\d.]+)\s+BY", body).group(1))
        head, obs = body.split("\n  OBS\n", 1) if "\n  OBS\n" in body else (body, None)
        rails = {"VSS": (0.0, RAIL_UM, "GROUND"), "VDD": (HEIGHT_UM - RAIL_UM, HEIGHT_UM, "POWER")}
        pins = ""
        for pin, (y0, y1, use) in rails.items():
            if re.search(rf"^\s*PIN {pin}\b", head, re.MULTILINE) or obs is None:
                continue
            obs = re.sub(rf"\n\s*RECT 0 {y0:g} {width:g} {y1:g} ;", "", obs)  # the rail leaves the obstructions
            pins += (
                f"  PIN {pin}\n    DIRECTION INOUT ;\n    USE {use} ;\n    SHAPE ABUTMENT ;\n    PORT\n"
                f"      LAYER Metal1 ;\n        RECT 0 {y0:g} {width:g} {y1:g} ;\n    END\n  END {pin}\n"
            )
        if obs is None:
            return body
        # each signal pin with a Metal2 pad: the pad alone, its Metal1 and Via1 shapes obstructions
        moved = []

        def pad_only(pin_match: re.Match) -> str:
            name, port = pin_match.group(1), pin_match.group(2)
            layers = re.findall(r"(      LAYER (\S+) ;\n(?:        RECT [^\n]*\n)+)", port)
            if name in rails or not any(layer == "Metal2" for _, layer in layers):
                return pin_match.group(0)
            for block, layer in layers:
                if layer != "Metal2":
                    moved.append(block.replace("      LAYER", "    LAYER").replace("        RECT", "      RECT"))
                    port = port.replace(block, "")
            return pin_match.group(0).replace(pin_match.group(2), port)

        head = re.sub(r"(?m)^  PIN (\S+)\n(.*?)^  END \1$", pad_only, head, flags=re.DOTALL)
        name = match.group(1)
        if name in tech.STD_CELLS:
            head = _trim(name, head)
        return head + "\n" + pins + "  OBS\n" + "".join(moved) + obs

    return re.sub(r"^MACRO (\S+)\n.*?^END \1$", macro, text, flags=re.DOTALL | re.MULTILINE)


TRIM: dict[str, list] = {}  # per row cell, (its pad's box, the y band kept) in nm


def _boxes(text: str, layer: str = "Metal2") -> list[tuple[int, int, int, int]]:
    """The RECTs (nm) on ``layer`` in a LEF PORT or OBS block."""
    out = []
    for block in re.findall(rf"LAYER {layer} ;\n((?:\s+RECT [^\n]*\n)+)", text):
        for r in re.findall(r"RECT (\S+) (\S+) (\S+) (\S+)", block):
            out.append(tuple(round(float(v) * 1000) for v in r))
    return out


def _trim(cell: str, head: str) -> str:
    """The pins of one row cell, each pad cut back to the M2 space from a wire on the tracks beside
    its own (the docstring above); TRIM gets the cuts for gds()."""
    hw, room = tech.M2W // 2, tech.PITCH - tech.M2W // 2 - tech.M2_SPACE
    tracks = [t for t in tech.STD_TRACKS if t % tech.PITCH == 0]
    cuts = []
    for match in re.finditer(r"(?m)^  PIN (\S+)\n(.*?)^  END \1$", head, re.DOTALL):
        if match.group(1) in tech.STD_SUPPLY or not (boxes := _boxes(match.group(2))):
            continue
        x0, y0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
        x1, y1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
        own = [t for t in tracks if y0 <= t - hw and t + hw <= y1]
        if not own:
            continue
        lo, hi = own[0] - room, own[0] + room
        if y0 >= lo and y1 <= hi:
            continue
        cuts.append(((x0, y0, x1, y1), (lo, hi)))
        block = match.group(2)
        for rect in re.findall(r"RECT \S+ \S+ \S+ \S+ ;", block):
            bx0, by0, bx1, by1 = (round(float(v) * 1000) for v in rect.split()[1:5])
            new = f"RECT {bx0 / 1000:g} {max(by0, lo) / 1000:g} {bx1 / 1000:g} {min(by1, hi) / 1000:g} ;"
            block = block.replace(rect, new)
        head = head.replace(match.group(0), match.group(0).replace(match.group(2), block))
    TRIM[cell] = cuts
    return head


def gds(out: Path) -> None:
    """The library's GDS (every cell, ``gds/<library>.gds``), each cell with its outline on PR_bndry
    (0/0)."""
    import klayout.db as kdb

    layout = kdb.Layout()
    layout.read(str(LIB / f"gds/{NAME}.gds"))
    boundary, m2 = layout.layer(0, 0), layout.layer(*tech.LAYERS["M2"])
    height = round(HEIGHT_UM / layout.dbu)
    for cell in layout.top_cells():
        found = re.search(rf"^MACRO {re.escape(cell.name)}\n.*?SIZE\s+([\d.]+)", _LEF, re.DOTALL | re.MULTILINE)
        if found:
            cell.shapes(boundary).insert(kdb.Box(0, 0, round(float(found.group(1)) / layout.dbu), height))
        if TRIM.get(cell.name):  # lef() first: the pads cut back from the tracks beside them
            metal = kdb.Region(cell.shapes(m2))
            for (x0, y0, x1, y1), (lo, hi) in TRIM[cell.name]:
                metal -= kdb.Region(kdb.Box(x0, y0, x1, y1)) - kdb.Region(kdb.Box(x0, lo, x1, hi))
            cell.shapes(m2).clear()
            cell.shapes(m2).insert(metal)
        if found:
            _implants(layout, cell, round(float(found.group(1)) / layout.dbu))
    layout.write(str(out))


# the library's own band edges, which its taps set: Pplus to 0.08 um above its P taps' COMP (0.6 um
# tall; NP.3cii keeps Nplus that far from them), Nplus from 5.54 um, where its N taps' Nplus starts
LIB_PP_TOP, LIB_NP_BOTTOM = 680, 5540


def _implants(layout, cell, width: int) -> None:
    """A cell's implants completed to the library's band profile across its whole width: Pplus
    to LIB_PP_TOP and STD_NW..LIB_NP_BOTTOM, Nplus LIB_PP_TOP..STD_NW and from LIB_NP_BOTTOM, the
    rail bands past the cell as the row cells' (-PP_TAP below it, to 2 H - NP_TAP above it), and
    the well to NW_TOP. The library's device implants stop 0.14 to 0.29 um short of the cell
    edges, its taps' implants reach past its bands near them, and its fillers have none, so cells
    and fillers abutting (or mirrored) left gaps and notches under the 0.4 um implant space (NP.2,
    PP.2); with every edge on the same bands they join, and a pad or row cell beside one meets
    implant edge to edge. The fill keeps off the other implant and the other type's COMP
    (NP.3cii, PP.3cii: 0.08 um) and drops what is narrower than the implant width (NP.1, PP.1), the
    neighbours' profile taken to continue past both edges."""
    import klayout.db as kdb

    od = kdb.Region(cell.begin_shapes_rec(layout.layer(*tech.LAYERS["OD"])))
    np_li, pp_li = layout.layer(*tech.LAYERS["NP"]), layout.layer(*tech.LAYERS["PP"])
    nplus, pplus = kdb.Region(cell.begin_shapes_rec(np_li)), kdb.Region(cell.begin_shapes_rec(pp_li))
    h, keep = round(HEIGHT_UM * 1000), 199  # keep: half the implant width (0.4 um), less 1 nm
    profile = {
        np_li: ((LIB_PP_TOP, tech.STD_NW), (LIB_NP_BOTTOM, 2 * h - tech.NP_TAP)),
        pp_li: ((-tech.PP_TAP, LIB_PP_TOP), (tech.STD_NW, LIB_NP_BOTTOM)),
    }
    # the other type's implant on a gate's poly within 0.32 um of the gate, touching included
    # (NP.12, PP.12): the library's own Pplus and Nplus islands at its gates' ends run on over them,
    # as boxes a grid step past them
    poly = kdb.Region(cell.begin_shapes_rec(layout.layer(*tech.LAYERS["PO"])))
    for li, imp, other, (y0, y1) in ((pp_li, pplus, nplus, (LIB_NP_BOTTOM, h)), (np_li, nplus, pplus, (0, LIB_PP_TOP))):
        rows = kdb.Region(kdb.Box(0, y0, width, y1))
        ends = (poly & (od & imp)).sized(319) & poly & rows
        for piece in ((imp & rows) + ends).merged().each():
            if not (kdb.Region(piece) & ends).is_empty():
                cell.shapes(li).insert(kdb.Region(piece.bbox().enlarged(tech.MFG_GRID, tech.MFG_GRID)) - other)
    nplus, pplus = kdb.Region(cell.begin_shapes_rec(np_li)), kdb.Region(cell.begin_shapes_rec(pp_li))
    keepout = {np_li: pplus + (od & pplus).sized(80), pp_li: nplus + (od & nplus).sized(80)}
    for li, bands in profile.items():
        fill = kdb.Region([kdb.Box(0, y0, width, y1) for y0, y1 in bands]) - keepout[li]
        beyond = kdb.Region(
            [kdb.Box(x0, y0, x1, y1) for y0, y1 in bands for x0, x1 in ((-2 * keep, 0), (width, width + 2 * keep))]
        )
        cell.shapes(li).insert((fill + beyond).merged().sized(-keep).sized(keep) & fill)
    # likewise the VDD band's well, which encloses a pad's or row cell's N tap there (DF.4d_LV)
    cell.shapes(layout.layer(*tech.LAYERS["NW"])).insert(kdb.Box(0, h, width, tech.NW_TOP))


def verilog(cells: list[str]) -> str:
    """One instance of each cell, unconnected (pdk/test_openroad.py links it)."""
    lines = [
        f"// One unconnected instance of every {NAME} cell: the design pdk/test_openroad.py links.",
        f"module {NAME} ();",
    ]
    lines += [f"  {cell} u{i} ();" for i, cell in enumerate(cells)]
    return "\n".join([*lines, "endmodule", ""])


def _gzip(src: Path, dst: Path) -> None:
    with src.open("rb") as file, gzip.GzipFile(dst, "wb", compresslevel=9, mtime=0) as out:
        shutil.copyfileobj(file, out)


_LEF = (LIB / f"lef/{NAME}.lef").read_text() if (LIB / f"lef/{NAME}.lef").exists() else ""


def main() -> None:
    for folder in ("lef", "lib", "gds", "sp", "v"):
        for old in (HERE / folder).glob("*"):
            old.unlink()
    for old in (HERE.parent / "hdl21").glob("gf180mcu_*.spice"):
        old.unlink()
    shutil.copyfile(LIB / f"tlef/{NAME}.tlef", HERE / "gf180mcu_tech.lef")
    (HERE / f"lef/{NAME}.lef").write_text(lef(_LEF))  # before gds(): the pads' trim (TRIM)
    _gzip(LIB / f"lib/{LIBERTY}", HERE / f"lib/{LIBERTY}.gz")
    plain = HERE / f"gds/{NAME}.gds"
    gds(plain)
    _gzip(plain, HERE / f"gds/{NAME}.gds.gz")
    plain.unlink()
    spice = (LIB / f"spice/{NAME}.spice").read_text()
    (HERE / f"sp/{NAME}.sp").write_text(netlist(spice, cdl=True))
    (HERE.parent / f"hdl21/{NAME}.spice").write_text(netlist(spice, cdl=False))
    liberty = (LIB / f"lib/{LIBERTY}").read_text()
    cells = sorted(set(re.findall(r"^\s*cell\s*\(\s*\"?([\w$]+)\"?\s*\)", liberty, re.MULTILINE)))
    (HERE / f"v/{NAME}.v").write_text(verilog(cells))


if __name__ == "__main__":
    main()
