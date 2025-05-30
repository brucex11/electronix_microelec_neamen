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
	calc_IE:float = ( VCC_d - VBE_NPN ) / clac_denom
	calc_IE = round(calc_IE,7)
	print( f"iE = {calc_IE}A = {round(calc_IE,7)*1000}mA" )

	print( f"Per iE = (1 + Beta)iB    Eq (5.9), calculate iB." )
	calc_IB:float = calc_IE / (1+Beta)
	calc_IB = round(calc_IB,8)
	# print( f"iB = {calc_IB}A = {round(calc_IB,8)*1e+06}uA." )

	try:
		assertions.assert_within_percentage( calc_IB, ans_d_iB, assert_percentage )
		print( f"ASSERT iB = {calc_IB}A is within {assert_percentage}% of accepted answer: {ans_d_iB}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	print( f"VC is the voltage-drop across RC: VC = VCC - iE*RC" )
	calc_VC:float = VCC_d - calc_IE * RC_d
	calc_VC = round(calc_VC,2)

	try:
		assertions.assert_within_percentage( calc_VC, ans_d_VC, assert_percentage )
		print( f"ASSERT VC = {calc_VC}V is within {assert_percentage}% of accepted answer: {ans_d_VC}V." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	print( '\n---- (Calc VB and VE) ------------------------------', end='' )

	# 1)
	calc_VRB:float = calc_IB * RB_d
	calc_VB:float = calc_VC - calc_VRB
	calc_VE:float = calc_VB - VBE_NPN

	# 2)
	calc_IC:float = Beta * calc_IB
	calc_IE:float = calc_IB + calc_IC
	calc_VE = calc_IE * RE_d
	calc_VB = calc_VE + VBE_NPN

	ans_string = f"""
With IB and VC now known, lets see the most accurate way to calc
VB and VE.

1) Calc the voltage-drop across RB and subtract from VC to get VB.
   Then subtract VBE from VB to get VE.
   VRB = {calc_IB} * {RB_d}
       = {calc_VRB}V.
    VB = {calc_VB}V.
    VE = {calc_VE}V.

2) Calc IC = Beta*IB, then IE = IB + IC.  Calc the voltage-drop
   across RE to get VE, then add VBE to get VB.
    VE = {calc_VE}V.
    VB = {calc_VB}V.

"""
	print( ans_string )



	print( f"\n--- END {self.prob_str} ---" )
