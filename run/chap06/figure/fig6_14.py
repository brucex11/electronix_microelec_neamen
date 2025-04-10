from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA


def fig6_14(self):
	"""Page 387:
	Determine Q-point IBQ, ICQ and VCEQ for Figure 6.14.
	Calculate circuit Av = Vo / Vs and compare with simulation.
	See ./LTspice/chap06/fig6_14/
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 3.5
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers -------------------
	ans_IBQ:float = -6.16e-06
	ans_ICQ:float = -1.249e-03

	# ---- Givens --------------------
	Beta:float = 203
	VCC:float = -5
	VBE:float = -0.66
	RC:float = 2e+03
	RB:float = 705e+03
	VBB = 1.2


	print( '\n---- (DC solution) -------------------------------' )
	IBQ:float = (VCC - VBE) / (RC + RB)
	ICQ = Beta * IBQ
	VCEQ:float = VCC - (ICQ * RC)
	# VCEQ:float = VCQ


	ans_string:str = f"""
Using KVL in B-E junction branch, calculate IBQ for Q in active-region.

  **> VCC - IBQ*RC - IBQ*RB - VBE = 0

  VCC - VBE = IBQ*RC + IBQ*RB
  VCC - VBE = IBQ * (RC + RB)
  IBQ = (VCC - VBE) / (RC + RB)

  IBQ = (VCC - VBE) / (RC + RB)
      = ({VCC} - {VBE}) / ({RC} + {RB})
      = ({VCC-VBE}) / ({RC+RB})
      = {IBQ}A.
  IBQ = {to_s_uA(val=IBQ,r_val=6)}.

Use Q's Beta to calculate ICQ and then VC.

  ICQ = Beta * IBQ
      = {Beta} * {to_s_uA(val=IBQ,r_val=6)}
      = {ICQ}A
      = {to_s_mA(val=ICQ,r_val=3)}.

With ICQ known, calculate VC = VCEQ per the current ICQ
thru RC.

   ICQ = (VCC - VCEQ) / RC
       = (VCC - VCEQ) / RC
  VCEQ = VCC - ICQ*RC
       = {VCC} - {to_s_mA(val=ICQ,r_val=3)}*{RC}
    VC = {round(VCEQ,1)}V.
"""
	print( ans_string )

	try:
		assert_within_percentage( IBQ, ans_IBQ, assert_percentage )
		print( f"ASSERT IBQ = {IBQ}A is within {assert_percentage}% of accepted answer: {ans_IBQ}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	assert_percentage:float = 1.2
	try:
		assert_within_percentage( ICQ, ans_ICQ, assert_percentage )
		print( f"ASSERT ICQ = {ICQ}A is within {assert_percentage}% of accepted answer: {ans_ICQ}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	print( '\n---- (AC solution) -------------------------------' )
	rpi_ICQ:float = abs( (Beta * self._vthrml0_026) / ICQ )
	rpi_IBQ:float = abs( self._vthrml0_026 / IBQ )
	gm:float = ICQ / self._vthrml0_026
	RBadded = 1
	Av:float = -( gm * RC * rpi_ICQ ) / (rpi_ICQ + RBadded)

	ans_string = f"""
Use small-signal equivalent to calc rpi, gm, and Av; let ro = inf.

  rpi = (Beta * VT) / ICQ
      = ({Beta} * {self._vthrml0_026}) / {ICQ}
      = {to_s_k(val=rpi_ICQ, r_val=3)}k-ohm.

  rpi = VT / IBQ
      = {self._vthrml0_026} / {IBQ}
      = {to_s_k(val=rpi_IBQ, r_val=3)}k-ohm.

  gm = ICQ / VT
     = {ICQ} / {self._vthrml0_026}
     = {gm}A/V.
     = {to_s_mA(gm, r_val=3)}/V.

Since Q1 is self-biased, RB is NOT in series with the
voltage-source, so assign RB = {RBadded}ohm.

RB-added = {RBadded}ohm.

Av = [Vo] / [Vs]
   = -[ (gm * Vpi) * RC ] / [ (Vpi / rpi) * (rpi + RB) ]
   Vpi cancels.
	 = -[ (gm) * RC ] / [ (1 / rpi) * (rpi + RB) ]
	 = -[ (gm) * RC ] / [ (rpi + RB) / rpi ]

   **>  Av = -[ (gm) * RC * rpi ] / [ (rpi + RB) ]

      = -[ ({gm}) * {RC} * {rpi_ICQ} ] / [ ({rpi_ICQ} + {RBadded}) ]
   Av = {Av}.
"""
	print( ans_string )

	print( '---- (Av calc vs simulation) -----------------' )
	Vs:float = 0.018
	Vo:float = 1.7
	Av_sim:float = Vo / Vs

	ans_string = f"""
According to LTspice, for an {Vs}Vp-p input-voltage Vs, the output
at collector Vc = Vo = {Vo}Vp-p.
See file ./LTspice/chap06/fig6_14/fig6_14a_AC-1DC-voltage_source.asc.

Therefore, the simulated Av is
  Av-sim = Vo / Vs
         = {Vo} / {Vs}
  Av-sim = {Av_sim}.
"""
	print( ans_string )

	assert_percentage:float = 1.5
	try:
		assert_within_percentage( Av, Av_sim, assert_percentage )
		print( f"ASSERT Av = {Av} is within {assert_percentage}% of simulation Av = {Av_sim}." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )
