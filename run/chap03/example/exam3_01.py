
from inspect import currentframe
import math
from typing import Dict, List, Tuple  # Any, Set

from assertions import assertions

def exam3_01(self):
	"""Page 134:
	Objective: Calculate the current in an n-channel MOSFET.
	Consider an n-channel enhancement-mode MOSFET with the following parameters:
	VTN = 0.4V, W = 20μm, L = 0.8μm, μn = 650 cm^2/V-s, tox = 200Å (oxide-thickness),
	and (oxide permittivity) εox = (3.9)(8.85e-14)F/cm. Determine the current
	when the transistor is biased in the saturation region for (a) vGS = 0.8V
	and (b) vGS = 1.6V.
	Comment: The current capability of a transistor can be increased by increasing
	the conduction parameter. For a given fabrication technology, Kn is adjusted
	by varying the transistor width W."
	ANS (a) iD = 0.224 mA  (b) iD = 2.02mA.
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


	ans_a:float = 0.224e-03   # A
	ans_b:float = 2.02e-03    # A
	ans_Kn:float = 1.4e-03    # A/V^2
	tuple_ans_iD:Tuple = ( ans_a, ans_b )

	tuple_vGS_control:Tuple = ( 0.8, 1.6 )
	list_calc_iD:List[float] = []

	# For each of the two iD calculations, the conduction-param Kn is calculated
	# and used for each iD calc.
	# Also, calculate the oxide-capacitance Cox per unit area (since εox and tox are given).
	# See pg 134, units for Kn = A/V^2.
	eox:float =  (3.9)*(8.85e-14)   # (oxide permittivity) εox = F/cm
	tox_A:float = 200    # Angstrom 
	angstroms_per_meter:float = 1e+10
	tox_AM:float = tox_A / angstroms_per_meter
	cm_per_meter:float = 100
	tox:float = tox_AM * cm_per_meter
	# print( f"---tox = {tox}" )
	Cox:float = eox / tox   # oxide-capacitance per unit area
	print( f"---Cox = {Cox}" )

	W:float = 20e-04   # centi-meters cm
	L:float = 0.8e-04  # cm
	un:float = 650     # inversion-layer electron-mobility

	abc:float = self.calc_MOSFET_oxide_capacitance( eox=eox, tox=tox )

	Kn:float = ( W * un * eox ) / ( 2 * L * tox )   # A/V^2
	print( f"LOCAL Kn: {Kn}" )

	# Test the object function call; build the kwargs Dict object
	conduction_parameter_params:Dict = {}
	conduction_parameter_params['channel_width'] = W
	conduction_parameter_params['channel_length'] = L
	conduction_parameter_params['carrier_mobility'] = un
	conduction_parameter_params['oxide_permittivity'] = eox
	conduction_parameter_params['oxide_thickness'] = tox
	Knf:float = self.calc_MOSFET_K_conduction_parameter( **conduction_parameter_params )
	print( f"LOCAL Knf: {Knf}" )

	try:
		assertions.assert_within_percentage( Kn, ans_Kn, assert_percentage )
		print( f"CALC Kn conduction parameter = {round(Kn,5)}A/V^2", end=' ' )
		print( f"is within {assert_percentage}% of accepted answer {ans_Kn}A/V^2." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# Now calculate the current in saturation region for given thresh voltage VTN.
	VTN:float = 0.4
	for vgs in tuple_vGS_control:
		id:float = Kn * ( vgs - VTN ) **2
		list_calc_iD.append( id )

	print( f"id SAT: {list_calc_iD}" )

	for idx, id in enumerate(tuple_ans_iD):
		try:
			assertions.assert_within_percentage( list_calc_iD[idx], id, assert_percentage )
			print( f"CALC saturation current iD = {list_calc_iD[idx]}A is within {assert_percentage}% of accepted answer." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )
