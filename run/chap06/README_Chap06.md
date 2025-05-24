# Python Project MICROELEC_NEAMEN
# Electronix Microelectronics Chap 06
Problems from the textbook: Microelectronics Circuit Analysis and Design, 4th Edition by Donald Neamen.

Figures and notes for all `./subdir` examples, exercises, and problems for this
chapter are contained in MSWord docx located in the `./docx/` folder.
Don't forget to update .gitignore to preclude .docx binaries from repository.

# Search This Document
Use the keywords below for python-code implementations, problems with plots, etc.
When applicable, each problem has keywords that reflect code in that problem.

## Available Keywords
* `voltage_divider`  `Thevenin_voltage`  `Thevenin_resistance`
* `small_signal`  `voltage_gain`  `current_gain`  `rpi`  `input_resistance`
* `impedance_reflection`  `output_resistance`  `transconductance`
* `output_voltage_swing`  `single_DC_supply`
* `gm`  `Vpi`  `rpi`  `voltage_gain`
* `Rin`  `Rib`  `rpi`  `Ro`  `ro`
* `current_divider`  `Thevenin`
* `Av`  `rpi`  `voltage_gain`  `Ri`  `Ro`
* `common_base_current_gain`  `common_base_voltage_gain`
* `iteration_range`
* `common_emitter_current_gain`  `common_emitter_voltage_gain`
* `python_iteration_range`  `AC_rides_on_DC_bias`


# Examples, Exercises, Test Your Understanding, Problems, and Figures
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.X):

X.X: Description
* worked-file PATH, page num
* associated word docx (optional)
* ./LTspice folder (optional)
* BENCH - ENKI2: C:\ENKI2\Electronix\BENCH\BENCH_subdir_struct.txt
* keywords list `YYY ZZZ`(optional)

Any python file that contains `*D.py` is a `D`ESIGN problem.

Figures are solutions to figures in the text.  This was inspired by development
of a tool to iterate resistances for simple circuits.  See Fig6_14.

## Examples
6.01: Calculate the small-signal voltage gain of the most-basic NPN BJT
circuit shown in Figure 6.3.
* example/exam6_01.py, page 382
* keywords: `gm`  `Vpi`  `rpi`  `voltage_gain`

6.06: Calculate the small-signal voltage gain of PNP BJT circuit shown
in Figure 6.32.
* example/exam6_06.py, page 404
* ./docx/chap06/example/chap06_exam6_06.docx
* keywords: `gm`  `Vpi`  `rpi`  `voltage_gain`

6.13: Calculate the small-signal Rin and Ro per Figure 6.49.
* example/exam6_13.py, pg 424
* keywords: `Rin`  `Rib`  `rpi`  `Ro`  `ro`


## Exercises
6.01: Calculate the small-signal voltage gain of the most-basic NPN BJT
circuit shown in Figure 6.3.
* exercise/exerm6_01.py, page 383
* keywords: `gm`  `Vpi`  `rpi`  `voltage_gain`

6.07: For the circuit in Figure 6.38, (a) determine the input resistance seen
by the signal source, and (b) find the small-signal voltage gain.
* exercise/exerm6_07.py, page 410
* ./docx/chap06/exercise/chap06_exer6_07.docx
* keywords: `Av`  `rpi`  `voltage_gain`  `Ri`  `Ro`


## Test Your Understanding
TYU6.07: For the circuit in Figure 6.39, let B = 125 and VA = 200V.
Determine the small-signal voltage gain Av and Ro.
* testunder/test6_07, pg 410
* ./LTspice/chap06/test6_07/
* ./docx/chap06/testunder/chap06_test6_07_LTspice.docx
* keywords: `impedance_reflection`  `inverse_impedance_reflection`

TYU6.13: For the circuit shown in Figure 6.63 calculate ICQ, VECQ, Av, Ai.
* testunder/test6_13, pg 434
* ./LTspice/chap06/test6_13/  (none as of 16Apr25)
* ./docx/chap06/testunder/chap06_test6_13.docx
* keywords: `common_base_current_gain`  `common_base_voltage_gain`
* Note: LTspice simulation confirms textbook answers (see docx).

## Problems
6.04: The transistor in Figure 6.3 has parameters β = 120 and VA = inf.
Determine iC, vCE, Av, Ai.
Use iteration to determine VBB:RB pair to satisfy Q-point; then simulate
using the problem given as input.
* problem/prob6_04.py, page 451
* ./LTspice/chap06/prob6_04
* ./docx/chap06/problem/chap06_04.docx
* keywords: `common_emitter_current_gain`  `common_emitter_voltage_gain`
* keywords: `python_iteration_range`  `AC_rides_on_DC_bias`

6.44_assumeIB: The transistor parameters for the circuit in Figure P6.44 are
β = 180	and	VA = inf.  Assume IB = 75μA.  (a) Find ICQ and VCEQ.
* problem/prob6_44assumeIB.py, page 459
* ./LTspice/chap06/prob6_44

![Fig6_44](../../doc/mdimg/chap06_figP6_44.png)

6.44a: The transistor parameters for the circuit in Figure P6.44 are β = 180
and	VA = inf.  Assume ideal Q1.  (a) Find ICQ and VCEQ.
* problem/prob6_44a.py, page 459
* ./LTspice/chap06/prob6_44
* keywords: `voltage_divider  Thevenin_voltage  Thevenin_resistance`

6.44b: The transistor parameters for the circuit in Figure P6.44 are β = 180
and	VA = inf.  Plot DC and AC load-lines using Q-point from part (a).
* problem/prob6_44b.py, page 459
* ./docx/chap06/problem/chap06_prob6_44b.docx
* keywords: `voltage_divider  Thevenin_voltage  Thevenin_resistance`

![P6.44b](../../docx/png/chap06_prob6_44b_acdc_load_lines.png)

6.44cd: The transistor parameters for the circuit in Figure P6.44 are β = 180
and	VA = inf.  Assume ideal Q1.  (c) Calculate the small-signal voltage gain.
(d) Calculate Rib and Ro.
* problem/prob6_44c.py, page 459
* ./docx/chap06/problem/chap06_prob6_44cd.docx
* ./LTspice/chap06/prob6_44
* keywords: `small_signal`  `voltage_gain`  `current_gain`  `rpi`  `input_resistance`
* keywords: `impedance_reflection`  `output_resistance`  `transconductance`

6.45a: The transistor parameters for the circuit in Figure P6.44 are β = 180
and	VA = inf.  Assume ideal Q1.  (a) Find ICQ and VCEQ.
* problem/prob6_45a.py, page 459
* ./docx/chap06/problem/chap06_prob6_45_VCC10V.docx
* ./LTspice/chap06/prob6_45
* keywords: `voltage_divider  Thevenin_voltage  Thevenin_resistance`

6.45b: The transistor parameters for the circuit in Figure P6.45 are β = 120
and	VA = inf.  Plot DC and AC load-lines using Q-point from part (a).
* problem/prob6_45b.py, page 459
* keywords: `voltage_divider  Thevenin_voltage  Thevenin_resistance`

![P6.45b](../../docx/png/chap06_prob6_45b_dc_load_line.png)

6.48: Consider the emitter-follower amplifier shown in Figure P6.48.
The transistor parameters are β = 100 and VA = 100 V. (a) Find the output
resistance Ro.
* problem/prob6_48.py, page 460
* ./docx/chap06/problem/chap06_prob6_48_VCC6V.docx
* keywords: `output_resistance`

D6.50: For the transistor in Figure P6.50, the parameters are β = 100 and
VA = inf.
(a) Design the circuit such that IEQ = 1mA and the Q-point is in the center
of the dc load line.
* problem/prob6_50D.py, page 460
* ./docx/chap06/problem/chap06_prob6_50D.docx
* ./LTspice/chap06/prob6_50D
* keywords: `small_signal`  `voltage_gain`  `rpi`

![P6.50D](../../LTspice/schematics_for_diagrams_only/chap06/prob6_50D/prob6_50D_AC_small-signal_equivalent.png)

![P6.50D](../../LTspice/schematics_for_diagrams_only/chap06/prob6_50D/prob6_50D_AC_small-signal_with_1k-load.png)

D6.56: For the emitter-follower circuit in Figure P6.54, assume VCC = 24V,
β = 75, and Ai = io/is = 8. Design the circuit to drive an 8Ω load.
(a) Design the circuit such that IEQ = 1mA and the Q-point is in the center
of the dc load line.
* problem/prob6_56D.py, page 462
* ./docx/chap06/problem/chap06_prob6_56D.docx
* ./LTspice/chap06/prob6_56D
* keywords: `current_divider`  `Thevenin`  `Thevenin_resistance`  `impedance_reflection`

![P6.56D](../../LTspice/schematics_for_diagrams_only/chap06/prob6_56D/prob6_56D_AC_small-signal_RTh.png)

6.76a: Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(a) Determine the small-signal parameters gm, rπ, and ro for both transistors.
* problem/prob6_76a.py, page 466
* keywords: `small_signal  voltage_gain  current_gain  rpi  input_resistance`
* keywords: `output_resistance  transconductance`

6.76b: Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(b) Plot the dc and ac load lines for both transistors.
* problem/prob6_76b.py, page 466
* ./docx/chap06/problem/chap06_prob6_76b.docx
* keywords: `small_signal  voltage_gain  current_gain  rpi  input_resistance`
* keywords: `output_resistance  transconductance`

![P6.76b](../../docx/png/chap06_prob6_76b_Q1_acdc_load_lines.png)

6.76cde: Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(b) Plot the dc and ac load lines for both transistors.
* problem/prob6_76cde.py, page 466
* ./docx/chap06/problem/chap06_prob6_76cde_LTspice.docx
* ./LTspice/chap06/prob6_76
* keywords: `small_signal`  `voltage_gain`  `current_gain`  `rpi`
* keywords: `output_resistance`  `output_voltage_swing`


## Figures
6.14: Determine Q-point IBQ, ICQ and VCEQ for Figure 6.14.
Calculate circuit Av = Vo / Vs and compare with simulation.
See ./LTspice/chap06/fig6_14/.
* figure/fig6_14.py, page 466
* ./docx/chap06/figure/chap06_fig6_14.docx
* ./LTspice/chap06/fig6_14
* BENCH - ENKI2: C:\ENKI2\Electronix\BENCH\BJT\CE_single_supply\
* keywords: `small_signal`  `voltage_gain`  `current_gain`  `rpi`
* keywords: `output_resistance`  `output_voltage_swing`  `single_DC_supply`


# Notes
* Pg XX: 
