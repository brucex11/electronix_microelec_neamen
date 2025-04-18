from inspect import currentframe
from math import trunc
from typing import List, Dict  # Any, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.equations import current_divider


def prob6_19(self):
	"""Page 451:
	Consider the circuit shown in Figure P6.19 where the signal-source is
	vs = 4sinωt mV. (a) For transistor parameters of β = 80 and VA = inf,
	(i) find the small-signal voltage gain Av = vo/vs and the transconductance
	function Gf = io/vs , and (ii) calculate vo(t) and io(t).
	(b) Repeat part (a) for β = 120.
	Thu, Apr 17, 2025  4:03:33 PM
	ANS: (a) (i)  Av = -26.97, Gf = io / vs = -5.39mA/V
	     (a) (ii) vo = -0.108sinωt V, io = -21.6sinωt μA
			 (b) (i)  Av = -30.5, Gf = io / vs = -6.1mA/V
	     (b) (ii) vo = -0.122sinωt V, io = -24.4sinωt μA.
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

	# ---- Givens (a) ----------------
	BetaDC:float = 80
	A_Vs:float = 4e-03   # sine Amplitude Asinωt
	vs_sinwt:str = f"sin(wt)"
	VA:str = 'inf'    # V
	VEE:float = 5
	VCC:float = -5
	RE:float = 10e+03
	RC:float = 5e+03
	RS:float = 2.5e+03
	RL:float = 5e+03

	# ---- Assumptions ---------------
	VEB:float = 0.7   # V

	# ---- Calcs (a) -----------------
	IBQ:float = ( VEE - VEB) / ( (1 + BetaDC) * RE + RS )
	ICQ = BetaDC * IBQ

	gm:float = self.calc_gm( ICQ )
	rpi:float = self.calc_rpi( IBQ )

	RC_p_RL:float = r1_parallel_r2( RC, RL )
	Av:float = -(( rpi / (rpi + RS) ) * gm * (RC_p_RL))
	io:float = (Av * A_Vs) / RL
	Gf:float = io / A_Vs


	ans_string:str = f"""
---- (a)(i) Av and Gf ----
Per the circuit shown in Figure P6.19, calculate IBQ using KVL
for the Q1 B-E branch.

  KVL: VEE - VRE - VEB - VRS = 0
           - VRE       - VRS = -VEE + VEB
           -(IEQ*RE) - (IBQ*RS) = -VEE + VEB

Solve for IBQ where IEQ = (1 + BetaDC)*IBQ.

  -(1 + BetaDC)IBQ*RE - IBQ*RS = -VEE + VEB
   (1 + BetaDC)IBQ*RE + IBQ*RS =  VEE - VEB
   IBQ[(1 + BetaDC)*RE + RS] =  VEE - VEB

  IBQ = ( VEE - VEB) / ( (1 + BetaDC) * RE + RS )
      = ( {VEE} - {VEB}) / ( (1 + {BetaDC}) * {RE} + {RS} )
  IBQ = {IBQ}A.

  ICQ = BetaDC * IBQ
      = {BetaDC} * {IBQ}
  ICQ = {ICQ}A.

  Q1 gm  = {gm} = {to_s_mA( gm, 3)}/V.
  Q1 rpi = {rpi} = {to_s_k(rpi,3)}k.

Per AC small-signal equivalent circuit, determine the voltage
gain Av and the tranconductance function Gf.
Recall that capacitors are shorts to sinusoidal signals,
so RE not in small-signal equivalent circuit, and also output
resistance is (RC||RL).

Voltage-divider on input, then substitute into equation for output.

INPUT
  Vpi = ( rpi / (rpi + RS) ) * Vs

OUTPUT
  Vo = -(Vpi * gm) * (RC||RL)

GAIN, substitute INPUT Vpi into OUTPUT equation.
  Vo = -(( rpi / (rpi + RS) ) * Vs  * gm * (RC||RL))
  Av = Vo / Vs
     -(( rpi / (rpi + RS) ) * gm * (RC||RL))
     -(( {rpi} / ({rpi} + {RS}) ) * {gm} * ({RC}||{RL}))
     -(( {rpi} / ({rpi} + {RS}) ) * {gm} * ({RC_p_RL}))
   Av = {Av}.

The transconductance function Gf = io/vs, therefore calculate io.

  io = vo / RL
     = (Av * vs) / RL
     = ({Av} * {A_Vs}) / {RL}A.
  io = {io} = {to_s_mA(io, 3)}.

Finally,

  Gf = io / vs
     = {to_s_mA(io, 3)} / {A_Vs}V
  Gf = {Gf} = {to_s_mA(Gf,3)}/V.
"""
	print( ans_string )


	# ---- Calcs signals out ----
	Ao:float = Av * A_Vs
	Ao = round(Ao,3)

	io:float = Gf * A_Vs


	ans_string = f"""
---- (a)(ii) output signals ----
Calculate the OUTPUT AC signals vo and io.

  vo = Av * vs
     = {Av} * {A_Vs}{vs_sinwt} V
  vo = {Ao}{vs_sinwt} V.

  io = Gf * vs
     = {Gf}A/V * {A_Vs}{vs_sinwt} V
     = {io}{vs_sinwt}A.
  io = {to_s_uA(io,6)}{vs_sinwt}uA.
"""
	print( ans_string )


	print( f"--- END {self.prob_str} ---" )
