"""Where the row cells find the gf180mcu_osu_sc_gp9t3v3 standard cells and the access points derived from them.

No dependencies, so ALIGN's own Python can import it too. Each path can be overridden by the
environment variable of the same name.

- ``GF180MCU_OSU_SC_GP9T3V3``: a directory of the library's views laid out as this PDK's copy
  (``openroad/``: gds/, sp/, lef/, the cells' outlines and rail pins added: openroad/views.py);
  without it, this PDK's copy.
- ``ROWS_ACCESS``: the cells' pin access points, written by ``stdcell_access.py`` into the
  superproject's ``build/layout/rows/``.
"""

import os
from pathlib import Path

_COPY = Path(__file__).resolve().parents[1] / "openroad"
_LIB = Path(os.environ["GF180MCU_OSU_SC_GP9T3V3"]).expanduser() if "GF180MCU_OSU_SC_GP9T3V3" in os.environ else _COPY

STD_GDS = _LIB / "gds/gf180mcu_osu_sc_gp9t3v3.gds.gz"
STD_SPICE = _LIB / "sp/gf180mcu_osu_sc_gp9t3v3.sp"
STD_LEF = _LIB / "lef/gf180mcu_osu_sc_gp9t3v3.lef"
# the library's Liberty (typical corner, its only one: its cells, pins and functions), which
# flow.circuit.cellmap reads for the hdl21 cell library
STD_LIBERTY = _COPY / "lib/gf180mcu_osu_sc_gp9t3v3_TT_25C.ccs.lib.gz"
ACCESS_JSON = Path(
    os.environ.get(
        "ROWS_ACCESS", Path(__file__).resolve().parents[3] / "build/layout/rows/gf180mcu_osu_sc_gp9t3v3_access.json"
    )
)
