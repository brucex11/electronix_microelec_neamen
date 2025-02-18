
import inspect
import math
from typing import List
from typing import Tuple

from assertions import assertions

def ex1_04(self):
	"""Page 20
	Objective: Calculate the diffusion current density for a given semiconductor.
	Consider silicon at T = 300 K. Assume the electron concentration varies linearly
	from n1 = 1e+12/cm^3 to n2 = 1e+16/cm^3 over the distance from x1 = 0 to x2 = 300 μm.
	Assume Dn = 35cm^2/s.
	Comment: Diffusion current densities on the order of a few hundred amperes per
	square centimeter can also be generated in a semiconductor.
	ANS:  Jn = 187A/cm^2
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	tolerance_percent:float = 2.0
	ans:float = 187  # A/cm^2
	Dn:float = 35  # electron diffusion coefficient in units of cm^2/sec
	n1:float = 1e+12
	n2:float = 1e+16
	x1:float = 0
	x2:float = 300e-06  # μm

	Jn:float = self.qev * Dn * ( (n1-n2)/(x1-x2) )

	try:
		assertions.assert_within_percentage( Jn, ans, tolerance_percent )
		print( f"CALC Jn diffusion current = {round(Jn,2)}A/cm^2 within {tolerance_percent}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
