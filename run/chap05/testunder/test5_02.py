from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def test5_02(self):
	"""Page 295:
	An npn transistor is biased in the forward-active mode. The base current is
	IB = 5.0μA and the collector current is IC = 0.62mA. Determine IE, β, and α.
	ANS: IE = 0.625mA, β = 124, α = 0.992.
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
	ans_IE:float = 0.625e-03   # A
	ans_Beta:float = 124
	ans_Alpha:float = 0.992

	# ---- Givens --------------------
	given_IB:float = 5e-06      # A
	given_IC:float = 0.62e-03   # A

	# ---- Calcs ---------------------
	calc_IE:float = given_IB + given_IC
	calc_Beta:float = given_IC / given_IB
	calc_Beta = round(calc_Beta,0)
	calc_Alpha:float = calc_Beta / ( 1 + calc_Beta )

	ans_string:str = f"""
For BJT, IE is always = IB + IC.  See Table 5.1 page 294 for summary of
BJT I-V characteristics.

  IE = {given_IB} + {given_IC} = {calc_IE}A = {calc_IE*1000}mA.

With IB and IC given, Beta = IC / IB.

  Beta = {given_IC} / {given_IB} = {calc_Beta}

Once Beta is calculated, Alpha = Beta / ( 1 + Beta )    Eq 5.11  pg 291

  Alpha = {calc_Beta} / ( 1 + {calc_Beta} ) = {calc_Alpha}
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
