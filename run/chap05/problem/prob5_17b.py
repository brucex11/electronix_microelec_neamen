from inspect import currentframe
# import math
# from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob5_17b(self):
	"""Page 353:
	For all the transistors in Figure P5.17, β = 75. The results of some
	measurements are indicated on the figures. Find the values of the other
	labeled currents, voltages, and/or resistor values.
 	ANS:  (b) VB = 0.164V, RC =  8.11kΩ."
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
	ans_VB:float = 0.164       # V
	ans_RC:float = 8.11e+03    # Ω

	# ---- Assumptions --------------------
	VBE_NPN:float = 0.7   # V


	# ---- Givens (a) --------------------
	Beta:float = 75
	VEE:float = 5    # V
	VCC:float = -5   # V
	IQ:float = 0.5e-03  # A
	VC:float = -1       # V
	RB:float = 25e+03   # Ω


	ans_string:str = """
Per schematics per Figure P5.17, some BJT characteristics may be assumed.
For example, for NPN, VBE ~= 0.7V,  for PNP, VBE = -0.7V
"""
	print( ans_string )


	print( '---- (Fig P5.17 b) -------------------------------------------', end='' )

	calc_iB:float = ( IQ / ( 1 + Beta ) )
	calc_iB = round(calc_iB,7)
	calc_VB:float = calc_iB * RB
	calc_VB = round(calc_VB,3)

	calc_iC = IQ - calc_iB

	calc_RC = ( VC - VCC ) / calc_iC
	calc_RC = int(calc_RC)

	ans_string = f"""
Transistor Q1 is PNP device, common-emitter configuration.  Since iE = IQ
is given and Beta is known, for the relationship between the emitter
and base currents:

    iE = (1 + Beta)iB    Eq (5.9)

Therefore.
  iB = iE / ( 1 +  Beta )
  iB = {IQ} / ( 1 + {Beta} )
  iB = {calc_iB}A.

With iB known, the voltage
  VB = iB * RB
  VB = {calc_iB} * {RB}
  VB = {calc_VB}V.

For all bipolar transistors, iE = IQ = iB + iC, therefore
  iC = iE - iB 
  iC = {IQ} - {calc_iB}
  iC = {calc_iC}A.

Finally, RC is the voltage-drop across it divided by the current throught it.
  RC = ( VC - VCC ) / iC
  RC = ( {VC} - {VCC} ) / {calc_iC}
  RC = {calc_RC}ohm
"""
	print( ans_string )

	print( f"\n--- END {self.prob_str} ---" )
