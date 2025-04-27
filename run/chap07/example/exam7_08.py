from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.equations import current_divider


def exam7_08(self):
	"""Page 505:
	Objective: Determine the 3 dB frequency of the short-circuit current gain
	for BJT.
	Consider a BJT with parameters rπ = 2.6kΩ, Cπ = 0.5pF, and Cμ = 0.025pF.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  τ

	# ---- Givens --------------------
	rπ:float = 2.6e+03  # 2.6kΩ
	Cπ:float = 0.5e-12  # 0.5pF
	Cμ:float = 0.025e-12  # 0.025pF

	# ---- Calcs ---------------------
	fb:float = self.beta_cutoff_freq( rπ=rπ, Cπ=Cπ, Cμ=Cμ )


	ans_string:str = f"""
3 dB frequency of the short-circuit current gain for BJT:

  fb = 1 / ( 2 * pi * rpi * ( Cpi + Cu) )
  fb = {fb:.6e}Hz.
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
