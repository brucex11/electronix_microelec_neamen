from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def test5_04(self):
	"""Page 297:
	The output resistance of a bipolar transistor is ro = 225Kohm at IC = 0.8mA.
	(a) Determine the Early voltage.
	(b) Using the results of part (a), find ro at (i) IC = 0.08mA and (ii) IC = 8mA.
	ANS: (a) VA = 180V  (b)(i) ro = 2.25Mohm  (ii)  ro = 22.5Kohm.
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

	# ---- Answers -------------------
	ans_a:float = 180   # V
	ans_bi:float = 2.25e+06    # ohm
	ans_bii:float = 22.5e+03   # ohm

	# ---- Givens --------------------
	IC:float = 0.8e-03  # A
	ro:float = 225e+03     # ohm
	IC_bi:float = 0.08e-03  # A
	IC_bii:float = 8e-03   # A

	ans_string:str = f"""
In Figure 5.14, the nonzero slope of the curves indicates that the
output resistance ro looking into the collector is finite.  Using
Equation (5.16), ro ~= VA / IC.
"""
	print( ans_string )

	print( '---- (a) -------------------------------------------' )
	# ---- Calcs ---------------------
	calc_Early_voltage:float = ro * IC

	try:
		assertions.assert_within_percentage( calc_Early_voltage, ans_a, assert_percentage )
		print( f"CALC Early voltage = {calc_Early_voltage}V is within {assert_percentage}% of accepted answer: {ans_a}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	print( '\n---- (b) -------------------------------------------' )
	# ---- Calcs ---------------------
	calc_ro_bi:float = calc_Early_voltage / IC_bi
	calc_ro_bii:float = calc_Early_voltage / IC_bii

	try:
		assertions.assert_within_percentage( calc_ro_bi, ans_bi, assert_percentage )
		print( f"CALC output resistance ro = {calc_ro_bi}ohm is within {assert_percentage}% of accepted answer: {ans_bi}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( calc_ro_bii, ans_bii, assert_percentage )
		print( f"CALC output resistance ro = {calc_ro_bii}ohm is within {assert_percentage}% of accepted answer: {ans_bii}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )
