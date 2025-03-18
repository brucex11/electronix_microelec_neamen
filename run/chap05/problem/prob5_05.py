from inspect import currentframe
from typing import List  # Any, Dict, Set, Tuple

from assertions import assertions

def prob5_05(self):
	"""Page 352:
	(a) For the following values of common-base current gain α, determine
	the corresponding common-emitter current gain β:

            α =  0.90  0.950  0.980  0.990  0.995  0.9990
	ANS(a): 	β =    9     19     49     99    199     999

	(b) For the following values of common-emitter current gain β, determine
	the corresponding common-base current gain α:

						β =    20     50      100      150      220      400
	ANS(b):		α =  0.9524  0.9804  0.9901  0.9934   0.9955   0.9975
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.2
	print( '-----------------------------------------------\nSolution' )

	# ---- Answers -------------------
	ans_a:List[int] = [ 9, 19, 49, 99, 199, 999 ]
	ans_b:List[float] = [ 0.9524, 0.9804, 0.9901, 0.9934, 0.9955, 0.9975 ]

	# ---- Givens --------------------
	list_Alpha:List[float] = [ 0.90, 0.950, 0.980, 0.990, 0.995, 0.9990 ]
	list_Beta:List[int] = [ 20, 50, 100, 150, 220, 400 ]


	ans_string:str = """
Alpha is the common-base current gain and is always slightly < 1.
    **>  Alpha = ( Beta / 1 + Beta )    Eq (5.11)

-and-

the common-emitter current gain in terms of the common-base current gain:

    **>  Beta = ( Alpha / 1 - Alpha )    Eq (5.12)
"""
	print( ans_string )

	print( '\n---- (a calc Beta) -------------------------------------------' )
	calc_list_Beta:List[float] = []

	for Alpha in list_Alpha:
		beta:float = ( Alpha / ( 1 - Alpha ) )
		beta = int(round(beta,1))
		calc_list_Beta.append( beta )

	for idx, Beta in enumerate(ans_a):
		try:
			assertions.assert_within_percentage( calc_list_Beta[idx], Beta, assert_percentage )
			print( f"ASSERT Beta = {calc_list_Beta[idx]} is within {assert_percentage}% of accepted answer: {Beta}." )
		except AssertionError as e:
			print( f"ASSERT AssertionError {pnum}: {e}" )


	print( '\n---- (b calc Alpha) -------------------------------------------' )
	calc_list_Alpha:List[float] = []

	for beta in list_Beta:
		alpha:float = ( beta / ( 1 + beta ) )
		alpha = round(alpha,4)
		calc_list_Alpha.append( alpha )

	for idx, Alpha in enumerate(ans_b):
		try:
			assertions.assert_within_percentage( calc_list_Alpha[idx], Alpha, assert_percentage )
			print( f"ASSERT Alpha = {calc_list_Alpha[idx]} is within {assert_percentage}% of accepted answer: {Alpha}." )
		except AssertionError as e:
			print( f"ASSERT AssertionError {pnum}: {e}" )
