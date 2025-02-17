import ast
import inspect
import math
# import numpy as np
from typing import List
from typing import Tuple

from assertions import assertions

def p1_27_plot(self):
	"""
	(a) The reverse-saturation current of a pn junction diode is IS = 1e-11A.
	Determine the diode current for diode voltages of 0.3, 0.5, 0.7, -0.02, -0.2, and -2V.
	(b) Repeat for IS = 1e-13A
	ANS(a): (i) 1.03μA, (ii) 2.25mA, (iii) 4.93A, (iv) -5.37ρA, (v) -1e-11A, (vi) -1e-11A
	ANS(a): (i) 0.0103μA, (ii) 22.5μA, (iii) 49.3mA, (iv) -537.0ρA, (v) -1e-13A, (vi) -1e-13A
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	# print( f"CALLED: {p1_27.__name__}" )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	diode_voltages:Tuple = ( -2.0, -0.2, -0.02, 0.3, 0.5, 0.7, 0.72, 0.74 )  # in ascending order for plot
	diode_current:List[float] = []
	IS:float = 1e-11

	for VD in diode_voltages:
		diode_current.append( IS * ( ( math.exp( VD / self.vthrml0_026) ) - 1 ) )
	# take log of all elements of diode-currents
	print( f">>>CALC (a) when IS = {IS}A: diode currents:       {diode_current}" )
	diode_current_log10:List[float] = [math.log10(abs(x)) for x in diode_current]
	print( f">>>CALC (a) when IS = {IS}A: diode currents log10: {diode_current_log10}" )

	answers1:Tuple = ( -1e-11, -1e-11, -5.37e-12, 1.03e-6, 2.25e-3, 4.93, 1, 1 )  # ordered to align with diode_voltages
	# ANS (a) when IS = 1e-11A: diode currents: [1.025854912131968e-06, 0.0022481068956995425, 4.92655962756388, -5.366306307688247e-12, -9.995436760994189e-12, -1e-11]

	for idx, ans in enumerate(answers1):
		try:
			assertions.assert_within_percentage( diode_current[idx], ans, 3.0 )
			print( f"CALC when IS = {IS}A and VD = {diode_voltages[idx]}, diode current ID = {diode_current[idx]}A" )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

	if( ast.literal_eval(self.cf.get_config_params['common']['draw_figure']) ):
		title:str = f"{pnum} Diode Volts, IS = {IS:.3e}A"
		fname_save_plot:str = 'p1_27_diode_volts_1.png'
		prep_fig( self, title, fname_save_plot, x=diode_voltages, y=diode_current )

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
			print( f"CALC when IS = {IS}A and VD = {diode_voltages[idx]}, diode current ID = {diode_current[idx]}A" )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

	if( ast.literal_eval(self.cf.get_config_params['common']['draw_figure']) ):
		title:str = f"{pnum} Diode Volts, IS = {IS:.3e}A"
		fname_save_plot:str = 'p1_27_diode_volts_2.png'
		prep_fig( self, title, fname_save_plot, x=diode_voltages, y=diode_current )


def prep_fig(self, title:str, fname_save_plot:str, x:Tuple=(), y:List[float]=[] ):
	import os
	import pathlib
	import matplotlib
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator
	# print( f"matplotlib.__version__ : {matplotlib.__version__}" )

	print( f"self.save_figure_dir: '{self.save_figure_dir}'" )
	pathlib.Path( self.save_figure_dir ).mkdir( parents=True, exist_ok=True )

	path_save_figure = os.path.join( self.save_figure_dir, fname_save_plot )
	print( f"path_save_figure: '{path_save_figure}'" )

	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )
	plt.scatter( x, y, color='blue', marker='o' )  # customize color and marker style

	# Set titles and labels
	plt.title( title )
	plt.xlabel('Diode V')
	plt.xlim( -2.5, 1 )
	# Set the x-axis to have 12 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

	plt.ylabel('Diode A')
	plt.ylim( -1, 25 )
	# plt.yscale( 'log' )

	if( self.save_figure ):
		plt.savefig( path_save_figure, dpi=300 )

	# Display the plot
	plt.show()
