from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.equations import current_divider


def casc_cc(self):
	"""
	LTspice support for python:
	./docx/labs/CE-CC_Cascade/LTspice/simulation/CC/casc_cc*.asc
	./docx/labs/CE-CC_Cascade/LTspice/simulation/small_signal/casc_cc__small-signal.asc

	Main report:
	./docx/labs/CE-CC_Cascade/LAB_CE-CC_Cascade.docx

	LTspice complete schematic:
	./docx/labs/CE-CC_Cascade/LTspice/simulation/CECC/assigned_schematic_sim0X.asc
	The '0X' is the Simulation number; the nums increment for changes to keep
	track-of.
	05 - looks pretty good

	This started with the LTspice simulation of the entire circuit that was
	close but not perfect.  See files above 'py_assigned*.asc' above.
	These are used as a starting-point for Q-point currents.
	When the LTspice .op directive/analysis-command is run, it generates
	a .log file (in same dir as .asc) that contains all currents.

	This is the 'process'.
	"""
	# fcn_name:str = currentframe().f_code.co_name
	# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Simulation num 01 .op log ----
	# Circuit: * C:\SourceCode\GitHub\electronix\microelec_neamen\docx\labs\CE-CC_Cascade\LTspice\simulation\py_assigned_schematic_sim01.asc
	# Start Time: Sat Apr 12 14:20:51 2025
	#
	# USE q2 values
	#
	# Name:       q1          q2
	# Model:    2n3904      2n3904
	# Ib:       1.34e-06    7.62e-05
	sim_IBQ2:float = 7.62e-05
	# Ic:       4.07e-04    2.29e-02
	sim_ICQ2:float = 2.29e-02
	# Vbe:      6.32e-01    7.40e-01
	sim_VBE2:float = 0.74
	# Vbc:     -1.68e+00   -5.52e+00
	# Vce:      2.31e+00    6.26e+00
	# BetaDC:   3.05e+02    3.00e+02
	sim_BetaDC:float = 300
	# Gm:       1.57e-02    8.42e-01
	# Rpi:      1.94e+04    3.39e+02
	sim_rpi2:float = 339
	# Rx:       2.00e+01    2.00e+01
	# Ro:       2.50e+05    4.61e+03
	sim_Ro:float = 4610
	# Cbe:      1.78e-11    3.08e-10
	# Cbc:      2.72e-12    1.99e-12
	# Cjs:      0.00e+00    0.00e+00
	# BetaAC:   3.04e+02    2.85e+02
	sim_BetaAC:float = 285
	# Cbx:      0.00e+00    0.00e+00
	# Ft:       1.22e+08    4.32e+08

	# --- Simulation num 01 .op Operating Point pop-up ---
	# V(vcq1):	 3.0419	 voltage
	# V(vbq1):	 1.36688	 voltage
	# V(veq1):	 0.735341	 voltage
	# V(vcc_vcq2):	 12	 voltage
	# V(vbq2):	 6.48211	 voltage
	# V(veq2):	 5.74222	 voltage
	# V(vo):	 2.23946e-14	 voltage
	# V(vs):	 0	 voltage
	# V(p001):	 1.36688e-14	 voltage
	# Ic(Q1):	 0.000407186	 device_current
	# Ib(Q1):	 1.33626e-06	 device_current
	# Ie(Q1):	 -0.000408523	 device_current
	# Ic(Q2):	 0.0228926	 device_current
	# Ib(Q2):	 7.62413e-05	 device_current
	# sim_IBQ2:float = 7.62413e-05
	# Ie(Q2):	 -0.0229689	 device_current
	sim_IEQ2:float = 0.023
	# I(Cby):	 3.44021e-17	 device_current
	# I(Cout):	 -5.74222e-17	 device_current
	# I(Cin):	 1.36688e-17	 device_current
	# I(R11):	 9.24619e-05	 device_current
	# I(R21):	 9.11256e-05	 device_current
	# I(R12):	 0.000110358	 device_current
	# I(R22):	 3.41164e-05	 device_current
	# I(Rc):	 0.000407186	 device_current
	# I(Re1):	 0.000408523	 device_current
	# I(Re2):	 0.0229689	 device_current
	# I(Rl):	 5.74222e-17	 device_current
	# I(Rs):	 1.36688e-17	 device_current
	# I(Vcc):	 -0.0235026	 device_current
	# I(Vs):	 1.36688e-17	 device_current


	# ---- Specs ---------------------
	RL:float = 390        # Ω
	RE2:float = 250       # Ω
	R12:float = 50e+03    # Ω
	R22:float = 190e+03   # Ω
	Rs:float = 1e+03      # Ω

	# ---- Calcs ---------------------
	ass_IEQ2:float = sim_IEQ2   # A
	ass_BetaDC:float = sim_BetaDC
	ass_RE2:float = 250

	IBQ2:float = ass_IEQ2 / ( 1 + ass_BetaDC )
	IBQ2 = round(IBQ2,6)
	ICQ2:float = ass_IEQ2 - IBQ2
	ICQ2 = round(ICQ2,3)

	rpi2:float = self._vthrml0_026 / IBQ2
	rpi2 = round(rpi2, 2)



	ans_string:str = f"""
For the overall circuit the following specifications were chosen:
  * VCC = 12V because output voltage requirement is 5Vp-p
  * Q1 and Q2 are 2N3904 because it is a general-purpose BJT, and
    it happens to be the very-first transistor data-sheet listed
    in the Motorola Small-Signal Transistor Data book.

Start with following assumptions for the CC-stage:
  * Q2 emitter current = {to_s_mA(ass_IEQ2,3)}
  * Q2 BetaDC = {ass_BetaDC}
  * RE2 = {ass_RE2}ohm.

Calc IBQ2 and ICQ2.
  IBQ2 = IEQ2 / (1 + Beta)
       = {ass_IEQ2} / (1 + {ass_BetaDC})
       = {to_s_mA(IBQ2,5)}.
  ICQ2 = IEQ2 + IBQ2
       = {ass_IEQ2} + {IBQ2}
       = {ICQ2}A.

Calc rpi2 based on Q-point IBQ2:
  rpi2 = VT / IBQ2
       = {rpi2}ohm.
"""
	print( ans_string )


	print( '---- Calc small-signal values ----', end='' )
	# Input resistance
	RE_p_RL:float = r1_parallel_r2( ass_RE2, RL)
	RE_eff:float = (1 + ass_BetaDC) * RE_p_RL   # emitter-node effective AC resistance
	Rib2:float = rpi2 + RE_eff
	Rib2 = round(Rib2, 0)

	Ri2:float = equivalent_parallel_resisitance( list_rs=[R12, R22, Rib2] )
	Ri2 = round(Ri2,0)

	# Output resistance Rs=0
	Rz2:float = rpi2 / (1 + ass_BetaDC)  # inv-Z-reflection
	Ro2_Rs0:float = equivalent_parallel_resisitance( list_rs=[Rz2, RE2, RL] )
	Ro2_Rs0 = round(Ro2_Rs0,2)
	# Output resistance Rs non-zero
	# Rz2:float = rpi2 / (1 + ass_BetaDC)  # inv-Z-reflection
	Rsinp:float = equivalent_parallel_resisitance( list_rs=[R12, R22, Rs] )
	Rz22:float = ((rpi2 + Rsinp) / (1 + ass_BetaDC))  # inv-Z-reflection
	Ro2:float = equivalent_parallel_resisitance( list_rs=[Rz22, RE2, RL] )
	Ro2 = round(Ro2,2)

	ans_string:str = f"""
Calc Q2 input impedance RiB:
  Rib2 = rpi2 + (1 + Beta) * (RE||RL)
       = {rpi2} + (1 + {ass_BetaDC}) * ({RE_p_RL})
       = {rpi2} + {RE_eff}
       = {Rib2}ohm.

Calc circuit input impedance Ri2:
  Ri2 = (R12||R22||Rib2)
      = ({R12}||{R22}||{Rib2})
      = {Ri2}ohm.
.

Q2 output resistance Ro.
There are two ways to make this determination:
  1) Input source resistance, call it Rs, is zero (ie ideal)
  2) Input source resistance Rs is real.


Use inverse-impedance-reflection (looking \"back\" toward source)
that applies dividing-by the (1+Beta) factor.

Also, little ro is considered ideal, ie, infinite.
1)
  Ro2 = (rpi2 / (1 + BetaDC))||RE2||ro||RL  Eq 6.74
      = (rpi2 / (1 + BetaDC))||RE2||RL
      = ({rpi2} / (1 + {ass_BetaDC}))||{RE2}||{RL}
  Ro2 = {Ro2_Rs0}ohm.

2)
  Ro2 = ( (rpi2 + (R12||R22||Rs) / (1 + BetaDC) )||RE2||ro||RL  Eq 6.79
      = ( (rpi2 + (R12||R22||Rs) / (1 + BetaDC) )||RE2||RL
      = ( ({rpi2} + ({R12}||{R22}||{Rs}) / (1 + {ass_BetaDC}) )||{RE2}||{RL}
      = {round(Rz22,3)}||{RE2}||{RL}
  Ro2 = {Ro2}ohm.

"""
	print( ans_string )

	try:
		assert_within_percentage( IBQ2, sim_IBQ2, assert_percentage )
		print( f"ASSERT IBQ2 = {IBQ2}A is within {assert_percentage}% of accepted answer: {sim_IBQ2}A." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )
	try:
		assert_within_percentage( ICQ2, sim_ICQ2, assert_percentage )
		print( f"ASSERT ICQ2 = {ICQ2}A is within {assert_percentage}% of accepted answer: {sim_ICQ2}A." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )
	try:
		assert_within_percentage( rpi2, sim_rpi2, assert_percentage )
		print( f"ASSERT rpi2 = {rpi2}ohm is within {assert_percentage}% of accepted answer: {sim_rpi2}ohm." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )
