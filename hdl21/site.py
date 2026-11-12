"""Site-local GF180MCU installation: the open PDK fetched by ciel (README.md), whose ngspice models,
KLayout decks and standard cells the kit reads, and the kit's copy of the standard cells' CDL."""

import os
from pathlib import Path

from .pdk_logic import VARIANT, Install

# the gf180mcuD variant under the ciel PDK root (open_pdks bd4da56c, README.md)
PDK_PATH = Path(os.environ.get("GF180_OPEN_PDK", "/users/kcaisley/Documents/libs/gf180mcu-open-pdk"), VARIANT)
# the standard cells' CDL (this package's copy of gf180mcu_osu_sc_gp9t3v3's: openroad/views.py)
STDCELL_PATH = Path(__file__).resolve().parents[1] / "openroad/sp/gf180mcu_osu_sc_gp9t3v3.sp"
install = Install(pdk_path=PDK_PATH, stdcell_path=STDCELL_PATH)
MODEL_FILES = tuple(install.pdk_path / relative for relative in Install.LOCAL_SPICE_FILES)
