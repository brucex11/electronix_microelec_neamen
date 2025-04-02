from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations import equations

def prob6_44cd(self):
	"""Page 459:
	The transistor parameters for the circuit in Figure P6.44 are β = 180
	and	VA = inf.  Assume ideal Q1.
	See ./docx/chap06/problem/chap06_prob6_44c.docx for Figures.
	(a) Find ICQ and VCEQ.
	(b) Plot the dc and ac load lines.
	(c) Calculate the small-signal voltage gain.
	(d) Determine the input and output resistances Rib and Ro.
	ANS(a):  ICQ = 15.6mA, VCEQ = 10.1V
	ANS(c):  rpi = 300Ω, Rib = 34237.5Ω, Av = 0.806
	ANS(d):  Ro = 6.18Ω
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

	#  α   β   Ω   μ   λ   γ   ξ   ω

	# ---- Answers -------------------
	ans_rpi = 0.3e+03      # V
	ans_Av = 0.806

	# ---- Givens --------------------
	given_ICQ = 15.6e-03   # A
	Beta:float = 180
	# VCC:float = 9
	# VEE:float = -9
	R1:float = 10000
	R2:float = 10000
	RS:float = 1000
	RE:float = 500
	RL:float = 300


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V
	list_3rs:List[float] = [500,500,500]


	# ---- Calcs ---------------------
	# Q's input resistance, Rib
	rpi:float = (Beta * self._vthrml0_026 ) / given_ICQ
	RE_pllel_RL:float = equations.r1_parallel_r2( RE, RL )
	# REzf, emitter-resistance due to impedance-reflection
	REzf:float = (1 + Beta) * RE_pllel_RL
	Rib:float = rpi + REzf

	# Circuit transistor's base-resistance; this is different than Rib;
	# this is the circuit resistance with respect to the source signal.
	# Small-signal equivalent-circuit input resistance, Ri.
	list_3rs:List[float] = [R1,R2,Rib]
	Ri:float = equations.equivalent_parallel_resisitance( list_3rs )
	Ri = round(Ri,0)
	calc_gm:float = Beta / rpi

	# Just plug in eq from solution manual:
	calc_Req_Av:float = Ri / ( Ri + RS )
	# calc_Av_numer:float = ( 1 + Beta ) * RE_pllel_RL
	# calc_Av_denom:float = ( 1 + Beta ) * RE_pllel_RL
	# calc_Av:float = ( REzf / Rib ) * calc_Req_Av
	# calc_Av:float = Beta * RE_pllel_RL / Ri
	calc_Av:float = ( REzf / Rib ) * ( Ri / (RS + Ri) )
	# calc_Av:float = ( REzf / (rpi + REzf) ) * ( Ri / (RS + Ri) )

  # Ro
	list_3rs:List[float] = [RS,R1,R2]
	calc_parallel_RS_R1_R2:float = equations.equivalent_parallel_resisitance( list_3rs )
	calc_parallel_RS_R1_R2 = round(calc_parallel_RS_R1_R2,0)
	Rlkb:float = rpi + calc_parallel_RS_R1_R2
	RBzf:float = Rlkb / (1 + Beta)
	# calc_RO_thev_R:float = (rpi + calc_parallel_RS_R1_R2) / (1 + Beta)
	Ro:float = equations.r1_parallel_r2( RE, RBzf )


	ans_string:str = f"""
The AC small-signal voltage gain, Av = Vo/Vs, of the circuit is defined
as the ratio of output signal voltage to input signal voltage.

Av depends on the following circuit factors:
  * voltage/signal source resistance
  * transistor DC Q-point
    - to determine transistor base-resistance, rpi
  * transistor Beta
    - to determine circuit base input-resistance, Rib
    - note: Beta does vary (slightly) with Q-point
  * effective emitter-resistance

Transistor base-emitter resistance, rpi:
  * also known as 'diffusion resistance'
  * is a function of the Q-point current

  rpi = VT / IBQ
      = (Beta * VT) / ICQ   Eq 6.22 page 379
        where VT = {self._vthrml0_026}V at room temp.

Since ICQ has been calculated per part (a) of this problem,
ICQ = {given_ICQ}A.

  rpi = ({Beta} * {self._vthrml0_026} ) / {given_ICQ}
      = {rpi}ohm.

To determine the transistor's input resistance Rib 'looking' into its base,
use the AC small-signal equivalent circuit and 'impedance reflection' to
perform the calculation.

  REzf = emitter resistance due to impedance-reflection
       = (1 + Beta) * (effective emitter-resistance)
       = (1 + Beta) * RE||RL
       = (1 + {Beta}) * {RE_pllel_RL}
       = {REzf}ohm.

    where effective emitter-resistance = RE||RL because capacitor CC2
    acts like a short for AC small-signal equivalent circuit.

    Then, Rib is simply the sum of rpi and REzf:
      Rib = rpi + REzf
          = {rpi} + {REzf}
          = {Rib}ohm.

The voltage source (Vs in series with Rs) 'looking-in' sees 3 resistors
in parallel; hence the input resistance, Ri:

  Ri = R1||R2||Rib
     = {R1}||{R2}||{Rib}
     = {Ri}ohm.

Av = small-signal voltage gain is defined as Vo / Vs (phasor notation).
Av is the product of two ratios:

  1) REzf / Rib
     where:
     REzf = emitter-resistance due to impedance-reflection
          = (1 + Beta) * RE||RL
     Rib = total input resistance at the base-terminal
         = rpi + emitter-resistance due to impedance-reflection
         = rpi + REzf

  2) Ri / (RS + Ri)
     where:
     Ri = see above
     RS = voltage source resistance

  Av = ( REzf /     Rib )      X ( Ri / (RS + Ri) )
     = ( REzf / (rpi + REzf) ) X ( Ri / (RS + Ri) )
     = ( {REzf} / ({rpi} + {REzf}) ) X ( {Ri} / ({RS} + {Ri}) )
     = {calc_Av}.

To determine output resistance, Ro, use impedance-reflection (analagous
to Ri determination) to 'look-back' from the emitter-terminal all the way
to the signal-source (that is an AC short-circuit).
This 'looks' like rpi in series with the 3 resistors at the node connecting
the source resistor RS and the base-bias voltage-divider resistors R1 and R2.
Since Vs is an AC-equivalent short:

  Rlkb = rpi + RS||R1||R2
       = {rpi} + {RS}||{R1}||{R2}
       = {rpi} + {calc_parallel_RS_R1_R2}
       = {Rlkb}ohm.

Then, per impedance-reflection, simply divide Rlkb by (1+Beta):

  RBzf = Rlkb / (1+Beta)
       = {Rlkb} / (1+{Beta})
       = {RBzf}ohm.

Finally, Ro from the perspective of the emitter-terminal is RE in parallel
with RBzf:

  Ro = RE || RBzf
     = {RE} || {RBzf}
     = {Ro}ohm.

Note that the output resistance Ro is ~= emitter-terminal reflection-impedance
since reflection-impedance << RE.
"""
	print( ans_string )


	try:
		assert_within_percentage( rpi, ans_rpi, assert_percentage )
		print( f"ASSERT rpi = {rpi}ohm is within {assert_percentage}% of accepted answer: {ans_rpi:.3e}ohm." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	try:
		assert_within_percentage( calc_Av, ans_Av, assert_percentage )
		print( f"ASSERT Av = {calc_Av}ohm is within {assert_percentage}% of accepted answer: {ans_Av}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	print( f"--- END {self.prob_str} ---" )
