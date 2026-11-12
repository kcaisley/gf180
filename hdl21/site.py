"""Site-local GF180MCU installation: the open PDK, an open_pdks release installed by ciel (its PDK
root, holding gf180mcuD/libs.ref and gf180mcuD/libs.tech; README.md has the version)."""

import os
from pathlib import Path

from .pdk_logic import Install

PDK_PATH = Path(os.environ.get("GF180_OPEN_PDK", "/users/kcaisley/Documents/libs/gf180mcu-open-pdk"))
install = Install(pdk_path=PDK_PATH)
MODEL_FILES = tuple(install.pdk_path / relative for relative in Install.LOCAL_SPICE_FILES)
