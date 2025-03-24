from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def exam5_03(self):
	"""Page 303:
	Objective: Calculate the base, collector, and emitter currents and the
	C-E voltage for a common-emitter circuit. Calculate the transistor power
	dissipation.
	For the circuit shown in Figure 5.19(a), the parameters are: VBB = 4V,
	RB = 220kΩ, RC = 2kΩ, VCC = 10V, VBE(on) = 0.7V, and β = 200.

	Comment: Since VBB > VBE (on) and VCE > VBE (on), the transistor is indeed
	biased in the forward-active mode. As a note, in an actual circuit, the voltage across
	a B-E junction may not be exactly 0.7V, as we have assumed using the piecewise
	linear approximation. This may lead to slight inaccuracies between the calculated
	currents and voltages and the measured values. Also note that, if we take the difference
	between IE and IC , which is the base current, we obtain IB = 20μA rather than
	15μA. The difference is the result of roundoff error in the emitter current.
	ANS: IB = 15μA, IC = 3mA, IE = 3.02mA, PT ~= 12mW
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
	ans_IB:float = 15e-06  # A
	ans_IC:float = 3e-03   # A
	ans_IE:float = 3.02e-03  # A
	ans_PT:float = 12e-03  # W

	# ---- Givens --------------------
	VBB:float =  4   # V
	VCC:float =  10  # V
	VBE_on:float =  0.7  # V
	RB:float = 220e+03  # Ω
	RC:float = 2e+03    # Ω
	Beta:float = 200

	# ---- Calcs ---------------------
	calc_IB:float = (VBB - VBE_on) / RB
	calc_IB = round(calc_IB,6)

	calc_IC:float = Beta * calc_IB
	calc_IC = round(calc_IC,3)

	calc_IE:float = ( 1 + Beta ) * calc_IB
	calc_IE = round(calc_IE,6)

	calc_VCE:float  = VCC - calc_IC * RC

	calc_PBE = calc_IB * VBE_on
	calc_PCE = calc_IC * calc_VCE
	calc_PT:float = calc_PBE  +  calc_PCE


	ans_string:str = f"""
The base current IB found using KVL around the base-circuit:

  IB = (VBB - VBE(on)) / RB = ({VBB} - {VBE_on}) / {RB:.3e}
     = {calc_IB}A.

With Beta given, calc IC AND IE:
  IC = Beta*IB
     = {Beta} * {calc_IB}
     = {calc_IC}A.

  IE = (1 +Beta)*IB
     = (1 + {Beta}) * {calc_IB}
     = {calc_IE}A.

Since the emitter is grounded, VCE == VC, and VC = VCC - VRC
where VRC is the voltage-drop across RC:

  VCE = VCC - IC*RC = {VCC} - {calc_VCE}
      = {calc_VCE}V.

The power dissipated in the transistor is due to the current passing
through the BE junction and across the collector-emitter CE at their
bias voltages:

  PBE = IB * VBE(on)  -and -  PCE = IC * VCE

Therefore, PT = PBE + PCE

  PT = IB * VBE(on)  +  IC * VCE
     = {calc_IB} * {VBE_on}  +  {calc_IC} * {calc_VCE}
     = {calc_PT}W.

"""
	print( ans_string, end='' )


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
		print( f"CALC IC = {calc_IE}A is within {assert_percentage}% of accepted answer: {ans_IE}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( calc_PT, ans_PT, assert_percentage )
		print( f"CALC Xistor power diss = {calc_PT}W is within {assert_percentage}% of accepted answer: {ans_PT}W." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
