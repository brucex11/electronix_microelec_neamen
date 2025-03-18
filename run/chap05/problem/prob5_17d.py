from inspect import currentframe
# import math
# from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob5_17d(self):
	"""Page 353:
	For all the transistors in Figure P5.17, β = 75. The results of some
	measurements are indicated on the figures. Find the values of the other
	labeled currents, voltages, and/or resistor values.
 	ANS:  (b) VB = 0.164V, RC =  8.11kΩ
	ANS:  (c) VCE = 1.96V, iC = 1.744mA
	ANS:  (d) VC = 1.49V, iB = 4.61μA."
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

	# ---- Answers -----------------------
	ans_d_VC:float = 1.49        # V
	ans_d_iB:float = 4.61e-06    # A

	# ---- Assumptions --------------------
	VBE_NPN:float = 0.7   # V


	# ---- Givens -------------------------
	Beta:float = 75
	VCC_d:float = 5       # V
	RC_d:float = 10e+03   # Ω
	RB_d:float = 20e+03   # Ω
	RE_d:float = 2e+03    # Ω



	ans_string:str = """
Per schematics per Figure P5.17, some BJT characteristics may be assumed.
For example, for NPN, VBE ~= 0.7V,  for PNP, VBE = -0.7V
"""
	print( ans_string )


	print( '---- (Fig P5.17 d) -------------------------------------------', end='' )

	ans_string = f"""
At node VC, iC and iB flow INTO the transistor Q1, and therefore
flow OUT of the node VC.
Since for any transistor iE = iC + iB, then the current INTO node
VC MUST = iE by KCL.

Therefore, iRC = iRE, and it follows that iE = iRE.

With one equation ( KVL through VCC, RC, RB, Q1-BE-junction and RE )
and one unknown, namely iE, iE is calculated.

Use iE = (1 + Beta)iB for RB current, iRB.

Once iE is known, along with Q1's Beta, iB and VC are calculated.

KVL:
VCC - iC*RC - iB*RB - VBE - iRE*RE = 0
and,
iB = iE / (1 + Beta)   Eq (5.9)

Substitute for iB and iRE (where iRE is in series with emitter)

  **>  VCC - iE*RC - ( iE / (1 + Beta) )*RB - VBE - iE*RE = 0

Solve equation above for iE, assume VBE = 0.7V.
"""
	print( ans_string )

	clac_denom:float = ( ( 1 / (1 + Beta)) * RB_d ) + RE_d + RC_d
	calc_iE:float = ( VCC_d - VBE_NPN ) / clac_denom
	calc_iE = round(calc_iE,7)
	print( f"iE = {calc_iE}A = {round(calc_iE,7)*1000}mA" )

	print( f"Per iE = (1 + Beta)iB    Eq (5.9), calculate iB." )
	calc_iB:float = calc_iE / (1+Beta)
	calc_iB = round(calc_iB,8)
	# print( f"iB = {calc_iB}A = {round(calc_iB,8)*1e+06}uA." )

	try:
		assertions.assert_within_percentage( calc_iB, ans_d_iB, assert_percentage )
		print( f"ASSERT iB = {calc_iB}A is within {assert_percentage}% of accepted answer: {ans_d_iB}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	print( f"VC is the voltage-drop across RC: VC = VCC - iE*RC\n" )
	calc_VC:float = VCC_d - calc_iE * RC_d
	calc_VC = round(calc_VC,2)

	try:
		assertions.assert_within_percentage( calc_VC, ans_d_VC, assert_percentage )
		print( f"ASSERT VC = {calc_VC}V is within {assert_percentage}% of accepted answer: {ans_d_VC}V." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )
