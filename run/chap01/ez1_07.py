
from inspect import currentframe
import math
from typing import List
from typing import Tuple

from scipy.constants import Boltzmann

from assertions import assertions

def ez1_07(self):
	"""Page 29:
	A silicon pn junction at T = 300 K has a reverse-saturation current of
	IS = 2e-14 A.  Determine the required forward-bias voltage VD to produce
	a current of (i) ID = 50μA and (ii) ID = 1mA. (b) Repeat part (a)
	for	IS = 2e-12A.
	ANS (a) (i) 0.563V, (ii) 0.641V; (b) (i) 0.443V, (ii) 0.521V.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	tolerance_percent:float = 1.0  # assertion accuracy
	print( '-----------------------------------------------' )

	ans_ai:float =  0.563
	ans_aii:float = 0.641
	ans_bi:float =  0.443
	ans_bii:float = 0.521

	print( '----- (a)(i) (ii) -----' )
	IS:float = 2e-14
	ID:float = 50e-06

	VD:float = self.calc_diode_ideal_voltage( IS, ID )

	try:
		assertions.assert_within_percentage( VD, ans_ai, tolerance_percent )
		print( f"CALC diode voltage VD = {round(VD,3)}V is within {tolerance_percent}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	ID:float = 1e-03

	VD:float = self.calc_diode_ideal_voltage( IS, ID )

	try:
		assertions.assert_within_percentage( VD, ans_aii, tolerance_percent )
		print( f"CALC diode voltage VD = {round(VD,3)}V is within {tolerance_percent}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( '----- (b)(i) (ii) -----' )

	IS:float = 2e-12
	ID:float = 50e-06

	VD:float = self.calc_diode_ideal_voltage( IS, ID )

	try:
		assertions.assert_within_percentage( VD, ans_bi, tolerance_percent )
		print( f"CALC diode voltage VD = {round(VD,3)}V is within {tolerance_percent}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	ID:float = 1e-03

	VD:float = self.calc_diode_ideal_voltage( IS, ID )

	try:
		assertions.assert_within_percentage( VD, ans_bii, tolerance_percent )
		print( f"CALC diode voltage VD = {round(VD,3)}V is within {tolerance_percent}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
