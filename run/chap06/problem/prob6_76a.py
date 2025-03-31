from inspect import currentframe

from equations.equations import r1_parallel_r2


def prob6_76a(self):
	"""Page 466:
	Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(a) Determine the small-signal parameters gm, rπ, and ro for both transistors.
	(b) Plot the dc and ac load lines for both transistors.
	(c) Determine the overall small-signal voltage gain Av = vo/vs.
	(d) Determine the input resistance Ris and the output resistance Ro.
	(e) Determine the maximum undistorted swing in the output voltage.
	ANS(a):  gm1 = 22mA/V, rpi1 = 5451.0Ω, ro1 = inf
					 gm2 = 187mA/V, rpi2 = 642.0Ω, ro2 = inf
	ANS(c):  
	ANS(d):  
	ANS(e):  
	Mon, Mar 31, 2025 12:03:39 PM
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers -------------------
	ans_ICQ = 15.7e-03   # A
	ans_VCEQ = 10.1      # V

	# ---- Givens --------------------
	Beta:float = 120  # both Q1 and Q2
	VCC:float = 12
	VEE:float = 0

	# Q1
	R1:float = 67.3e+03
	R2:float = 12.7e+03
	RC1:float = 10000
	RE1:float = 2000

	# Q2
	R3:float = 15e+03
	R4:float = 45e+03
	RE2:float = 1.6e+03

	# Load
	RL:float = 250


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V


	print( '\n---- (calcs for Q1) ------------------------------' )

	RTh1:float = r1_parallel_r2( R1, R2 )
	RTh1 = round(RTh1,0)
	VTh1:float = VCC * R2 / ( R1 + R2 )

	# KVL thru BE-junction
	IBQ1:float = -1 * ( -VTh1 + VBE + VEE ) / ( RTh1 + (1+Beta)*RE1 )
	IBQ1 = round(IBQ1,8)
	ICQ1:float = Beta * IBQ1
	ICQ1 = round(ICQ1,6)
	IEQ1:float = IBQ1 + ICQ1
	IEQ1 = round(IEQ1,6)

	# KVL thru CE-junction
	VRC1:float = ICQ1 * RC1
	VRE1:float = IEQ1 * RE1
	VCEQ1:float = VCC - (VRC1) - (VRE1) - VEE

	# Q1 transconductance, rpi, ro
	gm1:float = ICQ1 / self._vthrml0_026
	rpi1:float = self._vthrml0_026 / IBQ1
	rpi1 = round(rpi1,0)


	ans_string:str = f"""
For ideal transistor Q1, IB = 0. Therefore the Thevenin Equivalent voltage
Vth determined by the voltage-divider circuit of R1 and R2.

RTh1 = R1||R2 = {RTh1}ohm
VTh1 = VCC * R1||R2 = {VTh1}V.

Use KVL thru the BE-junction:

  **>  VTh1 - IB*RTh1 - VBE - VRE1 - (VEE) = 0

  where VRE1 is the voltage-drop across RE1:
        VRE1 = IE1 * RE1
             = (VTh1 - VBE) - (VEE) Volts

Now, solve for IBQ1 and then use Beta to solve for ICQ1.

  IE1 = (1 + Beta) * IBQ1

and (again) per KVL:

  **>  VTh1  -  IB*RTh1  - VBE - VRE1 - (VEE) = 0
  VTh1  -  IBQ1*RTh1  - VBE - (IE * RE1) - (VEE) = 0
  VTh1  -  IBQ1*RTh1  - VBE - ((1 + Beta) * IB * RE1) - (VEE) = 0
  -IBQ1*RTh1  - IBQ1*((1 + Beta) * RE1)  =  -VTh1 + VBE + (VEE)

  IBQ1 = -VTh1 + VBE + (VEE) / ( RTh1 + (1+Beta)*RE1 )
       = {VTh1} - {VBE} -({VEE}) / ( {RTh1} + (1+{Beta})*{RE1} )
       = {IBQ1}A.

  ICQ1 = Beta * IBQ1 = {Beta} * {IBQ1}
       = {ICQ1}A.
  IEQ1 = IBQ1 + ICQ1 = {IBQ1} * {ICQ1}
       = {IEQ1}A.

With Q1's Q-point calculated, determine the transconductance and input
resistance rpi.

  gm1 = ICQ1 / VT         Eq 6.27
      = {ICQ1} / {self._vthrml0_026}
      = {gm1}mho (A/V).

  rpi1 = VT / IBQ1        Eq 6.21b
       = {self._vthrml0_026} / {IBQ1}
       = {rpi1}ohm.

Per the hybrid-pi equivalent circuit (Fig 6.13a), to find the small-signal
transistor output resistance ro, set all independent sources to 0 (Vpi).
This implies that Q1's transconductance is 0 and therefore the dependent
current-source = gm*Vpi = 0.

  A current-source that generates 0 current is an open-circuit; and the
  resistance of an open-circuit is infinite.

Also, ro is influenced by the Early-effect voltage:
  ro = VA / ICQ.
And since VA is given as infinite, ro is infinite.

To plot the I-V characteristic, calculate VCEQ1.
Use KVL through CE-junction:

  **>  VCC - VRC1 - VCEQ1 - VRE1 - VEE = 0
 
and VRC1 = ICQ1 * RC1
        = {ICQ1} * {RC1}.
        = {VRC1}V.

and VRE1 = IEQ1 * RE1
        = {IEQ1} * {RE1}.
        = {VRE1}V.

  {VCC} - VRC1 - VCEQ - VRE1 - {VEE} = 0

  VCEQ = (VCC) - (VRC1) - (VRE1) - (VEE)
       = ({VCC}) - ({VRC1}) - ({VRE1}) - ({VEE})
       = {round(VCEQ1,2)}V.
"""
	print( ans_string )


	print( '\n---- (calcs for Q2) ------------------------------' )

	RTh2:float = r1_parallel_r2( R3, R4 )
	RTh2 = round(RTh2,0)
	VTh2:float = VCC * R4 / ( R3 + R4 )

	# KVL BE-junction
	IBQ2:float = -1 * ( -VTh2 + VBE + VEE ) / ( RTh2 + (1+Beta)*RE2 )
	IBQ2 = round(IBQ2,8)
	ICQ2:float = Beta * IBQ2
	ICQ2 = round(ICQ2,6)
	IEQ2:float = IBQ2 + ICQ2
	IEQ2 = round(IEQ2,6)

	# KVL thru CE-junction
	VRE2:float = IEQ2 * RE2
	VCEQ2:float = VCC - (VRE2) - VEE

	# Q1 transconductance, rpi, ro
	gm2:float = ICQ2 / self._vthrml0_026
	rpi2:float = self._vthrml0_026 / IBQ2
	rpi2 = round(rpi2,0)


	ans_string:str = f"""
For ideal transistor Q2, IB = 0. Therefore the Thevenin Equivalent voltage
Vth determined by the voltage-divider circuit of R3 and R4.

RTh2 = R3||R4 = {RTh2}ohm
VTh2 = VCC * R3||R4 = {VTh2}V.

Use KVL thru the BE-junction:

  **>  VTh2 - IB*RTh2 - VBE - VRE2 - (VEE) = 0

  where VRE2 is the voltage-drop across RE2:
        VRE2 = IEQ2 * RE2
             = (VTh2 - VBE) - (VEE) Volts

Now, solve for IBQ2 and then use Beta to solve for ICQ2.

  IEQ2 = (1 + Beta) * IBQ2

and (again) per KVL:

  **>  VTh2  -  IB*RTh2 - VBE - VRE2 - (VEE) = 0
  VTh2  -  IBQ2*RTh2  - VBE - (IE * RE2) - (VEE) = 0
  VTh2  -  IBQ2*RTh2  - VBE - ((1 + Beta) * IB * RE2) - (VEE) = 0
  -IBQ2*RTh2  - IBQ2*((1 + Beta) * RE2)  =  -VTh2 + VBE + (VEE)

  IBQ2 = -VTh2 + VBE + (VEE) / ( RTh2 + (1+Beta)*RE2 )
       = {VTh2} - {VBE} -({VEE}) / ( {RTh2} + (1+{Beta})*{RE2} )
       = {IBQ2}A.

  ICQ2 = Beta * IBQ2 = {Beta} * {IBQ2}
       = {ICQ2}A.
  IEQ2 = IBQ2 + ICQ2 = {IBQ2} * {ICQ2}
       = {IEQ2}A.

With Q1's Q-point calculated, determine the transconductance and input
resistance rpi.

  gm2 = ICQ2 / VT         Eq 6.27
      = {ICQ2} / {self._vthrml0_026}
      = {gm2}mho (A/V).

  rpi2 = VT / IBQ2        Eq 6.21b
       = {self._vthrml0_026} / {IBQ2}
       = {rpi2}ohm.

Per the hybrid-pi equivalent circuit (Fig 6.13a), to find the small-signal
transistor output resistance ro, set all independent sources to 0 (Vpi).
This implies that Q2's transconductance is 0 and therefore the dependent
current-source = gm*Vpi = 0.

  A current-source that generates 0 current is an open-circuit; and the
  resistance of an open-circuit is infinite.

Also, ro is influenced by the Early-effect voltage:
  ro = VA / ICQ.
And since VA is given as infinite, ro is infinite.

To plot the I-V characteristic, calculate VCEQ2.
Use KVL through CE-junction:

  **>  VCC - VCEQ2 - VRE2 - VEE = 0
 
and VRE2 = IEQ2 * RE2
         = {IEQ2} * {RE2}.
         = {VRE2}V.

  {VCC} - VCEQ - VRE2 - {VEE} = 0

  VCEQ2 = (VCC) - (VRE2) - (VEE)
        = ({VCC}) - ({VRE2}) - ({VEE})
        = {round(VCEQ2,2)}V.
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
