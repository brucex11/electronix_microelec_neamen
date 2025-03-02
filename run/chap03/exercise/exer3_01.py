
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def exer3_01(self):
	"""Page 134:
	An NMOS transistor with VTN = 1V has a drain current iD = 0.8mA
	when vGS = 3V and vDS = 4.5V.  Calculate the drain current when:
	a) vGS = 2V, vDS = 4.5V; and (b) vGS = 3V, vDS = 1V.

	Solution: Solve for Kn conduction parameter per equations 3.2a and 3.2b,
	then solve for drain current given vGS and vDS.

	Assuming operation in nonsaturation region where vDS < vDS(sat), use eq 3.2a.
	Assuming operation in saturation region where vGS > VTN, use eq 3.2b.

	ANS  (a) 0.2 mA  (b) 0.6 mA.
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

	VTN:float = 1.0      # V
	iD_given:float = 0.8e-03   # 0.8mA
	vGS_given:float = 3   # V
	vDS_given:float = 4.5   # V

	# Calc Kn in saturation region
	# iD_nonsat:float = Kn * ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 )
	Kn_sat:float = iD_given / (vGS_given - VTN )**2
	print( f"CALC Kn_sat = {Kn_sat}" )

	# ---- NON saturation region -------------------------------------------------
	#  iD = Kn[ 2(vGS-VTN)vDS - vDS^2]
	# a) vGS = 2V, vDS = 4.5V
	vGS:float = 2
	vDS:float = 4.5
	iD_nonsat:float = Kn_sat * ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 )
	print( f"CALC iD_nonsat = {iD_nonsat}" )

	# Kn_nonsat:float = iD_given / ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 )
	# print( f"CALC iD_nonsat = {iD_nonsat}" )

	# Kn_nonsat:float = iD_given / ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 )
	# print( f"CALC Kn_nonsat = {Kn_nonsat}" )


	# Kn:float = 1.4e-03
	# iD_nonsat:float = Kn * ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 )

	# ---- saturation region -------------------------------------------------
	#  iD = Kn(vGS-VTN)^2
	# a) vGS = 2V, vDS = 4.5V
	# vGS:float = 2

	# iD_a:float = Kn_sat * ( vGS - VTN )**2
	# print( f"CALC iD_a = {iD_a}" )



	calc_result:float = 0
	try:
		assertions.assert_within_percentage( calc_result, ans, assert_percentage )
		print( f"CALC diode current ID = {calc_result}A is within {assert_percentage}% of accepted answer." )
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
