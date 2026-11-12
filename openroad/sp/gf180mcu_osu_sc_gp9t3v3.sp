* gf180mcu_osu_sc_gp9t3v3 (CDL, M lines on the PDK's device names) for FRIDA (pdk/gf180/openroad/views.py)
.SUBCKT gf180mcu_osu_sc_gp9t3v3__addf_1 A B CI SUM CO VDD VSS
M0 a_76_73# B a_59_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 a_9_73# B VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 a_110_73# A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 SUM a_161_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M4 a_195_19# B a_178_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 SUM a_161_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M6 a_178_19# A a_161_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M7 a_195_73# B a_178_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M8 a_110_19# CI VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M9 a_59_19# CI a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M10 VSS B a_110_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M11 a_178_73# A a_161_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M12 a_110_73# CI VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M13 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M14 a_59_19# CI a_9_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M15 VDD B a_110_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M16 CO a_59_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M17 VDD A a_9_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M18 VSS CI a_195_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M19 CO a_59_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
M20 VDD CI a_195_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M21 VSS A a_76_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M22 a_161_19# a_59_19# a_110_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M23 a_76_19# B a_59_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M24 a_110_19# A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M25 VDD A a_76_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M26 a_161_19# a_59_19# a_110_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M27 a_9_19# B VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__addh_1 B SUM CO VDD VSS A
M0 a_91_73# A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M1 a_75_19# B a_91_19# VSS nfet_03v3 ad=0.34p pd=1.65u as=0.233p ps=1.4u w=0.85u l=0.3u
M2 a_19_14# A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 a_91_19# B a_91_73# VDD pfet_03v3 ad=0.68p pd=2.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 VSS a_19_14# a_75_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.34p ps=1.65u w=0.85u l=0.3u
M5 a_19_14# B a_42_19# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 VDD a_19_14# a_91_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.68p ps=2.5u w=1.7u l=0.3u
M7 VSS a_19_14# CO VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M8 VDD B a_19_14# VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 VDD a_19_14# CO VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M10 SUM a_91_19# VSS VSS nfet_03v3 ad=0.638p pd=3.2u as=0.233p ps=1.4u w=0.85u l=0.3u
M11 a_91_19# A a_75_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M12 SUM a_91_19# VDD VDD pfet_03v3 ad=1.28p pd=4.9u as=0.468p ps=2.25u w=1.7u l=0.3u
M13 a_42_19# A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__and2_1 A B Y VDD VSS
M0 VSS B a_28_19# VSS nfet_03v3 ad=0.383p pd=1.75u as=0.105p ps=1.1u w=0.85u l=0.3u
M1 VDD B a_12_19# VDD pfet_03v3 ad=0.638p pd=2.45u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 Y a_12_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.383p ps=1.75u w=0.85u l=0.3u
M3 Y a_12_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.638p ps=2.45u w=1.7u l=0.3u
M4 a_12_19# A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M5 a_28_19# A a_12_19# VSS nfet_03v3 ad=0.105p pd=1.1u as=0.425p ps=2.7u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__ant VDD VSS I
D0 VSS I diode_nd2ps_06v0 pj=2.1u area=0.27p
D1 I VDD diode_pd2nw_06v0 pj=2.1u area=0.27p
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__antfill VDD VSS A
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__aoi21_1 A0 A1 B Y VDD VSS
M0 Y A1 a_28_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.105p ps=1.1u w=0.85u l=0.3u
M1 a_9_73# A1 VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 VSS B Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M3 Y B a_9_73# VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 VDD A0 a_9_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M5 a_28_19# A0 VSS VSS nfet_03v3 ad=0.105p pd=1.1u as=0.425p ps=2.7u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__aoi22_1 A0 A1 B0 B1 Y VDD VSS
M0 a_9_73# B1 Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 Y A1 a_28_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.105p ps=1.1u w=0.85u l=0.3u
M2 a_9_73# A1 VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 a_56_19# B0 Y VSS nfet_03v3 ad=0.105p pd=1.1u as=0.233p ps=1.4u w=0.85u l=0.3u
M4 Y B0 a_9_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M5 VDD A0 a_9_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M6 VSS B1 a_56_19# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.105p ps=1.1u w=0.85u l=0.3u
M7 a_28_19# A0 VSS VSS nfet_03v3 ad=0.105p pd=1.1u as=0.425p ps=2.7u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__buf_1 A Y VDD VSS
M0 Y a_9_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.553p ps=2.35u w=1.7u l=0.3u
M1 VSS A a_9_19# VSS nfet_03v3 ad=0.275p pd=1.5u as=0.425p ps=2.7u w=0.85u l=0.3u
M2 VDD A a_9_19# VDD pfet_03v3 ad=0.553p pd=2.35u as=0.85p ps=4.4u w=1.7u l=0.3u
M3 Y a_9_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.275p ps=1.5u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__buf_16 Y VDD VSS A
M0 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M8 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M10 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M11 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M12 VSS a_9_19# Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M13 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M14 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M15 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M16 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M17 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M18 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M19 VDD a_9_19# Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M20 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M21 VDD A a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M22 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M23 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M24 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M25 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M26 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M27 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M28 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M29 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M30 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M31 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M32 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M33 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__buf_2 Y VDD VSS A
M0 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VSS a_9_19# Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M2 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M3 VDD a_9_19# Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 VDD A a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M5 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__buf_4 Y VDD VSS A
M0 Y a_10_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VDD A a_10_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M2 VSS a_10_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M3 VDD a_10_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 VSS a_10_19# Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 Y a_10_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 Y a_10_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M7 VDD a_10_19# Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M8 Y a_10_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 VSS A a_10_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__buf_8 Y VDD VSS A
M0 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M4 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M8 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M10 VDD A a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M11 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M12 VSS a_9_19# Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M13 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M14 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M15 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M16 VDD a_9_19# Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M17 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkbuf_1 A Y VDD VSS
M0 Y a_9_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.553p ps=2.35u w=1.7u l=0.3u
M1 VSS A a_9_19# VSS nfet_03v3 ad=0.275p pd=1.5u as=0.425p ps=2.7u w=0.85u l=0.3u
M2 VDD A a_9_19# VDD pfet_03v3 ad=0.553p pd=2.35u as=0.85p ps=4.4u w=1.7u l=0.3u
M3 Y a_9_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.275p ps=1.5u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkbuf_16 Y VDD VSS A
M0 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M8 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M10 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M11 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M12 VSS a_9_19# Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M13 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M14 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M15 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M16 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M17 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M18 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M19 VDD a_9_19# Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M20 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M21 VDD A a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M22 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M23 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M24 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M25 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M26 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M27 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M28 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M29 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M30 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M31 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M32 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M33 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkbuf_2 Y VDD VSS A
M0 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VSS a_9_19# Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M2 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M3 VDD a_9_19# Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 VDD A a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M5 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkbuf_4 Y VDD VSS A
M0 Y a_10_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VDD A a_10_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M2 VSS a_10_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M3 VDD a_10_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 VSS a_10_19# Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 Y a_10_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 Y a_10_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M7 VDD a_10_19# Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M8 Y a_10_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 VSS A a_10_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkbuf_8 Y VDD VSS A
M0 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M4 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 Y a_9_19# VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M8 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M10 VDD A a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M11 VSS a_9_19# Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M12 VSS a_9_19# Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M13 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M14 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M15 VDD a_9_19# Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M16 VDD a_9_19# Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M17 Y a_9_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkinv_1 A Y VDD VSS
M0 Y A VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M1 Y A VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkinv_16 A Y VDD VSS
M0 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 VDD A Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M8 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M10 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M11 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M12 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M13 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M14 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M15 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M16 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M17 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M18 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M19 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M20 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M21 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M22 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M23 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M24 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M25 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M26 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M27 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M28 VSS A Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M29 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M30 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M31 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkinv_2 A Y VDD VSS
M0 VDD A Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M2 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M3 VSS A Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkinv_4 A Y VDD VSS
M0 VDD A Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M3 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M4 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M5 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M6 VSS A Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M7 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__clkinv_8 A Y VDD VSS
M0 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 VSS A Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M4 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 VDD A Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M8 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M10 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M11 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M12 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M13 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M14 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M15 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__decap_1 VDD VSS
M0 VSS a_19_14# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.85p ps=5.4u w=0.85u l=0.3u
M1 VDD a_19_14# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=1.7p ps=8.8u w=1.7u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__dff_1 D CLK Q QN VDD VSS
M0 a_86_19# a_53_38# a_19_14# VSS nfet_03v3 ad=75f pd=0.85u as=0.343p ps=1.7u w=0.6u l=0.3u
M1 VSS a_161_42# a_148_19# VSS nfet_03v3 ad=0.215p pd=1.4u as=0.225p ps=1.35u w=0.6u l=0.3u
M2 a_42_73# D VDD VDD pfet_03v3 ad=0.638p pd=2.45u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 a_125_19# a_53_38# a_114_73# VDD pfet_03v3 ad=0.723p pd=2.55u as=0.213p ps=1.95u w=1.7u l=0.3u
M4 VSS a_9_19# a_86_19# VSS nfet_03v3 ad=0.215p pd=1.4u as=75f ps=0.85u w=0.6u l=0.3u
M5 a_86_73# CLK a_19_14# VDD pfet_03v3 ad=0.213p pd=1.95u as=0.723p ps=2.55u w=1.7u l=0.3u
M6 VDD a_161_42# a_148_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.638p ps=2.45u w=1.7u l=0.3u
M7 a_19_14# a_53_38# a_42_19# VSS nfet_03v3 ad=0.343p pd=1.7u as=0.318p ps=1.6u w=0.85u l=0.3u
M8 VSS a_161_42# QN VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M9 VDD a_9_19# a_86_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.213p ps=1.95u w=1.7u l=0.3u
M10 VDD a_161_42# QN VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M11 a_19_14# CLK a_42_73# VDD pfet_03v3 ad=0.723p pd=2.55u as=0.638p ps=2.45u w=1.7u l=0.3u
M12 VSS a_19_14# a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M13 a_53_38# CLK VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.215p ps=1.4u w=0.85u l=0.3u
M14 VDD a_19_14# a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M15 a_53_38# CLK VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M16 Q QN VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M17 a_148_19# CLK a_125_19# VSS nfet_03v3 ad=0.225p pd=1.35u as=0.343p ps=1.7u w=0.6u l=0.3u
M18 a_114_19# a_9_19# VSS VSS nfet_03v3 ad=0.105p pd=1.1u as=0.215p ps=1.4u w=0.85u l=0.3u
M19 a_161_42# a_125_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M20 a_148_73# a_53_38# a_125_19# VDD pfet_03v3 ad=0.638p pd=2.45u as=0.723p ps=2.55u w=1.7u l=0.3u
M21 Q QN VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M22 a_114_73# a_9_19# VDD VDD pfet_03v3 ad=0.213p pd=1.95u as=0.468p ps=2.25u w=1.7u l=0.3u
M23 a_161_42# a_125_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
M24 a_42_19# D VSS VSS nfet_03v3 ad=0.318p pd=1.6u as=0.233p ps=1.4u w=0.85u l=0.3u
M25 a_125_19# CLK a_114_19# VSS nfet_03v3 ad=0.343p pd=1.7u as=0.105p ps=1.1u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__dffn_1 D CLK Q QN VDD VSS
M0 a_86_19# a_53_38# a_19_14# VSS nfet_03v3 ad=75f pd=0.85u as=0.343p ps=1.7u w=0.6u l=0.3u
M1 VSS a_161_42# a_148_19# VSS nfet_03v3 ad=0.215p pd=1.4u as=0.225p ps=1.35u w=0.6u l=0.3u
M2 a_42_73# D VDD VDD pfet_03v3 ad=0.638p pd=2.45u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 a_125_19# a_53_38# a_114_73# VDD pfet_03v3 ad=0.723p pd=2.55u as=0.213p ps=1.95u w=1.7u l=0.3u
M4 Q QN VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 a_161_42# a_125_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 VSS a_9_19# a_86_19# VSS nfet_03v3 ad=0.215p pd=1.4u as=75f ps=0.85u w=0.6u l=0.3u
M7 a_86_73# a_50_62# a_19_14# VDD pfet_03v3 ad=0.213p pd=1.95u as=0.723p ps=2.55u w=1.7u l=0.3u
M8 VDD a_161_42# a_148_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.638p ps=2.45u w=1.7u l=0.3u
M9 Q QN VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M10 a_19_14# a_53_38# a_42_19# VSS nfet_03v3 ad=0.343p pd=1.7u as=0.318p ps=1.6u w=0.85u l=0.3u
M11 a_161_42# a_125_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M12 VDD a_9_19# a_86_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.213p ps=1.95u w=1.7u l=0.3u
M13 a_19_14# a_50_62# a_42_73# VDD pfet_03v3 ad=0.723p pd=2.55u as=0.638p ps=2.45u w=1.7u l=0.3u
M14 VSS a_19_14# a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M15 a_53_38# a_50_62# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.215p ps=1.4u w=0.85u l=0.3u
M16 VDD a_19_14# a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M17 VSS a_161_42# QN VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M18 a_53_38# a_50_62# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M19 VSS CLK a_50_62# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M20 a_148_19# a_50_62# a_125_19# VSS nfet_03v3 ad=0.225p pd=1.35u as=0.343p ps=1.7u w=0.6u l=0.3u
M21 VDD a_161_42# QN VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M22 a_114_19# a_9_19# VSS VSS nfet_03v3 ad=0.105p pd=1.1u as=0.215p ps=1.4u w=0.85u l=0.3u
M23 VDD CLK a_50_62# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M24 a_148_73# a_53_38# a_125_19# VDD pfet_03v3 ad=0.638p pd=2.45u as=0.723p ps=2.55u w=1.7u l=0.3u
M25 a_114_73# a_9_19# VDD VDD pfet_03v3 ad=0.213p pd=1.95u as=0.468p ps=2.25u w=1.7u l=0.3u
M26 a_42_19# D VSS VSS nfet_03v3 ad=0.318p pd=1.6u as=0.233p ps=1.4u w=0.85u l=0.3u
M27 a_125_19# a_50_62# a_114_19# VSS nfet_03v3 ad=0.343p pd=1.7u as=0.105p ps=1.1u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__dffsr_1 D CLK Q QN R VDD VSS S
M0 a_57_73# a_82_14# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 Q QN VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 a_234_73# CLK a_211_19# VDD pfet_03v3 ad=0.638p pd=2.45u as=0.723p ps=2.55u w=1.7u l=0.3u
M3 VSS a_25_19# a_247_47# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M4 a_172_73# a_137_41# a_82_14# VDD pfet_03v3 ad=0.213p pd=1.95u as=0.723p ps=2.55u w=1.7u l=0.3u
M5 a_247_47# a_25_19# a_291_73# VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M6 VSS a_41_73# a_172_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.105p ps=1.1u w=0.85u l=0.3u
M7 VSS a_247_47# a_234_19# VSS nfet_03v3 ad=0.215p pd=1.4u as=0.225p ps=1.35u w=0.6u l=0.3u
M8 VDD a_41_73# a_172_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.213p ps=1.95u w=1.7u l=0.3u
M9 VDD a_247_47# a_234_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.638p ps=2.45u w=1.7u l=0.3u
M10 a_41_73# a_25_19# VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M11 a_128_19# D VSS VSS nfet_03v3 ad=0.225p pd=1.35u as=0.3p ps=2.2u w=0.6u l=0.3u
M12 VSS a_247_47# QN VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M13 a_310_19# a_211_19# VSS VSS nfet_03v3 ad=0.105p pd=1.1u as=0.425p ps=2.7u w=0.85u l=0.3u
M14 a_25_19# R VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M15 a_128_73# D VDD VDD pfet_03v3 ad=0.638p pd=2.45u as=0.85p ps=4.4u w=1.7u l=0.3u
M16 VDD S a_57_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M17 VDD a_247_47# QN VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M18 a_200_19# a_41_73# VSS VSS nfet_03v3 ad=0.105p pd=1.1u as=0.233p ps=1.4u w=0.85u l=0.3u
M19 a_247_47# S a_310_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.105p ps=1.1u w=0.85u l=0.3u
M20 a_25_19# R VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
M21 a_57_73# a_25_19# a_41_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M22 a_291_73# S VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M23 a_211_19# CLK a_200_19# VSS nfet_03v3 ad=0.343p pd=1.7u as=0.105p ps=1.1u w=0.85u l=0.3u
M24 VDD a_211_19# a_291_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M25 a_82_14# a_137_41# a_128_19# VSS nfet_03v3 ad=0.343p pd=1.7u as=0.225p ps=1.35u w=0.6u l=0.3u
M26 a_137_41# CLK VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.215p ps=1.4u w=0.85u l=0.3u
M27 a_200_73# a_41_73# VDD VDD pfet_03v3 ad=0.213p pd=1.95u as=0.468p ps=2.25u w=1.7u l=0.3u
M28 a_211_19# a_137_41# a_200_73# VDD pfet_03v3 ad=0.723p pd=2.55u as=0.213p ps=1.95u w=1.7u l=0.3u
M29 a_82_14# CLK a_128_73# VDD pfet_03v3 ad=0.723p pd=2.55u as=0.638p ps=2.45u w=1.7u l=0.3u
M30 a_137_41# CLK VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M31 a_77_19# S a_41_73# VSS nfet_03v3 ad=0.105p pd=1.1u as=0.233p ps=1.4u w=0.85u l=0.3u
M32 Q QN VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M33 a_234_19# a_137_41# a_211_19# VSS nfet_03v3 ad=0.225p pd=1.35u as=0.343p ps=1.7u w=0.6u l=0.3u
M34 a_172_19# CLK a_82_14# VSS nfet_03v3 ad=0.105p pd=1.1u as=0.343p ps=1.7u w=0.85u l=0.3u
M35 VSS a_82_14# a_77_19# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.105p ps=1.1u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__dlat_1 D CLK Q VDD VSS
M0 Q a_137_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M1 a_43_73# D VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 VSS a_10_19# a_77_19# VSS nfet_03v3 ad=0.298p pd=1.55u as=0.383p ps=1.75u w=0.85u l=0.3u
M3 VDD a_10_19# a_77_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.893p ps=2.75u w=1.7u l=0.3u
M4 a_52_61# CLK VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.298p ps=1.55u w=0.85u l=0.3u
M5 VDD a_20_14# a_10_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M6 Q a_137_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 a_52_61# CLK VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M8 a_46_19# D VSS VSS nfet_03v3 ad=0.17p pd=1.25u as=0.298p ps=1.55u w=0.85u l=0.3u
M9 a_20_14# CLK a_46_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.17p ps=1.25u w=0.85u l=0.3u
M10 a_20_14# a_52_61# a_43_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M11 VSS a_10_19# a_137_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M12 VDD a_10_19# a_137_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M13 a_77_19# a_52_61# a_20_14# VSS nfet_03v3 ad=0.383p pd=1.75u as=0.233p ps=1.4u w=0.85u l=0.3u
M14 a_77_73# CLK a_20_14# VDD pfet_03v3 ad=0.893p pd=2.75u as=0.468p ps=2.25u w=1.7u l=0.3u
M15 VSS a_20_14# a_10_19# VSS nfet_03v3 ad=0.298p pd=1.55u as=0.425p ps=2.7u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__dlatn_1 D CLK Q VDD VSS
M0 a_43_73# D VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VSS a_10_19# a_77_19# VSS nfet_03v3 ad=0.298p pd=1.55u as=0.383p ps=1.75u w=0.85u l=0.3u
M2 VDD a_10_19# a_77_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.893p ps=2.75u w=1.7u l=0.3u
M3 VDD CLK a_54_14# VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
M4 a_52_61# a_54_14# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.298p ps=1.55u w=0.85u l=0.3u
M5 VDD a_20_14# a_10_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M6 a_52_61# a_54_14# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 a_46_19# D VSS VSS nfet_03v3 ad=0.17p pd=1.25u as=0.298p ps=1.55u w=0.85u l=0.3u
M8 a_20_14# a_54_14# a_46_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.17p ps=1.25u w=0.85u l=0.3u
M9 VSS a_10_19# a_173_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M10 a_20_14# a_52_61# a_43_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M11 VDD a_10_19# a_173_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M12 a_77_19# a_52_61# a_20_14# VSS nfet_03v3 ad=0.383p pd=1.75u as=0.233p ps=1.4u w=0.85u l=0.3u
M13 Q a_173_19# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M14 VSS CLK a_54_14# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M15 a_77_73# a_54_14# a_20_14# VDD pfet_03v3 ad=0.893p pd=2.75u as=0.468p ps=2.25u w=1.7u l=0.3u
M16 Q a_173_19# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M17 VSS a_20_14# a_10_19# VSS nfet_03v3 ad=0.298p pd=1.55u as=0.425p ps=2.7u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__fill_1 VDD VSS
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__fill_16 VDD VSS
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__fill_2 VDD VSS
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__fill_4 VDD VSS
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__fill_8 VDD VSS
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__inv_1 A Y VDD VSS
M0 Y A VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M1 Y A VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__inv_16 A Y VDD VSS
M0 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 VDD A Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M8 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M10 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M11 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M12 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M13 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M14 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M15 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M16 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M17 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M18 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M19 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M20 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M21 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M22 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M23 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M24 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M25 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M26 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M27 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M28 VSS A Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M29 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M30 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M31 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__inv_2 A Y VDD VSS
M0 VDD A Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M2 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M3 VSS A Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__inv_4 A Y VDD VSS
M0 VDD A Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M3 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M4 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M5 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M6 VSS A Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M7 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__inv_8 A Y VDD VSS
M0 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 VDD A Y VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M3 VSS A Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M4 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M5 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M6 VDD A Y VDD pfet_03v3 ad=0.935p pd=4.5u as=0.468p ps=2.25u w=1.7u l=0.3u
M7 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M8 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M9 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M10 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M11 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M12 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M13 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M14 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.468p ps=2.25u w=1.7u l=0.3u
M15 VSS A Y VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__mux2_1 A B Sel Y VDD VSS
M0 Y a_25_19# A VSS nfet_03v3 ad=0.298p pd=1.55u as=0.425p ps=2.7u w=0.85u l=0.3u
M1 a_25_19# Sel VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M2 Y Sel A VDD pfet_03v3 ad=0.595p pd=2.4u as=0.85p ps=4.4u w=1.7u l=0.3u
M3 a_25_19# Sel VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
M4 B Sel Y VSS nfet_03v3 ad=0.553p pd=3u as=0.298p ps=1.55u w=0.85u l=0.3u
M5 B a_25_19# Y VDD pfet_03v3 ad=1.11p pd=4.7u as=0.595p ps=2.4u w=1.7u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__nand2_1 A B Y VDD VSS
M0 VSS B a_28_19# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.105p ps=1.1u w=0.85u l=0.3u
M1 VDD B Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M2 Y A VDD VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M3 a_28_19# A Y VSS nfet_03v3 ad=0.105p pd=1.1u as=0.425p ps=2.7u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__nor2_1 A B Y VDD VSS
M0 a_28_73# A VDD VDD pfet_03v3 ad=0.213p pd=1.95u as=0.85p ps=4.4u w=1.7u l=0.3u
M1 Y B a_28_73# VDD pfet_03v3 ad=0.85p pd=4.4u as=0.213p ps=1.95u w=1.7u l=0.3u
M2 Y A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M3 VSS B Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__oai21_1 A0 A1 B Y VDD VSS
M0 a_27_73# A0 VDD VDD pfet_03v3 ad=0.255p pd=2u as=0.85p ps=4.4u w=1.7u l=0.3u
M1 Y A1 a_27_73# VDD pfet_03v3 ad=0.553p pd=2.35u as=0.255p ps=2u w=1.7u l=0.3u
M2 Y B a_8_19# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.275p ps=1.5u w=0.85u l=0.3u
M3 VSS A0 a_8_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M4 VDD B Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.553p ps=2.35u w=1.7u l=0.3u
M5 a_8_19# A1 VSS VSS nfet_03v3 ad=0.275p pd=1.5u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__oai22_1 A0 A1 B0 B1 Y VDD VSS
M0 a_27_73# A0 VDD VDD pfet_03v3 ad=0.255p pd=2u as=0.85p ps=4.4u w=1.7u l=0.3u
M1 Y A1 a_27_73# VDD pfet_03v3 ad=0.553p pd=2.35u as=0.255p ps=2u w=1.7u l=0.3u
M2 Y B0 a_8_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.275p ps=1.5u w=0.85u l=0.3u
M3 VSS A0 a_8_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M4 a_58_73# B0 Y VDD pfet_03v3 ad=0.213p pd=1.95u as=0.553p ps=2.35u w=1.7u l=0.3u
M5 VDD B1 a_58_73# VDD pfet_03v3 ad=0.85p pd=4.4u as=0.213p ps=1.95u w=1.7u l=0.3u
M6 a_8_19# B1 Y VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M7 a_8_19# A1 VSS VSS nfet_03v3 ad=0.275p pd=1.5u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__oai31_1 A0 A1 A2 B Y VDD VSS
M0 VDD B Y VDD pfet_03v3 ad=0.85p pd=4.4u as=0.553p ps=2.35u w=1.7u l=0.3u
M1 a_25_19# A1 VSS VSS nfet_03v3 ad=0.275p pd=1.5u as=0.233p ps=1.4u w=0.85u l=0.3u
M2 a_25_19# A2 VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M3 Y A1 a_45_73# VDD pfet_03v3 ad=0.553p pd=2.35u as=0.255p ps=2u w=1.7u l=0.3u
M4 Y B a_25_19# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.275p ps=1.5u w=0.85u l=0.3u
M5 a_34_73# A2 VDD VDD pfet_03v3 ad=0.213p pd=1.95u as=0.85p ps=4.4u w=1.7u l=0.3u
M6 VSS A0 a_25_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M7 a_45_73# A0 a_34_73# VDD pfet_03v3 ad=0.255p pd=2u as=0.213p ps=1.95u w=1.7u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__or2_1 A B Y VDD VSS
M0 VSS B a_9_73# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.233p ps=1.4u w=0.85u l=0.3u
M1 VDD B a_25_73# VDD pfet_03v3 ad=0.595p pd=2.4u as=0.213p ps=1.95u w=1.7u l=0.3u
M2 Y a_9_73# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M3 a_9_73# A VSS VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M4 a_25_73# A a_9_73# VDD pfet_03v3 ad=0.213p pd=1.95u as=0.85p ps=4.4u w=1.7u l=0.3u
M5 Y a_9_73# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.595p ps=2.4u w=1.7u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__tbuf_1 A EN Y VDD VSS
M0 a_44_73# a_9_19# VDD VDD pfet_03v3 ad=0.213p pd=1.95u as=0.553p ps=2.35u w=1.7u l=0.3u
M1 Y EN a_44_19# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.105p ps=1.1u w=0.85u l=0.3u
M2 a_49_59# EN VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M3 Y a_49_59# a_44_73# VDD pfet_03v3 ad=0.85p pd=4.4u as=0.213p ps=1.95u w=1.7u l=0.3u
M4 a_49_59# EN VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
M5 VSS A a_9_19# VSS nfet_03v3 ad=0.275p pd=1.5u as=0.425p ps=2.7u w=0.85u l=0.3u
M6 VDD A a_9_19# VDD pfet_03v3 ad=0.553p pd=2.35u as=0.85p ps=4.4u w=1.7u l=0.3u
M7 a_44_19# a_9_19# VSS VSS nfet_03v3 ad=0.105p pd=1.1u as=0.275p ps=1.5u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__tieh Y VDD VSS
M0 a_19_14# a_19_14# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M1 Y a_19_14# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__tiel Y VDD VSS
M0 Y a_19_14# VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.425p ps=2.7u w=0.85u l=0.3u
M1 a_19_14# a_19_14# VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.85p ps=4.4u w=1.7u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__tinv_1 A EN Y VDD VSS
M0 a_44_73# A VDD VDD pfet_03v3 ad=0.213p pd=1.95u as=0.553p ps=2.35u w=1.7u l=0.3u
M1 Y EN a_44_19# VSS nfet_03v3 ad=0.425p pd=2.7u as=0.105p ps=1.1u w=0.85u l=0.3u
M2 Y a_9_19# a_44_73# VDD pfet_03v3 ad=0.85p pd=4.4u as=0.213p ps=1.95u w=1.7u l=0.3u
M3 VSS EN a_9_19# VSS nfet_03v3 ad=0.275p pd=1.5u as=0.425p ps=2.7u w=0.85u l=0.3u
M4 VDD EN a_9_19# VDD pfet_03v3 ad=0.553p pd=2.35u as=0.85p ps=4.4u w=1.7u l=0.3u
M5 a_44_19# A VSS VSS nfet_03v3 ad=0.105p pd=1.1u as=0.275p ps=1.5u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__xnor2_1 A B Y VDD VSS
M0 VDD B a_78_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.298p ps=2.05u w=1.7u l=0.3u
M1 Y a_49_14# a_42_19# VSS nfet_03v3 ad=0.373p pd=1.75u as=0.147p ps=1.2u w=0.85u l=0.3u
M2 a_49_14# B VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M3 a_42_73# a_9_19# VDD VDD pfet_03v3 ad=0.298p pd=2.05u as=0.468p ps=2.25u w=1.7u l=0.3u
M4 Y a_49_14# a_42_73# VDD pfet_03v3 ad=0.723p pd=2.55u as=0.298p ps=2.05u w=1.7u l=0.3u
M5 a_49_14# B VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M6 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M7 VDD A a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M8 a_78_19# a_9_19# Y VSS nfet_03v3 ad=0.147p pd=1.2u as=0.373p ps=1.75u w=0.85u l=0.3u
M9 VSS B a_78_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.147p ps=1.2u w=0.85u l=0.3u
M10 a_78_73# A Y VDD pfet_03v3 ad=0.298p pd=2.05u as=0.723p ps=2.55u w=1.7u l=0.3u
M11 a_42_19# A VSS VSS nfet_03v3 ad=0.147p pd=1.2u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

.SUBCKT gf180mcu_osu_sc_gp9t3v3__xor2_1 A B Y VDD VSS
M0 a_42_73# A VDD VDD pfet_03v3 ad=0.425p pd=2.2u as=0.468p ps=2.25u w=1.7u l=0.3u
M1 VSS a_52_62# a_81_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.213p ps=1.35u w=0.85u l=0.3u
M2 VDD B a_81_73# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.425p ps=2.2u w=1.7u l=0.3u
M3 Y B a_42_19# VSS nfet_03v3 ad=0.36p pd=1.7u as=0.213p ps=1.35u w=0.85u l=0.3u
M4 VSS A a_9_19# VSS nfet_03v3 ad=0.233p pd=1.4u as=0.425p ps=2.7u w=0.85u l=0.3u
M5 Y a_52_62# a_42_73# VDD pfet_03v3 ad=0.723p pd=2.55u as=0.425p ps=2.2u w=1.7u l=0.3u
M6 VDD A a_9_19# VDD pfet_03v3 ad=0.468p pd=2.25u as=0.85p ps=4.4u w=1.7u l=0.3u
M7 a_81_19# a_9_19# Y VSS nfet_03v3 ad=0.213p pd=1.35u as=0.36p ps=1.7u w=0.85u l=0.3u
M8 a_52_62# B VSS VSS nfet_03v3 ad=0.425p pd=2.7u as=0.233p ps=1.4u w=0.85u l=0.3u
M9 a_81_73# a_9_19# Y VDD pfet_03v3 ad=0.425p pd=2.2u as=0.723p ps=2.55u w=1.7u l=0.3u
M10 a_52_62# B VDD VDD pfet_03v3 ad=0.85p pd=4.4u as=0.468p ps=2.25u w=1.7u l=0.3u
M11 a_42_19# A VSS VSS nfet_03v3 ad=0.213p pd=1.35u as=0.233p ps=1.4u w=0.85u l=0.3u
.ENDS

