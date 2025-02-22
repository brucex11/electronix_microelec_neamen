# import inspect
from inspect import currentframe
import math
import os
# from typing import List
# from typing import Tuple

from assertions import assertions

def exer2_01(self):
	"""Page 71:
	Objective: Determine the currents and voltages in a half-wave rectifier circuit.
	Consider the circuit shown in Figure 2.4. Assume VB = 4.5V, R = 250Ω, and
	Vγ = 0.6 V. Also assume vS(t) = 12sinωt . Determine the peak diode current,
	maximum reverse-bias diode voltage, and the fraction of the cycle over which
	the diode is conducting.
	ANS peak diode current = 27.6mA, max reverse-bias diode voltage = 16.5V, %-time = 36%.
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

	ans_id_peak:float = 114e-03  # mA
	ans_max_rev_voltage:float = 36   # V
	ans_percent_cycle:float = 36

	VB:float = 4.5
	R:float  = 250

	Vgamma:float = 0.6
	vS_t_peak:float = 24   # V

	# --- iD-peak ---
	iD_peak:float = ( vS_t_peak - VB - Vgamma ) / R
	try:
		assertions.assert_within_percentage( iD_peak, ans_id_peak, assert_percentage )
		print( f"CALC {pnum} iD-peak V = {iD_peak:.3e}A is within {assert_percentage}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# --- max reverse-bias diode voltage ---
	vR_max:float = vS_t_peak + VB
	try:
		assertions.assert_within_percentage( vR_max, ans_max_rev_voltage, assert_percentage )
		print( f"CALC {pnum} VR-max reverse diode voltage = {vR_max}V is within {assert_percentage}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# --- fraction of the cycle over which the diode is conducting ---
	# B:float = self.dict_semicond_mat_consts['GaAs']['B']
	# ni:float =  B * ( temp ** (3/2) ) \
	# 		* math.exp( -1.0 * self.dict_semicond_mat_consts['GaAs']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )
	# print( f"CALC {pnum} for GaAs @{temp}K, ni = {ni:.3e}/cm^3." )
	# print( 'These values were added to the Chap01 ctor.' )
