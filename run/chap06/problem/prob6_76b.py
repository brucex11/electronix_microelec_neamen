from inspect import currentframe
from typing import Dict, List, Tuple  # Any, Set

from equations.equations import r1_parallel_r2
def prob6_76b(self):
	"""Page 466:
	Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(a) Determine the small-signal parameters gm, rπ, and ro for both transistors.
	(b) Plot the dc and ac load lines for both transistors.
	(c) Determine the overall small-signal voltage gain Av = vo/vs.
	(d) Determine the input resistance Ris and the output resistance Ro.
	(e) Determine the maximum undistorted swing in the output voltage.
	ANS(a):  ICQ1 = 5.72AmA, VCEQ1 = 5.13V
	      :  ICQ2 = 4.86mA, VCEQ2 = 4.16V
	ANS(b):  See ./docx/chap06/problem/chap06_prob6_76.docx
	ANS(c):  
	ANS(d):  
	ANS(e):
	Mon, Mar 31, 2025 12:03:39 PM
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
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
	RS:float = 1000
	RE:float = 500
	RL:float = 300
	ICQ:float = 15.7e-03   # A
	VCEQ:float = 10.1      # V
	dict_Qpoint:Dict[str, float] = { 'VCEQ': VCEQ, 'ICQ': ICQ}


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V


	# ---- Calcs ---------------------
	# VTh = 0   # by inspection


	print( '\n---- (calc DC load-line) -----------------------' )

	IC0:float = (VCC - VEE) / RE
	VCE0:float = VCC - VEE

	dict_DC_load_line:Dict[str, float] = { 'VCE0': VCE0, 'IC0': IC0 }


	ans_string:str = f"""
The DC (and AC) load-line is a graph of the transistor's I-V
characteristic, that is, IC (y-axis) vs VCE (x-axis).

The endpoints of the DC load-line cross the IC and VCE axes.
  When VCE = 0, the current IC0 = current thru RE.
  When IC = 0, VCE0 is total voltage across the CE-junction.

  IC0 = (VCC - VEE) / RE
      = ({VCC} - {VEE}) / {RE}
      = {IC0}A.

  VCE0 = VCC - VEE
       = {VCC} - {VEE}
       = {VCE0}V.

From part (a), Q-point:
  VCEQ = {VCEQ}V.
  ICQ  = {ICQ}A

"""
	print( ans_string )

	# plot_load_lines( self, dc_ll=dict_DC_load_line, qpoint=dict_Qpoint )

	print( '\n---- (calc AC load-line) -----------------------' )

	RE_pllel_RL:float = r1_parallel_r2( RE, RL )
	ac_slope:float = -1 / RE_pllel_RL

	ic0:float = ICQ - ac_slope * VCEQ
	ic0 = round(ic0,4)
	vce0:float = -ic0 / ac_slope
	vce0 = round(vce0,2)

	dict_AC_load_line:Dict[str, float] = { 'vce0': vce0, 'ic0': ic0 }


	ans_string = f"""
For AC analysis, the only required value is the DC Q-point.  For AC signals
in an AC-equivalent circuit, voltages sources act like grounds since their
voltage is (assumed) constant and therefore AC-currents CANNOT/WILL-NOT produce
any change in voltage.
Conversely this is the same for AC-current sources; they act like grounds since
their current is (assumed) constant and therefore AC-voltages CANNOT/WILL-NOT
produce any change in current.

It follows that for the AC-equivalent circuit:
  * AC-voltage sources are "replaced" by short-circuits and act like ground
  * AC-current sources are "replaced" by open-circuits and act like ground

For the transistor's I-V characteristic, the AC load-line crosses the circuit's
DC Q-point.  The slope of the AC load-line = delta_ic / delta_vce where the
lower-case 'ic' and 'vce' notations refer to instantaneous AC values.

Once the AC load-line slope is determined, it is plotted on the
I-V characteristic graph and it values 'become' total instantaneous values
per the notations 'iC' and 'vCE'.

For AC signals, the current in the emitter is "split" between the emitter
resistor RE and the load resistor RL because the capacitor CC2 is treated
as a short-circuit.  The effective emitter load "resistor" to the ic current
is RE||RL.

  RLeffective = RE||RL
              = {RE} || {RL}
              = {RE_pllel_RL}ohm.

For the AC-equivalent circuit for output branch that includes Q1, RE, and RL
(per KVL and VCC = VEE = 0):

  **>  vce - vRLeff = 0
       vce = vRLeff.

However, vce and vRLeff are inversely proportional because:
  1) as vce increases, ic decreases
  2) and when ic decreases, so follows vRLeff.

Therefore:

  **>  vce = -vRLeff = -icRLeff

For AC load-line, its slope = rise/run = ic / vce:

  **>  ic / vce = -( 1 / RLeff )

Calculate the AC load-line endpoints:  vce0 @ ic=0, ic0 @ vce=0:
  > vce0 = {round(vce0,2)}V
  > ic0 = {round(ic0,4)}A.

Plot the load-lines.
"""
	print( ans_string )

	plot_load_lines( self, dc_ll=dict_DC_load_line, ac_ll=dict_AC_load_line, qpoint=dict_Qpoint )

	print( f"--- END {self.prob_str} ---" )


def plot_load_lines( self, dc_ll:Dict[str, float], ac_ll:Dict[str, float], qpoint:Dict[str, float] ):
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator

	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: function: '{fcn_name}'" )

	print( f"DC load-line endpoints: {dc_ll}" )
	print( f"AC load-line endpoints: {ac_ll}" )

	plt.figure( figsize=self.param_figure_figsize )

	# DC load-line
	x_axis:List = [0, dc_ll['VCE0']]
	y_axis:List = [dc_ll['IC0'], 0]
	plt.plot( x_axis, y_axis, label='DC load-line', color='b' )

	# AC load-line
	x_axis:List = [0, ac_ll['vce0']]
	y_axis:List = [ac_ll['ic0'], 0]
	plt.plot( x_axis, y_axis, label='AC load-line', color='g' )

	# Set titles and labels
	plt.title('P6.44(b) NPN I-V')
	plt.xlabel('VCE(V)')
	xlim_start:float = x_axis[0] - 1
	xlim_stop:float = dc_ll['VCE0'] + 2
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
	# DC load-line
	plt.text( dc_ll['VCE0'], 0.003, f"{dc_ll['VCE0']}", fontsize=10, color='k', ha='left', va='top')
	plt.text( 0, dc_ll['IC0']+0.003, f"{dc_ll['IC0']}", fontsize=10, color='k', ha='left', va='top')
	# AC load-line
	plt.text( ac_ll['vce0'], 0.003, f"{ac_ll['vce0']}", fontsize=10, color='k', ha='left', va='top')
	plt.text( 0, ac_ll['ic0']+0.003, f"{ac_ll['ic0']}", fontsize=10, color='k', ha='left', va='top')

	# Display the plot
	plt.tight_layout()
	plt.legend()
	plt.show()
	plt.close()
