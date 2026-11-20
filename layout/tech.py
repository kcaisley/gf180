"""GF180MCU (gf180mcuD, 3.3 V core) values for the row cells (flow/layout/rows), all in nm.

The generic cells import this module as ``tech``, so this directory goes on the path ahead of
theirs. Rule values are the open PDK's (its KLayout DRC deck, libs.tech/klayout/tech/drc, the
gf180mcu DRM's rule names in the comments; the _LV values, the 3.3 V devices'); row positions
follow the gf180mcu_osu_sc_gp9t3v3 library (Oklahoma State's: 6.3 um, nine 0.7 um tracks in its
LEF, its pins on a 0.6 um grid; ten 0.63 um M2 tracks here, cell widths on a 0.1 um grid padded to
0.6 um, VSS on even rail lines). The library's rails lie
inside its cells (M1 0 to 0.6 um from either edge), so where two rows meet the rail is 1.2 um wide,
centred on the line, as the row cells draw it (RAIL); a tap sits under each, P+ under VSS, N+ under
VDD, in every cell (RAIL_OD, RAIL_TAPS). No VT layer, no Dualgate: the 3.3 V devices.
"""

# ---- layers (GDS layer, datatype)
LAYERS = {
    "OD": (22, 0),  # COMP
    "PO": (30, 0),  # Poly2
    "CO": (33, 0),  # Contact
    "M1": (34, 0),
    "V1": (35, 0),
    "M2": (36, 0),
    "V2": (38, 0),
    "M3": (42, 0),
    "NW": (21, 0),  # Nwell
    "PP": (31, 0),  # Pplus
    "NP": (32, 0),  # Nplus
    "VTN": None,
    "VTP": None,
    "DUALGATE": (55, 0),  # thick (5/6 V) gate oxide: the I/O devices', not drawn by the rows
    "V5_XTOR": (112, 1),  # marks a Dualgate device as 5 V (nfet_05v0, pfet_05v0)
    "DNW": (12, 0),  # DNWELL
    "SAB": (49, 0),  # salicide block
    "RES_MK": (110, 5),  # resistor marker
    "BND": (0, 0),  # PR_bndry (the kit's copy of the library adds it to its cells: openroad/views.py)
    "V3": (40, 0),
    "M4": (46, 0),
    "V4": (41, 0),
    "M5": (81, 0),  # Metal5: gf180mcuD's top metal (11 kA)
    "TEXT": (63, 63),
    # Metal<n>_Label: pin labels (the LVS deck reads the metals' labels there)
    **{f"M{n}.PIN": (m, 10) for n, m in enumerate((34, 36, 42, 46, 81), 1)},
}
PIN_TEXT = {m: LAYERS[f"{m}.PIN"] for m in ("M1", "M2", "M3")}  # pin labels of the row cells
# the netlists' names (pdk.gf180.hdl21: the decks' nfet_03v3 / pfet_03v3 wrapped, which Spectre cannot
# call by name); the LVS source names them as the deck does (netlist/lvs.py)
MODELS = {"n": "nfet_3v3", "p": "pfet_3v3"}
MODEL_PREFIXES = {"n": ("nfet",), "p": ("pfet",)}  # MOS model families, for the schematic tools
DNW_MODELS = {"nfet_03v3": "nfet_03v3_dn"}  # NMOS over a deep N-well, as the LVS deck extracts it
STD_LIB = "gf180mcu_osu_sc_gp9t3v3"  # the standard-cell library
STD_DRIVE = r"_(\d+)$"  # a cell name's drive strength (flow.circuit.cellmap)
MFG_GRID = 5  # manufacturing grid
DBU = 0.001  # um per database unit (1 nm)

# contacts and vias have one size (CO.1, Vn.1 exact width): the off-grid router's bar cuts are made square
SQUARE_CUTS = True

# ---- metal and via rules, the whole stack (generators beyond the rows: the caparray), from the
# tech LEF (openroad/) and the DRC deck: metal width, space, pitch, area (nm2); via cut (square) and
# space between cuts. Rules the LEF holds only in tables (wide-metal spacing) are left out.
RULES = {
    "M1": {"width": 230, "space": 230, "pitch": 560, "area": 144_400},  # M1.1, M1.2a, M1.3
    # enclosure: (on two opposite sides, on the other two, on all four): 0.06 at a line end
    # (Vn.3c, Vn.4b), 0.01 elsewhere (Vn.4a; V1.3a allows M1 flush)
    **{f"V{n}": {"cut": 260, "space": 260, "enclosure": (60, 10, 10)} for n in range(1, 5)},
    # enclosed_area: the deck gives none; a conservative 1 um2 (it sizes the CDAC shield's holes)
    **{
        f"M{n}": {"width": 280, "space": 280, "pitch": 560, "area": 144_400, "enclosed_area": 1_000_000}
        for n in range(2, 5)
    },  # Mn.1, Mn.2a, Mn.3
    # the top metal (MT.1, MT.2a, MT.4): a MOM unit with fingers on it (MOM_LAYERS) is 2 x 0.9 um
    # wide, on the rows' 0.6 um grid (XPITCH), as ALIGN places it
    "M5": {"width": 440, "space": 460, "pitch": 900, "area": 562_500},
    # the poly resistor's cell keeps half this space between its poly and the cell edge (rescell):
    # its Pplus, 0.3 past the poly (PRES.5), then stays 0.4 from a neighbour's (PP.2), its poly 0.6
    # from a neighbour's COMP and poly (PRES.3, PRES.4); PL.3a is 0.24
    "PO": {"width": 200, "space": 1400},
}

# the metals a block's pins land on, lowest first (frida's flow.layout.pins: each landing on the
# lowest of them its route keeps clear of the block's other nets): the metals above the rows'
# routing (M1 to M3), the top one last, whose pitch takes the converter's double-width routes
PIN_METALS = (4, 5)

NW_SPACE = 600  # NW.2a_LV: N-well space, narrower gaps are closed

# ---- the standard-cell row
H = 6300  # row height; rails at 0 (VSS) and H (VDD)
# M2 track pitch (y), tracks on multiples of it: ten to a row, so the library's pin pads (on its
# 0.6 um grid, 2.55, 3.15, 3.75 um) each hold a track (2.52, 3.15, 3.78 um); at 0.7 um none does
PITCH = 630
XPITCH = 600  # M3 track pitch and cell width grid (x): two of the library's 0.3 um fillers
RAIL = 600  # M1 rail half width: the library's 0.6 um rail inside each of the two rows that meet
# rail taps as the library's, inside each cell under its own half of the rail: the diffusion 0.15 to
# 0.6 um from the rail line, the contacts 0.265 to 0.485 (a row cell's across a rail from a library
# cell keeps CO.2a to its contacts, and its diffusion DF.3a_LV)
TAP_Y = 375  # the taps' centre inside the cell from the rail line
TAP_OD = 225  # rail tap diffusion half height (the library's tap is 0.45 um tall)
TAP_PITCH = 600  # tap contacts at x = TAP_PITCH / 2 + k * TAP_PITCH
# the rail implant bands as the library's (its cells' full-width bands, which the kit's copy
# completes, openroad/views.py): Pplus to 0.68 um about VSS, Nplus from 0.68 below VDD, 0.08 past
# the taps (NP.3cii, PP.3ci: the other implant 0.08 from a tap)
PP_TAP = 680  # VSS rail implant band half height (Pplus)
NP_TAP = 5620  # VDD rail implant band bottom (Nplus; top 2 H - NP_TAP)
# device implants from one rail band to the other: Nplus over an NMOS cell, Pplus over a PMOS cell;
# they enclose the gates by 0.23 (NP.5a, PP.5a) and the diffusion by 0.16 (NP.5b, PP.5b)
DEV_IMP = {"n": (PP_TAP, NP_TAP), "p": (PP_TAP, NP_TAP)}
# well: VDD band bottom (NMOS cells: 0.43 above their N+ COMP, DF.16_LV), PMOS body bottom (0.43
# below its P+ COMP, DF.4c_LV), top (0.12 past the VDD tap, DF.4d_LV, into the next row)
NW_N, NW_P, NW_TOP = 3930, 2370, 6730
VT_BAND = (0, H)  # no VT layer drawn
STD_NW = 3200  # library cells: Nplus below (but for the VDD tap), Pplus and well from here
IMP_OH, NW_OH = 200, 430  # overhang of the rail implant bands and the VDD well band past a cell (PP.5b, DF.4d_LV)

# ---- the standard cells next to the rows (stdcell_access.py, netcells.py)
STD_CELLS = (
    "gf180mcu_osu_sc_gp9t3v3__inv_1",
    "gf180mcu_osu_sc_gp9t3v3__inv_4",
    "gf180mcu_osu_sc_gp9t3v3__inv_8",
    "gf180mcu_osu_sc_gp9t3v3__nor2_1",
    "gf180mcu_osu_sc_gp9t3v3__nand2_1",
    "gf180mcu_osu_sc_gp9t3v3__fill_1",
)
STD_SUPPLY = ("VDD", "VSS")  # supply pin names, VDD rail on top
STD_FILL, STD_FILL_W = "gf180mcu_osu_sc_gp9t3v3__fill_1", 300  # the narrowest filler
STD_FILLS = tuple((f"gf180mcu_osu_sc_gp9t3v3__fill_{n}", 300 * n) for n in (1, 2, 4, 8, 16))
# the library's decoupling capacitors, widest first: the cells a top level's filler pass
# places in a row's gaps before its fillers (OpenROAD's LEF cannot tell a decap from a filler)
STD_DECAPS = ('gf180mcu_osu_sc_gp9t3v3__decap_1',)
STD_PAD = 600  # cells padded to a multiple of the placement grid (their widths are 0.1 um multiples)
STD_TEXT_LAYERS: set[int] = set()  # the library's labels (on COMP and Metal2_Label): netcells drops all text
# pin access tracks, preferred first (middle of the cell): the library's pins are M2 pads, each a
# direct access on its track; the kit's copy trims the pads to the M2 space from the tracks beside
# them (openroad/views.py), so a router's wire on any track keeps clear of them
STD_TRACKS = (3150, 2520, 3780, 1890, 4410, 1260, 5040)
STD_WIDE = None  # one via on any plate
M2_PLATE = 1000  # library M2 this wide both ways is a plate: the cells' pin pads (0.5 x 0.4 um) are none
ISO_PAD = 430  # isolated std cells: pad on both sides (a row cell's well 0.43 from their N+ COMP, DF.16_LV)
EDGE_CUTS, EDGE_PAD = 1, (260, 140)  # row-end supply stack: one via per rail, M2 pad 520 x 280 (M2.3)

# ---- device placement in the row
GATE_TRACK = {"n": 3780, "p": 2520}  # gate bar and its M2 track (symmetric about the row's middle)
# S/D tracks: a strip's M1 keeps M1.2a to the rail and to the gate pads
SD_TRACKS = {"n": (1260, 1890, 2520, 3150), "p": (3150, 3780, 4410, 5040)}
# NMOS: its poly end 0.1 from the VSS tap (PL.5a_LV: 0.32 from the tap's diffusion, DF.3a_LV;
# 0.24 inside its Nplus, NP.5a), its first contact's M1 0.23 from the rail (M1.2a); the poly bar 0.1
# from the diffusion (PL.5a_LV), the gate contact 0.17 (CO.8), below the gate track; PMOS: 0.31
# inside its Pplus below the VDD band (PP.5a), mirrored about the gate track
OD_LIMIT = {"n": (920, 3500), "p": (2800, 5310)}  # (OD start at the rail side, furthest OD edge)
# the complementary row cells' diffusion bands (rowcell.inverter), split at the library's well
# (STD_NW, 0.43 each way): the NMOS's (lowest bottom, top), the PMOS's (bottom, highest top)
LOGIC_OD = {"n": (920, 2770), "p": (3630, 5310)}
W_MAX = 2230  # widest finger: ten 0.22 um units (MOS_FINGER_UNITS); the bands hold 2.58 / 2.51 um
EDGE = 430  # OD to the cell edge: DF.4c_LV / DF.16_LV against any neighbour's well
OD_GAP = 280  # diffusion break between a pair's devices that share no strip (DF.3a_LV)
GATE_GAP = 660  # gate to gate across a shared strip when the gates differ (their M2 bars, Mn.2a)

# ---- rule-derived dimensions
CO = 220  # CO.1 (exact size)
CO_PITCH = 470  # contacts along a strip (CO.2a 0.25)
CO_GATE = 150  # contact to gate (CO.7): the contacted pitch is L + CO + 2 CO_GATE
CO_OD_END, CO_OD_SIDE = 70, 70  # COMP enclosure of the contacts (CO.4)
OD_EXT = 180  # OD past the outermost strip centre (CO / 2 + CO.4): 0.44 past the gate (DF.6_LV 0.24)
V1, V2 = RULES["V1"]["cut"], RULES["V2"]["cut"]  # V1.1 / V2.1
# M1 strips and pads: via + 2 x 0.06 (V1.3d: their ends may then be flush); M2 / M3 bars: via + 2 x 0.01
M1W, M2W, M3W = 380, 280, 280
VIA_M1_W = 300  # a via inside a long M1 pin: 0.02 on its sides, 0.06 along it (V1.3d)
M1_CO_END = 60  # M1 past a contact along a strip (CO.6a, line end)
M1_SPACE = RULES["M1"]["space"]  # M1.2a
M1_MIN_W = 230  # M1.1
V1_PAIR = 520  # two vias side by side, centre to centre (V1.2a 0.26)
M1_MIN_LEN = 385  # an M1W-wide M1 piece meets M1.3 (0.1444 um2)
M1_BAR_MIN = 560  # shortest gate M1 bar, and the area that forces it
M1_AREA = RULES["M1"]["area"]
M2_SPACE = RULES["M2"]["space"]  # M2.2a
M2_LINE_END = M2_SPACE  # M2 line end to line end: no end-of-line rule, ALIGN's M2 EndToEnd
M2_MIN_LEN = 980  # M2.3 (520 nm), and spans an M3 track: XPITCH + 2 BAR_END
BAR_END = 190  # a bar past its outermost via centre (V / 2 + 0.06 line-end enclosure, V1.4b)
GATE_PAD = 130  # M1 pad half height around a gate contact: the via flush, 0.06 beside it (V1.3d)
PO_ENDCAP = 220  # poly past COMP (PL.4_LV)
PO_HEAD = 180  # poly head half height around a gate contact (CO / 2 + CO.3 0.07)
PO_BAR_END = 180  # poly bar past its outer gates (CO / 2 + CO.3)
SHORT_L = 700  # shorter gates leave room for the gate pads beside the S/D contacts (M1.2a)
M1_EDGE, M2_EDGE, M3_EDGE = 115, 140, 300  # bars kept from the cell edge

# the metals a fringe MOM capacitor stacks (flow/momcap), from the top: Metal3 to Metal5; an
# N-layer unit uses the top N, its shield the metal below them. The array units' channels run on the
# metal below their plates, which must be the horizontal Metal2 on its tracks (primitives/mom.py), so
# a three-layer unit takes the thick top metal (Metal5, 0.44 / 0.46 um), whose width and space the
# fingers then share
MOM_LAYERS = (3, 4, 5)

# the unsalicided P+ poly resistor ppolyf_u (flow/layout/rows/rescell.py, 350 ohm/sq): its LVS
# device (Poly2 under Pplus, SAB and RES_MK, the deck's ppolyf_u) and model; PRES.1 (width); SAB
# over the body and 0.28 past the poly across it (PRES.6), at least 2 um2 (SB.13), RES_MK the body
# alone, as the PDK's own resistor cells; Pplus 0.3 past all the poly (PRES.5); the contacts 0.22
# from SAB (PRES.7), CO.3; the substrate under it is its third terminal. The LVS source line
# compares W and L (the deck's BResistor; R is not compared)
RES = {
    "model": "ppolyf_u",
    "width": 800,
    "markers": {"SAB": (0, 280), "RES_MK": (0, 0)},
    "implant": ("PP", 300),
    "co_space": 220,
    "well_space": 600,  # the body clear of the NMOS cells' N-well band (the sub variant of the device)
    "co_enc": 70,
    "min_area": {"SAB": 2_010_000},
    "cdl": "R{name} {plus} {minus} {bulk} ppolyf_u l={l}u w={w}u",
    "bulk": True,  # the model's third terminal, the substrate
    "sim_model": "ppolyf_u_lw",  # the package's wrapper taking the body's l and w (hdl21/spectre_devices.scs, hdl21/ngspice_devices.spice)
}

# capdac's drivers (flow.capdac.subckt._drive_r_ohm): the kit's settling time constants over the
# model's (its tables' on- and switching resistances, its FO4 delay), from capdac frida1 at the
# typical corner (2026-11-19, run 20261119_003037): at 1 it settled in 547 ps pre-layout and 625 ps
# post-layout (KLayout-PEX 2.5-D; its MSB 625 ps), so the post-layout over the 500 ps target
DRIVER_TAU_SCALE = 1.43
# (2026-11-19, run 20261119_012549: at 1.25 its MSB settled post-layout in 573 ps, so 1.25 times that over 500 ps)

# capdac's drivers: each plate's wiring from its driver to its landing (F), the load the
# momcap table leaves out; from capdac frida1's extraction (run 20261119_012549), the
# difference plates' extracted capacitance against the model's, the intercept of a line fit
DRIVER_ROUTE_F = 2.6e-15
