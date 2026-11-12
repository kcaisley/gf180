"""Where the row cells find the gf180mcu_fd_sc_mcu7t5v0 standard cells and the access points derived from them.

No dependencies, so ALIGN's own Python can import it too. Each path can be overridden by the
environment variable of the same name.

- ``GF180MCU_FD_SC_MCU7T5V0``: the library directory of the open PDK
  (gf180mcuD/libs.ref/gf180mcu_fd_sc_mcu7t5v0: {gds,cdl,lef}); without it, this PDK's copy (``openroad/``).
- ``ROWS_ACCESS``: the cells' pin access points, written by ``stdcell_access.py`` into the
  superproject's ``build/layout/rows/``.
"""

import os
from pathlib import Path

_COPY = Path(__file__).resolve().parents[1] / "openroad"

if "GF180MCU_FD_SC_MCU7T5V0" in os.environ:
    _LIB = Path(os.environ["GF180MCU_FD_SC_MCU7T5V0"]).expanduser()
    STD_GDS = _LIB / "gds/gf180mcu_fd_sc_mcu7t5v0.gds"
    STD_SPICE = _LIB / "cdl/gf180mcu_fd_sc_mcu7t5v0.cdl"
    STD_LEF = _LIB / "lef/gf180mcu_fd_sc_mcu7t5v0.lef"
else:
    STD_GDS = _COPY / "gds/gf180mcu_fd_sc_mcu7t5v0.gds.gz"
    STD_SPICE = _COPY / "sp/gf180mcu_fd_sc_mcu7t5v0.sp"
    STD_LEF = _COPY / "lef/gf180mcu_fd_sc_mcu7t5v0.lef"
# the library's Liberty (typical corner: its cells, pins and functions are every corner's), which
# flow.circuit.cellmap reads for the hdl21 cell library
STD_LIBERTY = _COPY / "lib/gf180mcu_fd_sc_mcu7t5v0__tt_025C_5v00.lib.gz"
ACCESS_JSON = Path(
    os.environ.get(
        "ROWS_ACCESS", Path(__file__).resolve().parents[3] / "build/layout/rows/gf180mcu_fd_sc_mcu7t5v0_access.json"
    )
)
