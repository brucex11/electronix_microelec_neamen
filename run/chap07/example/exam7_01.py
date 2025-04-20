from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.equations import current_divider


def exam7_01(self):
	"""Page 479:
	Objective: Determine the corner frequencies and maximum-magnitude
	asymptotes of the Bode plots for a specified circuit.
	For the circuits in Figures 7.2 and 7.3, the parameters are: RS = 1kΩ,
	RP = 10kΩ, CS = 1μF, and CP = 3pF.
	Fri, Apr 18, 2025  4:54:56 PM
	ANS:  τ = 11ms, max mag = 0.909, f = 58.3MHz"
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

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  τ

	# ---- Answers -------------------
	ans:float = 0

	# ---- Givens --------------------
	RS:float = 1e+03
	RP:float = 10e+03
	CS:float = 1e-06   # uF
	CP:float = 3e-12   # pF

	# ---- Calcs ---------------------

	tRC1:float = self.calc_RC_tau( (RS+RP), CS )
	f1:float = 1 / (2 * math.pi * tRC1)
	maxm1:float = RP / (RS + RP)
	maxdb1 = 20 * math.log10( maxm1 )

	RS_p_RP:float = r1_parallel_r2( RS, RP )
	tRC2:float = self.calc_RC_tau( RS_p_RP, CP )
	f2:float = 1 / (2 * math.pi * tRC2)
	maxm2:float = RP / (RS + RP)
	maxdb2 = 20 * math.log10( maxm2 )


	ans_string:str = f"""
FIG 7.2, (Resistor + Capacitor in series)
  TC (time constant) = ((RS+RP) * CS)s.
                     = (({RS}+{RP}) * {CS})s.
  TC = {tRC1}s.

Corner frequency:
  f = 1 / (2 * pi * tau)
    = 1 / (2 * pi * {tRC1})
  f = {f1}Hz.

Maximum magnitude asymptotes:
  RP / (RS + RP)
  {RP} / ({RS} + {RP}) = {maxm1}
-OR-
  20log( RP / (RS + RP) ) = {maxdb1}dB.

FIG 7.3, (Resistor + Capacitor in parallel):
Time constant still involves R and C, but it's influenced by the
effective resistance seen by the capacitor.
If a voltage source is applied, capacitor charges instantly (in theory)
through the resistor branch, but in practice, the circuit's time behavior
still has a characteristic shape, depending on current splitting and
equivalent resistance.
  TC (time constant) = ((RS||RP) * CP)s.
                     = (({RS}||{RP}) * {CP})s.
                     = (({RS_p_RP}) * {CP})s.
  TC = {tRC2}s.

Corner frequency:
  f = 1 / (2 * pi * tau)
    = 1 / (2 * pi * {tRC2})
  f = {f2:.6e}Hz.

Maximum magnitude asymptotes:
  RP / (RS + RP)
  {RP} / ({RS} + {RP}) = {maxm2}
-OR-
  20log( RP / (RS + RP) ) = {maxdb2}dB.

The maximum magnitude is the same as just calculated: 0.909 or -0.828 dB.

Comment: Since the two capacitance values are substantially different,
the two time constants differ by orders of magnitude, which means that
the two corner frequencies also differ by orders of magnitude.
"""
	print( ans_string )

	# print( '\n---- (a) ----' )

	# try:
	# 	assert_within_percentage( calc_result, ans, assert_percentage )
	# 	print( f"ASSERT ID = {calc_result}A is within {assert_percentage}% of accepted answer: {ans}." )
	# except AssertionError as e:
	# 	print( f"AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )
