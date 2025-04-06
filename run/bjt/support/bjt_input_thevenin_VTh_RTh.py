# from inspect import currentframe
from typing import List

from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2


def bjt_input_thevenin_VTh_RTh(self):
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
	Rs:float = 1000
	R1:float = 2000
	R2:float = 3000
	list_Rs:List[float] = [Rs,R1,R2]

	Vs:float = 1

	# ---- Calc VTh --------------------
	R1_pllel_R2:float = r1_parallel_r2( R1, R2)
	VTh:float = ( R1_pllel_R2 / ( Rs + R1_pllel_R2 ) ) * Vs

	# ---- Calc RTh --------------------
	RTh:float = equivalent_parallel_resisitance( list_rs=list_Rs )


	print( f"\n--- VTh = {VTh} For Vs = {Vs} ---" )

	ans_string:str = f"""
Equivalent resistance for these {len(list_Rs)} resistances in parallel:
"""
	print( ans_string, end='' )

	for idx, r in enumerate(list_Rs):
		print( f"R{idx} = {r}" )

	print( f"--- RTh = {RTh} ---" )
