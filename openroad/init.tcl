# GF180MCU (gf180mcuD) for plain OpenROAD: the technology and the gf180mcu_fd_sc_mcu7t5v0 standard cells.
# A design script sources this first, then reads its own views, netlist and constraints.

set PLATFORM_DIR [file dirname [file normalize [info script]]]

read_lef $PLATFORM_DIR/gf180mcu_tech.lef
read_lef $PLATFORM_DIR/lef/gf180mcu_fd_sc_mcu7t5v0.lef
read_liberty $PLATFORM_DIR/lib/gf180mcu_fd_sc_mcu7t5v0__tt_025C_5v00.lib.gz  ;# typical; ss_125C_4v50 is slow
