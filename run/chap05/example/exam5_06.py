from inspect import currentframe
from typing import Dict, List, Tuple

from assertions import assertions

def exam5_06(self):
	"""Page 311:
	Objective: Develop the voltage transfer curves for the circuits shown
	in Figures 5.27(a) and 5.27(b).
	Assume npn transistor parameters of VBE(on) = 0.7V, β=120, VCE(sat) = 0.2V,
	and VA = inf, and pnp transistor parameters of VEB(on) = 0.7V, β=80,
	VEC(sat) = 0.2V, and VA = inf.
	ANS: (a) VIS = 1.9V (when Qn enters saturation)
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

	#  α   β   Ω   μ   λ   ξ   ω

	# ---- Answers -------------------
	ans_VIS_a:float = 1.9   #

	# ---- Givens --------------------
	VCC:float = 5
	RB_a:float = 150e+03
	RC_a:float = 5e+03
	VCEsat_a:float = 0.2
	Beta_a:float = 120

	Beta_b:float = 80

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------
	calc_VRC_a:float = VCC - VCEsat_a
	calc_VIS_a:float = VBE - ( RB_a / (Beta_a * RC_a) ) * ( VCEsat_a - VCC )
	calc_ICEsat_a:float = calc_VRC_a / RC_a
	calc_ICEsat_a = round(calc_ICEsat_a,5)
	calc_IBsat_a:float = calc_ICEsat_a / Beta_a
	calc_VIS_a:float = calc_IBsat_a * RB_a + VBE

	print( '\n---- (a) -------------------------------------------' )


	ans_string:str = f"""
Per the available biasing, Qn operates in cut-off, active, and saturation
regions.  Assuming VBE = 0.7V and given VCE(sat) = 0.2V, calculate the input
voltage (VI) range from 0 to +5V.

Let VIS = the input-voltage when Qn reaches saturation (VCE(sat) = 0.2V).

Cut-off: Qn is OFF until VI reaches 0.7V
       : VI range = 0 to 0.7V
Saturation: Qn is fully ON, IC is saturated (at maximum).
          : VI > VIS
Active: At what input voltage does Qn enter saturation?
      : VI range = 0.7 to VIS

Calculate VIS.

In saturation, VRC = VCC - VCE(sat)
                   = {VCC} - {VCEsat_a}
                   = {calc_VRC_a}

Calculate IRC = ICE(sat), then using Beta calculate IB.
At this current for IB, calculate VIS = IB*RB + VBE.

  ICE(sat) = VRC / RC
           = {calc_VRC_a} / {RC_a}
           = {calc_ICEsat_a}A = {round(calc_ICEsat_a*1000,5)}mA.

  IB(sat) = ICE(sat) / Beta
          = {calc_ICEsat_a} / {Beta_a}
          = {calc_IBsat_a}A.

Using IB(sat), calculate VIS per KVL for Qn BE-junction loop.

  IB(sat) * RB = VIS - VBE
  VIS = IB(sat) * RB + VBE
      = {calc_IBsat_a} * {RB_a} + {VBE}
      = {calc_VIS_a}V.

Therefore, Qn operates in active-region when 0.7 < VIS < {calc_VIS_a}V.
All I-V point/coordinates are available to plot the VO-VI transfer
function.
At VI = VBE = {VBE}V, VO = {VCC}V,
   VI = VIS = {calc_VIS_a}V, VO = VCE(sat) = {VCEsat_a}V.
"""
	print( ans_string )

	# Load the plot-points into dict for pass to plotting function.
	# The dict-key indicates the range for VI at crucial VI: 0, VBE, VIS, VCC.
	dict_xfer_func_pts:Dict[str,Tuple] = {  }
	dict_xfer_func_pts['VI_eq_0'] = (0,VCC)
	dict_xfer_func_pts['VI_eq_VBE'] = (VBE,VCC)
	dict_xfer_func_pts['VI_eq_VIS'] = (calc_VIS_a,VCEsat_a)
	dict_xfer_func_pts['VI_gt_VIS'] = (VCC,VCEsat_a)

	plot_voltage_xfer_function( self, pts=dict_xfer_func_pts )

	print( '\n---- (b) -------------------------------------------' )


	try:
		assertions.assert_within_percentage( calc_VIS_a, ans_VIS_a, assert_percentage )
		print( f"ASSERT VIS = {calc_VIS_a}V is within {assert_percentage}% of accepted answer: {ans_VIS_a}V." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )



def plot_voltage_xfer_function( self, pts:Dict[str,Tuple] ):
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator

	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: function: '{fcn_name}'" )

	# print( pts )

	x_axis:List = [ pts['VI_eq_0'][0], pts['VI_eq_VBE'][0], pts['VI_eq_VIS'][0], pts['VI_gt_VIS'][0] ]
	y_axis:List = [ pts['VI_eq_0'][1], pts['VI_eq_VBE'][1], pts['VI_eq_VIS'][1], pts['VI_gt_VIS'][1] ]

	plt.figure( figsize=self.param_figure_figsize )
	plt.plot( x_axis, y_axis, color='blue' )
	# Set titles and labels
	plt.title('Exam 5.6(a) Qn VO-VI transfer function')
	plt.xlabel('VI(V)')
	# xlim_start:float = x_axis[0] - 1
	# xlim_stop:float = dc_ll['VC0'] + 2
	# plt.xlim( xlim_start, xlim_stop )
	# Set the x-axis to have 10 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=10) )

	plt.ylabel('VO(V)')

	# Add vertical guide lines @ VBE and VIS
	plt.axvline( x=pts['VI_eq_VBE'][0], color='r', linestyle='--', linewidth=1.0 )
	# Add a vertical guide line at origin
	plt.axvline( x=pts['VI_eq_VIS'][0], color='r', linestyle='--', linewidth=1.0 )

	# Display the plot
	plt.tight_layout()
	plt.legend()
	plt.show()
	plt.close()
