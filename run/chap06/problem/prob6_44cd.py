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
	ANS(a):  ICQ = 15.7mA, VCEQ = 10.1V
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
	VTh = 0   # by inspection
	RTh:float = equations.r1_parallel_r2( R1, R2 )
	print( f"Test equations module: Rth = {RTh}" )
	RE_pllel_RL:float = equations.r1_parallel_r2( RE, RL )
	print( f"Test equations module: RE||RL = {RE_pllel_RL}" )
	req:float = equations.equivalent_parallel_resisitance( list_3rs )
	print( f"Test equations module: R1||R2||R3 = {req}" )


	calc_rpi:float = (Beta * self._vthrml0_026 ) / given_ICQ
	calc_Rib:float = calc_rpi + (1 + Beta) * RE_pllel_RL
	list_3rs:List[float] = [R1,R2,calc_Rib]
	calc_parallel_R1_R2_Rib:float = equations.equivalent_parallel_resisitance( list_3rs )
	calc_parallel_R1_R2_Rib = round(calc_parallel_R1_R2_Rib,0)
	calc_gm:float = Beta / calc_rpi

	# Just plug in eq from solution manual:
	calc_Req_Av:float = calc_parallel_R1_R2_Rib / ( calc_parallel_R1_R2_Rib + RS )
	calc_Av_numer:float = ( 1 + Beta ) * RE_pllel_RL
	# calc_Av_denom:float = ( 1 + Beta ) * RE_pllel_RL
	calc_Av:float = ( calc_Av_numer / calc_Rib ) * calc_Req_Av

  # Ro
	list_3rs:List[float] = [R1,R2,RS]
	calc_parallel_R1_R2_RS:float = equations.equivalent_parallel_resisitance( list_3rs )
	calc_parallel_R1_R2_RS = round(calc_parallel_R1_R2_RS,0)
	calc_RO_thev_R:float = (calc_rpi + calc_parallel_R1_R2_RS) / (1 + Beta)
	calc_Ro:float = equations.r1_parallel_r2( RE, calc_RO_thev_R )


	ans_string:str = f"""
The small-signal voltage gain, Av = Vo/Vs, of the circuit is defined
as the ratio of output signal voltage to input signal voltage.

Av depends on the transistor's base-emitter resistance rpi:
  * rpi is called the diffusion resistance
  * rpi is a function of the Q-point parameters.

  rpi = VT / IBQ
      = (Beta * VT) / ICQ   Eq 6.22 page 379
        where VT = {self._vthrml0_026}V at room temp

Since ICQ has been calculated per part (a) of this problem,
ICQ = {given_ICQ}A.

  rpi = ({Beta} * {self._vthrml0_026} ) / {given_ICQ}
      = {calc_rpi}ohm.

Rib is the input resistance into the base:

  Rib = rpi + (1 + Beta) * RE||RL
      = {calc_rpi} + (1 + {Beta}) * {RE_pllel_RL}
      = {calc_Rib}ohm.

Equivalent resistance of the transitor base and the base-bias-circuit
voltage-divider:

  R1||R2||Rib = {R1}||{R2}||{calc_Rib}
              = {calc_parallel_R1_R2_Rib}ohm.

  Av = small-signal voltage gain
     = Vo / Vs  (phasor notation)
     = -(gm * RC) / ( rpi / ( rpi + RB ) )
     = {calc_Av}.

Output resistance Ro:

  Ro = RE || [ ( rpi + R1||R2||RS ) / (1 + Beta) ]
     = {calc_Ro}ohm.

"""
	print( ans_string )


	try:
		assert_within_percentage( calc_rpi, ans_rpi, assert_percentage )
		print( f"ASSERT rpi = {calc_rpi}ohm is within {assert_percentage}% of accepted answer: {ans_rpi:.3e}ohm." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	try:
		assert_within_percentage( calc_Av, ans_Av, assert_percentage )
		print( f"ASSERT Av = {calc_Av}ohm is within {assert_percentage}% of accepted answer: {ans_Av}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	print( f"--- END {self.prob_str} ---" )
