
import inspect
import math
from typing import List
from typing import Tuple

from assertions import assertions

def p1_1(self):
	"""
	ANS(a): (i) 1.03μA, (ii) 2.25mA
	ANS(b): (i) 0.0103μA, (ii) 22.5μA
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	tolerance_percent:float = 2.0  # assertion accuracy

	ans:float = 0

	calc_result:float = 0

	try:
		assertions.assert_within_percentage( calc_result, ans, tolerance_percent )
		print( f"CALC diode current ID = {calc_result}A within {tolerance_percent}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )



# 	for idx, ans in enumerate(answers2):
# 		try:
# 			assertions.assert_within_percentage( calc_result[idx], ans, 3.0 )
# 			print( f"CALC when IS = {IS}A and VD = {diode_voltages[idx]}, diode current ID = {calc_result[idx]}A" )
# 		except AssertionError as e:
# 			print( f"CALC AssertionError {pnum}: {e}" )

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
