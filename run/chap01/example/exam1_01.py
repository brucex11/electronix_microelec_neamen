from inspect import currentframe
import math

from assertions import assertions

def exam1_01(self):
	"""
	Objective: Calculate the intrinsic carrier concentration in silicon at T = 300 K.
	ANS Si: ni = 1.5e+10/cm^3
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	tolerance_percent:float = 5.0  # assertion accuracy
	print( '-----------------------------------------------' )

	# --- Si ---
	B:float = self.dict_semicond_mat_consts['Si']['B']
	temp:float = self.Tk_300   # Kelvin
	ni:float =  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Si']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )
	book_ans:float = 1.5e+10   # /cm^3

	try:
		assertions.assert_within_percentage( ni, book_ans, tolerance_percent )
		print( f"CALC {pnum} for Si @{temp}K, ni = {ni:.3e}/cm^3 is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# --- Ge ---
	B:float = self.dict_semicond_mat_consts['Ge']['B']
	ni:float =  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Ge']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )
	print( f"CALC {pnum} for Ge @{temp}K, ni = {ni:.3e}/cm^3." )

	# --- GaAs ---
	B:float = self.dict_semicond_mat_consts['GaAs']['B']
	ni:float =  B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['GaAs']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )
	print( f"CALC {pnum} for GaAs @{temp}K, ni = {ni:.3e}/cm^3." )
	print( 'These values were added to the Chap01 ctor.' )
