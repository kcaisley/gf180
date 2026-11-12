.subckt mos_inv in out vdd vss
Mn out in vss vss nfet_05v0 w=1200n l=600n nf=2 m=1
Mp out in vdd vdd pfet_05v0 w=1800n l=500n nf=2 m=1
.ends mos_inv
