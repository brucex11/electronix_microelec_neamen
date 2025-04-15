from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.equations import current_divider


def test6_07(self):
	"""Page 410:
	For the circuit in Figure 6.39, let β = 125, VBE(on) = 0.7V, and VA = 200V.
	(a) Determine the small-signal voltage gain Av.
	(b) Determine the output resistance Ro.
	ANS:  (a) Av = -50.5 (b) Ro = 2.28kΩ.
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

	#  α   β   Ω   μ   λ   γ   ξ   ω

	# ---- Answers -------------------
	ans_Av:float = -50.5
	ans_Ro:float = 2.28e+03   # Ω

	# ---- Givens --------------------
	BetaDC:float = 125
	VA:float = 200    # V
	VCC:float = 5
	VEE:float = -5
	R1:float = 20e+03
	R2:float = 20e+03
	RC:float = 2.3e+03
	RE:float = 5e+03
	RL:float = 5e+03


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V
	VB:float = 0    # V

	# ---- DC op point calcs ---------------------
	IEQ:float =  ( VB - VBE - VEE ) / RE
	IBQ:float = IEQ / (1 + BetaDC)
	ICQ:float = IEQ - IBQ
	gm:float = ICQ / self._vthrml0_026

	# INPUT Z
	RTh:float = r1_parallel_r2( R1, R2 )
	rpi:float = (self._vthrml0_026) / IBQ
	rpi = round(rpi,0)
	re:float = (self._vthrml0_026) / IEQ
	re = round(re,0)
	re_IZR:float = rpi / BetaDC   # inverse-impedance-reflection
	re_IZR = round(re_IZR,0)

	rpi_ZR:float = (1 + BetaDC) * re  # impedance-reflection

	Ri_ZR:float = equivalent_parallel_resisitance( [R1, R2, rpi_ZR] )
	Ri_IZR:float = equivalent_parallel_resisitance( [R1, R2, rpi] )
	# rL:float = equivalent_parallel_resisitance( [ro, RL] )

	# OUTPUT Z
	ro:float = VA / ICQ
	Ro:float = r1_parallel_r2( ro, RC )
	Ro = round(Ro,0)


	ans_string:str = f"""
---- (DC op point) ----
Assume IB is negligible, therefore VB = 0V.  With VBE(on) = 0.7V,
calc current IEQ thru RE:

Q-point currents:
  IEQ = IRE = ( VB - VBE - VEE ) / RE
  IEQ = ( VB - VBE - VEE ) / RE
      = ( {VB} - {VBE} - {VEE} ) / {RE}
  IEQ = {IEQ} = {to_s_mA(IEQ, 3)}.

  IBQ = IEQ / (1 + BetaDC)
      = {IEQ} / (1 + {BetaDC})
  IBQ = {IBQ}

  ICQ = IEQ - IBQ
      = {IEQ} - {IBQ}
  ICQ = {ICQ} = {to_s_mA(ICQ, 3)}.

Transconductance:
  gm = ICQ / VT
     = {ICQ} / {self._vthrml0_026}
  gm = {gm} = {to_s_mA(gm, 3)}/V.


Q-point INPUT impedances:
  rpi = VT / IBQ
      = {self._vthrml0_026} / {IBQ}
  rpi = {rpi}

  re = VT / IEQ
     = {self._vthrml0_026} / {IEQ}
  re = {re}


Q-point OUTPUT impedance:
Early-voltage is a DC-parameter (it depends on the DC bias point),
but it's mainly used to calculate AC/small-signal output resistance.
  ro = VA / ICQ
     = {VA} / {ICQ}
  ro = {ro} = {to_s_k(ro,3)}kohm.


In-circuit INPUT impedance:
By inverse-impedance-reflection (divide by Beta):
  re = rpi / BetaDC  <- inverse-impedance-reflection
     = {rpi} / {BetaDC}
  re = {re_IZR}

  Ri_IZR = (R1||R2||(rpi / BetaDC))
         = ({R1}||{R2}||{re_IZR})
  Ri_IZR = {Ri_IZR}

By impedance-reflection (multiply by Beta):
  rpi = (1 + BetaDC) * re  <- impedance-reflection
      = (1 + {BetaDC}) * {re}
  rpi = {rpi_ZR}

  Ri_ZR = (R1||R2||((1 + BetaDC) * re))
        = ({R1}||{R2}||{rpi_ZR})
  Ri_ZR = {Ri_ZR}

In-circuit OUTPUT impedance:
  Ro = ro||RC.
     = ({ro})||({RC})
  Ro = {Ro} = {to_s_k(Ro,3)}kohm.
"""
	print( ans_string )


	# ---- AC op point calcs ---------------------
	Ro_p_RL:float = r1_parallel_r2( Ro, RL )
	Av:float = -1.0 * BetaDC * Ro_p_RL / rpi

	ans_string:str = f"""
---- (AC analysis) ----
Per the AC small-signal circuit, Av = vo / vb
INPUT side:
  vb = ib * rpi
  ib = (vb / rpi)

OUTPUT side using KCL:
  -BetaDC * ib = vo / (Ro||RL)

To calculate Av, substitute ib from the INPUT side into
the OUTPUT side:

  -BetaDC * (vb / rpi) = vo / (Ro||RL)
	-BetaDC / rpi = (vo / vb) / (Ro||RL)
	-BetaDC / rpi * (Ro||RL) = (vo / vb) = Av

  Av = -BetaDC * (Ro||RL) / rpi
     = -{BetaDC} * ({Ro}||{RL}) / {rpi}
  Av = {Av}.
"""
	print( ans_string )


	try:
		assert_within_percentage( Ro, ans_Ro, assert_percentage )
		print( f"ASSERT Ro = {Ro} is within {assert_percentage}% of accepted answer: {ans_Ro}kohm." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	try:
		assert_within_percentage( Av, ans_Av, assert_percentage )
		print( f"ASSERT Av = {Av} is within {assert_percentage}% of accepted answer: {ans_Av}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	print( f"--- END {self.prob_str} ---" )
