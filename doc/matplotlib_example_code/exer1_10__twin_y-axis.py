import ast
from inspect import currentframe
# import math
from typing import Any, List, Tuple

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
# import numpy as np

from assertions import assertions

def exer1_10(self) -> None:
	"""Page 41:
	Objective: Determine the diode current and voltage characteristics of the
	circuit shown in Figure 1.28. using ideal diode calcs.
	Compare to the LTspice simulation:
	C:\\SourceCode\\GitHub\\electronix\\microelec_neamen\\LTspice\\chap01\\exer1_10\\exer1_10_Dcust01.asc

	Let R = 20kΩ over VPS range 0 to 10V.

	ANS Q-point VD = 0.579V, ID = 469μA.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0  # assertion accuracy
	print( '-----------------------------------------------' )

	ans_VD:float = 0.579     # V
	ans_ID:float = 469e-06   # A

	# Write the KVL equation:
	# VPS = R * (ideal diode eq) + VD
	VPS:float = 10     # V
	R:float = 20000    # Ω
	IS:float = 1e-13   # A
	VD_iter_val:List[float] = [round(0.54 + i * 0.001, 3) for i in range(51)]  # 51 values from 0.54 to 0.59
	print( f"VD_iter_val: {VD_iter_val}V" )

	# Iteratively solve for VPS using range of values for VD.
	VD_per_iteration:float = -1
	ID_per_iteration:float = -1
	q_point:Any = []   # [V,D,qidx]
	for qidx, VDi in enumerate(VD_iter_val):
		ID_ideal:float = self.calc_diode_ideal_current( IS=IS, VD=VDi )
		qVPS_iter_val:float = R * ID_ideal + VDi
		# print( f"[{qidx}] qVPS_iter_val = {round(qVPS_iter_val,3)}V when VD = {VDi}V, and ID = {round(ID_ideal,5)}A" )

		# check the iteral value against VPS
		try:
			assertions.assert_within_percentage( VPS, qVPS_iter_val, assert_percentage )
			print( f"CALC iterate qVPS = {round(qVPS_iter_val,3)}V when VD = {VDi}V, and ID = {round(ID_ideal,6)}A" )
			q_point = [VDi, ID_ideal, qidx]
			# break
		except AssertionError:
			pass
	print( f"Q-point: ({q_point[0]}V, {round(q_point[1],5)}A) @ qidx:[{q_point[2]}]" )

	# At this point, the ideal ID when the assertion was satified == Q-point loop current.
	try:
		assertions.assert_within_percentage( q_point[0], ans_VD, assert_percentage )
		print( f"CALC VD @ Q-point = {round(q_point[0],3)}V", end=' ' )
		print( f"within {assert_percentage}% of accepted answer: {round(ans_VD,3)}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( q_point[1], ans_ID, assert_percentage )
		print( f"CALC using diode ideal-ID value @ Q-point = {round(q_point[1],5)}A", end=' ' )
		print( f"within {assert_percentage}% of accepted answer: {round(ans_ID,5)}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# However, the dividing-the-voltage-difference-across-a-resistor approach
	# is used extensively in the analysis of diode and transistor circuits.

	ID_final:float = ( VPS - q_point[0] ) / R
	try:
		assertions.assert_within_percentage( ID_final, ans_ID, assert_percentage )
		print( f"CALC (VPS-VD)/R = ID = {ID_final}A within {assert_percentage}% of accepted answer: {ans_ID}A" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	# ----------------------------------------------------------------------------
	# ------ Implement the LTspice simulation ------------------------------------
	# ----------------------------------------------------------------------------
	VD_iter_val.clear()
	VD_iter_val:List[float] = [round(0 + i * 0.002, 3) for i in range(1001)]  # 501 values from 0 to 10V
	# print( f"VD_iter_val: {VD_iter_val}V" )

	# Iteratively solve for VPS using range of values for VD.
	# Create the lists that take the values to plot
	vd1:List[float] = []
	id1:List[float] = []
	VPS_x_coord:List[float] = []
	# ID_per_iteration:float = -1
	# q_point:Any = []   # [V,D,qidx]
	for qidx, VDi in enumerate(VD_iter_val):
		ID_ideal:float = self.calc_diode_ideal_current( IS=IS, VD=VDi )
		qVPS_iter_val:float = R * ID_ideal + VDi
		# print( f"[{qidx}] qVPS_iter_val = {round(qVPS_iter_val,3)}V when VD = {VDi}V, and ID = {ID_ideal}A" )
		id1.append( ID_ideal )
		vd1.append( VDi )
		VPS_x_coord.append( qVPS_iter_val )
		if qVPS_iter_val > 10:
			break


	# --- GENERATE figure and plot the load_line. --------------------------------
	# plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )
	# plt.plot( VPS_x_coord, id1, color='blue' )  # customize color

	fig, ax1 = plt.subplots()  # Create a figure and axis for the first plot
	ax1.set_xlabel('VPS V')  # shared x-axis

	# Diode voltage (vd1) - create first y-axis (vd1) sharing the same x-axis (VPS)
	ax1.plot( VPS_x_coord, vd1, color='r', label='V(vd1)' )
	ax1.set_ylabel('V(vd1) V', color='r')  # Set y-axis label for the first axis
	ax1.tick_params(axis='y', labelcolor='r')
	plt.legend()  # adds a legend to label the current curve

	# Diode current - create second y-axis (id1) on to-be-shared x-axis (VPS)
	ax2 = ax1.twinx()
	ax2.plot( VPS_x_coord, id1, color='b', label='I(D1)' )  # customize color, recall 'k' = black
	ax2.set_ylabel('I(D1) A', color='b')  # Set y-axis label for the second axis
	ax2.tick_params(axis='y', labelcolor='b')
	plt.legend()  # adds a legend to label the voltage curve

	# drop a point on the graph at the Q_point
	plt.scatter( x=q_point[0], y=q_point[1], color='black', label=f"Q-point ({q_point[0]}V, {round(q_point[1],5)*1000}mA)" )

	plt.title( f"{pnum} Diode I-V with Q-point Fig 1.29, pg 38" )

	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()
