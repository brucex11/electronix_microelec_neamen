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
* `Kn_in_NONsaturation  Kn_in_saturation  calc_Knp_from_conduction_parameters`
* `calc_Kn_via_iteration`
* `MOSFET_conduction_param_Kn  MOSFET_saturation_current  NMOS_threshold_voltage_VTN`
* `NMOS_calc_iD_function  PMOS_calc_iD_function`
* `calc_iDS_for_NMOS_enhancement_in_nonsaturation  calc_iDS_for_NMOS_enhancement_in_saturation`
* `ratio_equations_iDS_in_nonsaturation`
* `estimate_VTN_iDS_per_graph  matplotlib_multiple_curves  scatterplot_intersection`
* `matplotlib_slice  matplotlib_stop_plot_past_point`
* `region_of_operation  saturation  ohmic  cutoff`
* `ratio_of_currents  ratio_of_voltages  solve_for_W/L`
* `plot_scatter_line  PMOS_vSDsat_iSD`
* `NMOS_finite_output_resistance  NMOS_body_effect`
* `given_Kn_calc_VGS  ohmic_vs_saturation_region`
* `PMOS_depletion_mode`


# Examples, Exercises, Test Your Understanding, and Problems
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.X):

X.X: Description
* worked-file PATH, textbook page num
* associated word docx (optional)
* LTspice folder (optional)
* keywords list `YYY`  `ZZZ`(optional)


## Examples
3.1: Calculate the current in an n-channel MOSFET.
* example/exam3_01.py, textbook page 134
* keywords: `calc_Knp_from_conduction_parameters`
* keywords: `MOSFET_conduction_param_Kn`  `MOSFET_saturation_current`  `NMOS_threshold_voltage_VTN`
* keywords: `angstroms_per_meter`  `cm_per_meter`

3.2: Determine the source-to-drain voltage vSD required to bias a p-channel
enhancement-mode MOSFET in the saturation region.
* example/exam3_02.py, textbook page 136


## Exercises
3.1: Solve for Kn conduction parameter per equations 3.2a and 3.2b, then calc iDS.
* exercise/exer3_01.py, textbook page 134
* keywords: `Kn_in_NONsaturation`  `Kn_in_saturation`

3.2: For PMOS in enhancement mode, calculate current iSD.
* exercise/exer3_02.py, textbook page 137
* keywords: `NMOS_calc_iD_function`  `PMOS_calc_iD_function`


## Test Your Understanding
3.1: An n-channel enhancement-mode MOSFET has a threshold voltage of
VTN = 1.2V and an applied gate-to-source voltage of vGS = 2V.
Determine the  region of operation.
* ./chap03/testunder/test3_01, textbook pg 145
* keywords: `calc_iDS_for_NMOS_enhancement_in_nonsaturation  calc_iDS_for_NMOS_enhancement_in_saturation`
* keywords: `calc_Kn_via_iteration`

3.2: For NMOS devices described in Exercise TYU 3.1e, calculate conduction param Kn.
* ./chap03/testunder/test3_02, textbook pg 145
* ./doc/testunder/chap03_testunder3_02.md  for explanation of λ in context
of MOSFET conduction parameter calculation Kn/Kp (there is none).


## Problems
3.1: Calculate the drain current in an NMOS transistor.
* problem/prob3_01.py, textbook page 194
* keywords: `iDS_in_saturation`  `iDS_in_NONsaturation`

3.2: Calculate Kn and vDS using ratio of equations for iDS in nonsaturation.
* problem/prob3_02.py, pg 194
* keywords: `ratio_equations_iDS_in_nonsaturation`

3.3: Given graph transistor characteristics iD versus vDS for an NMOS device,
estimate VTN and iDS, and calc iD(sat) for vGS = 3.5V and vGS = 4.5V.
* problem/prob3_03.py, pg 194
* keywords: `estimate_VTN_iDS_per_graph`

3.3.plot: Given graph transistor characteristics iD versus vDS for an NMOS device,
estimate VTN and iDS, and calc iD(sat) for vGS = 3.5V and vGS = 4.5V.
* problem/prob3_03_plot.py, pg 194
* ./docx/problem/chap03_problem3_03_plot.docx
* keywords: `matplotlib_multiple_curves  scatterplot_intersection`

3.3.plot.full: Continuation of 3.3.plot; draw the saturation-region of the iDS
by slicing-off the non-sat curve after the transition-point for each VGS.
* problem/prob3_03_plot_full.py, pg 194
* ./docx/problem/chap03_problem3_03_plot.docx
* keywords: `matplotlib_slice  matplotlib_stop_plot_past_point`

3.5: The threshold voltage of each transistor in Figure P3.5 is VTN = 0.4V.
Determine the region of operation of the transistor in each circuit.
* problem/prob3_05.py, pg 194
* keywords: `region_of_operation  saturation  ohmic  cutoff`

3.13: For a p-channel enhancement-mode MOSFET, k'p = 50μA/V^2 ... Determine the
W/L ratio and the value of VTP.
* problem/prob3_13.py, pg 195
* keywords: `ratio_of_currents  ratio_of_voltages  solve_for_W/L`

3.16: A p-channel depletion-mode MOSFET has parameters VTP = +2V ...  calculate
	the drain current in the saturation	region.
* problem/prob3_16.py, pg 196
* ./docx/problem/chap03_prob3_16_PMOS_plot.docx
* keywords: `plot_scatter_line  PMOS_vSDsat_iSD`

3.19: Design the widths for the two PMOS and NMOS transistors such that they
are electrically equivalent.
* problem/prob3_19.py, pg 196
* keywords: `angstroms_per_meter  solve_for_W/L`

3.22: At what value of VSB will the threshold voltage change by 2V due
to the body effect?
* problem/prob3_22.py, pg 196
* keywords: `NMOS_finite_output_resistance  NMOS_body_effect`

3.30: Consider the circuit in Figure P3.30.
* problem/prob3_30.py, pg 197
* ./LTspice/chap03/prob3_30/prob3_30.asc
* keywords: ``

3.34: Per Figure P3.34, determine VGS such that ID = 0.35mA; determine VDS
and VDS (sat).
* problem/prob3_34.py, pg 198
* keywords: `given_Kn_calc_VGS  ohmic_vs_saturation_region`

3.41: Design the circuit in Figure P3.41 so that VSD = 2.5V.
* problem/prob3_41.py, pg 199
* keywords: `PMOS_depletion_mode`


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
* Pg 133: `Kn` is the `conduction parameter` which for an n-channel/p-substrate
device is given by equation 3.3a.
* Pg 136: `Kp` is the `conduction parameter` which for an p-channel/n-substrate
device is given by equation 3.5a.
* Pg 133: The conduction parameter `(Kn | Kp)` is a function of both `electrical`
and `geometric parameters`:
  - the `electrical` oxide capacitance and carrier mobility are essentially
    constants for a given fabrication technology, and
  - the `geometry`, or width-to-length ratio W/L, is a variable in the MOSFET's
    structure/footprint.
* Pg 136: Biasing a transistor in either the saturation or the nonsaturation
 region depends on both the gate-to-source voltage and the drain-to-source
 voltage.
* Pg 1: 
* Pg 1: 
* Pg 1: 
* Pg 1: 
* Pg 1: 
* Pg 1: 
