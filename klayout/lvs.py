"""GF180MCU LVS with the open PDK's KLayout deck (gf180mcuD): CORRECT or not.

    uv run python pdk/gf180/klayout/lvs.py GDS TOP SOURCE SOURCE_TOP RUN_DIR

The deck pairs the top cells by name: the source's top subcircuit is renamed to the layout's. It
runs as the deck's own ``run_lvs.py --variant=D --combine --top_lvl_pins`` does (its switches
given to KLayout here, without the script's docopt dependency).

The deck: ``$GF180_OPEN_PDK`` (default ~/Documents/libs/gf180mcu-open-pdk)/gf180mcuD/libs.tech/klayout/tech/lvs.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

DECK = (
    Path(os.environ.get("GF180_OPEN_PDK", "~/Documents/libs/gf180mcu-open-pdk")).expanduser()
    / "gf180mcuD/libs.tech/klayout/tech/lvs"
)
# run_lvs.py's switches for variant D (five metals, 11 kA top metal, MIM option B, 1 kohm/sq poly
# resistor, 2 fF/um2 MIM), devices combined, the top cell's pins from its labels
SWITCHES = {
    "thr": "8",
    "run_mode": "deep",
    "metal_top": "11K",
    "mim_option": "B",
    "metal_level": "5LM",
    "poly_res": "1k",
    "mim_cap": "2",
    "lvs_sub": "gf180mcu_gnd",
    "verbose": "false",
    "spice_net_names": "true",
    "spice_comments": "false",
    "scale": "false",
    "schematic_simplify": "false",
    "net_only": "false",
    "top_lvl_pins": "true",
    "combine": "true",
    "purge": "false",
    "purge_nets": "false",
}


def lvs(gds: Path, top: str, source: Path, source_top: str, run_dir: Path) -> tuple[bool, Path]:
    """Whether the layout's ``top`` matches the source's ``source_top``, and the run's log (the
    LVS database ``<gds stem>.lvsdb`` and the extracted netlist beside it)."""
    if not (DECK / "gf180mcu.lvs").is_file():
        raise FileNotFoundError(f"no GF180MCU LVS deck at {DECK}: set GF180_OPEN_PDK to the open PDK's install")
    run_dir = Path(run_dir).resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    renamed = run_dir / "source.cdl"
    renamed.write_text(
        re.sub(rf"(?im)^(\.subckt|\.ends)(\s+){re.escape(source_top)}\b", rf"\1\2{top}", Path(source).read_text())
    )
    stem = Path(gds).name.split(".")[0]
    switches = {
        **SWITCHES,
        "topcell": top,
        "input": str(Path(gds).resolve()),
        "schematic": str(renamed),
        "report": str(run_dir / f"{stem}.lvsdb"),
        "target_netlist": str(run_dir / f"{stem}.cir"),
    }
    cmd = ["klayout", "-b", "-r", str(DECK / "gf180mcu.lvs")]
    for key, value in switches.items():
        cmd += ["-rd", f"{key}={value}"]
    from flow.logs import run_logged

    # its whole output in run_lvs.log and the flow's log (klayout.lvs), a mismatch not a failure
    text = run_logged(cmd, cwd=run_dir, log=run_dir / "run_lvs.log", name="klayout.lvs", allowed=tuple(range(256)))
    ok = "Congratulations! Netlists match" in text
    return ok, run_dir / "run_lvs.log"


if __name__ == "__main__":
    ok, log = lvs(Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]), sys.argv[4], Path(sys.argv[5]))
    print(f"LVS {'CORRECT' if ok else 'INCORRECT'}: {log}")
