from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage

def prob6_48(self):
	"""Page 460:
	Consider the emitter-follower amplifier shown in Figure P6.48. The transistor
	parameters are β = 100 and VA = 100V. (a) Find the output resistance
	Ro. (b) Determine the small-signal voltage gain for (i) RL = 500 and
	(ii) RL = 5k.
	ANS(a):  ro = 50.5kΩ, Ro = 112Ω
	ANS(b):  (i) 0.974, (ii) 0.997
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

	#  α   β   Ω   μ   λ   γ   ξ   ω

	# ---- Answers -------------------
	ans_ro:float = 50.5e+03   # Ω
	ans_Ro:float = 112        # Ω

	# ---- Givens --------------------
	Beta = 100
	VA:float = 100   # V

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------
	calc_Ro:float = ans_Ro

	ans_string:str = f"""
REPLACE THIS TEXT.
"""
	print( ans_string )

	print( '\n---- (a) -------------------------------------------' )

	try:
		assert_within_percentage( calc_Ro, ans_Ro, assert_percentage )
		print( f"ASSERT Ro = {calc_Ro}ohm is within {assert_percentage}% of accepted answer: {ans_Ro}ohm." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )
