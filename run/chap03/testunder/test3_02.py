import ast
from inspect import currentframe
# import math
from typing import Dict, List, Tuple   #, Any, Dict, Set

import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator

from assertions import assertions

def test3_02(self):
	"""Page 145:
	The NMOS devices described in Exercise TYU 3.1 have parameters
	W = 20μm, L = 0.8μm, tox = 200°A, μn = 500 cm^2/V-s, and λ = 0.
	(a) Calculate the conduction parameter Kn for each device.
	(b) Calculate the drain current for each bias condition listed in TYU 3.1.
	Page 145:
	ANS (a) Kn = 1.08mA/V2;	(b) iD = 0.518mA, 0.691mA, and 0.691mA; iD = 2.59mA, 5.83mA, and 11.1mA.
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

	# This was a hack by working backwards from the answer for Kn/Kp.  Not that
	# it was necessary, but the "missing" value for eox was calculated using
	# iteration to determine eox when Kn/Kp = 1.08mA/V^2.
	# Per page 139 of the textbook, the equation used for conduction parameter K.
	ans_Kn:float = 1.08e-03  # A/V^2

	W:float = 20e-06   # 20μm
	L:float = 0.8e-06  # 0.8μm
	un:float = 500     # inversion-layer electron-mobility

	tox_A:float = 200    # Angstrom 
	angstroms_per_meter:float = 1e+10
	tox_AM:float = tox_A / angstroms_per_meter
	um_per_meter:float = 1e+06
	tox:float = tox_AM * um_per_meter
	print( f"---tox: {tox_A}Angstrom = {tox}micro-meter" )

	# Try values for eox to approx book ans: 1.08e-03
	eox:float = 3.47e-09

	# ----------------------------------------------------------------------------
	# ----- (a) Calculate the conduction parameter Kn for each device. -----------

	conduction_parameter_params:Dict = {}
	conduction_parameter_params['channel_width'] = W
	conduction_parameter_params['channel_length'] = L
	conduction_parameter_params['carrier_mobility'] = un
	conduction_parameter_params['oxide_permittivity'] = eox
	conduction_parameter_params['oxide_thickness'] = tox
	# Function below calls calc_MOSFET_oxide_capacitance() and then uses that
	# result to calculate conduction-parameter.
	Knf:float = self.calc_MOSFET_K_conduction_parameter( **conduction_parameter_params )
	print( f"---Knf = {Knf:.5e}A/V^2 for eox = {eox}" )

	# keyword: `calc_Kn_via_iteration`
	eox_start:float = 3.0e-09
	while True:
		eox_start += 0.001e-09
		conduction_parameter_params['oxide_permittivity'] = eox_start
		# Kni:float = ( W * un * eox_start ) / ( 2 * L * tox )
		Kni:float = \
			self.calc_MOSFET_K_conduction_parameter( **conduction_parameter_params )
		if( Kni > ans_Kn ):
			print( f"---Kn per iteration = {Kni:.5e}A/V^2 for eox = {eox_start}" )
			break

	# ----------------------------------------------------------------------------
	# ---Calculate the drain current for each bias condition listed in TYU 3.1. --
	#
	# OUTPUT of TYU 3.1:
	# -----------------------------------------------
	# An n-channel enhancement-mode MOSFET has:
	#   * VTN = +1.2V
	#   * vGS = 2V
	# When vDS = 0.4V,  region of operation is 'nonsaturation/ohmic/triode'
	# When vDS = 1V,  region of operation is 'saturation'
	# When vDS = 5V,  region of operation is 'saturation'

	# An n-channel depletion-mode MOSFET has:
	#   * VTN = -1.2V
	#   * vGS = 2V
	# When vDS = 0.4V,  region of operation is 'nonsaturation/ohmic/triode'
	# When vDS = 1V,  region of operation is 'nonsaturation/ohmic/triode'
	# When vDS = 5V,  region of operation is 'saturation'


	# (b)(i) -  region of operation is 'nonsaturation/ohmic/triode'
	# calc iDS
	vGS:float = 2   # V
	VTN:float = 1.2   # V
	list_vDS:Tuple = (0.4, 1, 5)   #V
	ans_b_iDS:Tuple = (0.518e-03, 0.691e-03, 0.691e-03)   # A
	ans_b_op_mode:Tuple = ('nonsaturation/ohmic/triode', 'saturation', 'saturation' )

	idx:int = 0   # index into Tuple and List

	iDS:float = self.calc_iDS_for_NMOS_enhancement_in_nonsaturation(
		Kn_nonsat=Kni, vGS=vGS, VTN=VTN, vDS=list_vDS[idx]
	)
	# print( iDS )

	string_calc_nmos_enha:str = \
		f"CALC NMOS enhancement-mode in `{ans_b_op_mode[idx]}` operation/region: iDS"
	try:
		assertions.assert_within_percentage( iDS, ans_b_iDS[idx], assert_percentage )
		print( f"{string_calc_nmos_enha } = {iDS:.3e}A is within {assert_percentage}%", end=' ' )
		print( f"of accepted answer: {ans_b_iDS[idx]:.3e}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# (b)(ii) -  region of operation is 'saturation'
	# calc iDS
	iDS:float = self.calc_iDS_for_NMOS_enhancement_in_saturation(
		Kn_sat=Kni, vGS=vGS, VTN=VTN
	)
	idx += 1
	string_calc_nmos_enha:str = \
		f"CALC NMOS enhancement-mode in `{ans_b_op_mode[idx]}` operation/region: iDS"
	try:
		assertions.assert_within_percentage( iDS, ans_b_iDS[idx], assert_percentage )
		print( f"{string_calc_nmos_enha } = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_b_iDS[idx]:.3e}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# (b)(iii) -  region of operation is 'saturation'
	# calc iDS
	iDS:float = self.calc_iDS_for_NMOS_enhancement_in_saturation(
		Kn_sat=Kni, vGS=vGS, VTN=VTN
	)
	idx += 1
	string_calc_nmos_enha:str = \
		f"CALC NMOS enhancement-mode in `{ans_b_op_mode[idx]}` operation/region: iDS"
	try:
		assertions.assert_within_percentage( iDS, ans_b_iDS[idx], assert_percentage )
		print( f"{string_calc_nmos_enha } = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_b_iDS[idx]:.3e}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	# (b)(i) -  region of operation is 'nonsaturation/ohmic/triode'
	# calc iDS
	# vGS:float = 2   # V already initialized
	VTN:float = -1.2   # V
	# list_vDS:Tuple = (0.4, 1, 5)   # V already initialized
	ans_b_iDS:Tuple = (2.59e-03, 5.83e-03, 11.1e-03)   #
	ans_b_op_mode:Tuple = ('nonsaturation/ohmic/triode', 'nonsaturation/ohmic/triode', 'saturation' )

	idx = 0   # reset for depletion-mode
	string_calc_nmos_depl:str = \
		f"CALC NMOS depletion-mode in `{ans_b_op_mode[idx]}` operation/region: iDS"
	iDS:float = self.calc_iDS_for_NMOS_enhancement_in_nonsaturation(
		Kn_nonsat=Kni, vGS=vGS, VTN=VTN, vDS=list_vDS[0]
	)
	# print( iDS )
	try:
		assertions.assert_within_percentage( iDS, ans_b_iDS[idx], assert_percentage )
		print( f"{string_calc_nmos_depl} = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_b_iDS[idx]:.3e}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# (b)(ii) -  region of operation is 'nonsaturation/ohmic/triode'
	idx += 1
	# calc iDS
	iDS:float = self.calc_iDS_for_NMOS_enhancement_in_nonsaturation(
		Kn_nonsat=Kni, vGS=vGS, VTN=VTN, vDS=list_vDS[idx]
	)
	string_calc_nmos_depl:str = \
		f"CALC NMOS depletion-mode in `{ans_b_op_mode[idx]}` operation/region: iDS"
	try:
		assertions.assert_within_percentage( iDS, ans_b_iDS[idx], assert_percentage )
		print( f"{string_calc_nmos_depl} = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_b_iDS[idx]:.3e}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# (b)(iii) -  region of operation is 'saturation'
	# calc iDS
	iDS:float = self.calc_iDS_for_NMOS_enhancement_in_saturation(
		Kn_sat=Kni, vGS=vGS, VTN=VTN
	)
	idx += 1
	string_calc_nmos_enha:str = \
		f"CALC NMOS depletion-mode in `{ans_b_op_mode[idx]}` operation/region: iDS"
	try:
		assertions.assert_within_percentage( iDS, ans_b_iDS[idx], assert_percentage )
		print( f"{string_calc_nmos_enha } = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_b_iDS[idx]:.3e}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
