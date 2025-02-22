from inspect import currentframe
import math
from typing import List


def p1_2(self):
	"""
	Page 57:
	(a) The intrinsic carrier concentration in silicon is to be no larger than
	ni = 1e+12/cm^3. Determine the maximum allowable temperature. (b) Repeat
	part (a) for ni = 1e+09/cm^3.

	Rather than deriving the equation for Tk, programatically iterate through
	a range of temps, then assert that the concentration n_i meets the requirement
	less than 1e+12 and 1e+09 per cm^3.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	# --- (a) ---
	B:float = self.dict_semicond_mat_consts['Si']['B']
	ni_required:float = 1.0e+12

	# utilize python "list comprehension" capability to spec the range of temps.
	# Descend from 500 to 200 and decrement by 2 each iteration.
	# temps:List[float] = [temp for temp in range(380, 359, -2) ]
	temps:List[float] = [temp for temp in range(380, 359, -1) ]
	# print( f"temps: {temps}" )

	for temp in temps:
		n_i:float =  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Si']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )

		try:
			assert ni_required <= n_i
			print( f"CALC for temp: {temp}K : n_i = {n_i:.3e}/cm^3" )
		except AssertionError:
			print( f"for ni in silicon no larger than {ni_required:.3e}, temp cannot exceed {temp}K" )
			break

	# --- (b) ---
	ni_required:float = 1.0e+09
	temps:List[float] = [temp for temp in range(278, 263, -1) ]

	for temp in temps:
		n_i:float =  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Si']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )

		try:
			assert ni_required <= n_i
			print( f"CALC for temp: {temp}K : n_i = {n_i:.3e}/cm^3" )
		except AssertionError:
			print( f"for ni in silicon no larger than {ni_required:.3e}, temp cannot exceed {temp}K" )
			break
