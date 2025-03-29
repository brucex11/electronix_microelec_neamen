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
	ANS: (a) VIS = 1.9V (when Qn leaves active)
	ANS: (b) VIS = 2.8V (when Qp enters active)
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
	ans_VIS_a:float = 1.9   # V
	ans_VIS_b:float = 2.8   # V

	# ---- Givens --------------------
	VCC:float = 5
	RB_a:float = 150e+03
	RC_a:float = 5e+03
	VCEsat:float = 0.2
	Beta_a:float = 120

	VECsat:float = 0.2
	RB_b:float = 200e+03
	RC_b:float = 8e+03
	Beta_b:float = 80

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V
	VEB:float = 0.7   # V

	print( '\n---- (a) -------------------------------------------' )
	# ---- Calcs ---------------------
	calc_VRC_a:float = VCC - VCEsat
	calc_VIS_a:float = VBE - ( RB_a / (Beta_a * RC_a) ) * ( VCEsat - VCC )
	calc_ICEsat:float = calc_VRC_a / RC_a
	calc_ICEsat = round(calc_ICEsat,5)
	calc_IBsat_a:float = calc_ICEsat / Beta_a
	calc_VIS_a:float = calc_IBsat_a * RB_a + VBE


	ans_string:str = f"""
Per the available biasing, Qn operates in cut-off, active, and saturation
regions.  Assuming VBE = 0.7V and given VCE(sat) = 0.2V, calculate the input
voltage (VI) range from 0 to +5V.

Let VIS = the input-voltage when Qn reaches saturation (VCE(sat) = 0.2V).

Cut-off: Qn is OFF until VI reaches 0.7V
       : VI range = 0 to 0.7V
Saturation: Qn is fully ON, IC is saturated (at maximum).
          : VI > VIS
Active: At what input voltage does Qn leave cut-off and enter active?
      : VI range = 0.7 to VIS

Calculate VIS.

In saturation, VRC = VCC - VCE(sat)
                   = {VCC} - {VCEsat}
                   = {calc_VRC_a}

Calculate IRC = ICE(sat), then using Beta calculate IB.
At this current for IB, calculate VIS = IB*RB + VBE.

  ICE(sat) = VRC / RC
           = {calc_VRC_a} / {RC_a}
           = {calc_ICEsat}A = {round(calc_ICEsat*1000,5)}mA.

  IB(sat) = ICE(sat) / Beta
          = {calc_ICEsat} / {Beta_a}
          = {calc_IBsat_a}A.

Using IB(sat), calculate VIS per KVL for Qn BE-junction loop.

  IB(sat) * RB = VIS - VBE
  VIS = IB(sat) * RB + VBE
      = {calc_IBsat_a} * {RB_a} + {VBE}
      = {calc_VIS_a}V.

Therefore, Qn operates in active-region when 0.7 < VIS < {calc_VIS_a}V.
All I-V point/coordinates are available to plot the VO-VI transfer
function.
At VI = VBE = {VBE}V, VO = {VCC}V, (leave cut-off, enter active)
   VI = VIS = {calc_VIS_a}V, VO = VCE(sat) = {VCEsat}V (leave active, enter saturation).
"""
	print( ans_string )

	# Load the plot-points into dict for pass to plotting function.
	# The dict-key indicates the range for VI at crucial VI
	# from left to right: 0, VBE, VIS, VCC.
	dict_xfer_func_pts:Dict[str,Tuple] = {}
	dict_xfer_func_pts['VI_0'] = (0,VCC)
	dict_xfer_func_pts['VI_1'] = (VBE,VCC)
	dict_xfer_func_pts['VI_2'] = (calc_VIS_a,VCEsat)
	dict_xfer_func_pts['VI_3'] = (VCC,VCEsat)

	plot_voltage_xfer_function( self, pts=dict_xfer_func_pts, title_type='NPN' )

	try:
		assertions.assert_within_percentage( calc_VIS_a, ans_VIS_a, assert_percentage )
		print( f"ASSERT VIS = {calc_VIS_a}V is within {assert_percentage}% of accepted answer: {ans_VIS_a}V." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	print( '\n---- (b) -------------------------------------------' )
	# ---- Calcs ---------------------
	calc_VRC_b:float = VCC - VECsat
	calc_IECsat = calc_VRC_b / RC_b
	calc_IBsat_b:float = calc_IECsat / Beta_b
	calc_IBsat_b = round(calc_IBsat_b,9)
	calc_VIS_b:float = (VCC - VEB) - calc_IBsat_b * RB_b

	ans_string = f"""
Per the available biasing, Qp operates in cut-off, active, and saturation
regions.  Assuming VEB = 0.7V and given VEC(sat) = 0.2V, calculate the input
voltage (VI) range from 0 to +5V.

Let VIS = the input-voltage when Qp reaches saturation (VEC(sat) = 0.2V).

Cut-off: Qp is OFF until VI reaches VCC - {VEB}V
       : VI range = ({VCC} - {VEB}) to {VCC}V
Saturation: Qp is fully ON, IC is saturated (at maximum).
          : VI < VIS
Active: At what input voltage does Qp leave saturation and enter active?
      : VI range = VIS to (VCC - VEB).

Calculate VIS.

In saturation, VRC = VCC - VEC(sat)
                   = {VCC} - {VECsat}
                   = {calc_VRC_b}

Calculate IRC = IEC(sat), then using Beta calculate IB.
At this current for IB, calculate VIS = IB*RB + (VCC - VEC(sat)).

  IEC(sat) = VRC / RC
           = {calc_VRC_b} / {RC_b}
           = {calc_IECsat}A = {round(calc_IECsat*1000,5)}mA.

  IB(sat) = ICE(sat) / Beta
          = {calc_IECsat} / {Beta_b}
          = {calc_IBsat_b}A.

Using IB(sat), calculate VIS per KVL for Qp BE-junction loop.

  IB(sat) * RB = (VCC - VEB) - VIS
  VIS = (VCC - VEB) - IB(sat) * RB
      = ({VCC} - {VEB}) - {round(calc_IBsat_b,9)} * {RB_b}
      = {calc_VIS_b}V.

Therefore, Qp operates in active-region when {calc_VRC_b} > VIS > {calc_VIS_b}V.
All I-V point/coordinates are available to plot the VO-VI transfer
function.
At VI = {calc_VIS_b}V, VO = {calc_VRC_b}V, (leave saturation, enter active)
   VI = VIS = {VCC - VEB}V, VO = {VECsat}V  (leave active, enter cut-off).
"""
	print( ans_string )

	# Load the plot-points into dict for pass to plotting function.
	# The dict-key indicates the range for VI at crucial VI
	# from left to right: 0, VIS, Vcutoff, VCC.
	dict_xfer_func_pts.clear()
	dict_xfer_func_pts['VI_0'] = (0,VCC-VECsat)
	dict_xfer_func_pts['VI_1'] = (calc_VIS_b,VCC-VCEsat)
	dict_xfer_func_pts['VI_2'] = (VCC-VEB,0)
	dict_xfer_func_pts['VI_3'] = (VCC,0)

	plot_voltage_xfer_function( self, pts=dict_xfer_func_pts, title_type='PNP' )

	try:
		assertions.assert_within_percentage( calc_VIS_b, ans_VIS_b, assert_percentage )
		print( f"ASSERT VIS = {calc_VIS_b}V is within {assert_percentage}% of accepted answer: {ans_VIS_b}V." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	print( f"--- END {self.prob_str} ---" )


def plot_voltage_xfer_function( self, pts:Dict[str,Tuple], title_type:str ):
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator

	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: function: '{fcn_name}'" )

	# print( pts )

	# x_axis:List = [ pts['VI_eq_0'][0], pts['VI_eq_VBE'][0], pts['VI_eq_VIS'][0], pts['VI_gt_VIS'][0] ]
	# y_axis:List = [ pts['VI_eq_0'][1], pts['VI_eq_VBE'][1], pts['VI_eq_VIS'][1], pts['VI_gt_VIS'][1] ]
	x_axis:List = [ pts['VI_0'][0],
									pts['VI_1'][0],
									pts['VI_2'][0],
									pts['VI_3'][0]
								]
	y_axis:List = [ pts['VI_0'][1],
									pts['VI_1'][1],
									pts['VI_2'][1],
									pts['VI_3'][1]
								]
	# y_axis:List = [ pts['VI_eq_0'][1], pts['VI_eq_VBE'][1], pts['VI_eq_VIS'][1], pts['VI_gt_VIS'][1] ]

	plt.figure( figsize=self.param_figure_figsize )
	plt.plot( x_axis, y_axis, color='blue' )
	# Set titles and labels
	plt.title( f"Exam 5.6(a) {title_type} VO-VI transfer function" )
	plt.xlabel('VI(V)')
	# xlim_start:float = x_axis[0] - 1
	# xlim_stop:float = dc_ll['VC0'] + 2
	# plt.xlim( xlim_start, xlim_stop )
	# Set the x-axis to have 10 divisions
	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=10) )

	plt.ylabel('VO(V)')

	# Add vertical guide lines @ VBE and VIS
	plt.axvline( x=pts['VI_1'][0], color='r', linestyle='--', linewidth=1.0 )
	# Add a vertical guide line at origin
	plt.axvline( x=pts['VI_2'][0], color='r', linestyle='--', linewidth=1.0 )

	# Plot the DC sweep for VI.
	x_vin:List = [0,5]
	y_vin:List = [0,5]
	plt.plot( x_vin, y_vin, color='r' )

	# Display the plot
	plt.tight_layout()
	# plt.legend()
	plt.show()
	plt.close()
