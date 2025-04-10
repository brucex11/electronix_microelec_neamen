from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_mA, to_s_uA


def exer6_01(self):
	"""Page age 383:
	Calculate the small-signal voltage gain of the most-basic NPN BJT
	circuit shown in Figure 6.3.
	Assume the transistor and circuit parameters are: Beta = 120, VCC = 3.3V,
	VBE = 0.7V, RC = 15k, RB = 180k, and VBB = 0.85V.
	Thu, Apr  3, 2025  7:03:12 AM"
	ANS(DC):  ICQ = 0.1mA, VCEQ = 1.8V
	ANS(AC):  rpi = 31.2k, gm = 3.846mA/V, Av = -8.52.
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

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers -------------------
	ans_ICQ:float = 0.1e-03
	ans_rpi:float = 31200   # Ω

	# ---- Givens --------------------
	Beta:float = 120
	VCC:float = 3.3
	VBE:float = 0.7
	RC:float = 15e+03
	RB:float = 180e+03
	VBB = 0.85


	print( '\n---- (DC Solution) -------------------------------' )
	IBQ:float = (VBB - VBE) / RB
	IBQuA:str = to_s_uA( IBQ, r_val=6 )
	ICQ = Beta * IBQ
	ICQmA:str = to_s_mA( ICQ, r_val=4 )
	VCQ:float = VCC - (ICQ * RC)
	VCEQ:float = VCQ


	ans_string:str = f"""
Calculate Q-point ICQ and VCEQ.  Q is in active-region.

IBQ = (VBB - VBE) / RB
    = ({VBB} - {VBE}) / {RB}
    = {IBQuA}.
ICQ = Beta * IBQ
    = {Beta} * {IBQ}
    = {ICQmA}.

VCQ = VCC - (ICQ * RC)
    = {VCC} - ({ICQmA} * {RC})
    = {round(VCQ,1)}V.

Since there is no emitter resistor, VCEQ = VCQ = {round(VCEQ,1)}V.
"""
	print( ans_string )

	try:
		assert_within_percentage( ICQ, ans_ICQ, assert_percentage )
		print( f"ASSERT ICQ = {ICQmA} is within {assert_percentage}% of accepted answer: {to_s_mA(ans_ICQ, r_val=4)}." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	print( '\n---- (AC Solution) -------------------------------' )
	rpi:float = (Beta * self._vthrml0_026) / ICQ
	gm:float = ICQ / self._vthrml0_026
	Av:float = -( gm * RC * rpi ) / (rpi + RB)

	ans_string = f"""
Use the small-signal equivalent circuit (Fig 6.11) to solve
for rpi, gm and Av.

rpi = (Beta * VT) / ICQ
    = ({Beta} * {self._vthrml0_026}) / {ICQmA}
    = {rpi}ohm.

gm = ICQ / VT
   = {ICQmA} / {self._vthrml0_026}V
   = {to_s_mA(gm, r_val=3)}/V.

Av = Vo / Vs.

At the output:
Vo = -(Ic * RC)  and is negative because (conventional) current
flows thru RC from 'negative ground' to positive Vo.

  **>  Ic = gm * Vpi  (phasor notation)

Vo = -(gm * Vpi) * RC    Eq 6.31 pg 381

At the input:
Use voltage-divider to find Vs.

  Vpi = Vs * rpi / (rpi + RB)
	Vpi * (rpi + RB) = Vs * rpi
	Vs = (Vpi / rpi) * (rpi + RB)

Av = [Vo] / [Vs]
   = -[ (gm * Vpi) * RC ] / [ (Vpi / rpi) * (rpi + RB) ]
   Vpi cancels.
	 = -[ (gm) * RC ] / [ (1 / rpi) * (rpi + RB) ]
	 = -[ (gm) * RC ] / [ (rpi + RB) / rpi ]

   **>  Av = -[ (gm) * RC * rpi ] / [ (rpi + RB) ]

           = -[ ({gm}) * {RC} * {rpi} ] / [ ({rpi} + {RB}) ]
           = {Av}.
"""
	print( ans_string )

	try:
		assert_within_percentage( rpi, ans_rpi, assert_percentage )
		print( f"ASSERT rpi = {rpi}ohm is within {assert_percentage}% of accepted answer: {ans_rpi}ohm." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )
