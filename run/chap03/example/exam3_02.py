
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def exam3_02(self):
	"""Page 136:
	Objective: Determine the source-to-drain voltage vSD required to bias
	a p-channel	enhancement-mode MOSFET in the saturation region.
	Consider an enhancement-mode p-channel MOSFET for which Kp = 0.2mA/V^2,
	VTP = -0.50V, and iD = 0.50mA.
	Solution: In the saturation region, the drain current is given by
	iD = Kp(vSG + VTP)^2.
	Comment: Biasing a transistor in either the saturation or the nonsaturation
	region depends on both the gate-to-source voltage and the drain-to-source
	voltage.
	ANS vSD > vSD(sat) = vSG + VTP = 2.08e-0.5 = 1.58V.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.2
	print( '-----------------------------------------------' )

	ans:float = 1.58   # V

	# Givens
	Kp:float = 0.2e-03   # A/V^2
	VTP:float = -0.5     # V
	iD:float = 0.5e-03   # A

	# To solve fo vSG, manipulate the equation for the current iD.
	vSG:float = math.sqrt( iD / Kp ) - VTP

	# To bias this p-channel MOSFET in the saturation region, the following must
	# apply:
	vSD = vSG + VTP

	try:
		assertions.assert_within_percentage( vSD, ans, assert_percentage )
		print( f"CALC vSG in saturation = {round(vSD,2)}V", end=' ' )
		print( f"is within {assert_percentage}% of accepted answer {ans}V." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
