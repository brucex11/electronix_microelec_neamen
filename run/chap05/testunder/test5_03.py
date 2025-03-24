from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def test5_03(self):
	"""Page 295:
	The emitter current in a pnp transistor biased in the forward-active mode
	is IE = 1.20mA. The common-base current gain of the transistor is α = 0.9915.
	Determine β, IB, and IC.
	ANS:  β = 117, IC = 1.19mA, IB = 10.2uA.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )

	# ---- Answers -------------------
	ans_IB:float = 10.2e-06   # A
	ans_IC:float = 1.19e-03   # A
	ans_Beta:float = 117

	# ---- Givens --------------------
	given_IE:float = 1.2e-03      # A
	given_Alpha:float = 0.9915

	# ---- Calcs ---------------------
	calc_Beta:float = given_Alpha / ( 1 - given_Alpha )
	calc_Beta = round(calc_Beta,0)
	calc_IC:float = given_Alpha * given_IE
	calc_IB:float = given_IE / ( 1 + calc_Beta )
	calc_IB = round(calc_IB,7)

	ans_string:str = f"""
For BJT, IE is always = IB + IC.  See Table 5.1 page 294 for summary of
BJT I-V characteristics.

Given Alpha, calculate Beta = Alpha / ( 1 - Alpha )

  Beta = {given_Alpha} / ( 1 - {given_Alpha} ) = {calc_Beta}

IC = Alpha * IE = {given_Alpha} * {given_IE}
   = {calc_IC}A = {calc_IC*1000}mA.

Finally,
IB = IE / ( 1 + Beta ) = {given_IE} / ( 1 + {calc_Beta} )
   = {calc_IB}A = {round(calc_IB*1000000,7)}uA.
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
