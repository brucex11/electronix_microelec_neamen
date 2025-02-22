
from inspect import currentframe
import math
from typing import List
from typing import Tuple

from assertions import assertions

def exer1_05(self):
	"""Page 25:
	(a) Calculate Vbi for a GaAs pn junction at T = 300 K for Na = 1e+16/cm^3
	and Nd = 1e+17/cm^3 (b) Repeat part (a) for a Germanium pn junction with the
	same doping concentrations.
	SEE ALSO EX 1.1."
	ANS:  (a) Vbi = 1.23 V  (b) Vbi = 0.374 V.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	tolerance_percent:float = 1.0  # assertion accuracy
	print( '-----------------------------------------------' )

	ans_a:float = 1.23  # V
	ans_b:float = 0.374  # V

	temp:float = self.Tk_300   # Kelvin
	Na:float = 1e+16		# /cm^3 net acceptor concentration in the p-region
	Nd:float = 1e+17		# /cm^3 net donor concentration in the n-region

	# --- GaAs SEE ALSO EX 1.1 ---
	B:float = self.dict_semicond_mat_consts['GaAs']['B']
	ni:float =  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['GaAs']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )


	# The natural logarithm is only defined for positive numbers (x > 0).
	# math.log(x) computes ln(x) for positive values of x.
	Vbi = self.vthrml0_026 * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( Vbi, ans_a, tolerance_percent )
		print( f"CALC {pnum} (a) for GaAs, Vbi = {round(Vbi, 3)}V is within {tolerance_percent}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	# --- Ge ---
	B:float = self.dict_semicond_mat_consts['Ge']['B']
	ni:float =  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Ge']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )
	Vbi = self.vthrml0_026 * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( Vbi, ans_b, tolerance_percent )
		print( f"CALC {pnum} (a) for GaAs, Vbi = {round(Vbi, 3)}V is within {tolerance_percent}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
