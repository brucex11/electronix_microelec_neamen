from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob6_44assumeIB(self):
	"""Page 459:
	The transistor parameters for the circuit in Figure P6.44 are β = 180
	and	VA = inf.  Assume IB = 75μA.  See README_chap06.md for figure.
	(a) Find ICQ and VCEQ.
	(b) Plot the dc and ac load lines.
	(c) Calculate the small-signal voltage gain.
	(d) Determine the input and output resistances Rib and Ro.
	ANS(a):  ICQ = 15.7mA, VCEQ = 10.1V
	ANS(c):  
	ANS(d):  
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	# assert_percentage:float = 1.0
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω

	# ---- Answers -------------------
	ans_ICQ = 15.7e-03   # A
	ans_VCEQ = 10.1      # V

	# ---- Givens --------------------
	Beta:float = 180
	VCC:float = 9
	VEE:float = -9
	R1:float = 10000
	R2:float = 10000
	RE:float = 500


	# ---- Assumptions ---------------
	VBE:float = 0.731   # V
	IB:float = 75e-06


	# ---- Calcs ---------------------

	print( '\n---- (calc VB) -------------------------------------------' )

	calc_IR1:float = VCC / R1
	calc_IR2:float = VEE / R2

	calc_VB:float = -1 * ( (IB - calc_IR1 - calc_IR2) / ( (1/R1) + (1/R2) ) )
	calc_VB:float = -( IB - VEE/R2 - VCC/R1 ) / (1/R1 + 1/R2)
	calc_VB = round(calc_VB,4)

	ans_string:str = f"""
Since IB is NOT zero, assume IB = {IB*1000000}uA.

Use KCL at node VB:

  **>  IR1 = IB + IR2

Then,
IR1 = (VCC - VB) / R1
IR2 = (VB - VEE) / R2

  **>  (VCC - VB) / R1 = IB + (VB - VEE) / R2

Now with one equation-one unknown, solve for VB:

  (VCC - VB) / R1 = IB + (VB - VEE) / R2  <**
  VCC/R1 - VB/R1 = IB + VB/R2 - VEE/R2
  -VB/R1 - VB/R2 = IB - VEE/R2 - VCC/R1
  -VB(1/R1 + 1/R2) = IB - VEE/R2 - VCC/R1
  -VB = ( IB - VEE/R2 - VCC/R1 ) / (1/R1 + 1/R2)
   VB = -( IB - VEE/R2 - VCC/R1 ) / (1/R1 + 1/R2)  <==== THIS SOLVES FOR VB

   VB = -( {IB} - {VEE}/{R2} - {VCC}/{R1} ) / (1/{R1} + 1/{R2})
      = {calc_VB}V.
"""
	print( ans_string )


	print( '\n---- (calc ICQ and VCEQ) ---------------------------------' )

	calc_VE:float = calc_VB - VBE
	calc_VE = round(calc_VE,5)

	calc_IE = ( calc_VE - VEE ) / RE

	calc_ICQ:float = IB + calc_IE

	calc_VCEQ:float = VCC - calc_VE

	ans_string = f"""
Using transistor current relations equations, assume VBE = {VBE}V:

  VE = VB - VBE
     = {calc_VB} - {VBE}
     = {calc_VE}V.

  IE = (VE - VEE) / RE
     = ({calc_VE} - {VEE}) / {RE}
     = {calc_IE}

  ICQ = IB + IE
      = {IB} + {calc_IE}
      = {calc_ICQ}A.

  VCEQ = VCC - VE
       = {VCC} - ({calc_VE})
       = {calc_VCEQ}V.
"""
	print( ans_string )


	assert_percentage:float = 1.4
	try:
		assertions.assert_within_percentage( calc_ICQ, ans_ICQ, assert_percentage )
		print( f"ASSERT ICQ = {calc_ICQ}A is within {assert_percentage}% of accepted answer: {ans_ICQ}A." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )

	assert_percentage = 1.0
	try:
		assertions.assert_within_percentage( calc_VCEQ, ans_VCEQ, assert_percentage )
		print( f"ASSERT VCEQ = {calc_VCEQ}V is within {assert_percentage}% of accepted answer: {ans_VCEQ}V." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	print( f"\n--- END {self.prob_str} ---" )





	# Usage single value:
	# ans_a:float = 0.518e-03   # A
	# try:
	# 	assertions.assert_within_percentage( iDS, ans_a, assert_percentage )
	# 	print( f"ASSERT NMOS iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_a:.3e}." )
	# except AssertionError as e:
	# 	print( f"AssertionError {pnum}: {e}" )

	# try:
	# 	assertions.assert_within_percentage( iSD, ans_a, assert_percentage )
	# 	print( f"ASSERT PMOS enhancement mode in saturation: iSD = {round(iSD,7)}V", end=' ' )
	# 	print( f"is within {assert_percentage}% of accepted answer {ans_a}V." )
	# except AssertionError as e:
	# 	print( f"AssertionError {pnum}: {e}" )

	# Usage with List:
	# list_calc_iD:List[float] = []   #  don't forget to use list_calc_iD.append(val) to load the list!!
	# ans_a_iDS:Tuple = (0.518e-03, 0.691e-03, 0.691e-03)   #
	# for idx, ans_iDS in enumerate(ans_a_iDS):
	# 	try:
	# 		assertions.assert_within_percentage( list_calc_iDS[idx], ans_iDS, assert_percentage )
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
