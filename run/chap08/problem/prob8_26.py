from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.equations import current_divider


def prob8_26(self):
	"""Page 609:
	A simplified class-AB output stage with BJTs is shown in Figure 8.24.
	The circuit parameters are VCC = 5V and RL = 1k. For each transistor,
	IS = 2e-15A.
	(a) Determine the value of VBB that produces iCn = iCp = 1mA when
	vI = 0. What is the power dissipated in each transistor?
	(b) For vO = -3.5V, determine iL , iCn, iCp, and vI . What is the
	power dissipated in Qn, Qp, and RL ?
	Thu, May  1, 2025  6:03:54 PM"
	ANS: (a)  VBB = 2VBE = 1.40077V, PQ = 5mW
			 (b)  iL=3.5mA, iCn=0.2857mA, ."
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

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  η

	# ---- Answers -------------------
	ans:float = 0

	# ---- Givens --------------------
	VCC:float = 5
	VCE:float = 5
	iCn:float = 1e-03
	iCp:float = 1e-03
	RL:float = 1e+03
	IS:float = 2e-15   # A
	calc_result:float = 0

	# ---- Assumptions ---------------
	VT:float = self._vthrml0_026   # V

	# ---- Calcs ---------------------
	VBE:float = VT * math.log(iCn/IS)
	VBB:float = 2 * VBE
	VBB = round(VBB,5)

	PQn:float = iCn * VCE

	ans_string:str = f"""
---- (Calc VBB) ----
In this basic schematic, Qn and Qp individually operate as an emitter
follower.

With IS and iCn given, the quiescent collector currents in each
transistor are given by:

  iCn = iCp = IS * exp(VBE/VT)   (1)

  where VT is thermal voltage 0.026V.

  Divide (1) by IS and take the log both sides to isolate VBE.

  iCn / IS = exp(VBE/VT)
  ln(iCn/IS) = VBE / VT

  VBE = VT * ln(iCn/IS)
      = {VT} * ln({iCn}/{IS})
  VBE = {VBE}V.

  VBB = 2VBE = 2 * VBE = {VBB}V.

---- (Calc power dissipation) ----
The power dissipation in the transistor at Q-point, neglecting the base
current, is the product of the collector current and VCE.
With Qn biased to the edge of conduction, the power is:

  PQn = iCn * VCE
      = {iCn} * {VCE}
  PQn = {PQn}W.

"""
	print( ans_string )

	# print( '\n---- (a) ----' )

	try:
		assert_within_percentage( calc_result, ans, assert_percentage )
		print( f"ASSERT ID = {calc_result}A is within {assert_percentage}% of accepted answer: {ans}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )


