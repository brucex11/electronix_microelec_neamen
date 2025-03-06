import ast
from inspect import currentframe
# import math
from typing import List, Tuple   #, Any, Dict, Set

import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator

from assertions import assertions

def test3_01(self):
	"""Page 145:
	(a) An n-channel enhancement-mode MOSFET has a threshold voltage of
	VTN = 1.2V and an applied gate-to-source voltage of vGS = 2V. Determine the
	region of operation when: (i) vDS = 0.4V; (ii) vDS = 1V; and (iii) vDS = 5V.
	(b) Repeat part (a) for an n-channel depletion-mode MOSFET with a threshold
	voltage of VTN = -1.2V.
	Page 145:
	ANS (a) (i) nonsaturation, (ii) saturation, (iii) saturation
			(b) (i) nonsaturation, (ii) nonsaturation, (iii) saturation.
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

