import inspect
import math
from typing import List
from typing import Tuple

from assertions import assertions

def ez1_06(self):
	"""Page 26:
	A silicon pn junction at T = 300 K is doped at Nd = 1e+16/cm^3 and
	Na = 1e+17/cm^3. The junction capacitance is to be Cj = 0.8pF when a reverse
	bias voltage of VR = 5V is applied.
	Find the zero-biased junction capacitance Cj0.
	ANS: 2.21pF
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )

	ans:float = 2.21e-12  # pF
	Na:float = 1.0e16   # per cm^3
	Nd:float = 1.0e15
	ni:float = 1.5e10   # Si intrinsic doping per cm^3
	Vr:float = 5   # V

	# First, calculate the pn-junction depletion-region built-in barrier voltage.
	# Vbi = Vtherm ln[ (Na*Nd) / ni^2 ]
	Vbi:float = self.vthrml0_026 * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( Vbi, 0.637, 1.0 )
		print( f"CALC {pnum}: Vbi = {round(Vbi, 3)}V" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# Now, using Vbi, able to calculate the zero-biased junction capacitance.
	Cj:float = 0.8e-12  # 0.8pF

	Cj0:float = Cj * math.sqrt( ( 1 + (Vr/round(Vbi, 3)) ) )

	try:
		assertions.assert_within_percentage( Cj0, ans, 8.0 )
		print( f"CALC {pnum}: Cj0 = {Cj0:.3e}F." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
