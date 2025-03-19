from inspect import currentframe

def prob5_20a(self):
	"""Page 354:
	The current gain for each transistor in the circuits shown in
	Figure P5.20 is Beta = 120. For each circuit, determine IC and VCE."
	ANS:  (a) IC =  , VCE = 1.96V.
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
	ans_IC:float = 0
	ans_VCE:float = 0

	# ---- Givens --------------------
	VCC:float = 2.0    # V
	VBB:float = 0.2    # V
	RC:float = 4e+03   # Ω


	ans_string:str = f"""
Voltage at Q1 base = 0.2V which is < typical "turn-on" threshold
VBE @ 0.7V.  Therefore, IC ~= 0, and VCE = 2V because voltage-drop
across RC = 0.
This is in agreement with LTspice simulation.

--- END {self.prob_str} ---
"""
	print( ans_string )
