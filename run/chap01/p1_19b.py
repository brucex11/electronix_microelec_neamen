from inspect import currentframe
import math
from assertions import assertions

def p1_19b(self):
	"""
	ANS: 1.19b (i) 1.13V, (ii) 1.21V, (iii) 1.41V
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( f"Problem: {self.prob_str}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	tolerance_percent:float = 2.0  # assertion accuracy
	print( '-----------------------------------------------' )

	ans_i:float = 1.13
	ans_ii:float = 1.21
	ans_iii:float = 1.41
	pnum:str = f"{self.prob_str}(all-3)"

	# First, calc the intrinsic carrier concentration.
	B = self.dict_semicond_mat_consts['GaAs']['B']
	ni =  B * ( self.Tk_300 ** (3/2) ) \
					* math.exp( -1.0 * self.dict_semicond_mat_consts['GaAs']['Eg_ev'] / (2 * self.boltzmann_ev * self.Tk_300) )
	print( f"CALC {pnum}:\tfor GaAs @300K, ni = {ni:.3e}/cm^3" )

	# Next, calc the barrier voltage for each of the concentrations Na and Nd.
	pnum:str = f"{self.prob_str}(i)"
	Na:float = 5.0e+15		# net acceptor concentration in the p-region
	Nd:float = 5.0e+15		# net donor concentration in the n-region
	vbi = self.vthermal * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( vbi, ans_i, tolerance_percent )
		print( f"CALC {pnum}:\tfor GaAs, Vbi = {round(vbi, 3)}V is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	pnum:str = f"{self.prob_str}(ii)"
	Na:float = 1.0e+15		# net acceptor concentration in the p-region
	Nd:float = 5.0e+17		# net donor concentration in the n-region
	vbi = self.vthermal * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( vbi, ans_ii, tolerance_percent )
		print( f"CALC {pnum}:\tfor GaAs, Vbi = {round(vbi, 3)}V is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	pnum:str = f"{self.prob_str}(iii)"
	Na:float = 1.0e+18		# net acceptor concentration in the p-region
	Nd:float = 1.0e+18		# net donor concentration in the n-region
	vbi = self.vthermal * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( vbi, ans_iii, tolerance_percent )
		print( f"CALC {pnum}:\tfor GaAs, Vbi = {round(vbi, 3)}V is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
