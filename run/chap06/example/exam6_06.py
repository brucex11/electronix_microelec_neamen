from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.current import current_divider
from equations.voltage import voltage_divider


def exam6_06(self):
	"""Page 404:
	Objective: Analyze a pnp transistor circuit.
	Consider the circuit shown in Figure 6.32(a). Determine the quiescent parameter
	values and then the small-signal voltage gain.
	Assume the transistor parameters are: β=80, VBE=0.7V, VA=inf.
	Sat, May 24, 2025  6:52:13 AM
	ANS(DC):  ICQ = .559mA, VECQ = 1.63V
	ANS(AC):  Av = -1.93.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.2
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers -------------------
	ans_Av:float = -1.93
	ans_ICQ:float = .559e-03  # A
	ans_VECQ:float = 1.63  # V
	ans_Av:float = -1.93

	# ---- Givens --------------------
	Beta:float = 80
	VA:str = 'inf'    # V
	VCC:float = -2.5
	VEE:float = 2.5
	R1:float = 40e+03
	R2:float = 60e+03
	RC:float = 4e+03
	RE:float = 2e+03


	# ---- Assumptions ---------------
	VEB:float = .7   # V

	# ---- DC op point calcs ---------------------
	RTh:float = r1_parallel_r2( R1, R2 )
	# VTh:float = ((VEE / R1) + (VCC/R2)) / ((1/R1) + (1/R2))
	VTh:float = voltage_divider( VEE, R1, R2, VCC )
	VTh1:float = ((VEE*R2) + (VCC*R1)) / (R1 + R2)

	# IEQ:float =  ( VB - VBE - VEE ) / RE
	IBQ:float = (VEE - VEB - VTh) / ((1 + Beta)*RE + RTh)
	ICQ:float = Beta*IBQ
	IEQ:float = IBQ + ICQ
	VECQ:float = VEE - IEQ*RE - ICQ*RC - VCC
	VECQ = round(VECQ,2)

	# INPUT Z
	re:float = (self._vthrml0_026) / IEQ


	ans_string:str = f"""
---- (DC op point) ----
Calculate the Thevenin-equivalent circuit for the Q-point at the base.

'Looking-in' from the base, the resistance is R1||R2.

  RTh = Voc / Isc
  RTh = {RTh}ohm
  VTh = {VTh}V
  VTh1 = {VTh1}V.

  re = VT / IEQ
     = {self._vthrml0_026} / {IEQ}
  re = {re}ohm.


Calc Q-point current for IBQ using KVL of the Thevenin-equivalent circuit
thru the BE junction:

  VEE -  VRE -   VEB -  VRTh   - VTh = 0
  VEE - IEQ*RE - VEB - IBQ*RTh - VTh = 0

And, IEQ = IBQ + ICQ = IBQ + Beta*IBQ = (1 + Beta)*IBQ.

Substitute IEQ and solve for IBQ:

  VEE - (1 + Beta)*IBQ*RE - VEB - IBQ*RTh - VTh = 0
  (1 + Beta)*IBQ*RE + IBQ*RTh = VEE - VEB - VTh

  IBQ * ((1 + Beta)*RE + RTh) = VEE - VEB - VTh
  IBQ = (VEE - VEB - VTh) / ((1 + Beta)*RE + RTh)
      = ({VEE} - {VEB} - {VTh}) / ((1 + {Beta})*{RE} + {RTh})
  IBQ = {IBQ} = {to_s_uA(IBQ,3)}.
  ICQ = Beta*IBQ
      = {Beta}*{IBQ}
  ICQ = {ICQ} = {to_s_mA(ICQ,3)}.

Using KVL around the EC-branch/loop:

  VEE - VRE - VECQ - VRC - VCC = 0
  VECQ = VEE - IEQ*RE - ICQ*RC - VCC
       = {VEE} - {IEQ}*{RE} - {ICQ}*{RC} - {VCC}
       = {VEE} - {IEQ*RE} - {ICQ*RC} - {VCC}
  VECQ = {VECQ}V.
"""
	print( ans_string )

	try:
		assert_within_percentage( ICQ, ans_ICQ, assert_percentage )
		print( f"ASSERT ICQ = {ICQ} is within {assert_percentage}% of accepted answer: {ans_ICQ}A." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	try:
		assert_within_percentage( VECQ, ans_VECQ, assert_percentage )
		print( f"ASSERT VECQ = {VECQ} is within {assert_percentage}% of accepted answer: {ans_VECQ}V." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	# ---- AC analysis calcs ---------------------
	rπ:float = (self._vthrml0_026) / IBQ
	gm:float = ICQ / (self._vthrml0_026)

	Av:float = -(gm * RC) / (1 + ((1 + Beta ) / rπ) * RE)


	ans_string:str = f"""
---- (Solution (ac analysis)) ----
Calculate the Thevenin-equivalent circuit for the Q-point at the base.

The small-signal hybrid-π parameters are as follows:

  rπ = VT / IBQ
     = {self._vthrml0_026} / {IBQ}
  rπ = {rπ}ohm.
 
  gm = ICQ / VT
     = {ICQ} / {self._vthrml0_026}
  gm = {gm}
  gm = {to_s_mA(gm,3)}/V.

Since VA = inf, ro = inf.

Per the small-signal equivalent circuit and KVL around the BE-branch/loop:

  Vs - Vπ - VRE = 0
  Vs - Vπ - Ie*RE = 0

The current thru RE = Ie = Ib + Ic, where Beta = gm * rπ :

  Ib = Vπ / rπ
  Ic = gm * Vπ

  Ie =     Ib    +    Ic
  Ie = (Vπ / rπ) + (gm * Vπ)
  Ie = (Vπ / rπ) + ((Beta / rπ) * Vπ)

Therefore KVL around the BE-branch/loop,

  Vs = Vπ + [(Vπ / rπ) + ((Beta / rπ) * Vπ)]*RE
     = Vπ + Vπ[(1 / rπ) + (Beta / rπ)]*RE
     = Vπ + Vπ[(1 / Beta) / rπ)]*RE
  Vs = Vπ * [(1 / Beta) / rπ)]*RE

The output voltage Vo is the dependent-current times RC:

  Vo = -gm * Vπ * RC

  Av = Vo / Vs
     = (-gm * Vπ * RC) / [Vπ * [(1 / Beta) / rπ)]*RE]

The Vπ's cancel:
  Av = -(gm * RC) / (1 + ((1 + Beta) / rπ) * RE)
     = -({gm} * {RC}) / (1 + ((1 + {Beta}) / {rπ}) * {RE})
  Av = {Av}.

"""
	print( ans_string )

	try:
		assert_within_percentage( Av, ans_Av, assert_percentage )
		print( f"ASSERT Av = {Av} is within {assert_percentage}% of accepted answer: {ans_Av}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	self.lg.info( f"--- END {self.prob_str} ---" )
	print( f"--- END {self.prob_str} ---" )
