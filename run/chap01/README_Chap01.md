# Python Project MICROELEC_NEAMEN
# Electronix Microelectronics Chap 01
Problems from the textbook: Microelectronics Circuit Analysis and Design, 4th Edition by Donald Neamen.

Figures and notes for all `./subdir` examples, exercises, and problems for this
chapter are contained in MSWord docx located in the `./docx/` folder.
Don't forget to update .gitignore to preclude .docx binaries from repository.

# Search This Document
Use the keywords below for python-code implementations, problems with plots, etc.
When applicable, each problem has keywords that reflect code in that problem.

## Available Keywords
* `iteration`
* `KVL`
* `line_plot  Q_point twin_y_axes`
* `list_comprehension  list_range_for_rationals`
* `scatter_plot  highlight_point_diff_color  plot_horiz_vert_line`
* `semilog_plot`

# Examples, Exercises, Test Your Understanding, and Problems
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.X):

X.X: Description
* worked-file PATH, textbook page num
* associated word docx (optional)
* LTspice folder (optional)
* keywords list `YYY ZZZ`(optional)


## Examples
Exam 1.1: Calculate the intrinsic carrier concentration at T = 300 K for `Si, Ge, GaAs`.
* example/exam1_01.py, textbook page 13 (also covers exer 1.1)

Exam 1.2: Calculate the majority and minority carrier concentrations.
* example/exam1_02, textbook pg 16

Exam 1.3: Calculate the drift current density for a given semiconductor.
* example/exam1_03, textbook pg 18

Exam 1.4: Calculate the drift current density for a given semiconductor.
* example/exam1_04, textbook pg 20

Exam 1.5: Calculate the built-in potential barrier of a pn junction.
* example/exam1_05, textbook pg 24, SEE ALSO p1.19

Exam 1.6: Calculate the pn junction capacitance at VR = 1V and VR = 5V.
* example/exam1_06, textbook pg 26

Exam 1.7: Determine the current in a pn junction diode given voltage VD across it.
* example/exam1_07, textbook pg 28
* example/docx/exam1_07.docx
* keywords: `scatter_plot  line_plot list_comprehension  highlight_point_diff_color`
* keywords: `semilog_plot  plot_horiz_vert_line list_range_for_rationals`

Exam 1.8: Use iteration to determine the diode voltage and current for simple circuit.
Also, use graphic analysis by plotting the `load line`.
* example/exam1_08, textbook pg 36
* ./run/chap01/example/docx/exam1_08.docx
* keywords: `iteration  KVL  list_range_for_rationals  load_line  Q_point`

Exam 1.9 SKIP: Simple diode circuit piecewise linear model.

Exam 1.10 LtSpice: Simple diode circuit piecewise linear model.
* ./LTspice/chap01/exam1_10/   textbook pg 41
* chap01/example/exam1_10, textbook pg 41
* ./docx/example/chap01_example1_10.docx
* ./run/chap01/example/docx/exam1_10.docx
* of note: image (exam1_10.png) of twin-plot saved manually from 'show window' task-bar
* keywords: `twin_y_axes  list_range_for_rationals`


## Exercises
Exer 1.1: See example 1.1.

Exer 1.2: Calculate the majority and minority carrier concentrations.
* exercise/exer1_02, textbook pg 16

Exer 1.3: Determine the resistivity (reciprocal of conductivity) of the material GaAs.
* exercise/exer1_03, textbook pg 19

Exer 1.4: Calculate the hole diffusion current density of Si at (a) x = 0 and
(b) x = 1e-03cm.
* exercise/exer1_04, textbook pg 21

Exer 1.5: Calculate Vbi for GaAs and Ge pn junction with specified donor and acceptor
doping concentrations.
* exercise/exer1_05, textbook pg 25

Exer 1.6: Find the zero-biased pn junction capacitance Cj0.
* exercise/exer1_06, textbook pg 26

Exer 1.7: Determine the required forward-bias voltage to produce a given current of ID.
* exercise/exer1_07, textbook pg 29

Exer 1.8: Use iteration to determine the diode voltage and current for simple circuit.
* exercise/exer1_08, textbook pg 37

Exer 1.9 SKIP: Simple diode circuit piecewise linear model.

Exer 1.10 LtSpice: Simple diode circuit piecewise linear model.
* ./LTspice/chap01/exer1_10/   textbook pg 42
* ./docx/exercise/chap01_exercise1_10.docx
* chap01/exercise/exer1_10, textbook pg 41
* keywords: `twin_y_axes  list_range_for_rationals`


## Test Your Understanding
TYU 1.9: Per Exercise EX 1.8, Fig 1.28, determine VD and ID, using the graphical technique.
* ./chap01/testunder/test1_09, textbook pg 43


## Problems
Prob 1.1: Calculate the intrinsic carrier concentration in Si and GaAs.
* problem/prob1_01, textbook pg 57

Prob 1.2: Determine the maximum allowable temperature of a pn junction by
programatically iterating through	a range of temps, then assert that the
intrinsic concentration n_i meets the requirement	less than 1e+12 and 1e+09 per cm^3.
* problem/prob1_02, textbook pg 57
* keywords: `iteration`

Prob 1.3: Calculate the intrinsic carrier concentration in Si and Ge at various temps K.
* problem/prob1_03, textbook pg 57

Prob 1.5: Find the concentration of electrons and holes. Is the semiconductor n-type
or p-type?
* problem/prob1_05, textbook pg 58

Prob 1.19: Determine the built-in potential barrier Vbi in Si and GaAs pn junction.
* problem/prob1_19a, textbook pg 59
* problem/prob1_19b, textbook pg 59

Prob 1.27: Determine the diode current for various diode voltages per the
reverse-saturation current IS.
* problem/prob1_27_plot, textbook pg 60

Prob 1.29: Determine the reverse-bias saturation current for pn junction diode given
an emission coefficient.
* problem/prob1_29, textbook pg 60


# Notes
* Pg 12: In order to break the covalent bond, the valence electron must gain a minimum energy,
  `Eg`, called the bandgap energy. The electrons that gain this minimum energy now exist in the
  conduction band and are said to be free electrons.
* Pg 12: In a <i>semiconductor</i>, the bandgap energy `Eg` is on the order of 1 eV.
* Pg 13: An `intrinsic semiconductor` is a single-crystal semiconductor material with
  no other types of atoms within the crystal.  In an `intrinsic semiconductor`,
  the densities of electrons and holes are equal.
* Pg 13: The `intrinsic concentration ni` is a parameter that appears often in the current–voltage
  equations for semiconductor devices.
* Pg 14: A semiconductor that contains `donor` impurity atoms is called an n-type semiconductor
  (for the negatively charged electrons) and has a preponderance of electrons compared to holes.
* Pg 15 A semiconductor that contains `acceptor` impurity atoms is called a p-type semiconductor
  (for the positively charged holes created) and has a preponderance of holes compared to electrons.
* Pg 15 A fundamental relationship between the electron and hole concentrations in a
  semiconductor in thermal equilibrium is given by:
  - `no * po = ni^2`
  - where `no` is the thermal equilibrium concentration of free electrons, `po` is the thermal
    equilibrium concentration of holes, and `ni` is the intrinsic carrier concentration.
* Pg 15 If the `acceptor` concentration `Na` is much larger than the intrinsic concentration, then
  - `po ~= Na`
	* Pg 15 If the `donor` concentration `Nd` is much larger than the intrinsic concentration, then
  - `no ~= Nd`
* Pg 16 In an n-type semiconductor, <i>electrons</i> are called the `majority carrier` because
  they far outnumber the holes, which are termed the `minority carrier`.
* Pg 16 In a p-type semiconductor, <i>holes</i> are called the `majority carrier` because
  they far outnumber the electrons, which are termed the `minority carrier`.
* Pg 17 The two basic processes which cause electrons and holes to move in a semiconductor are:
  - (a) drift, which is the movement caused by electric fields, and
	- (b) diffusion, which is the flow caused by variations in the concentration, that is, concentration gradients.
	- See EX 1.3
* Pg 17 An electric field `E` applied in one direction produces a force on the electrons in the `opposite` direction,
  because of the electrons’ negative charge.
	- The drift current in an `n-type` semiconductor is in the `same direction` as the applied electric field.
	- The drift current in an `p-type` semiconductor is (also) in the `same direction` as the applied electric field.
* Pg 17 The electron drift produces a drift current density Jn (A/cm2) given by
  - `Jn = −e*n*vdn = −en(−μnE) = +enμnE`
* Pg 18 <b>Being able to control the conductivity of a semiconductor by selective doping is what enables fabrication
  of the variety of electronic devices that are available.</b>
* Pg 19 `Carrier drift velocities` are linear functions of the applied electric field for relatively small electric fields.
* Pg 19 `Drift velocity saturation` is when drift velocities reach a maximum value of approximately `1e+07cm/s`.
Any further increase in electric field will not produce an increase in `drift velocity`.
* Pg 19 In the diffusion process, particles flow from a region of high concentration to a region
of lower concentration.
  - See EX 1.4
* Pg 21 The mobility values in the drift current equations and the diffusion coefficient values in the diffusion current
equations are not independent quantities. They are related by the `Einstein relation: kT/e ~= 0.026V` at 300K (room temp).
* Pg 21 The total current density is the sum of the drift and diffusion components. Fortunately, in most cases only one
component dominates the current at any one time in a given region of a semiconductor.
* Pg 21 When a voltage is applied to, or a current exists in, a semiconductor device, both an electron and a hole are
produced, thus generating an electron–hole pair. These additional electrons and holes are called `excess electrons`
and `excess holes`.
* Pg 22 `n = no + δn` and `p = po + δp`
         where no and po are the thermal equilibrium concentrations of electrons and holes, and δn and δp are the
         `excess electron` and `excess hole` concentrations.
* Pg 22 The mean time over which an excess electron and hole exist before recombination is called the
`excess carrier lifetime`.
* Pg 23 The real power of semiconductor electronics occurs when p- and n-regions are `directly adjacent` to each other,
forming a pn junction. In most integrated circuit applications, the entire semiconductor material is a `single crystal`,
with one region doped to be p-type and the adjacent region doped to be n-type.

* Pg 23 The `[p|n]` interface at x = 0 is called the `metallurgical junction`.
               ^
              x=0
* Pg 23 A large density gradient in both the hole and electron concentrations occurs across the `metallurgical junction`.
Initially, holes diffuse into the n-region, and electrons diffuse into the p-region.
* Pg 24  See Fig 1.12. With no voltage applied to the pn junction, the diffusion of holes and electrons must eventually
cease.
* Pg 24 The positively charged region and the negatively charged region comprise the `space-charge region`, or
`depletion region`, of the pn junction, in which there are essentially no mobile electrons or holes.
* Pg 24 Because of the electric field in the space-charge region, there is a potential difference across that region
[Figure 1.12(b)].  This potential difference is called the built-in potential barrier, or `built-in voltage`, for which
there is an equation.
* Pg 25 With an increasing `reverse-bias` voltage, space-charge `width` also increases. This effect is shown in Figure 1.14.
* Pg 26 `junction capacitance` is generated across the pn junction when a reverse-bias voltage is applied.
* Pg 27 `Forward bias` voltage must always be less than the `built-in voltage`.
* Pg 28 The pn junction, with `nonlinear rectifying current characteristics`, is called a pn junction diode.
* Pg 30 Since both IS and VT are functions of temperature, diode characteristics also vary with `temperature`.
* Pg 30 The actual (vs ideal) reverse-bias diode current, as a general rule, doubles for every 10°C rise in temperature.
* Pg 31 The most common breakdown mechanism is called `avalanche breakdown`, which occurs when carriers crossing the
space charge region gain sufficient kinetic energy from the high electric field to be able to break covalent bonds
during a collision process.
* Pg 32 A second breakdown mechanism, `Zener breakdown`, is a result of tunneling of carriers across the junction.
This effect is prominent at very high doping concentrations and results in breakdown voltages less than 5V.
* Pg 34 For an `ideal diode` (as opposed to a diode with ideal I–V characteristics), when a reverse-bias voltage
is applied, the current through the diode is zero; when current through the diode is greater than zero, the voltage
across the diode is zero.
* Pg 37 For the simple diode circuit Figure 1.28, the equation ID = (VPS - VD) / R is referred to as the circuit `load line`,
and is usually plotted on a graph with the current ID as the vertical axis and the voltage VD as the horizontal axis.
* Pg 3
* Pg 3
* Pg 3
* Pg 3
* Pg 3

