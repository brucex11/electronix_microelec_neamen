
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_01(self):
	"""Page 134:
	(a) Calculate the drain current in an NMOS transistor with parameters
	VTN = 0.4V, k'n = 120μA/V^2, W = 10μm, L = 0.8μm, and with applied
	voltages of VDS = 0.1V and (i) VGS = 0, (ii) VGS = 1V,
	(iii) VGS = 2V, and (iv) VGS = 3V.
	(b) Repeat part (a) for VDS = 4V.
	ANS(a): ID = 0  (ii) ID = 82.5μA  (iii) ID = 0.2325mA  (iv) ID = 0.3825mA
	ANS(b): ID = 0  (ii) ID = 0.27mA  (iii) ID = 1.92mA  (iv) ID = 5.07mA
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

	# Since answer = 0 for both (a) and (b) by inspection, just calculate
	# when VGS > VTN.
	ans_a_iDS:Tuple = ( 82.5e-06, 232.5e-06, 382.5e-06 )
	ans_b_iDS:Tuple = ( 0.27e-03, 1.92e-03, 5.07e-03 )
	# list_calc_iD:List[float] = []

	angstroms_per_meter:float = 1e+10
	cm_per_meter:float = 100

	# Givens for (a) and (b):
	VTN:float = 0.4   # V
	k_prime_n:float = 120e-06   # A/V^2
	W_m:float = 10e-06   # meter
	L_m:float = 0.8e-06  # m

	# Since the W/L ratio is needed, no need to convert m to cm
	W_over_L:float = W_m / L_m

	# Therefore, Kn = k'n * W/L / 2
	Kn:float = k_prime_n * W_over_L / 2
	print( f"---Kn = {Kn:.3e}A/V2" )


	vGS_given:Tuple = ( 1, 2, 3 )

	# ------- (a)(i) - (iv)
	# Since VGS < VTN, 0 < 0.4V, then current iDS = 0
	a_VDS:float = 0.1   # V
	list_calc_iD:List[float] = []   # first answer = 0A
	for VGS in vGS_given:
		ids:float = Kn * ( ( 2 * (VGS - VTN ) * a_VDS ) - a_VDS**2 )   # <=== EQUATION for iDS_in_NONsaturation
		list_calc_iD.append( ids )

	# Assert the calculations
	print( f"(a) NMOS operating in nonsaturation region")
	print( f"CALC @VGS = 0V, VDS = {a_VDS}V, then iDS = 0A by inspection." )
	for idx, iDS in enumerate(list_calc_iD):
		try:
			assertions.assert_within_percentage( iDS, ans_a_iDS[idx], assert_percentage )
			print( f"CALC @VGS = {vGS_given[idx]}V, VDS = {a_VDS}V, then iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )


	# ------- (b)(i) - (iv)
	# Since VGS < VTN, 0 < 0.4V, then current iDS = 0
	b_VDS:float = 4   # V
	list_calc_iD.clear()
	for VGS in vGS_given:
		ids:float = Kn * ( VGS - VTN )**2   # <=== EQUATION for iDS_in_NONsaturation
		list_calc_iD.append( ids )

	# Assert the calculations
	print( f"(b) NMOS operating in saturation region")
	print( f"CALC @VGS = 0V, VDS = {b_VDS}V, then iDS = 0A by inspection." )
	for idx, iDS in enumerate(list_calc_iD):
		try:
			assertions.assert_within_percentage( iDS, ans_b_iDS[idx], assert_percentage )
			print( f"CALC @VGS = {vGS_given[idx]}V, VDS = {b_VDS}V, then iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

