from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.current import current_divider
from equations.voltage import voltage_divider


def test7_01(self):
	"""Page 483:
	For the equivalent circuit shown in Figure 7.13, the parameters are:
	RS = 1kΩ, rpi = 2kΩ, RL = 4kΩ, gm = 50mA/V, and CC = 1μF.
	(a) Determine the expression for the circuit time constant.
	(b) Calculate the 3 dB frequency and maximum gain asymptote.
	(c) Sketch the Bode plot of the transfer function magnitude.
	Sat, Apr 19, 2025  8:31:05 PM
	ANS:  (a) τ = (rpi+ RS)CC, (b) f3dB = 53.1Hz, |T(jω)|max = 133."
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
	rpi:float = 2e+03
	RL:float = 4e+03
	CC:float = 1e-06    # uF
	gm:float = 50e-03   # A/V

	# ---- Calcs ---------------------

	tRC:float = self.calc_RC_tau( (RS + rpi), CC )
	f_3dB:float = 1 / (2 * math.pi * tRC)
	w_3dB:float = 1 / (tRC)
	w_3dB = round(w_3dB,1)
	# maxm1:float = RP / (RS + RP)
	# maxdb1 = 20 * math.log10( maxm1 )
	K:float = CC*gm*RL*rpi
	T_max:float = K * w_3dB

	ans_string:str = f"""
FIG 7.13, small-signal equivalent circuit.

For the input-side, since capacitor CC is in series between the input Vi
and output Vpi terminals, it behaves as:
  * a coupling capacitor
  * a high-pass filter (HPF).

This is well known, time-constant:

  tau = (RS + rpi)CC sec
      = ({RS} + {rpi})*{CC}
  tau = {tRC}s.

Corner frequency (f-3dB):
  f = 1 / (2 * pi * tau)
    = 1 / (2 * pi * {tRC})
  f-3dB = {f_3dB}Hz.
  w-3dB = {w_3dB}rad.

To calculate the maximum-gain asymptote, write the equations
for the circuit and then substitute the input-side equation
into the output-side equation.

Input-side: voltage-divider

  Vpi = [ rpi / (RS + (1/sCC) + rpi) ] * Vi

Output-side: current thru RL

  Vo = -(gm * Vpi)RL

Substitute for Vpi in output equation, then take ratio Vo/Vi
for transfer function.

  Vo = -(gm*RL)*Vpi
     = -(gm*RL) * [ rpi / (RS + (1/sCC) + rpi) ] * Vi
     = -(gm*RL*rpi) * [ 1 / (RS + (1/sCC) + rpi) ] * Vi
Multiply right-hand side by (sCC/sCC) = 1.

  Vo = -(sCC*gm*RL*rpi) / ( sCC*RS + 1 + sCC*rpi ) * Vi
     = -(sCC*gm*RL*rpi) / ( sCC*(RS + rpi) + 1 ) * Vi    (1)

where:
  tau = (RS + rpi)CC, and
  K = constant = CC*gm*RL*rpi

Per (1) rearranged,

	Vo = -(sCC*gm*RL*rpi) / ( s*(RS + rpi)CC + 1 ) * Vi
     = -Ks / (s*tau + 1) * Vi

  **> T(s) = Vo / Vi = -Ks / (s*tau + 1)

  **> T(jw) = -Kjw / (jw*tau + 1)   Eq 7.8 pg 474

To calculate magnitude of the Gain-transfer function,
mag(jw) is just w at 90deg, so mag = w.
mag(jw*tau + 1) = sqrt( 1^2 + (w*tau)^2 )

  **> |T(w)| = K * [ w / sqrt( 1^2 + (w*tau)^2 ) ]
             = K * [ w / sqrt( 1 + (w*tau)^2 ) ]

At max-freq w = infinity, the ratio of omegas = 1,
therefore, the

  K = {CC}*{gm}*{RL}*{rpi}
  |T(w)| max = K * w-3dB.
             = {K} * {w_3dB}
  |T(w)| max = {T_max}.
"""
	print( ans_string )

	# print( '\n---- (a) ----' )

	# try:
	# 	assert_within_percentage( calc_result, ans, assert_percentage )
	# 	print( f"ASSERT ID = {calc_result}A is within {assert_percentage}% of accepted answer: {ans}." )
	# except AssertionError as e:
	# 	print( f"AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )



# Maximum magnitude asymptotes:
#   RP / (RS + RP)
#   {RP} / ({RS} + {RP}) = {maxm1}
# -OR-
#   20log( RP / (RS + RP) ) = {maxdb1}dB.
