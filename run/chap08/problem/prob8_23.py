from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.current import current_divider
from equations.voltage import voltage_divider


def prob8_23(self):
	"""Page 609:
	Consider an idealized class-B output stage shown in Figure P8.22.
	The effective turn-on voltages of devices A and B are zero, and the
	effective 'saturation' voltages of vA and vB are zero.
	The output stage is to deliver 50W of average power to a 24Ω load for
	a symmetrical input sine wave. Assume the supply voltages are ±n volts,
	where n is an integer.
	(a) The power supply voltages are to be at least 3V greater than the
	maximum output voltage.  What must be the power supply voltages?
	(b) What is the peak current in each device?
	(c) What is the power conversion efficiency?
	Wed, Apr 30, 2025  5:40:00 PM
	Page 1346:
	ANS: (a) V+ = 52V, V- -52V  (b) 2.04A  (c) η = 74%
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
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  η

	# ---- Answers -------------------
	ans_Vp:float = 49   # V


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Givens  -------------------
	RL:float = 24
	P_avg:float = 50

	# ---- Calcs ---------------------
	Vp:float = math.sqrt( 2 * RL * P_avg )
	Vp = round(Vp,2)
	V_plus = Vp + 3

	ans_string:str = f"""
---- (a) ----
  P(load) = (1/2)Vp^2 / RL
  {P_avg}W = (1/2)Vp^2 / {RL}

  Vp = math.sqrt( 2 * RL * P_avg )
     = math.sqrt( 2 * {RL} * {P_avg} )
  Vp = {Vp}V.

Since the power supply voltages are to be at least 3V greater than the
maximum output voltage, the power supply voltages are Vp +- 3V:

  V+ = Vp + 3 = 52V
  V- = -Vp - 3 = -52V

"""
	print( ans_string )

	try:
		assert_within_percentage( Vp, ans_Vp, assert_percentage )
		print( f"ASSERT Vp = {Vp}A is within {assert_percentage}% of accepted answer: {ans_Vp}." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	# ---- Calcs ---------------------
	Ip:float = Vp / RL
	Ip = round(Ip,2)

	ans_string:str = f"""
---- (b) ----
  Ip = Vp / RL
  Ip = {Vp} / {RL}
  Ip = {Ip}A.

"""
	print( ans_string )


	# ---- Calcs ---------------------
	eta:float = (math.pi/4)*(Vp/V_plus)

	ans_string:str = f"""
---- (c) ----
  eta = (pi/4)*(Vp/VCC)
      = (pi/4)*(Vp/V+)
      = ({math.pi}/4)*({Vp}/{V_plus})
  eta = {eta}

"""
	print( ans_string )
	print( f"--- END {self.prob_str} ---" )


# Usage single value:
# ans_a:float = 0.518e-03   # A
# try:
# 	assert_within_percentage( iDS, ans_a, assert_percentage )
# 	print( f"ASSERT NMOS iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_a:.3e}." )
# except AssertionError as e:
# 	print( f"AssertionError {pnum}: {e}" )

# try:
# 	assert_within_percentage( iSD, ans_a, assert_percentage )
# 	print( f"ASSERT PMOS enhancement mode in saturation: iSD = {round(iSD,7)}V", end=' ' )
# 	print( f"is within {assert_percentage}% of accepted answer {ans_a}V." )
# except AssertionError as e:
# 	print( f"AssertionError {pnum}: {e}" )

# Usage with List:
# list_calc_iD:List[float] = []   #  don't forget to use list_calc_iD.append(val) to load the list!!
# ans_a_iDS:Tuple = (0.518e-03, 0.691e-03, 0.691e-03)   #
# for idx, ans_iDS in enumerate(ans_a_iDS):
# 	try:
# 		assert_within_percentage( list_calc_iDS[idx], ans_iDS, assert_percentage )
# 		print( f"ASSERT NMOS iDS = {list_calc_iDS[idx]:.3e}A is within {assert_percentage}% of accepted answer: {ans_iDS:.3e}." )
# 	except AssertionError as e:
# 		print( f"AssertionError {pnum}: {e}" )


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
