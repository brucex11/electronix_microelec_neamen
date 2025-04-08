from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
import equations.equations


def ce_active_Zreflect_BtoE(self):
	"""
	See schematics_for_diagrams_only:
	./LTspice/schematics_for_diagrams_only/bjt_input_thevenin_VTh_RTh.asc.
	./LTspice/schematics_for_diagrams_only/CE_small_signal_AC_equivalent.asc.
	See simulation schematics:
	./LTspice/bjt/ce/CE_active-region.asc.
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

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers -------------------
	ans:float = 0

	# ---- Givens --------------------
	calc_result:float = 0

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------


	ans_string:str = f"""
These are the equations for the AC-eq ckt for CE in active-region.
See file ./docx/png/bjt/CE/CE_small_signal_AC_equivalent.png. 
vTh and RTh have been calculated.

  vThevenin is voltage-divider at Q1 base-node
  on source-side of circuit:

    vTh = [ (R1||R2) / (Rs + R1||R2) ] * Vs

  RTh is equivalent resistance at Q1's base-node 'looking-back'
  toward the source Vs:

    RTH = Rs||R1||R2

Goal here is to derive an equation for ib and substitute into the
equation for the Ohm's Law equation for vLoad.

KVL base-junction loop: (note B = Beta)

  vTh - ib*RTh - (B+1) * ib * [re + RE||RE1] = 0
  Note that ib occurs twice, so rearrange:

  vTh = ib * [RTh + (B+1)*(re + RE||RE1)]   <== vTh

  **> ib = vTh / [RTh + (B+1)*(re + RE||RE1)]

Ohm's Law for load-resistance RL:

  vLoad = -(ic) * (RC||RL)
        = -(B*ib) * (RC||RL)  because ic = B*ib

Substitue for ib (from above):

  vLoad = -B * [vTh / [Rth + (B+1)*(re + RE||RE1)] * (RC||RL)

By substituting for vTh above, now have an equation for Av = vLoad / vs.

  vLoad = -B * [[(R1||R2) / (Rs + R1||R2)] * Vs] / [Rth + (B+1)*(re + RE||RE1)] * (RC||RL)

Divide by vs, use Z-reflection from the base-side to obtain those
resistances, and rearrange and divide all terms by (B+1).

Finally, vLoad / vs:

  Av = vLoad / vs === one huge equation in terms of Beta and R.

There is a simpler way to do this using
Z-reflection and inspection by either option:
  1) Z-reflect base into emitter
  2) Z-reflect emitter into base
___________________________________________________________
Recall that Z-reflection is only used ONCE when calculating
the small-signal equivalent circuit:
  * If Z-reflection is from base->emitter, divide by Beta
  * If Z-reflection is from emiller->base, multiply by Beta
-----------------------------------------------------------

OPTION 1: use Z-reflection base->emitter.

Concepts to recall:
-------------------
1) Since the collector is a current-source, the resistance
   'looking in' is infinite.m


--- AC-equivalent circuit ---
INPUT-side
Input is the voltage at the base-node, call it vd, as the
voltage-divider-calculated voltage.
Determine Rin while ignoring Q1 (Q1 will be addressed for emitter).

  Rin = R1||R2

Therefore, the voltage-divider 'output' voltage vd:

  INPUT **> vd = (R1||R2) * vs / (Rs + R1||R2)


GAIN-section
By inspection, the gain is determined by 'all R as seen by'
the collector divided by 'all R as seen by' the emitter.

  A = RC-equivalent / RE-equivalent

Since the collector is a current-source, for the collector branch:

  RC-equiv = RC.

For RE-equiv, the resistances 'seen' by the emitter branch are:
  * Z-reflection back into the base; when this is done,
    DIVIDE all resisistance by Beta.
  * re + (RE||RE1)

  Rz = (Rs||R1||R2) / Beta

  RE-equiv = Rz + re + (RE||RE1)

  **>  A = -RC / [Rz + re + (RE||RE1)]


OUTPUT-side
The voltage-divider 'output' voltage vLoad is driven by the
source-voltage vs:

  OUTPUT **> vLoad = vs * (RL / (RC + RL))

Therefore, vLoad is the product of INPUT, GAIN-section, and OUTPUT:

  vLoad = INPUT * GAIN-section * OUTPUT

For the ratio that is the linear-gain, Av, divide-it from OUTPUT:

  **>  Av = vLoad / vs
          = INPUT * GAIN-section * (RL / (RC + RL))



"""
	print( ans_string )

	print( '\n---- (a) -------------------------------------------' )


	try:
		assert_within_percentage( calc_result, ans, assert_percentage )
		print( f"ASSERT ID = {calc_result}A is within {assert_percentage}% of accepted answer: {ans}." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	print( f"--- END {self.prob_str} ---" )


# 	for idx, ans in enumerate(answers2):
# 		try:
# 			assertions.assert_within_percentage( calc_result[idx], ans, 3.0 )
# 			print( f"ASSERT when IS = {IS}A and VD = {diode_voltages[idx]}, diode current ID = {calc_result[idx]}A" )
# 		except AssertionError as e:
# 			print( f"ASSERT AssertionError {pnum}: {e}" )

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
