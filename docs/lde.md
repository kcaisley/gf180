# Layout-Dependent Effects (LDE): GF180MCU

- The kit's core devices `nfet_3v3` and `pfet_3v3` (`hdl21/spectre_devices.scs`,
  `hdl21/ngspice_devices.spice`) call the open PDK's `nfet_03v3` and `pfet_03v3` by X line:
  subcircuit wrappers in `sm141064.ngspice` (section `fets_mm`) around the **3.3 V BSIM4** model
  cards (`nfet_03v3`, `pfet_03v3`: level 54, version 4.5, 16 bins each; sections `nfet_03v3_t`,
  `_f`, `_s`, `_fs`, `_sf`). The package's own name exists because Spectre cannot instance
  `nfet_03v3` by name (subcircuit and model cards alike named, SFE-405); the LVS source names the
  PDK's device (`netlist/lvs.py`). The gf180mcu_osu_sc_gp9t3v3 cells are made of the same devices.
- The wrappers take `w` (total), `l`, `nf`, `m`, `as/ad/ps/pd`, `nrd/nrs`, `sa`, `sb`, `sd`,
  `par`, `dtemp`, and pass `sa`, `sb`, `sd` to the card; but the cards switch **LOD off**
  (`ku0 = kvth0 = kvsat = 0`; `saref = sbref = 0.44 um` without effect) and **WPE off** (no
  `web`, `wec`, `kvth0we`, `k2we`, `ku0we`: BSIM4's defaults, 0).
- PSE, OSE, MBE and CESL are not modeled.
- **Junction areas and perimeters**: the wrappers default `as = ad = ps = pd = 0` and pass them on
  as given, and BSIM4 reads a given 0 as no junction: a netlist that gives none simulates without
  source and drain junction capacitance. This package's compile pass gives every MOS the row
  cells' own diffusions (`hdl21/pdk_logic.py` `junctions`: an outer strip 0.44 um along the
  channel, a shared one 0.52 um, gate edges in the perimeters), which is what the open KLayout
  LVS deck extracts (`AS`, `AD`, `PS`, `PD`) for the same device.
- **Gate resistance and NQS** are off in the cards (`rgatemod = 0`, `trnqsmod = acnqsmod = 0`),
  as are the body resistance network (`rbodymod = 0`) and the S/D resistance network
  (`rdsmod = 0`); there is no `rgflag`, `ccoflag` or `rcoflag`.
- **Corners**: the model library's `ff` and `ss` sections switch the 3.3 V cards (`nfet_03v3_f`,
  `_s`): the core devices' process varies with a FAST or SLOW run (nfet +16 % / -16 % drain
  current at 3 / 0.28 um), besides the supply (`SUPPLY_RAILS`) and temperature. The 6 V cards,
  and so the 5 V I/O devices on them, stay at typical in every section (`nfet_06v0_t`).
- **Mismatch** is the wrappers' own: `delvto` and `mulu0` from `agauss` draws scaled by
  `sw_stat_mismatch` (0 in `design.ngspice`); there is no Spectre statistics block.
- The open KLayout LVS (`libs.tech/klayout/tech/lvs`) extracts `W`, `L`, the junctions and
  compares `W` and `L`; nothing for LOD or WPE.
- Interconnect parasitics are not in the device models; they come from extraction (KLayout-PEX).

FRIDA's layouts therefore need no LDE-driven sizing in GF180MCU: matching relies on the usual
symmetry (common centroid, dummies) rather than on the model.

### Sources

- [sm141064.ngspice](file:///users/kcaisley/Documents/libs/gf180mcu-open-pdk/gf180mcuD/libs.tech/ngspice/sm141064.ngspice) — corner sections, the `fets_mm` wrappers (`nfet_03v3`, `pfet_03v3`), the BSIM4 cards (`nfet_03v3_t`, `pfet_03v3_t`, ...)
- [design.ngspice](file:///users/kcaisley/Documents/libs/gf180mcu-open-pdk/gf180mcuD/libs.tech/ngspice/design.ngspice) — statistics and noise-corner switches
- [mos_extraction.lvs](file:///users/kcaisley/Documents/libs/gf180mcu-open-pdk/gf180mcuD/libs.tech/klayout/tech/lvs/rule_decks/mos_extraction.lvs) — the LVS deck's MOS devices and their parameters

## Flags

| Effect | Type | Flag | Setting | Default |
|--------|------|------|---------|---------|
| LOD / STI stress | LDE | — | `sa`/`sb` passed; `ku0 = kvth0 = kvsat = 0` | Not modeled |
| Poly Spacing Effect (PSE) | LDE | — | — | Not modeled |
| OD Spacing Effect (OSE) | LDE | — | — | Not modeled |
| Well Proximity Effect (WPE) | LDE | — | no `web`, `wec` (0) | Not modeled |
| Metal Boundary Effect (MBE) | LDE | — | — | Not modeled |
| Contact Etch Stop Liner (CESL) | LDE | — | — | Not modeled |
| Contact-to-poly parasitic capacitance (CCO) | Pre-layout | — | — | Not modeled |
| Poly gate resistance (RG) | Pre-layout | `rgatemod` | `rgatemod = 0` in the cards | Off |
| S/D contact resistance (RCO) | Pre-layout | `rdsmod` | `rdsmod = 0` in the cards | Off |
| S/D junctions | Pre-layout | `as/ad/ps/pd` | given by the compile pass (`junctions`) | **0** in the wrappers |

The same notes for the other PDKs: `pdk/<kit>/docs/lde.md`.
