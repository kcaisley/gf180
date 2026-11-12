"""GF180MCU (gf180mcuD, 5 V core) values for the row cells (flow/layout/rows), all in nm.

The generic cells import this module as ``tech``, so this directory goes on the path ahead of
theirs. Rule values are the open PDK's (its KLayout DRC deck, libs.tech/klayout/tech/drc, the
gf180mcu DRM's rule names in the comments; the _MV values, the 5 V devices'); row positions follow
the gf180mcu_fd_sc_mcu7t5v0 library (3.92 um, 7 tracks of 0.56 um, 0.56 um sites, VSS on even
rail lines). The library's rails carry no diffusion: the N+ and P+ implants continue over them
(N+ at VSS, P+ at VDD) and the wells are tied by its filltie cell, which every row end gets
(EDGE_TIE). Its devices are the 5 V pair under Dualgate and V5_XTOR (nfet_05v0, pfet_05v0), which
the row cells draw too: both markers over every cell (VT_MARKS), no VT layer.
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
    "DUALGATE": (55, 0),  # thick (5/6 V) gate oxide
    "V5_XTOR": (112, 1),  # marks a Dualgate device as 5 V (nfet_05v0, pfet_05v0)
    "LVPWELL": (204, 0),  # the library cells' P-well under their NMOS half (not drawn by the rows)
    "DNW": (12, 0),  # DNWELL
    "SAB": (49, 0),  # salicide block
    "RES_MK": (110, 5),  # resistor marker
    "BND": (0, 0),  # PR_bndry, as the standard cells
    "V3": (40, 0),
    "M4": (46, 0),
    "V4": (41, 0),
    "M5": (81, 0),  # Metal5: gf180mcuD's top metal (11 kA)
    "TEXT": (63, 63),
    # Metal<n>_Label: pin labels (the LVS deck reads the metals' labels there)
    **{f"M{n}.PIN": (m, 10) for n, m in enumerate((34, 36, 42, 46, 81), 1)},
}
PIN_TEXT = {m: LAYERS[f"{m}.PIN"] for m in ("M1", "M2", "M3")}  # pin labels of the row cells
MODELS = {"n": "nfet_05v0", "p": "pfet_05v0"}  # LVS (and simulation) device names of the row transistors
MODEL_PREFIXES = {"n": ("nfet",), "p": ("pfet",)}  # MOS model families, for the schematic tools
DNW_MODELS = {"nfet_05v0": "nfet_05v0_dn"}  # NMOS over a deep N-well, as the LVS deck extracts it
STD_LIB = "gf180mcu_fd_sc_mcu7t5v0"  # the standard-cell library
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
    # the top metal: MT.1 0.44, MT.2a 0.46 (MT.4 the area), its space taken at 0.68 so a MOM unit
    # with fingers on it (MOM_LAYERS) abuts on the rows' 0.56 um grid (pitch 1.12), as ALIGN places it
    "M5": {"width": 440, "space": 680, "pitch": 1120, "area": 562_500},
    # the poly resistor's cell keeps half this space between its poly and the cell edge (rescell):
    # its Pplus, 0.3 past the poly (PRES.5), then stays 0.4 from a neighbour's (PP.2), its poly 0.6
    # from a neighbour's COMP and poly (PRES.3, PRES.4); PL.3a is 0.24
    "PO": {"width": 200, "space": 1400},
}
NW_SPACE = 740  # NW.2a_MV: N-well space, narrower gaps are closed

# ---- the standard-cell row
H = 3920  # row height; rails at 0 (VSS) and H (VDD)
PITCH = 560  # M2 track pitch (y), tracks on multiples of it
XPITCH = 560  # M3 track pitch and cell width grid (x): the library's site width
RAIL = 300  # M1 rail half width (600 nm, as the std cells)
TAP_OD = 110  # (no rail diffusion: RAIL_OD)
TAP_PITCH = 560
RAIL_OD = False  # no diffusion under the rails, as the library
RAIL_TAPS = False  # and no taps: filltie cells tie the wells
LVS_BUTTED_TAPS = False  # so no source reaches a tap through the silicide (flow.layout.klayout_lvs)
RAIL_IMPLANTS = ("NP", "PP")  # the implants continue over the rails as the library's: N+ at VSS, P+ at VDD
PP_TAP = 200  # VSS rail implant band half height (the library's Nplus reaches 0.2 past the rail)
NP_TAP = 3720  # VDD rail implant band bottom (top 2 H - NP_TAP)
# device implants from one rail band to the other: N+ over an NMOS cell, P+ over a PMOS cell; they
# enclose the gates by 0.23 (NP.5a, PP.5a) and the diffusion by 0.16 (NP.5b, PP.5b)
DEV_IMP = {"n": (PP_TAP, NP_TAP), "p": (PP_TAP, NP_TAP)}
# well: VDD band bottom (NMOS cells: 0.6 above their N+ COMP, DF.16_MV; 0.86 tall alone, NW.1a),
# PMOS body bottom (0.6 below its P+ COMP, DF.4c_MV), top (the library's, 0.43 past the VDD rail)
NW_N, NW_P, NW_TOP = 3200, 1000, 4350
VT_BAND = (-280, 4200)  # Dualgate and V5_XTOR over the cell, Dualgate 0.28 past the rails as the library's
VT_MARKS = {"n": ("DUALGATE", "V5_XTOR"), "p": ("DUALGATE", "V5_XTOR")}  # the 5 V devices' markers
STD_NW = 1760  # library cells: Nplus (and LVPWELL) below, Pplus and well from here
IMP_OH, NW_OH = 200, 430  # overhang of the rail implant bands and the VDD well band past a cell, as the library
EDGE_TIE = ("gf180mcu_fd_sc_mcu7t5v0__filltie", 1120)  # tie cell at every row end, and its width
EDGE_W = 1680  # row end cell: the tie cell and one site of padding (its well and LVPWELL overhang 0.43)

# ---- the standard cells next to the rows (stdcell_access.py, netcells.py)
STD_CELLS = (
    "gf180mcu_fd_sc_mcu7t5v0__inv_1",
    "gf180mcu_fd_sc_mcu7t5v0__inv_4",
    "gf180mcu_fd_sc_mcu7t5v0__inv_8",
    "gf180mcu_fd_sc_mcu7t5v0__nor2_2",
    "gf180mcu_fd_sc_mcu7t5v0__nand2_1",
    "gf180mcu_fd_sc_mcu7t5v0__fill_1",
    "gf180mcu_fd_sc_mcu7t5v0__filltie",
)
STD_SUPPLY = ("VDD", "VSS")  # supply pin names, VDD rail on top (the wells VNW, VPW on them: openroad/views.py)
STD_FILL, STD_FILL_W = "gf180mcu_fd_sc_mcu7t5v0__fill_1", 560  # one-site filler
STD_TEXT_LAYERS: set[int] = set()  # labels sit on the metal layers' label datatype: netcells drops all text
# pin access tracks, preferred first (middle of the cell): the library's horizontal pins sit on its
# own tracks, half a pitch off the rows' M2 tracks (PIN_PITCH), so both are tried; bars there keep
# M2.2a to the next track's
STD_TRACKS = (1960, 1680, 2240, 1400, 2520, 1120, 2800, 840, 3080, 560, 3360)
PIN_PITCH = 280
STD_WIDE = None  # one via on any plate
ISO_PAD = 430  # isolated std cells: pad on both sides, the library cell's well and LVPWELL overhang
EDGE_CUTS, EDGE_PAD = 1, (260, 140)  # row-end supply stack: one via per rail, M2 pad 520 x 280 (M2.3)

# ---- device placement in the row
GATE_TRACK = {"n": 2800, "p": 1120}  # gate bar and its M2 track
# S/D tracks: a strip's M1 keeps M1.2a to the rail and to the gate pads
SD_TRACKS = {"n": (1120, 1680, 2240), "p": (2800, 2240, 1680)}
# NMOS: its first contact's M1 0.23 from the rail (M1.2a); the poly bar 0.3 from the diffusion
# (PL.5a_MV) below the gate track; PMOS mirrored. Mirrored rows keep their poly 0.24 apart (PL.3a)
OD_LIMIT = {"n": (520, 2320), "p": (1600, 3400)}  # (OD start at the rail side, furthest OD edge)
# the complementary row cells' diffusion bands (rowcell.inverter), the library inverters' facing
# edges: the NMOS's (lowest bottom, top), the PMOS's (bottom, highest top)
LOGIC_OD = {"n": (520, 1160), "p": (2360, 3400)}  # their outer edges as the analog cells' (M1.2a to the rails)
W_MAX = 1800  # widest finger
EDGE = 600  # OD to the cell edge: DF.4c_MV / DF.16_MV against any neighbour's well
OD_GAP = 360  # diffusion break between a pair's devices that share no strip (DF.3a_MV)
GATE_GAP = 660  # gate to gate across a shared strip when the gates differ (their M2 bars, Mn.2a)

# ---- rule-derived dimensions
CO = 220  # CO.1 (exact size)
CO_PITCH = 470  # contacts along a strip (CO.2a 0.25)
CO_GATE = 150  # contact to gate (CO.7): the contacted pitch is L + CO + 2 CO_GATE
CO_OD_END, CO_OD_SIDE = 70, 70  # COMP enclosure of the contacts (CO.4)
OD_EXT = 180  # OD past the outermost strip centre (CO / 2 + CO.4): 0.44 past the gate (DF.6_MV 0.4)
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
M2_MIN_LEN = 940  # M2.3 (520 nm), and spans an M3 track: XPITCH + 2 BAR_END
BAR_END = 190  # a bar past its outermost via centre (V / 2 + 0.06 line-end enclosure, V1.4b)
GATE_PAD = 130  # M1 pad half height around a gate contact: the via flush, 0.06 beside it (V1.3d)
PO_ENDCAP = 220  # poly past COMP (PL.4)
PO_HEAD = 180  # poly head half height around a gate contact (CO / 2 + CO.3 0.07)
PO_BAR_END = 180  # poly bar past its outer gates (CO / 2 + CO.3)
SHORT_L = 700  # shorter gates leave room for the gate pads beside the S/D contacts (M1.2a)
M1_EDGE, M2_EDGE, M3_EDGE = 115, 140, 280  # bars kept from the cell edge

# the metals a fringe MOM capacitor stacks (flow/momcap), from the top: Metal3 to Metal5; an
# N-layer unit uses the top N, its shield the metal below them. The array units' channels run on the
# metal below their plates, which must be the horizontal Metal2 on its tracks (primitives/mom.py), so
# a three-layer unit takes the thick top metal (Metal5, its space at 0.68 um in RULES), whose width and
# space the fingers then share
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
    "co_enc": 70,
    "min_area": {"SAB": 2_010_000},
    "cdl": "R{name} {plus} {minus} {bulk} ppolyf_u l={l}u w={w}u",
    "bulk": True,  # the model's third terminal, the substrate
    "sim_model": "ppolyf_u_lw",  # the package's wrapper taking the body's l and w (hdl21/spectre_devices.scs, hdl21/ngspice_devices.spice)
}
