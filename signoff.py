"""Signoff provider for frida's ``flow/layout/signoff.py``: DRC, LVS and extraction of a block in GF180MCU.

All open tools. DRC: gdscheck where installed, its embedded deck of the open PDK (``gf180mcuD``,
the core and antenna suites: what a block alone must pass) or, where this gdscheck lacks it, the
kit's precheck (``gdscheck/drc.yaml``); then the open PDK's KLayout deck without density
(``klayout/drc.py``). LVS: the open PDK's KLayout deck (``klayout/lvs.py``). Both decks need the
open PDK (``GF180_OPEN_PDK``). Extraction: KLayout-PEX by FasterCap on the kit's process stack
(``kpex/stack.json``), the layout's own net names (``flow.layout.kpex``). The checkers run in
``drc/``, ``lvs/`` and ``pex/`` under the run directory.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

from klayout import rdb

from pdk.gf180.klayout.drc import drc
from pdk.gf180.klayout.lvs import lvs

PRECHECK = Path(__file__).resolve().parent / "gdscheck" / "drc.yaml"
PROCESS = "gf180mcuD"  # gdscheck's embedded deck of the open PDK
SUITES = ("core", "antenna")  # its main less density and recommended


def _runs(executable: str) -> list[tuple[str, str]]:
    """gdscheck's (process, suite) runs: its embedded gf180mcuD core and antenna suites, else the
    kit's precheck."""
    listed = subprocess.run([executable, "list-processes"], capture_output=True, text=True, check=False).stdout
    if re.search(rf"^{PROCESS}\b", listed, re.MULTILINE):
        return [(PROCESS, suite) for suite in SUITES]
    return [(str(PRECHECK), "precheck")]


def _gdscheck(gds_path: Path, layout_top: str, run_dir: Path) -> dict[str, int]:
    """gdscheck's violations per rule (``gdscheck:<rule>``); none where gdscheck is not installed."""

    executable = shutil.which("gdscheck")
    if executable is None:
        return {}
    counts: dict[str, int] = {}
    for process, suite in _runs(executable):
        report = run_dir / f"gdscheck.{suite}.lyrdb"
        report.unlink(missing_ok=True)
        command = [executable, "run", "-i", str(gds_path), "-p", process, "-t", layout_top, "-s", suite]
        done = subprocess.run([*command, "-r", str(report)], capture_output=True, text=True, check=False)
        (run_dir / f"gdscheck.{suite}.log").write_text(done.stdout + done.stderr)
        if not report.exists():
            raise RuntimeError(f"gdscheck ({suite}) wrote no report; see {run_dir / f'gdscheck.{suite}.log'}")
        db = rdb.ReportDatabase("")
        db.load(str(report))
        for item in db.each_item():
            rule = f"gdscheck:{db.category_by_id(item.category_id()).name()}"
            counts[rule] = counts.get(rule, 0) + 1
    return counts


def _report(run_dir: Path, checker: str, found: dict[str, int], waived: re.Pattern[str] | None) -> Path:
    """``drc_violations.json``: the violated rules and the waived ones, with counts; raises when a
    rule outside the waivers is violated."""

    skip = {rule: n for rule, n in found.items() if waived is not None and waived.match(rule)}
    violations = {rule: n for rule, n in found.items() if rule not in skip}
    report = run_dir / "drc_violations.json"
    report.write_text(json.dumps({"checker": checker, "violations": violations, "waived": skip}, indent=1) + "\n")
    if violations:
        raise RuntimeError(f"DRC: {len(violations)} rules violated; see {report}")
    return report


def run_drc(*, run_dir: Path, gds_path: Path, layout_top: str, options: object = None) -> Path:
    """gdscheck, then KLayout DRC; returns ``drc_violations.json`` and raises unless clean."""

    work = run_dir / "drc"
    work.mkdir(parents=True, exist_ok=True)
    found = _gdscheck(gds_path, layout_top, work) | drc(gds_path, layout_top, work)
    return _report(run_dir, "klayout", found, None)


def run_lvs(
    *, run_dir: Path, gds_path: Path, source_path: Path, layout_top: str, source_top: str, options: object = None
) -> tuple[bool, Path]:
    """KLayout LVS in ``lvs/``: whether the netlists match, and its log."""

    return lvs(gds_path, layout_top, source_path, source_top, run_dir / "lvs")


def run_pex(
    *,
    run_dir: Path,
    gds_path: Path,
    source_path: Path,
    layout_top: str,
    source_top: str,
    output_stem: str,
    options: object = None,
) -> Path:
    """KLayout-PEX (FasterCap) of the layout in ``pex/``, by its own net names (the kit has no
    extractor that reads a schematic): the Spectre netlist of its nets' capacitances."""

    from flow.layout.kpex import run_layout_pex

    del source_path, source_top, options
    return run_layout_pex("gf180", gds_path, layout_top, output_stem, run_dir / "pex")


def run_layout_pex(*, run_dir: Path, gds_path: Path, layout_top: str, output_stem: str) -> Path:
    """The kit's own extraction of a layout by its own net names (``Extractor.CALIBRE`` names the
    kit's extractor, which for an open PDK is KLayout-PEX too): FasterCap on ``kpex/stack.json`` in
    ``pex/``."""

    from flow.layout.kpex import run_layout_pex as extract

    return extract("gf180", gds_path, layout_top, output_stem, run_dir / "pex")
