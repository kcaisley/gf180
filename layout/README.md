# Layout (GF180MCU)

The PDK's layout description, shared by every generator and layout tool: the layers, the metal and
via rules, and the values of the row cells (cells one standard-cell row tall,
gf180mcu_osu_sc_gp9t3v3), so analog blocks place like digital logic and share rows, rails and wells
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
| diffusion (`OD_LIMIT`) | 920..3500 | 2800..5310 |
| gate bar and its M2 track (`GATE_TRACK`) | 3780 | 2520 |
| S/D M2 tracks (`SD_TRACKS`) | 1260 1890 2520 3150 | 3150 3780 4410 5040 |
| device implant (`DEV_IMP`) | Nplus 680..5620 | Pplus 680..5620 |
| rail taps (`TAP_Y`, `TAP_OD`) | 150..600 above VSS | 150..600 below VDD |
| N-well (`NW_N`, `NW_P`, `NW_TOP`) | 3930..6730 | 2370..6730 |

Row height `H` = 6300, M2 track pitch `PITCH` = 630 (ten tracks a row), placement grid `XPITCH` =
600, rail half width `RAIL` = 600, widest finger `W_MAX` = 2230 (ten 220 nm units; the bands hold
2580 / 2510), diffusion to the cell edge `EDGE` = 430; MOS models nfet_3v3 / pfet_3v3 (the decks'
nfet_03v3 / pfet_03v3, L >= 280).

## Notes

- The rules are the 3.3 V devices' (`_LV`): 0.43 um from a diffusion to the other type's well
  (DF.4c_LV, DF.16_LV) sets `EDGE`, 0.1 um from field poly to a diffusion (PL.5a_LV) and 0.17 um
  from a gate contact (CO.8) the room between a diffusion and its gate bar, 0.23 um of implant past
  a gate (NP.5a, PP.5a) the PMOS diffusion's end against the VDD band; the NMOS diffusion starts
  0.32 um from the VSS tap (its poly end 0.1 um from it, PL.5a_LV).
- The library's rails lie inside its cells (M1 0..0.6 um from either edge, a tap under each: P+
  under VSS, N+ under VDD); rows alternate R0 / MX, so where two rows meet the rail is 1.2 um, as
  the row cells draw it (`RAIL` 600 about the line, `RAIL_OD`, `RAIL_TAPS`): every cell ties its
  wells, no tie cell at the row ends. The taps lie inside each cell as the library's, 0.375 um
  from the rail line (`TAP_Y`: diffusion 0.15 to 0.6 um, contacts 0.265 to 0.485 um), so a row
  cell's and a library cell's across a rail keep CO.2a and DF.3a_LV. The rail bands' implants are
  the library's (Pplus 0.68 um about VSS, Nplus from 0.68 um below VDD, 0.08 past the taps: NP.3cii,
  PP.3ci); deeper, a row cell's Nplus band would cover the library's Pplus beside its PMOS gates
  across the rail (NP.12).
- The library's N-well starts at 3.2 um (`STD_NW`); the row cells' VDD band overhangs 0.43 um
  past them and 0.43 um into the next row, enclosing the VDD tap (DF.4d_LV), as the kit's copy of
  the library's cells now does too.
- Library pins are Metal2 pads (0.5 x 0.4 um) on the library's 0.6 um pin grid (2.55, 3.15,
  3.75 um). The M2 pitch is 0.63 um so that each pad holds a track (2.52, 3.15, 3.78 um): the pin
  is a direct M2 access there (`STD_TRACKS`, ALIGN's grid); at the library's own 0.7 um none does.
  The kit's copy trims the pads to the M2 space (0.28 um) from a wire on the tracks beside their
  own (20 nm off the A and Y pads), and its LEF names a pin by its pad (openroad/views.py).
- The library stops its device implants 0.14 to 0.29 um short of the cell edges, its taps'
  implants reach past its bands near them, and its fillers have none; the kit's copy completes
  every cell's implants to the library's own band edges across its width (Pplus to 0.68 and
  3.2..5.54 um, Nplus 0.68..3.2 and from 5.54 um, the rail bands past the cell as the row cells',
  the well to `NW_TOP`; the Pplus islands at its PMOS gate ends run over the poly ends, NP.12), so
  cells, fillers, mirrored neighbours, the wrappers' pads (`ISO_PAD`) and row cells all meet
  implant edge to edge.
- Cell widths are on a 0.1 um grid; fillers (0.3 um and up) pad them to the 0.6 um placement grid
  (`STD_PAD`); cells off the 0.3 um grid (buf_1, or2_1) cannot be padded.
- The poly resistor is ppolyf_u (350 ohm/sq, 0.8 um wide, `RES`): SAB, RES_MK and Pplus as the
  PDK's own resistor cells, its Pplus joined to the VSS band, its body 0.6 um clear of the N-well;
  its cell keeps its Pplus 0.4 um from a neighbour's (`RULES["PO"]`).
- MOM capacitors stack Metal3 to Metal5 (`MOM_LAYERS`): an array unit's channels need Metal2 below
  its plates, so a three-layer unit takes the 11 kA top metal (0.44 / 0.46 um, the fingers').
- MOS fingers are `nf` in the models; `w` is the total width.
