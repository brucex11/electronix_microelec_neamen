from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def exam5_04(self):
	"""Page 305:
	Objective: Calculate the base, collector, and emitter currents and the
	C-E voltage for a PNP common-emitter circuit.  Calc RC and transistor power
	dissipation.
	For the circuit shown in Figure 5.22(a), the parameters are: VBB = 1.5V,
	RB = 580kΩ, VEE = 5V, VEB(on) = 0.6V, and β = 100.

	Comment: In this case, the difference between V+ and VBB is greater than the
	transistor turn-on voltage, or (V+ - VBB) > VEB(on). Also, because VEC > VEB(on),
	the pnp bipolar transistor is biased in the forward-active mode.
	Discussion: In this example, we used an emitter-base turn-on voltage of
	VEB(on) = 0.6V, whereas previously we used a value of 0.7V. The turn-on voltage
	is an approximation and the actual base-emitter voltage
	will depend on the type of transistor used and the current level.
	In most situations, a value of 0.6V or 0.7V will make only minor differences.
	However, 0.7V is most common.
	
	ANS: IB = 5μA, IC = 0.5mA, IE = 0.505mA, RC = 5k, PT ~= ??mW
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.5
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   ξ   ω

	# ---- Answers -------------------
	ans_IB:float = 5e-06  # A
	ans_IC:float = 0.5e-03   # A
	ans_IE:float = 0.505e-03  # A
	ans_RC:float = 5e+03    # Ω
	ans_PT:float = 1.253e-03  # W

	# ---- Givens --------------------
	VBB:float =  1.5   # V
	VEE:float =  5  # V
	VEB_on:float =  0.6  # V
	RB:float = 580e+03  # Ω
	Beta:float = 100

	# ---- Calcs ---------------------
	assume_VEC:float = 2.5   # V

	calc_IB:float = (VEE - VEB_on - VBB) / RB

	calc_IC:float = Beta * calc_IB
	calc_IC = round(calc_IC,4)

	calc_IE:float = ( 1 + Beta ) * calc_IB
	calc_IE = round(calc_IE,6)

	calc_RC:float = (VEE - assume_VEC) / calc_IC

	calc_PEB = calc_IB * VEB_on
	calc_PEC = calc_IC * assume_VEC
	calc_PT:float = calc_PEB  +  calc_PEC


	ans_string:str = f"""
using KVL equation around the E-B loop:

  VEE - VEB(on) - IB*RB = VBB

Solve for IB:

  IB = (VEE - VEB(on) - VBB) / RB
     = ({VEE} - {VEB_on} - {VBB}) / {RB}
     = {calc_IB}A.

With Beta given, calc IC AND IE:
  IC = Beta*IB
     = {Beta} * {calc_IB}
     = {calc_IC}A.

  IE = (1 +Beta)*IB
     = (1 + {Beta}) * {calc_IB}
     = {calc_IE}A.
 
Assume that VEC = 2.5V which is one-half the supply voltage VEE.
Calculate RC:

  RC = (VEE - VEC) / IC
     = ({VEE} - {assume_VEC}) / {calc_IC}
     = {calc_RC}ohm.

The power dissipated in the transistor is due to the current passing
through the EB junction and across the emitter-collector EC at their
bias voltages:

  PEB = IB * VEB(on)  -and -  PEC = IC * VEC

Therefore, PT = PEB + PEC

  PT = IB * VEB(on)  +  IC * VCE
     = {calc_IB} * {VEB_on}  +  {calc_IC} * {assume_VEC}
     = {calc_PT}W.
"""
	print( ans_string )


	print( '---- (assertions) -------------------------------------------' )

	try:
		assertions.assert_within_percentage( calc_IB, ans_IB, assert_percentage )
		print( f"CALC IB = {calc_IB}A is within {assert_percentage}% of accepted answer: {ans_IB}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( calc_IC, ans_IC, assert_percentage )
		print( f"CALC IC = {calc_IC}A is within {assert_percentage}% of accepted answer: {ans_IC}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( calc_IE, ans_IE, assert_percentage )
		print( f"CALC IE = {calc_IE}A is within {assert_percentage}% of accepted answer: {ans_IE}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( calc_RC, ans_RC, assert_percentage )
		print( f"CALC RC = {calc_RC}ohm is within {assert_percentage}% of accepted answer: {ans_RC}ohm." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( calc_PT, ans_PT, assert_percentage )
		print( f"CALC Xistor power diss = {calc_PT}W is within {assert_percentage}% of accepted answer: {ans_PT}W." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
