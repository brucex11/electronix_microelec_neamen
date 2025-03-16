from inspect import currentframe

from assertions import assertions

def prob5_02(self):
	"""Page 352:
	(a) A bipolar transistor is biased in the forward-active mode. The collector
	current is iC = 726μA and the emitter current is iE = 732μA. Determine
	β, α, and iB. (b) Repeat part (a) if iC = 2.902mA and iE = 2.961mA.
	ANS:  (a) β = 121, α = 0.9918, iB = 6μA
	ANS:  (b) β = 49.19, α = 0.9801, iB = 59μA
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}\nSolution" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.4
	print( '-----------------------------------------------' )

	# ---- Answers -------------------
	ans_a_iB:float = 6e-06   # A
	ans_b_iB:float = 59e-06   # A

	# ---- Givens --------------------
	iCa:float = 726e-06   # A
	iEa:float = 732e-06   # A

	iCb:float = 2.902e-03   # A
	iEb:float = 2.961e-03   # A

	ans_string:str = """
Current Relationships: page 291
Modeling the bipolar transistor as a single node, by Kirchhoff's current law:

    iE = iC + iB    Eq (5.7)

When the transistor is biased in the forward-active mode, then

  **  iC = Beta(iB)   Eq (5.8)  note: conventional current gain,

Substitute Equation (5.8) into (5.7) for the relationship between the emitter
and base currents:

    iE = (1 + Beta)iB    Eq (5.9)

Solving for iB in Equation (5.8) and substituting into Equation (5.9), the
relationship between the collector and emitter currents is:

  **  iC = ( Beta / 1 + Beta ) * iE   Eq (5.10)

Define   Alpha = ( Beta / 1 + Beta )    Eq (5.11)
   and   Alpha is the common-base current gain and is always slightly < 1.
		
And therefore:

  **  iC = Alpha * iE, then:

From Equation (5.11), the common-emitter current gain in terms of the
common-base current gain:

    Beta = ( Alpha / 1 - Alpha )    Eq (5.12)
"""
	print( ans_string )

	print( '\n---- (a) -------------------------------------------' )

	alpha_a:float = iCa / iEa
	alpha_a = round(alpha_a,4)
	print( f"Alpha = iC / iE = {alpha_a}  Eq 5.10" )

	# ratio_iE_over_iC:float = iEa / iCa
	# ratio_iE_over_iC = round(ratio_iE_over_iC,4)
	# print( f"iE / iC = {ratio_iE_over_iC}" )

	calc_beta_a:float = alpha_a / ( 1 - alpha_a )
	calc_beta_a = int( round(calc_beta_a,0) )
	print( f"Beta = ( Alpha / 1 - Alpha ) = {calc_beta_a}" )

	calc_iBa:float = iEa - iCa
	calc_iBa = round(calc_iBa,7)
	# print( f"iB = ( iE - iC ) = {calc_iBa} = {calc_iBa*1e06}uA" )

	try:
		assertions.assert_within_percentage( calc_iBa, ans_a_iB, assert_percentage )
		print( f"CALC iB = {calc_iBa}A is within {assert_percentage}% of accepted answer: {ans_a_iB}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	print( '\n---- (b) -------------------------------------------' )

	alpha_b:float = iCb / iEb
	alpha_b = round(alpha_b,4)
	print( f"Alpha = iC / iE = {alpha_b}  Eq 5.10" )

	calc_beta_b:float = alpha_b / ( 1 - alpha_b )
	calc_beta_b = int( round(calc_beta_b,2) )
	print( f"Beta = ( Alpha / 1 - Alpha ) = {calc_beta_b}" )

	calc_iBb:float = iEb - iCb
	calc_iBb = round(calc_iBb,7)
	# print( f"iB = ( iE - iC ) = {calc_iBb} = {calc_iBb*1e06}uA" )

	try:
		assertions.assert_within_percentage( calc_iBb, ans_b_iB, assert_percentage )
		print( f"CALC iB = {calc_iBb}A is within {assert_percentage}% of accepted answer: {ans_b_iB}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )
