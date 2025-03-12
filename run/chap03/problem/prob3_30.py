
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_30(self):
	"""Page 197:
	Consider the circuit in Figure P3.30.  The transistor parameters are
	VTP = -0.8 V and Kp = 0.5mA/V^2.  Determine ID, VSG, and VSD.
	ANS  ID= 0.2332mA, VSG = 1.483V, VSD = 4.72V
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------' )


	ans:float = 0
	calc_result:float = 0

	ans_string:str = """
Firstly, since the given VTP < 0, device is p-chan enhancement mode.

The current (IGB) in the voltage-divider circuit that drives the PMOS gate
is biased by 6V across R1 and R2.  (GB: gate bias).
Calculate the gate voltage to determine if the threshold voltage is exceeded
to "turn on" the transistor.

    IGB = Vtot / (R1 + R2)

Then, to calc the gate voltage, subtract the voltage-drop across R1 from the
+3 supply voltage VSS.
"""
	print( ans_string )

	VPT:float = -0.8    # V
	Kp:float = 0.5e-03  # A/V^2
	VSS:float = 3   # V
	VDD:float = -3   # V
	Vtotal:float = VSS - VDD    # V
	R1:float = 8e+03
	R2:float = 22e+03
	RS:float = 0.5e+03
	RD:float = 5e+03

	print( '---- (gate voltage) -----------------------------------------------' )
	IGB:float = Vtotal / (R1+R2)
	VR1 = IGB * R1
	VGB:float = VSS - VR1
	print( f"The gate bias voltage VGB = {VGB}V" )

	print( '---- (PMOS cutoff) ------------------------------------------------' )
	print( f"At cutoff, iD = 0, therefore with 0 voltage-drop across RS, VS = +3, and then VSG = VS - VGB" )
	VSG_cutoff:float = VSS - VGB
	print( f"CALC VSG(cutoff) = {VSG_cutoff}V" )

	ans_string = """
---- (PMOS saturation) ------------------------------------------------.

In saturation, the current (ID) is 6V across RS and RD.
Calc ID = 6V / RS + RD.
Then, to calc the source voltage, subtract the voltage-drop across RS from the
+3 supply voltage VSS.
"""
	print( ans_string )

	iD:float = Vtotal / (RS+RD)
	VS_sat:float = VSS - (iD * RS)
	VSG_sat:float = VS_sat - VGB
	print( f"CALC VSG(saturation) = {VSG_sat}V" )

	# try:
	# 	assertions.assert_within_percentage( calc_result, ans, assert_percentage )
	# 	print( f"CALC diode current ID = {calc_result}A is within {assert_percentage}% of accepted answer." )
	# except AssertionError as e:
	# 	print( f"CALC AssertionError {pnum}: {e}" )



	# Usage single value:
	# ans_a:float = 0.518e-03   # A
	# try:
	# 	assertions.assert_within_percentage( iDS, ans_a, assert_percentage )
	# 	print( f"CALC NMOS iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_a:.3e}." )
	# except AssertionError as e:
	# 	print( f"CALC AssertionError {pnum}: {e}" )

	# try:
	# 	assertions.assert_within_percentage( iSD, ans_a, assert_percentage )
	# 	print( f"CALC PMOS enhancement mode in saturation: iSD = {round(iSD,7)}V", end=' ' )
	# 	print( f"is within {assert_percentage}% of accepted answer {ans_a}V." )
	# except AssertionError as e:
	# 	print( f"CALC AssertionError {pnum}: {e}" )

	# Usage with List:
	# list_calc_iD:List[float] = []   #  don't forget to use list_calc_iD.append(val) to load the list!!
	# ans_a_iDS:Tuple = (0.518e-03, 0.691e-03, 0.691e-03)   #
	# for idx, ans_iDS in enumerate(ans_a_iDS):
	# 	try:
	# 		assertions.assert_within_percentage( list_calc_iDS[idx], ans_iDS, assert_percentage )
	# 		print( f"CALC NMOS iDS = {list_calc_iDS[idx]:.3e}A is within {assert_percentage}% of accepted answer: {ans_iDS:.3e}." )
	# 	except AssertionError as e:
	# 		print( f"CALC AssertionError {pnum}: {e}" )


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
