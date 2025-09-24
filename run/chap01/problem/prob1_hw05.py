from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
# from equations.equations import to_s_k, to_s_mA, to_s_uA
# from equations.equations import equivalent_parallel_resisitance
# from equations.equations import r1_parallel_r2
# from equations.current import current_divider
# from equations.voltage import voltage_divider


def prob1_hw05(self):
	"""
	A silicon n-channel JFET is fabricated with a channel length of 10 microns,
	a channel width of 2 microns, and a channel thickness of 3 microns.
	The channel is doped at a level of 2e+16/cm^3.
		1. Find its channel resistance.

	See also ./doc/problem/electron_mobility_n-type_Si.md

	ANS(a): (i) 1.03μA, (ii) 2.25mA.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  η  σ

	# ---- Answers -------------------
	ans:float = 0
	σ_conductivity:float = 0.0

	# ---- Givens --------------------
	μ_n:float = self.dict_electron_mobility_doping_Si_cm['light']['mobility']
	doping_concentration:float = self.dict_electron_mobility_doping_Si_cm['light']['concentration']
	calc_result:float = 0

	# ---- Assumptions ---------------

	# ---- Calcs ---------------------


	ans_string:str = """
----  ----
Electron mobility (μ_e) is a measure of how quickly electrons can move through
a semiconductor material (like silicon) when an electric field is applied.
It is defined as the average drift velocity per unit electric field.

  μ_e = (electron drift-velocity) / (Electric field) cm^2/(volt-sec)
"""
	print( ans_string )

	σ_conductivity_str:str = f"{self.qev} * {μ_n} * {doping_concentration}"
	σ_conductivity = self.qev * μ_n * doping_concentration

	print( '\n---- σ_conductivity ----' )
	print( f"σ_conductivity = {σ_conductivity_str}" )
	print( f"σ_conductivity = {σ_conductivity}" )
	print( f"μ_n = {μ_n}" )
	# print( f"type(self._dict_electron_mobility_doping_Si_cm): {type(self.dict_electron_mobility_doping_Si_cm)}" )
	# print( f"(self._dict_electron_mobility_doping_Si_cm): {(self.dict_electron_mobility_doping_Si_cm)}" )

	try:
		assert_within_percentage( calc_result, ans, assert_percentage )
		print( f"ASSERT ID = {calc_result}A is within {assert_percentage}% of accepted answer: {ans}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )


# Usage single value:
# ans_a:float = 0.518e-03   # A
# try:
# 	assert_within_percentage( iDS, ans_a, assert_percentage )
# 	print( f"ASSERT NMOS iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_a:.3e}." )
# except AssertionError as e:
# 	print( f"AssertionError {pnum}: {e}" )

# try:
# 	assert_within_percentage( iSD, ans_a, assert_percentage )
# 	print( f"ASSERT PMOS enhancement mode in saturation: iSD = {round(iSD,7)}V", end=' ' )
# 	print( f"is within {assert_percentage}% of accepted answer {ans_a}V." )
# except AssertionError as e:
# 	print( f"AssertionError {pnum}: {e}" )

# Usage with List:
# list_calc_iD:List[float] = []   #  don't forget to use list_calc_iD.append(val) to load the list!!
# ans_a_iDS:Tuple = (0.518e-03, 0.691e-03, 0.691e-03)   #
# for idx, ans_iDS in enumerate(ans_a_iDS):
# 	try:
# 		assert_within_percentage( list_calc_iDS[idx], ans_iDS, assert_percentage )
# 		print( f"ASSERT NMOS iDS = {list_calc_iDS[idx]:.3e}A is within {assert_percentage}% of accepted answer: {ans_iDS:.3e}." )
# 	except AssertionError as e:
# 		print( f"AssertionError {pnum}: {e}" )
