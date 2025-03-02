
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def exam3_01(self):
	"""Page 134:
	Objective: Calculate the current in an n-channel MOSFET.
	Consider an n-channel enhancement-mode MOSFET with the following parameters:
	VT N = 0.4V, W = 20μm, L = 0.8μm, μn = 650 cm^2/V-s, tox = 200Å,
	and (oxide permittivity) εox = (3.9)(8.85e-14)F/cm. Determine the current
	when the transistor is biased in the saturation region for (a) vGS = 0.8V
	and (b) vGS = 1.6V.
	Comment: The current capability of a transistor can be increased by increasing
	the conduction parameter. For a given fabrication technology, Kn is adjusted
	by varying the transistor width W."
	ANS (a) iD = 0.224 mA  (b) iD = 2.02mA.
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
	print( '-----------------------------------------------' )


	ans_a:float = 0.224e-03   # A
	ans_b:float = 2.02e-03    # A

	calc_result:float = 0

	try:
		assertions.assert_within_percentage( calc_result, ans_a, assert_percentage )
		print( f"CALC current iD = {calc_result}A is within {assert_percentage}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )



	try:
		assertions.assert_within_percentage( calc_result, ans_b, assert_percentage )
		print( f"CALC current iD = {calc_result}A is within {assert_percentage}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
