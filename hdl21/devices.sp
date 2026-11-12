* The package's device names the GF180MCU decks lack, in SPICE, which Spectre and ngspice both
* read (pdk_logic.Install.include_devices): include after the resistor models (res_<corner>).

* the unsalicided P+ poly resistor by its body's length and width (meters), the parameters of
* frida's poly-resistor requests (flow/layout/devices/polyres), on the deck's ppolyf_u
.subckt ppolyf_u_lw p n b l=2e-6 w=8e-7
xr p n b ppolyf_u r_length=l r_width=w
.ends ppolyf_u_lw
