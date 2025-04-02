from inspect import currentframe
from typing import Dict, List, Tuple  # Any, Set

from equations import equations

def prob6_76b(self):
	"""Page 466:
	Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(a) Determine the small-signal parameters gm, rπ, and ro for both transistors.
	(b) Plot the dc and ac load lines for both transistors.
	(c) Determine the overall small-signal voltage gain Av = vo/vs.
	(d) Determine the input resistance Ris and the output resistance Ro.
	(e) Determine the maximum undistorted swing in the output voltage.
	ANS(a):  IBQ1 = 4.77e-06A,  IEQ1 = 0.577mA, ICQ1 = 0.572mA, VCEQ1 = 5.13V
				:  IBQ2 = 4.052e-05A, IEQ2 = 4.90mA, ICQ2 = 4.86mA, VCEQ2 = 4.16V
	ANS(b):  See ./docx/chap06/problem/chap06_prob6_76b.docx
	             ./docx/png/chap06_prob6_76b_Q1_acdc_load_lines.png
	             ./docx/png/chap06_prob6_76b_Q2_acdc_load_lines.png
	ANS(c):  
	ANS(d):  
	ANS(e):
	Tue, Apr  1, 2025  3:14:12 PM
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

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers -------------------
	ans_ICQ = 15.7e-03   # A
	ans_VCEQ = 10.1      # V

	# ---- Givens per (a) --------------------
	IBQ_Q1 = 4.77e-06    # A
	IEQ_Q1 = 0.577e-03   # A
	ICQ_Q1 = 0.572e-03   # A
	VCEQ_Q1 = 5.13       # V
	dict_Q1_Qpoint:Dict[str, float] = { 'VCEQ': VCEQ_Q1, 'ICQ': ICQ_Q1}
	IBQ_Q2 = 4.052e-05  # A
	IEQ_Q2 = 4.90e-03   # A
	ICQ_Q2 = 4.86e-03   # A
	VCEQ_Q2 = 4.16      # V
	dict_Q2_Qpoint:Dict[str, float] = { 'VCEQ': VCEQ_Q2, 'ICQ': ICQ_Q2}

	# ---- Givens per problem --------------------
	Beta:float = 120  # both Q1 and Q2
	VCC:float = 12
	VEE:float = 0

	# Q1
	R1:float = 67.3e+03
	R2:float = 12.7e+03
	RC1:float = 10000
	RE1:float = 2000

	# Q2
	R3:float = 15e+03
	R4:float = 45e+03
	RE2:float = 1.6e+03

	# Load
	RL:float = 250

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V


	print( '\n---- (calc Q1 DC load-line) -----------------------' )

	IC0_Q1:float = (VCC - VEE) / (RC1 + RE1)
	VCE0_Q1:float = VCC - VEE

	dict_Q1_DC_load_line:Dict[str, float] = { 'VCE0': VCE0_Q1, 'IC0': IC0_Q1 }


	ans_string:str = f"""
The DC (and AC) load-line is a graph of the transistor's
collector I-V characteristic, that is, IC (y-axis) vs VCE (x-axis).

The endpoints of the DC load-line cross the IC and VCE axes.
  When VCE = 0, the current IC0 = current thru RC1 + RE1.
  When IC = 0, VCE0 is total voltage across the CE-junction.

  IC0_Q1 = (VCC - VEE) / (RC1 + RE1)
         = ({VCC} - {VEE}) / ({RC1} + {RE1})
         = {IC0_Q1}A.

  VCE0_Q1 = VCC - VEE
          = {VCC} - {VEE}
          = {VCE0_Q1}V.

From part (a), Q-point:
  VCEQ = {VCEQ_Q1}V.
  ICQ  = {ICQ_Q1}A

"""
	print( ans_string )


	print( '---- (calc Q1 AC load-line) -----------------------' )

	rpi_Q2:float = self._vthrml0_026 / IBQ_Q2
	rpi_Q2 = round(rpi_Q2,1)
	RE2_parallel_RL = equations.r1_parallel_r2( RE2, RL )
	Rib_Q2:float = rpi_Q2 + (1+Beta)*RE2_parallel_RL
	Rib_Q2 = round(Rib_Q2,0)
	list_Ri_Q2:List[float] = [ R3, R4, Rib_Q2 ]
	Ri_Q2:float = equations.equivalent_parallel_resisitance( list_Ri_Q2 )
	Ri_Q2 = round(Ri_Q2,0)

	ro_Q1:float = equations.r1_parallel_r2( RC1, Ri_Q2 )
	ro_Q1 = round(ro_Q1,0)
	ac_slope_Q1:float = -1 / ro_Q1

	# Calculate AC load-line endpoints for plotting.  With slope now known,
	# use the equation of a line to find ic0 (b = y-intercept), and vce0.
	# NB: do NOT round these values; plot's Q-point is offset from intersection
	# of DC and AC load-lines.
	ic0:float = ICQ_Q1 - ac_slope_Q1 * VCEQ_Q1
	vce0:float = -ic0 / ac_slope_Q1
	dict_Q1_AC_load_line:Dict[str, float] = { 'vce0': vce0, 'ic0': ic0 }


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

For the Q1's collector I-V characteristic, the AC load-line crosses Q1's
DC Q-point.  The slope of the AC load-line = delta_ic / delta_vce where the
lower-case 'ic' and 'vce' notations refer to instantaneous AC values.

Once the AC load-line slope is determined, it is plotted on the collector
I-V characteristic graph and it values 'become' total instantaneous values
per the notations 'iC' and 'vCE'.

For AC signals, the current in the collector is "split" between RC1, R3, R4,
and Q2's Rib (base input resistance).  Since RE1 is bypassed by CE, the
emitter as at ground and therefore the resistance against the Q1 collector
current is infinite (again, ground acts like an open-circuit to AC).

To determine Q2's Rib, first calculate its rpi:

  rpiQ2 = VT / IBQ_Q2
        = {self._vthrml0_026} / {IBQ_Q2}
        = {rpi_Q2}ohm
Then,
  **>  Q2 Rib = rpiQ2 + (1+Beta) * (RE2||RL)
              = {rpi_Q2} + (1+{Beta}) * (RE2_parallel_RL)
              = {rpi_Q2} + (1+{Beta}) * (RE2_parallel_RL)
              = {Rib_Q2}ohm.

Therefore, Q2's input resistance (seen at Q1's collector) is
Ri_Q2 = R3||R4||Q2-Rib.

  Ri_Q2 = {R3}||{R4}||{Rib_Q2}
        = {Ri_Q2}ohm.

Finally, Q1's output resistance is RC1||Ri_Q2.

  Ro_Q1 = {RC1}||{Ri_Q2}
        = {ro_Q1}ohm.

Calculate DC and AC load-line endpoints for plotting.

  ac_slope_Q1 = -1 / Q1-ro
              = -1 / {ro_Q1}mA/V.

  ic0 is y-intercept = ICQ_Q1 - ac_slope_Q1 * VCEQ_Q1
                     = {ICQ_Q1} - {ac_slope_Q1} * {VCEQ_Q1}
                     = {round(ic0,4)}A.
"""
	print( ans_string )

	plot_load_lines( self, dc_ll=dict_Q1_DC_load_line, ac_ll=dict_Q1_AC_load_line, qpoint=dict_Q1_Qpoint, title='P6.76(b) Q1 collector I-V' )


	print( '\n---- (calc Q2 DC load-line) -----------------------' )

	IC0:float = (VCC - VEE) / RE2
	VCE0:float = VCC - VEE

	dict_Q2_DC_load_line:Dict[str, float] = { 'VCE0': VCE0, 'IC0': IC0 }


	ans_string:str = f"""
The DC (and AC) load-line is a graph of the Q2's collector I-V
characteristic, that is, IC (y-axis) vs VCE (x-axis).

The endpoints of the DC load-line cross the IC and VCE axes.
  When VCE = 0, the current IC0 = current thru RE2.
	When IC = 0, VCE0 is total voltage across the CE-junction.

  IC0 = (VCC - VEE) / RE2
      = ({VCC} - {VEE}) / {RE2}
      = {IC0}A.

  VCE0 = VCC - VEE
       = {VCC} - {VEE}
       = {VCE0}V.

From part (a), Q-point:
  VCEQ = {VCEQ_Q2}V.
  ICQ  = {ICQ_Q2}A

"""
	print( ans_string )


	print( '\n---- (calc Q2 AC load-line) -----------------------' )

	RE_pllel_RL:float = equations.r1_parallel_r2( RE2, RL )
	ac_slope:float = -1 / RE_pllel_RL

	ic0:float = ICQ_Q2 - ac_slope * VCEQ_Q2
	# ic0 = round(ic0,4)
	vce0:float = -ic0 / ac_slope
	# vce0 = round(vce0,2)

	dict_Q2_AC_load_line:Dict[str, float] = { 'vce0': vce0, 'ic0': ic0 }


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

For the transistor's collector I-V characteristic, the AC load-line crosses
the circuit's DC Q-point.  The slope of the AC load-line =
delta_ic / delta_vce where the lower-case 'ic' and 'vce' notations refer
to instantaneous AC values.

Once the AC load-line slope is determined, it is plotted on the collector
I-V characteristic graph and it values 'become' total instantaneous values
per the notations 'iC' and 'vCE'.

For AC signals, the current in the emitter is "split" between the emitter
resistor RE2 and the load resistor RL because the capacitor CC3 is treated
as a short-circuit.  The effetive emitter "resistor" to ic current is RE2||RL.

  RLeffective = RE2||RL
              = {RE2} || {RL}
              = {RE2} || {RL}
              = {round(RE_pllel_RL,0)}ohm.

For the AC-equivalent circuit for output branch that includes Q2, RE2, and RL
(per KVL and VCC = VEE = 0):

  **>  vce - vRLeff = 0
       vce = vRLeff.

However, vce and vRLeff are inversely proportional because as:
  1) vce increases, ic decreases
  2) and when ic decreases, so follows vRLeff.

Therefore:

  **>  vce = -vRLeff = -icRLeff

For AC load-line, its slope = rise/run = ic / vce:

  **>  ic / vce = -( 1 / RLeff )

Calculate the AC load-line endpoints:  vce0 @ ic=0, ic0 @ vce=0
  vce0 = -ic0 / ac_slope
       = -{ic0} / {ac_slope}
       = {round(vce0,2)}V
  ic0 = ICQ_Q2 - ac_slope * VCEQ_Q2
      = {ICQ_Q2} - {ac_slope} * {VCEQ_Q2}
      = {round(ic0,4)}A.

Plot the load-lines.
"""
	print( ans_string )

	plot_load_lines( self, dc_ll=dict_Q2_DC_load_line, ac_ll=dict_Q2_AC_load_line, qpoint=dict_Q2_Qpoint, title='P6.76(b) Q2 collector I-V' )

	print( f"--- END {self.prob_str} ---" )


def plot_load_lines( self,
	dc_ll:Dict[str, float],
	ac_ll:Dict[str, float],
	qpoint:Dict[str, float],
	title:str ):
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator

	# fcn_name:str = currentframe().f_code.co_name
	# print( f"ENTRYPOINT: function: '{fcn_name}'" )

	print( f"Q-point: {qpoint}" )
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
	plt.title(title)
	plt.xlabel('VCE(V)')
	xlim_start:float = x_axis[0] - 1
	xlim_stop:float = dc_ll['VCE0'] + 2
	plt.xlim( xlim_start, xlim_stop )
	# Set the x-axis to have 12 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

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
	icq:float = round(qpoint['ICQ']*1000,6)
	highlight_y = [qpoint['ICQ']]   # y-coordinate of the Q-point
	plt.scatter(
		highlight_x, highlight_y, color='r',
		label=f"Q-point: ({qpoint['VCEQ']}V, {icq}mA)"
	)

	# Plot the x- and y-axis crossings
	# DC load-line
	plt.text( dc_ll['VCE0'], 0.00005,  f"{round(dc_ll['VCE0'],2)}", fontsize=10, color='k', ha='left', va='top')
	plt.text( 0, dc_ll['IC0']+0.00004, f"{round(dc_ll['IC0'],4)}", fontsize=10, color='k', ha='left', va='top')
	# AC load-line
	plt.text( ac_ll['vce0'], 0.00005,  f"{round(ac_ll['vce0'],2)}", fontsize=10, color='k', ha='left', va='top')
	plt.text( 0, ac_ll['ic0']+0.00004, f"{round(ac_ll['ic0'],4)}", fontsize=10, color='k', ha='left', va='top')

	# Display the plot
	plt.tight_layout()
	plt.legend()
	plt.show()
	plt.close()
