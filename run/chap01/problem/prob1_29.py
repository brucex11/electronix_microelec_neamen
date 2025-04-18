from inspect import currentframe
import math

from assertions import assertions

def prob1_29(self):
	"""
	A silicon pn junction diode has an emission coefficient of n = 1. The diode current is ID = 1mA
	when VD = 0.7V. (a) What is the reverse-bias saturation current?
	(b) Plot, on the same graph, log10 ID versus VD over the range 0.1 <= VD <= 0.7 V when the emission coefficient
	is (i) n = 1 and (ii) n = 2.

	ANS (a) 2.03e-15A
  ANS (b) (i)  At VD = 0.1V,  ID = 9.50e-14A;  at VD = 0.7V, ID = 1mA
         (ii) At VD = 0.1 V, ID = 1.39e-14 A; at VD = 0.7V, ID = 1.42e-9A
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	tolerance_percent:float = 2.0  # assertion accuracy
	print( '-----------------------------------------------\nSolution' )

	n:int = 1	# emission coefficient
	ID:float = 1.0e-3
	VD:float = 0.7

	# ID = IS * ( ( math.exp( VD / n*self.vthrml0_026) ) - 1 ) )
	exp:float = VD / (n*self.vthrml0_026)
	# print( f"exp: {exp}" )
	IS:float = ID / ( math.exp( exp ) - 1 )

	ans_a:float = 2.03e-15
	try:
		assertions.assert_within_percentage( IS, ans_a, 1.0 )
		print( f"CALC (a) reverse saturation current IS = {round(IS,18)}A is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )
