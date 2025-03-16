
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_13(self):
	"""Page 195:
	For a p-channel enhancement-mode MOSFET, k'p = 50μA/V^2. The device
	has drain currents of (a) ID = 0.225mA at VSG = VSD = 2V and
	(b) ID = 0.65mA at VSG = VSD = 3V.
	Determine the W/L ratio and the	value of VTP.
	ANS  VTP = -0.571V, W/L = 4.41
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
	print( '-----------------------------------------------\nSolution' )


	ans_VTP:float = -0.571   # V
	ans_WoverL:float = 4.41

	# --- Givens ---
	k_prime_p:float = 50e-06   # A/V^2
	# scenario 'a'
	IDa:float = 0.225e-03   # A
	VSGa:float = 2   # V
	VSDa:float = VSGa
	# scenario 'b'
	IDb:float = 0.65e-03   # A
	VSGb:float = 3   # V
	VSDb:float = VSGb


	ans_string:str = """
For the p-channel enhancement-mode MOSFET, both operating scenarios('a' and 'b')
have VSG = VSD; therefore, the device is operating in saturation region.
In saturation, the source-drain current ISD is calculated using Eq. 3.4b:
  iD = Kp(VSG + VTP)^2
Since Kp = 0.5k'p*(W/L), and k'p is given, take the ratio of the iD equations
to solve for VTP.
Then, using VTP, solve the W/L ratio 2 ways, once for each operating scenario
and note that the W/L ratios are practically equal.
"""
	print( ans_string )

	print( '---- calc VTP -------------------------------------------' )

	print( f"ID = 0.5 * k'p * (W/L) * (VSG + VTP)^2" )

	IDb_over_IDa:float = round( math.sqrt( IDb / IDa ), 2 )
	print( f"ratio of currents: IDb/IDa = {IDb_over_IDa}" )
	print( f"ratio of voltages: ({VSGb}+VTP)/({VSGa}+VTP)" )
	print( f"Set ratio of currents {IDb_over_IDa} == ratio of voltages: ({VSGb}+VTP)/({VSGa}+VTP)" )
	print( f"  and solve for VTP:" )
	print( f"{VSGb}+VTP = {IDb_over_IDa}({VSGa}+VTP)" )
	print( f"{VSGb}+VTP = {2*IDb_over_IDa} + {IDb_over_IDa}VTP" )
	print( f"VTP - {IDb_over_IDa}VTP = {2*IDb_over_IDa} - {VSGb}" )
	print( f"{1-IDb_over_IDa}VTP = {round(2*IDb_over_IDa-VSGb,  2)}" )
	calc_VTP:float = round(2*IDb_over_IDa-VSGb,  2) / (1-IDb_over_IDa)
	calc_VTP = round(calc_VTP, 3)
	print( f"VTP = {calc_VTP}V" )

			# ---- OUTPUT -------------------------------------------
			# ID = 0.5 * k'p * (W/L) * (VSG + VTP)^2
			# ratio of currents: IDb/IDa = 1.7
			# ratio of voltages: (3+VTP)/(2+VTP)
			# Set ratio of currents 1.7 == ratio of voltages: (3+VTP)/(2+VTP)
			#   and solve for VTP:
			# 3+VTP = 1.7(2+VTP)
			# 3+VTP = 3.4 + 1.7VTP
			# VTP - 1.7VTP = 3.4 - 3
			# -0.7VTP = 0.4
			# VTP = -0.571V
			# CALC Threshold voltage VTP = -0.571V is within 1.0% of accepted answer.

	try:
		assertions.assert_within_percentage( calc_VTP, ans_VTP, assert_percentage )
		print( f"CALC Threshold voltage VTP = {calc_VTP}V is within {assert_percentage}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( '\n---- calc W/L -------------------------------------------' )
	print( f"Solve for W/L using the ID current equation in saturation:")
	print( f"        IDa = ( k'p / 2 )(W/L)( VSGa + VTP )^2")
	print( f"   {IDa} = ( {k_prime_p} / 2 )(W/L)( {VSGa} + {calc_VTP })^2")
	print( 'Solve for W/L:')

	calc_WoverL:float = ( IDa * 2 ) / k_prime_p / ( VSGa + calc_VTP )**2
	print( f" >> W/L = {calc_WoverL}" )


	print( f"        IDb = ( k'p / 2 )(W/L)( VSGb + VTP )^2")
	print( f"   {IDb} = ( {k_prime_p} / 2 )(W/L)( {VSGb} + {calc_VTP })^2")
	print( 'Solve for W/L:')

	calc_WoverL = ( IDb * 2 ) / k_prime_p / ( VSGb + calc_VTP )**2
	print( f" >> W/L = {calc_WoverL}" )

	try:
		assertions.assert_within_percentage( calc_WoverL, ans_WoverL, assert_percentage )
		print( f"CALC W/L ratio = {calc_WoverL} is within {assert_percentage}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )
