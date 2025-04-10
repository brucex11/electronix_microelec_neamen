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
* `output_voltage_swing`  `self_bias`
* `gm`  `Vpi`  `rpi`  `voltage_gain`
* `Rin`  `Rib`  `rpi`  `Ro`  `ro`


# Examples, Exercises, Test Your Understanding, Problems, and Figures
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.X):

X.X: Description
* worked-file PATH, page num
* associated word docx (optional)
* ./LTspice folder (optional)
* keywords list `YYY ZZZ`(optional)

Any python file that contains `*D.py` is a `D`ESIGN problem.

Figures are solutions to figures in the text.  This was inspired by development
of a tool to iterate resistances for simple circuits.  See Fig6_14.

## Examples
6.01: Calculate the small-signal voltage gain of the most-basic NPN BJT
circuit shown in Figure 6.3.
* example/exam6_01.py, page 382
* keywords: `gm`  `Vpi`  `rpi`  `voltage_gain`

6.13: Calculate the small-signal Rin and Ro per Figure 6.49.
* example/exam6_13.py, pg 424
* keywords: `Rin`  `Rib`  `rpi`  `Ro`  `ro`


## Exercises
6.01: Calculate the small-signal voltage gain of the most-basic NPN BJT
circuit shown in Figure 6.3.
* exercise/exerm6_01.py, page 383
* keywords: `gm`  `Vpi`  `rpi`  `voltage_gain`


## Test Your Understanding
TYU 77.9: Per Exercise EX 1.8, Fig 1.28, determine VD and ID, using the graphical technique.
* /testunder/test1_09, pg 43


## Problems
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
* keywords: `small_signal`  `voltage_gain`  `current_gain`  `rpi`
* keywords: `output_resistance`  `output_voltage_swing`  `self_bias`


# Notes
* Pg XX: 
