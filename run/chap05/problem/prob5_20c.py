from inspect import currentframe

def prob5_20c(self):
	"""Page 354:
	The current gain for each transistor in the circuits shown in
	Figure P5.20 is Beta = 120. For each circuit, determine IC and VCE."
	ANS:  (a) IC = 0.275mA , VCE = 2V (saturation).
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

	# ---- Answers -------------------
	ans_IC:float = 0
	ans_VCE:float = 0

	# ---- Givens --------------------
	VCC:float = 2.0    # V
	VBB:float = 1.4    # V
	RC:float = 4e+03   # Ω
	RE:float = 2e+03   # Ω
	Beta:float = 120

	# ---- Assumptions ---------------
	VBE_NPN:float = 0.7         # V
	VCE_sat_mode:float = 0.2    # V

	# ---- Calculations --------------
	calc_VE = VBB - VBE_NPN
	calc_IE = calc_VE / RE

	calc_Alpha:float = Beta / (1 + Beta)
	calc_Alpha = round(calc_Alpha,4)

	calc_IC:float = calc_Alpha * calc_IE
	calc_IC = round(calc_IC,7)

	calc_VRC:float = calc_IC * RC
	calc_VRC = round(calc_VRC,7)
	calc_VC:float = VCC - calc_VRC
	calc_VC = round(calc_VC,7)

	calc_VCE:float = calc_VC - calc_VE
	calc_VCE = round(calc_VCE,7)

	calc_VC_sat:float = calc_VE + VCE_sat_mode
	calc_VC_sat = round(calc_VC_sat,1)

	calc_IC_sat:float = ( VCC - calc_VC_sat ) / RC


	ans_string:str = f"""
With voltage source at Q1 base = 1.4V, Q1's "turn-on"
voltage-threshold of 0.7V is exceeded.

Therefore, VE is simply VCC - 0.7 = 0.7V.

Then, the voltage-drop across RE drives the current through it:

  **>  IE = VE - 0 / RE
       IE = VE / RE = {calc_VE} / {RC}
       IE = {calc_IE}A.

Next, calculate Aplha per known Beta and solve for IC:
Alpha = ( Beta / (1 + Beta) )    Eq (5.11)

Alpha = {calc_Alpha}

  **>  IC =  Alpha * IE
       IC = {calc_IC}A

With IC known, calculate VC:  VCC - (voltage-drop-across-RC)
  **>  VC = VCC - (IC * RC)
       VC = {VCC} - {calc_VRC}
       VC = {calc_VC}V.

Therefore, VCE = VC - VE:
  **>  VCE = {calc_VC} - {calc_VE}
       VCE = {calc_VCE}V.

Since VCE = {calc_VCE}V is impossible, Q1 must be in saturation-mode.
In saturation for common-emitter circuit, VCE ~= 0.2V.
Therefore, VC = VE + VCE:
  **>  VC = {calc_VE} + {VCE_sat_mode}
  **>  VC = {calc_VC_sat}

Then, the voltage-drop across RC drives the current through it:
  **>  IC = ( VCC - VC ) / RC
       IC = ( {VCC} - {calc_VC_sat} ) / {RC}
       IC = {calc_IC_sat}A.
"""
	print( ans_string )

	VCE_sat_mode = 0.028    # V
	calc_VC_sat = calc_VE + VCE_sat_mode
	calc_VC_sat = round(calc_VC_sat,3)

	calc_IC_sat = ( VCC - calc_VC_sat ) / RC
	calc_IC_sat = round(calc_IC_sat,6)


	ans_string = f"""
To approach LTspice simulation, in saturation for common-emitter
circuit, choose VCE ~= 0.028V.

Therefore, VC = VE + VCE:
  **>  VC = {calc_VE} + {VCE_sat_mode}
  **>  VC = {calc_VC_sat}

Then, the voltage-drop across RC drives the current through it:
  **>  IC = ( VCC - VC ) / RC
       IC = ( {VCC} - {calc_VC_sat} ) / {RC}
       IC = {calc_IC_sat}A.
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---")
