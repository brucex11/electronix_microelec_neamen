from inspect import currentframe
# import math
# from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob5_17(self):
	"""Page 353:
	For all the transistors in Figure P5.17, β = 75. The results of some
	measurements are indicated on the figures. Find the values of the other
	labeled currents, voltages, and/or resistor values.
	ANS:  (a) iC =  1.836mA, RC =  3.65kΩ
 	ANS:  (b) VB = 0.164V, RC =  8.11kΩ
	ANS:  (c) VCE = 1.96V, iC = 1.744mA
	ANS:  (d) VC = 1.49V, iB = 4.61μA."
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
	print( '-----------------------------------------------\nSolution' )

	# ---- Answers -------------------
	ans_a_iC:float = 1.836e-03   # A
	ans_a_RC:float = 3.65e+03    # Ω

	ans_b_VB:float = 0.164       # V
	ans_b_RC:float = 8.11e+03    # Ω

	ans_c_VCE:float = 1.96       # V
	ans_c_iC:float = 1.744e-03   # A

	ans_d_VC:float = 1.49        # V
	ans_d_iB:float = 4.61e-06    # A

	# ---- Assumptions --------------------
	VBE_NPN:float = 0.7   # V


	# ---- Givens (a) --------------------
	Beta:float = 75
	VCC_a:float = 10    # V
	VEE_a:float = -10   # V
	VCE_a:float = 4     # V
	RE_a:float = 5000   # Ω
	VB_a:float = 0   # V, by inspection

	# ---- Givens (d) --------------------
	VCC_d:float = 5       # V
	RC_d:float = 10e+03   # Ω
	RB_d:float = 20e+03   # Ω
	RE_d:float = 2e+03    # Ω



	ans_string:str = """
Per schematics per Figure P5.17, some BJT characteristics may be assumed.
For example, for NPN, VBE ~= 0.7V,  for PNP, VBE = -0.7V
"""
	print( ans_string )


	print( '---- (Fig P5.17 a) -------------------------------------------', end='' )

	calc_VE:float = ( VB_a - VBE_NPN )
	calc_iE = ( calc_VE - VEE_a) / RE_a
	calc_iC:float = ( Beta / ( 1 + Beta) ) * calc_iE
	calc_iC = round(calc_iC,6)

	ans_string = f"""
Assume VBE is typical 0.7V, therefore VE = ( VB - VBE )
  where VB = {VB_a}V
  VE = VB - VBE = {calc_VE}V

Current OUT of emitter and through RE, calculate iE = (VE - VEE) / RE
iE = ( {calc_VE} - ({VEE_a}) ) / {RE_a}
iE = {calc_iE}A = {calc_iE*1000}mA

With iE now known, calculate iC = ( Beta / 1 + Beta ) * iE   Eq (5.10)
iC = ( {Beta}) / ( 1 + {Beta}) ) * {calc_iE}
iC = {calc_iC}A = {round(calc_iC*1000,6)}mA
"""
	print( ans_string )

	try:
		assertions.assert_within_percentage( calc_iC, ans_a_iC, assert_percentage )
		print( f"ASSERT iC = {calc_iC}A is within {assert_percentage}% of accepted answer: {ans_a_iC}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	calc_VC:float = calc_VE + VCE_a
	calc_RC:float = ( VCC_a - calc_VC ) / calc_iC
	calc_RC = round(calc_RC,-1)

	ans_string:str = f"""
To calculate RC, find the voltage drop across it and divide by current iC.
Therefore, find VC = VE + VCE.
VC = {calc_VE} + {VCE_a}
VC = {calc_VC}V
RC = ( VCC - VC ) / iC
RC = ( {VCC_a} - {calc_VC} ) / {calc_iC}
RC = {calc_RC}ohm = {round(calc_RC/1000,2)}kohm
"""
	print( ans_string )


	try:
		assertions.assert_within_percentage( calc_RC, ans_a_RC, assert_percentage )
		print( f"ASSERT RC = {calc_RC}ohm is within {assert_percentage}% of accepted answer: {ans_a_RC}ohm." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	print( '---- (Fig P5.17 d) -------------------------------------------', end='' )

	ans_string = f"""
At node VC, iC and iB flow INTO the transistor Q1, and therefore flow OUT
of the node VC.
Since iE = iC + iB, then the current INTO node VC MUST = iE by KCL.

With one equation ( KVL through RC, RB, Q1-BE-junction and RE and one
unknown, namely iE, iE is calculated.

Use iE = (1 + Beta)iB for RB current.

Once iE is known, along with Q1's Beta, iB and iC are calculated.

KVL:
VCC - iB*RB - VBE - iRE*RE = 0
and,
iB = iE / (1 + Beta)   Eq (5.9)

Substitute for iB and iRE (where iRE is in series with emitter)

  **>  VCC - iE*RC - ( iE / (1 + Beta) )*RB - VBE - iE*RE = 0

Solve equation above for iE, assume VBE = 0.7V
"""
	print( ans_string )

	clac_denom:float = ( ( 1 / (1 + Beta)) * RB_d ) + RE_d + RC_d
	calc_iE:float = ( VCC_d - VBE_NPN ) / clac_denom
	calc_iE = round(calc_iE,7)
	print( f"iE = {calc_iE}A = {round(calc_iE,7)*1000}mA" )

	print( f"Per iE = (1 + Beta)iB    Eq (5.9), calculate iB." )
	calc_iB:float = calc_iE / (1+Beta)
	calc_iB = round(calc_iB,8)
	# print( f"iB = {calc_iB}A = {round(calc_iB,8)*1e+06}uA." )

	try:
		assertions.assert_within_percentage( calc_iB, ans_d_iB, assert_percentage )
		print( f"ASSERT iB = {calc_iB}A is within {assert_percentage}% of accepted answer: {ans_d_iB}A." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )


	print( f"VC is the voltage-drop across RC: VC = VCC - iE*RC\n" )
	calc_VC:float = VCC_d - calc_iE * RC_d
	calc_VC = round(calc_VC,2)

	try:
		assertions.assert_within_percentage( calc_VC, ans_d_VC, assert_percentage )
		print( f"ASSERT VC = {calc_VC}V is within {assert_percentage}% of accepted answer: {ans_d_VC}V." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	# print( f"VC is the voltage-drop across RC: VC = VCC - iE*RC" )

	print( f"\n--- END {self.prob_str} ---" )








	# try:
	# 	assertions.assert_within_percentage( calc_iC, ans_a_iC, assert_percentage )
	# 	print( f"ASSERT iC = {calc_iC}A is within {assert_percentage}% of accepted answer: {ans_a_iC}A." )
	# except AssertionError as e:
	# 	print( f"ASSERT AssertionError {pnum}: {e}" )

	# print( f"\n--- END {self.prob_str} ---" )


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
