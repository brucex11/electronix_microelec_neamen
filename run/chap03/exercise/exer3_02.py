
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def exer3_02(self):
	"""Page 137:
	A PMOS device with VTP = -1.2V has a drain current iD = 0.5mA
	when vSG = 3V and vSD = 5V. Calculate the drain current when (a) vSG = 2V,
	vSD = 3V; and (b) vSG = 5V, vSD = 2V.
	ANS (a) 0.0986mA  (b) 1.72mA.
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

	ans_a:float = 0.0986e-03   # A
	ans_b:float = 1.72e-03     # A

	# Givens
	VTP:float = -1.2     # V
	iDS_given:float = 0.5e-03  # A
	vSG_given:float = 3        # V
	vSD_given:float = 5        # V

	# Calc Kp_in_NONsaturation region
	# See page 136
	# iD_nonsat:float = Kp * ( ( 2 * (vSG + VTN ) * vSD ) - vSD**2 )
	Kp_nonsat:float = iDS_given / ( ( 2 * (vSG_given + VTP ) * vSD_given ) - vSD_given**2 )
	print( f"CALC Kp_nonsat = {Kp_nonsat}" )

	# Calc Kp_in_saturation region
	# See page 136
	# iDS_sat:float = Kp_sat * ( vGS - VTN )**2
	Kp_sat:float = iDS_given /  ( vSG_given + VTP )**2
	print( f"CALC Kp_sat = {Kp_sat}" )

	# --- (a) --------------------------------------------------------------------
	vSG_a:float = 2   # V
	vSD_a:float = 3   # V

	iSD_a:float = self.pmos_enhancement_iDS_saturation(
		Kp_sat=Kp_sat, vSG=vSG_a, VTP=VTP
	)
	try:
		assertions.assert_within_percentage( iSD_a, ans_a, assert_percentage )
		print( f"CALC PMOS enhancement mode in saturation: iSD = {round(iSD_a,7)}V", end=' ' )
		print( f"is within {assert_percentage}% of accepted answer {ans_a}V." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# --- (b) --------------------------------------------------------------------
	vSG_b:float = 5   # V
	vSD_b:float = 2   # V

	iSD_b:float = self.pmos_enhancement_iDS_nonsaturation(
		Kp_nonsat=Kp_sat, vSG=vSG_b, VTP=VTP, vSD=vSD_b
	)
	try:
		assertions.assert_within_percentage( iSD_b, ans_b, assert_percentage )
		print( f"CALC PMOS enhancement mode in non-saturation: iSD = {round(iSD_b,5)}V", end=' ' )
		print( f"is within {assert_percentage}% of accepted answer {ans_b}V." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
