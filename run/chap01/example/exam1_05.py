
from inspect import currentframe
import math
from typing import List
from typing import Tuple

from assertions import assertions

def exam1_05(self):
	"""Page 24:
	Objective: Calculate the built-in potential barrier of a pn junction.
	Consider a Si pn junction at T = 300 K, doped at Na = 1e+16/cm^3 in the
	p-region and Nd = 1e+17/cm^3 in the n-region.
	Comment: Because of the log function, the magnitude of Vbi is not a strong
	function of the doping concentrations. Therefore, the value of Vbi for Si
	pn junctions is usually within 0.1 to 0.2 V of this calculated value.
	SEE ALSO p1.19."
	ANS:  0.757V.
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

	ans:float = 0.757  # V

	Na:float = 1e+16		# /cm^3 net acceptor concentration in the p-region
	Nd:float = 1e+17		# /cm^3 net donor concentration in the n-region


	# The natural logarithm is only defined for positive numbers (x > 0).
	# math.log(x) computes ln(x) for positive values of x.
	Vbi = self.vthrml0_026 * math.log( Na * Nd / self.ni_Si_300K**2 )
	try:
		assertions.assert_within_percentage( Vbi, ans, 1.0 )
		print( f"CALC {pnum} for Si, Vbi = {round(Vbi, 3)}V is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
