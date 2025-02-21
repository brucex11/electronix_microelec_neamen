from inspect import currentframe

from assertions import assertions

def ex1_07(self):
	"""Page 28:
	Determine the current in a pn junction diode.
	Consider a pn junction at T = 300 K in which IS = 1e-14A and n = 1. Find the
	diode current for VD = +0.70V and VD = -0.7V."
	ANS ID=4.93e-03A @ +0.7V, ID=-1e-14A @ -0.7V..
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	tolerance_percent:float = 2.0  # assertion accuracy
	print( '-----------------------------------------------' )

	IS:float = 1e-14  # A
	VD:float = 0.7    # V
	Tk:float = 300    # Kelvin
	n:float = 1       # mission coefficient

	ID:float = self.calc_diode_ideal_current_complete( IS, VD, Tk, n )
	# ID:float = self.calc_diode_ideal_current( IS, VD )

	ans:float = 4.93e-03  # A
	try:
		assertions.assert_within_percentage( ID, ans, tolerance_percent )
		print( f"CALC {pnum}: ID = {round(ID, 5)}A @ VD=+0.7V within {tolerance_percent}% of accepted answer: {ans}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	VD:float = -0.7    # V

	# ID:float = self.calc_diode_ideal_current_complete( IS, VD, Tk, n )
	ID:float = self.calc_diode_ideal_current( IS, VD )

	ans:float = -1e-14  # A
	try:
		assertions.assert_within_percentage( ID, ans, tolerance_percent )
		print( f"CALC {pnum}: ID = {ID}A @ VD=-0.7V within {tolerance_percent}% of accepted answer: {ans}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
