import inspect
import math
from typing import List
from typing import Tuple

from assertions import assertions

def p1_3(self):
	"""
	Calculate the intrinsic carrier concentration in silicon and germanium at
	(a) T = 100K, (b) T = 300K, and (c) T = 500K.
	ANS(a) Si ni: (a) 8.79e-10/cm^3, (b) 1.5e+10/cm^3, (c) 1.63e+14/cm^3
	ANS(b) Ge ni: (a) 35.9/cm^3, (b) 2.4e+13/cm^3, (c) 8.62e+15/cm^3."
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	answersSi:Tuple = ( 8.79e-10, 1.5e+10, 1.63e+14 )
	answersGe:Tuple = ( 35.9, 2.4e+13, 8.62e+15 )

	Tk:Tuple = ( 100, 300, 500 )	# Kelvin

	# lists for calculation results
	ni_Si:List[float] = []
	ni_Ge:List[float] = []

	print( '--- (a) Si ---' )
	B:float = self.dict_semicond_mat_consts['Si']['B']

	for temp in Tk:
		ni_Si.append(  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Si']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )
		)

	for idx, ans in enumerate(answersSi):
		try:
			assertions.assert_within_percentage( ni_Si[idx], ans, 5.0 )
			print( f"CALC Si: when Tk = {int(Tk[idx])}K, intrinsic concentration ni = {ni_Si[idx]:.3e}/cm^3" )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )


	print( '--- (b) Ge ---' )
	B = self.dict_semicond_mat_consts['Ge']['B']

	for temp in Tk:
		ni_Ge.append(  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Ge']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )
		)

	for idx, ans in enumerate(answersGe):
		try:
			assertions.assert_within_percentage( ni_Ge[idx], ans, 5.0 )
			print( f"CALC Si: when Tk = {int(Tk[idx])}K, intrinsic concentration ni = {ni_Ge[idx]:.3e}/cm^3" )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )
