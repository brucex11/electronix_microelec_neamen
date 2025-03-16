import ast
from inspect import currentframe
import math
from typing import Dict, List, Tuple  # Any, Set


def prob3_03_plot_full(self):
	"""Page 194:
	The transistor characteristics iD versus vDS for an NMOS device are shown
	in Figure P3.3. (a) Is this an enhancement-mode or depletion-mode device?
	(b) Determine the values for Kn and VTN. (c) Determine iD(sat) for
	vGS = 3.5V and vGS = 4.5V

	Previously, calc and plot the iDS ONLY FOR nonsaturation/ohmic region equation.
	See file prob3_03_plot.py.

	Complete the ideal IV-curves for the MOSFET, the iDS(sat) portions of the
	VGS= curves	are "tacked-on" to these curves at the transition-point	for each
	VGS: 2,3,4,5 Volts.

	This is a brute-force method; the iDS nonsat curves are sliced at the
	transition-point for each VGS curve, then the iDS at saturation is tacked-on.
	This will not work for non-ideal IV characteristics.
	Better method would be to build the "entire" iDS-curve by "switching" to the
	iDS(sat) equation to build the "rest" of the curve.  This will support
	non-ideal IV curves when slope of iDS in saturation > 0.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}\nSolution" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.5
	print( '-----------------------------------------------' )

	# nonsaturation: iDS = Kn_nonsat * ( 2 * (vGS - VTN) * vDS - vDS**2 )
	# saturation: iDS = Kn_sat * (vGS - VTN)**2
	# VTN = vGS - vDS(sat)

	ans_mode:str = 'enhancement-mode'
	ans_VTN = 1.5   # V
	ans_Kn:float = 0.064e-03   # A/V^2
	tuple_ans_iDS_sat:Tuple = ( 0.256e-03, 0.576e-03 )

	print( '\n---- (a) -------------------------------------------' )
	ans_string:str = f"Since VGS is positive, device is {ans_mode}."
	print( ans_string )

	max_for_curve_calc_plot_range:int = 301
	list_VDS_range:List[float] = [round(0 + i * 0.02, 3) for i in range(max_for_curve_calc_plot_range)]  # from 0.0 to 6.0
	x_VDS_range:Tuple = tuple( list_VDS_range )
	# print ( x_VDS_range )

	# iDS for VGS = 2V
	vGS_2:float = 2    # V
	iv_params:Dict = {}
	iv_params['VGS'] = vGS_2
	iv_params['VTN'] = ans_VTN
	iv_params['Kn'] = ans_Kn
	iv_params['x_VDS_range'] = x_VDS_range

	list_calc_iDS_vgs_2:List[float] = self.calc_MOSFET_IV_ohmic_curve_given_VGS(
		**iv_params
	)
	iDS_sat:float = max( list_calc_iDS_vgs_2 )
	iDS_idx:int = list_calc_iDS_vgs_2.index( iDS_sat )
	print( f"iDS(sat) = {iDS_sat} @ index:[{iDS_idx}]" )

	# iDS for VGS = 3V
	vGS_3:float = 3    # V
	# Update VGS in function-call params
	iv_params['VGS'] = vGS_3
	list_calc_iDS_vgs_3:List[float] = self.calc_MOSFET_IV_ohmic_curve_given_VGS(
		**iv_params
	)
	iDS_sat:float = max( list_calc_iDS_vgs_3 )
	iDS_idx:int = list_calc_iDS_vgs_3.index( iDS_sat )
	print( f"iDS(sat) = {iDS_sat} @ index:[{iDS_idx}]" )

	# iDS for VGS = 4V
	vGS_4:float = 4    # V
	iv_params['VGS'] = vGS_4
	list_calc_iDS_vgs_4:List[float] = self.calc_MOSFET_IV_ohmic_curve_given_VGS(
		**iv_params
	)
	iDS_sat:float = max( list_calc_iDS_vgs_4 )
	iDS_idx:int = list_calc_iDS_vgs_4.index( iDS_sat )
	print( f"iDS(sat) = {iDS_sat} @ index:[{iDS_idx}]" )

	# iDS for VGS = 5V
	vGS_5:float = 5    # V
	iv_params['VGS'] = vGS_5
	list_calc_iDS_vgs_5:List[float] = self.calc_MOSFET_IV_ohmic_curve_given_VGS(
		**iv_params
	)
	iDS_sat:float = max( list_calc_iDS_vgs_5 )
	iDS_idx:int = list_calc_iDS_vgs_5.index( iDS_sat )
	print( f"iDS(sat) = {iDS_sat} @ index:[{iDS_idx}]" )


	# Calculate iDS(sat) curve for "incremental" range of VGS.
	list_VGS_range:List[float] = [round(0 + i * 0.02, 3) for i in range(max_for_curve_calc_plot_range)]  # from 0.0 to 6.
	list_iDSsat:List[float] = [0] * max_for_curve_calc_plot_range
	iDS_idx_max:int = 0
	iDS_idx_VGS_2:int = -1
	iDS_idx_VGS_3:int = -1
	iDS_idx_VGS_4:int = -1
	iDS_idx_VGS_5:int = -1
	for idx, VGS in enumerate(list_VGS_range):
		iv_params['VGS'] = VGS
		list_calc_iDS:List[float] = self.calc_MOSFET_IV_ohmic_curve_given_VGS(
			**iv_params
		)

		# Pickup the iDS(sat) value from the max of the curve per NONsaturation
		# calculation; where the slope of the curve's derivative == 0.
		# It is critical to grab the index and load the iDS_sat AT THAT INDEX
		# in the `list_iDSsat` that is used for plotting.
		iDS_sat1:float = max( list_calc_iDS )
		iDS_idx:int = list_calc_iDS.index( iDS_sat1 )
		list_iDSsat[iDS_idx] = iDS_sat1
		# The max-index, below, is updated with every iteration; this is used to
		# 'slice' the 'list_iDSsat' to plot ONLY through the range of VDS that is
		# valid.  The LAST time through this loop is the desired value.
		iDS_idx_max = iDS_idx
		# debug and scatterplot support
		if( VGS == 2):
			iDS_idx:int = list_calc_iDS.index( iDS_sat1 )
			iDS_idx_VGS_2 = list_calc_iDS.index( iDS_sat1 )
		elif( VGS == 3):
			iDS_idx:int = list_calc_iDS.index( iDS_sat1 )
			iDS_idx_VGS_3 = list_calc_iDS.index( iDS_sat1 )
		elif( VGS == 4):
			iDS_idx:int = list_calc_iDS.index( iDS_sat1 )
			iDS_idx_VGS_4 = list_calc_iDS.index( iDS_sat1 )
		elif( VGS == 5):
			print( f"&&&&&&&&&&&&&&&ids_sat1 = {iDS_sat1} @ VGS = {VGS}V" )
			iDS_idx:int = list_calc_iDS.index( iDS_sat1 )
			iDS_idx_VGS_5 = list_calc_iDS.index( iDS_sat1 )
			print( f"&&&&&&&&&&&&&&&ids_sat1 = {iDS_sat1} @ index:[{iDS_idx}]" )

	# print( f"list_iDSsat:::{list_iDSsat}" )
	# print( f"LEN list_iDSsat:::{len(list_iDSsat)}" )


	if( ast.literal_eval(self.cf.get_config_params['common']['draw_figure']) ):
		print( '---- DRAW PLOT -----' )
		title:str = f"{pnum} NMOS I-V, Kn = {ans_Kn}A/V^2"
		fname_save_plot:str = f"{fcn_name}.png"
		print( f"title: '{title}'" )
		print( f"fname_save_plot: '{fname_save_plot}'" )

		# --- Draw all lines one plot ----------------------------------------------
		# see also for 'twin' : chap02/example/exam1_10.py
		import matplotlib.pyplot as plt

		plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )

		# Slice the VGS curve data at transition-point to make room for the
		# saturation-region part of the curve.
		# VGS = 5
		x_slice:Tuple = x_VDS_range[:iDS_idx_VGS_5]
		y_slice:List[float] = list_calc_iDS_vgs_5[:iDS_idx_VGS_5]
		plt.plot( x_slice, y_slice, color='k', label=f"VGS={vGS_5}V" )  # customize color, recall 'k' = black
		# Next, replace the 'sliced-off' curve from the transition-point to the end.
		x_slice = x_VDS_range[iDS_idx_VGS_5:]
		len_x_slice:int = len(x_slice)
		len_y_slice:int = max_for_curve_calc_plot_range - len_x_slice - 1
		# print( f"LLLLLLLLLEN len_y_slice: {len_y_slice}" )
		# Below, get the value of iDS at transition-point from list of iDS to build
		# the list of same values = saturation-current.
		y_slice = [ list_calc_iDS_vgs_5[len_y_slice] ] * len_x_slice
		plt.plot( x_slice, y_slice, color='k' )


		# Slice the VGS curve data at transition-point to make room for the
		# saturation-region part of the curve.
		# VGS = 4
		x_slice = x_VDS_range[:iDS_idx_VGS_4]
		y_slice = list_calc_iDS_vgs_4[:iDS_idx_VGS_4]
		plt.plot( x_slice, y_slice, color='b', label=f"VGS={vGS_4}V" )
		# Next, replace the 'sliced-off' curve from the transition-point to the end.
		x_slice = x_VDS_range[iDS_idx_VGS_4:]
		len_x_slice = len(x_slice)
		len_y_slice = max_for_curve_calc_plot_range - len_x_slice - 1
		# Below, get the value of iDS at transition-point from list of iDS to build
		# the list of same values = saturation-current.
		y_slice = [ list_calc_iDS_vgs_4[len_y_slice] ] * len_x_slice
		plt.plot( x_slice, y_slice, color='b' )


		# Slice the VGS curve data at transition-point to make room for the
		# saturation-region part of the curve.
		# VGS = 3
		x_slice = x_VDS_range[:iDS_idx_VGS_3]
		y_slice = list_calc_iDS_vgs_3[:iDS_idx_VGS_3]
		plt.plot( x_slice, y_slice, color='r', label=f"VGS={vGS_3}V" )
		# Next, replace the 'sliced-off' curve from the transition-point to the end.
		x_slice = x_VDS_range[iDS_idx_VGS_3:]
		len_x_slice = len(x_slice)
		len_y_slice = max_for_curve_calc_plot_range - len_x_slice - 1
		# Below, get the value of iDS at transition-point from list of iDS to build
		# the list of same values = saturation-current.
		y_slice = [ list_calc_iDS_vgs_3[len_y_slice] ] * len_x_slice
		plt.plot( x_slice, y_slice, color='r' )


		# Slice the VGS curve data at transition-point to make room for the
		# saturation-region part of the curve.
		# VGS = 2
		x_slice = x_VDS_range[:iDS_idx_VGS_2]
		y_slice = list_calc_iDS_vgs_2[:iDS_idx_VGS_2]
		plt.plot( x_slice, y_slice, color='g', label=f"VGS={vGS_2}V" )
		# Next, replace the 'sliced-off' curve from the transition-point to the end.
		x_slice = x_VDS_range[iDS_idx_VGS_2:]
		len_x_slice = len(x_slice)
		len_y_slice = max_for_curve_calc_plot_range - len_x_slice - 1
		# Below, get the value of iDS at transition-point from list of iDS to build
		# the list of same values = saturation-current.
		y_slice = [ list_calc_iDS_vgs_2[len_y_slice] ] * len_x_slice
		plt.plot( x_slice, y_slice, color='g' )


		# Slice the IDSsat data to stop plotting when iDSsat is maximum.
		x_slice = x_VDS_range[:iDS_idx_max]
		y_slice = list_iDSsat[:iDS_idx_max]
		plt.plot( x_slice, y_slice, color='#800080', label=f"iDS(sat)" )  # purple

		highlight_x:List[float] = [x_slice[iDS_idx_VGS_5]]  # x-coordinate of the point to highlight
		highlight_y:List[float] = [y_slice[iDS_idx_VGS_5]]  # y-coordinate of the point to highlight
		plt.scatter(
			highlight_x, highlight_y, color='k',
			label=f"({x_slice[iDS_idx_VGS_5]}V, {round(y_slice[iDS_idx_VGS_5],5):.3e}A)"
		)

		highlight_x = [x_slice[iDS_idx_VGS_4]]  # x-coordinate of the point to highlight
		highlight_y = [y_slice[iDS_idx_VGS_4]]  # y-coordinate of the point to highlight
		plt.scatter(
			highlight_x, highlight_y, color='b',
			label=f"({x_slice[iDS_idx_VGS_4]}V, {round(y_slice[iDS_idx_VGS_4],5):.3e}A)"
		)

		highlight_x = [x_slice[iDS_idx_VGS_3]]  # x-coordinate of the point to highlight
		highlight_y = [y_slice[iDS_idx_VGS_3]]  # y-coordinate of the point to highlight
		plt.scatter(
			highlight_x, highlight_y, color='r',
			label=f"({x_slice[iDS_idx_VGS_3]}V, {round(y_slice[iDS_idx_VGS_3],5):.3e}A)"
		)

		highlight_x = [x_slice[iDS_idx_VGS_2]]  # x-coordinate of the point to highlight
		highlight_y = [y_slice[iDS_idx_VGS_2]]  # y-coordinate of the point to highlight
		plt.scatter(
			highlight_x, highlight_y, color='g',
			label=f"({x_slice[iDS_idx_VGS_2]}V, {round(y_slice[iDS_idx_VGS_2],5):.3e}A)"
		)

		plt.xlabel('VDS(V)')  # shared x-axis
		plt.ylabel('iDS(A)')  # shared x-axis

		plt.title( title )
		plt.ylim( 0, 0.00085 )

		# plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )
		plt.legend()  # adds a legend to label the highlighted point
		plt.show()


def plot_diode_IV_characteristic(self,
		title:str, fname_save_plot:str, VD:Tuple, ID:List[float] ) -> None:
	"""
	Show and save depending on config.ini [common][draw_figure] param:
	* show - [common][draw_figure] = True
	* show - [common][save_figure] = False

	Args:
		title:str - at top of plot
		fname_save_plot:str - for save to disk if [common][save_figure] = True
		VD:Tuple - list of voltages across pn junction
		ID:List  - list of calculated currents through pn junction

	"""
	import os
	import pathlib
	# import matplotlib
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator
	# print( f"matplotlib.__version__ : {matplotlib.__version__}" )

	iDS_idx:int = 75   # VGS = 3
	# iDS_idx:int = 125   # VGS = 4

	print( f"self.save_figure_dir: '{self.save_figure_dir}'" )
	pathlib.Path( self.save_figure_dir ).mkdir( parents=True, exist_ok=True )

	path_save_figure = os.path.join( self.save_figure_dir, fname_save_plot )
	print( f"path_save_figure: '{path_save_figure}'" )

	# print the (x=VD, y=ID)values to be plotted
	# for idx, VDacr in enumerate(VD):
	# 	print( f"PLOT: [{idx}] (x={VDacr}, y=ID: {ID[idx]})" )
	# print( f"count PLOT pts: (x=VD={len(VD)}, y=ID={len(ID)})" )

	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )

	# Highlight a specific point with a different color
	highlight_x = [VD[iDS_idx]]  # x-coordinate of the point to highlight
	highlight_y = [ID[iDS_idx]]  # y-coordinate of the point to highlight

	# Add a horizontal guide line at y = ID[iDS_idx]
	plt.axhline( y=ID[iDS_idx], color='k', linestyle='--' )  #, label='y = 1000')
	# Add a vertical guide line at x = VD[iDS_idx]
	plt.axvline( x=VD[iDS_idx], color='k', linestyle='--' )  # , label='x = 3')

	# --- SCATTER plot ---
	# plt.scatter( VD, ID, color='blue', marker='o' )  # customize color and marker style
	# # Plot the highlighted point with a different color
	# # plt.scatter(highlight_x, highlight_y, color='red', s=100, label='Highlighted Point')  # 's' for size
	# plt.scatter( highlight_x, highlight_y, color='red', label=f"({VD[iDS_idx]}, {round(ID[iDS_idx],5):.3e})" )

	# --- LINE plot ---
	plt.plot( VD, ID, color='red' )  # customize color
	plt.plot( highlight_x, highlight_y, color='k', label=f"iDS(sat):({VD[iDS_idx]}, {round(ID[iDS_idx],5):.3e})" )

	# Set titles and labels
	plt.title( title )
	plt.xlabel('VDS(V)')
	# plt.xlim( -0.3, 1 )
	plt.xlim( 0, 6 )
	# Set the x-axis to have 12 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

	plt.ylabel('iD(A)')
	# plt.ylim( -1, 11 )
	plt.ylim( -0.5e-03, 0.0005 )
	# plt.yscale( 'log' )

	if( self.save_figure ):
		plt.savefig( path_save_figure, dpi=300 )

	# Display the plot
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()
