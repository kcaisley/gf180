# GF180 HDL21 PDK

HDL21 device compilation and FRIDA layout and signoff data for the open GlobalFoundries 180 nm MCU
PDK (GF180MCU), variant **gf180mcuD**: five metals (Metal1 to Metal4 and an 11 kA top metal,
Metal5), MIM option B, the 1 kohm/sq poly resistor. The repository holds no PDK model files: the
models, the standard cells' sources and the KLayout decks are the open PDK's, installed beside it.

Its HDL21 integration derives from the Hdl21 GF180 package (`pdks/Gf180`) and keeps that package's
BSD 3-Clause license and attribution.

FRIDA mounts this repository at `pdk/gf180`, where it is imported as `pdk.gf180`. Run its tests
from a FRIDA checkout:

```text
uv run pytest pdk/gf180/tests
uv run pytest pdk/gf180/tests -m site_pdk
```

## The open PDK

open_pdks release **2026.10.20**, commit `bd4da56c564e6d57794cd4cf4f8cbf807230f608`, installed by
ciel 3.2.0 (all of the family's variants; this kit uses gf180mcuD):

```text
uvx ciel==3.2.0 enable --pdk-root ~/Documents/libs/gf180mcu-open-pdk \
    --pdk-family gf180mcu bd4da56c564e6d57794cd4cf4f8cbf807230f608
```

`GF180_OPEN_PDK` names the ciel PDK root (default `~/Documents/libs/gf180mcu-open-pdk`, read by
`hdl21/site.py`, `klayout/drc.py`, `klayout/lvs.py`, `openroad/views.py`); the kit reads
`$GF180_OPEN_PDK/gf180mcuD/libs.ref` and `.../libs.tech`. `gf180mcuD/SOURCES` names the release.

## Choices

- **Standard cells: gf180mcu_fd_sc_mcu7t5v0** (7 tracks, 3.92 um rows of 0.56 um sites), LibreLane's
  default for gf180mcuD and denser than mcu9t5v0's 5.04 um rows; their rows are the row cells'.
- **Core devices: nfet_05v0 / pfet_05v0**, the 5 V devices the cells are made of (Dualgate and
  V5_XTOR, L >= 0.6 / 0.5 um, on the 6 V family's cards); **VDD 5.0 V** (4.5 / 5.5 V corners, the
  cells' tt_025C_5v00 and ss_125C_4v50 Liberty). The 6 V devices are the I/O family. The 3.3 V
  devices are left out: their PMOS cannot share an N-well with the cells' (DV.9) and the rows'
  wells run unbroken.
- **Poly resistor: ppolyf_u** (unsalicided P+, 350 ohm/sq); **MOM capacitors** on Metal2 to Metal4.
- **Simulators**: Spectre and ngspice both read the open PDK's ngspice decks (Spectre takes their
  SPICE as it is), so FRIDA's Spectre flows run here unchanged. The 6 V devices are not
  instanced by name in Spectre: the decks name a subcircuit and model cards alike `nfet_06v0`
  (`Install.UNMODELED`). The decks' `ff` / `ss` sections vary the 3.3 V devices only
  (`docs/lde.md`).
- **Signoff: open tools.** DRC: gdscheck's embedded gf180mcuD deck (core and antenna suites; the
  kit's own `gdscheck/drc.yaml` is a metal-stack precheck where a gdscheck lacks it) and the open
  PDK's KLayout deck without density (`klayout/drc.py`). LVS: the open PDK's KLayout deck
  (`klayout/lvs.py`). Extraction: KLayout-PEX by FasterCap on `kpex/stack.json` (its 2.5-D
  coefficients in `kpex/parasitics.json`, kpex's own gf180mcuD ones).

## Contents

| Path | Contents |
| --- | --- |
| `hdl21/` | devices (`pdk_data`, `primitives`), the compile pass and the site installation (`pdk_logic`, `site`), the logic cells (`stdcells`), the generic cell library (`cells.py`, written by `flow.circuit.cellmap`), the device names the decks lack (`spectre_devices.scs`, `ngspice_devices.spice`), the cells for ngspice (`gf180mcu_fd_sc_mcu7t5v0.spice`) |
| `layout/` | the row profile and rules (`tech.py`, `README.md`), the library locations (`paths.py`), ALIGN's files written by `flow/layout/make_pdk.py` (`layers.json`, `models.sp`, `rows.json`, `user_template.sp`), `netlists/` |
| `netlist/lvs.py` | the LVS source rules |
| `signoff.py` | the signoff provider of `flow/layout/signoff.py` |
| `klayout/` | layer palette and technology (`.lyp`, `.lyt`, `.lyd25`, `.map`, the open PDK's), DRC and LVS on its decks |
| `gdscheck/` | the metal-stack precheck |
| `kpex/` | the process stack and 2.5-D coefficients for KLayout-PEX |
| `openroad/` | tech LEF, the cells' `lef/ lib/ gds/ sp/`, `v/` (every cell once), `init.tcl`; `views.py` writes them from the open PDK |
| `devices/` | the precharacterized device tables (`flow/layout/devices`) |
| `docs/lde.md` | layout-dependent effects in the models |
| `tests/` | the kit's tests |

## Regenerating

```text
uv run python pdk/gf180/openroad/views.py                                     # openroad/, hdl21/*.spice
uv run python -c "from flow.layout.pdkproc import in_pdk; in_pdk('gf180', 'flow.layout.make_pdk', 'build', 'gf180')"
uv run python -c "from flow.circuit.cellmap import write_library; write_library('gf180')"
uv run python -m flow.layout.devices.mosfet.characterize gf180                # also moscap, polyres (Spectre)
uv run python -m flow.layout.devices.momcap.characterize gf180 --workers 8    # KLayout-PEX
```

## Limits

- The row engine ties wells only at row ends (`EDGE_TIE`); the filltie's taps reach 15 um
  (DF.13_MV, DF.14_MV), so rows wider than about 30 um fail those rules.
- The passivation above Metal5 in `kpex/stack.json` is assumed (1.0 um oxide, 0.7 um nitride):
  kpex's gf180mcuD stack gives its permittivities, not its thicknesses. It touches Metal5 alone.
