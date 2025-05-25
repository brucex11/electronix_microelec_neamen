from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance, r1_parallel_r2
from equations.current import current_divider
from equations.voltage import voltage_divider


def prob6_56D(self):
	"""Page 462:
	(a) For the emitter-follower circuit in Figure P6.54, assume VCC = 24V,
			β = 75, and Ai = io/is = 8. Design the circuit to drive an 8Ω load.
	(b) Determine the maximum undistorted swing in the output voltage.
	(c) Determine the output resistance Ro.
	Fri, Apr 11, 2025 11:17:55 PM
	ANS:  (a) ./LTspice/chap06/prob6_56D/
				(b) max-swing
			  (c) Ro = .
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
	VCC:float = 24   # V
	Beta:float = 75
	RL:float = 8     # Ω
	Ai:float = 8

	# ---- Assumptions ---------------
	RE:float = 24   # Ω
	VCEQ = VCC / 2  # V


	print( '---- Calc Q-point currents ----', end='' )
	IEQ:float = VCEQ / RE
	IBQ:float = IEQ / ( 1 + Beta )
	IBQ = round(IBQ,6)
	ICQ:float = IEQ - IBQ
	ICQ = round(ICQ,3)

	rpi:float = self._vthrml0_026 / IBQ
	rpi = round(rpi, 2)

	ans_string:str = f"""
Let RE = {RE}ohm, VCEQ = {VCC} / 2 = {VCEQ}V.

Calc IEQ based on assumed RE value:
  IEQ = VCEQ / RE
      = {VCEQ} / {RE}
      = {IEQ}A.

Calc IBQ and ICQ.
  IBQ = IEQ / (1 + Beta)
      = {IEQ} / (1 + {Beta})
      = {to_s_mA(IBQ,5)}.
  ICQ = IEQ = IBQ
      = {IEQ} = {IBQ}
      = {ICQ}A.

Calc rpi based on Q-point IBQ:
  rpi = VT / IBQ
      = {rpi}ohm.
"""
	print( ans_string )


	print( '---- Calc small-signal values ----', end='' )
	RE_p_RL:float = r1_parallel_r2( RE, RL)
	RE_eff:float = (1 + Beta) * RE_p_RL   # emitter-node effective AC resistance
	Rib:float = rpi + RE_eff
	Rib = round(Rib, 0)

	# IRLQ:float = current_divider( RL, RE, (1+Beta)*IBQ )
	# RTh:float = 75
	# Aii:float =  ( (1 + Beta) * ( RE / (RE + RL) )) * (RTh / (RTh + Rib) )

	Ai_num:float = (1 + Beta) * ( RE / (RE + RL) )  # numerator
	Ai_div:float = Ai / Ai_num
	Ai_div = round(Ai_div,4)

	RTh:float = -1.0 * ( Ai_div * Rib ) / ( Ai_div - 1 )
	RTh = round(RTh,1)

	ans_string:str = f"""
Calc Q input impedance RiB using impedance-reflection:
  Rib = rpi + (1 + Beta) * (RE||RL)
      = {rpi} + (1 + {Beta}) * ({RE_p_RL})
      = {rpi} + {RE_eff}
      = {Rib}ohm.

Since Ai is given ({Ai}) and Ai =  Io / Is, use it to
to determine the RTh resistance for the INPUT circuit
where RTh = (R1||R2).

To determine the current Io through load resistor RL,
use KCL current-divider for the OUTPUT circuit:

  (1 + Beta)*Ib = IRE + IRL
  Io = IRL = (1 + Beta)*Ib * ( RE / (RE + RL) )

Do the same for the INPUT circuit to find Is:

  Is = Ib + I*(R1||R2)
  Is = Ib + I*(RTh)
  Current divider:
  Ib = ( (RTh) / (RTh) + Rib) ) * Is
	Is = Ib / ( (RTh) / (RTh) + Rib) )

Calc RTh:

  Ai = Io / Is
  Ai =                   Io                 /               Is
     = [(1 + Beta)*Ib * ( RE / (RE + RL) )] / [Ib / ( RTh / (RTh + Rib) )]

Ib in equation above cancels.

  Ai = [(1 + Beta) * ( RE / (RE + RL) )] / [1 / ( RTh / (RTh + Rib) )]
  Ai = [(1 + Beta) * ( RE / (RE + RL) )] * [RTh / (RTh + Rib)]

Solve for minumum RTh.

  Ai = [(1 + Beta) * ( RE / (RE + RL) )] * [RTh / (RTh + Rib)]
  Ai = [(1 + {Beta}) * ( {RE} / ({RE} + {RL}) )] * [RTh / (RTh + {Rib})]
  {Ai}  = {Ai_num} * [RTh / (RTh + {Rib})]

  {Ai_div} = [RTh / (RTh + {Rib})]

  RTh(min) = {RTh}ohm.
"""
	print( ans_string )


	# try:
	# 	assert_within_percentage( calc_result, ans, assert_percentage )
	# 	print( f"ASSERT ID = {calc_result}A is within {assert_percentage}% of accepted answer: {ans}." )
	# except AssertionError as e:
	# 	print( f"AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )
