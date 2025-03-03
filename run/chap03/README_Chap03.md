# Python Project MICROELEC_NEAMEN
# Electronix Microelectronics
Problems from the textbook: Microelectronics Circuit Analysis and Design, 4th Edition by Donald Neamen.

Figures and notes for all `./subdir` examples, exercises, and problems for this
chapter are contained in MSWord docx located in the `./subdir/doc` folder.
Don't forget to update .gitignore to preclude .docx binaries from repository.

# Search This Document
Use the keywords below for python-code implementations, problems with plots, etc.
When applicable, each problem has keywords that reflect code in that problem.

## Available Keywords
* `conduction  angstroms_per_meter  cm_per_meter`
* `iDS_in_saturation  iDS_in_NONsaturation`
* `Kn_in_NONsaturation  Kn_in_saturation`
* `MOSFET_conduction_param_Kn  MOSFET_saturation_current  NMOS_threshold_voltage_VTN`


# Examples, Exercises, Test Your Understanding, and Problems
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.X):

X.X: Description
* worked-file PATH, textbook page num
* associated word docx (optional)
* LTspice folder (optional)
* keywords list `YYY  ZZZ`(optional)


## Examples
3.1: Calculate the current in an n-channel MOSFET.
* example/exam3_01.py, textbook page 134
* keywords: `MOSFET_conduction_param_Kn  MOSFET_saturation_current  NMOS_threshold_voltage_VTN`
* keywords: `angstroms_per_meter  cm_per_meter`


## Exercises
3.1: Solve for Kn conduction parameter per equations 3.2a and 3.2b, then calc iDS.
* exercise/exer3_01.py, textbook page 134
* keywords: `Kn_in_NONsaturation  Kn_in_saturation`


## Test Your Understanding
TYU 77.9: Per Exercise EX 1.8, Fig 1.28, determine VD and ID, using the graphical technique.
* ./chap01/testunder/test1_09, textbook pg 43


## Problems
3.1: Calculate the drain current in an NMOS transistor.
* problem/prob3_01.py, textbook page PP
* keywords: `iDS_in_saturation  iDS_in_NONsaturation`


# Notes
* Pg 126: The `metal-oxide-semiconductor field-effect transistor` (MOSFET)
achieved volume production in 1967. The MOSFET, compared to BJTs, are very
small (that is, it occupies a very small area on an IC chip).
* Pg 126: `field effect`: modulate the conductance of a semiconductor, or control
the current in a semiconductor, by applying an electric field perpendicular to
the surface.
* Pg 127: For Fig 3.1, the parameter tox is the thickness of the oxide and
 εox is the `oxide permittivity`.
* Pg 127: For an n-channel MOSFET, a large, positive gate voltage generates
an `electron inversion layer` inside the p-type substrate against the oxide-layer.
* Pg 128: For a p-channel MOSFET, a large, negative gate voltage generates
a `hole inversion layer` inside the n-type substrate against the oxide-layer.
* Pg 128: The magnitude of the charge in the `inversion layer` is a function
of the applied gate voltage.
* Pg 128: The term `enhancement mode` means that a Gate Voltage (VG) must be
applied to the gate to create the inversion layer.
* Pg 128: To enable `enhancement mode`, the Gate Voltage (VG) must be the
`same polarity` as the substrate-type and `opposite polarity` of the channel-type.
* Therefore, to induce current flow for the 2 channel-types in `enhancement mode`:
  - `(NMOS)` N-CHANNEL ENHANCEMENT with p-type substrate: VG is positive, and
	  the current carriers in the N-CHANNEL are `electrons`.
  - `(PMOS)` P-CHANNEL ENHANCEMENT with n-type substrate: VG is negative, and
	  the current carriers in the P-CHANNEL are `holes`.
* Pg 129: The MOSFET substrate is also called the `body` and is denoted as `B`
on its schematic symbol.
* Pg 130: The source terminal supplies carriers that flow through the channel,
and the drain terminal allows the carriers to drain from the channel.
* Pg 130: Since the gate terminal is separated from the channel by an oxide
or insulator, there is `no gate current`.
  - Similarly, since the channel and substrate are separated by a space-charge
	  region, there is essentially `no current through the substrate`.
* Pg 130: The `threshold voltage VTN` of the n-channel MOSFET (NMOS) is defined
as the applied gate voltage needed to create an `inversion charge` in which the
density is equal to the concentration of majority carriers in the semiconductor
substrate.
  - In simple terms, we can think of the `threshold voltage` as the gate voltage
required to `turn on` the transistor.
  - For `PMOS`, threshold voltage == `VTP`.
* Pg 133: `Kn` is the `conduction parameter` which for an n-channel device
is given by equation 3.3a.
* Pg 1: 
* Pg 1: 
* Pg 1: 
* Pg 1: 
