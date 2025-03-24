from inspect import currentframe

from assertions import assertions


def test5_01(self):
	"""Page 295:
	(a) The common-emitter current gains of two transistors are β = 60 and
	β = 150. Determine the corresponding common-base current gains.
	(b) The common-base current gains of two transistors are α = 0.9820
	and α = 0.9925. Determine the corresponding common-emitter current gains.
	ANS(a): α = 0.9836, α = 0.9934
	ANS(b): β = 54.6, β = 132.3
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"TYU: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 1.0
	print( '-----------------------------------------------\nSolution' )

	# ---- Answers -------------------
	ans_Alpha_a1:float = 0.9836
	ans_Alpha_a2:float = 0.9934
	ans_Beta_b1:float = 54.6
	ans_Beta_b2:float = 132.3

	# ---- Givens --------------------
	Beta_a1:float = 60
	Beta_a2:float = 150
	Alpha_b1:float = 0.9820
	Alpha_b2:float = 0.9925


	ans_string:str = """
The current gain of a BJT is driven by its in-circuit configuration:
 * common-base     (Alpha) - always < 1 (slightly)
 * common-emitter  (Beta)

   Alpha = Beta / ( 1 + Beta )    Eq 5.11  pg 291

   Beta = Alpha / ( 1 - Alpha )   Eq 5.12  pg 291

"""
	print( ans_string )

	print( '---- (a) -------------------------------------------' )

	calc_Alpha_a1:float = Beta_a1 / ( 1 + Beta_a1 )

	try:
		assertions.assert_within_percentage( calc_Alpha_a1, ans_Alpha_a1, assert_percentage )
		print( f"CALC Alpha a1 = {calc_Alpha_a1} is within {assert_percentage}% of accepted answer: {ans_Alpha_a1}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	calc_Alpha_a2:float = Beta_a2 / ( 1 + Beta_a2 )

	try:
		assertions.assert_within_percentage( calc_Alpha_a2, ans_Alpha_a2, assert_percentage )
		print( f"CALC Alpha a2 = {calc_Alpha_a2} is within {assert_percentage}% of accepted answer: {ans_Alpha_a2}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	print( '\n---- (b) -------------------------------------------' )

	calc_Beta_b1:float = Alpha_b1 / ( 1 - Alpha_b1 )

	try:
		assertions.assert_within_percentage( calc_Beta_b1, ans_Beta_b1, assert_percentage )
		print( f"CALC Alpha a1 = {calc_Beta_b1} is within {assert_percentage}% of accepted answer: {ans_Beta_b1}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	calc_Beta_b2:float = Alpha_b2 / ( 1 - Alpha_b2 )

	try:
		assertions.assert_within_percentage( calc_Beta_b2, ans_Beta_b2, assert_percentage )
		print( f"CALC Alpha a2 = {calc_Beta_b2} is within {assert_percentage}% of accepted answer: {ans_Beta_b2}." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )
