from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA


def exam6_01(self):
	"""Page 382:
	Calculate the small-signal voltage gain of the most-basic
	NPN BJT circuit	shown in Figure 6.3.
	Assume the transistor and circuit parameters are: β = 100, VCC = 12V,
	VBE =	0.7V, RC = 6k, RB = 50k, and VBB = 1.2V.
	ANS(DC):  ICQ = 1mA, VCEQ = 6 V
	ANS(AC):  rπ = 2.6k, gm = 38.5mA/V, Av = -11.4.
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
	ans_ICQ:float = 1e-03

	# ---- Givens --------------------
	Beta:float = 100
	VCC:float = 12
	VBE:float = 0.7
	RC:float = 6e+03
	RB:float = 50e+03
	VBB = 1.2


	print( '\n---- (DC Solution) -------------------------------' )
	IBQ:float = (VBB - VBE) / RB
	ICQ = Beta * IBQ
	VCQ:float = VCC - (ICQ * RC)
	VCEQ:float = VCQ


	ans_string:str = f"""
Calculate Q-point ICQ and VCEQ.  Q is in active-region.

IBQ = (VBB - VBE) / RB
    = ({VBB} - {VBE}) / {RB}
    = {IBQ}A.
ICQ = Beta * IBQ
    = {Beta} * {IBQ}
    = {ICQ}A.

VCQ = VCC - (ICQ * RC)
    = {VCC} - ({ICQ} * {RC})
    = {VCQ}V.

Since there is no emitter resistor, VCEQ = VCQ = {VCEQ}V.
"""
	print( ans_string )

	try:
		assert_within_percentage( ICQ, ans_ICQ, assert_percentage )
		print( f"ASSERT ICQ = {ICQ}A is within {assert_percentage}% of accepted answer: {ans_ICQ}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	print( '\n---- (AC Solution) -------------------------------' )
	rpi:float = (Beta * self._vthrml0_026) / ICQ
	rpi_IBQ:float = self._vthrml0_026 / IBQ
	gm:float = ICQ / self._vthrml0_026
	Av:float = -( gm * RC * rpi ) / (rpi + RB)

	ans_string = f"""
Use the small-signal equivalent circuit (Fig 6.11) to solve
for rpi, gm and Av.

  rpi = (Beta * VT) / ICQ
      = ({Beta} * {self._vthrml0_026}) / {ICQ}
      = {rpi}ohm.

  rpi = VT / IBQ
      = {self._vthrml0_026} / {IBQ}
      = {to_s_k(val=rpi_IBQ, r_val=1)}k-ohm.

  gm = ICQ / VT
     = {ICQ} / {self._vthrml0_026}
     = {gm}A/V.
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

	print( f"--- END {self.prob_str} ---" )
