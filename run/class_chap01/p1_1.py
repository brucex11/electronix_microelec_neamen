from inspect import currentframe
import math

from assertions import assertions

def p1_1(self):
	"""
	(a) Calculate the intrinsic carrier concentration in silicon at (i) T = 250 K
			and (ii) T = 350 K. (b) Repeat part (a) for gallium arsenide.
	ANS(a) Si:   (i) 1.61e+8/cm^3, (ii) 3.97e+11/cm^3
	ANS(b) GaAs: (i) 6.02e+3/cm^3, (ii) 1.09e+8/cm^3
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

	Tk_250 = 250		# Kelvin
	Tk_350 = 350

	# --- (a)(i) ---
	B:float = self.dict_semicond_mat_consts['Si']['B']
	ni:float =  B * ( Tk_250 ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['Si']['Eg_ev'] / (2 * self.boltzmann_ev * Tk_250) )
	book_ans:float = 1.61e+8

	try:
		assertions.assert_within_percentage( ni, book_ans, tolerance_percent )
		print( f"CALC {pnum}(a)(i):\tfor Si @250K, ni = {ni:.3e}/cm^3 is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# --- (a)(ii) ---
	ni =  B * ( Tk_350 ** (3/2) ) \
		 * math.exp( -1.0 * self.dict_semicond_mat_consts['Si']['Eg_ev'] / (2 * self.boltzmann_ev * Tk_350) )
	book_ans = 3.97e+11
	tolerance_percent:float = 4.0
	try:
		assertions.assert_within_percentage( ni, book_ans, tolerance_percent )
		print( f"CALC {pnum}(a)(ii):\tfor Si @350K, ni = {ni:.3e}/cm^3 is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# --- (b)(i) ---
	B = self.dict_semicond_mat_consts['GaAs']['B']
	ni =  B * ( Tk_250 ** (3/2) ) \
					* math.exp( -1.0 * self.dict_semicond_mat_consts['GaAs']['Eg_ev'] / (2 * self.boltzmann_ev * Tk_250) )
	book_ans = 6.02e+3
	tolerance_percent:float = 8.0
	try:
		assertions.assert_within_percentage( ni, book_ans, tolerance_percent )
		print( f"CALC {pnum}(b)(i):\tfor GaAs @250K, ni = {ni:.3e}/cm^3 is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# --- (b)(ii) ---
	ni =  B * ( Tk_350 ** (3/2) ) \
		 * math.exp( -1.0 * self.dict_semicond_mat_consts['GaAs']['Eg_ev'] / (2 * self.boltzmann_ev * Tk_350) )
	book_ans = 1.09e+8
	tolerance_percent:float = 7.0
	try:
		assertions.assert_within_percentage( ni, book_ans, tolerance_percent )
		print( f"CALC {pnum}(a)(ii):\tfor GaAs @350K, ni = {ni:.3e}/cm^3 is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# --- EX 1.1 page 13 ---
	B = self.dict_semicond_mat_consts['Si']['B']
	ni =  B * ( self.Tk_300 ** (3/2) ) \
		 * math.exp( -1.0 * self.dict_semicond_mat_consts['Si']['Eg_ev'] / (2 * self.boltzmann_ev * self.Tk_300) )
	book_ans = 1.5e+10
	tolerance_percent:float = 5.0
	try:
		assertions.assert_within_percentage( ni, book_ans, tolerance_percent )
		print( f"CALC {pnum} Ex 1.1:\tfor Si @300K, ni = {ni:.3e}/cm^3 is within {tolerance_percent}% of book answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )







	# answers2:Tuple = ( -1e-13, -1e-13, -5.37e-14, 0.0103e-6, 22.5e-6, 49.3e-3 )  # ordered to align with diode_voltages
	# for idx, book_ans in enumerate(answers2):
	# 	try:
	# 		assertions.assert_within_percentage( calc_result[idx], book_ans, 3.0 )
	# 		print( f"when IS = {IS}A and VD = {diode_voltages[idx]}, diode current ID = {calc_result[idx]}A" )
	# 	except AssertionError as e:
	# 		print( f"AssertionError {pnum}: {e}" )

# 	if( ast.literal_eval(self.dict_params['draw_figure']) ):
# 		prep_fig( self, x=diode_voltages, y=calc_result )

# def prep_fig(self, x=(), y=[] ):
# 	import os
# 	import pathlib
# 	import matplotlib.pyplot as plt
# 	from matplotlib.ticker import MaxNLocator

# 	print( f"{prep_fig.__name__}" )
# 	print( f"p1_27.__name__: {p1_27.__name__}" )
# 	dir_plot = os.path.join( self.dir_draw_root, self.dir_draw_subdir )
# 	print( f"dir_plot: '{dir_plot}'" )
# 	pathlib.Path( dir_plot ).mkdir( parents=True, exist_ok=True )

# 	fname = "{a}.png".format( a=p1_27.__name__ )
# 	path_plot = os.path.join( dir_plot, fname )
# 	print( f"path_plot: '{path_plot}'" )

# 	# x = [1, 2, 3, 4, 5]
# 	# y = [2, 3, 5, 7, 11]
# 	x = x
# 	y = y

# 	plt.figure( figsize=self.param_figure_figsize )
# 	plt.scatter(x, y, color='blue', marker='o')  # You can customize the color and marker style

# 	# Set titles and labels
# 	plt.title('Diode Current')
# 	plt.xlabel('Diode V')
# 	plt.xlim( -2.5, 1 )
# 	# Set the x-axis to have 12 divisions
# 	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

# 	plt.ylabel('Diode A')
# 	plt.ylim( -1, 25 )
# 	# plt.yscale( 'log' )

# 	# Display the plot
# 	plt.show()
