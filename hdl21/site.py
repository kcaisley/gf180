"""Site-local GF180MCU installation: the open PDK, an open_pdks release installed by ciel (its PDK
root, holding gf180mcuD/libs.ref and gf180mcuD/libs.tech; README.md has the version)."""

import os
from pathlib import Path

from .pdk_logic import Install

PDK_PATH = Path(os.environ.get("GF180_OPEN_PDK", "/users/kcaisley/Documents/libs/gf180mcu-open-pdk"))
# the standard cells' CDL, the wells on the rails (this package's copy: openroad/views.py)
STDCELL_PATH = Path(__file__).resolve().parents[1] / "openroad/sp/gf180mcu_fd_sc_mcu7t5v0.sp"
install = Install(pdk_path=PDK_PATH, stdcell_path=STDCELL_PATH)
MODEL_FILES = tuple(install.pdk_path / relative for relative in Install.LOCAL_SPICE_FILES)
