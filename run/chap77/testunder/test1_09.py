import ast
from inspect import currentframe
# import math
from typing import List, Tuple   #, Any, Dict, Set

import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator

from assertions import assertions

def test77_09(self):
	"""Page 43:
	Consider the diode and circuit in Exercise EX 1.8.  Determine VD and ID
	using the graphical technique.
	From page 37, exercise 1.8:
	Use iteration to determine the diode voltage and current for the circuit
	per Figure 1.28.  Consider a diode with a given reverse-saturation current
	of IS = 1e-13A.  VPS = V; R=4kΩ.
	Comment: Once the diode voltage is known, the current can also be determined
	from the ideal diode equation. However, dividing the voltage difference across
	a resistor by the resistance is usually easier, and this approach is used
	extensively in the analysis of diode and transistor circuits.
	Page 37:
	ANS VD ~= 0.54 V, ID ~= 0.87mA.

	See example/doc/exam1_08.docx (because this exercise is essentially the same).

	Solution:
	Use KVL to write the voltage equation around the loop:
		VPS = ID*R + VD
	Then, solve above for ID.

	Note, the diode I-V characteristic == Ideal Diode Equation
			see Chap01.calc_diode_ideal_current( ID, VD ).
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

