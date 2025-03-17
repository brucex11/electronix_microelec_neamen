from inspect import currentframe

def exam5_01(self):
	"""Page 292:
	Objective: Calculate the collector and emitter currents given the
	base current and current gain.
	Assume a common-emitter current gain of β = 150 and a base current
	of iB = 15uA. Also assume that the transistor is biased in the
	forward-active mode.
	Comment: For reasonable values of β, the collector and emitter currents
	are nearly equal, and the common-base current gain is nearly 1.
	Page 292:
	ANS:  iC = 2.25mA, iE = 2.27mA, Aplha = 0.9934.
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
	ans_iC:float = 2.25e-03   # A
	ans_iE:float = 2.27e-03   # A
	ans_alpha: float = 0.9934

	# ---- Givens --------------------
	Beta:float = 150
	iB:float = 15e-06  # A


	print( '\n---- (iC) -------------------------------------------' )
	calc_iC:float = Beta * iB
	print( f"iC = Beta * iB = {calc_iC}A" )

	print( '\n---- (iE) -------------------------------------------' )
	calc_iE:float = ( 1 + Beta ) * iB
	print( f"iE = ( 1 + Beta ) * iB = {calc_iE}A" )

	print( '\n---- (Alpha) ----------------------------------------' )
	calc_alpha:float = Beta / ( 1 + Beta )
	print( f"From Equation (5.11), the common-base current gain Alpha:" )
	print( f"Alpha = Beta / ( 1 + Beta ) = {calc_alpha}" )

