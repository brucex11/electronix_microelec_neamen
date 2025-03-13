
from inspect import currentframe
from math import sqrt
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_41(self):
	"""Page 199:
	Design the circuit in Figure P3.41 so that VSD = 2.5V. The current in the
	bias resistors should be no more than 10 percent of the drain current. The
	transistor parameters are VTP = +1.5V and Kp = 0.5mA/V^2.
	ANS: Page 1363:
	IDQ = 1.25mA, R2 = 59.4kΩ, R1 = 20.6kΩ.
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


	VSS:float = 5          # V
	VDD:float = -5         # V
	RS:float = 2000        # ohm
	VSD_spec:float = 2.5   # V
	VTP:float = +1.5       # V
	Kp:float = 0.5e-03     # A/V^2

	# calc_ID:float = 0

	ans_string:str = """
Per the schematic MOSFET symbol, the device is manufactured in depletion-mode.
Therefore, a channel exists even at zero gate voltage, and a positive gate voltage
must be applied to turn the transistor OFF.

Per the given specs: since VSD = 2.5V, then the voltage drop across RS = 5 - 2.5 = 2.5V.
This "forces" the current through the PMOS channel since the channel is in series
with RS.
"""
	print( ans_string )

	print( '---- (calc ID) ---------------------------------------------' )

	calc_IDQ: float = ( VSS - VSD_spec ) / RS
	print( f"IDQ = ( VSS - VSD_spec ) / RS = {calc_IDQ}A" )


	ans_string = """
Per the given specs: current through the bias resistors R1 and R2 must be less
than or equal to 10% of drain current.  To meet this, start by calculating the
series resistance R1 + R2 between 10V supply (VSS - VDD) and (0.1)(IDQ).
"""
	print( ans_string )

	# print( '---- (calc R1+R2) ---------------------------------------------' )
	# Rbias_total:float = ( VSS - VDD ) / (0.1 * calc_IDQ )
	# print( f"R1+R2 = Rbias_total = ( VSS - VDD ) / (0.1 * IDQ ) = {Rbias_total}ohm" )

	print( '---- (calc VSG in saturation) -------------------------------------' )

	calc_VSG:float = sqrt( calc_IDQ / Kp ) - VTP
	print( f"VSG = sqrt( IDQ / Kp ) - VTP = {calc_VSG}V" )


	ans_string = """
By determining the gate voltage, the voltage drops across the bias resistors
will be known, and with the bias current already specified and calulated,
the individual bias resistor values are calculated.

The gate voltage VG is simply VS - VGS.
"""
	print( ans_string )

	print( '---- (calc R1 and R2) ---------------------------------------------' )
	Ibias_lim:float = 0.1   # 10%
	print( f"Ibias current limit = {Ibias_lim * 100}%")
	calc_VG:float = VSD_spec - calc_VSG
	print( f"VG = VS - VSG = {round(calc_VG, 2)}V" )

	calc_R1:float = ( VSS - round(calc_VG, 2) ) / ( Ibias_lim * calc_IDQ )
	print( f"R1 = ( VSS - VG ) / ( Ibias_lim * IDQ ) = {calc_R1}ohm" )

	calc_R2:float = ( round(calc_VG, 2) - VDD ) / ( Ibias_lim * calc_IDQ )
	print( f"R2 = ( VG - VDD ) / ( Ibias_lim * IDQ ) = {calc_R2}ohm" )


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
