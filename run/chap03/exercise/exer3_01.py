
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def exer3_01(self):
	"""Page 134:
	An NMOS transistor with VTN = 1V has a drain current iD = 0.8mA
	when vGS = 3V and vDS = 4.5V.  Calculate the drain current when:
	a) vGS = 2V, vDS = 4.5V; and (b) vGS = 3V, vDS = 1V.

	Solution: Solve for Kn conduction parameter per equations 3.2a and 3.2b,
	then solve for drain current given vGS and vDS.

	Assuming operation in nonsaturation region where vDS < vDS(sat), use eq 3.2a.
	Assuming operation in saturation region where vGS > VTN, use eq 3.2b.

	ANS  (a) 0.2 mA  (b) 0.6 mA.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 1.0
	print( '-----------------------------------------------' )

	ans_a:float = 0.2e-03   # A
	ans_b:float = 0.6e-03   # A

	VTN:float = 1.0     # V
	iDS_given:float = 0.8e-03   # 0.8mA
	vGS_given:float = 3     # V
	vDS_given:float = 4.5   # V

	# Calc Kn in NONsaturation region
	# See page 132
	# iD_nonsat:float = Kn * ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 )
	Kn_nonsat:float = iDS_given / ( ( 2 * (vGS_given - VTN ) * vDS_given ) - vDS_given**2 )
	print( f"CALC Kn_nonsat = {Kn_nonsat}" )

	# Calc Kn in saturation region
	# See page 133
	# iDS_sat:float = Kn_sat * ( vGS - VTN )**2
	Kn_sat:float = iDS_given /  ( vGS_given - VTN )**2
	print( f"CALC Kn_sat = {Kn_sat}" )

	# Note that Kn for nonsaturation region is NEGATIVE, and for all intents
	# and purposes, this cannot be.
	# However, Kn is POSITIVE for saturation region of operation, so we'll take
	# that value of Kn to calculate iDS for the other situations (a) and (b).


	# ------ a) vGS = 2V, vDS = 4.5V ---------------------------------------------
	# Since vDS is fairly high and the "only" difference between the given
	# parameters and the "new ones" is that the gate voltage is reduced by 1V.
	# Therefore, assume that the operating region is "still" saturation and so
	# use the equation for iDS in saturation region.
	vGS:float = 2
	vDS:float = 4.5
	iDS_sat:float = Kn_sat * ( vGS - VTN )**2   # <=== EQUATION for iDS_in_saturation
	# print( f"CALC iDS_sat = {iDS_sat}" )

	try:
		assertions.assert_within_percentage( iDS_sat, ans_a, assert_percentage )
		print( f"CALC NMOS iDS = {iDS_sat}A is within {assert_percentage}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# ------ b) vGS = 3V, vDS = 1V -----------------------------------------------
	# Here, vGS is the same as the given, but now vDS has been reduced to a quite-
	# low value = 1v; therefore, assume operating in NONsaturation region and
	# use the corresponding equation.
	vGS:float = 3
	vDS:float = 1
	iDS_nonsat:float = Kn_sat * ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 )   # <=== EQUATION for iDS_in_NONsaturation
	# print( f"CALC iD_nonsat = {iDS_nonsat}" )

	try:
		assertions.assert_within_percentage( iDS_nonsat, ans_b, assert_percentage )
		print( f"CALC NMOS iDS = {round(iDS_nonsat, 4)}A is within {assert_percentage}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
