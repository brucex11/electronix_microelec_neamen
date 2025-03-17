from inspect import currentframe

def exer5_01(self):
	"""Page 293:
	An NPN transistor is biased in the forward-active mode. The base current
	is IB = 8.50μA and the emitter current is IE = 1.20mA.
	Determine β, α, and IC.
	ANS:  Beta = 140.2, Alpha = 0.9929, iC = 1.1915mA.
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

	# ---- Givens --------------------
	iB:float = 8.5e-06  # A
	iE:float = 1.2e-03  # A

	print( '\n---- (Beta) -------------------------------------------' )
	print( f"  iE = (1 + Beta)iB    Eq (5.9)" )
	calc_Beta:float = iE / iB - 1
	print( f"Beta = {calc_Beta}" )

	print( '\n---- (iC) -------------------------------------------' )
	print( f"  iC = Beta*iB" )
	calc_iC:float = calc_Beta * iB
	calc_iC = round(calc_iC,7)
	print( f"iC = {calc_iC}A" )

	print( '\n---- (Alpha) ----------------------------------------' )
	calc_alpha:float = calc_iC / iE
	print( f"**>  iC = Alpha * iE" )
	print( f"Alpha = {calc_alpha}" )
