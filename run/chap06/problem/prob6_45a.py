from inspect import currentframe
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations import equations

def prob6_45a(self):
	"""Page 459:
	The transistor parameters for the circuit in Figure P6.44 are β = 120
	and	VA = inf.  Assume ideal Q1.
	See ./docx/chap06/problem/chap06_prob6_45_VCC10V.docx for Figures and note
	that VCC = 10V for this problem and not ground, and VEE = ground.
	According to LTspice (./LTspice/chap06/prob6_45/prob6_45_VCC10V_Beta120.asc),
	Q1 is biased in active-region (see answers below).
	(a) Find ICQ and VCEQ.
	(b) Plot the dc and ac load lines.
	(c) Calculate the small-signal voltage gain.
	(d) Determine the input and output resistances Rib and Ro.
	ANS(a) LTspice:   ICQ = 2.10mA, VCEQ = 3.65V
	ANS(a) textbook:  ICQ = 2.11mA, VCEQ = 3.69V
	ANS(c):  
	ANS(d):  
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
	ans_ICQ = 2.11e-03   # A
	ans_VCEQ = 3.69      # V

	# ---- Givens --------------------
	Beta:float = 120
	VCC:float = 10
	VEE:float = 0
	R1:float = 10000
	R2:float = 10000
	RC:float = 1000
	RE:float = 2000
	RS:float = 5000


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V


	print( '\n---- (calc IB, IBQ and IEQ) -----------------------' )

	RTh:float = equations.r1_parallel_r2( R1, R2 )

	VTh:float = (VCC*R2 + VEE*R1) / (R1 + R2)
	IBQ:float = -1 * ( -VTh + VBE + VEE ) / ( RTh + (1+Beta)*RE )
	ICQ:float = Beta * IBQ
	IEQ:float = IBQ + ICQ

	Iloop:float = (VCC - VEE) / (R1 + R2)

	VR1:float = Iloop * R1
	VR2:float = Iloop * R2

	ans_string:str = f"""
For ideal transistor Q1, IB = 0. Therefore the Thevenin Equivalent voltage
Vth determined by the voltage-divider circuit of R1 and R2; by inspection,
VTh = 0.

However, calculate VTh using KVL:  VCC - VR1 - VR2 - VEE = 0
where VTh is voltage for node at base of Q1 and between R1 and R2:
  VR1 = (VCC - VTh)
  VR2 = (VTh - VEE)

First, calculate the loop-current Iloop(I) by substitution into KVL equation:

  VCC - I*R1 - I*R2 - VEE = 0
  -IR1 - IR2   = -VCC + VEE
  -I(R1 + R2)  = -VCC + VEE
  -I = (-VCC + VEE) / (R1 + R2)
  I = (VCC - VEE) / (R1 + R2)
  Iloop = ({VCC} - {VEE}) / ({R1} + {R2})
  Iloop = {Iloop}A.

With loop-current now known, VTh can be calculated (and confirmed) via
the voltage-drops across/through R1 and R2.

  VR1 = Iloop * R1 = {Iloop} * {R1}
      = {VR1}V.
  VR2 = Iloop * R2 = {Iloop} * {R2}
      = {VR2}V.

Per R1, VTh = VCC - VR1 = {VCC} - {VR1} = {VCC-VR1}V.
Per R2, VTh = VR2 + VEE = {VR2} + {VEE} = {VR2+VEE}V.
VTh are equal, so confirmed.

Or, just calculate VTh using voltage-divider:

  VTh = (VCC*R2 + VEE*R1) / (R1 + R2)
      = ({VCC}*{R2} + {VEE}*{R1}) / ({R1} + {R2})
      = {VTh}V.

The Thevenin resistance RTh of the divider circuit is R1||R2 = {RTh}ohm.

Use KVL around node VB and the BE-junction:

  **>  VTh - IB*RTh - VBE - VRE - (VEE) = 0

  where VRE is the voltage-drop across RE:
        VRE = IE * RE
            = (VTh - VBE) - (VEE) Volts

Now, solve for IB and then use Beta to solve for ICQ.

  IE = (1 + Beta) * IB

and (again) per KVL:

  **>  VTh  -  IB*RTh  - VBE - VRE - (VEE) = 0
  VTh  -  IB*RTh  - VBE - (IE * RE) - (VEE) = 0
  VTh  -  IB*RTh  - VBE - ((1 + Beta) * IB * RE) - (VEE) = 0
  -IB*RTh  - IB*((1 + Beta) * RE)  =  -VTh + VBE + (VEE)

  IB = -VTh + VBE + (VEE) / ( RTh + (1+Beta)*RE )
  IB = {VTh} - {VBE} -({VEE}) / ( {RTh} + (1+{Beta})*{RE} )
     = {IBQ}A.

  ICQ = Beta * IBQ = {Beta} * {IBQ}
      = {ICQ}A.
  IEQ = IBQ + ICQ = {IBQ} * {ICQ}
      = {IEQ}A.
"""
	print( ans_string )

	try:
		assert_within_percentage( ICQ, ans_ICQ, assert_percentage )
		print( f"ASSERT ICQ = {ICQ:.3e}A is within {assert_percentage}% of accepted answer: {ans_ICQ:.3e}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	print( '\n---- (VCEQ) ----------------------------------------' )

	VRC:float = ICQ * RC
	VRE:float = IEQ * RE
	VCEQ:float = VCC - VRC - VRE - VEE
	VCEQ = round(VCEQ,1)

	ans_string = f"""
Use KVL through CE-junction:

  **>  VCC - VRC - VCEQ - VRE - VEE = 0
 
where VRC = ICQ * RC
          = {ICQ} * {RC}.
          = {VRC}V.

and VRE = IEQ * RE
        = {IEQ} * {RE}.
        = {VRE}V.

  VCC - VRC - VCEQ - VRE - VEE = 0
  {VCC} - {VRC} - {VCEQ} - {VRE} - {VEE} = 0

  VCEQ = (VCC) - (VRC) - (VRE) - (VEE)
       = ({VCC}) - ({VRC}) - ({VRE}) - ({VEE})
       = {VCEQ}V.
"""
	print( ans_string )

	try:
		assert_within_percentage( VCEQ, ans_VCEQ, assert_percentage )
		print( f"ASSERT VCEQ = {VCEQ:.3e}V is within {assert_percentage}% of accepted answer: {ans_VCEQ:.3e}V." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	print( f"--- END {self.prob_str} ---" )
