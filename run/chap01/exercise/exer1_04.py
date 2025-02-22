
from inspect import currentframe
import math
from typing import List
from typing import Tuple

from assertions import assertions

def exer1_04(self):
	"""	Page 21:
	Consider silicon at T = 300 K. Assume the hole concentration is given
 	by p = 1e+16*e^-(x/Lp) (per cm^3), where Lp = 1e-03cm. Calculate the hole
 	diffusion current density at (a) x = 0 and (b) x = 1e-03cm. Assume Dp = 10 cm^2/s.
	ANS  (a) 16A/cm^2  (b) 5.89A/cm^2.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	tolerance_percent:float = 2.0  # assertion accuracy
	print( '-----------------------------------------------' )


	ans_a:float = 16    # A/cm^2
	ans_b:float = 5.89  # A/cm^2

	Lp:float = 1e-03  # cm
	x_a:float = 0  # cm
	x_b:float = 1e-03
	delta_x:float = x_a - x_b
	Dp:float = 10  # hole diffusion coefficient in units of cm^2/sec

	# hole concentration per cm^3
	p_a:float = 1e+16 * math.exp( -(x_a/Lp) )
	p_b:float = 1e+16 * math.exp( -(x_b/Lp) )
	p_concentration_diff:float = p_a - p_b
	print( f"p_a = {p_a:.3e}, p_b = {p_b:.3e}, p_conc = {p_concentration_diff:.3e}")


	# hole diffusion current density at (a) x = 0cm
	Jp:float = -1.0 * self.qev * Dp * ( (p_concentration_diff)/(delta_x) )
	print( f"Jp = {Jp}" )

	# try:
	# 	assertions.assert_within_percentage( calc_result, ans_a, tolerance_percent )
	# 	print( f"CALC diode current ID = {calc_result}A is within {tolerance_percent}% of accepted answer." )
	# except AssertionError as e:
	# 	print( f"CALC AssertionError {pnum}: {e}" )

	# # hole diffusion current density at (a) x = 1e-03cm


	# try:
	# 	assertions.assert_within_percentage( calc_result, ans_b, tolerance_percent )
	# 	print( f"CALC diode current ID = {calc_result}A is within {tolerance_percent}% of accepted answer." )
	# except AssertionError as e:
	# 	print( f"CALC AssertionError {pnum}: {e}" )
