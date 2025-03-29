from inspect import currentframe
import math
from typing import Dict, List, Tuple  # Any, Set

from assertions import assertions

def prob6_44b(self):
	"""Page 459:
	The transistor parameters for the circuit in Figure P6.44 are β = 180
	and	VA = inf.  Assume ideal Q1.  See README_chap06.md for figure.
	(b) Plot the dc and ac load lines.
	ANS(b):  See plot.
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
	ICQ:float = 15.7e-03   # A
	VCEQ:float = 10.1      # V
	dict_Qpoint:Dict[str, float] = { 'VCEQ': VCEQ, 'ICQ': ICQ}


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V


	# ---- Calcs ---------------------
	VTh = 0   # by inspection


	print( '\n---- (calc DC load-line) -----------------------' )

	IC0:float = (VCC - VEE) / RE
	VC0:float = VCC - VEE

	dict_DC_load_line:Dict[str, float] = {}
	dict_DC_load_line['IC0'] = IC0
	dict_DC_load_line['VC0'] = VC0

	ans_string:str = f"""
The DC (and AC) load-line is a graph of the transistor's I-V
characteristic, that is, IC (y-asix) vs VCE (x-axis).

The endpoints of the DC load-line cross the IC and VCE axes.
  When VCE = 0, the current IC0 = current thru RE.
	When IC = 0, VCE0 is total voltage across the CE-junction.

  IC0 = (VCC - VEE) / RE
      = ({VCC} - {VEE}) / {RE}
      = {IC0}A.

  VC0 = VCC - VEE
      = {VCC} - {VEE}
      = {VC0}V.

From part (a), Q-point:
  VCEQ = {VCEQ}V.
  ICQ  = {ICQ}A

"""
	print( ans_string )

	plot_load_line( self, dc_ll=dict_DC_load_line, qpoint=dict_Qpoint )

	print( '\n---- (calc AC load-line) -----------------------' )



	ans_string = f"""
.
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )


def plot_load_line( self, dc_ll:Dict[str, float], qpoint:Dict[str, float] ):
	import os
	import pathlib
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator

	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: function: '{fcn_name}'" )

	print( dc_ll )

	x_axis:List = [0, dc_ll['VC0']]
	y_axis:List = [dc_ll['IC0'], 0]

	plt.figure( figsize=self.param_figure_figsize )
	plt.plot( x_axis, y_axis, label='DC load-line', color='blue' )
	# Set titles and labels
	plt.title('P6.44(b) I-V')
	plt.xlabel('VCE(V)')
	xlim_start:float = x_axis[0] - 1
	xlim_stop:float = dc_ll['VC0'] + 2
	plt.xlim( xlim_start, xlim_stop )
	# Set the x-axis to have 12 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=10) )

	plt.ylabel('IC(A)')
	# plt.ylim( -1, 25 )

	# Add a horizontal guide line at origin
	plt.axhline( y=0, color='k', linestyle='-', linewidth=0.2 )
	# Add a vertical guide line at origin
	plt.axvline( x=0, color='k', linestyle='-', linewidth=0.2 )

	# Add Q-point axes
	plt.axhline( y=qpoint['ICQ'], color='r', linestyle='--', linewidth=1.0 )
	# Add a vertical guide line at origin
	plt.axvline( x=qpoint['VCEQ'], color='r', linestyle='--', linewidth=1.0 )

	# Add Q-point
	highlight_x = [qpoint['VCEQ']]  # x-coordinate of the Q-point
	icq:float = qpoint['ICQ']*1000
	highlight_y = [qpoint['ICQ']]   # y-coordinate of the Q-point
	plt.scatter(
		highlight_x, highlight_y, color='r',
		label=f"Q-point: ({qpoint['VCEQ']}V, {icq}mA)"
	)

	# Plot the x- and y-axis crossings
	plt.text( dc_ll['VC0'], 0.001, f"VC0={dc_ll['VC0']}V", fontsize=10, color='k', ha='left', va='top')
	plt.text( 1, dc_ll['IC0'], f"IC0={dc_ll['IC0']}A", fontsize=10, color='k', ha='left', va='top')

	# Display the plot
	plt.tight_layout()
	plt.legend()
	plt.show()
	plt.close()
