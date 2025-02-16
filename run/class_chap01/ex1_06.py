import math
from typing import List
from typing import Tuple

from assertions import assertions

def ex1_06(self):
	"""
	Consider a silicon pn junction at T = 300 K, with doping concentrations
	of Na = 1e16/cm^3 and Nd = 1e15/cm^3. Assume that ni = 1.5e10/cm^3 and let
	Cjo = 0.5pF where Cjo is the junction capacitance at zero applied voltage.
	Calculate the junction capacitance at VR = 1V and VR = 5V.
	"""
	# print( f"CALLED: {ex1_06.__name__}" )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_text}" )
	print( f"{self.problem_ans}" )

	Na:float = 1.0e16   # per cm^3
	Nd:float = 1.0e15
	ni:float = 1.5e10   # Si intrinsic doping per cm^3

	# First, calculate the pn-junction depletion-region built-in barrier voltage.
	# Vbi = Vtherm ln[ (Na*Nd) / ni^2 ]
	Vbi:float = self.vthrml0_026 * math.log( Na * Nd / ni**2 )
	print( f"ANS {pnum}: Vbi = {Vbi} = {round(Vbi, 3)}V" )
	try:
		assertions.assert_within_percentage( Vbi, 0.637, 1.0 )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	# Now, using Vbi, able to calculate the junction capacitance.
	Cjo:float = 0.5e-12  #  0.5pF

	tuple_VR:Tuple = ( 1, 5 )  # Volts
	junction_capacitance_calculated:List[float] = []

	for VR in tuple_VR:
		junction_capacitance_calculated.append( Cjo / math.sqrt( ( 1 + (VR/round(Vbi, 3)) ) ) )

	# print( f"ANS junction capacitance: {junction_capacitance_calculated}" )

	answers:Tuple = ( 0.312e-12, 0.168e-12 )
	for idx, ans in enumerate(answers):
		try:
			assertions.assert_within_percentage( junction_capacitance_calculated[idx], ans, 3.0 )
			print( f"ANS junction capacitance: {junction_capacitance_calculated[idx]}" )
		except AssertionError as e:
			print( f"AssertionError {pnum}: {e}" )
