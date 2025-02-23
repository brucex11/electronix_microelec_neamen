# Python Project MICROELEC_NEAMEN
# Electronix Microelectronics
Problems from the textbook: Microelectronics Circuit Analysis and Design, 4th Edition by Donald Neamen.

Figures and notes for all `./subdir` examples, exercises, and problems for this
chapter are contained in MSWord docx located in the `./subdir/doc` folder.
Don't forget to update .gitignore to preclude .docx binaries from repository.

## Examples
1.1: Calculate the intrinsic carrier concentration at T = 300 K for:
* `Si, Ge, GaAs`
* example/exam1_01.py, textbook page 13 (also covers exer 1.1)

1.2: Calculate the majority and minority carrier concentrations.
* example/exam1_02, textbook pg 16

1.3: Calculate the drift current density for a given semiconductor.
* example/exam1_03, textbook pg 18

1.4: Calculate the drift current density for a given semiconductor.
* example/exam1_04, textbook pg 20

1.5: Calculate the built-in potential barrier of a pn junction.
* example/exam1_05, textbook pg 24, SEE ALSO p1.19

1.6: Calculate the pn junction capacitance at VR = 1V and VR = 5V.
* example/exam1_06, textbook pg 26

1.7: Determine the current in a pn junction diode given voltage VD across it.
* example/exam1_07, textbook pg 28
* example/doc/exam1_07.docx

## Exercises
1.1: See example 1.1.

1.2: Calculate the majority and minority carrier concentrations.
* exercise/exer1_02, textbook pg 16

1.3: Determine the resistivity (reciprocal of conductivity) of the material GaAs.
* exercise/exer1_03, textbook pg 19

1.4: Calculate the hole diffusion current density of Si at (a) x = 0 and
(b) x = 1e-03cm.
* exercise/exer1_04, textbook pg 21

1.5: Calculate Vbi for GaAs and Ge pn junction with specified donor and acceptor
doping concentrations.
* exercise/exer1_05, textbook pg 25

1.6: Find the zero-biased pn junction capacitance Cj0.
* exercise/exer1_06, textbook pg 26

1.7: Determine the required forward-bias voltage to produce a given current of ID.
* exercise/exer1_07, textbook pg 29

## Problems
1.1: Calculate the intrinsic carrier concentration in Si and GaAs.
* problem/prob1_01, textbook pg 57

1.2: Determine the maximum allowable temperature of a pn junction by
programatically iterating through	a range of temps, then assert that the
intrinsic concentration n_i meets the requirement	less than 1e+12 and 1e+09 per cm^3.
* problem/prob1_02, textbook pg 57

1.3: Calculate the intrinsic carrier concentration in Si and Ge at various temps K.
* problem/prob1_03, textbook pg 57

1.5: Find the concentration of electrons and holes. Is the semiconductor n-type
or p-type?
* problem/prob1_05, textbook pg 58

1.19: Determine the built-in potential barrier Vbi in Si and GaAs pn junction.
* problem/prob1_19a, textbook pg 59
* problem/prob1_19b, textbook pg 59

1.27: Determine the diode current for various diode voltages per the
reverse-saturation current IS.
* problem/prob1_27_plot, textbook pg 60

1.29: Determine the reverse-bias saturation current for pn junction diode given
an emission coefficient.
* problem/prob1_29, textbook pg 60


## Notes
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
equations are not independent quantities. They are related by the Einstein relation.
* Pg 


