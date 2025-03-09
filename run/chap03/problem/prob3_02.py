
from inspect import currentframe
from math import sqrt
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_02(self):
	"""Page 194:
	The current in an NMOS transistor is (a) 0.5mA when VGS - VTN = 0.6V and
	(b) 1.0mA when VGS - VTN = 1.0V. The device is operating in the nonsaturation
	region. Determine VDS and Kn.
	ANS none
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.5
	print( '-----------------------------------------------' )

	ans_vDS:float = 0.4   # V
	ans_Kn:float  = 1.56e-03   # A/V^2

	# nonsaturation: iDS = Kn_nonsat * ( 2 * (vGS - VTN) * vDS - vDS**2 )
	# saturation: iDS = Kn_sat * (vGS - VTN)**2

	ans_string:str = """The conduction parameter `(Kn | Kp)` is a function
 of both `electrical`and `geometric parameters`:
  - the `electrical` oxide capacitance and carrier mobility are essentially
    constants for a given fabrication technology, and
  - the `geometry`, or width-to-length ratio W/L, is a variable in the MOSFET's
    structure/footprint."""
	print( ans_string )
	ans_string:str = """Given that the device is operating in nonsaturation-region,
use the ideal current-voltage characteristics Eq 3.2a to solve for Kn and vDS:
    iDS = Kn * ( 2 * (vGS - VTN) * vDS - vDS**2 )
Also, since operation is nonsaturation, vDS should be in range of 0 - 1V.
Note that 'nonsaturation' is also known as 'ohmic' or 'triode'.\n"""
	print( ans_string )
	ans_string:str = """Given two operating points iDS and (vGS-VTN), use the ratio
of two iDS-nonsaturation equations such that Kn cancels and values for
iDS can be substituted leaving only vDS to be solved.\n"""
	print( ans_string )

	ans_string:str = """  Ratio:
    0.5 = Kn[2(0.6)vDS - vDS^2)]
    ---------------------------
    1.0 = Kn[2(1.0)vDS - vDS^2)]

The Kn's cancal and the above reduces algebraically:
    vDS - 0.5vDS^2 = 1.2vDS - vDS^2 , divide both sides by vDS
    1   - 0.5vDS   = 1.2    - vDS
"""
	print( ans_string )

	iDS_a:float = 0.5e-03        # A
	VGS_minus_VTN_a:float = 0.6  # V

	iDS_b:float = 1e-03        # A
	VGS_minus_VTN_b:float = 1  # V

	vDS:float = ( 1.2 - 1) / 0.5
	print( f"Finally, vDS = {round(vDS,2)}V.\n" )
	print( f"Solve for Kn in nonsaturation: Kn = iDS / ( 2 * (vGS - VTN) * vDS - vDS**2 )" )
	print( f"  when iDS = {iDS_a}A and (vGS-VTN) = {VGS_minus_VTN_a}V:" )
	Kn:float = iDS_a / ( 2 * (VGS_minus_VTN_a) * vDS - vDS**2 )
	print( f"  Kn = {Kn:.3e}A/V^2" )

	print( f"  when iDS = {iDS_b}A and (vGS-VTN) = {VGS_minus_VTN_b}V:" )
	Kn:float = iDS_b / ( 2 * (VGS_minus_VTN_b) * vDS - vDS**2 )
	print( f"  Kn = {Kn:.3e}A/V^2\n" )

	try:
		assertions.assert_within_percentage( vDS, ans_vDS, assert_percentage )
		print( f"CALC NMOS vDS = {round(vDS,2)}V is within {assert_percentage}% of accepted answer: {ans_vDS}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( Kn, ans_Kn, assert_percentage )
		print( f"CALC NMOS iDS = {Kn:.3e}A/V^2 is within {assert_percentage}% of accepted answer: {ans_Kn:.3e}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
