# Layout (GF180MCU)

The PDK's layout description, shared by every generator and layout tool: the layers, the metal and
via rules, and the values of the row cells (cells one standard-cell row tall,
gf180mcu_fd_sc_mcu7t5v0), so analog blocks place like digital logic and share rows, rails and wells
with the library. The generators themselves know no PDK: the row engine and the ALIGN driver are
in `flow/layout/`, and everything they generate goes to the superproject's `build/layout/`.

| Module | Contents |
| --- | --- |
| `tech.py` | layers (`LAYERS`), DBU and grid, metal and via rules (`RULES`), and the row profile and rule values the row engine draws with |
| `paths.py` | library and access-point locations |
| `netlists/` | the PDK's hand-written test netlists (`mos_inv.sp`, the single-device test) |

## Row profile (the row cells)

nm, cell frame R0 (VSS at the bottom), from `tech.py`:

| | NMOS | PMOS |
| --- | --- | --- |
| diffusion (`OD_LIMIT`) | 520..2320 | 1600..3400 |
| gate bar and its M2 track (`GATE_TRACK`) | 2800 | 1120 |
| S/D M2 tracks (`SD_TRACKS`) | 1120 1680 2240 | 2800 2240 1680 |
| device implant (`DEV_IMP`) | Nplus 200..3720 | Pplus 200..3720 |
| N-well (`NW_N`, `NW_P`, `NW_TOP`) | 3200..4350 | 1000..4350 |

Row height `H` = 3920, M2 track pitch `PITCH` = 560, placement grid `XPITCH` = 560, rail half
width `RAIL` = 300, widest finger `W_MAX` = 1800 (six 300 nm units), diffusion to the cell edge
`EDGE` = 600; MOS models nfet_05v0 / pfet_05v0 (the 5 V core; frida's unit length 600 for both, the NMOS's minimum).

## Notes

- The rules are the 5 V devices' (`_MV`): 0.6 um from a diffusion to the other type's well
  (DF.4c_MV, DF.16_MV) sets `EDGE`, 0.3 um from field poly to a diffusion (PL.5a_MV) the room
  between a diffusion and its gate bar, 0.4 um of diffusion past a gate (DF.6_MV) `OD_EXT`.
- Every row cell carries Dualgate and V5_XTOR over its whole frame (`VT_MARKS`, `VT_BAND`), as the
  library cells do: the LVS deck reads a gate under both as nfet_05v0 / pfet_05v0. The 3.3 V
  devices are not drawn: their PMOS cannot share an N-well with the cells' 5 V ones (DV.9).
- No diffusion and no taps under the rails (`RAIL_OD`, `RAIL_TAPS = False`): the implants run on
  over them (Nplus at VSS, Pplus at VDD, `RAIL_IMPLANTS`), and the library's filltie
  (`EDGE_TIE`) at every row end ties the wells. Its taps reach 15 um (DF.13_MV, DF.14_MV): a row
  wider than about 30 um needs a tie inside it too, which the row engine does not place.
- The library cells keep their LVPWELL (the P-well marker under their NMOS half, 0.43 um past
  them); the row cells draw none, and an isolated library cell's pads (`ISO_PAD`) hold its
  overhang. The cells' well pins (VNW, VPW) are on their rails in this kit's netlists of them.
- Library pins sit on the library's own tracks, half a pitch off the rows' M2 tracks
  (`PIN_PITCH`): the access tracks (`STD_TRACKS`) include both.
- The poly resistor is ppolyf_u (350 ohm/sq, 0.8 um wide, `RES`): SAB, RES_MK and Pplus as the
  PDK's own resistor cells; its cell keeps its Pplus 0.4 um from a neighbour's (`RULES["PO"]`).
- MOM capacitors stack Metal3 to Metal5 (`MOM_LAYERS`): an array unit's channels need Metal2 below
  its plates, so a three-layer unit takes the 11 kA top metal, whose rules (0.44 / 0.46 um) `RULES`
  takes at 0.56 / 0.56 um: the fingers share them, and a unit abuts on the rows' 0.56 um grid.
- MOS fingers are `nf` in the models; `w` is the total width.
