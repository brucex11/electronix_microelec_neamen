from inspect import currentframe
import math
from typing import Any, Dict, List, Tuple  #  Dict, Set

from assertions.assertions import assert_within_percentage
import equations.equations


def ce_collector_IV_char(self):
	"""
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

	#  α   β   Ω   μ   λ   ξ   ω  π

	# ---- Answers -------------------
	ans:float = 0   #

	# ---- Givens --------------------

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------
	calc_result:float = 0

	# vt:float = self.thermal_voltage( TK=300 )
	# print( f"VT: {vt}" )

	ans_string:str = f"""
"""
	print( ans_string )

	print( '\n---- (a) -------------------------------------------' )

	# iDS for VGS = 2V
	vGS_2:float = 2    # V
	iv_params:Dict = {}
	iv_params['IS'] = 1e-14
	iv_params['TK'] = 300
	iv_params['VA'] = 100
	iv_params['VBE'] = 0.7
	iv_params['VCE'] = 0
	IC:float = self.bjt_collector_IV_characteristic_IC( **iv_params )
	print( f"IC: {IC}A" )

	iv_params.clear()
	iv_params['IS'] = 1e-14
	iv_params['TK'] = 300
	iv_params['VA'] = 80
	iv_params['VBE'] = 0.68
	plot_params:Dict = {}
	plot_params['VCE_max_volts'] = 30
	plot_params['VCE_list_count'] = 200
	iv_params['plot_params'] = plot_params
	# Run first time to generate the VCE range; list_IC not used.
	dict_IV:Dict[str,Any] = self.bjt_collector_IV_characteristic_IC_list( **iv_params )
	list_VCE:List[float] = dict_IV['VCE']

	# Loop through the range of VBE values to create individual lists of IC
	# values that are plotted against list_VCE.
	list_list_IC:List[float] = []
	list_VBE:List[float] = [0.69,0.695, 0.70, 0.705, 0.71]
	list_ro:List[str] = []
	for VBE in list_VBE:
		iv_params['VBE'] = VBE
		dict_IV:Dict[str,Any] = self.bjt_collector_IV_characteristic_IC_list( **iv_params )
		list_list_IC.append( dict_IV['IC'] )
		# Prep ro for string to plot legend in kΩ.
		ro:float = round(dict_IV['ro'] / 1000, 1)
		ro_str:str = f"{str(ro)}k"
		print( f"ro = {dict_IV['ro']}" )
		list_ro.append( ro_str )
		dict_IV.clear()

	# iv_params['VBE'] = 0.7
	# dict_IV = self.bjt_collector_IV_characteristic_IC_list( **iv_params )
	# list_list_IC.append(dict_IV['IC'])

	# plot_IV( self, dict_IV['VCE'], dict_IV['IC'] )
	plot_list_IV( self,
		list_VCE=list_VCE,
		list_list_IC=list_list_IC,
		list_VBE=list_VBE,
		list_ro=list_ro,
		IS=str(iv_params['IS'])
	)

	# try:
	# 	assert_within_percentage( calc_result, ans, assert_percentage )
	# 	print( f"ASSERT ID = {calc_result}A is within {assert_percentage}% of accepted answer: {ans}." )
	# except AssertionError as e:
	# 	print( f"AssertionError {pnum}: {e}" )



def plot_IV(self, x:List[float]=[], y:List[float]=[] ):
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator

	x = x
	y = y

	plt.figure( figsize=self.param_figure_figsize )
	plt.plot(x, y, color='b')

	# Set titles and labels
	plt.title('Collector IV')
	plt.xlabel('VCE(V)')
	# plt.xlim( -2.5, 1 )
	# Set the x-axis to have 12 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

	plt.ylabel('IC(A)')
	# plt.ylim( -1, 25 )
	# plt.yscale( 'log' )

	# Display the plot
	plt.show()
	plt.close()



def plot_list_IV(self,
	list_VCE:List[float]=[],
	list_list_IC:List[float]=[],
	list_VBE:List[float]=[],
	list_ro:List[str]=[],
	IS:str='' ):

	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator

	plt.figure( figsize=self.param_figure_figsize )

	x = list_VCE
	line_color:List[str] = ['r', 'b', 'b', 'b', 'g', 'b', 'b', 'b', 'b']
	for idx, list_IC in enumerate(list_list_IC):
		y = list_IC
		plt.plot(x, y, color=line_color[idx], label=f"VBE={list_VBE[idx]},ro={list_ro[idx]}")

	# Set titles and labels
	plt.title( f"CE Collector I-V, IS={IS}A" )
	plt.xlabel('VCE(V)')
	# plt.xlim( -2.5, 1 )
	# Set the x-axis to have 12 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

	plt.ylabel('IC(A)')
	# plt.ylim( -1, 25 )
	# plt.yscale( 'log' )

	# Add a vertical guide line at VCE(sat)
	plt.axvline( x=0.3, color='k', label='VCE(sat)=0.3', linestyle='--', linewidth=1.0 )

	# Display the plot
	plt.legend()
	plt.show()
	plt.close()
