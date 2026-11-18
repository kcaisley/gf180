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
`hdl21/site.py`, `klayout/drc.py`, `klayout/lvs.py`); the kit reads
`$GF180_OPEN_PDK/gf180mcuD/libs.tech`. `gf180mcuD/SOURCES` names the release.

## The standard cells

Oklahoma State's **gf180mcu_osu_sc_gp9t3v3** (3.3 V, 9 tracks, 6.3 um rows, 0.1 um sites), from
their repository at commit `8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3` (the one open_pdks names;
the open PDK installs only the 5 V libraries):

```text
git clone https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc ~/Documents/libs/gf180mcu_osu_sc
git -C ~/Documents/libs/gf180mcu_osu_sc checkout 8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3
```

`GF180_OSU_SC` names the clone (default `~/Documents/libs/gf180mcu_osu_sc`), which only
`openroad/views.py` reads: the kit carries its own views of the cells (`openroad/`,
`hdl21/gf180mcu_osu_sc_gp9t3v3.spice`), derived from the library's under its Apache License 2.0. The library's Liberty (Cadence Liberate, CCS) has one
corner, typical at 25 C and 3.30 V; OpenSTA reads it (three warnings: the flops' timing on Q
related to QN).

## Choices

- **Core devices: nfet_03v3 / pfet_03v3** (the package's `nfet_3v3` / `pfet_3v3`, see Simulators),
  the 3.3 V devices the cells are made of, at frida's unit length 0.28 um, their minimum; **VDD
  3.3 V** (2.97 / 3.63 V corners). The 5 V devices (`nfet_05v0`, `pfet_05v0`, Dualgate and
  V5_XTOR) are the I/O family; the 6 V devices are left out.
- **Standard cells: gf180mcu_osu_sc_gp9t3v3**, the open 3.3 V library (above); their rows are the
  row cells' (M2 tracks at 0.63 um, ten a row, so that each of the library's pin pads, on its
  0.6 um grid, holds one). The kit's views change the library's (`openroad/views.py`): the rails
  are VDD / VSS pins (the library's LEF has none), each signal pin is its Metal2 pad (the row
  cells' pads trimmed 20 nm where they came within the M2 space of the next track), and each
  cell's implants are completed to the rows' band profile, with a PR boundary (the library stops
  its implants short of the cell edges and gives its fillers none).
- **Poly resistor: ppolyf_u** (unsalicided P+, 350 ohm/sq); **MOM capacitors** on Metal3 to
  Metal5 (the array units' channels need Metal2 below the plates: a three-layer unit takes the
  thick top metal).
- **Simulators**: Spectre and ngspice both read the open PDK's ngspice decks (Spectre takes their
  SPICE as it is), so FRIDA's Spectre flows run here unchanged, but for one name: the decks call a
  subcircuit and its model cards alike `nfet_03v3` (and `pfet_03v3`), which Spectre cannot
  instance (SFE-405), so the package calls them through `nfet_3v3` / `pfet_3v3` (`hdl21/*_devices.*`,
  and the cells' SPICE copy); the LVS source names the PDK's devices (`netlist/lvs.py`). The decks'
  MOS wrappers leave the source and drain junctions out unless given: the compile pass gives the
  row cells' own. The decks' `ff` / `ss` sections vary the 3.3 V devices (`docs/lde.md`).
- **Signoff: open tools.** DRC (`signoff.run_drc`): gdscheck's embedded gf180mcuD deck (core and
  antenna suites; the kit's own `gdscheck/drc.yaml` is a metal-stack precheck, which frida's CLI
  runs until its `GDSCHECK_PROCESSES` names gf180mcuD) and the open PDK's KLayout deck without
  density (`klayout/drc.py`). LVS: the open PDK's KLayout deck
  (`klayout/lvs.py`). Extraction: KLayout-PEX by FasterCap on `kpex/stack.json` (its 2.5-D
  coefficients in `kpex/parasitics.json`, fitted to 2-D field solves in that stack).

## Contents

| Path | Contents |
| --- | --- |
| `hdl21/` | devices (`pdk_data`, `primitives`), the compile pass and the site installation (`pdk_logic`, `site`), the logic cells (`stdcells`), the generic cell library (`cells.py`, written by `flow.circuit.cellmap`), the device names Spectre needs and the decks lack (`spectre_devices.scs`, `ngspice_devices.spice`), the cells for Spectre and ngspice (`gf180mcu_osu_sc_gp9t3v3.spice`) |
| `layout/` | the row profile and rules (`tech.py`, `README.md`), the library locations (`paths.py`), ALIGN's files written by `flow/layout/make_pdk.py` (`layers.json`, `models.sp`, `rows.json`, `user_template.sp`), `netlists/` |
| `netlist/lvs.py` | the LVS source rules |
| `signoff.py` | the signoff provider of `flow/layout/signoff.py` |
| `klayout/` | layer palette and technology (`.lyp`, `.lyt`, `.lyd25`, `.map`, the open PDK's), DRC and LVS on its decks |
| `gdscheck/` | the metal-stack precheck |
| `kpex/` | the process stack and 2.5-D coefficients for KLayout-PEX |
| `openroad/` | tech LEF, the cells' `lef/ lib/ gds/ sp/`, `v/` (every cell once), `init.tcl`; `views.py` writes them from the library's repository |
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

## Notes

- The library's taps sit inside each cell (contacts 0.265 to 0.485 um from the rail line), the
  row cells' and the wrappers' pads' on the rail line (`rowcell.rails`, `std_pad`): where a
  library cell and a row cell or pad face each other across a rail, their contacts come 0.155 um
  apart (CO.2a; comp's StrongARM: 84 markers, all else clean, LVS correct). Rows of library cells,
  rows of row cells, and the two mixed within a row are clean; the row engine needs a tap offset
  to match the library across a rail.
- The library has one Liberty corner (typical); there is no NOR2 of drive 2, and its `decap_1`
  leaves its gates floating (no decap cell in `pdk_logic`).
- The passivation above Metal5 in `kpex/stack.json` is assumed (1.0 um oxide, 0.7 um nitride):
  kpex's gf180mcuD stack gives its permittivities, not its thicknesses. It touches Metal5 alone.
