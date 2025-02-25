
import ast
from inspect import currentframe
# import math
from typing import List, Tuple  # , Any, Dict, Set

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from assertions import assertions

def exam1_08(self):
	"""Page 36:
	Use iteration to determine the diode voltage and current for the circuit
	per Figure 1.28.  Consider a diode with a given reverse-saturation current
	of IS = 1e-13A.  VPS = 5V; R=2kΩ.
	Comment: Once the diode voltage is known, the current can also be determined
	from the ideal diode equation. However, dividing the voltage difference across
	a resistor by the resistance is usually easier, and this approach is used
	extensively in the analysis of diode and transistor circuits.
	Also, use graphic analysis by plotting the `load line`.
	Page 37:
	ANS VD = 0.619 V, ID = 2.19mA.

	See example/doc/exam1_08.docx.

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

	ans_VD:float = 0.619     # V
	ans_ID:float = 2.19e-03  # A

	# Write the KVL equation:
	# VPS = R * (ideal diode eq) + VD
	VPS:float = 5     # V
	R:float = 2000    # Ω
	IS:float = 1e-13  # A
	VD_iter_val:List[float] = [round(0.6 + i * 0.001, 3) for i in range(24)]  # 24 values from 0.6 to 0.623
	print( f"VD_iter_val: {VD_iter_val}V" )

	# Iteratively solve for VPS using range of values for VD.
	VD_per_iteration:float = -1
	for VDi in VD_iter_val:
		ID_ideal:float = self.calc_diode_ideal_current( IS=IS, VD=VDi )
		VPS_iter_val:float = R * ID_ideal + VDi
		print( f"VPS_iter_val = {VPS_iter_val}V" )

		# check the iteral value against VPS
		try:
			assertions.assert_within_percentage( VPS, VPS_iter_val, assert_percentage )
			print( f"CALC VPS = {round(VPS_iter_val,3)}V when VD = {VDi}V, and ID = {ID_ideal}A" )
			VD_per_iteration = VDi
			break
		except AssertionError:
			pass

	# At this point, the ideal ID when the assertion was satified IS the loop current.
	try:
		assertions.assert_within_percentage( ID_ideal, ans_ID, assert_percentage )
		print( f"CALC using diode ideal-ID value = {ID_ideal}A within {assert_percentage}% of accepted answer: {ans_ID}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# However, the dividing-the-voltage-difference-across-a-resistor approach
	# is used extensively in the analysis of diode and transistor circuits.

	ID_final:float = ( VPS - VD_per_iteration ) / R
	try:
		assertions.assert_within_percentage( ID_final, ans_ID, assert_percentage )
		print( f"CALC (VPS-VD)/R = ID = {ID_ideal}A within {assert_percentage}% of accepted answer: {ans_ID}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	# --------- Use graphic analysis by plotting the `load line`. ----------------
	# From Equation ID = (VPS-VD)/R, when ID = 0, then VD = VPS which is the
	# horizontal axis intercept. Also from this equation, if VD = 0, then ID = VPS/R
	# which is the vertical axis intercept. The load line can be drawn between these two
	# points; the slope of the load line is -1/R.

	# Current (I) is the x-axis; voltage (V) is the y-axis.

	# Set up the points to draw the 'load line'.
	# x = [1, 4]  # x-coordinates of the two points
	# y = [2, 5]  # y-coordinates of the two points

	# The actual points:
	horiz_axis_intercept:Tuple = (VPS, 0)
	vert_axis_intercept:Tuple  = (0, VPS/R)

	# use the load line endpoints to calc the slope
	rise:float = 0 - VPS / R  # current is vertical y-axis
	run:float  = VPS - 0      # voltage is horiz x-axis
	slope_load_line:float = rise / run
	print( f"slope_load_line: {slope_load_line} = -1/R = {-1/R}" )

	# Then for plot ("draw" left to right):
	x = [0, VPS]      # x-coordinates of the two points
	y = [VPS/R, 0]    # y-coordinates of the two points

	# --- GENERATE figure and plot the load_line. --------------------------------
	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )
	plt.plot( x, y, color='blue' )  # customize color

	# ------ Calc the diode's I-V characteristic ---------------------------------
	# keyword: list_range_for_rationals
	VD_range:List[float] = [round(0 + i * 0.02, 2) for i in range(34)]  # 34 values from 0 to 0.66

	diode_current:List[float] = []
	for idx, VDa in enumerate(VD_range):
		ID_this_scope:float = self.calc_diode_ideal_current( IS, VDa )
		diode_current.append( ID_this_scope )
		# print( f"ID: {ID_this_scope} @ {VDa}" )

	# --- Plot the diode's I-V characteristic --------------------------------
	plt.plot( VD_range, diode_current, color='red' )  # customize color

	# dump the VD and ID lists to find where to "locate" the Q_point.
	# By inspection of the graph, the Q-point is ~ (0.62V, 2.2ma)
	# NOTE: this didn't work so well, so set the horiz and vert lines directly.
	# print( f"VD_range: {VD_range}" )
	# print( f"diode_current: {diode_current}" )
	# # Add a horizontal guide line at y = ID[40]
	# plt.axhline( y=diode_current[31], color='black', linestyle='--' )  #, label='y = 1000')
	# # Add a vertical guide line at x = VD[40]
	# plt.axvline( x=VD_range[31], color='black', linestyle='--' )  # , label='x = 3')

	plt.axhline( y=2.2e-03, color='black', linestyle='--' )  #, label='y = 1000')
	# Add a vertical guide line at x = VD[40]
	plt.axvline( x=0.61, color='black', linestyle='--' )  # , label='x = 3')

	# drop a point on the graph at the Q_point
	plt.scatter( x=0.61, y=2.2e-03, color='black', label=f"Q point (0.61, {2.2}m)" )


	plt.xlim( 0 , 5 )
	plt.ylim( -5e-05, 3e-03 )

	# Add labels and title
	plt.xlabel('Voltage V')
	plt.ylabel('Current I')
	plt.title('Load Line, Q-point Fig 1.29, pg 38')

	# Show the plot
	plt.show()
