from inspect import currentframe
# import math
from typing import List  #, Tuple   #, Any, Dict, Set

from assertions import assertions

def exer1_08(self):
	"""Page 37:
	Use iteration to determine the diode voltage and current for the circuit
	per Figure 1.28.  Consider a diode with a given reverse-saturation current
	of IS = 1e-13A.  VPS = V; R=4kΩ.
	Comment: Once the diode voltage is known, the current can also be determined
	from the ideal diode equation. However, dividing the voltage difference across
	a resistor by the resistance is usually easier, and this approach is used
	extensively in the analysis of diode and transistor circuits.
	Page 37:
	ANS VD = 0.535 V, ID = 0.866mA.

	See example/doc/exam1_08.docx (because this exercise is essentially the same).

	Solution:
	Use KVL to write the voltage equation around the loop:
		VPS = ID*R + VD
	Then, solve above for ID.

	Note, the diode I-V characteristic == Ideal Diode Equation
			see Chap01.calc_diode_ideal_current( ID, VD ).
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

	ans_VD:float = 0.535     # V
	ans_ID:float = 0.866e-03  # A

	# Write the KVL equation:
	# VPS = R * (ideal diode eq) + VD
	VPS:float = 4     # V
	R:float = 4000    # Ω
	IS:float = 1e-12  # A
	VD_iter_val:List[float] = [round(0.52 + i * 0.001, 3) for i in range(24)]  # 24 values from 0.6 to 0.623
	print( f"VD_iter_val: {VD_iter_val}V" )

	# Iteratively solve for VPS using range of values for VD.
	VD_per_iteration:float = -1
	for VDi in VD_iter_val:
		ID_ideal:float = self.calc_diode_ideal_current( IS=IS, VD=VDi )
		VPS_iter_val:float = R * ID_ideal + VDi
		print( f"VPS_iter_val = {VPS_iter_val}V" )

		# check the iteral value against VPS
		try:
			assertions.assert_within_percentage( VPS, VPS_iter_val, assert_percentage )
			print( f"CALC VPS = {round(VPS_iter_val,3)}V when VD = {VDi}V, and ID = {ID_ideal}A" )
			VD_per_iteration = VDi
			break
		except AssertionError:
			pass

	# At this point, the ideal ID when the assertion was satified IS the loop current.
	try:
		assertions.assert_within_percentage( ID_ideal, ans_ID, assert_percentage )
		print( f"CALC using diode ideal-ID value = {ID_ideal}A within {assert_percentage}% of accepted answer: {ans_ID}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# However, the dividing-the-voltage-difference-across-a-resistor approach
	# is used extensively in the analysis of diode and transistor circuits.

	ID_final:float = ( VPS - VD_per_iteration ) / R
	try:
		assertions.assert_within_percentage( ID_final, ans_ID, assert_percentage )
		print( f"CALC (VPS-VD)/R = ID = {ID_ideal}A within {assert_percentage}% of accepted answer: {ans_ID}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
