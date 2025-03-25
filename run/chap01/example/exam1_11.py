
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def exam1_11(self):
	"""Page 45:
	Objective: Analyze the circuit shown in Figure 1.35(a).
	Assume circuit and diode parameters of VPS = 5V, R = 5kΩ, Vγ = 0.6V,
	and vi = 0.1sinωt(V).
	ANS:  IDQ = 0.88mA, Vo = 4.4V, rd = 0.0295kΩ, id = 19.9sinωt (μa),
	vo = 0.0995sinωt(V).
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

	#  α   β   Ω   μ   λ   γ   ξ   ω

	# ---- Answers -------------------
	ans:float = 0
	ans_IDQ = 0.88e-03

	# ---- Givens --------------------
	VPS:float = 5   # V
	R:float = 5000   # Ω
	Vgamma:float = 0.6   # V
	vi_ac:str = 'sin(omega-t)'
	vi_A:float = 0.1   # V

	# ---- Calcs ---------------------
	calc_IDQ:float = ( VPS - Vgamma ) / R

	calc_Vo:float = calc_IDQ * R

	calc_rd:float = self.vthrml0_026 / calc_IDQ

	calc_id_mag:float = vi_A / (calc_rd + R)
	calc_id_mag = round(calc_id_mag,8)

	calc_vo_mag:float = calc_id_mag * R


	ans_string:str = f"""
Divide the analysis into two parts: the dc analysis and the ac analysis.
For the dc analysis, we set vi = 0 and then determine the dc quiescent current
from Figure 1.36(a).

  IDQ = (VPS - Vgamma) / R
      = ({VPS} - {Vgamma}) / {R}
      = {calc_IDQ}A.

The dc value of the output voltage is:

  Vo = IDQ*R = {calc_IDQ} * {R}
     = {calc_Vo}V.

For the ac analysis, only the ac signals and parameters in the circuit
in Figure 1.36(b) are considered. This effectively sets VPS = 0.
The ac KVL equation:

  vi = id*rd + id*R = id*(rd + R)
  where rd is again the small-signal diode diffusion resistance.

Calc rd per Eq 1.32 pg 45:

  rd = VT / IDQ = {self.vthrml0_026} / {calc_IDQ}
     = {calc_rd} Ohm

The ac diode current:

  id = vi / (rd + R) = {vi_A}{vi_ac} / ({calc_rd} + {R})
     = {calc_id_mag}{vi_ac} (A).

The ac component of the output voltage:

  vo = id*R = {calc_id_mag}{vi_ac} * {R}
     = {calc_vo_mag}{vi_ac} (V).

"""
	print( ans_string )

	# print( '---- (a) -------------------------------------------' )

	try:
		assertions.assert_within_percentage( calc_IDQ, ans_IDQ, assert_percentage )
		print( f"ASSERT IDQ = {calc_IDQ}A is within {assert_percentage}% of accepted answer: {ans_IDQ}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )


	# Usage single value:
	# ans_a:float = 0.518e-03   # A
	# try:
	# 	assertions.assert_within_percentage( iDS, ans_a, assert_percentage )
	# 	print( f"ASSERT NMOS iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_a:.3e}." )
	# except AssertionError as e:
	# 	print( f"ASSERT AssertionError {pnum}: {e}" )

	# try:
	# 	assertions.assert_within_percentage( iSD, ans_a, assert_percentage )
	# 	print( f"ASSERT PMOS enhancement mode in saturation: iSD = {round(iSD,7)}V", end=' ' )
	# 	print( f"is within {assert_percentage}% of accepted answer {ans_a}V." )
	# except AssertionError as e:
	# 	print( f"ASSERT AssertionError {pnum}: {e}" )

	# Usage with List:
	# list_calc_iD:List[float] = []   #  don't forget to use list_calc_iD.append(val) to load the list!!
	# ans_a_iDS:Tuple = (0.518e-03, 0.691e-03, 0.691e-03)   #
	# for idx, ans_iDS in enumerate(ans_a_iDS):
	# 	try:
	# 		assertions.assert_within_percentage( list_calc_iDS[idx], ans_iDS, assert_percentage )
	# 		print( f"ASSERT NMOS iDS = {list_calc_iDS[idx]:.3e}A is within {assert_percentage}% of accepted answer: {ans_iDS:.3e}." )
	# 	except AssertionError as e:
	# 		print( f"ASSERT AssertionError {pnum}: {e}" )


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
