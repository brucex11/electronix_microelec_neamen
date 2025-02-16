import ast
import math
import numpy as np
from typing import List
from typing import Tuple

from assertions import assertions

def p1_27(self):
	"""
	ANS(a): (i) 1.03μA, (ii) 2.25mA, (iii) 4.93A, (iv) -5.37ρA, (v) -1e-11A, (vi) -1e-11A
	ANS(a): (i) 0.0103μA, (ii) 22.5μA, (iii) 49.3mA, (iv) -537.0ρA, (v) -1e-13A, (vi) -1e-13A
	"""
	# print( f"CALLED: {p1_27.__name__}" )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_text}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	diode_voltages:Tuple = ( -2.0, -0.2, -0.02, 0.3, 0.5, 0.7, 0.72, 0.74 )  # in ascending order for plot
	diode_current:List[float] = []
	IS:float = 1e-11

	for VD in diode_voltages:
		diode_current.append( IS * ( ( math.exp( VD / self.vthrml0_026) ) - 1 ) )
	# take log of all elements of diode-currents
	print( f">>>ANS (a) when IS = {IS}A: diode currents:       {diode_current}" )
	diode_current_log10:List[float] = [math.log10(abs(x)) for x in diode_current]
	print( f">>>ANS (a) when IS = {IS}A: diode currents log10: {diode_current_log10}" )

	answers1:Tuple = ( -1e-11, -1e-11, -5.37e-12, 1.03e-6, 2.25e-3, 4.93, 1, 1 )  # ordered to align with diode_voltages
	# ANS (a) when IS = 1e-11A: diode currents: [1.025854912131968e-06, 0.0022481068956995425, 4.92655962756388, -5.366306307688247e-12, -9.995436760994189e-12, -1e-11]

	for idx, ans in enumerate(answers1):
		try:
			assertions.assert_within_percentage( diode_current[idx], ans, 3.0 )
			print( f"when IS = {IS}A and VD = {diode_voltages[idx]}, diode current ID = {diode_current[idx]}A" )
		except AssertionError as e:
			print( f"AssertionError {pnum}: {e}" )

	if( ast.literal_eval(self.cf.get_config_params['common']['draw_figure']) ):
		prep_fig( self, x=diode_voltages, y=diode_current )

	print( '-----------------------------------------------------' )
	IS:float = 1e-13
	diode_current.clear()

	for VD in diode_voltages:
		diode_current.append( IS * ( ( math.exp( VD / self.vthrml0_026) ) - 1 ) )

	answers2:Tuple = ( -1e-13, -1e-13, -5.37e-14, 0.0103e-6, 22.5e-6, 49.3e-3 )  # ordered to align with diode_voltages
	# print( f"ANS (b) when IS = {IS}A: diode currents: {diode_current}" )
	# ANS (b) when IS = 1e-13A: diode currents: [1.0258549121319682e-08, 2.2481068956995425e-05, 0.049265596275638805, -5.3663063076882465e-14, -9.99543676099419e-14, -1e-13]

	for idx, ans in enumerate(answers2):
		try:
			assertions.assert_within_percentage( diode_current[idx], ans, 3.0 )
			print( f"when IS = {IS}A and VD = {diode_voltages[idx]}, diode current ID = {diode_current[idx]}A" )
		except AssertionError as e:
			print( f"AssertionError {pnum}: {e}" )

	if( ast.literal_eval(self.cf.get_config_params['common']['draw_figure']) ):
		prep_fig( self, x=diode_voltages, y=diode_current )


def prep_fig(self, x=(), y=[] ):
	import os
	import pathlib
	import matplotlib
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator
	print( f"matplotlib.__version__ : {matplotlib.__version__}" )

	# print( f"{prep_fig.__name__}" )
	# print( f"p1_27.__name__: {p1_27.__name__}" )
	dir_plot = os.path.join(
		self.cf.get_config_params['common']['dir_draw_root'],
		self.cf.get_config_params['common']['dir_draw_subdir'] )
	print( f"dir_plot: '{dir_plot}'" )
	pathlib.Path( dir_plot ).mkdir( parents=True, exist_ok=True )

	fname = "{a}.png".format( a=p1_27.__name__ )
	path_plot = os.path.join( dir_plot, fname )
	print( f"path_plot: '{path_plot}'" )

	# x = [1, 2, 3, 4, 5]
	# y = [2, 3, 5, 7, 11]
	x = x
	y = y

	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )
	plt.scatter( x, y, color='blue', marker='x' )  # customize color and marker style

	# Set titles and labels
	plt.title('Diode Current')
	plt.xlabel('Diode V')
	plt.xlim( -2.5, 1 )
	# Set the x-axis to have 12 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

	plt.ylabel('Diode A')
	plt.ylim( -1, 25 )
	# plt.yscale( 'log' )

	# Display the plot
	plt.show()
