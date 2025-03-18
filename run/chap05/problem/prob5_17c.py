from inspect import currentframe
# import math
# from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob5_17c(self):
	"""Page 353:
	For all the transistors in Figure P5.17, β = 75. The results of some
	measurements are indicated on the figures. Find the values of the other
	labeled currents, voltages, and/or resistor values.
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
	ans_VCE:float = 1.96        # V
	ans_iC:float  = 1.744e-03   # A

	# ---- Assumptions --------------------
	VBE_NPN:float = 0.7   # V


	# ---- Givens (a) --------------------
	Beta:float = 75
	VCC:float = 8    # V
	VEE:float = -8   # V
	RC:float = 4000    # Ω
	RB:float = 10000   # Ω
	RE:float = 4000    # Ω


	ans_string:str = """
Per schematics per Figure P5.17, some BJT characteristics may be assumed.
For example, for NPN, VBE ~= 0.7V, for PNP, VBE = -0.7V
"""
	print( ans_string )


	print( '---- (Fig P5.17 c) -------------------------------------------', end='' )

	calc_iE:float = ( -VEE - VBE_NPN ) / ( ( RB / ( 1 + Beta) ) + RE )
	calc_iE = round(calc_iE,6)

	calc_iC:float = ( Beta / ( 1 + Beta) ) * calc_iE
	calc_iC = round(calc_iC,6)

	calc_VRC:float = calc_iC * RE
	calc_VRE:float = calc_iE * RE
	calc_VCE:float = (VCC - VEE ) - calc_VRC - calc_VRE
	calc_VCE = round(calc_VCE,2)

	ans_string = f"""
The relationship between the emitter and base currents:

    iE = (1 + Beta)iB    Eq (5.9)

Voltage-drop across RB:  VRB = iB*RB = [ iE / (1+Beta) ] * RB
Voltage-drop across RE:  VRE = iE*RE.
Voltage-drop across PN junction = VBE = 0.7V.
Using KVL from the ground terminal on RB to VEE (-8V):

  **>  0 - VRB - VBE - VRE - VEE = 0

Write KVL terms using the resistance values, VEE, and iE:

  **>  0 - ( [ iE / (1+Beta) ] * RB ) - VBE - iE*RE - VEE = 0
  **>  0 - ( [ iE / (1+Beta) ] * RB ) - {VBE_NPN} - iE*RE = -({VEE})

Solve for iE.
iE = {calc_iE}A = {calc_iE*1000}mA

iC = ( Beta / 1+Beta) * iE = {calc_iC}A = {round(calc_iC*1000,6)}mA.

To solve for VCE, use KVL and calculate the voltage-drops from VCC to VEE.

VRC + VCE + VRE = 16
VRC = iC * RC, VRE = iE * RE, and so

VCE = 16 - VRC - VRE
VCE = {calc_VCE}V
"""
	print( ans_string )

# 	try:
# 		assertions.assert_within_percentage( calc_iC, ans_a_iC, assert_percentage )
# 		print( f"ASSERT iC = {calc_iC}A is within {assert_percentage}% of accepted answer: {ans_a_iC}A." )
# 	except AssertionError as e:
# 		print( f"ASSERT AssertionError {pnum}: {e}" )


# 	calc_VC:float = calc_VE + VCE_a
# 	calc_RC:float = ( VCC_a - calc_VC ) / calc_iC
# 	calc_RC = round(calc_RC,-1)

# 	ans_string:str = f"""
# To calculate RC, find the voltage drop across it and divide by current iC.
# Therefore, find VC = VE + VCE.
# VC = {calc_VE} + {VCE_a}
# VC = {calc_VC}V
# RC = ( VCC - VC ) / iC
# RC = ( {VCC_a} - {calc_VC} ) / {calc_iC}
# RC = {calc_RC}ohm = {round(calc_RC/1000,2)}kohm
# """
# 	print( ans_string )


# 	try:
# 		assertions.assert_within_percentage( calc_RC, ans_a_RC, assert_percentage )
# 		print( f"ASSERT RC = {calc_RC}ohm is within {assert_percentage}% of accepted answer: {ans_a_RC}ohm." )
# 	except AssertionError as e:
# 		print( f"ASSERT AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )
