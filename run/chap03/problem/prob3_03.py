
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_03(self):
	"""Page 194:
	The transistor characteristics iD versus vDS for an NMOS device are shown
	in Figure P3.3. (a) Is this an enhancement-mode or depletion-mode device?
	(b) Determine the values for Kn and VTN. (c) Determine iD(sat) for
	vGS = 3.5V and vGS = 4.5V
	ANS (a) enhancement-mode  (b) Kn(avg) = 0.064mA/V^2, VTN = 1.5V
	(ci) iDS(sat) = 0.256mA  (cii) iDS(sat) = 0.576mA.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.5
	print( '-----------------------------------------------' )

	# nonsaturation: iDS = Kn_nonsat * ( 2 * (vGS - VTN) * vDS - vDS**2 )
	# saturation: iDS = Kn_sat * (vGS - VTN)**2
	# VTN = vGS - vDS(sat)

	ans_a:str = 'enhancement-mode'
	ans_VTN = 1.5   # V
	ans_Kn:float = 0.064e-03   # A/V^2
	tuple_ans_iDS_sat:Tuple = ( 0.256e-03, 0.576e-03 )

	print( '\n---- (a) -------------------------------------------' )
	ans_string:str = f"Since VGS is positive, device is {ans_a}."
	print( ans_string )

	print( '\n---- (b) -------------------------------------------' )
	ans_string:str = """The threshold voltage VTN can be determined when vDS reaches saturation
by the relationship: VTN = vGS - vDS(sat).
Per the graph, vDS reaches saturation where the slope of the VGS curve goes to zero (ideally).
"""
	print( ans_string )

	print( f"By inspection, for each of the VGS curves, the slope goes to zero at approx {ans_VTN}V.\n" )

	ans_string:str = """Also by inspection per the graph, the values for IDS at saturation-points:
iDS ~= 0.03mA @ VDS = 1v
iDS ~= 0.15mA @ VDS = 2v
iDS ~= 0.40mA @ VDS = 3v
iDS ~= 0.80mA @ VDS = 4v.
"""
	print( ans_string )

	ans_string:str = """To calculate Kn, use the ideal equation for iDS in saturation for
the three highest VGS curves per the graph:  Kn_sat = iDS / (vGS - VTN)**2.
Kn is then the average of these three values.
"""
	print( ans_string )
	print( f"VTN ~= {ans_VTN}V." )
	# Generate the List to take the 4 calculations.
	list_calc_KN_sat:List[float] = []

	# To use a loop, generate the Tuples that take the VGS and iDS values,
	# but leave out the lowest.
	tuple_VGS_per_graph:Tuple = ( 3, 4, 5 )   # V
	tuple_iDS_per_graph:Tuple = ( 0.15e-03, 0.4e-03, 0.8e-03 )   # V

	for idx, vGS in enumerate(tuple_VGS_per_graph):
		Kn:float = tuple_iDS_per_graph[idx] / ( vGS - ans_VTN )**2
		list_calc_KN_sat.append( Kn )
		# print( Kn )

	# Take the average Kn.
	avg_Kn:float = sum(list_calc_KN_sat) / len(list_calc_KN_sat)
	# print( f"Kn(avg) = {avg_Kn}A/V^2")
	try:
		assertions.assert_within_percentage( avg_Kn, ans_Kn, assert_percentage )
		print( f"CALC Kn(avg) = {avg_Kn:.3e}A/V^2 is within {assert_percentage}% of accepted answer: {ans_Kn:.3e}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( '\n---- (c) -------------------------------------------' )
	ans_string:str = """Finally, calculate iDS(sat) using the ideal equation for iDS
in saturation:
    iDS = Kn(avg) * (vGS - VTN)**2."""
	print( ans_string )

	vGS_curve:Tuple = ( 3.5, 4.5 )
	list_calc_iDS_sat:List[float] = []
	for vGS in vGS_curve:
		list_calc_iDS_sat.append( avg_Kn * (vGS - ans_VTN)**2 )
	# print( list_calc_iDS_sat )

	for idx, ans_iDS in enumerate(tuple_ans_iDS_sat):
		try:
			assertions.assert_within_percentage( list_calc_iDS_sat[idx], ans_iDS, assert_percentage )
			print( f"CALC iDS(sat) = {list_calc_iDS_sat[idx]:.3e}A is within {assert_percentage}% of accepted answer: {ans_iDS:.3e}." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

	print( '--- END ---' )
