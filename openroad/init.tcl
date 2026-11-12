# GF180MCU (gf180mcuD, 3.3 V) for plain OpenROAD: the technology and the gf180mcu_osu_sc_gp9t3v3 standard cells.
# A design script sources this first, then reads its own views, netlist and constraints.

set PLATFORM_DIR [file dirname [file normalize [info script]]]

read_lef $PLATFORM_DIR/gf180mcu_tech.lef
read_lef $PLATFORM_DIR/lef/gf180mcu_osu_sc_gp9t3v3.lef
read_liberty $PLATFORM_DIR/lib/gf180mcu_osu_sc_gp9t3v3_TT_25C.ccs.lib.gz  ;# typical, 25 C, 3.30 V: the library's only corner
