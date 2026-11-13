"""Every cell of gf180mcu_osu_sc_gp9t3v3 for hdl21 and the generic cells (flow.circuit.cells) it implements.

Written by flow.circuit.cellmap from the library's Liberty and SPICE; do not edit:
    uv run python -c "from flow.circuit.cellmap import write_library; write_library('gf180')"
"""

DOMAIN = "gf180"
LIBRARY = "gf180mcu_osu_sc_gp9t3v3"

# cell -> (pins in SPICE order, their directions)
CELLS = {
    'gf180mcu_osu_sc_gp9t3v3__addf_1': (('A', 'B', 'CI', 'SUM', 'CO', 'VDD', 'VSS'), ('input', 'input', 'input', 'output', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__addh_1': (('B', 'SUM', 'CO', 'VDD', 'VSS', 'A'), ('input', 'output', 'output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__and2_1': (('A', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__aoi21_1': (('A0', 'A1', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__aoi22_1': (('A0', 'A1', 'B0', 'B1', 'Y', 'VDD', 'VSS'), ('input', 'input', 'input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__buf_1': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__buf_16': (('Y', 'VDD', 'VSS', 'A'), ('output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__buf_2': (('Y', 'VDD', 'VSS', 'A'), ('output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__buf_4': (('Y', 'VDD', 'VSS', 'A'), ('output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__buf_8': (('Y', 'VDD', 'VSS', 'A'), ('output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__clkbuf_1': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__clkbuf_16': (('Y', 'VDD', 'VSS', 'A'), ('output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__clkbuf_2': (('Y', 'VDD', 'VSS', 'A'), ('output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__clkbuf_4': (('Y', 'VDD', 'VSS', 'A'), ('output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__clkbuf_8': (('Y', 'VDD', 'VSS', 'A'), ('output', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__clkinv_1': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__clkinv_16': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__clkinv_2': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__clkinv_4': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__clkinv_8': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__decap_1': (('VDD', 'VSS'), ('inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__dff_1': (('D', 'CLK', 'Q', 'QN', 'VDD', 'VSS'), ('input', 'input', 'output', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__dffn_1': (('D', 'CLK', 'Q', 'QN', 'VDD', 'VSS'), ('input', 'input', 'output', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__dffsr_1': (('D', 'CLK', 'Q', 'QN', 'R', 'VDD', 'VSS', 'S'), ('input', 'input', 'output', 'output', 'input', 'inout', 'inout', 'input')),
    'gf180mcu_osu_sc_gp9t3v3__dlat_1': (('D', 'CLK', 'Q', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__dlatn_1': (('D', 'CLK', 'Q', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__inv_1': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__inv_16': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__inv_2': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__inv_4': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__inv_8': (('A', 'Y', 'VDD', 'VSS'), ('input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__mux2_1': (('A', 'B', 'Sel', 'Y', 'VDD', 'VSS'), ('input', 'input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__nand2_1': (('A', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__nor2_1': (('A', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__oai21_1': (('A0', 'A1', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__oai22_1': (('A0', 'A1', 'B0', 'B1', 'Y', 'VDD', 'VSS'), ('input', 'input', 'input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__oai31_1': (('A0', 'A1', 'A2', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__or2_1': (('A', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__tbuf_1': (('A', 'EN', 'Y', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__tieh': (('Y', 'VDD', 'VSS'), ('output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__tiel': (('Y', 'VDD', 'VSS'), ('output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__tinv_1': (('A', 'EN', 'Y', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__xnor2_1': (('A', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
    'gf180mcu_osu_sc_gp9t3v3__xor2_1': (('A', 'B', 'Y', 'VDD', 'VSS'), ('input', 'input', 'output', 'inout', 'inout')),
}
# generic cell -> (library cell, {cell pin: generic pin}, cell pins held high, cell pins held low)
GENERIC = {
    'inv_x1': ('gf180mcu_osu_sc_gp9t3v3__inv_1', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'inv_x2': ('gf180mcu_osu_sc_gp9t3v3__inv_2', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'inv_x4': ('gf180mcu_osu_sc_gp9t3v3__inv_4', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'inv_x8': ('gf180mcu_osu_sc_gp9t3v3__inv_8', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'inv_x16': ('gf180mcu_osu_sc_gp9t3v3__inv_16', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'buf_x2': ('gf180mcu_osu_sc_gp9t3v3__buf_2', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'buf_x4': ('gf180mcu_osu_sc_gp9t3v3__buf_4', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'buf_x8': ('gf180mcu_osu_sc_gp9t3v3__buf_8', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'buf_x16': ('gf180mcu_osu_sc_gp9t3v3__buf_16', {'A': 'A', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'nand2_x1': ('gf180mcu_osu_sc_gp9t3v3__nand2_1', {'A': 'A', 'B': 'B', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'nor2_x1': ('gf180mcu_osu_sc_gp9t3v3__nor2_1', {'A': 'A', 'B': 'B', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'and2_x1': ('gf180mcu_osu_sc_gp9t3v3__and2_1', {'A': 'A', 'B': 'B', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'or2_x1': ('gf180mcu_osu_sc_gp9t3v3__or2_1', {'A': 'A', 'B': 'B', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'xor2_x1': ('gf180mcu_osu_sc_gp9t3v3__xor2_1', {'A': 'A', 'B': 'B', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'xnor2_x1': ('gf180mcu_osu_sc_gp9t3v3__xnor2_1', {'A': 'A', 'B': 'B', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'mux2_x1': ('gf180mcu_osu_sc_gp9t3v3__mux2_1', {'A': 'A', 'B': 'B', 'Sel': 'S', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'oai21_x1': ('gf180mcu_osu_sc_gp9t3v3__oai21_1', {'A0': 'A', 'A1': 'B', 'B': 'C', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'aoi22_x1': ('gf180mcu_osu_sc_gp9t3v3__aoi22_1', {'A0': 'A', 'A1': 'B', 'B0': 'C', 'B1': 'D', 'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'dff_x1': ('gf180mcu_osu_sc_gp9t3v3__dff_1', {'D': 'D', 'CLK': 'CLK', 'Q': 'Q', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'dffr_x1': ('gf180mcu_osu_sc_gp9t3v3__dffsr_1', {'D': 'D', 'CLK': 'CLK', 'Q': 'Q', 'R': 'RN', 'VDD': 'VDD', 'VSS': 'VSS'}, ('S',), ()),
    'latch_x1': ('gf180mcu_osu_sc_gp9t3v3__dlat_1', {'D': 'D', 'CLK': 'EN', 'Q': 'Q', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'tiehi_x1': ('gf180mcu_osu_sc_gp9t3v3__tieh', {'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
    'tielo_x1': ('gf180mcu_osu_sc_gp9t3v3__tiel', {'Y': 'Y', 'VDD': 'VDD', 'VSS': 'VSS'}, (), ()),
}
# generic cells the library cannot implement (they stay generic)
MISSING = ('nand2_x2', 'nand3_x1', 'nand4_x1', 'nor2_x2', 'nor3_x1', 'nor3_x2', 'nor4_x2', 'and2_x2', 'and3_x1', 'and3_x2', 'or2_x2', 'or3_x1', 'or3_x2', 'mux2_x2', 'aoi21_x2', 'ao21_x1', 'dff_x2', 'dffr_x2')
