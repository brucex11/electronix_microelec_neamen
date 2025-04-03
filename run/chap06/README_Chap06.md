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
* `output_voltage_swing`
* `gm`  `Vpi`  `rpi`  `voltage_gain`


# Examples, Exercises, Test Your Understanding, and Problems
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.X):

X.X: Description
* worked-file PATH, textbook page num
* associated word docx (optional)
* ./LTspice folder (optional)
* keywords list `YYY ZZZ`(optional)


## Examples
6.01: Calculate the small-signal voltage gain of the most-basic NPN BJT
circuit shown in Figure 6.3.
* example/exam6_01.py, textbook page 382
* keywords: `gm`  `Vpi`  `rpi`  `voltage_gain`


## Exercises
X.X: DESCRIPTION.
* exercise/exerX_XX.py, textbook page PP
* keywords: `YYY ZZZ`


## Test Your Understanding
TYU 77.9: Per Exercise EX 1.8, Fig 1.28, determine VD and ID, using the graphical technique.
* /testunder/test1_09, textbook pg 43


## Problems
6.44_assumeIB: The transistor parameters for the circuit in Figure P6.44 are
β = 180	and	VA = inf.  Assume IB = 75μA.  (a) Find ICQ and VCEQ.
* problem/prob6_44assumeIB.py, textbook page 459
* ./LTspice/chap06/prob6_44

![Fig6_44](../../doc/mdimg/chap06_figP6_44.png)

6.44a: The transistor parameters for the circuit in Figure P6.44 are β = 180
and	VA = inf.  Assume ideal Q1.  (a) Find ICQ and VCEQ.
* problem/prob6_44a.py, textbook page 459
* ./LTspice/chap06/prob6_44
* keywords: `voltage_divider  Thevenin_voltage  Thevenin_resistance`

6.44b: The transistor parameters for the circuit in Figure P6.44 are β = 180
and	VA = inf.  Plot DC and AC load-lines using Q-point from part (a).
* problem/prob6_44b.py, textbook page 459
* ./docx/chap06/problem/chap06_prob6_44b.docx
* keywords: `voltage_divider  Thevenin_voltage  Thevenin_resistance`

![P6.44b](../../docx/png/chap06_prob6_44b_acdc_load_lines.png)

6.44cd: The transistor parameters for the circuit in Figure P6.44 are β = 180
and	VA = inf.  Assume ideal Q1.  (c) Calculate the small-signal voltage gain.
(d) Calculate Rib and Ro.
* problem/prob6_44c.py, textbook page 459
* ./docx/chap06/problem/chap06_prob6_44cd.docx
* ./LTspice/chap06/prob6_44
* keywords: `small_signal`  `voltage_gain`  `current_gain`  `rpi`  `input_resistance`
* keywords: `impedance_reflection`  `output_resistance`  `transconductance`

6.45a: The transistor parameters for the circuit in Figure P6.44 are β = 180
and	VA = inf.  Assume ideal Q1.  (a) Find ICQ and VCEQ.
* problem/prob6_45a.py, textbook page 459
* ./docx/chap06/problem/chap06_prob6_45_VCC10V.docx
* ./LTspice/chap06/prob6_45
* keywords: `voltage_divider  Thevenin_voltage  Thevenin_resistance`

6.45b: The transistor parameters for the circuit in Figure P6.45 are β = 120
and	VA = inf.  Plot DC and AC load-lines using Q-point from part (a).
* problem/prob6_45b.py, textbook page 459
* keywords: `voltage_divider  Thevenin_voltage  Thevenin_resistance`

![P6.45b](../../docx/png/chap06_prob6_45b_dc_load_line.png)

6.48: Consider the emitter-follower amplifier shown in Figure P6.48.
The transistor parameters are β = 100 and VA = 100 V. (a) Find the output
resistance Ro.
* problem/prob6_48.py, textbook page 460
* ./docx/chap06/problem/chap06_prob6_48_VCC6V.docx
* keywords: `output_resistance`

6.76a: Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(a) Determine the small-signal parameters gm, rπ, and ro for both transistors.
* problem/prob6_76a.py, textbook page 466
* keywords: `small_signal  voltage_gain  current_gain  rpi  input_resistance`
* keywords: `output_resistance  transconductance`

6.76b: Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(b) Plot the dc and ac load lines for both transistors.
* problem/prob6_76b.py, textbook page 466
* ./docx/chap06/problem/chap06_prob6_76b.docx
* keywords: `small_signal  voltage_gain  current_gain  rpi  input_resistance`
* keywords: `output_resistance  transconductance`

![P6.76b](../../docx/png/chap06_prob6_76b_Q1_acdc_load_lines.png)

6.76cde: Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(b) Plot the dc and ac load lines for both transistors.
* problem/prob6_76cde.py, textbook page 466
* ./docx/chap06/problem/chap06_prob6_76cde_LTspice.docx
* ./LTspice/chap06/prob6_76
* keywords: `small_signal`  `voltage_gain`  `current_gain`  `rpi`
* keywords: `output_resistance`  `output_voltage_swing`


# Notes
* Pg XX: 
