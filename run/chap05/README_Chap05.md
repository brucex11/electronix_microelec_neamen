# Python Project MICROELEC_NEAMEN
# Electronix Microelectronics Chap 05
Problems from the textbook: Microelectronics Circuit Analysis and Design, 4th Edition by Donald Neamen.

Figures and notes for all `./subdir` examples, exercises, and problems for this
chapter are contained in MSWord docx located in the `./docx/` folder.
Don't forget to update .gitignore to preclude .docx binaries from repository.

# Search This Document
Use the keywords below for python-code implementations, problems with plots, etc.
When applicable, each problem has keywords that reflect code in that problem.

## Available Keywords
* `Alpha  Beta  reverse_saturation_current  active_region`
* `iE_EQ_iC_plus_iB  KVL_transistor`
* `Q1_saturation_VCE_impossible`
* `Early_voltage  output_resistance`


# Examples, Exercises, Test Your Understanding, and Problems
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.XX):

X.X: Description
* worked-file PATH, textbook page XXX
* associated word docx (optional)
* LTspice folder (optional)
* keywords list `YYY ZZZ`(optional)


## Examples
5.1: Objective: Calculate the collector and emitter currents given the
base current and current gain.
* example/exam5_01.py, page 292
* keywords: `Alpha  Beta`


## Exercises
5.1: An NPN transistor is biased in the forward-active mode.
Determine β, α, and IC.
* exercise/exer5_01.py, page XXX
* keywords: `Alpha  Beta`


## Test Your Understanding
TYU 5.1: The common-emitter current gains of two transistors are β = 60
and β = 150.
Determine the common-base and common-emitter current gains.
* ./chap05/testunder/test5_01, pg 295
* keywords: `Alpha_vs_Beta  Beta_vs_Alpha`

TYU 5.2: An npn transistor is biased in the forward-active mode.
Determine IE, β, and α.
* ./chap05/testunder/test5_02, pg 295

TYU 5.3: The emitter current in a pnp transistor biased in the forward-active
mode.  Determine β, IB, and IC.
* ./chap05/testunder/test5_03, pg 295

TYU 5.4: The output resistance of a bipolar transistor is ro = 225Kohm
at IC = 0.8mA. Determine the Early voltage.
* ./chap05/testunder/test5_04, pg 297
* keywords: `Early_voltage  output_resistance`


## Problems
5.2: A bipolar transistor is biased in the forward-active mode.  Determine
Beta, Alpha, and iB.
* problem/prob5_02.py, page 352
* keywords: `Alpha  Beta`

5.5: Calculate Alpha given Beta, calc Beta given Alpha.
* problem/prob5_05.py, page 352
* keywords: `Alpha  Beta`

5.10: An npn transistor has a reverse-saturation current of IS = 5e-15A...
* problem/prob5_10.py, page 353
* keywords: `Alpha  Beta  reverse_saturation_current  active_region`

5.17(a-d): For all the transistors in Figure P5.17, β = 75.
* problem/prob5_17a.py, page 353
* problem/prob5_17b.py, page 353
* problem/prob5_17c.py, page 353
* problem/prob5_17d.py, page 353
* LTspice: ./LTspice/chap05/prob5_17/
* keywords: `iE_EQ_iC_plus_iB  KVL_transistor`

5.20(a-c): For all the transistors in Figure P5.20, β = 120.
* problem/prob5_20a.py, page 354
* problem/prob5_20b.py, page 354
* problem/prob5_20c.py, page 354
* LTspice: ./LTspice/chap05/prob5_20/
* keywords: `Q1_saturation_VCE_impossible`


# Notes
* Pg 286: Current in the transistor is due to the flow of both electrons
and holes, hence the name `bipolar`.

* Pg 287: Since the transistor has two pn junctions, `four possible bias combinations`
may be applied to the device, depending on whether a forward or reverse bias
is applied to each junction.

![img](../../doc/mdimg/chap05_BJT_quadrant_operations.png)

* Pg 287: For the transistor applied as an amplifying device, the `base–emitter`
`(B–E) junction is forward biased` and the
`base–collector` `(B–C) junction is reverse biased`, in a configuration called
the forward-active operating mode, or simply the `active region`.

* Pg 294: Table 5.1.

![Tbl5.1](../../doc/mdimg/chap05_table5.1_BJT_I-V_ACTIVE_region.png)

* Pg 297: In Figure 5.14, the nonzero slope of the curves indicates that the
output resistance ro looking into the collector is finite.  Using
Equation (5.16), ro ~= VA / IC.

![Fig5.14](../../doc/mdimg/chap05_CE_Early_voltage.png)

* Pg XXX: 
* Pg XXX: 
* Pg XXX: 
* Pg XXX: 
* Pg XXX: 
