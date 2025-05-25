from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.current import current_divider
from equations.voltage import voltage_divider


def exer6_07(self):
	"""Page 410:
	The circuit in Figure 6.38 has parameters V+ = 5V, V- = -5V,
	RE = 4k, RC = 4k, RB = 100k, and RS = 0.5k. The transistor parameters
	are BetaDC = 120, VBE(on) = 0.7V, and VA = 80V.
	(a) Determine the input resistance seen by the signal source.
	(b) Find the small-signal voltage gain.
	Tue, Apr 15, 2025 11:37:23 AM
	ANS:  (a) Ri = 3.91k, (b) Av = -114.
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
	ans_RVs:float = 3.91e+03
	ans_Av:float = -114

	# ---- Givens --------------------
	BetaDC:float = 120
	VA:float = 80    # V
	VCC:float = 5
	VEE:float = -5
	# VBB:float = none
	RS:float = 500
	RB:float = 100e+03
	RC:float = 4e+03
	RE:float = 4e+03
	# RL:float = none

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------
	# input resistance
	IBQ:float  = -(VEE + VBE) / ( RB + (1 + BetaDC) * RE)
	rpi:float = self._vthrml0_026 / IBQ
	Ri:float = r1_parallel_r2( RB, rpi)
	RVs:float = RS + Ri

	# output resistance
	ro:float = VA / IBQ
	Ro:float = RC

	# gain
	Av:float = -(BetaDC * RC / rpi) * (Ri / (Ri + RS))

	ans_string:str = f"""
---- (Input resistance) ----
Calc IBQ using KVL in the B-E junction branch.

  0 - VB - VBE - VRE - VEE = 0

where VB = IBQ * RB and VRE = (1 + BetaDC)* IBQ * RE.

  -(IBQ * RB) - VBE - VRE = VEE
  -(IBQ * RB) - VBE - [(1 + BetaDC)* IBQ * RE] = VEE
  -(IBQ * RB) - IBQ * [(1 + BetaDC) * RE] = VEE + VBE
  -(IBQ) * ( RB + (1 + BetaDC) * RE) = VEE + VBE
  IBQ = -(VEE + VBE) / ( RB + (1 + BetaDC) * RE)
  IBQ = {IBQ}
  IBQ = {to_s_uA(IBQ,8)}.

Next, calc rpi which is also Rib.

  rpi = VT / IBQ
      = {self._vthrml0_026} / {IBQ}
  rpi = {rpi}.
.
The circuit input resistance Ri:

  Ri = (RB||rpi)
     = ({RB}||{rpi})
  Ri = {Ri}.

Therefore, the input resistance seen by the signal source
is the series of RS and Ri.

  RVs = RS + Ri
      = {RS} + {Ri}
  RVs = {RVs} = {to_s_k(RVs,3)}k.

---- (Output resistance) ----
Given Early voltage VA,

  ro = VA / IBQ
     = {VA} / {IBQ}
     = {ro}
  ro = {to_s_k(ro,6)}k.

For the AC small-signal equivalent circuit, since
and RE is AC-bypassed with a capacitor (RE = 0), and
since ro >> RC,

  Ro = (ro||RC||RE) = RC
  Ro = RC.

---- (AC gain) ----
AC output:
  -BetaDC * Ib = Vo     Eq (1)

AC input current:
  Ib = Vin / Rib
  Ib = Vin / rpi        Eq (2)

AC input voltage (divider):
  Vin = ( Ri / (Ri + RS) ) * Vs   Eq (3)

Substitute (2) into (1):

  Vo = -BetaDC * (Vin / rpi) * RC   (4)

To solve for voltage gain Av = Vo / Vs,
substitute (3) into (4).

  Vo = -(BetaDC * RC / rpi) * (Ri / (Ri + RS)) * Vs

  Av = Vo / Vs
     = -(BetaDC * RC / rpi) * (Ri / (Ri + RS))
     = -({BetaDC} * {RC} / {rpi}) * ({Ri} / ({Ri} + {RS}))
  Av = {Av}.
"""
	print( ans_string )

	# print( '\n---- (DC op point) ----' )

	try:
		assert_within_percentage( RVs, ans_RVs, assert_percentage )
		print( f"ASSERT RVs = {RVs}ohm is within {assert_percentage}% of accepted answer: {ans_RVs}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )
