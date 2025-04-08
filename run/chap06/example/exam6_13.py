from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations import equations


def exam6_13(self):
	"""Page 424:
	Objective: Calculate the input and output resistance of the
	emitter-follower circuit shown in Figure 6.49. Assume RS = 0.
	The small-signal parameters, as determined in Example 6.12,
	are rπ = 3.28k, β = 100, and ro = 100k.
	Tue, Apr  8, 2025  5:54:54 PM
	ANS:  .
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

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers -------------------
	ans:float = 0

	# ---- Givens --------------------
	rpi:float = 3.28e+03
	ro:float = 100e+03
	B:float = 100
	R1:float = 50e+03
	R2:float = 50e+03
	RE:float = 2000

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------
	ro_pllel_RE:float = equations.r1_parallel_r2( ro, RE )
	Rib:float = rpi + (1+B) *ro_pllel_RE
	Rin:float = equations.equivalent_parallel_resisitance( [R1,R2,Rib] )


	print( '\n---- (Input Resistance) ----------------------------' )
	ans_string:str = f"""
The input resistance looking into the base was determined
in Example 6.12 as:

  Rib = rpi + (1+B)( ro||RE )
      = {rpi} + (1+{B})( {ro}||{RE} )
      = {rpi} + (1+{B})( {ro_pllel_RE} )
  Rib = {Rib}ohm.

And the INPUT RESISTANCE \"seen\" by the AC small-signal
voltage-source, vs:

  Rin = R1||R2||Rib
      = {R1}||{R2}||{Rib}
  Rin = {Rin}ohm.

Comment: The input resistance of the emitter-follower looking
into the base is substantially larger than that of the simple
common-emitter circuit because of the (1 + B) factor. This is
one advantage of the emitter-follower circuit. However, in this
case, the input resistance seen by the signal source is
dominated by the bias resistors R1 and R2. To take advantage
of the large input resistance of the emitter-follower
circuit, the bias resistors must be designed to be much larger.
"""
	print( ans_string )

	print( '\n---- (Output Resistance) ----------------------------' )

	rBeta:float = rpi / (1+B)
	Ro:float = equations.equivalent_parallel_resisitance(
		[rBeta,RE,ro]
	)

	ans_string:str = f"""
The output resistance is found from Equation (6.74)

  **>  Ro = ( rpi / (1+B) )||RE||ro
          = ( {rpi} / (1+{B}) )||{RE}||{ro}
          = {Ro}ohm.

The output resistance is DOMINATED by the first term that
has (1 + B) in the denominator.

Comment: The emitter-follower circuit is sometimes referred to as
an impedance transformer because the input impedance is large and
the output impedance is small. The very low output resistance makes
the emitter-follower act almost like an ideal voltage source, so
the output is not loaded down when used to drive another load.
Because of this, the emitter-follower is often used as the output
stage of a multistage amplifier.
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
