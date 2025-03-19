from inspect import currentframe

def prob5_20b(self):
	"""Page 354:
	The current gain for each transistor in the circuits shown in
	Figure P5.20 is Beta = 120. For each circuit, determine IC and VCE."
	ANS:  (b) IC = 0.24mA, VCE = 1.04V.
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

	# ---- Answers -------------------
	ans_IC:float = 0.24e-03  # A
	ans_VCE:float = 1.04     # V

	# ---- Givens --------------------
	VCC:float = 2.0    # V
	IBB:float = 2e-06  # A
	RC:float = 4e+03   # Ω
	Beta:float = 120

	calc_IC:float = Beta * IBB
	calc_IC = round(calc_IC,5)

	calc_VC:float = VCC - calc_IC * RC

	ans_string:str = f"""
With current source at Q1 base = 2uA, IC is calculated as Beta*iB:

  **>  IC = Beta * IB
       IC = {calc_IC}A

Then, the current through RC drives the voltage-drop across it:

  **>  IC * RC = VCC - VC
    {calc_IC} * {RC}  =  {VCC} - VC

Solve for VC:  VC = {calc_VC}V.

Since Q1's emitter is connected to ground:

  **> VCE = VC - VE = {calc_VC}V.

This is in agreement with LTspice simulation.

--- END {self.prob_str} ---
"""
	print( ans_string )
