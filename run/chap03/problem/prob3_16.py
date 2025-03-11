
import ast
from inspect import currentframe
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_16(self):
	"""Page 196:
	A p-channel depletion-mode MOSFET has parameters VTP = +2V,
	k'p = 40μA/V^2, and W/L = 6. Determine VSD(sat) for: (a) VSG = -1V,
	(b) VSG = 0, and (c) VSG = +1V.
	If the transistor is biased in the saturation	region, calculate
	the drain current for each value of VSG.
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

	ans_string:str = """
For PMOS depletion-mode, vSD(sat) = vSG + VTP per Eq 3.6 pg 136.
"""
	print( ans_string )
	print( '---- (Determine VSD(sat)) -----------------------------------------' )
	VSG_given:Tuple = ( -3, -2, -1, 0, 1, 2 )   # V
	VTP_given:float = 2   # V

	list_calc_vSD_sat:List[float] = []
	for vSG in VSG_given:
		vsat:float = vSG + VTP_given
		list_calc_vSD_sat.append( vsat )

	ans_vSD_sat:Tuple = ( -1, 0, 1, 2, 3, 4 )   # V
	for idx, ans_vSD in enumerate(ans_vSD_sat):
		try:
			assertions.assert_within_percentage( list_calc_vSD_sat[idx], ans_vSD, assert_percentage )
			print( f"CALC PMOS vSD(sat) = {list_calc_vSD_sat[idx]}V is within {assert_percentage}% of accepted answer: {ans_vSD}V." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

	if( self.draw_figure ):
		title:str = f"{pnum} PMOS depl vSD(sat) for VTP = +2V"
		plot_PMOS_depl_vSG_vs_vSDsat( self,
			title=title,
			fname_save_plot='',
			vSG=VSG_given,
			vSD=list_calc_vSD_sat
		)


	ans_string:str = """
With the PMOS depletion-mode MOSFET biased in the saturation region, per Eq 3.4a
pg 136, calculate drain current:

      iD = Kp(vSG + VTP)^2 = Kp * [vSD(sat)]^2
And,
since Kp = (k'p/2)(W/L), calculate Kp and substitute into the equation for iD.
"""
	print( ans_string )
	print( '---- (calculate drain current) ------------------------------------' )

	k_prime_p:float = 40e-06   # A/V^2
	ratio_WL:float = 6
	Kp:float = ( k_prime_p / 2 ) * ( ratio_WL )

	list_calc_iSD:List[float] = []

	for vSD_sat in list_calc_vSD_sat:
		ids:float = Kp * vSD_sat**2
		list_calc_iSD.append( ids )

	# print( list_calc_iSD )

	tuple_ans_iSD:Tuple = (0.00012, 0.0, 0.00012, 0.00048, 0.00108, 0.00192 )
	for idx, ans_iSD in enumerate(tuple_ans_iSD):
		try:
			assertions.assert_within_percentage( list_calc_iSD[idx], ans_iSD, assert_percentage )
			print( f"CALC PMOS iSD = {list_calc_iSD[idx]:.3e}A @ vSD(sat) = {list_calc_vSD_sat[idx]} is  within {assert_percentage}% of accepted answer: {ans_iSD:.3e}." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

	if( self.draw_figure ):
		# Convert list to tuple for call to plot...
		tuple_calc_iSD = tuple(list_calc_iSD)
		title:str = f"{pnum} PMOS depl iSD for VTP = +2V"
		plot_PMOS_depl_iSD_vs_vSDsat( self,
			title=title,
			fname_save_plot='',
			iSD=tuple_calc_iSD,
			vSD=list_calc_vSD_sat
		)

	print( '---- END ----------------------------------------------------------' )


def plot_PMOS_depl_vSG_vs_vSDsat(self,
		title:str, fname_save_plot:str, vSG:Tuple, vSD:List[float] ) -> None:
	"""
	Show and save depending on config.ini [common][draw_figure] param:
	* show - [common][draw_figure] = True
	* show - [common][save_figure] = False

	Args:
		title:str - at top of plot
		fname_save_plot:str - for save to disk if [common][save_figure] = True
		vSG:Tuple - voltages source-to-gate
		vSD:List  - voltages source-to-drain

	"""
	import matplotlib.pyplot as plt
	# from matplotlib.ticker import MaxNLocator
	# print( f"matplotlib.__version__ : {matplotlib.__version__}" )

	# print( f"self.save_figure_dir: '{self.save_figure_dir}'" )
	# pathlib.Path( self.save_figure_dir ).mkdir( parents=True, exist_ok=True )
	# path_save_figure = os.path.join( self.save_figure_dir, fname_save_plot )
	# print( f"path_save_figure: '{path_save_figure}'" )

	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )

	# --- SCATTER plot ---
	plt.scatter( vSD, vSG, color='b', marker='o' )  # customize color and marker style
	# --- LINE plot ---
	plt.plot( vSD, vSG, color='b' )  # customize color

	# Plot the highlighted point with a different color
	# Highlight a specific point with a different color
	highlight_x = [vSD[3]]  # x-coordinate of the point to highlight
	highlight_y = [vSG[3]]  # y-coordinate of the point to highlight

	# Add a horizontal guide line
	plt.axhline( y=vSG[3], color='r', linestyle='--', label=f"vSG={vSG[3]}" )
	# Add a vertical guide line
	plt.axvline( x=vSD[3], color='b', linestyle='--', label=f"vSD={vSD[3]}" )

	plt.scatter( highlight_x, highlight_y, color='red', label=f"vSD == VTP\nvSD(sat) = vSG + VTP" )


	# Set titles and labels
	plt.title( title )
	# plt.text(5, 10, 'vSD(sat) = vSG + VTP', ha='center', fontsize=10)  doesn't seem to work
	plt.xlabel('vSD( V )')
	# plt.xlim( -0.3, 1 )
	# Set the x-axis to have 12 divisions
	# plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

	plt.ylabel('vSG( V )')
	# plt.ylim( -1, 11 )

	# if( self.save_figure ):
	# 	plt.savefig( path_save_figure, dpi=300 )

	# Display the plot
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()
	plt.close()


def plot_PMOS_depl_iSD_vs_vSDsat(self,
		title:str, fname_save_plot:str, iSD:Tuple, vSD:List[float] ) -> None:
	"""
	Show and save depending on config.ini [common][draw_figure] param:
	* show - [common][draw_figure] = True
	* show - [common][save_figure] = False

	Args:
		title:str - at top of plot
		fname_save_plot:str - for save to disk if [common][save_figure] = True
		iSG:Tuple - voltages source-to-gate
		vSD:List  - voltages source-to-drain

	"""
	if( not self.draw_figure ):
		return

	import matplotlib.pyplot as plt
	# from matplotlib.ticker import MaxNLocator
	# print( f"matplotlib.__version__ : {matplotlib.__version__}" )

	# print( f"self.save_figure_dir: '{self.save_figure_dir}'" )
	# pathlib.Path( self.save_figure_dir ).mkdir( parents=True, exist_ok=True )
	# path_save_figure = os.path.join( self.save_figure_dir, fname_save_plot )
	# print( f"path_save_figure: '{path_save_figure}'" )

	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )

	# --- SCATTER plot ---
	plt.scatter( vSD, iSD, color='b', marker='o' )  # customize color and marker style
	# --- LINE plot ---
	plt.plot( vSD, iSD, color='b' )  # customize color

	# Plot the highlighted point with a different color
	# Highlight a specific point with a different color
	highlight_x = [vSD[3]]  # x-coordinate of the point to highlight
	highlight_y = [iSD[3]]  # y-coordinate of the point to highlight

	# Add a horizontal guide line
	plt.axhline( y=iSD[3], color='r', linestyle='--', label=f"iSD={iSD[3]:.2e}" )
	# Add a vertical guide line
	plt.axvline( x=vSD[3], color='b', linestyle='--', label=f"vSD={vSD[3]}" )

	plt.scatter( highlight_x, highlight_y, color='red', label=f"vSD == VTP\nvSD(sat) = vSG + VTP" )


	# Set titles and labels
	plt.title( title )
	# plt.text(5, 10, 'vSD(sat) = vSG + VTP', ha='center', fontsize=10)  doesn't seem to work
	plt.xlabel('vSD( V )')
	# plt.xlim( -0.3, 1 )
	# Set the x-axis to have 12 divisions
	# plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

	plt.ylabel('iSD( A )')
	# plt.ylim( -1, 11 )

	# if( self.save_figure ):
	# 	plt.savefig( path_save_figure, dpi=300 )

	# Display the plot
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()
