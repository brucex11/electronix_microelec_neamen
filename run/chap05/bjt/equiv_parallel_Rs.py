# from inspect import currentframe
from typing import List

from equations.equations import equivalent_parallel_resisitance


def equiv_parallel_Rs(self):
	"""Calculate equivalent resistance of parallel resistors.
	"""
	# fcn_name:str = currentframe().f_code.co_name
	# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )


	#  α   β   Ω   μ   λ   γ   ξ   ω  π


	# ---- Givens --------------------
	# list_Rs:List[float] = [22e+3,50e+3,190e+03]
	# list_Rs:List[float] = [14.4e+3,250]
	list_Rs:List[float] = [14.4e+3,150]

	req = equivalent_parallel_resisitance( list_rs=list_Rs )

	ans_string:str = f"""
Equivalent resistance for these {len(list_Rs)} resistances in parallel:
"""
	print( ans_string, end='' )

	for idx, r in enumerate(list_Rs):
		print( f"R{idx} = {r}" )

	print( f"--- Req = {req} ---" )
