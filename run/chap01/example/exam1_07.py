import ast
from inspect import currentframe
from typing import List, Tuple

import numpy as np

from assertions import assertions

def exam1_07(self):
	"""Page 28:
	Determine the current in a pn junction diode given voltage VD across it.
	Consider a pn junction at T = 300 K in which IS = 1e-14A and n = 1. Find the
	diode current for VD = +0.70V and VD = -0.7V.
	ANS ID=4.93e-03A @ +0.7V, ID=-1e-14A @ -0.7V.

	Additionally, create a range of VD from -0.7V to +1.4V at 0.1V increments
	and plot the I-V characteristic.
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

	# ID:float = self.calc_diode_ideal_current_complete( IS, VD, Tk, n )
	ID:float = self.calc_diode_ideal_current( IS, VD )

	ans:float = 4.93e-03  # A
	try:
		assertions.assert_within_percentage( ID, ans, tolerance_percent )
		print( f"CALC {pnum}: ID = {round(ID, 5)}A @ VD=+{VD}V within {tolerance_percent}% of accepted answer: {ans}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	VD:float = -0.7  # V

	# ID:float = self.calc_diode_ideal_current_complete( IS, VD, Tk, n )
	ID:float = self.calc_diode_ideal_current( IS, VD )

	ans:float = -1e-14  # A
	try:
		assertions.assert_within_percentage( ID, ans, tolerance_percent )
		print( f"CALC {pnum}: ID = {ID}A @ VD={VD}V within {tolerance_percent}% of accepted answer: {ans}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# ----- Plot the I-V characteristic ------------------------------------------

	# --- WIDE RANGE of voltages across the diode ---
	# 2 ways to create list of floats from -0.7 to 1.4 in increments of 0.1 (Volts)
	# numpy - use round otherwise values look like this, eg: 0.2999999999999998
	# VD_range = np.round( np.arange(-0.7, 1.5, 0.1), 1).tolist()
	# VD_across:Tuple = tuple( VD_range )
	# VD_range = np.round( np.arange(-0.2, 0.9, 0.02), 2).tolist()  # 55 values from -0.2 to 0.88
	# VD_across:Tuple = tuple( VD_range )
	# python - range(22) creates 22 steps, and the round() function ensures each value is to one decimal place.
	# VD_range:List[float] = [round(-0.7 + i * 0.1, 1) for i in range(22)]  # 22 values from -0.7 to 1.4
	VD_range:List[float] = [round(-0.2 + i * 0.02, 2) for i in range(56)]  # 56 values from -0.2 to 0.9
	VD_across:Tuple = tuple( VD_range )
	# print( f"VD_across: {VD_across}, COUNT elements: {len(VD_across)}" )

	diode_current:List[float] = []
	for idx, VDa in enumerate(VD_across):
		ID_this_scope:float = self.calc_diode_ideal_current( IS, VDa )
		diode_current.append( ID_this_scope )
		# print( f"ID: {ID_this_scope} @ {VDa}" )

	if( ast.literal_eval(self.cf.get_config_params['common']['draw_figure']) ):
		print( '---- DRAW PLOT -----' )
		# print( f"VD_across:     {VD_across}, COUNT elements: {len(VD_across)}" )
		# print( f"diode_voltages: {VD_range}, COUNT elements: {len(diode_voltages)}" )
		# print( f"diode_current:  {diode_current}, COUNT elements: {len(diode_current)}" )
		title:str = f"{pnum} Diode I-V, IS = {IS:.0e}A"
		fname_save_plot:str = f"{fcn_name}.png"
		print( f"title: '{title}'" )
		print( f"fname_save_plot: '{fname_save_plot}'" )
		plot_diode_IV_characteristic( self, title, fname_save_plot, VD=VD_across, ID=diode_current )


	# --- NARROW RANGE of voltages across the diode to show the "knee" ---
	VD_range:List[float] = [round(0.5 + i * 0.005, 3) for i in range(64)]  # 36 values from -0.2 to 0.9
	VD_across:Tuple = tuple( VD_range )
	# print( f"VD_across: {VD_across}, COUNT elements: {len(VD_across)}" )

	# clear the list for the next plot
	diode_current.clear()
	for idx, VDacr in enumerate(VD_across):
		ID_thru:float = self.calc_diode_ideal_current( IS, VDacr )
		diode_current.append( ID_thru )
		# print( f"ID: {ID_thru} @ {VDacr}" )

	if( ast.literal_eval(self.cf.get_config_params['common']['draw_figure']) ):
		print( '---- DRAW PLOT -----' )
		print( f"VD_across:     {VD_across}, COUNT elements: {len(VD_across)}" )
		# print( f"diode_voltages: {VD_range}, COUNT elements: {len(diode_voltages)}" )
		print( f"diode_current:  {diode_current}, COUNT elements: {len(diode_current)}" )
		title:str = f"{pnum} Diode I-V, IS = {IS:.0e}A"
		fname_save_plot:str = f"{fcn_name}.png"
		print( f"title: '{title}'" )
		print( f"fname_save_plot: '{fname_save_plot}'" )
		plot_diode_IV_characteristic( self, title, fname_save_plot, VD=VD_across, ID=diode_current )




def plot_diode_IV_characteristic(self, title:str, fname_save_plot:str, VD:Tuple, ID:List[float] ):
	import os
	import pathlib
	# import matplotlib
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator
	# print( f"matplotlib.__version__ : {matplotlib.__version__}" )

	print( f"self.save_figure_dir: '{self.save_figure_dir}'" )
	pathlib.Path( self.save_figure_dir ).mkdir( parents=True, exist_ok=True )

	path_save_figure = os.path.join( self.save_figure_dir, fname_save_plot )
	print( f"path_save_figure: '{path_save_figure}'" )

	# print the (x=VD, y=ID)values to be plotted
	for idx, VDacr in enumerate(VD):
		print( f"PLOT: [{idx}] (x={VDacr}, y=ID: {ID[idx]})" )
	print( f"count PLOT pts: (x=VD={len(VD)}, y=ID={len(ID)})" )

	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )

	# --- SCATTER plot ---
	plt.scatter( VD, ID, color='blue', marker='o' )  # customize color and marker style
	# Highlight a specific point (e.g., the third point) with a different color
	highlight_x = [VD[40]]  # x-coordinate of the point to highlight
	highlight_y = [ID[40]]  # y-coordinate of the point to highlight

	# Plot the highlighted point with a different color
	# plt.scatter(highlight_x, highlight_y, color='red', s=100, label='Highlighted Point')  # 's' for size
	plt.scatter( highlight_x, highlight_y, color='red', label=f"({VD[40]}, {round(ID[40],5):.3e})" )

	# --- LINE plot ---
	# plt.plot( VD, ID, color='blue' )  # customize color

	# Set titles and labels
	plt.title( title )
	plt.xlabel('Diode V')
	# plt.xlim( -0.3, 1 )
	plt.xlim( 0.48, 0.72 )
	# Set the x-axis to have 12 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

	plt.ylabel('Diode A')
	# plt.ylim( -1, 11 )
	plt.ylim( -1e-03, 7e-03 )
	# plt.yscale( 'log' )

	if( self.save_figure ):
		plt.savefig( path_save_figure, dpi=300 )

	# Display the plot
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()
