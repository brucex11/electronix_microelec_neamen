
from inspect import currentframe

from assertions import assertions

def prob3_45(self):
	"""Page 200:
	Consider the circuit in Figure P3.44. The transistor parameters for M1 are
	VTN = 0.4V and k'n = 120μA/V^2, and for M2 are VTN = -0.6V,
	k'n = 120uA/V^2, and W/L = 1. Determine the W/L ratio of M1 such that
	vO = 0.025V when vI = 3V.
	Page 1340:
	ANS: (W/L)M1 = 2.78
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.4
	print( '-----------------------------------------------' )

	VDD:float = 5        # V
	VTN_M1:float = 0.4   # V
	k_prime_n_M1:float = 120e-06   # A/V^2
	VTN_M2:float = -0.6   # V
	k_prime_n_M2:float = 120e-06   # A/V^2
	WoverL_M2:float = 1

	vo_spec:float = 0.025   # V
	VG_M1_spec:float = 3    # VI (per the schematic), V

	ans_WoverL_M1:float = 2.78

	ans_string:str = """
M2 is manufactured as depletion-mode, M1 as enhancement-mode.
Both are n-channel.
Based on the specs (givens), gate, source, and drain voltages are known for
both MOSFETs M1 and M2.
It follows that the operation-region for both can be determined.
M2: VGS = 0, VDS = VDD - vo
"""
	print( ans_string )
	print( '---- (M1 voltages) ------------------------------------------------' )
	VG_M1:float = VG_M1_spec   # V
	VS_M1:float = 0   # V
	VD_M1:float = vo_spec
	calc_VGS_M1:float = VG_M1 - VS_M1
	calc_VDS_M1:float = VD_M1 - VS_M1
	calc_VDS_M1_sat:float = calc_VGS_M1 - VTN_M1
	print( f"M1: VGS = {calc_VGS_M1}V, VDS = {calc_VDS_M1}V, and VG > VD." )
	print( f"    Since VDS(sat) = VGS - VTN = {calc_VDS_M1_sat}V, then VDS << VDS(sat)," )
	print(  '    hence operation-region is ohmic/triode/nonsaturation.' )

	print( '---- (M2 voltages) ------------------------------------------------' )
	VG_M2:float = vo_spec   # V
	VS_M2:float = vo_spec   # V
	VD_M2:float = VDD
	calc_VGS_M2:float = VG_M2 - VS_M2
	calc_VDS_M2:float = VD_M2 - VS_M2
	calc_VDS_M2_sat:float = calc_VGS_M2 - VTN_M2
	print( f"M2: VGS = {calc_VGS_M2}V, VDS = {calc_VDS_M2}V, and VG < VD." )
	print( f"    Since VDS(sat) = VGS - VTN = {calc_VDS_M2_sat}V, then VDS >> VDS(sat)," )
	print(  '    hence operation-region is saturation.' )

	print( '---- (M1 ID == M2 ID - in series) ---------------------------------' )

	ans_string = """
With M1 and M2 in series, the current through their channels must be equal.
Use the ideal I-V current equations:
 - ID(ohmic) for M1
 - ID(saturation) for M2

IDM1 in ohmic-region = IDM2 in saturation-region:
IDM1(ohmic) = Kn[ 2(VGS - VTN)VDS - VDS^2 ]
IDM2(sat)   = Kn( VGS - VTN )^2

Since Kn is known for both, use the Kn-version with (W/L) and solve for M1's (W/L).
"""
	print( ans_string )

	calc_ID_M2:float = ( k_prime_n_M2 / 2 ) * WoverL_M2 * ( calc_VGS_M2 - VTN_M2 )**2
	print( f"Calculate M2 drain current:\nIDM2(sat) = {calc_ID_M2}A" )

	print( f"Then set the ohmic-ID equation to IDM1(sat) and solve for (W/L)M1:" )
	# print( f"calc_VGS_M1 = {calc_VGS_M1}")
	# print( f"VTN_M1 = {VTN_M1}")
	# print( f"calc_VDS_M1 = {calc_VDS_M1}")
	# print( f"ABC = {2 * ( calc_VGS_M1 - VTN_M1) * calc_VDS_M1 - calc_VDS_M1**2 }")
	calc_WoverL_M1:float = ( 2 * calc_ID_M2 / k_prime_n_M1 ) / ( 2 * ( calc_VGS_M1 - VTN_M1) * calc_VDS_M1 - calc_VDS_M1**2 )
	calc_WoverL_M1 = round(calc_WoverL_M1,3)
	print( f"(W/L)M1 = {calc_WoverL_M1} ")

	try:
		assertions.assert_within_percentage( calc_WoverL_M1, ans_WoverL_M1, assert_percentage )
		print( f"CALC (W/L)M1 = {calc_WoverL_M1} is within {assert_percentage}% of accepted answer {ans_WoverL_M1}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
