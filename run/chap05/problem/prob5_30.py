from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob5_30(self):
	"""Page 357:
	The circuit shown in Figure P5.30 is to be designed such that ICQ = 0.8mA
	and VCEQ = 2V for the case when (a) RE = 0 and (b) RE = 1kΩ. Assume
	β = 80. (c) The transistor in Figure P5.30 is replaced with one with
	a value	of β = 120. Using the results of parts (a) and (b), determine
	the Q-point	values ICQ and VCEQ. Which design shows the smallest change
	in Q-point values?
	ANS(a): (i) 1.03μA, (ii) 2.25mA
	ANS(b): (i) 0.0103μA, (ii) 22.5μA
	ANS(c): (i) 0.0103μA, (ii) 22.5μA.
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
	ans:float = 0

	# ---- Givens --------------------
	ICQ:float = 0.8e-03   # A
	VCEQ:float = 2   # V
	VCC:float = 5    # V
	VEE:float = 0    # V
	VBB:float = 2      # V
	RE_a:float = 0     # Ω
	RE_b:float = 1000  # Ω
	Beta_a:float = 80
	Beta_b:float = 120

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V
	VB_a:float = VBB - VBE  # since RE = 0, emitter at ground

	# ---- Calcs (a) ---------------------
	calc_VRB_a:float = VBB - VBE
	calc_RB_a:float = Beta_a * calc_VRB_a / ICQ
	calc_RC_a:float = (VCC - VCEQ) / ICQ

	# ---- Calcs (b) ---------------------
	# Alpha:float = Beta_a / ( 1 + Beta_a )
	calc_IB_b:float = ICQ / Beta_a
	calc_IE_b:float = ( 1 + Beta_a ) * calc_IB_b
	calc_IE_b = round(calc_IE_b,6)

	calc_VRE_b:float = calc_IE_b * RE_b
	calc_VRE_b = round(calc_VRE_b,3)

	calc_VRB_b:float = VBB - VBE - calc_VRE_b
	calc_RB_b = calc_VRB_b / calc_IB_b
	calc_RB_b = round(calc_RB_b,0)

	calc_VRC_b:float = VCC - VCEQ - calc_VRE_b
	calc_RC_b:float = calc_VRC_b / ICQ


	ans_string:str = f"""
With RE = {RE_a}Ohm, the KVL for BE-junction circuit is relatively simple:

  VBB - VB - VBE = 0, therefore, voltage-drop across RB:

  VRB = VBB - VBE
      = {VBB} - {VBE}
      = {calc_VRB_a}V.

The current through RB is forced.

  IRB = IB = VRB / RB

For any transistor, IC = Beta * IB.  With Beta and ICQ given,
and IRB(=IB) equation in terms of RB:

  ICQ = Beta * VRB / RB, solve for RB:
  RB = Beta * VRB / ICEQ
     = {Beta_a} * {calc_VRB_a} / {ICQ}
     = {calc_RB_a}ohm.

To calculate RC, just use the voltage-drop across it using ICQ.		 

  ICQ = (VCC - VCEQ) / RC
   RC = (VCC - VCEQ) / ICQ
      = ({VCC} - {VCEQ}) / {ICQ}
      = {calc_RC_a}ohm.


With RE = {RE_b}ohm,
  IB = ICQ / Beta = {ICQ} / {Beta_a}
     = {calc_IB_b}A.
  IE = ( 1 + Beta ) * IB
     = ( 1 + {Beta_a} ) * {calc_IB_b}
     = {calc_IE_b}A.

The KVL for BE-junction circuit is:

  VBB - VRB - VBE - VRE = 0,
    where
    VRB = IB * RB  -AND-  VRE = IE * RE

  VRE = IE * RE = {calc_IE_b} * {RE_b}
      = {calc_VRE_b}V.

Solve for VRB:
  VBB - VRB - VBE = VRE
  VRB = {VBB} - {VBE} - {calc_VRE_b}
      = {calc_VRB_b}V.

Such that RB = VRB / IB.
  RB = {calc_VRB_b} / {calc_IB_b}
     = {calc_RB_b}ohm.

The KVL for CE-junction circuit is:

  VCC - VRC - VCEQ - VRE = 0,
    where
    VRC = ICQ * RC  -AND-  VRE = IE * RE

Solve for RC:
  VRC = VCC - VCEQ - VRE
      = {VCC} - {VCEQ} - {calc_VRE_b}
      = {calc_VRC_b}

  RC = VRC / ICQ
     = {calc_VRC_b} / {ICQ}
     = {calc_RC_b}ohm.
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
