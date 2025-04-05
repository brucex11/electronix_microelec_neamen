from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage


def exer5_04(self):
	"""Page 306:
	The circuit elements in Figure 5.22(a) are V+ = 3.3V, VBB = 1.2V,
	RB = 400kΩ, and RC = 5.25kΩ. The transistor parameters are β = 80 and
	VEB(on) = 0.7V. Determine IB, IC, and VEC.
	Thu, Apr  3, 2025  6:26:00 PM
	ANS:  IB = 3.5μA, IC = 0.28mA, VEC = 1.83V.
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
	VEE:float = 3.3
	VBB:float = 1.2
	RB:float = 400e+03
	RC:float = 5.25e+03
	Beta:float = 80
	VEB:float = 0.7   # V

	# ---- Calcs ---------------------
	VB:float = VEE - VEB
	VB = round(VB,1)

	IRB:float = (VB - VBB) / RB
	IRB = round(IRB,9)

	IC:float = Beta * IRB
	IC = round(IC,6)
	IE:float = IRB + IC
	IE = round(IE,6)

	VC:float = IE * RC
	VCE = VEE - VC

	# confirm bias in active-region
	VE_gt_VB:float = VEE - VB
	VB_gt_VC:float = VB - VC

	ans_string:str = f"""
With the given schematic and circuit parameters, start by
assuming active-mode for this PNP BJT.
For PNP active mode, bias voltages must be in this range:
VE > VB > VC.
Which means that the B-E junction is forward=biased and the
C-B junction is reverse-biased.

Voltage at base-terminal = VEE - VEB = {VB}V.
Current thru RB = (VB - VBB) / RB = {IRB}A.

IC = Beta * IB = {Beta} * {IRB} = {IC}A.

IE = IB + IC = {IRB} + {IC} = {IE}A.

With IE now known, calc the voltage at collector-terminal.
VC = IE * RC = {IE} * {RC} = {VC}V.
Then, VCE = VEE - VC = {VEE} - {VC} = {VCE}V.
"""
	print( ans_string, end='' )


	ans_string = f"""
---- (confirm active-region bias voltages) ----
To confirm active-region of operation, check VE > VB > VC.

  {VEE} > {VB} > {VC}
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )

