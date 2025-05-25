from inspect import currentframe
from math import trunc
from typing import List, Dict  # Any, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.current import current_divider
from equations.voltage import voltage_divider


def prob6_04(self):
	"""Page 451:
	The transistor in Figure 6.3 has parameters β = 120 and VA = inf.
	The circuit parameters are VCC = 3.3V, RC = 15kΩ, and ICQ = 0.12mA.
	A small signal vbe = 5sinωt mV is applied.
	(a) Determine iC and vCE.
	(b) What is the small-signal voltage gain Av = vce/vbe?
	Wed, Apr 16, 2025 12:20:00 PM
	ANS: (a) iC = (0.12 + 2.31e-05sin(wt))mA, vCE = 1.5 - 0.3465sin(wt)V
			 (b) Av = vce/vbe = -69.3.
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
	BetaDC:float = 120
	Avbe:float = 5e-03   # sine Amplitude Asinωt
	vbe_str:str = f"sin(wt)"
	VA:str = 'inf'    # V
	VCC:float = 3.3
	VEE:float = 0
	ICQ:float = 0.12e-03  # A
	# VBB:float = -1
	RC:float = 15e+03
	calc_result:float = 0

	# ---- Assumptions ---------------
	VBE:float = 0.6   # V

	# ---- Calcs (a) -----------------
	gm:float = ICQ / self._vthrml0_026
	gm = round(gm,6)

	A:float = gm * Avbe
	A = round(A,7)

	VCEQ:float = VCC - (ICQ * RC)
	VCEQ = round(VCEQ,1)

	iCXRC:float = A * RC

	Av:float = -(iCXRC / Avbe)

	ans_string:str = f"""
---- (a) ----
Per Eq 6.13b page 377, iC = ICQ + ic, where:

  ic = (gm * vbe)
  iC = ICQ + (gm * vbe).

gm = ICQ / VT
   = {ICQ} / {self._vthrml0_026}
gm = {gm}A/V = {to_s_mA(gm,3)}/V.

ic = {A}A = {to_s_mA(A,6)}, and

  **> iC = ({round(ICQ*1000,6)} + {A}{vbe_str})mA.

To calculate vce, use KVL for C-E branch.

  vce = VCEQ - (iC * RC).

VCEQ = VCC - (ICQ * RC)
     = {VCC} - ({ICQ} * {RC})
VCEQ = {VCEQ}V.

iC * RC = {A} * {RC}
iC * RC = {iCXRC}

      vCE = VCEQ - (iC * RC)
  **> vCE = {VCEQ} - {iCXRC}{vbe_str}V.

---- (b) ----
    Av = -(vce / vbe)
    = -({iCXRC} / {Avbe})
**> Av = {Av}.
"""
	print( ans_string )


	# ---- Calcs (RB) ----------------
	IBQ:float = ICQ / BetaDC

	VBB_range:List[float] = [round(0.9 + i * 0.04, 2) for i in range(31)]  # 21 values from 0.2 to 2.2
	# list_RB:List[float] = []
	dict_VBB_RB:Dict[str,str] = {}

	for VBB in VBB_range:
		RB:float = (VBB - VBE) / IBQ
		RB = int(round(RB,0))
		# prep for Dict entry
		RB_str:str = f"{to_s_k(RB,0)}k"
		dict_VBB_RB[f"{VBB}V"] = RB_str

	ans_string = f"""
---- (calc RB) ----
Assume VBE = {VBE}V in active-region.

IBQ = ICQ / BetaDC
    = {ICQ} / {BetaDC}
IBQ = {IBQ}uA.

Iterate the VBB using IBQ to find a suitable RB.
"""
	print( ans_string )

	for vbb, rb in dict_VBB_RB.items():
		print(f"{vbb}: {rb}")

	ans_string = f"""
---- (LTspice) ----
Per the simulation, see folder ./LTspice/chap06/prob6_04/,
VBE = 0.6V

So the VBE original 0.7V was changed to 0.6; this was rerun
to generate new VBB:RB pairs.

Using 1.3V:700k, ICQ and IBQ are dead-on to the given and calculated.

Per simulation:

  Av = vc / vb = 688m / 10m = 68.8 (p-p)
  Ai = ic / ib = 46u / 388n = 118.5 (p-p).
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
