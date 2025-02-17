
import inspect
import math
from typing import List
from typing import Tuple

from assertions import assertions

def ex1_02(self):
	"""
	ANS (a) po = 2.25e+04/cm^3  (b) no = 4.5+e03/cm^3
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	ans_a:float = 2.25e+04
	# Since Nd >> ni , the electron concentration no ~= 1e+16/cm^3
	Nd:float = 1e+16
	po:float = self.ni**2 / Nd

	try:
		assertions.assert_within_percentage( po, ans_a, 3.0 )
		print( f"CALC (a): po = {po:.3e}/cm^3" )
	except AssertionError as e:
		print( f"CALC (a) AssertionError {pnum}: {e}" )

	ans_b:float = 4.5e+03
	# Since Na >> ni , the hole concentration po ~= 5e+16/cm^3
	Na:float = 5e+16
	no:float = self.ni**2 / Na

	try:
		assertions.assert_within_percentage( no, ans_b, 3.0 )
		print( f"CALC (a): po = {no:.3e}/cm^3" )
	except AssertionError as e:
		print( f"CALC (a) AssertionError {pnum}: {e}" )
