import ast
from inspect import currentframe
# import math
from typing import List, Tuple   #, Any, Dict, Set

import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator

from assertions import assertions

def test3_02(self):
	"""Page 145:
	The NMOS devices described in Exercise TYU 3.1 have parameters
	W = 20μm, L = 0.8μm, tox = 200°A, μn = 500 cm2/V-s, and λ = 0.
	(a) Calculate the conduction parameter Kn for each device.
	(b) Calculate the drain current for each bias condition listed in TYU 3.1.
	Page 145:
	ANS (a) Kn = 1.08mA/V2;	(b) iD = 0.518mA, 0.691mA, and 0.691mA; iD = 2.59mA, 5.83mA, and 11.1mA.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 1.0
	print( '-----------------------------------------------' )

	ans_VD:float = 0.54     # V
	ans_ID:float = 0.87e-03  # A

