import inspect
import math
from typing import List
from typing import Tuple

from assertions import assertions

def p1_5(self):
	"""
	ANS(a) p-type, po = 1e+16/cm^3, no = 3.24e-04/cm^3
	ANS(b) p-type, po = 1e+16/cm^3, no = 5.76e+10/cm^3."
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	ans_a_no:float = 3.24e-04

	Na:float = 1e+16  # /cm^3

	print( '--- (a) GaAs ---' )

	B:float = self.dict_semicond_mat_consts['GaAs']['B']
	ni:float =  B * ( self.Tk_300 ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['GaAs']['Eg_ev'] / (2 * self.boltzmann_ev * self.Tk_300) )
	print( f"CALC GaAs ni @ 300K: {ni:.4e}/cm^3" )

	no:float = ni**2 / Na
	print( f"CALC GaAs Na = 1e+16, no = {no:.4e}/cm^3" )

	try:
		assertions.assert_within_percentage( no, ans_a_no, 11.3 )
		print( f"CALC GaAs no = {no:.3e}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	print( '--- (b) Ge ---' )
	ans_b_no:float = 5.76e+10
	B = self.dict_semicond_mat_consts['Ge']['B']
	ni =  B * ( self.Tk_300 ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Ge']['Eg_ev'] / (2 * self.boltzmann_ev * self.Tk_300) )
	print( f"CALC Ge ni @ 300K: {ni:.4e}/cm^3" )

	no = ni**2 / Na
	print( f"CALC Ge Na = 1e+16, no = {no:.4e}/cm^3" )

	try:
		assertions.assert_within_percentage( no, ans_b_no, 5.0 )
		print( f"CALC GaAs no = {no:.3e}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
