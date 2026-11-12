.subckt mos_inv in out vdd vss
Mn out in vss vss nfet_3v3 w=1320n l=280n nf=2 m=1
Mp out in vdd vdd pfet_3v3 w=2640n l=280n nf=2 m=1
.ends mos_inv
