from inspect import currentframe
# import math
# from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob5_17a(self):
	"""Page 353:
	For all the transistors in Figure P5.17, β = 75. The results of some
	measurements are indicated on the figures. Find the values of the other
	labeled currents, voltages, and/or resistor values.
	ANS:  (a) iC =  1.836mA, RC =  3.65kΩ
 	ANS:  (b) VB = 0.164V, RC =  8.11kΩ
	ANS:  (c) VCE = 1.96V, iC = 1.744mA."
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

	# ---- Answers -------------------
	ans_a_iC:float = 1.836e-03   # A
	ans_a_RC:float = 3.65e+03    # Ω

	# ---- Assumptions --------------------
	VBE_NPN:float = 0.7   # V


	# ---- Givens (a) --------------------
	Beta:float = 75
	VCC_a:float = 10    # V
	VEE_a:float = -10   # V
	VCE_a:float = 4     # V
	RE_a:float = 5000   # Ω
	VB_a:float = 0   # V, by inspection


	ans_string:str = """
Per schematics per Figure P5.17, some BJT characteristics may be assumed.
For example, for NPN, VBE ~= 0.7V,  for PNP, VBE = -0.7V
"""
	print( ans_string )


	print( '---- (Fig P5.17 a) -------------------------------------------', end='' )

	calc_VE:float = ( VB_a - VBE_NPN )
	calc_iE = ( calc_VE - VEE_a) / RE_a
	calc_iC:float = ( Beta / ( 1 + Beta) ) * calc_iE
	calc_iC = round(calc_iC,6)

	ans_string = f"""
Assume VBE is typical 0.7V, therefore VE = ( VB - VBE )
  where VB = {VB_a}V
  VE = VB - VBE = {calc_VE}V

Current OUT of emitter and through RE, calculate iE = (VE - VEE) / RE
iE = ( {calc_VE} - ({VEE_a}) ) / {RE_a}
iE = {calc_iE}A = {calc_iE*1000}mA

With iE now known, calculate iC = ( Beta / 1 + Beta ) * iE   Eq (5.10)
iC = ( {Beta}) / ( 1 + {Beta}) ) * {calc_iE}
iC = {calc_iC}A = {round(calc_iC*1000,6)}mA
"""
	print( ans_string )

	try:
		assertions.assert_within_percentage( calc_iC, ans_a_iC, assert_percentage )
		print( f"ASSERT iC = {calc_iC}A is within {assert_percentage}% of accepted answer: {ans_a_iC}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	calc_VC:float = calc_VE + VCE_a
	calc_RC:float = ( VCC_a - calc_VC ) / calc_iC
	calc_RC = round(calc_RC,-1)

	ans_string:str = f"""
To calculate RC, find the voltage drop across it and divide by current iC.
Therefore, find VC = VE + VCE.
VC = {calc_VE} + {VCE_a}
VC = {calc_VC}V
RC = ( VCC - VC ) / iC
RC = ( {VCC_a} - {calc_VC} ) / {calc_iC}
RC = {calc_RC}ohm = {round(calc_RC/1000,2)}kohm
"""
	print( ans_string )


	try:
		assertions.assert_within_percentage( calc_RC, ans_a_RC, assert_percentage )
		print( f"ASSERT RC = {calc_RC}ohm is within {assert_percentage}% of accepted answer: {ans_a_RC}ohm." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )
