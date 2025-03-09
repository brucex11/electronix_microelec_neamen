
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
	assert_percentage:float = 2.0
	print( '-----------------------------------------------' )

	# nonsaturation: iDS = Kn_nonsat * ( 2 * (vGS - VTN) * vDS - vDS**2 )
	# saturation: iDS = Kn_sat * (vGS - VTN)**2

	ans_string1:str = """The conduction parameter `(Kn | Kp)` is a function
 of both `electrical`and `geometric parameters`:
  - the `electrical` oxide capacitance and carrier mobility are essentially
    constants for a given fabrication technology, and
  - the `geometry`, or width-to-length ratio W/L, is a variable in the MOSFET's
    structure/footprint."""
	print( ans_string1 )
	ans_string2:str = """It thereby follows that Kn is independent of any MOSFET's
mode, enhancement or depletion, and operating-region, nonsaturation or saturation.
Therefore, calculate Kn in saturation region for each operation-region, then
calculate the corresponding vDS in nonsaturation-region of operation.
Note that 'nonsaturation' is also known as 'ohmic' or 'triode'."""
	print( ans_string2 )

	# --- (a) --------------------------------------------------------------------
	iDS_a:float = 0.5e-03        # A
	VGS_minus_VTN_a:float = 0.6  # V

	iDS_b:float = 1e-03        # A
	VGS_minus_VTN_b:float = 1  # V

	print( f"Kn in saturation = iDS / (vGS - VTN)**2")

	# Kn_a:float = iDS_a / VGS_minus_VTN_a**2
	Kn_a:float = iDS_a / (VGS_minus_VTN_a * VGS_minus_VTN_a)
	# print( f"Kn_a in saturation = {Kn_a:.5e}A/V^2")
	print( f"Kn_a in saturation = {Kn_a}A/V^2")
	# return


	# Find when eq > 0 for constant vDS
	vDS_const:float = 2
	VTN_const:float = 1
	vGS_range:List[float] = [round(0 + i * 0.01, 2) for i in range(320)]  # 56 values from -0.2 to 0.9
	print( f"vGS_range: {vGS_range}" )
	# return
	for vGS in vGS_range:
		expr:float = ( 2 * (vGS - VTN_const) * vDS_const - vDS_const**2 )
		if( expr > 0 ):
			print( f"expr > 0 when vGS = {vGS} and VTN = {VTN_const}" )
			print( f"when (vGS - VTN) = {vGS - VTN_const} and vDS = {vDS_const}" )
			break


	vDS_const:float = 2
	VTN_const:float = 2
	for vGS in vGS_range:
		expr:float = ( 2 * (vGS - VTN_const) * vDS_const - vDS_const**2 )
		if( expr > 0 ):
			print( f"expr > 0 when vGS = {vGS} and VTN = {VTN_const}" )
			print( f"when (vGS - VTN) = {vGS - VTN_const} and vDS = {vDS_const}" )
			break

	return
	print( f"Calculate vDS when iDS = 0.5mA and (VGS - VTN) = 0.6V in ohmic-region.")


	# --- (b) --------------------------------------------------------------------

	# Kn_b:float = iDS_b / VGS_minus_VTN_b**2
	# print( f"Kn in saturation = {Kn_b:.5e}A/V^2")


	# # --- quadradic equation -----------------------------------------------------
	# a:float = 1.0
	# b:float = 2.0 * VGS_minus_VTN_a
	# print( f"b = {b}" )
	# b_sq:float = b**2
	# print( f"b_sq = {b_sq}" )
	# c:float = iDS_a / Kn_a
	# print( f"c = iDS_a / Kn_a = {c}" )
	# print( f"a * c = {a*c}" )
	# four_a_c:float = 4.0 * (a * c)
	# print( f"four_a_c = {four_a_c}" )
	# # sqrt_a:float = sqrt( b_sq - (4 * a * c) )
	# sqrt_a:float = sqrt( b_sq - four_a_c )
	# print( f"sqrt_a = {sqrt_a}" )
	# x_p:float = -b + sqrt( b**2 - (4.0 * a * c) ) / ( 2.0 * a )
	# print( f"x_p = {x_p}" )
	# x_n:float = -b - sqrt( b**2 - (4.0 * a * c) ) / ( 2.0 * a )
	# print( f"x_n = {x_n}" )
	# # check result by calculating iDS in nonsat
	# iDS = Kn_a * ( (2 * (VGS_minus_VTN_a) * x_p) - x_p**2 )
	# print( f"iDS = {iDS}" )




	# # b:float = 2 * VGS_minus_VTN_b
	# b:float = 2 * VGS_minus_VTN_b
	# c:float = iDS_b / Kn_b
	# sqrt_b:float = sqrt( b**2 - (4 * a * c) )
	# print( f"sqrt_b = {sqrt_b}" )
	# x_p:float = -b + sqrt( b**2 - (4 * a * c) ) / ( 2 * a )
	# print( f"x_p = {x_p}" )
	# x_n:float = -b - sqrt( b**2 - (4 * a * c) ) / ( 2 * a )
	# print( f"x_n = {x_n}" )
